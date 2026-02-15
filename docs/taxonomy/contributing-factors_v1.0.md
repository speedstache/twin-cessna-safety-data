# Contributing Factor Taxonomy
## Version 1.0

Adopted: 2026-02-20  
Status: Active Baseline

---

# 1. Purpose

This document defines the official contributing-factor taxonomy used
in the Twin Cessna Safety Data & Research Project.

The taxonomy exists to:

- Standardize event coding
- Enable cross-model comparison
- Support co-occurrence analysis
- Prevent subjective drift
- Maintain analytical reproducibility

Each event record must include:

taxonomy_version: 1.0

No contributing factor may be used unless defined in this document.

---

# 2. Structural Rules

1. Maximum of three primary contributing factors per event.
2. At least one factor must be assigned unless explicitly coded as "unknown".
3. Factors must be supported by documented evidence or strong factual indication.
4. Contributing factors are not equivalent to official probable cause statements.
5. Severity (fatalities, destruction) is stored separately from contributing factors.

---

# 3. Taxonomy Domains

Version 1.0 includes four major domains:

1. Human / Cognitive
2. Maintenance / Mechanical
3. Performance / Operational
4. Experience-Related

These domains are analytical groupings and are not coded as dataset columns.
Only individual factors are coded.

---

# 4. Factor Definitions (v1.0)

---

## HUMAN / COGNITIVE

### normalization_of_deviance

Definition:
Gradual acceptance of degraded conditions, procedural shortcuts, or abnormal indications as normal.

Indicators:
- Known recurring discrepancy tolerated
- Repeated informal procedural deviation
- Deferred item treated as routine

Exclusions:
- One-time omission (see checklist_non_compliance)

---

### assumption_of_performance

Definition:
Implicit belief that adequate aircraft performance margins exist without verification.

Indicators:
- No documented performance calculation
- Overreliance on past experience
- Departure or climb attempted without confirming margins

Exclusions:
- Explicit performance miscalculation (see density_altitude_underestimation or weight_balance_misjudgment)

---

### plan_continuation_bias

Definition:
Continuation of original plan despite emerging cues that warrant revision.

Indicators:
- Continuing approach below stabilized criteria
- Continuing flight into worsening weather
- Continuing into icing without exit planning

Exclusions:
- Pure cognitive overload without clear cue recognition (see task_saturation)

---

### checklist_non_compliance

Definition:
Failure to follow written checklist procedures when required.

Indicators:
- Omitted checklist item
- Improper configuration documented
- Missed emergency procedure steps

Exclusions:
- Situations where no checklist existed

---

### task_saturation

Definition:
Cognitive overload resulting in degraded situational awareness or decision quality.

Indicators:
- Multiple simultaneous failures
- High workload environment (IMC, engine failure, abnormal indications)
- Missed communications or procedural steps due to overload

Exclusions:
- Deliberate continuation decision (see plan_continuation_bias)

---

## MAINTENANCE / MECHANICAL

### aging_aircraft_degradation

Definition:
Failure attributable to wear, corrosion, fatigue, or time-related deterioration.

Indicators:
- Corrosion findings
- Fatigue cracking
- Seal degradation
- Component time exceedance

Exclusions:
- Improper installation (see maintenance_induced_failure)

---

### incomplete_troubleshooting

Definition:
Partial or insufficient diagnostic effort preceding mechanical failure.

Indicators:
- Repeated unresolved discrepancies
- Prior maintenance attempt without root cause resolution

Exclusions:
- Known discrepancy intentionally deferred (see deferred_discrepancy_normalization)

---

### deferred_discrepancy_normalization

Definition:
Acceptance of unresolved mechanical discrepancy as operationally acceptable.

Indicators:
- Known issue not corrected
- Repeated deferral without mitigation

Exclusions:
- Regulatory MEL compliance when properly documented

---

### maintenance_induced_failure

Definition:
Failure directly attributable to maintenance error, improper installation, or improper adjustment.

Indicators:
- Incorrect torque
- Mis-rigged control
- Incorrectly installed component

Exclusions:
- Failure due purely to aging component (see aging_aircraft_degradation)

---

## PERFORMANCE / OPERATIONAL

### weight_balance_misjudgment

Definition:
Incorrect loading or center-of-gravity calculation affecting controllability or performance.

Indicators:
- Documented overweight
- Aft or forward CG beyond limits
- Incorrect fuel distribution affecting balance

Exclusions:
- Performance margin assumption without documented W&B issue

---

### density_altitude_underestimation

Definition:
Failure to adequately account for high density altitude performance penalties.

Indicators:
- High elevation + high temperature
- Inadequate climb performance
- No DA calculation performed

Exclusions:
- General assumption of performance without specific DA relevance

---

### single_engine_performance_assumption

Definition:
Incorrect assumption of climb or controllability margins following engine failure.

Indicators:
- Attempted climb beyond aircraft capability
- Failure to respect VMC or zero-rate climb performance
- Improper engine-out decision gate

Exclusions:
- Pure engine mechanical failure (unless performance misunderstanding contributed)

---

### icing_performance_degradation

Definition:
Failure to adequately account for aerodynamic or performance penalties due to icing.

Indicators:
- Continued flight in known icing
- Loss of control after accumulation
- Degraded climb performance in icing

Exclusions:
- Structural icing damage unrelated to pilot decision

---

## EXPERIENCE-RELATED

### low_time_in_type

Definition:
Limited familiarity with aircraft type contributing to degraded decision-making.

Guideline:
Generally <50 hours in type, but must be contextual.

Exclusions:
- High time pilot unfamiliar with specific subsystem unless documented

---

### high_time_complacency

Definition:
Overconfidence associated with extensive experience reducing vigilance.

Indicators:
- Experienced pilot bypassing verification steps
- Dismissal of abnormal indications

Caution:
Use conservatively to avoid hindsight bias.

---

### lapsed_recency

Definition:
Expired currency or insufficient recent experience affecting performance.

Indicators:
- Expired flight review
- Long period since last multi-engine flight
- Lapsed IPC or instrument currency

---

### informal_or_incomplete_training

Definition:
Non-standardized or insufficient training in systems, procedures, or emergency handling.

Indicators:
- No documented formal multi-engine training
- Improvised emergency procedures
- Absence of type-specific training

Exclusions:
- Simple lack of experience (see low_time_in_type)

---

## UNKNOWN

### unknown

Definition:
Used only when evidence does not allow reasonable attribution to any defined category.

Guidelines:
- Must be used alone (single factor)
- Should not exceed 10% of coded events over time
- Indicates data limitation, not analytical failure

---

# 5. Application Standards

- Do not infer internal thought processes without evidence.
- Avoid assigning more than three factors.
- If two factors overlap, choose the one most directly supported by evidence.
- If no factor clearly applies, use unknown.

---

# 6. Known Limitations (v1.0)

- Cognitive factors may overlap in borderline cases.
- Mechanical categories may require refinement after larger dataset review.
- Experience-related factors require careful evidence-based application.
- Some accident chains involve environmental elements not fully captured in this version.

These limitations will be evaluated after coding the first 25–50 events.

---

# 7. Revision Policy

Any modification to:

- Factor names
- Definitions
- Structural limits
- Domain organization

Requires:

1. Taxonomy version increment.
2. Update to taxonomy-change-log.md.
3. Assessment of impact on previously coded records.

Silent modification is not permitted.

---

# 8. Analytical Intent

This taxonomy is designed to answer:

"What specific, repeatable hazards across Twin Cessna operations are most likely to be mitigated through better standardization, training, or maintenance practices?"

It is not designed to assign blame or replace official investigative conclusions.
