#!/usr/bin/env python3
"""
Ranked Pattern Summaries (counts-only, no exposure-based rates)

Outputs:
  data/analysis/pattern_summaries_fleet.md
  data/analysis/pattern_summaries_<MODEL>.md

Assumptions about accident_master.csv:
  - Columns: model, operation_type, phase_of_flight, event_type
  - Severity: fatal, serious_injury, aircraft_destroyed
  - Contributing factors as boolean columns: cf_<factor_key> (including cf_unknown)
"""

import os
from datetime import datetime
import pandas as pd

MASTER_PATH = "data/master/accident_master.csv"
OUTPUT_DIR = "data/analysis"

TAXONOMY_VERSION = "1.3"
TOP_N = 15  # change if you want longer/shorter ranked lists


def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_master():
    df = pd.read_csv(MASTER_PATH)
    # Normalize some common empties
    for col in ["model", "operation_type", "phase_of_flight", "event_type"]:
        if col in df.columns:
            df[col] = df[col].fillna("").astype(str).str.strip()
            df.loc[df[col] == "", col] = "Unknown"
    return df


def factor_columns(df):
    return [c for c in df.columns if c.startswith("cf_")]


def non_unknown_factor_columns(df):
    return [c for c in factor_columns(df) if c != "cf_unknown"]


def unknown_factor_rate(df):
    fac_cols = non_unknown_factor_columns(df)
    known_assignments = int(df[fac_cols].sum().sum()) if fac_cols else 0
    unknown_assignments = int(df["cf_unknown"].sum()) if "cf_unknown" in df.columns else 0
    denom = known_assignments + unknown_assignments
    return round(unknown_assignments / denom, 4) if denom else 0.0


def header_block(df, analysis_gate_status: str):
    ds_total = len(df)
    ds_per_model = df["model"].value_counts().to_dict() if "model" in df.columns else {}
    unk_rate = unknown_factor_rate(df)

    lines = [
        f"taxonomy_version: {TAXONOMY_VERSION}",
        f"dataset_size_total: {ds_total}",
        f"dataset_size_per_model: {ds_per_model}",
        f"unknown_factor_rate: {unk_rate}",
        f"analysis_gate_status: {analysis_gate_status}",
        "",
    ]
    return "\n".join(lines)


def ranked_counts(series: pd.Series, top_n: int):
    """Rank values by count; return DataFrame with count + share_of_events."""
    counts = series.value_counts(dropna=False)
    df = counts.rename("count_events").reset_index().rename(columns={"index": "value"})
    df["share_of_events"] = (df["count_events"] / df["count_events"].sum()).round(4)
    return df.head(top_n)


def ranked_two_way(df: pd.DataFrame, a: str, b: str, top_n: int):
    """Rank (a,b) combinations by event count and share of events."""
    tmp = (
        df.groupby([a, b])
          .size()
          .reset_index(name="count_events")
          .sort_values(["count_events", a, b], ascending=[False, True, True])
    )
    tmp["share_of_events"] = (tmp["count_events"] / len(df)).round(4) if len(df) else 0.0
    return tmp.head(top_n)


def ranked_factor_counts(df: pd.DataFrame, top_n: int):
    """
    Rank factors by:
      - events_with_factor (count of events where factor column is 1)
      - share_of_events
      - share_of_factor_assignments (denominator = total factor assignments in slice)
    """
    fac_cols = non_unknown_factor_columns(df)
    if not fac_cols:
        return pd.DataFrame(columns=["factor", "events_with_factor", "share_of_events", "share_of_factor_assignments"])

    total_events = len(df)
    total_assignments = int(df[fac_cols].sum().sum())

    rows = []
    for col in fac_cols:
        events_with = int(df[col].sum())
        rows.append({
            "factor": col.replace("cf_", ""),
            "events_with_factor": events_with,
            "share_of_events": round(events_with / total_events, 4) if total_events else 0.0,
            "share_of_factor_assignments": round(events_with / total_assignments, 4) if total_assignments else 0.0,
        })

    out = pd.DataFrame(rows).sort_values(
        ["events_with_factor", "factor"],
        ascending=[False, True]
    )
    return out.head(top_n)


def ranked_phase_factor(df: pd.DataFrame, top_n: int):
    """Rank (phase_of_flight, factor) by count of events containing that factor in that phase."""
    fac_cols = non_unknown_factor_columns(df)
    if not fac_cols:
        return pd.DataFrame(columns=["phase_of_flight", "factor", "count_events", "share_of_events"])

    rows = []
    for phase, g in df.groupby("phase_of_flight"):
        for col in fac_cols:
            c = int(g[col].sum())
            if c > 0:
                rows.append({
                    "phase_of_flight": phase,
                    "factor": col.replace("cf_", ""),
                    "count_events": c,
                    "share_of_events": round(c / len(df), 4) if len(df) else 0.0
                })
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    out = out.sort_values(["count_events", "phase_of_flight", "factor"], ascending=[False, True, True])
    return out.head(top_n)


def ranked_event_factor(df: pd.DataFrame, top_n: int):
    """Rank (event_type, factor) by count of events containing that factor within that event type."""
    fac_cols = non_unknown_factor_columns(df)
    if not fac_cols:
        return pd.DataFrame(columns=["event_type", "factor", "count_events", "share_of_events"])

    rows = []
    for et, g in df.groupby("event_type"):
        for col in fac_cols:
            c = int(g[col].sum())
            if c > 0:
                rows.append({
                    "event_type": et,
                    "factor": col.replace("cf_", ""),
                    "count_events": c,
                    "share_of_events": round(c / len(df), 4) if len(df) else 0.0
                })
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    out = out.sort_values(["count_events", "event_type", "factor"], ascending=[False, True, True])
    return out.head(top_n)


def ranked_operation_factor(df: pd.DataFrame, top_n: int):
    """Rank (operation_type, factor) by count of events containing that factor within that operation type."""
    fac_cols = non_unknown_factor_columns(df)
    if not fac_cols:
        return pd.DataFrame(columns=["operation_type", "factor", "count_events", "share_of_events"])

    rows = []
    for op, g in df.groupby("operation_type"):
        for col in fac_cols:
            c = int(g[col].sum())
            if c > 0:
                rows.append({
                    "operation_type": op,
                    "factor": col.replace("cf_", ""),
                    "count_events": c,
                    "share_of_events": round(c / len(df), 4) if len(df) else 0.0
                })
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    out = out.sort_values(["count_events", "operation_type", "factor"], ascending=[False, True, True])
    return out.head(top_n)


def df_to_md_table(df: pd.DataFrame):
    if df is None or df.empty:
        return "_(no rows)_\n"
    return df.to_markdown(index=False) + "\n"


def render_report(df: pd.DataFrame, scope_label: str, analysis_gate_status: str) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    lines.append(f"# Ranked Pattern Summaries — {scope_label}")
    lines.append("")
    lines.append(f"_Generated: {now}_")
    lines.append("")
    lines.append("## Analysis Header (Required)")
    lines.append("")
    lines.append("```")
    lines.append(header_block(df, analysis_gate_status).rstrip())
    lines.append("```")
    lines.append("")
    lines.append("## Guardrails")
    lines.append("")
    lines.append("- Rankings are **counts-only** (no exposure-based rates).")
    lines.append("- Shares are labeled as **share_of_events** or **share_of_factor_assignments**.")
    lines.append("- Interpret patterns as “appears more frequently in this dataset,” not “higher risk.”")
    lines.append("")

    # Baseline
    lines.append("## Baseline Severity Context (counts by model within this scope)")
    lines.append("")
    if "model" in df.columns and df["model"].nunique() > 1:
        base = (
            df.groupby("model")
              .agg(
                total_events=("model", "count"),
                fatal_events=("fatal", "sum") if "fatal" in df.columns else ("model", "count"),
                serious_injury_events=("serious_injury", "sum") if "serious_injury" in df.columns else ("model", "count"),
                destroyed_aircraft=("aircraft_destroyed", "sum") if "aircraft_destroyed" in df.columns else ("model", "count"),
              )
              .reset_index()
        )
        lines.append(df_to_md_table(base))
    else:
        # single-model scope
        base = {
            "total_events": len(df),
            "fatal_events": int(df["fatal"].sum()) if "fatal" in df.columns else "n/a",
            "serious_injury_events": int(df["serious_injury"].sum()) if "serious_injury" in df.columns else "n/a",
            "destroyed_aircraft": int(df["aircraft_destroyed"].sum()) if "aircraft_destroyed" in df.columns else "n/a",
        }
        lines.append(f"- total_events: {base['total_events']}")
        lines.append(f"- fatal_events: {base['fatal_events']}")
        lines.append(f"- serious_injury_events: {base['serious_injury_events']}")
        lines.append(f"- destroyed_aircraft: {base['destroyed_aircraft']}")
        lines.append("")

    # Ranked: Event type / Phase / Operation
    lines.append(f"## Top {TOP_N} Event Types (ranked by count)")
    lines.append("")
    lines.append(df_to_md_table(ranked_counts(df["event_type"], TOP_N)))

    lines.append(f"## Top {TOP_N} Phases of Flight (ranked by count)")
    lines.append("")
    lines.append(df_to_md_table(ranked_counts(df["phase_of_flight"], TOP_N)))

    lines.append(f"## Top {TOP_N} Operation Types (ranked by count)")
    lines.append("")
    lines.append(df_to_md_table(ranked_counts(df["operation_type"], TOP_N)))

    # Two-way event patterns
    lines.append(f"## Top {TOP_N} Phase × Event Type Patterns (ranked by count)")
    lines.append("")
    lines.append(df_to_md_table(ranked_two_way(df, "phase_of_flight", "event_type", TOP_N)))

    # Factors
    lines.append(f"## Top {TOP_N} Contributing Factors (ranked by events_with_factor)")
    lines.append("")
    lines.append(df_to_md_table(ranked_factor_counts(df, TOP_N)))

    lines.append(f"## Top {TOP_N} Phase × Factor Patterns (ranked by count)")
    lines.append("")
    lines.append(df_to_md_table(ranked_phase_factor(df, TOP_N)))

    lines.append(f"## Top {TOP_N} Event Type × Factor Patterns (ranked by count)")
    lines.append("")
    lines.append(df_to_md_table(ranked_event_factor(df, TOP_N)))

    lines.append(f"## Top {TOP_N} Operation Type × Factor Patterns (ranked by count)")
    lines.append("")
    lines.append(df_to_md_table(ranked_operation_factor(df, TOP_N)))

    # Unknown notes
    if "cf_unknown" in df.columns:
        lines.append("## Unknown Factor Notes")
        lines.append("")
        unk_events = int(df["cf_unknown"].sum())
        lines.append(f"- events_with_unknown_factor: {unk_events}")
        lines.append(f"- unknown_factor_rate (assignment-based): {unknown_factor_rate(df)}")
        lines.append("")

    return "\n".join(lines)


def write_report(text: str, filename: str):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    ensure_output_dir()
    df = load_master()

    # Fleet report
    fleet_gate_status = (
        "Fleet gate OPEN (>= 75 total). Cross-model comparisons permitted. "
        "Counts-only; no exposure-based rates without exposure data."
    )
    fleet_report = render_report(df, "Fleet (C310/C340/C402)", fleet_gate_status)
    fleet_path = write_report(fleet_report, "pattern_summaries_fleet.md")
    print(f"Wrote: {fleet_path}")

    # Per-model reports
    for model in sorted(df["model"].unique()):
        sub = df[df["model"] == model].copy()
        model_status = (
            f"Per-model gate scope for {model}. Pattern summaries permitted within this model. "
            "Counts-only; no exposure-based rates without exposure data."
        )
        report = render_report(sub, f"Model {model}", model_status)
        out_name = f"pattern_summaries_{model}.md"
        path = write_report(report, out_name)
        print(f"Wrote: {path}")


if __name__ == "__main__":
    main()