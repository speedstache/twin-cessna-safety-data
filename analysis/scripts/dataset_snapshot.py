#!/usr/bin/env python3
"""
dataset_snapshot.py

Generate a *descriptive* snapshot of the current accidents_master.csv dataset.
This is intended for capability demonstration and governance tracking — not analysis.

Outputs (to stdout):
- taxonomy_version (if present)
- dataset_size_total
- dataset_size_per_model
- dataset_size_by_operation_type (91 vs 135, if present)
- dataset_size_by_year (if present)
- event_type distribution (if present)
- unknown_factor_rate (based on contributing_factors field)

Optionally writes:
- JSON summary (--out-json)
- CSV tables (--out-dir)

Usage:
  python dataset_snapshot.py --csv data/structured/accidents_master.csv
  python dataset_snapshot.py --csv accidents_master.csv --out-json snapshot.json --out-dir snapshot_tables/
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd


def _pick_col(df: pd.DataFrame, candidates: List[str]) -> Optional[str]:
    """Return first matching column name (case-insensitive) from candidates."""
    cols_lower = {c.lower(): c for c in df.columns}
    for cand in candidates:
        if cand.lower() in cols_lower:
            return cols_lower[cand.lower()]
    return None


def _parse_factor_list(val: Any) -> List[str]:
    """
    Parse contributing_factors cell into a list of normalized tokens.
    Supports:
      - JSON-like lists: '["a","b"]'
      - YAML-ish: '- a; - b' (rare in CSV)
      - Delimited: 'a|b', 'a;b', 'a,b'
      - Single strings
    """
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return []
    s = str(val).strip()
    if not s:
        return []

    # Try JSON list
    if (s.startswith("[") and s.endswith("]")) or (s.startswith('["') and s.endswith('"]')):
        try:
            parsed = json.loads(s)
            if isinstance(parsed, list):
                return [str(x).strip().lower() for x in parsed if str(x).strip()]
        except Exception:
            pass

    # Remove common YAML list markers
    s = re.sub(r"^\s*-\s*", "", s)
    s = s.replace("\n- ", "|").replace("\n-", "|").replace("\n", "|")

    # Split on common delimiters
    parts = re.split(r"[|;,]", s)
    factors = [p.strip().lower() for p in parts if p.strip()]

    # If still empty, treat as single
    if not factors and s:
        factors = [s.lower()]

    return factors


def _unknown_factor_flag(val: Any) -> bool:
    factors = _parse_factor_list(val)
    if not factors:
        # If missing, treat as unknown-ish for rate purposes? No — keep missing separate.
        return False
    return any(f == "unknown" for f in factors)


def _safe_value_counts(df: pd.DataFrame, col: Optional[str]) -> Dict[str, int]:
    if not col:
        return {}
    s = df[col].fillna("Unknown").astype(str).str.strip()
    s = s.replace({"": "Unknown"})
    vc = s.value_counts(dropna=False)
    return {str(k): int(v) for k, v in vc.items()}


def _to_markdown_kv(title: str, kv: List[Tuple[str, Any]]) -> str:
    lines = [f"## {title}"]
    for k, v in kv:
        lines.append(f"- **{k}**: {v}")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate a descriptive dataset snapshot for accidents_master.csv")
    ap.add_argument("--csv", required=True, help="Path to accidents_master.csv")
    ap.add_argument("--out-json", default=None, help="Optional path to write JSON summary")
    ap.add_argument("--out-dir", default=None, help="Optional directory to write CSV summary tables")
    args = ap.parse_args()

    csv_path = Path(args.csv).expanduser().resolve()
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    df = pd.read_csv(csv_path)

    # Column picks (robust to minor naming differences)
    col_model = _pick_col(df, ["model", "aircraft_model"])
    col_variant = _pick_col(df, ["variant"])
    col_year = _pick_col(df, ["year", "event_year", "occurrence_year"])
    col_op = _pick_col(df, ["operation_type", "operation", "op_type", "part"])
    col_event_type = _pick_col(df, ["event_type", "occurrence_type"])
    col_tax = _pick_col(df, ["taxonomy_version", "taxonomy"])
    col_factors = _pick_col(df, ["contributing_factors", "factors"])

    dataset_size_total = int(len(df))

    taxonomy_versions = _safe_value_counts(df, col_tax) if col_tax else {}
    # If multiple taxonomy versions exist, show distribution; if one, show value.
    taxonomy_version_display: Any
    if not taxonomy_versions:
        taxonomy_version_display = "Unknown (no taxonomy_version column found)"
    elif len(taxonomy_versions) == 1:
        taxonomy_version_display = next(iter(taxonomy_versions.keys()))
    else:
        taxonomy_version_display = taxonomy_versions

    # Unknown factor rate
    unknown_factor_rate: Any = "Unknown (no contributing_factors column found)"
    unknown_count = None
    if col_factors:
        flags = df[col_factors].apply(_unknown_factor_flag)
        unknown_count = int(flags.sum())
        # Rate is on records where factors are present (so missing doesn't inflate unknown)
        has_any = df[col_factors].apply(lambda v: len(_parse_factor_list(v)) > 0)
        denom = int(has_any.sum())
        if denom == 0:
            unknown_factor_rate = "Unknown (no parsable factors found)"
        else:
            unknown_factor_rate = round(unknown_count / denom, 4)

    # Aggregations
    per_model = _safe_value_counts(df, col_model)
    by_operation = _safe_value_counts(df, col_op)
    by_year = _safe_value_counts(df, col_year)
    by_event_type = _safe_value_counts(df, col_event_type)

    # Build summary dict
    summary: Dict[str, Any] = {
        "taxonomy_version": taxonomy_version_display,
        "dataset_size_total": dataset_size_total,
        "dataset_size_per_model": per_model,
        "dataset_size_by_operation_type": by_operation,
        "dataset_size_by_year": by_year,
        "event_type_distribution": by_event_type,
        "unknown_factor_rate": unknown_factor_rate,
        "columns_present": list(df.columns),
        "source_file": str(csv_path),
    }

    # Print human-readable snapshot
    print("# Dataset Snapshot (Descriptive — Not Analytical)")
    print(f"_Source_: `{csv_path}`")
    print()
    print(
        _to_markdown_kv(
            "Core",
            [
                ("taxonomy_version", taxonomy_version_display),
                ("dataset_size_total", dataset_size_total),
                ("unknown_factor_rate", unknown_factor_rate),
            ],
        )
    )
    print()
    print("## Dataset Size per Model")
    if per_model:
        for k, v in per_model.items():
            print(f"- **{k}**: {v}")
    else:
        print("- Unknown (no model column found)")

    if by_operation:
        print()
        print("## Dataset Size by Operation Type")
        for k, v in by_operation.items():
            print(f"- **{k}**: {v}")

    if by_year:
        print()
        print("## Dataset Size by Year")
        for k, v in by_year.items():
            print(f"- **{k}**: {v}")

    if by_event_type:
        print()
        print("## Event Type Distribution")
        for k, v in by_event_type.items():
            print(f"- **{k}**: {v}")

    # Optional outputs
    if args.out_json:
        out_json = Path(args.out_json).expanduser().resolve()
        out_json.parent.mkdir(parents=True, exist_ok=True)
        with out_json.open("w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)
        print()
        print(f"Wrote JSON summary: {out_json}")

    if args.out_dir:
        out_dir = Path(args.out_dir).expanduser().resolve()
        out_dir.mkdir(parents=True, exist_ok=True)

        # Write tables as 2-column CSVs
        def write_table(name: str, data: Dict[str, int]) -> None:
            if not data:
                return
            tdf = pd.DataFrame({"value": list(data.keys()), "count": list(data.values())})
            tdf.to_csv(out_dir / f"{name}.csv", index=False)

        write_table("dataset_size_per_model", per_model)
        write_table("dataset_size_by_operation_type", by_operation)
        write_table("dataset_size_by_year", by_year)
        write_table("event_type_distribution", by_event_type)

        # Factor unknown count (if computable)
        if unknown_count is not None:
            pd.DataFrame(
                {
                    "metric": ["unknown_factor_records"],
                    "count": [unknown_count],
                }
            ).to_csv(out_dir / "unknown_factor_records.csv", index=False)

        print()
        print(f"Wrote CSV tables to: {out_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
