#!/usr/bin/env python3
"""
analysis_gate_status.py

Prints the required analysis header fields and enforces dataset maturity gates.

This script is governance tooling. It does NOT perform analysis.

Required header (per project instructions):
  taxonomy_version:
  dataset_size_total:
  dataset_size_per_model:
  unknown_factor_rate:
  analysis_gate_status:

Gates (locked rules from project instructions):
- Per-model gate opens at >= 25 accidents in one model (pattern summaries allowed for that model only).
- Fleet-level gate opens at >= 75 accidents total (cross-model comparisons allowed).
- Unknown Factor Rule: if unknown_factor_rate > 0.40, pause and reassess taxonomy clarity.

Usage:
  python scripts/analysis_gate_status.py --csv data/structured/accidents_master.csv
  python scripts/analysis_gate_status.py --csv accidents_master.csv --json-out gate_status.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd


PER_MODEL_GATE = 25
FLEET_GATE = 75
UNKNOWN_FACTOR_THRESHOLD = 0.40


def _pick_col(df: pd.DataFrame, candidates: List[str]) -> Optional[str]:
    cols_lower = {c.lower(): c for c in df.columns}
    for cand in candidates:
        if cand.lower() in cols_lower:
            return cols_lower[cand.lower()]
    return None


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

    # YAML-ish / newline formats
    s = s.replace("\n- ", "|").replace("\n-", "|").replace("\n", "|")
    s = re.sub(r"^\s*-\s*", "", s)

    # Delimiters
    parts = re.split(r"[|;,]", s)
    factors = [p.strip().lower() for p in parts if p.strip()]
    if not factors and s:
        factors = [s.lower()]
    return factors


def _unknown_factor_rate(df: pd.DataFrame, col_factors: Optional[str]) -> Any:
    """
    Unknown factor rate defined as:
      (# records with contributing_factors containing 'unknown') / (# records with any parsable factor list)
    If no factors column exists or no parsable factors exist, returns a descriptive string.
    """
    if not col_factors:
        return "Unknown (no contributing_factors column found)"

    factors_lists = df[col_factors].apply(_parse_factor_list)
    has_any = factors_lists.apply(lambda lst: len(lst) > 0)
    denom = int(has_any.sum())
    if denom == 0:
        return "Unknown (no parsable factors found)"

    unknown_flags = factors_lists.apply(lambda lst: any(x == "unknown" for x in lst))
    return round(int(unknown_flags.sum()) / denom, 4)


def _taxonomy_version_display(df: pd.DataFrame, col_tax: Optional[str]) -> Any:
    if not col_tax:
        return "Unknown (no taxonomy_version column found)"
    vc = (
        df[col_tax]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .replace({"": "Unknown"})
        .value_counts(dropna=False)
    )
    dist = {str(k): int(v) for k, v in vc.items()}
    if len(dist) == 1:
        return next(iter(dist.keys()))
    return dist


def _dataset_size_per_model(df: pd.DataFrame, col_model: Optional[str]) -> Dict[str, int]:
    if not col_model:
        return {}
    vc = (
        df[col_model]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .replace({"": "Unknown"})
        .value_counts(dropna=False)
    )
    return {str(k): int(v) for k, v in vc.items()}


def _gate_status(
    dataset_size_total: int,
    per_model_counts: Dict[str, int],
    unknown_rate: Any,
) -> Dict[str, Any]:
    """
    Returns a structured gate status summary.
    """
    # Per-model
    models_meeting_gate = {m: c for m, c in per_model_counts.items() if c >= PER_MODEL_GATE and m != "Unknown"}
    per_model_gate_open = len(models_meeting_gate) > 0

    # Fleet
    fleet_gate_open = dataset_size_total >= FLEET_GATE

    # Unknown factor rule
    unknown_flag = None
    unknown_pause_required = False
    if isinstance(unknown_rate, (int, float)):
        unknown_flag = unknown_rate > UNKNOWN_FACTOR_THRESHOLD
        unknown_pause_required = bool(unknown_flag)

    # Narrative status (governance language)
    status_lines = []

    if unknown_pause_required:
        status_lines.append(
            f"PAUSE: unknown_factor_rate ({unknown_rate}) exceeds {UNKNOWN_FACTOR_THRESHOLD:.2f} threshold; reassess taxonomy clarity and coding guidance."
        )

    if per_model_gate_open:
        # List models meeting gate
        models_str = ", ".join([f"{m}={c}" for m, c in sorted(models_meeting_gate.items(), key=lambda x: (-x[1], x[0]))])
        status_lines.append(
            f"Per-model gate OPEN for: {models_str}. Pattern summaries permitted ONLY within these model(s)."
        )
    else:
        status_lines.append(
            f"Per-model gate CLOSED (need >= {PER_MODEL_GATE} accidents in at least one model)."
        )

    if fleet_gate_open:
        status_lines.append(
            f"Fleet gate OPEN (>= {FLEET_GATE} total). Cross-model comparisons permitted."
        )
    else:
        status_lines.append(
            f"Fleet gate CLOSED (need >= {FLEET_GATE} total). Cross-model comparisons NOT permitted."
        )

    # Always remind on what is allowed right now
    if not per_model_gate_open:
        allowed = "Allowed outputs: validation, descriptive snapshots, governance metrics, traceability demos. No pattern summaries or rankings."
    elif per_model_gate_open and not fleet_gate_open:
        allowed = "Allowed outputs: per-model pattern summaries ONLY for models meeting gate; no cross-model or 91 vs 135 comparisons."
    else:
        allowed = "Allowed outputs: pattern summaries, risk rankings, comparative analysis per project standards (still no exposure-based rates without exposure data)."

    status_lines.append(allowed)

    return {
        "per_model_gate": {
            "threshold": PER_MODEL_GATE,
            "open": per_model_gate_open,
            "models_meeting_threshold": models_meeting_gate,
        },
        "fleet_gate": {
            "threshold": FLEET_GATE,
            "open": fleet_gate_open,
        },
        "unknown_factor_rule": {
            "threshold": UNKNOWN_FACTOR_THRESHOLD,
            "unknown_factor_rate": unknown_rate,
            "pause_required": unknown_pause_required,
        },
        "analysis_gate_status": " | ".join(status_lines),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Compute and print dataset maturity gate status.")
    ap.add_argument("--csv", required=True, help="Path to accidents_master.csv")
    ap.add_argument("--json-out", default=None, help="Optional path to write JSON output")
    args = ap.parse_args()

    csv_path = Path(args.csv).expanduser().resolve()
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    df = pd.read_csv(csv_path)

    col_tax = _pick_col(df, ["taxonomy_version", "taxonomy"])
    col_model = _pick_col(df, ["model", "aircraft_model"])
    col_factors = _pick_col(df, ["contributing_factors", "factors"])

    taxonomy_version = _taxonomy_version_display(df, col_tax)
    dataset_size_total = int(len(df))
    per_model_counts = _dataset_size_per_model(df, col_model)
    unknown_rate = _unknown_factor_rate(df, col_factors)

    gate = _gate_status(dataset_size_total, per_model_counts, unknown_rate)

    # ---- Required header output (plain) ----
    # This format is intentionally simple to paste into analysis docs.
    print("taxonomy_version:", taxonomy_version)
    print("dataset_size_total:", dataset_size_total)
    print("dataset_size_per_model:", per_model_counts if per_model_counts else "Unknown (no model column found)")
    print("unknown_factor_rate:", unknown_rate)
    print("analysis_gate_status:", gate["analysis_gate_status"])

    out_obj: Dict[str, Any] = {
        "taxonomy_version": taxonomy_version,
        "dataset_size_total": dataset_size_total,
        "dataset_size_per_model": per_model_counts,
        "unknown_factor_rate": unknown_rate,
        **gate,
        "source_file": str(csv_path),
    }

    if args.json_out:
        out_path = Path(args.json_out).expanduser().resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(out_obj, indent=2), encoding="utf-8")
        print(f"\nWrote JSON output: {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
