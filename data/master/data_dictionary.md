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
Format: [Model]-[Source]-[Year]-[Sequential ID]
Example: C310-ACC-2012-001
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

operation_type
Type: categorical string
Allowed values:
91
135

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
Example: 1.3
Purpose: Indicates the record schema/taxonomy version used for this dataset row,
including required fields and controlled vocabularies (e.g., event_type list and
contributing factor taxonomy).
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
Commercial
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

density_altitude_category
Type: categorical string
Allowed values:
Low
Moderate
High
Extreme
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

Note (v1.3):
event_type was split into a controlled primary event_type and an optional event_subtype to reduce label drift.
Legacy compound values (e.g., "Loss_of_Control_Go_Around") must be migrated to:
event_type=Loss_of_Control, event_subtype=Go_Around.

event_type
Type: categorical string (controlled)
Allowed values:
Loss_of_Control
CFIT
Fuel_Starvation
Fuel_Exhaustion
Fire
Engine_Failure
Landing_Gear_Malfunction
Runway_Excursion
Hard_Landing
Midair_Collision
Ground_Collision
System_Malfunction
Other

Purpose:
Primary outcome class. Use the smallest stable vocabulary so counts do not fragment.

Rules:
- event_type must be one of the allowed values above.
- Do NOT encode phase of flight, weather, or mechanical trigger in event_type.
- Use machine-friendly underscores exactly as shown.

event_subtype
Type: categorical string (controlled, optional)
Allowed values:
Go_Around
Unstabilized_Approach
Rejected_Takeoff
Forced_Landing
Gear_Collapse
Gear_Up_Landing
Gear_Separation
Gear_Failure
Brake_Failure
Engine_Loss_Power
Engine_Fire
Bird_Strike
Unknown

Purpose:
Single modifier describing operational context or initiating trigger for the primary event_type.

Rules:
- event_subtype may be blank if no single modifier is clearly supported by the report.
- Only ONE value may be used (no lists, no compound strings).
- event_subtype must be one of the allowed values above; new values require schema change protocol.
- Do NOT duplicate event_type (e.g., don’t use Runway_Excursion as a subtype).


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
