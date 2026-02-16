#!/usr/bin/env python3
"""
completeness_monitor.py

Governance tool: Audits data completeness across the master dataset.

Tracks per-field:
- column_present
- blank_or_null_count
- explicit_unknown_count
- known_rate
- filled_rate

Separates:
- schema drift (missing columns)
- extraction gaps (blank/null)
- disciplined uncertainty ("Unknown")

Also retains:
- contributing_factor unknown_rate (taxonomy clarity gate)

Usage:
  python scripts/completeness_monitor.py --csv data/master/accidents_master.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, Any, Optional

import pandas as pd


BLANK_TOKENS = {"", "0", "false", "no", "none", "null", "nan", "na"}
UNKNOWN_TOKEN = "unknown"

REQUIRED_FIELDS = [
    # Identification
    "event_id",
    "model",
    "year",
    "operation_type",
    "source",
    "report_number",
    "drive_path",
    "downloaded",
    "taxonomy_version",

    # Context
    "phase_of_flight",
    "mission_profile",
    "weather_category",
    "density_altitude_category",
    "maintenance_context",

    # Pilot bands
    "total_time_band",
    "multi_time_band",
    "time_in_type_band",
    "recency_status",

    # Classification
    "event_type",
    "fatal",
    "serious_injury",
    "aircraft_destroyed",

    # Factors
    "contributing_factors"
]


def normalize_series(series: pd.Series) -> pd.Series:
    return series.fillna("").astype(str).str.strip().str.lower()


def compute_field_metrics(df: pd.DataFrame, field: str) -> Dict[str, Any]:
    if field not in df.columns:
        return {
            "column_present": False,
            "blank_or_null_count": None,
            "explicit_unknown_count": None,
            "known_rate": None,
            "filled_rate": None,
        }

    series = normalize_series(df[field])
    total = len(series)

    blank_mask = series.isin(BLANK_TOKENS)
    unknown_mask = series == UNKNOWN_TOKEN

    blank_count = int(blank_mask.sum())
    unknown_count = int(unknown_mask.sum())

    known_rate = round((total - unknown_count) / total, 4) if total else None
    filled_rate = round((total - blank_count - unknown_count) / total, 4) if total else None

    return {
        "column_present": True,
        "blank_or_null_count": blank_count,
        "explicit_unknown_count": unknown_count,
        "known_rate": known_rate,
        "filled_rate": filled_rate,
    }


def compute_factor_unknown_rate(df: pd.DataFrame) -> Dict[str, Any]:
    if "contributing_factors" not in df.columns:
        return {"unknown_factor_rate": None}

    series = normalize_series(df["contributing_factors"])
    total = len(series)

    unknown_count = int(series.str.contains(r"\bunknown\b").sum())
    denom = total

    return {
        "records_total": total,
        "unknown_records": unknown_count,
        "unknown_factor_rate": round(unknown_count / denom, 4) if denom else None
    }


def group_completeness(df: pd.DataFrame, group_field: str) -> Optional[pd.DataFrame]:
    if group_field not in df.columns:
        return None

    grouped = []
    for value, sub in df.groupby(df[group_field].fillna("Unknown")):
        metrics = compute_field_metrics(sub, "density_altitude_category")
        grouped.append({
            "group_value": value,
            "records_total": len(sub),
            **metrics
        })

    return pd.DataFrame(grouped)


def main() -> int:
    ap = argparse.ArgumentParser(description="Audit data completeness.")
    ap.add_argument("--csv", required=True)
    args = ap.parse_args()

    csv_path = Path(args.csv).expanduser().resolve()
    df = pd.read_csv(csv_path)

    print("# Data Completeness Monitor")
    print(f"Source: {csv_path}")
    print()

    print("## Overall Field Completeness")
    rows = []

    for field in REQUIRED_FIELDS:
        metrics = compute_field_metrics(df, field)
        rows.append({"field": field, **metrics})

    completeness_df = pd.DataFrame(rows)
    print(completeness_df.to_string(index=False))

    print()
    print("## Contributing Factor Unknown Rate")
    factor_metrics = compute_factor_unknown_rate(df)
    print(factor_metrics)

    print()
    print("## Density Altitude Completeness by Model")
    by_model = group_completeness(df, "model")
    if by_model is not None:
        print(by_model.to_string(index=False))
    else:
        print("model column not present")

    print()
    print("## Density Altitude Completeness by Operation Type")
    by_op = group_completeness(df, "operation_type")
    if by_op is not None:
        print(by_op.to_string(index=False))
    else:
        print("operation_type column not present")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
