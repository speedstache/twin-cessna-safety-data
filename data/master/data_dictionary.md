# Twin Cessna Safety Project
## Master Dataset Data Dictionary

This document defines the structure, allowable values, and usage rules
for the master datasets:

- accident_master.csv
- incident_master.csv
- asrs_master.csv

Each row represents:
One aircraft, one occurrence.

Structured event records in data/structured/ are the source of truth.
Master CSV files are generated from those records via script.

---

# SECTION 1 — IDENTIFICATION FIELDS

event_id
Type: string
Format: [Model]-[Source]-[Year]-[State]-[Sequential ID]
Example: C310-ACC-2012-FL-001
Purpose: Unique identifier for each aircraft occurrence.

model
Type: categorical string
Allowed values:
C310
C320
C340
C402
C414
C421
Purpose: Aircraft model family.

variant
Type: string
Example: Q, A, B, C
May be "UNK" if unknown.

engine_type
Type: string
Example: IO-470, TSIO-520
May be "UNK" if not specified.

year
Type: integer
Range: 1950–present
Purpose: Year of occurrence.

state
Type: string (2-letter code)
Example: FL, TX, CA
Use "UNK" if not known (primarily ASRS).

country
Type: string
Default: USA
Used for international comparison cases.

source
Type: categorical string
Allowed values:
NTSB
ASRS
FAA
Other
Purpose: Identifies originating dataset.

report_number
Type: string
NTSB: ERA12FA123
ASRS: ASRS_178901
Purpose: Traceability to raw evidence.

drive_path
Type: string
Relative path within Evidence Vault.
Example:
01_NTSB/C340/2018/CEN18FA234.pdf
Purpose: Direct evidence linkage.

downloaded
Type: date (YYYY-MM-DD)
Purpose: Audit trail for evidence acquisition.

taxonomy_version
Type: string
Example: 1.0
Purpose: Indicates contributing-factor schema version used.

---

# SECTION 2 — CONTEXT FIELDS

phase_of_flight
Type: categorical string
Allowed values:
Takeoff
Initial_Climb
Cruise
Descent
Approach
Landing
Go_Around
Taxi
Unknown

mission_profile
Type: categorical string
Allowed values:
Personal
Business
Training
Ferry
Maintenance_Flight
Unknown

weather_category
Type: categorical string
Allowed values:
VMC
IMC
Night
Icing
High_DA
Mixed
Unknown

maintenance_context
Type: categorical string
Allowed values:
Recent_Work
Deferred
None_Noted
Unknown

---

# SECTION 3 — PILOT EXPERIENCE FIELDS

total_time_band
Type: categorical string
Allowed values:
<500
500-1500
1500-5000
>5000
Unknown

multi_time_band
Type: categorical string
Same banding as total_time_band.

time_in_type_band
Type: categorical string
Allowed values:
<50
50-200
200-1000
>1000
Unknown

recency_status
Type: categorical string
Allowed values:
Current
Lapsed
Unknown

---

# SECTION 4 — OUTCOME FIELDS

event_type
Type: categorical string
Examples:
Loss_of_Control
Engine_Failure
Runway_Excursion
Fuel_Exhaustion
Rejected_Takeoff
Unstable_Approach
Icing_Encounter
Brake_System_Malfunction

Machine-friendly format (use underscores).

fatal
Type: boolean
TRUE or FALSE
ASRS: leave blank.

serious_injury
Type: boolean
TRUE or FALSE
ASRS: leave blank.

aircraft_destroyed
Type: boolean
TRUE or FALSE
ASRS: leave blank.

Purpose:
Separates severity from contributing factors.

---

# SECTION 5 — PREVENTION FIELDS

prevention_category
Type: categorical string
Suggested values:
Training
Maintenance
SOP
Equipment
Awareness
Unknown

prevention_summary
Type: short text
1–2 sentence description of interruptible prevention leverage.
Not used for coding.

---

# SECTION 6 — CONTRIBUTING FACTOR FIELDS

Each factor is stored as a boolean column:

TRUE = factor present
FALSE = factor not coded

Maximum of three primary factors per event.
"cf_unknown" may be TRUE if insufficient evidence exists.

Human / Cognitive

cf_normalization_of_deviance
cf_assumption_of_performance
cf_plan_continuation_bias
cf_checklist_non_compliance
cf_task_saturation

Maintenance / Mechanical

cf_aging_aircraft_degradation
cf_incomplete_troubleshooting
cf_deferred_discrepancy_normalization
cf_maintenance_induced_failure

Performance / Operational

cf_weight_balance_misjudgment
cf_density_altitude_underestimation
cf_single_engine_performance_assumption
cf_icing_performance_degradation

Experience-Related

cf_low_time_in_type
cf_high_time_complacency
cf_lapsed_recency
cf_informal_or_incomplete_training

Unknown

cf_unknown

---

contributing_factors_raw
Type: string
Comma-separated factor keys as originally coded.
Example:
single_engine_performance_assumption,low_time_in_type

Purpose:
Traceability to structured record YAML.

---

# SECTION 7 — STRUCTURAL RULES

1. One aircraft, one occurrence = one row.
2. Accident, Incident, and ASRS datasets remain separate.
3. Boolean factor columns must align with taxonomy version.
4. No free-text categorical drift allowed.
5. Schema changes require taxonomy-change-log update.
6. No accident rate inference without verified exposure data.

---

# SECTION 8 — ANALYTICAL PRINCIPLES

The dataset is structured to allow:

- Phase-of-flight clustering
- Cross-model comparisons
- Co-occurring factor analysis
- Severity vs frequency separation
- Precursor (ASRS) alignment analysis

This dataset does not:

- Support exposure-adjusted rate calculation
- Infer causation from correlation
- Replace original investigation findings

---

# PRIMARY RESEARCH QUESTION

“What specific, repeatable hazards across Twin Cessna operations are most likely to be mitigated through better standardization, training, or maintenance practices?”

All analysis derived from this dataset must support answering this question.
