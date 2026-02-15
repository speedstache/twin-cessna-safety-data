# Next Data Pull Plan
## Phase 1 – Initial 25 Accident Events

---

# Objective

Acquire the first 25 NTSB accident events
covering Twin Cessna piston models (C310, C320, C340, C402, C414, C421)
within the primary 20-year analysis window.

This pull is designed to stress-test Taxonomy v1.0
across multiple hazard types and flight phases.

This is not a comprehensive pull.
It is a controlled initial dataset.

---

# Data Source

Primary:
NTSB CAROL Query System

Dataset:
Aviation Accident & Incident Data

---

# Aircraft Filters

Aircraft Make:
Cessna

Aircraft Model (exact matches where available):

310
320
340
402
414
421

Exclude:
- Caravan (208)
- Citation series
- Turbine conversions unless clearly piston-based

---

# Operational Filter

Prefer:
Part 91 operations

Exclude where identifiable:
Scheduled Part 135 commuter operations

If operational classification is unclear:
Include initially and flag for later review.

---

# Time Window

Primary window:
2006–Present

If insufficient representation for a model:
Extend backward selectively (document if done).

---

# Event Type

Accidents only.

Exclude incidents for this pull.
Exclude ASRS for this pull.

Accident and ASRS datasets must remain separate.

---

# Diversity Targets (Phase 1 Stress Test)

Within first 25 selected events, aim to include:

- ≥2 engine failure events
- ≥2 takeoff / initial climb loss-of-control events
- ≥2 approach / landing instability or LOC events
- ≥2 maintenance-related failure events
- ≥2 high density altitude cases
- ≥2 icing-related events

This ensures taxonomy exposure to varied chains.

This is a diversity target, not a hard rule.

---

# Selection Method

Step 1:
Run CAROL query with model filters and date range.

Step 2:
Export CSV results.

Step 3:
Archive export in:
06_Archived_Queries/CAROL_Exports/

Step 4:
Select first 25 qualifying events,
ensuring model distribution where possible.

Document any model imbalance.

---

# Evidence Intake Checklist (Per Event)

For each selected event:

1. Download final report PDF.
2. Download docket if available and relevant.
3. Store in:
   01_NTSB/<Model>/<Year>/
4. Confirm report_number matches filename.
5. Record download date in structured YAML.
6. Do NOT begin coding until all 25 reports are downloaded.

---

# Expected Deliverables From This Pull

- 25 raw NTSB accident reports stored in Drive
- 1 archived CAROL export
- No structured records yet

Coding begins only after evidence intake is complete.

---

# Risks

Risk 1:
Unintentional inclusion of commuter/Part 135 patterns.

Mitigation:
Flag such events during coding for possible exclusion later.

Risk 2:
Overrepresentation of one model (e.g., C310).

Mitigation:
Attempt balanced selection where feasible.

Risk 3:
Early bias toward dramatic fatal accidents.

Mitigation:
Include non-fatal accidents to balance severity spectrum.

---

# Completion Criteria

This data pull is complete when:

- 25 accident reports are stored in Drive
- CAROL export archived
- Model distribution documented
- Evidence intake checklist complete for all events

Only then does Phase 1 structured coding begin.
