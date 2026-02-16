# Contributing Factor Taxonomy Change Log

This document records all formal modifications to the contributing-factor taxonomy
used in the Twin Cessna Safety Data & Research Project.

The purpose of this log is to:

- Prevent silent coding drift
- Preserve analytical continuity
- Ensure reproducibility of findings
- Document rationale for taxonomy evolution

All structured event records must include:
taxonomy_version: X.X

If a taxonomy revision materially alters definitions or factor structure,
prior records must be reviewed and re-coded if necessary.

---

## Version 1.0
Adopted: 2026-02-20
Status: Initial Baseline

### Summary

Version 1.0 establishes the initial contributing-factor framework
for fleet-wide twin Cessna analysis (C310, C320, C340, C402, C414, C421).

This version introduces four major contributing-factor domains:

1. Human / Cognitive
2. Maintenance / Mechanical
3. Performance / Operational
4. Experience-Related

Each event may include 1–3 primary contributing factors.
"Unknown" may be used when evidence is insufficient.

Boolean columns are used in master datasets for analytical clarity.

---

### Factor Definitions – Version 1.0

#### Human / Cognitive

normalization_of_deviance  
Gradual acceptance of degraded conditions or procedural shortcuts as normal.

assumption_of_performance  
Implicit belief that aircraft performance margins exist without verification.

plan_continuation_bias  
Continuation of original plan despite emerging cues suggesting revision.

checklist_non_compliance  
Failure to follow written checklist procedures when required.

task_saturation  
Cognitive overload resulting in degraded decision quality.

low_light_conditions
Poor visibility during dusk or sunrise leading to impact or pilot error

---

#### Maintenance / Mechanical

aging_aircraft_degradation  
Failure attributable to wear, corrosion, or time-related deterioration.

incomplete_troubleshooting  
Partial or insufficient diagnostic effort preceding mechanical failure.

deferred_discrepancy_normalization  
Acceptance of unresolved mechanical discrepancies as operationally acceptable.

maintenance_induced_failure  
Failure directly attributable to maintenance error or improper installation.

---

#### Performance / Operational

weight_balance_misjudgment  
Incorrect loading or CG miscalculation affecting performance or controllability.

density_altitude_underestimation  
Failure to account adequately for high DA performance penalties.

single_engine_performance_assumption  
Incorrect assumption of climb or controllability margins following engine failure.

icing_performance_degradation  
Failure to adequately account for aerodynamic or performance penalties due to icing.

---

#### Experience-Related

low_time_in_type  
Limited familiarity with aircraft type contributing to degraded decision-making.

high_time_complacency  
Overconfidence associated with extensive experience reducing vigilance.

lapsed_recency  
Expired currency or insufficient recent experience affecting performance.

informal_or_incomplete_training  
Non-standardized or insufficient training in systems or emergency procedures.

---

#### Unknown

unknown  
Used only when evidence does not allow reasonable attribution to other categories.

---

### Structural Rules Established in v1.0

- Maximum of three primary contributing factors per event.
- Accident, Incident, and ASRS datasets remain separate.
- Boolean factor columns in master CSV.
- Free-text prevention_summary allowed but not used for coding.
- No rate inference without exposure data.

---

### Known Limitations in v1.0

- Human factors may overlap conceptually (e.g., task_saturation vs plan_continuation_bias).
- Aging_aircraft_degradation may require refinement if recurring subsystem patterns emerge.
- High_time_complacency requires careful application to

### Observation – Environmental / Wildlife Events

During coding of C310-ACC-2006-001 (CHI06LA060), no existing contributing factor category adequately captured wildlife strike–initiated accidents resulting in secondary system failures.

No taxonomy change made at this time. Monitor for recurrence threshold (≥3 similar events).

---

### Observation – Airspeed Management Cases

Takeoff stall case (C310-ACC-2006-004) revealed that current taxonomy does not explicitly include an airspeed management or pitch control factor. For now, coded under assumption_of_performance. Monitor recurrence before adding new factor.

---

### Version 1.1 – Added "Commercial" as allowed value for mission_profile.

Rationale: Distinguish Part 135 and revenue operations from owner-flown Part 91 flights to enable comparative analysis of operational context.

 ---

 ### Version 1.2 – Added Operation_Type and Density_Altitude_Category as required fields.

Rationale: Formally Distinguish Part 135 and revenue operations from owner-flown Part 91 flights to enable comparative analysis of operational context. Add context for Density Altitude for additional analysis. 

Updated all structured accident files to new taxonomy, validator and build files to match. 

 ---