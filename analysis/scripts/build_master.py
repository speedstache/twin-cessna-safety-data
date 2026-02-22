#!/usr/bin/env python3
"""
Build master CSV datasets from structured event record Markdown files (YAML front matter).

This script is the single source of truth for generating:
- data/master/accident_master.csv
- data/master/incident_master.csv
- data/master/asrs_master.csv

Assumptions:
- Each structured record is a .md file with YAML front matter at the top.
- Contributing factors are recorded as a YAML list in `contributing_factors`.
- Master CSVs use fixed boolean columns: cf_<factor_key>.

Usage (from repo root):
  python3 analysis/scripts/build_master.py
  python3 analysis/scripts/build_master.py --type accidents
  python3 analysis/scripts/build_master.py --type accidents --out data/master/accident_master.csv

Recommended flow:
  python3 analysis/scripts/validate_records.py
  python3 analysis/scripts/build_master.py
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
import yaml


RE_FRONT_MATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# Taxonomy v1.0 factor keys (must align with docs/taxonomy/contributing-factors_v1.md)
FACTOR_KEYS = [
    # Human / Cognitive
    "normalization_of_deviance",
    "assumption_of_performance",
    "plan_continuation_bias",
    "checklist_non_compliance",
    "task_saturation",
    # Maintenance / Mechanical
    "aging_aircraft_degradation",
    "incomplete_troubleshooting",
    "deferred_discrepancy_normalization",
    "maintenance_induced_failure",
    # Performance / Operational
    "weight_balance_misjudgment",
    "density_altitude_underestimation",
    "single_engine_performance_assumption",
    "icing_performance_degradation",
    # Experience-related
    "low_time_in_type",
    "high_time_complacency",
    "lapsed_recency",
    "informal_or_incomplete_training",
    # Unknown
    "unknown",
]

# Base columns for all masters (must align with data/master/data_dictionary.md)
BASE_COLUMNS = [
    # Identification
    "event_id",
    "model",
    "variant",
    "engine_type",
    "year",
    "operation_type",
    "state",
    "country",
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
    # Experience
    "total_time_band",
    "multi_time_band",
    "time_in_type_band",
    "recency_status",
    # Outcome
    "event_type",
    "event_subtype",
    "fatal",
    "serious_injury",
    "aircraft_destroyed",
    # Prevention
    "prevention_category",
    "prevention_summary",
]

CF_COLUMNS = [f"cf_{k}" for k in FACTOR_KEYS]

# Keep the raw list for traceability
TRACE_COLUMNS = ["contributing_factors", "contributing_factors_raw"]

ALL_COLUMNS = BASE_COLUMNS + CF_COLUMNS + TRACE_COLUMNS


def load_front_matter(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    m = RE_FRONT_MATTER.search(text)
    if not m:
        raise ValueError("Missing YAML front matter at top of file (--- ... ---).")
    data = yaml.safe_load(m.group(1))
    return data or {}


def to_bool_or_none(x: Any) -> Optional[bool]:
    if x is None or x == "":
        return None
    if isinstance(x, bool):
        return x
    if isinstance(x, (int, float)):
        return bool(x)
    s = str(x).strip().lower()
    if s in {"true", "t", "yes", "y", "1"}:
        return True
    if s in {"false", "f", "no", "n", "0"}:
        return False
    return None


def contributing_factors_list(d: Dict[str, Any]) -> List[str]:
    cfs = d.get("contributing_factors", [])
    if cfs is None:
        return []
    if isinstance(cfs, str):
        return [cfs.strip()]
    if isinstance(cfs, list):
        return [str(x).strip() for x in cfs if str(x).strip() != ""]
    return []


def record_to_row(d: Dict[str, Any], dataset_type: str) -> Dict[str, Any]:
    """
    dataset_type: 'accidents' | 'incidents' | 'asrs'
    """
    row: Dict[str, Any] = {}

    # Base fields
    for c in BASE_COLUMNS:
        row[c] = d.get(c)

    # Normalize year to integer (if possible)
    y = row.get("year")
    try:
        row["year"] = int(y) if y is not None and y != "" else None
    except Exception:
        # Leave as-is; validate_records.py should catch this
        row["year"] = y

    # Normalize booleans
    for b in ["fatal", "serious_injury", "aircraft_destroyed"]:
        if dataset_type == "asrs":
            # ASRS typically has no reliable outcome fields; keep blank
            row[b] = None
        else:
            row[b] = to_bool_or_none(row.get(b))

    # Expand contributing factors to boolean columns
    cfs = contributing_factors_list(d)
    cf_set = set(cfs)

    for k in FACTOR_KEYS:
        row[f"cf_{k}"] = (k in cf_set)

    # Traceability
    row["contributing_factors"] = "|".join(cfs)      # analysis-friendly
    row["contributing_factors_raw"] = ",".join(cfs)  # keep as-is for legacy/trace

    # Ensure missing optional fields become blank rather than NaN at write time
    return row


def collect_records(root: Path) -> List[Path]:
    return sorted([p for p in root.rglob("*.md") if p.is_file()])


def build_dataset(repo_root: Path, dataset_type: str) -> Tuple[pd.DataFrame, Path]:
    """
    dataset_type maps to:
      accidents -> data/structured/accidents -> data/master/accident_master.csv
      incidents -> data/structured/incidents -> data/master/incident_master.csv
      asrs      -> data/structured/asrs      -> data/master/asrs_master.csv
    """
    if dataset_type not in {"accidents", "incidents", "asrs"}:
        raise ValueError("dataset_type must be one of: accidents, incidents, asrs")

    in_dir = repo_root / "data" / "structured" / dataset_type
    if not in_dir.exists():
        raise FileNotFoundError(f"Input directory not found: {in_dir}")

    files = collect_records(in_dir)
    rows: List[Dict[str, Any]] = []

    for f in files:
        d = load_front_matter(f)
        rows.append(record_to_row(d, dataset_type))

    df = pd.DataFrame(rows)

    # Ensure all expected columns exist and enforce order
    for c in ALL_COLUMNS:
        if c not in df.columns:
            df[c] = None
    df = df[ALL_COLUMNS]

    out_dir = repo_root / "data" / "master"
    out_dir.mkdir(parents=True, exist_ok=True)

    out_name = {
        "accidents": "accident_master.csv",
        "incidents": "incident_master.csv",
        "asrs": "asrs_master.csv",
    }[dataset_type]

    return df, (out_dir / out_name)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    # Keep empty cells empty (not "nan")
    df = df.copy()
    df.to_csv(path, index=False)


def main() -> int:
    ap = argparse.ArgumentParser(description="Build master CSV datasets from structured event records.")
    ap.add_argument(
        "--type",
        type=str,
        default="all",
        choices=["all", "accidents", "incidents", "asrs"],
        help="Which dataset to build (default: all).",
    )
    ap.add_argument(
        "--out",
        type=str,
        default="",
        help="Optional output path (only valid when --type is not 'all').",
    )
    args = ap.parse_args()

    repo_root = Path.cwd()

    datasets = ["accidents", "incidents", "asrs"] if args.type == "all" else [args.type]

    for ds in datasets:
        df, default_out = build_dataset(repo_root, ds)

        out_path = default_out
        if args.out:
            if args.type == "all":
                print("ERROR: --out cannot be used with --type all.")
                return 2
            out_path = Path(args.out).expanduser()
            out_path.parent.mkdir(parents=True, exist_ok=True)

        write_csv(df, out_path)

        print(f"Wrote {len(df)} rows -> {out_path.as_posix()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
