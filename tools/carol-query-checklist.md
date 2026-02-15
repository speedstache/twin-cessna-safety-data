# NTSB CAROL Query Checklist
## Twin Cessna Safety Data & Research Project

This document defines the standardized procedure for retrieving
Twin Cessna accident data from the NTSB CAROL system.

Every bulk data pull must follow this checklist.

All exports must be archived in:

06_Archived_Queries/CAROL_Exports/

---

# 1. Access Point

Website:
https://data.ntsb.gov/carol-main-public/

Dataset:
Aviation Accident & Incident Data

Do NOT use:
- Media summaries
- Secondary search tools
- Third-party aggregators

Only official NTSB CAROL database is permitted.

---

# 2. Baseline Query Configuration (Phase 1)

### 2.1 Event Type Filter

Event Type:
☑ Accident
☐ Incident (exclude for Phase 1)

Rationale:
Accident dataset remains separate from Incident and ASRS datasets.

---

### 2.2 Date Range

Start Date:
01/01/2006

End Date:
Current Date

Rationale:
Primary 20-year analysis window.
If extended backward, document justification in weekly-progress.md.

---

### 2.3 Aircraft Make

Make:
Cessna

Important:
Do not rely solely on Make filter — must also filter by model.

---

### 2.4 Aircraft Model (Add Individually)

Add each model separately:

Model contains:
310
320
340
402
414
421

Important:
Confirm turbine models (e.g., 425, 441) are NOT included.

If model search returns mixed turbine results:
Manually review and exclude.

---

### 2.5 Operation Type (If Available)

If CAROL provides operational filter:

Include:
Part 91

Exclude:
Part 135 commuter operations (when clearly identifiable)

If unclear:
Include initially and flag for review during coding.

Do NOT exclude based on assumption.

---

### 2.6 Aircraft Category

If available:
Select Airplane.

Do not restrict further unless necessary.

---

# 3. Output Configuration

Before exporting:

Ensure the following fields are included in export:

- Event ID
- Accident Number
- Event Date
- Location (City, State)
- Aircraft Make
- Aircraft Model
- Registration
- Injury Severity
- Aircraft Damage
- Phase of Flight (if available)
- Operation Type
- FAR Description
- Weather Condition

If custom field selection is available:
Select all relevant descriptive fields.

---

# 4. Export Procedure

Step 1:
Run query.

Step 2:
Review top and bottom of result set to confirm:
- No turbine aircraft included.
- No Caravan or Citation entries.
- Models correctly match piston twin types.

Step 3:
Export results as CSV.

Step 4:
Name file:

CAROL_ACC_TwinCessna_2006-Present_<YYYY-MM-DD>.csv

Example:
CAROL_ACC_TwinCessna_2006-Present_2026-02-21.csv

Step 5:
Store in:

06_Archived_Queries/CAROL_Exports/

---

# 5. Query Documentation

Immediately after export, record:

Query Date:
YYYY-MM-DD

Date Range Used:
Start – End

Models Included:
[List explicitly]

Total Records Returned:
[Count]

Notes:
- Any anomalies?
- Any model imbalance?
- Any unexpected aircraft types?

Record this in weekly-progress.md.

---

# 6. Selection for Coding

From exported dataset:

Select first 25 qualifying events
for Phase 1 sprint, ensuring:

- Model diversity where possible
- Phase-of-flight diversity
- Mixture of fatal and non-fatal accidents

Selection criteria must be documented.

Do NOT cherry-pick based on narrative interest.

---

# 7. Verification Step

Before beginning coding:

Randomly open 3 exported records in CAROL
and confirm they match the CSV export.

If discrepancies exist:
Repeat export.

---

# 8. Version Control Rule

Every time a new CAROL query is executed:

- Archive CSV
- Log query parameters
- Do NOT overwrite prior exports
- Treat each export as immutable

---

# 9. Red Flags Requiring Pause

Stop and reassess if:

- >20% of returned aircraft are turbine variants.
- Operation types appear dominated by commuter operations.
- Unexpected aircraft models appear repeatedly.
- Date range produces unusually small or unusually large dataset.

Document findings before proceeding.

---

# 10. Reproducibility Standard

A query is considered reproducible if:

- Another analyst can run the same filters
- Same date range used
- Same model filters applied
- Result count is materially similar
- Export file exists in archive

If any of these fail, the query is invalid.

---

# Reminder

CAROL defines the boundary of the accident universe.

If the boundary shifts,
the dataset shifts,
and conclusions shift.

Query discipline is foundational.
