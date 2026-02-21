#!/usr/bin/env python3
"""
One-time migration helper: split legacy/compound event_type into v1.3
event_type (primary) + event_subtype (optional, single modifier).

What it does:
- Scans .md record files with YAML front matter.
- Ensures 'event_subtype' key exists (blank by default).
- Migrates compound/legacy event_type strings using:
  1) explicit mapping table (high confidence)
  2) safe heuristics (only when unambiguous)
- Optionally sets taxonomy_version to 1.3
- Writes updated files with a .bak backup (only with --apply)

Usage (from repo root):
  python3 analysis/scripts/migrate_event_type_v13.py --path data/structured/accidents
  python3 analysis/scripts/migrate_event_type_v13.py --path data/structured/accidents --apply --set-taxonomy

Notes:
- Default mode is DRY RUN (no writes).
- This script is intentionally conservative: if it can't safely map, it reports "NEEDS_REVIEW".
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any, Dict, Tuple, List

import yaml

RE_FRONT_MATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# v1.3 controlled vocabularies (must match validator/data_dictionary)
ALLOWED_EVENT_TYPE_V13 = {
    "Loss_of_Control",
    "CFIT",
    "Fuel_Starvation",
    "Fuel_Exhaustion",
    "Fire",
    "Engine_Failure",
    "Landing_Gear_Malfunction",
    "Runway_Excursion",
    "Hard_Landing",
    "Midair_Collision",
    "Ground_Collision",
    "System_Malfunction",
    "Other",
}

ALLOWED_EVENT_SUBTYPE_V13 = {
    "Go_Around",
    "Unstabilized_Approach",
    "Rejected_Takeoff",
    "Forced_Landing",
    "Gear_Collapse",
    "Gear_Up_Landing",
    "Gear_Separation",
    "Gear_Failure",
    "Brake_Failure",
    "Engine_Loss_Power",
    "Engine_Fire",
    "Bird_Strike",
    "Unknown",
}

# --- High-confidence explicit mappings for known legacy compounds ---
# Add to this list as you encounter real legacy labels in your repo.
EXPLICIT_EVENT_MAP: Dict[str, Tuple[str, str]] = {
    # LOC compounds
    "Loss_of_Control_Go_Around": ("Loss_of_Control", "Go_Around"),
    "Unstabilized_Approach_Loss_of_Control": ("Loss_of_Control", "Unstabilized_Approach"),
    "Icing_Stall_Terrain_Impact": ("Loss_of_Control", "Unknown"),  # If you know it's icing-driven, change to ("Loss_of_Control","Unknown")? Keep conservative.

    # Fuel compounds
    "Fuel_Starvation_Forced_Landing": ("Fuel_Starvation", "Forced_Landing"),
    "Fuel_Exhaustion_Forced_Landing": ("Fuel_Exhaustion", "Forced_Landing"),

    # Gear compounds
    "Gear_Failure_Runway_Excursion": ("Landing_Gear_Malfunction", "Gear_Failure"),
    "Gear_Separation_Runway_Excursion": ("Landing_Gear_Malfunction", "Gear_Separation"),
    "Landing_Gear_Collapse": ("Landing_Gear_Malfunction", "Gear_Collapse"),
    "Gear_Collapse": ("Landing_Gear_Malfunction", "Gear_Collapse"),
    "Gear_Up_Landing": ("Landing_Gear_Malfunction", "Gear_Up_Landing"),

    # Ground/taxi collisions
    "Taxi_Collision_Object": ("Ground_Collision", "Unknown"),
    "Taxi_Collision": ("Ground_Collision", "Unknown"),

    # Misc patterns often used
    "Rejected_Takeoff": ("Runway_Excursion", "Rejected_Takeoff"),  # if you used RTO as primary; review if needed
}

# --- Heuristic keywords to primary event types (conservative) ---
GEAR_TOKENS = {"Gear", "Landing_Gear", "Gear_Failure", "Gear_Separation", "Gear_Collapse", "Gear_Up"}


def load_front_matter(path: Path) -> Tuple[Dict[str, Any], str, str]:
    """
    Returns (yaml_dict, front_matter_text, body_text).
    """
    text = path.read_text(encoding="utf-8")
    m = RE_FRONT_MATTER.search(text)
    if not m:
        raise ValueError("Missing YAML front matter (--- ... ---)")

    fm_text = m.group(1)
    body = text[m.end() :]
    data = yaml.safe_load(fm_text) or {}
    if not isinstance(data, dict):
        raise ValueError("Front matter YAML did not parse to a dict.")
    return data, fm_text, body


def dump_front_matter(d: Dict[str, Any]) -> str:
    # Keep order as inserted; avoid YAML anchors; prefer block style
    return yaml.safe_dump(d, sort_keys=False).strip()


def ensure_event_subtype_key(d: Dict[str, Any]) -> None:
    if "event_subtype" not in d:
        d["event_subtype"] = ""  # schema-stable but optional value


def safe_norm(s: Any) -> str:
    if s is None:
        return ""
    return str(s).strip()


def migrate_event_fields(d: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Mutates d in-place.
    Returns (changed, status), where status is one of:
      - "OK"
      - "OK_EXPLICIT"
      - "OK_HEURISTIC"
      - "NEEDS_REVIEW"
      - "SKIP_NO_EVENT"
    """
    ensure_event_subtype_key(d)

    et_raw = safe_norm(d.get("event_type"))
    es_raw = safe_norm(d.get("event_subtype"))

    if not et_raw:
        return False, "SKIP_NO_EVENT"

    # Already v1.3 compliant primary event type?
    if et_raw in ALLOWED_EVENT_TYPE_V13:
        # If subtype exists and is nonblank, validate it lightly; else keep as-is
        if es_raw and es_raw not in ALLOWED_EVENT_SUBTYPE_V13:
            # don't change, but flag
            return False, "NEEDS_REVIEW"
        return False, "OK"

    # Explicit map first
    if et_raw in EXPLICIT_EVENT_MAP:
        new_et, new_es = EXPLICIT_EVENT_MAP[et_raw]
        d["event_type"] = new_et
        # Only overwrite subtype if blank (avoid stomping a manual fix)
        if not es_raw:
            d["event_subtype"] = new_es if new_es != "Unknown" else ""
        return True, "OK_EXPLICIT"

    # Heuristic: try to split by trailing subtype token (last underscore group)
    # Example: Loss_of_Control_Go_Around -> primary Loss_of_Control, subtype Go_Around
    parts = et_raw.split("_")
    if len(parts) >= 2:
        candidate_sub = parts[-2] + "_" + parts[-1] if (parts[-2] + "_" + parts[-1]) in ALLOWED_EVENT_SUBTYPE_V13 else parts[-1]
        if candidate_sub in ALLOWED_EVENT_SUBTYPE_V13:
            # Determine how many tokens to drop
            drop = 2 if (parts[-2] + "_" + parts[-1]) == candidate_sub else 1
            candidate_primary = "_".join(parts[:-drop])
            if candidate_primary in ALLOWED_EVENT_TYPE_V13:
                d["event_type"] = candidate_primary
                if not es_raw:
                    d["event_subtype"] = candidate_sub
                return True, "OK_HEURISTIC"

    # Heuristic: gear-related strings -> Landing_Gear_Malfunction if unambiguous
    if any(tok in et_raw for tok in ("Gear", "Landing_Gear")):
        # pick best subtype if present in string
        sub = ""
        for s in ("Gear_Up_Landing", "Gear_Separation", "Gear_Collapse", "Gear_Failure"):
            if s in et_raw and s in ALLOWED_EVENT_SUBTYPE_V13:
                sub = s
                break
        d["event_type"] = "Landing_Gear_Malfunction"
        if not es_raw and sub:
            d["event_subtype"] = sub
        # If no subtype, leave blank—still better than a drifting primary
        return True, "OK_HEURISTIC"

    # Heuristic: fuel starvation/exhaustion embedded
    if "Fuel_Starvation" in et_raw:
        d["event_type"] = "Fuel_Starvation"
        if not es_raw and "Forced_Landing" in et_raw:
            d["event_subtype"] = "Forced_Landing"
        return True, "OK_HEURISTIC"
    if "Fuel_Exhaustion" in et_raw:
        d["event_type"] = "Fuel_Exhaustion"
        if not es_raw and "Forced_Landing" in et_raw:
            d["event_subtype"] = "Forced_Landing"
        return True, "OK_HEURISTIC"

    # Heuristic: LOC embedded
    if "Loss_of_Control" in et_raw or et_raw.startswith("LOC"):
        d["event_type"] = "Loss_of_Control"
        # only set subtype if we see a known one
        if not es_raw:
            if "Go_Around" in et_raw:
                d["event_subtype"] = "Go_Around"
            elif "Unstabilized" in et_raw:
                d["event_subtype"] = "Unstabilized_Approach"
        return True, "OK_HEURISTIC"

    # If we got here, we don't trust a mapping
    return False, "NEEDS_REVIEW"


def write_back(path: Path, d: Dict[str, Any], body: str) -> None:
    new_fm = dump_front_matter(d)
    out = f"---\n{new_fm}\n---\n{body}"
    path.write_text(out, encoding="utf-8")


def collect_md_files(root: Path) -> List[Path]:
    return sorted([p for p in root.rglob("*.md") if p.is_file()])


def main() -> int:
    ap = argparse.ArgumentParser(description="Migrate event_type -> (event_type, event_subtype) for v1.3.")
    ap.add_argument(
        "--path",
        type=str,
        default="data/structured",
        help="Root folder to scan for .md records (default: data/structured)",
    )
    ap.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to files (creates .bak backups). Default is dry-run.",
    )
    ap.add_argument(
        "--set-taxonomy",
        action="store_true",
        help="Also set taxonomy_version to '1.3' when writing.",
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

    changed = 0
    needs_review: List[Path] = []
    skipped = 0

    print(f"{'APPLY' if args.apply else 'DRY RUN'} — scanning {len(files)} files under {scan_root}\n")

    for f in files:
        try:
            d, _fm_text, body = load_front_matter(f)
        except Exception as ex:
            print(f"[ERROR] {f}: {ex}")
            needs_review.append(f)
            continue

        before_et = safe_norm(d.get("event_type"))
        before_es = safe_norm(d.get("event_subtype"))

        did_change, status = migrate_event_fields(d)

        # Optionally set taxonomy_version
        if args.set_taxonomy:
            tv = safe_norm(d.get("taxonomy_version"))
            if tv != "1.3":
                d["taxonomy_version"] = "1.3"
                did_change = True

        after_et = safe_norm(d.get("event_type"))
        after_es = safe_norm(d.get("event_subtype"))

        # Report only when interesting
        if status == "SKIP_NO_EVENT":
            skipped += 1
            continue

        if status == "NEEDS_REVIEW":
            needs_review.append(f)

        if did_change:
            changed += 1
            rel = f.relative_to(repo_root) if f.is_absolute() else f
            print(f"[{status}] {rel}")
            print(f"  event_type:    {before_et!r} -> {after_et!r}")
            print(f"  event_subtype: {before_es!r} -> {after_es!r}")

            if args.apply:
                bak = f.with_suffix(f.suffix + ".bak")
                if not bak.exists():
                    bak.write_text(f.read_text(encoding="utf-8"), encoding="utf-8")
                write_back(f, d, body)

    print("\n---")
    print(f"Files scanned:     {len(files)}")
    print(f"Files changed:     {changed}")
    print(f"Files skipped:     {skipped}")
    print(f"Needs review:      {len(needs_review)}")

    if needs_review:
        print("\nNEEDS_REVIEW list:")
        for p in needs_review:
            rel = p.relative_to(repo_root) if p.is_absolute() else p
            print(f"  - {rel}")

    if args.apply:
        print("\nDone. Re-run validate_records.py after this migration.")
    else:
        print("\nDry run only. Re-run with --apply to write changes (backups will be created).")

    # Return nonzero if review needed (useful in CI)
    return 1 if needs_review else 0


if __name__ == "__main__":
    raise SystemExit(main())
