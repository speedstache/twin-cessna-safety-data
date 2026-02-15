# Coding Guidelines
## Twin Cessna Safety Data & Research Project

These guidelines define how to code events into structured records and master datasets with consistency, auditability, and minimal drift.

Structured event records in `data/structured/` are the source of truth.  
Master CSV files in `data/master/` are generated from structured records via script.

---

## 1. Core Principles

### 1.1 One Aircraft, One Occurrence
- Create **one** event record per aircraft occurrence.
- Do not merge separate accidents, separate aircraft, or separate occurrences.

If multiple aircraft are involved in one event:
- Create separate event records per aircraft.
- Evidence may point to the same Drive file(s).

### 1.2 Separate Facts From Interpretation
- The narrative must be factual and neutral.
- Contributing factors are a coded interpretation based on documented evidence.
- Prevention leverage identifies an interruptible point, without hindsight bias language.

### 1.3 Keep Evidence Immutable
- Evidence is stored in Google Drive and is never modified.
- Do not annotate PDFs.
- Corrections or alternative versions are stored separately.

### 1.4 Prevent Schema Drift
- Use only allowed categorical values.
- Never invent a new contributing factor ad hoc.
- If you need a new category repeatedly, log it as a limitation and propose a taxonomy update (v1.1+).

---

## 2. Required Record Format (Structured Event File)

Each event record is a Markdown file with YAML front matter at the top.

Location:
- `data/structured/accidents/<model>/`
- `data/structured/incidents/<model>/`
- `data/structured/asrs/<model>/`

Naming:
- `C310-ACC-2012-001.md`
- `C414-INC-2017-004.md`
- `C402-ASRS-2020-005.md`

---

## 3. YAML Front Matter Rules

### 3.1 Required YAML Fields
Minimum required fields (baseline validation):
- `event_id`
- `model`
- `year`
- `source`
- `taxonomy_version`
- `phase_of_flight`
- `mission_profile`
- `weather_category`
- `maintenance_context`
- `event_type`
- `contributing_factors`
- `drive_path`
- `report_number`

If a required value is unknown:
- Use `Unknown` for categorical fields
- Use `UNK` for short identifiers like `state`, `variant`, `engine_type` (when applicable)

### 3.2 Allowed Values (Categorical Fields)
Use the exact strings below to prevent drift.

phase_of_flight:
- Takeoff
- Initial_Climb
- Cruise
- Descent
- Approach
- Landing
- Go_Around
- Taxi
- Unknown

mission_profile:
- Personal
- Business
- Training
- Ferry
- Maintenance_Flight
- Unknown

weather_category:
- VMC
- IMC
- Night
- Icing
- High_DA
- Mixed
- Unknown

maintenance_context:
- Recent_Work
- Deferred
- None_Noted
- Unknown

recency_status:
- Current
- Lapsed
- Unknown

Time bands:
total_time_band / multi_time_band:
- <500
- 500-1500
- 1500-5000
- >5000
- Unknown

time_in_type_band:
- <50
- 50-200
- 200-1000
- >1000
- Unknown

### 3.3 Boolean Fields
For accidents/incidents (when known):
- `fatal`: true/false
- `serious_injury`: true/false
- `aircraft_destroyed`: true/false

For ASRS:
- Leave these blank or omit from YAML (preferred: omit). Do not force false.

---

## 4. Contributing Factor Coding

### 4.1 Selection Rule
Each event must be assigned **1–3 primary contributing factors**.

Exception:
- If evidence is insufficient, use `unknown` only (single-item list).

### 4.2 Approved Factor Keys (Taxonomy v1.0)
Human / Cognitive:
- normalization_of_deviance
- assumption_of_performance
- plan_continuation_bias
- checklist_non_compliance
- task_saturation

Maintenance / Mechanical:
- aging_aircraft_degradation
- incomplete_troubleshooting
- deferred_discrepancy_normalization
- maintenance_induced_failure

Performance / Operational:
- weight_balance_misjudgment
- density_altitude_underestimation
- single_engine_performance_assumption
- icing_performance_degradation

Experience-Related:
- low_time_in_type
- high_time_complacency
- lapsed_recency
- informal_or_incomplete_training

Unknown:
- unknown

### 4.3 Evidence Standard for Factor Assignment
A factor should be coded only when supported by:
- Explicit report findings, OR
- Strongly indicated factual sequence (e.g., documented omission, documented maintenance error)

Avoid:
- Guessing a cognitive state without cues
- “Filling in” missing data
- Overcoding (using 3 factors for every event)

### 4.4 Common Coding Boundaries (to reduce overlap)
- plan_continuation_bias: continued plan in presence of cues to stop/change
- task_saturation: overload environment leading to missed steps or degraded control
- assumption_of_performance: lack of verified performance margin (DA, W&B, SE climb) treated as “it’ll be fine”
- checklist_non_compliance: procedural step missed where checklist exists (gear, mixture/props, fuel config)
- normalization_of_deviance: recurring acceptance of degraded condition (deferred squawk, routine shortcut)

When uncertain between two, pick the one most directly supported by documented facts.

---

## 5. Prevention Leverage Coding

### 5.1 Definition
Prevention leverage is the most plausible interruptible action that could have broken the event chain.

It must be:
- Specific
- Actionable
- Not blame-oriented
- Not dependent on perfect hindsight

### 5.2 Prevention Category Values
Use one of:
- Training
- Maintenance
- SOP
- Equipment
- Awareness
- Unknown

prevention_summary:
- 1–2 sentences
- Avoid “should have known”
- Prefer “standardize,” “verify,” “require,” “brief,” “gate,” “trigger,” “cross-check”

---

## 6. Narrative Summary (5–10 Sentences)

### 6.1 Requirements
Narrative must be:
- Factual
- Neutral tone
- Free of speculation (unless explicitly labeled as uncertainty)
- Clear on sequence: setup → triggering event → outcome → key findings

### 6.2 Structure (Suggested)
1. Flight context and phase
2. Triggering malfunction/decision/environmental condition
3. Aircraft response and pilot actions (as documented)
4. Outcome (damage/injuries, if known)
5. Investigation findings (mechanical/operational)
6. Any explicitly stated probable cause / findings (do not paraphrase emotionally)

---

## 7. Handling Missing or Conflicting Information

### 7.1 Unknowns
Use:
- `Unknown` for categorical fields
- `UNK` for short identifiers (state/variant/engine_type when needed)
- `contributing_factors: [unknown]` if factors cannot be supported

### 7.2 Conflicts
If sources conflict:
- Prefer primary investigative source
- Note uncertainty in narrative
- Avoid forcing a factor assignment

---

## 8. Workflow Discipline (Solo-Coder)

### 8.1 Batch Cadence
Recommended:
- Evidence intake first (download/store)
- Code in batches of 5
- Validate after each batch
- Commit after each batch

### 8.2 Validation
Run:
- `python3 analysis/scripts/validate_records.py`
before building master datasets.

### 8.3 Drift Control
Every 25 events:
- Re-code the first 5 events without looking
- Compare factor choices
- Log discrepancies in `worklog/weekly-progress.md`
If systematic, propose taxonomy revision (v1.1).

---

## 9. Dataset Separation Rules

- Accidents, incidents, and ASRS are maintained separately.
- Do not compute combined frequency counts across source types.
- Comparative analysis is allowed, but must be explicitly labeled and methodologically careful.

---

## 10. Change Control

If you need to:
- Add a new categorical value
- Add a new column
- Rename a factor key
- Split or merge factor definitions

You must:
1. Update `docs/taxonomy/taxonomy-change-log.md`
2. Update `data/master/data_dictionary.md`
3. Consider backfilling prior records if impacted
4. Increment `taxonomy_version` (minor or major as appropriate)

Silent changes are not permitted.

---

## North Star

All coding exists to answer:

“What specific, repeatable hazards across Twin Cessna operations are most likely to be mitigated through better standardization, training, or maintenance practices?”

If a coding choice does not help answer that question, it should not be made.
