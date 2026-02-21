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

### Version 1.3

Date: 2026-02-20
Scope: Schema refinement – Event classification structure
Applies To: All structured accident records

## Change Summary

- Split event_type into two controlled fields:
- event_type (primary outcome class – controlled vocabulary)
- event_subtype (single initiating trigger modifier – controlled vocabulary, optional)
- This change eliminates compound event labels (e.g., Loss_of_Control_Go_Around) and prevents fragmentation of primary event counts.

## Rationale

Under v1.2, event_type was functioning as both:

- A primary safety outcome classification
- A contextual/initiating modifier
- This resulted in compound strings encoding multiple dimensions (phase, trigger, outcome), which creates:

- Frequency fragmentation
- Reduced analytical clarity
- Increased risk of uncontrolled vocabulary drift
- Difficulty aggregating across models and years
- Splitting the field preserves:
- Stable primary outcome categories
- Analytical clarity
- Controlled dimensional separation
- Future scalability beyond 75+ records

## Structural Changes
1. event_type

Now restricted to controlled primary outcome list:

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

## Compound labels are no longer permitted.

2. New Field: event_subtype

Optional controlled modifier field.

Purpose:
Captures the single initiating trigger or procedural modifier most directly associated with the primary event.

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

## Rules:

- Only one subtype permitted.
- Must not duplicate event_type.
- Must not encode phase_of_flight.
- Must not encode weather_category.
- Blank allowed if no single trigger clearly supported.
- Expansion requires schema change protocol.

## Migration Rules (v1.2 → v1.3)

All legacy compound event_type values must be migrated:

Example:

Loss_of_Control_Go_Around
→ event_type: Loss_of_Control
→ event_subtype: Go_Around

Fuel_Starvation_Forced_Landing
→ event_type: Fuel_Starvation
→ event_subtype: Forced_Landing

Gear_Failure_Runway_Excursion
→ event_type: Landing_Gear_Malfunction
→ event_subtype: Gear_Failure

CFIT
→ event_type: CFIT
→ event_subtype: blank

# All records must:

- Update taxonomy_version to 1.3
- Pass updated validator
- Rebuild master dataset

# Backward Compatibility

- v1.2 structured files are not compliant with v1.3 until migrated.
- Master dataset must not mix taxonomy versions.
- Expected Analytical Impact
- Reduced event label fragmentation
- Cleaner frequency aggregation
- Improved co-occurrence analysis with contributing factors
- More stable cross-model comparison once dataset maturity gates are met