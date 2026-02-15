# Phase 1 Coding Sprint Plan
## Twin Cessna Safety Data & Research Project

---

# Purpose

Phase 1 establishes:

- Baseline dataset integrity
- Taxonomy v1.0 stress test
- Initial pattern visibility
- Coding discipline calibration
- Workflow efficiency refinement

This sprint is not intended to produce public conclusions.
It is intended to validate the analytical foundation.

---

# Scope of Phase 1

Total events: 25 accidents

Aircraft coverage goal:
- Minimum of 3–5 events per primary model where available:
  C310
  C320
  C340
  C402
  C414
  C421

If distribution does not permit equal representation,
document the imbalance in weekly-progress.md.

Time horizon:
- Prefer events within the last 15 years
- Include at least 2 high-severity engine-out cases
- Include at least 2 approach/landing loss-of-control cases
- Include at least 2 maintenance-related events

Purpose:
Expose taxonomy to diverse hazard types early.

---

# Phase 1 Deliverables

1. 25 structured event records (validated YAML)
2. Updated accident_master.csv
3. Taxonomy stress-test notes
4. Initial pattern observations (internal only)
5. Coding drift self-audit

---

# Sprint Structure

## Step 1 — Batch Selection

Pull first 25 NTSB events meeting:

- Aircraft model in scope
- Part 91 if identifiable
- Within primary time window
- Excluding clear Part 135 commuter operations

Archive CAROL export in:
06_Archived_Queries/

---

## Step 2 — Evidence Intake

For each event:

1. Download report PDF
2. Store in correct model/year folder
3. Record download date
4. Confirm report number format

Do not code yet.

Complete evidence acquisition first.

---

## Step 3 — Structured Coding

For each event:

1. Complete YAML header
2. Assign 1–3 contributing factors
3. Write neutral 5–10 sentence narrative
4. Identify prevention leverage (interruptible point)
5. Run validate_records.py
6. Commit in small batches (5 at a time)

Commit message format:

Phase1: Add C310-ACC-2018-TX-002

---

## Step 4 — Self-Calibration Check (After 10 Events)

Pause and review:

- Are factor definitions holding?
- Are categories overlapping?
- Are more than 3 factors frequently needed?
- Are you drifting toward over-attribution?

If ambiguity appears repeatedly:
Document in taxonomy-change-log.md (do not change taxonomy yet).

---

## Step 5 — Completion Review (After 25 Events)

Perform structured review:

### A. Factor Frequency Snapshot

Count frequency of each cf_* column.

Identify:
- Most common 3 factors
- Rare factors
- Unused factors

Do not draw conclusions — only note distribution.

---

### B. Co-Occurrence Scan

Identify recurring pairs:
Example:
- single_engine_performance_assumption + low_time_in_type
- plan_continuation_bias + task_saturation

Flag potential recurring chains.

---

### C. Phase-of-Flight Clustering

Count events by:
- Takeoff / Initial Climb
- Approach / Landing
- Cruise
- Taxi

Identify any dominant clustering.

---

### D. Mechanical vs Operational Balance

Count events involving:
- Maintenance domain factors
- Performance domain factors
- Human cognitive domain factors

Evaluate whether taxonomy domains feel proportionate.

---

# Coding Drift Audit

After 25 events:

Re-code the first 5 events from memory (without looking at prior coding).

Compare:

- Factor selection differences
- Prevention category differences

If discrepancies exist:
Document them.

If systematic:
Revise taxonomy definitions in next version.

---

# Phase 1 Success Criteria

Phase 1 is successful if:

- All 25 events validate cleanly
- No schema drift occurs
- No ad hoc factor additions occur
- Taxonomy shows internal coherence
- Workflow feels repeatable
- Average coding time per event < 45 minutes

---

# What Phase 1 Is NOT

It is NOT:

- A statistical study
- A public report
- A training recommendation
- A frequency declaration

It is a structural validation phase.

---

# Expected Outcomes

At the end of Phase 1 you should know:

- Whether taxonomy v1.0 is stable
- Whether 3-factor limit is appropriate
- Which hazard classes dominate early sample
- Whether mechanical or cognitive patterns appear stronger
- Whether any model-specific signals are emerging

---

# Transition to Phase 2

If taxonomy is stable:

Phase 2 target: 75–100 accidents total

If taxonomy shows instability:

- Revise to v1.1
- Re-code 25 events
- Document impact
- Then expand

---

# North Star Reminder

This sprint is not about finding conclusions.

It is about building a system capable of producing reliable conclusions.

If structural rigor is compromised, the sprint has failed.
