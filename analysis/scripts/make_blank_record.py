#!/usr/bin/env python3
"""
make_blank_record.py

Creates a blank structured accident record as a YAML-frontmatter Markdown file.

Assumptions (based on your project):
- Structured records live under: data/structured/accidents/<MODEL>/
- File naming: <Model>-ACC-<Year>-<Sequence>.md  (sequence is per model, per year)
- YAML format matches your existing record style (--- header ---).

This script:
- Auto-increments the per-model/per-year sequence by scanning existing files
- Writes a new record with required fields + safe placeholders (Unknown / false)
- Does NOT attempt to infer anything from PDFs (no guessing)

Usage examples:
  python analysis/scripts/make_blank_record.py --model C310 --year 2006 --report-number ERA23LA018
  python analysis/scripts/make_blank_record.py --model C414 --year 2014 --report-number WPR14LA123 --variant A --engine-type TSIO-520-NB
  python analysis/scripts/make_blank_record.py --model C310 --year 2006 --report-number ERA23LA018 --operation-type 91

Notes:
- If you want operation_type unknown, omit --operation-type.
- drive_path is set to: 01_NTSB/<Model>/<Year>/<ReportNumber>.pdf
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Optional


SEQ_RE = re.compile(r"^(?P<model>[A-Z0-9]+)-ACC-(?P<year>\d{4})-(?P<seq>\d{3})\.md$", re.IGNORECASE)


@dataclass(frozen=True)
class Args:
    model: str
    year: int
    report_number: str
    variant: str
    engine_type: str
    operation_type: str
    source: str
    state: str
    country: str
    taxonomy_version: str
    out_root: Path
    downloaded: str


def normalize_model(model: str) -> str:
    m = model.strip().upper()
    # Accept "310" and normalize to "C310"
    if re.fullmatch(r"\d{3}", m):
        m = f"C{m}"
    return m


def next_sequence(model_dir: Path, model: str, year: int) -> int:
    """
    Determine next 3-digit sequence for files matching <Model>-ACC-<Year>-<Seq>.md
    within model_dir.
    """
    max_seq = 0
    if not model_dir.exists():
        return 1

    for p in model_dir.glob(f"{model}-ACC-{year}-*.md"):
        m = SEQ_RE.match(p.name)
        if not m:
            continue
        try:
            seq = int(m.group("seq"))
            max_seq = max(max_seq, seq)
        except ValueError:
            continue
    return max_seq + 1


def render_record_yaml(a: Args, event_id: str, drive_path: str) -> str:
    """
    Produce YAML-frontmatter record with safe placeholders.
    Keep this aligned with your validator/schema expectations.
    """
    # You can tighten these placeholders later; for blank records, Unknown is safer than guessing.
    y = f"""---
event_id: {event_id}
model: {a.model}
variant: {a.variant}
engine_type: {a.engine_type}
year: {a.year}
operation_type: {a.operation_type}
state: {a.state}
country: {a.country}
source: {a.source}
report_number: {a.report_number}
drive_path: {drive_path}
downloaded: {a.downloaded}
taxonomy_version: {a.taxonomy_version}

# Context
phase_of_flight: Unknown
mission_profile: Unknown
weather_category: Unknown
density_altitude_category: Unknown
maintenance_context: Unknown

# Pilot Bands
total_time_band: Unknown
multi_time_band: Unknown
time_in_type_band: Unknown
recency_status: Unknown

# Classification

event_type: Unknown
fatal: false
serious_injury: false
aircraft_destroyed: false

# Contributing Factors (max 3)
contributing_factors:
  - unknown

# Prevention
prevention_category: Unknown
prevention_summary: "TBD"

# Narrative (5–10 factual sentences; no speculation)
narrative: "TBD"
---
"""
    return y


def parse_args() -> Args:
    ap = argparse.ArgumentParser(description="Create a blank structured accident record (YAML-frontmatter markdown).")
    ap.add_argument("--model", required=True, help="Aircraft model (e.g., C310, 310, C414)")
    ap.add_argument("--year", required=True, type=int, help="Event year used for filename/sequence (YYYY)")
    ap.add_argument("--report-number", required=True, help="NTSB report number (e.g., ERA23LA018)")

    ap.add_argument("--variant", default="Unknown", help="Variant (e.g., Q, R). Default: Unknown")
    ap.add_argument("--engine-type", default="Unknown", help="Engine type (e.g., IO-520-MB). Default: Unknown")
    ap.add_argument("--operation-type", default="Unknown", help="Operation type (91, 135, Unknown). Default: 91")

    ap.add_argument("--source", default="NTSB", help="Data source. Default: NTSB")
    ap.add_argument("--state", default="Unknown", help="Data source. Default: Unknown")
    ap.add_argument("--country", default="USA", help="Country. Default: USA")
    ap.add_argument("--taxonomy-version", default="1.2", help="Taxonomy version string. Default: 1.2")

    ap.add_argument(
        "--out-root",
        default="data/structured/accidents",
        help="Root directory for structured accident records. Default: data/structured/accidents",
    )
    ap.add_argument(
        "--downloaded",
        default=str(date.today()),
        help="Downloaded date (YYYY-MM-DD). Default: today",
    )

    ns = ap.parse_args()

    model = normalize_model(ns.model)
    out_root = Path(ns.out_root)

    return Args(
        model=model,
        year=int(ns.year),
        report_number=str(ns.report_number).strip(),
        variant=str(ns.variant).strip() if str(ns.variant).strip() else "Unknown",
        engine_type=str(ns.engine_type).strip() if str(ns.engine_type).strip() else "Unknown",
        operation_type=str(ns.operation_type).strip() if str(ns.operation_type).strip() else "Unknown",
        source=str(ns.source).strip() if str(ns.source).strip() else "NTSB",
        state=str(ns.state).strip() if str(ns.state).strip() else "Unknown",
        country=str(ns.country).strip() if str(ns.country).strip() else "USA",
        taxonomy_version=str(ns.taxonomy_version).strip() if str(ns.taxonomy_version).strip() else "1.1",
        out_root=out_root,
        downloaded=str(ns.downloaded).strip(),
    )


def main() -> int:
    a = parse_args()

    model_dir = a.out_root / a.model
    model_dir.mkdir(parents=True, exist_ok=True)

    seq = next_sequence(model_dir, a.model, a.year)
    seq_str = f"{seq:03d}"

    filename = f"{a.model}-ACC-{a.year}-{seq_str}.md"
    out_path = model_dir / filename

    event_id = f"{a.model}-ACC-{a.year}-{seq_str}"
    drive_path = f"01_NTSB/{a.model}/{a.year}/{a.report_number}.pdf"

    if out_path.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {out_path}")

    content = render_record_yaml(a, event_id=event_id, drive_path=drive_path)
    out_path.write_text(content, encoding="utf-8")

    print(f"Created: {out_path}")
    print(f"event_id: {event_id}")
    print(f"drive_path: {drive_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())