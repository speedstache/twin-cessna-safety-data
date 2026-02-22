#!/usr/bin/env python3
"""
Cross-model comparison report for accident patterns.

Reads:
  data/master/accident_master.csv

Writes:
  data/analysis/cross_model_comparison.md

The report is counts-only and compares where each model over-indexes relative
to fleet-level shares for:
  - event_type
  - phase_of_flight
  - operation_type
  - contributing factors (cf_* columns except cf_unknown)
"""

from __future__ import annotations

import argparse
import os
from datetime import datetime
from typing import Iterable, List

import pandas as pd

MASTER_PATH = "data/master/accident_master.csv"
DEFAULT_OUT = "data/analysis/cross_model_comparison.md"
DEFAULT_MIN_EVENTS = 8
DEFAULT_TOP_N = 10


def load_master(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    for col in ["model", "event_type", "phase_of_flight", "operation_type"]:
        if col in df.columns:
            df[col] = df[col].fillna("").astype(str).str.strip()
            df.loc[df[col] == "", col] = "Unknown"
    return df


def factor_columns(df: pd.DataFrame) -> List[str]:
    return [c for c in df.columns if c.startswith("cf_") and c != "cf_unknown"]


def unknown_factor_rate(df: pd.DataFrame) -> float:
    fac_cols = factor_columns(df)
    known = int(df[fac_cols].sum().sum()) if fac_cols else 0
    unknown = int(df["cf_unknown"].sum()) if "cf_unknown" in df.columns else 0
    denom = known + unknown
    return round(unknown / denom, 4) if denom else 0.0


def ensure_output_dir(path: str) -> None:
    out_dir = os.path.dirname(path) or "."
    os.makedirs(out_dir, exist_ok=True)


def md_table(df: pd.DataFrame) -> str:
    if df.empty:
        return "_(no rows)_\n"
    return df.to_markdown(index=False) + "\n"


def model_baseline(df: pd.DataFrame, models: Iterable[str]) -> pd.DataFrame:
    sub = df[df["model"].isin(models)].copy()
    total = len(sub)

    rows = []
    for model, g in sub.groupby("model"):
        n = len(g)
        rows.append(
            {
                "model": model,
                "events": n,
                "share_of_dataset": round(n / total, 4) if total else 0.0,
                "fatal_events": int(g["fatal"].sum()) if "fatal" in g.columns else None,
                "fatal_share_of_model_events": round(g["fatal"].mean(), 4) if "fatal" in g.columns else None,
                "serious_injury_events": int(g["serious_injury"].sum()) if "serious_injury" in g.columns else None,
                "destroyed_aircraft": int(g["aircraft_destroyed"].sum()) if "aircraft_destroyed" in g.columns else None,
            }
        )
    return pd.DataFrame(rows).sort_values(["events", "model"], ascending=[False, True])


def over_index_for_category(
    df: pd.DataFrame,
    models: Iterable[str],
    category_col: str,
    top_n: int,
) -> pd.DataFrame:
    sub = df[df["model"].isin(models)].copy()
    fleet_counts = sub[category_col].value_counts(dropna=False)
    fleet_total = len(sub)
    fleet_share = (fleet_counts / fleet_total).to_dict() if fleet_total else {}

    rows = []
    for model, g in sub.groupby("model"):
        model_total = len(g)
        if model_total == 0:
            continue
        counts = g[category_col].value_counts(dropna=False)
        for value, c in counts.items():
            share_model = c / model_total
            share_fleet = fleet_share.get(value, 0.0)
            rows.append(
                {
                    "model": model,
                    "value": value,
                    "count_events": int(c),
                    "share_in_model": round(share_model, 4),
                    "share_in_fleet": round(share_fleet, 4),
                    "delta_share": round(share_model - share_fleet, 4),
                    "index_vs_fleet": round((share_model / share_fleet), 3) if share_fleet > 0 else None,
                }
            )

    out = pd.DataFrame(rows)
    if out.empty:
        return out

    out = out[out["delta_share"] > 0].copy()
    if out.empty:
        return out

    out = out.sort_values(
        ["model", "delta_share", "count_events", "value"],
        ascending=[True, False, False, True],
    )
    return out.groupby("model", as_index=False).head(top_n)


def over_index_for_factors(df: pd.DataFrame, models: Iterable[str], top_n: int) -> pd.DataFrame:
    sub = df[df["model"].isin(models)].copy()
    fac_cols = factor_columns(sub)
    if not fac_cols:
        return pd.DataFrame()

    fleet_n = len(sub)
    fleet_share = {col: float(sub[col].mean()) for col in fac_cols} if fleet_n else {}

    rows = []
    for model, g in sub.groupby("model"):
        n = len(g)
        if n == 0:
            continue
        for col in fac_cols:
            c = int(g[col].sum())
            share_model = c / n
            share_fleet = fleet_share.get(col, 0.0)
            rows.append(
                {
                    "model": model,
                    "factor": col.replace("cf_", ""),
                    "events_with_factor": c,
                    "share_in_model": round(share_model, 4),
                    "share_in_fleet": round(share_fleet, 4),
                    "delta_share": round(share_model - share_fleet, 4),
                    "index_vs_fleet": round((share_model / share_fleet), 3) if share_fleet > 0 else None,
                }
            )

    out = pd.DataFrame(rows)
    if out.empty:
        return out
    out = out[(out["events_with_factor"] > 0) & (out["delta_share"] > 0)].copy()
    if out.empty:
        return out

    out = out.sort_values(
        ["model", "delta_share", "events_with_factor", "factor"],
        ascending=[True, False, False, True],
    )
    return out.groupby("model", as_index=False).head(top_n)


def render_report(
    df: pd.DataFrame,
    models: List[str],
    min_events: int,
    top_n: int,
    input_path: str,
) -> str:
    created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    baseline = model_baseline(df, models)
    event_over = over_index_for_category(df, models, "event_type", top_n)
    phase_over = over_index_for_category(df, models, "phase_of_flight", top_n)
    op_over = over_index_for_category(df, models, "operation_type", top_n)
    factor_over = over_index_for_factors(df, models, top_n)

    lines: List[str] = []
    lines.append("# Cross-Model Comparison (Accidents)")
    lines.append("")
    lines.append(f"_Generated: {created}_")
    lines.append("")
    lines.append("## Analysis Header")
    lines.append("")
    lines.append("```")
    lines.append(f"input_dataset: {input_path}")
    lines.append(f"dataset_size_total: {len(df)}")
    lines.append(f"models_compared: {models}")
    lines.append(f"model_min_events_gate: {min_events}")
    lines.append(f"unknown_factor_rate: {unknown_factor_rate(df)}")
    lines.append("analysis_guardrail: counts-only; no exposure-based risk inference")
    lines.append("```")
    lines.append("")
    lines.append("## Baseline by Model")
    lines.append("")
    lines.append(md_table(baseline))
    lines.append("## Over-Indexed Event Types by Model")
    lines.append("")
    lines.append(md_table(event_over))
    lines.append("## Over-Indexed Phases by Model")
    lines.append("")
    lines.append(md_table(phase_over))
    lines.append("## Over-Indexed Operation Types by Model")
    lines.append("")
    lines.append(md_table(op_over))
    lines.append("## Over-Indexed Contributing Factors by Model")
    lines.append("")
    lines.append(md_table(factor_over))
    lines.append("## Notes")
    lines.append("")
    lines.append("- `delta_share` is model share minus fleet share for the same pattern.")
    lines.append("- `index_vs_fleet > 1` means the pattern appears more often in that model's dataset slice.")
    lines.append("- Results are descriptive frequency comparisons, not risk estimates.")
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build cross-model comparison report.")
    parser.add_argument("--input", default=MASTER_PATH, help="Path to accident master CSV.")
    parser.add_argument("--out", default=DEFAULT_OUT, help="Output markdown path.")
    parser.add_argument(
        "--models",
        nargs="*",
        default=None,
        help="Optional list of models to compare (default: models meeting --min-events).",
    )
    parser.add_argument(
        "--min-events",
        type=int,
        default=DEFAULT_MIN_EVENTS,
        help="Minimum events per model required for comparison when --models not set.",
    )
    parser.add_argument("--top-n", type=int, default=DEFAULT_TOP_N, help="Top rows per model per section.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = load_master(args.input)

    if "model" not in df.columns:
        raise ValueError("Input dataset must include a `model` column.")

    if args.models:
        models = sorted(set(args.models))
    else:
        counts = df["model"].value_counts()
        models = sorted(counts[counts >= args.min_events].index.tolist())

    if len(models) < 2:
        raise ValueError(
            "Need at least 2 models for cross-model comparison. "
            "Lower --min-events or pass --models explicitly."
        )

    text = render_report(df, models=models, min_events=args.min_events, top_n=args.top_n, input_path=args.input)
    ensure_output_dir(args.out)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote: {args.out}")


if __name__ == "__main__":
    main()
