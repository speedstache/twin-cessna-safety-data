#!/usr/bin/env python3
"""
unknown_monitor.py

Monitors usage of 'unknown' in contributing factors and flags governance thresholds.

Purpose (governance tooling, NOT analysis):
- Track unknown_factor_rate overall and by key context fields
- Warn when unknown_factor_rate exceeds the project threshold (default 0.40)
- Provide a repeatable, auditable output for checkpoint reporting

Supports contributing factors stored as:
A) Single column list/string (e.g. contributing_factors_raw, contributing_factors, factors)
B) Multiple slot columns (factor_1/2/3 etc.)
C) One-hot boolean columns (cf_*), e.g. cf_task_saturation, cf_unknown

Definition (governance):
- unknown_factor_rate = (# records whose factors include 'unknown')
                       / (# records with ANY factor present)

For one-hot:
- "any factor present" means any cf_* column is truthy OR contributing_factors_raw parses to non-empty (if provided)

Usage:
  python scripts/unknown_monitor.py --csv data/master/accidents_master.csv
  python scripts/unknown_monitor.py --csv data/master/accidents_master.csv --threshold 0.4
  python scripts/unknown_monitor.py --csv data/master/accidents_master.csv --mode onehot
  python scripts/unknown_monitor.py --csv data/master/accidents_master.csv --factors-col contributing_factors_raw
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd


DEFAULT_THRESHOLD = 0.40


# ----------------- Helpers -----------------

def _pick_col_exact_case_insensitive(df: pd.DataFrame, name: str) -> Optional[str]:
    cols_lower = {c.lower(): c for c in df.columns}
    return cols_lower.get(name.lower())


def _truthy(val: Any) -> bool:
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return False
    if isinstance(val, (bool, int)):
        return bool(val)
    s = str(val).strip().lower()
    if s in {"", "0", "false", "no", "n", "none", "null", "nan", "na"}:
        return False
    return True


def _parse_factor_list(val: Any) -> List[str]:
    """Parse a single-cell factor list/string into normalized tokens."""
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return []
    s = str(val).strip()
    if not s:
        return []

    # JSON list support
    if s.startswith("[") and s.endswith("]"):
        try:
            parsed = json.loads(s)
            if isinstance(parsed, list):
                return [str(x).strip().lower() for x in parsed if str(x).strip()]
        except Exception:
            pass

    # YAML-ish / newline list support
    s = s.replace("\n- ", "|").replace("\n-", "|").replace("\n", "|")
    s = re.sub(r"^\s*-\s*", "", s)

    parts = re.split(r"[|;,]", s)
    factors = [p.strip().lower() for p in parts if p.strip()]
    if not factors and s:
        factors = [s.lower()]
    return factors


def _unknown_rate_from_factor_lists(factor_lists: pd.Series) -> Dict[str, Any]:
    """factor_lists: series of List[str] per row"""
    has_any = factor_lists.apply(lambda lst: len(lst) > 0)
    denom = int(has_any.sum())
    if denom == 0:
        return {
            "denominator_records_with_factors": 0,
            "unknown_records": 0,
            "unknown_factor_rate": "Unknown (no parsable factors found)",
        }
    unknown = factor_lists.apply(lambda lst: any(x == "unknown" for x in lst))
    unknown_count = int(unknown.sum())
    return {
        "denominator_records_with_factors": denom,
        "unknown_records": unknown_count,
        "unknown_factor_rate": round(unknown_count / denom, 4),
    }


def _group_unknown_rates(df: pd.DataFrame, group_col: str, compute_fn) -> pd.DataFrame:
    """
    compute_fn(sub_df) -> metrics dict containing:
      denominator_records_with_factors, unknown_records, unknown_factor_rate
    """
    g = df.groupby(df[group_col].fillna("Unknown").astype(str).str.strip().replace({"": "Unknown"}))
    rows = []
    for key, sub in g:
        metrics = compute_fn(sub)
        rows.append({"group": group_col, "value": key, "records_total": int(len(sub)), **metrics})
    out = pd.DataFrame(rows)

    # Sort by numeric unknown_factor_rate desc
    if "unknown_factor_rate" in out.columns:
        numeric_mask = out["unknown_factor_rate"].apply(lambda x: isinstance(x, (int, float)))
        out_num = out[numeric_mask].copy()
        out_non = out[~numeric_mask].copy()
        out_num = out_num.sort_values(
            ["unknown_factor_rate", "unknown_records", "records_total"],
            ascending=[False, False, False],
        )
        out_non = out_non.sort_values(["unknown_records", "records_total"], ascending=[False, False])
        out = pd.concat([out_num, out_non], ignore_index=True)

    return out


# ----------------- Factor storage detection -----------------

def _detect_mode(
    df: pd.DataFrame,
    mode_override: Optional[str],
    factors_col_override: Optional[str],
    factor_cols_override: Optional[List[str]],
) -> Dict[str, Any]:
    """
    Returns dict:
      mode: 'onehot' | 'single' | 'slots'
      onehot_cols: List[str]
      single_col: Optional[str]
      slot_cols: List[str]
    """
    if mode_override:
        m = mode_override.lower()
        if m not in {"onehot", "single", "slots"}:
            raise ValueError("--mode must be one of: onehot, single, slots")
        # Resolve based on override + overrides
        if m == "single":
            if not factors_col_override:
                raise ValueError("--mode single requires --factors-col <column_name>")
            col = _pick_col_exact_case_insensitive(df, factors_col_override)
            if not col:
                raise ValueError(f"--factors-col '{factors_col_override}' not found.")
            return {"mode": "single", "onehot_cols": [], "single_col": col, "slot_cols": []}
        if m == "slots":
            if not factor_cols_override:
                raise ValueError("--mode slots requires --factor-cols col1,col2,col3")
            resolved = []
            for name in factor_cols_override:
                col = _pick_col_exact_case_insensitive(df, name)
                if not col:
                    raise ValueError(f"--factor-cols column '{name}' not found.")
                resolved.append(col)
            return {"mode": "slots", "onehot_cols": [], "single_col": None, "slot_cols": resolved}
        # onehot
        onehot_cols = [c for c in df.columns if str(c).lower().startswith("cf_")]
        if not onehot_cols:
            raise ValueError("--mode onehot selected but no cf_* columns found.")
        return {"mode": "onehot", "onehot_cols": sorted(onehot_cols), "single_col": None, "slot_cols": []}

    # If user explicitly gave a single column, use it
    if factors_col_override:
        col = _pick_col_exact_case_insensitive(df, factors_col_override)
        if not col:
            raise ValueError(f"--factors-col '{factors_col_override}' not found.")
        return {"mode": "single", "onehot_cols": [], "single_col": col, "slot_cols": []}

    # If user explicitly gave slot columns, use them
    if factor_cols_override:
        resolved = []
        for name in factor_cols_override:
            col = _pick_col_exact_case_insensitive(df, name)
            if not col:
                raise ValueError(f"--factor-cols column '{name}' not found.")
            resolved.append(col)
        return {"mode": "slots", "onehot_cols": [], "single_col": None, "slot_cols": resolved}

    # Auto-detect onehot first (your schema)
    onehot_cols = [c for c in df.columns if str(c).lower().startswith("cf_")]
    if onehot_cols:
        return {"mode": "onehot", "onehot_cols": sorted(onehot_cols), "single_col": None, "slot_cols": []}

    # Auto-detect single-column names
    for candidate in ["contributing_factors", "factors", "contributing_factors_raw", "contributing_factor_codes", "factor_codes"]:
        col = _pick_col_exact_case_insensitive(df, candidate)
        if col:
            return {"mode": "single", "onehot_cols": [], "single_col": col, "slot_cols": []}

    # Auto-detect slots
    slot_pattern = re.compile(
        r"^(contributing_?factors?|contributing_?factor|factors?|factor|cf)(?:[ _\-.]?\[?\d+\]?)$",
        re.IGNORECASE,
    )
    slot_cols = [c for c in df.columns if slot_pattern.match(str(c).strip())]
    if slot_cols:
        # sort by embedded number
        def sort_key(name: str):
            m = re.search(r"(\d+)", name)
            return (int(m.group(1)) if m else 9999, name.lower())
        slot_cols = sorted(slot_cols, key=sort_key)
        return {"mode": "slots", "onehot_cols": [], "single_col": None, "slot_cols": slot_cols}

    # Fail: show candidates
    candidates = [c for c in df.columns if re.search(r"factor|contribut|cf", str(c), re.IGNORECASE)]
    candidates = sorted(candidates, key=lambda x: str(x).lower())
    raise ValueError(
        "No contributing factors found.\n"
        "Expected either cf_* onehot columns, a single factors column, or slot columns.\n"
        + ("Factor-ish columns found:\n  - " + "\n  - ".join(map(str, candidates)) if candidates else "")
    )


# ----------------- Computation per mode -----------------

def _compute_metrics_onehot(df: pd.DataFrame, onehot_cols: List[str]) -> Dict[str, Any]:
    """
    Denominator: records where ANY cf_* is truthy
    Unknown: records where cf_unknown is truthy (or cf_unknown column missing -> 0 unknown, but still compute)
    """
    if not onehot_cols:
        return {
            "denominator_records_with_factors": 0,
            "unknown_records": 0,
            "unknown_factor_rate": "Unknown (no cf_* columns found)",
        }

    # Any factor present
    subset = df[onehot_cols].fillna("").astype(str).apply(lambda c: c.str.strip().str.lower())
    truthy = ~subset.isin(["", "0", "false", "no", "n", "none", "null", "nan", "na"])
    any_factor = truthy.any(axis=1)
    denom = int(any_factor.sum())
    if denom == 0:
        return {
            "denominator_records_with_factors": 0,
            "unknown_records": 0,
            "unknown_factor_rate": "Unknown (no truthy cf_* values found)",
        }

    # Unknown flag
    cf_unknown_col = None
    for c in onehot_cols:
        if str(c).lower() == "cf_unknown":
            cf_unknown_col = c
            break

    if cf_unknown_col:
        unknown_flags = df[cf_unknown_col].apply(_truthy)
        unknown_count = int((unknown_flags & any_factor).sum())
    else:
        unknown_count = 0

    return {
        "denominator_records_with_factors": denom,
        "unknown_records": unknown_count,
        "unknown_factor_rate": round(unknown_count / denom, 4),
    }


def _compute_metrics_single(df: pd.DataFrame, single_col: str) -> Dict[str, Any]:
    lists = df[single_col].apply(_parse_factor_list)
    return _unknown_rate_from_factor_lists(lists)


def _compute_metrics_slots(df: pd.DataFrame, slot_cols: List[str]) -> Dict[str, Any]:
    merged = df[slot_cols].fillna("").astype(str).agg("|".join, axis=1)
    lists = merged.apply(_parse_factor_list)
    return _unknown_rate_from_factor_lists(lists)


# ----------------- Main -----------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Monitor and report 'unknown' usage in contributing factors.")
    ap.add_argument("--csv", required=True, help="Path to accidents_master.csv")
    ap.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD, help="Unknown factor rate threshold (default 0.40)")
    ap.add_argument("--out-json", default=None, help="Optional JSON output path")
    ap.add_argument("--out-dir", default=None, help="Optional directory to write CSV outputs")
    ap.add_argument("--top", type=int, default=10, help="Top N rows to print for each grouping (default 10)")
    ap.add_argument("--mode", default=None, help="Override: onehot | single | slots")
    ap.add_argument("--factors-col", default=None, help="Override: single column name containing factors")
    ap.add_argument("--factor-cols", default=None, help="Override: comma-separated factor slot columns (e.g. cf1,cf2,cf3)")
    args = ap.parse_args()

    csv_path = Path(args.csv).expanduser().resolve()
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    df = pd.read_csv(csv_path)

    factor_cols_override = None
    if args.factor_cols:
        factor_cols_override = [c.strip() for c in args.factor_cols.split(",") if c.strip()]

    storage = _detect_mode(
        df,
        mode_override=args.mode,
        factors_col_override=args.factors_col,
        factor_cols_override=factor_cols_override,
    )

    # Grouping columns (only include if present)
    def pick_group(cands: List[str]) -> Optional[str]:
        for c in cands:
            col = _pick_col_exact_case_insensitive(df, c)
            if col:
                return col
        return None

    group_candidates = {
        "model": pick_group(["model", "aircraft_model"]),
        "phase_of_flight": pick_group(["phase_of_flight", "phase"]),
        "operation_type": pick_group(["operation_type", "operation", "op_type", "part"]),
        "source": pick_group(["source", "data_source"]),
    }

    # Metrics compute function
    if storage["mode"] == "onehot":
        compute_fn = lambda sub: _compute_metrics_onehot(sub, storage["onehot_cols"])
        overall = compute_fn(df)
    elif storage["mode"] == "single":
        compute_fn = lambda sub: _compute_metrics_single(sub, storage["single_col"])
        overall = compute_fn(df)
    else:
        compute_fn = lambda sub: _compute_metrics_slots(sub, storage["slot_cols"])
        overall = compute_fn(df)

    pause_required = isinstance(overall["unknown_factor_rate"], (int, float)) and overall["unknown_factor_rate"] > args.threshold

    # Group tables
    group_tables: Dict[str, pd.DataFrame] = {}
    for name, col in group_candidates.items():
        if col:
            group_tables[name] = _group_unknown_rates(df, col, compute_fn)

    # ---- Print report ----
    print("# Unknown Monitor (Governance — Not Analytical)")
    print(f"_Source_: `{csv_path}`")
    print()
    print("## Contributing Factors Storage")
    print(f"- **mode**: {storage['mode']}")
    if storage["mode"] == "onehot":
        print(f"- **cf_columns_count**: {len(storage['onehot_cols'])}")
        print(f"- **cf_unknown_present**: {'cf_unknown' in [str(c).lower() for c in storage['onehot_cols']]}")
    elif storage["mode"] == "single":
        print(f"- **column**: {storage['single_col']}")
    else:
        print(f"- **columns**: {storage['slot_cols']}")

    print()
    print("## Overall")
    print(f"- **records_total**: {int(len(df))}")
    print(f"- **records_with_any_factor (denominator)**: {overall['denominator_records_with_factors']}")
    print(f"- **unknown_records**: {overall['unknown_records']}")
    print(f"- **unknown_factor_rate**: {overall['unknown_factor_rate']}")
    print(f"- **threshold**: {args.threshold}")
    print(f"- **pause_required**: {pause_required}")

    if pause_required:
        print()
        print("### WARNING")
        print("unknown_factor_rate exceeds threshold. Per project rules, pause pattern work and reassess taxonomy clarity / coding guidance.")

    for name, tbl in group_tables.items():
        print()
        print(f"## Unknown by {name} (top {args.top})")
        if tbl.empty:
            print("- (no data)")
            continue
        show = tbl.head(args.top)
        for _, r in show.iterrows():
            print(
                f"- **{r['value']}** | total: {int(r['records_total'])} | denom: {int(r['denominator_records_with_factors'])} | unknown: {int(r['unknown_records'])} | rate: {r['unknown_factor_rate']}"
            )

    out_obj: Dict[str, Any] = {
        "source_file": str(csv_path),
        "threshold": args.threshold,
        "pause_required": pause_required,
        "overall": overall,
        "factor_storage": storage,
        "groupings_included": {k: bool(v) for k, v in group_candidates.items()},
    }

    if args.out_json:
        out_path = Path(args.out_json).expanduser().resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_obj["group_tables"] = {k: v.to_dict(orient="records") for k, v in group_tables.items()}
        out_path.write_text(json.dumps(out_obj, indent=2), encoding="utf-8")
        print(f"\nWrote JSON output: {out_path}")

    if args.out_dir:
        out_dir = Path(args.out_dir).expanduser().resolve()
        out_dir.mkdir(parents=True, exist_ok=True)

        pd.DataFrame(
            [
                {
                    "records_total": int(len(df)),
                    **overall,
                    "threshold": args.threshold,
                    "pause_required": pause_required,
                    "factor_storage_mode": storage["mode"],
                    "single_col": storage.get("single_col"),
                    "slot_cols": "|".join(storage.get("slot_cols", [])),
                    "onehot_cols_count": len(storage.get("onehot_cols", [])),
                }
            ]
        ).to_csv(out_dir / "unknown_overall.csv", index=False)

        for name, tbl in group_tables.items():
            tbl.to_csv(out_dir / f"unknown_by_{name}.csv", index=False)

        print(f"Wrote CSV tables to: {out_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
