#!/usr/bin/env python3
"""
Validate structured event record files for the Twin Cessna Safety Data & Research Project.

What this script checks (v1.0 baseline):
- YAML front matter exists and parses
- Required fields present
- Allowed categorical values enforced (prevents drift)
- event_id matches filename
- model is in scope (C310/C320/C340/C402/C414/C421)
- contributing_factors contains 1–3 items, OR exactly ['unknown']
- contributing_factors keys are valid for taxonomy v1.0
- Basic sanity checks (year range, booleans)

Usage (from repo root):
  python3 analysis/scripts/validate_records.py
  python3 analysis/scripts/validate_records.py --path data/structured/accidents
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

RE_FRONT_MATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# ---- Scope (fleet-wide) ----
ALLOWED_MODELS = {"C310", "C320", "C340", "C402", "C414", "C421"}
ALLOWED_SOURCES = {"NTSB", "ASRS", "FAA", "Other"}
ALLOWED_OPERATION = {91, 135}

# ---- Allowed categorical values (must match data_dictionary.md) ----
ALLOWED_PHASE = {
    "Takeoff",
    "Initial_Climb",
    "Cruise",
    "Descent",
    "Approach",
    "Landing",
    "Go_Around",
    "Taxi",
    "Unknown",
}
ALLOWED_MISSION = {
    "Personal",
    "Business",
    "Training",
    "Ferry",
    "Maintenance_Flight",
    "Commercial",
    "Unknown",
}
ALLOWED_WEATHER = {"VMC", "IMC", "Night", "Icing", "High_DA", "Mixed", "Unknown"}
ALLOWED_DENSITY_ALT = {"Low", "Moderate", "High", "Extreme", "Unknown"}
ALLOWED_MAINT_CONTEXT = {"Recent_Work", "Deferred", "None_Noted", "Unknown"}
ALLOWED_RECENCY = {"Current", "Lapsed", "Unknown"}

ALLOWED_TOTAL_BAND = {"<500", "500-1500", "1500-5000", ">5000", "Unknown"}
ALLOWED_MULTI_BAND = ALLOWED_TOTAL_BAND
ALLOWED_TYPE_BAND = {"<50", "50-200", "200-1000", ">1000", "Unknown"}

ALLOWED_PREVENTION_CATEGORY = {"Training", "Maintenance", "SOP", "Equipment", "Awareness", "Unknown"}

# ---- Taxonomy v1.0 factor keys (YAML list entries) ----
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
FACTOR_SET = set(FACTOR_KEYS)

# ---- Required YAML fields (baseline validation) ----
REQUIRED_FIELDS = [
    "event_id",
    "model",
    "year",
    "operation_type",
    "state",
    "country",
    "source",
    "report_number",
    "drive_path",
    "downloaded",
    "taxonomy_version",
    "phase_of_flight",
    "mission_profile",
    "weather_category",
    "density_altitude_category",
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


@dataclass
class ValidationIssue:
    path: Path
    level: str  # "ERROR" or "WARN"
    message: str


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


def filename_stem(path: Path) -> str:
    return path.name.rsplit(".", 1)[0]


def validate_required_fields(path: Path, d: Dict[str, Any], issues: List[ValidationIssue]) -> None:
    for f in REQUIRED_FIELDS:
        if f not in d or d[f] in (None, "", []):
            issues.append(ValidationIssue(path, "ERROR", f"Missing required field: {f}"))


def validate_event_id_matches_filename(path: Path, d: Dict[str, Any], issues: List[ValidationIssue]) -> None:
    eid = d.get("event_id")
    if not eid:
        return
    stem = filename_stem(path)
    if str(eid).strip() != stem:
        issues.append(
            ValidationIssue(
                path,
                "ERROR",
                f"event_id '{eid}' does not match filename stem '{stem}'.",
            )
        )


def validate_enums(path: Path, d: Dict[str, Any], issues: List[ValidationIssue]) -> None:
    def check(field: str, allowed: set[str]) -> None:
        v = d.get(field)
        if v is None or v == "":
            return
        if v not in allowed:
            issues.append(
                ValidationIssue(
                    path,
                    "ERROR",
                    f"Invalid {field}='{v}'. Allowed: {sorted(allowed)}",
                )
            )

    model = d.get("model")
    if model and model not in ALLOWED_MODELS:
        issues.append(ValidationIssue(path, "ERROR", f"Invalid model='{model}'. Allowed: {sorted(ALLOWED_MODELS)}"))

    source = d.get("source")
    if source and source not in ALLOWED_SOURCES:
        issues.append(ValidationIssue(path, "ERROR", f"Invalid source='{source}'. Allowed: {sorted(ALLOWED_SOURCES)}"))

    check("phase_of_flight", ALLOWED_PHASE)
    check("mission_profile", ALLOWED_MISSION)
    check("operation_type", ALLOWED_OPERATION)
    check("weather_category", ALLOWED_WEATHER)
    check("density_altitude_category", ALLOWED_DENSITY_ALT)
    check("maintenance_context", ALLOWED_MAINT_CONTEXT)
    check("recency_status", ALLOWED_RECENCY)
    check("total_time_band", ALLOWED_TOTAL_BAND)
    check("multi_time_band", ALLOWED_MULTI_BAND)
    check("time_in_type_band", ALLOWED_TYPE_BAND)
    check("prevention_category", ALLOWED_PREVENTION_CATEGORY)


def validate_year(path: Path, d: Dict[str, Any], issues: List[ValidationIssue]) -> None:
    y = d.get("year")
    if y is None or y == "":
        return
    try:
        yy = int(y)
        if yy < 1950 or yy > 2100:
            issues.append(ValidationIssue(path, "WARN", f"Suspicious year value: {yy}"))
    except Exception:
        issues.append(ValidationIssue(path, "ERROR", f"Year must be an integer. Got: {y!r}"))


def validate_booleans(path: Path, d: Dict[str, Any], issues: List[ValidationIssue]) -> None:
    # For accidents/incidents these should be present and parseable; for ASRS they may be omitted.
    # We won't error if absent; we WILL error if present but unparseable.
    for b in ["fatal", "serious_injury", "aircraft_destroyed"]:
        if b in d:
            parsed = to_bool_or_none(d.get(b))
            if parsed is None and d.get(b) not in (None, ""):
                issues.append(ValidationIssue(path, "ERROR", f"Field '{b}' must be boolean true/false if present."))


def validate_contributing_factors(path: Path, d: Dict[str, Any], issues: List[ValidationIssue]) -> None:
    cfs = d.get("contributing_factors")
    if cfs is None:
        return

    if isinstance(cfs, str):
        cfs_list = [cfs]
    elif isinstance(cfs, list):
        cfs_list = cfs
    else:
        issues.append(ValidationIssue(path, "ERROR", "contributing_factors must be a list (or single string)."))
        return

    # Normalize items
    cfs_list = [str(x).strip() for x in cfs_list if str(x).strip() != ""]

    if not cfs_list:
        issues.append(ValidationIssue(path, "ERROR", "contributing_factors is empty. Use 1–3 factors or ['unknown']."))
        return

    unknown_only = (len(cfs_list) == 1 and cfs_list[0] == "unknown")
    if not unknown_only and not (1 <= len(cfs_list) <= 3):
        issues.append(ValidationIssue(path, "ERROR", "contributing_factors must contain 1–3 items (or ['unknown'])."))

    # Validate keys
    for cf in cfs_list:
        if cf not in FACTOR_SET:
            issues.append(ValidationIssue(path, "ERROR", f"Unknown contributing factor key: '{cf}'"))

    # Guardrail: don't mix unknown with others
    if "unknown" in cfs_list and not unknown_only:
        issues.append(ValidationIssue(path, "ERROR", "Do not combine 'unknown' with other factors. Use ['unknown'] only."))

    # Warn if duplicates
    if len(set(cfs_list)) != len(cfs_list):
        issues.append(ValidationIssue(path, "WARN", "Duplicate entries found in contributing_factors."))


def validate_drive_path(path: Path, d: Dict[str, Any], issues: List[ValidationIssue]) -> None:
    p = d.get("drive_path")
    if not p:
        return
    s = str(p).strip()
    # Policy expects Drive-relative paths (no protocol)
    if s.startswith("http://") or s.startswith("https://"):
        issues.append(ValidationIssue(path, "ERROR", "drive_path must be a Drive-relative path, not a URL."))
    # Expected top-level folders per vault policy
    if not any(s.startswith(prefix) for prefix in ("01_NTSB/", "02_ASRS/", "03_FAA_Publications/", "04_International_Investigations/", "05_Evergreen_Pre2005/", "06_Archived_Queries/")):
        issues.append(
            ValidationIssue(
                path,
                "WARN",
                "drive_path does not start with a standard Evidence Vault prefix (01_NTSB/, 02_ASRS/, ...).",
            )
        )


def validate_downloaded_date_format(path: Path, d: Dict[str, Any], issues: List[ValidationIssue]) -> None:
    # Light validation: YYYY-MM-DD
    v = d.get("downloaded")
    if not v:
        return
    s = str(v).strip()
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", s):
        issues.append(ValidationIssue(path, "ERROR", f"downloaded must be YYYY-MM-DD. Got: {s!r}"))


def validate_event_type_format(path: Path, d: Dict[str, Any], issues: List[ValidationIssue]) -> None:
    # event_type should be machine-friendly (underscores). We warn only.
    v = d.get("event_type")
    if not v:
        return
    s = str(v).strip()
    if " " in s:
        issues.append(ValidationIssue(path, "WARN", "event_type contains spaces; prefer underscores (e.g., Loss_of_Control)."))


def validate_record(path: Path) -> List[ValidationIssue]:
    issues: List[ValidationIssue] = []
    try:
        d = load_front_matter(path)
    except Exception as ex:
        return [ValidationIssue(path, "ERROR", f"Failed to parse YAML front matter: {ex}")]

    validate_required_fields(path, d, issues)
    validate_event_id_matches_filename(path, d, issues)
    validate_enums(path, d, issues)
    validate_year(path, d, issues)
    validate_booleans(path, d, issues)
    validate_contributing_factors(path, d, issues)
    validate_drive_path(path, d, issues)
    validate_downloaded_date_format(path, d, issues)
    validate_event_type_format(path, d, issues)

    return issues


def collect_md_files(root: Path) -> List[Path]:
    return sorted([p for p in root.rglob("*.md") if p.is_file()])


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate structured event records (YAML front matter).")
    ap.add_argument(
        "--path",
        type=str,
        default="data/structured",
        help="Root folder to scan for .md records (default: data/structured)",
    )
    ap.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="Treat warnings as errors (nonzero exit if any WARN).",
    )
    args = ap.parse_args()

    repo_root = Path.cwd()
    scan_root = (repo_root / args.path).resolve()

    if not scan_root.exists():
        print(f"ERROR: Path does not exist: {scan_root}")
        return 2

    files = collect_md_files(scan_root)
    if not files:
        print(f"ERROR: No .md files found under: {scan_root}")
        return 3

    all_issues: List[ValidationIssue] = []
    for f in files:
        all_issues.extend(validate_record(f))

    errors = [i for i in all_issues if i.level == "ERROR"]
    warns = [i for i in all_issues if i.level == "WARN"]

    # Print grouped output
    if all_issues:
        by_file: Dict[Path, List[ValidationIssue]] = {}
        for issue in all_issues:
            by_file.setdefault(issue.path, []).append(issue)

        for f, issues in by_file.items():
            rel = f.relative_to(repo_root) if f.is_absolute() else f
            print(f"\n{rel}")
            for issue in issues:
                print(f"  {issue.level}: {issue.message}")

    # Summary
    print("\n---")
    print(f"Files scanned: {len(files)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warns)}")

    if errors:
        print("Validation FAILED (errors present).")
        return 1

    if args.warnings_as_errors and warns:
        print("Validation FAILED (warnings treated as errors).")
        return 1

    print("Validation PASSED.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
