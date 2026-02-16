🛩 Twin Cessna Accident Coding Checklist

v1.1 – YAML Workflow with Standardized Time Bands

One aircraft = one file
Max 3 contributing factors
No guessing. No hindsight.
Unknown is acceptable. Guessing is not.

STEP 0 — Create Record
python analysis/scripts/make_blank_record.py --model C310 --year 2006 --report-number ERA23LA018


Open the generated file.

STEP 1 — Metadata Sweep (2–3 minutes)

Fill only what is explicitly stated in the report.

Identification

 model + variant

 engine_type

 year correct

 operation_type (91 / 135 / Unknown)

 confirm drive_path

 source (usually NTSB)

Context

 phase_of_flight

 mission_profile

 weather_category (VMC / IMC / Unknown)

 density_altitude_category (if mentioned)

 maintenance_context (if relevant)

Injury & Damage

 fatal true/false

 serious_injury true/false

 aircraft_destroyed true/false

If not explicitly stated → use Unknown or false.
Do not infer.

STEP 2 — Pilot Bands (2 minutes)

Convert documented numbers into standardized bands.

If not stated → Unknown.

Total Time Band (total_time_band)
Reported Hours	Code As
< 500	<500
500–1999	500-2000
2000–4999	2000-5000
≥ 5000	5000+
Not stated	Unknown
Multi-Engine Time Band (multi_time_band)
Reported Hours	Code As
< 100	<100
100–499	100-500
500–1999	500-2000
≥ 2000	2000+
Not stated	Unknown
Time in Type Band (time_in_type_band)
Reported Hours	Code As
< 50	<50
50–199	50-200
200–999	200-1000
≥ 1000	1000+
Not stated	Unknown
Recency Status (recency_status)

Only code if explicitly supported in the report.

Allowed values:

Current

Lapsed

Unknown

Do not infer from total time.

STEP 3 — Event Classification (1 minute)

 event_type selected

 matches primary failure mode

 not over-specified

Keep it simple and aligned with validator expectations.

STEP 4 — Contributing Factors (Critical Step)

Maximum: 3

If unsure → unknown

Evidence Rule

Can you point to a sentence in the report supporting this factor?

If no → do not code it.

Human Factors

normalization_of_deviance

Chronic workaround

Repeated informal behavior documented

assumption_of_performance

Assumed capability without verification

plan_continuation_bias

Continued despite worsening conditions

checklist_noncompliance

Checklist skipped or incomplete

task_saturation

High workload or distraction documented

Maintenance Factors

aging_aircraft_degradation

Wear, corrosion, fatigue documented

maintenance_induced_failure

Improper installation or assembly

incomplete_troubleshooting

Root cause not identified before return to service

deferred_discrepancy_normalization

Known issue repeatedly deferred

Performance Factors

weight_balance_misjudgment

CG or loading error documented

density_altitude_underestimation

Density altitude explicitly cited

single_engine_performance_assumption

Assumed engine-out climb capability

icing_performance_degradation

Icing reduced performance

Experience Factors

low_time_in_type

Low model time supported by report

high_time_complacency_risk

Only if supported by findings

lapsed_recency

Currency lapse documented

informal_or_incomplete_training

Training deficiency documented

If none clearly supported:

contributing_factors:
  - unknown


Unknown is acceptable.
Guessing is not.

STEP 5 — Prevention Summary (1–2 minutes)

One operational sentence.

Focus on leverage point.

Not:

“Pilot should have…”

Instead:

“Emphasize verified performance calculations before engine-out departure decisions.”

STEP 6 — Narrative (5–10 factual sentences)

Rules:

Only facts from report

No speculation

No hindsight bias

No moral language

No “should have”

Neutral and precise.

STEP 7 — Self Audit (30 seconds)

 ≤ 3 contributing factors

 All factors supported by report

 No narrative speculation

 operation_type not assumed

 Time bands correctly mapped

 Unknown used only when necessary

STEP 8 — Validate
python analysis/scripts/validate_records.py
python analysis/scripts/build_master.py


Fix any errors immediately.

STEP 9 — Governance Pulse (Every 5–10 Records)
python analysis/scripts/unknown_monitor.py --csv data/master/accidents_master.csv


Monitor:

Unknown factor rate

Factor consistency

Dataset growth

Discipline Rule

When torn between two factors:

Choose the one with explicit report support.
If neither is explicit → unknown.

Consistency > speed
Restraint > cleverness
Signal > storytelling