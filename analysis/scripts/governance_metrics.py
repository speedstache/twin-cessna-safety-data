#!/usr/bin/env python3
"""
governance_metrics.py

Governance/quality metrics for Twin Cessna safety dataset (accidents_master.csv).

Purpose:
- Demonstrate data discipline, completeness, taxonomy usability, and gate readiness.
- NOT an analysis script (no trends, no risk rankings, no recommendations).

Outputs:
- Record counts and missingness for required fields (configurable)
- Unknown factor rate (based on contributing_factors)
- Contributing factor count distribution (0/1/2/3/>3)
- Basic distributions: phase_of_flight, weather_category, mission_profile, operation_type
- Optional JSON and CSV exports

Usage:
  python scripts/governance_metrics.py --csv data/structured/accidents_master.csv
  python scripts/governance_metrics.py --csv accidents_master.csv --out-json governance.json --out-dir governance_tables/

Notes:
- If your column names differ slightly, this script attempts to auto-detect common variants.
- Adjust REQUIRED_FIELDS if your validator uses a different set.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd


# ---- Configure required fields for "record completeness" checks ----
# Keep this aligned with your validator. If unsure, start strict and relax later.
REQUIRED_FIELDS = [
    "event_id",
    "model",
    "variant",
    "engine_type",
    "year",
    "country",
    "source",
    "report_number",
    "drive_path",
    "downloaded",
    "taxonomy_version",
    "phase_of_flight",
    "mission_profile",
    "weather_category",
    "maintenance_context",
    "total_time_band",
    "multi_time_band",
    "time_in_type_band",
    "recency_status",
    "event_type",
    "contributing_factors",
    "prevention_category",
    "prevention_summary",
]


def _pick_col(df: pd.DataFrame, candidates: List[str]) -> Optional[str]:
    cols_lower = {c.lower(): c for c in df.columns}
    for cand in candidates:
        if cand.lower() in cols_lower:
            return cols_lower[cand.lower()]
    return None


def _norm_str(val: Any) -> str:
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return ""
    return str(val).strip()


def _is_missing(val: Any) -> bool:
    s = _norm_str(val)
    return s == "" or s.lower() in {"na", "nan", "none", "null"}


def _parse_factor_list(val: Any) -> List[str]:
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return []
    s = str(val).strip()
    if not s:
        return []

    # Try JSON list
    if s.startswith("[") and s.endswith("]"):
        try:
            parsed = json.loads(s)
            if isinstance(parsed, list):
                return [str(x).strip().lower() for x in parsed if str(x).strip()]
        except Exception:
            pass

    # YAML-ish or newline list
    s = s.replace("\n- ", "|").replace("\n-", "|").replace("\n", "|")
    s = re.sub(r"^\s*-\s*", "", s)

    parts = re.split(r"[|;,]", s)
    factors = [p.strip().lower() for p in parts if p.strip()]
    if not factors and s:
        factors = [s.lower()]
    return factors


def _factor_count(val: Any) -> int:
    return len(_parse_factor_list(val))


def _unknown_factor_flag(val: Any) -> bool:
    factors = _parse_factor_list(val)
    if not factors:
        return False
    return any(f == "unknown" for f in factors)


def _value_counts(df: pd.DataFrame, col: Optional[str]) -> Dict[str, int]:
    if not col:
        return {}
    s = df[col].fillna("Unknown").astype(str).str.strip()
    s = s.replace({"": "Unknown"})
    vc = s.value_counts(dropna=False)
    return {str(k): int(v) for k, v in vc.items()}


def _missingness_table(df: pd.DataFrame, fields: List[str]) -> pd.DataFrame:
    rows = []
    for f in fields:
        col = _pick_col(df, [f])
        if not col:
            rows.append(
                {
                    "field": f,
                    "present_in_csv": False,
                    "missing_count": len(df),
                    "missing_rate": 1.0 if len(df) else 0.0,
                }
            )
            continue

        miss = df[col].apply(_is_missing)
        missing_count = int(miss.sum())
        missing_rate = round(missing_count / len(df), 4) if len(df) else 0.0
        rows.append(
            {
                "field": f,
                "present_in_csv": True,
                "missing_count": missing_count,
                "missing_rate": missing_rate,
            }
        )
    return pd.DataFrame(rows).sort_values(["missing_rate", "field"], ascending=[False, True])


def _record_completeness(df: pd.DataFrame, fields: List[str]) -> Tuple[int, float]:
    """Count records with no missing required fields (based on what's present)."""
    if len(df) == 0:
        return 0, 0.0

    # Only evaluate fields that exist in df
    existing_cols = []
    for f in fields:
        col = _pick_col(df, [f])
        if col:
            existing_cols.append(col)

    if not existing_cols:
        return 0, 0.0

    # Vectorized missing detection instead of applymap
    subset = df[existing_cols].astype(str).fillna("").apply(lambda col: col.str.strip().str.lower())
    missing_any = subset.isin(["", "na", "nan", "none", "null"]).any(axis=1)

    complete_count = int((~missing_any).sum())
    complete_rate = round(complete_count / len(df), 4)

    return complete_count, complete_rate


def main() -> int:
    ap = argparse.ArgumentParser(description="Governance / data-quality metrics for accidents_master.csv")
    ap.add_argument("--csv", required=True, help="Path to accidents_master.csv")
    ap.add_argument("--out-json", default=None, help="Optional path for JSON summary output")
    ap.add_argument("--out-dir", default=None, help="Optional directory for CSV outputs")
    ap.add_argument(
        "--required-fields",
        default=None,
        help="Optional path to a text file with required field names, one per line (overrides built-in list).",
    )
    args = ap.parse_args()

    csv_path = Path(args.csv).expanduser().resolve()
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    df = pd.read_csv(csv_path)

    # Load required fields override if provided
    required_fields = REQUIRED_FIELDS
    if args.required_fields:
        rf_path = Path(args.required_fields).expanduser().resolve()
        lines = [ln.strip() for ln in rf_path.read_text(encoding="utf-8").splitlines()]
        required_fields = [ln for ln in lines if ln and not ln.startswith("#")]

    # Column detection for distributions
    col_model = _pick_col(df, ["model", "aircraft_model"])
    col_op = _pick_col(df, ["operation_type", "operation", "op_type", "part"])
    col_phase = _pick_col(df, ["phase_of_flight", "phase"])
    col_weather = _pick_col(df, ["weather_category", "weather"])
    col_mission = _pick_col(df, ["mission_profile", "mission"])
    col_tax = _pick_col(df, ["taxonomy_version", "taxonomy"])
    col_factors = _pick_col(df, ["contributing_factors", "factors"])

    dataset_size_total = int(len(df))

    # Missingness + completeness
    miss_tbl = _missingness_table(df, required_fields)
    complete_count, complete_rate = _record_completeness(df, required_fields)

    # Taxonomy versions
    taxonomy_versions = _value_counts(df, col_tax) if col_tax else {}

    # Factors metrics
    unknown_factor_rate: Any = "Unknown (no contributing_factors column found)"
    unknown_count = None
    factors_count_dist: Dict[str, int] = {}
    over3_count = None

    if col_factors:
        factor_counts = df[col_factors].apply(_factor_count)
        unknown_flags = df[col_factors].apply(_unknown_factor_flag)

        unknown_count = int(unknown_flags.sum())

        has_any = factor_counts > 0
        denom = int(has_any.sum())
        unknown_factor_rate = round(unknown_count / denom, 4) if denom else "Unknown (no parsable factors found)"

        # Distribution buckets
        buckets = {
            "0": int((factor_counts == 0).sum()),
            "1": int((factor_counts == 1).sum()),
            "2": int((factor_counts == 2).sum()),
            "3": int((factor_counts == 3).sum()),
            ">3": int((factor_counts > 3).sum()),
        }
        factors_count_dist = buckets
        over3_count = buckets[">3"]

    # Distributions (descriptive)
    per_model = _value_counts(df, col_model)
    by_operation = _value_counts(df, col_op)
    by_phase = _value_counts(df, col_phase)
    by_weather = _value_counts(df, col_weather)
    by_mission = _value_counts(df, col_mission)

    summary: Dict[str, Any] = {
        "source_file": str(csv_path),
        "dataset_size_total": dataset_size_total,
        "record_completeness": {
            "complete_count": complete_count,
            "complete_rate": complete_rate,
            "required_fields_checked": required_fields,
            "note": "Completeness computed only across required fields present in the CSV.",
        },
        "missingness_by_field": miss_tbl.to_dict(orient="records"),
        "taxonomy_versions": taxonomy_versions if taxonomy_versions else "Unknown (no taxonomy_version column found)",
        "contributing_factors_metrics": {
            "unknown_factor_rate": unknown_factor_rate,
            "unknown_factor_records": unknown_count,
            "factor_count_distribution": factors_count_dist if factors_count_dist else "Unknown (no contributing_factors column found)",
            "over_3_factor_records": over3_count,
            "note": "Validator should enforce max 3 factors; any >3 indicates a governance breach.",
        },
        "descriptive_distributions": {
            "dataset_size_per_model": per_model,
            "dataset_size_by_operation_type": by_operation,
            "phase_of_flight_distribution": by_phase,
            "weather_category_distribution": by_weather,
            "mission_profile_distribution": by_mission,
        },
        "columns_present": list(df.columns),
    }

    # ---- Print report (stdout) ----
    print("# Governance Metrics (Descriptive — Not Analytical)")
    print(f"_Source_: `{csv_path}`")
    print()
    print("## Core")
    print(f"- **dataset_size_total**: {dataset_size_total}")
    print(f"- **complete_records**: {complete_count} ({complete_rate})")
    if taxonomy_versions:
        print(f"- **taxonomy_versions**: {taxonomy_versions}")
    else:
        print("- **taxonomy_versions**: Unknown (no taxonomy_version column found)")

    print()
    print("## Contributing Factors Governance")
    print(f"- **unknown_factor_rate**: {unknown_factor_rate}")
    if unknown_count is not None:
        print(f"- **unknown_factor_records**: {unknown_count}")
    if factors_count_dist:
        print(f"- **factor_count_distribution**: {factors_count_dist}")
        if over3_count and over3_count > 0:
            print("  - **WARNING**: Records with >3 factors present (validator breach).")

    print()
    print("## Missingness by Required Field (Top 10 by missing_rate)")
    top10 = miss_tbl.head(10)
    for _, r in top10.iterrows():
        print(
            f"- **{r['field']}** | present: {bool(r['present_in_csv'])} | missing_count: {int(r['missing_count'])} | missing_rate: {r['missing_rate']}"
        )

    # Helpful distributions for demo
    def print_dist(title: str, dist: Dict[str, int]) -> None:
        if not dist:
            return
        print()
        print(f"## {title}")
        for k, v in dist.items():
            print(f"- **{k}**: {v}")

    print_dist("Dataset Size per Model", per_model)
    print_dist("Dataset Size by Operation Type", by_operation)
    print_dist("Phase of Flight Distribution", by_phase)
    print_dist("Weather Category Distribution", by_weather)
    print_dist("Mission Profile Distribution", by_mission)

    # ---- Optional exports ----
    if args.out_json:
        out_json = Path(args.out_json).expanduser().resolve()
        out_json.parent.mkdir(parents=True, exist_ok=True)
        out_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        print()
        print(f"Wrote JSON summary: {out_json}")

    if args.out_dir:
        out_dir = Path(args.out_dir).expanduser().resolve()
        out_dir.mkdir(parents=True, exist_ok=True)

        # Missingness table
        miss_tbl.to_csv(out_dir / "missingness_by_required_field.csv", index=False)

        # Distributions as CSV
        def write_dist(name: str, dist: Dict[str, int]) -> None:
            if not dist:
                return
            pd.DataFrame({"value": list(dist.keys()), "count": list(dist.values())}).to_csv(out_dir / f"{name}.csv", index=False)

        write_dist("dataset_size_per_model", per_model)
        write_dist("dataset_size_by_operation_type", by_operation)
        write_dist("phase_of_flight_distribution", by_phase)
        write_dist("weather_category_distribution", by_weather)
        write_dist("mission_profile_distribution", by_mission)

        # Factors distribution
        if factors_count_dist:
            pd.DataFrame({"bucket": list(factors_count_dist.keys()), "count": list(factors_count_dist.values())}).to_csv(
                out_dir / "contributing_factor_count_distribution.csv", index=False
            )

        print()
        print(f"Wrote CSV tables to: {out_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
