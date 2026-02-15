#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# ---- Config you can tune ----
TARGET_MODELS = {"310", "320", "340", "402", "414", "421"}
TURBINE_RED_FLAGS = {"425", "441", "208", "500", "501", "510", "525", "560", "650"}  # crude but useful

DEFAULT_DATE_RANGE_LABEL = "2006-Present"


# ---- Helpers ----
def norm(s: str) -> str:
    return "".join(ch.lower() for ch in str(s).strip())


def find_col(df: pd.DataFrame, candidates: List[str], required: bool = False) -> Optional[str]:
    """
    Find a column whose normalized name contains any candidate tokens.
    candidates are compared as substrings against normalized column names.
    """
    cols = list(df.columns)
    norm_cols = {c: norm(c) for c in cols}

    # exact matches first
    for cand in candidates:
        c_norm = norm(cand)
        for c, nc in norm_cols.items():
            if nc == c_norm:
                return c

    # substring matches
    for cand in candidates:
        c_norm = norm(cand)
        for c, nc in norm_cols.items():
            if c_norm in nc:
                return c

    if required:
        raise KeyError(f"Could not find required column. Tried tokens: {candidates}. Available: {cols}")
    return None


def coerce_str(series: pd.Series) -> pd.Series:
    return series.astype(str).fillna("").str.strip()


def extract_year(series: pd.Series) -> pd.Series:
    s = coerce_str(series)
    years = s.str.extract(r"(\d{4})", expand=False)
    return pd.to_numeric(years, errors="coerce").astype("Int64")


def normalize_model(raw_model: str) -> str:
    """
    Normalize model strings into one of:
    C310/C320/C340/C402/C414/C421 or OTHER
    """
    m = norm(raw_model)
    m2 = (
        m.replace("cessna", "")
        .replace("-", "")
        .replace("_", "")
        .replace(" ", "")
        .replace("/", "")
    )
    for digits in TARGET_MODELS:
        if digits in m2:
            return f"C{digits}"
    return "OTHER"


def value_counts_table(series: pd.Series, top_n: int = 15) -> pd.DataFrame:
    vc = series.value_counts(dropna=False).head(top_n)
    return vc.rename_axis("value").reset_index(name="count")


def pct(n: int, d: int) -> str:
    if d == 0:
        return "0.0%"
    return f"{(100.0 * n / d):.1f}%"


def detect_turbine_or_out_of_scope_models(df: pd.DataFrame, model_col: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    raw = coerce_str(df[model_col])
    normalized = raw.map(normalize_model)

    out_scope = df.loc[normalized == "OTHER", [model_col]].copy()
    out_scope["model_raw"] = raw[normalized == "OTHER"].values

    def has_red_flag(x: str) -> bool:
        xx = norm(x).replace(" ", "")
        return any(flag in xx for flag in TURBINE_RED_FLAGS)

    red = df.loc[raw.map(has_red_flag), [model_col]].copy()
    red["model_raw"] = raw[raw.map(has_red_flag)].values
    return out_scope.drop(columns=[model_col]), red.drop(columns=[model_col])


def summarize(df: pd.DataFrame) -> Dict[str, object]:
    # Column detection (fuzzy)
    make_col = find_col(df, ["Make", "Aircraft Make", "ACFT Make", "Make Name"])
    model_col = find_col(df, ["Model", "Aircraft Model", "ACFT Model", "Model Name"], required=True)
    date_col = find_col(df, ["Event Date", "Accident Date", "Occurrence Date", "Date"], required=True)
    state_col = find_col(df, ["State", "Occ State", "Location State", "State Code"])
    far_col = find_col(df, ["FAR", "FAR Description", "Regulation", "FAR Part"])
    op_col = find_col(df, ["Operation", "Operation Type", "Op Type", "FAR Part", "Part 91", "Part 135"])
    phase_col = find_col(df, ["Phase", "Phase of Flight", "Flight Phase"])
    weather_col = find_col(df, ["Weather", "Weather Condition", "Wx"])
    severity_col = find_col(df, ["Injury Severity", "Inj Severity", "Severity"])
    damage_col = find_col(df, ["Aircraft Damage", "Damage", "ACFT Damage"])

    total_rows = len(df)

    model_norm = coerce_str(df[model_col]).map(normalize_model)
    years = extract_year(df[date_col])

    make_counts = value_counts_table(coerce_str(df[make_col])) if make_col else None
    model_dist = value_counts_table(model_norm)
    state_dist = value_counts_table(coerce_str(df[state_col])) if state_col else None
    far_dist = value_counts_table(coerce_str(df[far_col])) if far_col else None
    op_dist = value_counts_table(coerce_str(df[op_col])) if op_col else None
    phase_dist = value_counts_table(coerce_str(df[phase_col])) if phase_col else None
    weather_dist = value_counts_table(coerce_str(df[weather_col])) if weather_col else None
    severity_dist = value_counts_table(coerce_str(df[severity_col])) if severity_col else None
    damage_dist = value_counts_table(coerce_str(df[damage_col])) if damage_col else None

    out_scope, turbine_flags = detect_turbine_or_out_of_scope_models(df, model_col=model_col)

    part135_like = 0
    if op_col:
        op_vals = coerce_str(df[op_col]).str.lower()
        part135_like = int(op_vals.str.contains("135").sum())
    elif far_col:
        far_vals = coerce_str(df[far_col]).str.lower()
        part135_like = int(far_vals.str.contains("135").sum())

    summary = {
        "total_rows": total_rows,
        "cols_used": {
            "make": make_col,
            "model": model_col,
            "event_date": date_col,
            "state": state_col,
            "far": far_col,
            "operation": op_col,
            "phase": phase_col,
            "weather": weather_col,
            "injury_severity": severity_col,
            "aircraft_damage": damage_col,
        },
        "year_min": int(years.min()) if years.notna().any() else None,
        "year_max": int(years.max()) if years.notna().any() else None,
        "years_missing": int(years.isna().sum()),
        "make_counts": make_counts,
        "model_distribution": model_dist,
        "state_distribution": state_dist,
        "far_distribution": far_dist,
        "operation_distribution": op_dist,
        "phase_distribution": phase_dist,
        "weather_distribution": weather_dist,
        "injury_severity_distribution": severity_dist,
        "aircraft_damage_distribution": damage_dist,
        "out_of_scope_models_sample": out_scope.head(25),
        "turbine_red_flags_sample": turbine_flags.head(25),
        "part135_like_count": part135_like,
        # helpful extras
        "model_norm_series": model_norm,
    }
    return summary


def write_markdown_report(
    summary: Dict[str, object],
    input_path: Path,
    date_range_label: str,
    output_path: Path,
) -> None:
    total = summary["total_rows"]
    year_min = summary["year_min"]
    year_max = summary["year_max"]
    years_missing = summary["years_missing"]
    part135_like = summary["part135_like_count"]

    cols_used = summary["cols_used"]

    def df_to_md(df: Optional[pd.DataFrame]) -> str:
        if df is None or df.empty:
            return "_(not available)_\n"
        return df.to_markdown(index=False) + "\n"

    md = []
    md.append(f"# CAROL Export Summary\n")
    md.append(f"- Source file: `{input_path.as_posix()}`\n")
    md.append(f"- Intended window: `{date_range_label}`\n")
    md.append(f"- Rows: **{total}**\n")
    if year_min and year_max:
        md.append(f"- Event years (observed): **{year_min}–{year_max}** (missing year parse: {years_missing})\n")
    else:
        md.append(f"- Event years: _(could not parse)_ (missing year parse: {years_missing})\n")
    md.append(f"- Part 135-like rows (heuristic): **{part135_like}** ({pct(part135_like, total)})\n")

    md.append("\n## Columns Detected\n")
    md.append("| Field | Column |\n|---|---|\n")
    for k, v in cols_used.items():
        md.append(f"| {k} | {v or '—'} |\n")

    md.append("\n## Model Distribution (Normalized)\n")
    md.append(df_to_md(summary["model_distribution"]))

    md.append("\n## Make Distribution (Top)\n")
    md.append(df_to_md(summary["make_counts"]))

    md.append("\n## Operation / FAR Distribution (Top)\n")
    md.append("### Operation\n")
    md.append(df_to_md(summary["operation_distribution"]))
    md.append("### FAR\n")
    md.append(df_to_md(summary["far_distribution"]))

    md.append("\n## Phase / Weather Distribution (Top)\n")
    md.append("### Phase of Flight\n")
    md.append(df_to_md(summary["phase_distribution"]))
    md.append("### Weather\n")
    md.append(df_to_md(summary["weather_distribution"]))

    md.append("\n## Severity / Damage Distribution (Top)\n")
    md.append("### Injury Severity\n")
    md.append(df_to_md(summary["injury_severity_distribution"]))
    md.append("### Aircraft Damage\n")
    md.append(df_to_md(summary["aircraft_damage_distribution"]))

    md.append("\n## Red Flags (Samples)\n")
    md.append("### Out-of-scope models (normalized = OTHER)\n")
    md.append(df_to_md(summary["out_of_scope_models_sample"]))
    md.append("### Turbine-ish model red flags (crude substring check)\n")
    md.append(df_to_md(summary["turbine_red_flags_sample"]))

    output_path.write_text("".join(md), encoding="utf-8")


def build_weekly_snippet(
    summary: Dict[str, object],
    input_path: Path,
    date_range_label: str,
) -> str:
    total = summary["total_rows"]
    year_min = summary["year_min"]
    year_max = summary["year_max"]
    years_missing = summary["years_missing"]
    part135_like = summary["part135_like_count"]

    model_norm: pd.Series = summary["model_norm_series"]  # type: ignore
    model_counts = model_norm.value_counts()
    # ensure stable order for known models
    ordered_models = ["C310", "C320", "C340", "C402", "C414", "C421", "OTHER"]
    model_lines = []
    for m in ordered_models:
        c = int(model_counts.get(m, 0))
        if c > 0 or m != "OTHER":
            model_lines.append(f"- {m}: {c} ({pct(c, total)})")
    out_scope_ct = int(model_counts.get("OTHER", 0))

    # Samples
    out_scope_sample: pd.DataFrame = summary["out_of_scope_models_sample"]  # type: ignore
    turbine_sample: pd.DataFrame = summary["turbine_red_flags_sample"]  # type: ignore

    def sample_list(df: pd.DataFrame, max_items: int = 5) -> str:
        if df is None or df.empty:
            return "None observed."
        items = [str(x) for x in df["model_raw"].dropna().unique().tolist()]
        items = items[:max_items]
        return ", ".join(items) if items else "None observed."

    snippet = []
    snippet.append("### CAROL Export Summary (for audit trail)\n")
    snippet.append(f"- Export file: `{input_path.name}`\n")
    snippet.append(f"- Intended window: `{date_range_label}`\n")
    snippet.append(f"- Rows returned: **{total}**\n")
    if year_min and year_max:
        snippet.append(f"- Event years observed: **{year_min}–{year_max}** (unparsed dates: {years_missing})\n")
    else:
        snippet.append(f"- Event years observed: _(could not parse)_ (unparsed dates: {years_missing})\n")
    snippet.append(f"- Part 135-like rows (heuristic): **{part135_like}** ({pct(part135_like, total)})\n")

    snippet.append("\n**Model distribution (normalized):**\n")
    snippet.extend([f"{line}\n" for line in model_lines])

    snippet.append(f"\n**Out-of-scope model count (OTHER):** {out_scope_ct} ({pct(out_scope_ct, total)})\n")
    snippet.append(f"- Out-of-scope sample: {sample_list(out_scope_sample)}\n")
    snippet.append(f"- Turbine-ish red-flag sample: {sample_list(turbine_sample)}\n")

    snippet.append("\n_(Full markdown report saved via --out, if specified.)_\n")
    return "".join(snippet)


def main() -> int:
    ap = argparse.ArgumentParser(description="Summarize an NTSB CAROL CSV export for Twin Cessna scope.")
    ap.add_argument("csv", type=str, help="Path to CAROL export CSV")
    ap.add_argument("--date-range-label", type=str, default=DEFAULT_DATE_RANGE_LABEL, help="Label for intended date window")
    ap.add_argument(
        "--out",
        type=str,
        default="analysis/outputs/carol_export_summary.md",
        help="Output markdown report path",
    )
    ap.add_argument(
        "--weekly-snippet",
        action="store_true",
        help="Print a ready-to-paste snippet for worklog/weekly-progress.md",
    )
    ap.add_argument(
        "--weekly-snippet-out",
        type=str,
        default="",
        help="Optional file path to write the weekly snippet markdown (in addition to printing).",
    )
    args = ap.parse_args()

    csv_path = Path(args.csv).expanduser().resolve()
    if not csv_path.exists():
        print(f"ERROR: CSV not found: {csv_path}")
        return 2

    try:
        df = pd.read_csv(csv_path, dtype=str, encoding_errors="replace")
    except Exception as ex:
        print(f"ERROR reading CSV: {ex}")
        return 3

    summary = summarize(df)

    out_path = Path(args.out).expanduser()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    write_markdown_report(summary, csv_path, args.date_range_label, out_path)

    print(f"Wrote markdown report: {out_path.as_posix()}")

    if args.weekly_snippet:
        snippet = build_weekly_snippet(summary, csv_path, args.date_range_label)
        print("\n" + snippet)

        if args.weekly_snippet_out.strip():
            snip_path = Path(args.weekly_snippet_out).expanduser()
            snip_path.parent.mkdir(parents=True, exist_ok=True)
            snip_path.write_text(snippet, encoding="utf-8")
            print(f"Wrote weekly snippet: {snip_path.as_posix()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
