# Twin Cessna Safety Data & Research Project
## Scope Definition

This document defines the formal scope of the Twin Cessna Safety Data & Research Project.

The purpose of scope definition is to:

- Prevent mission creep
- Maintain analytical rigor
- Ensure dataset integrity
- Clarify inclusion and exclusion boundaries
- Protect long-term reproducibility

If a proposed activity does not fall within this scope,
it must not be added without formal revision.

---

# 1. Primary Objective

To identify specific, repeatable hazards in Twin Cessna operations that are most likely to be mitigated through improved standardization, training, or maintenance practices.

The project is strictly evidence-driven.

It does not:
- Deliver training curriculum
- Advocate regulatory changes
- Publish opinion-based commentary
- Replace official accident investigation findings

---

# 2. Aircraft Included

The following piston twin Cessna aircraft are within scope:

C310 (all variants)  
C320  
C340  
C402  
C414  
C421  

These aircraft are analyzed individually and comparatively.

Aircraft outside this list are excluded unless formally added through scope revision.

Turbine conversions are excluded unless explicitly labeled and analyzed separately.

---

# 3. Operational Scope

Included:

- Part 91 operations
- Owner-flown aircraft
- Personal and business operations
- Maintenance flights when relevant to incident chain

Excluded unless explicitly labeled:

- Scheduled Part 135 commuter operations
- Military operations
- Flight school fleet-level safety analysis (unless part of event chain)

The project does not attempt to normalize for operational exposure.

---

# 4. Event Types Included

Included:

- Accidents (NTSB investigations)
- Incidents
- Voluntary safety reports (ASRS)
- International investigation reports (English-language only)

Excluded:

- Anecdotal accounts
- Informal pilot narratives
- Forum discussions
- Non-investigated minor occurrences without documentation

Accident, incident, and ASRS datasets are maintained separately.

They are never merged for frequency calculations.

---

# 5. Geographic Scope

Primary:

United States (NTSB and ASRS)

Secondary (comparative only):

AAIB (United Kingdom)  
TSB (Canada)  
ATSB (Australia)

International data are used for pattern comparison,
not pooled statistical rate inference.

---

# 6. Time Horizon

Primary analysis window:

Most recent 20 years.

Older cases (pre-2005) may be included only if:

- They illustrate recurring hazard patterns
- They clarify persistent performance misconceptions
- They remain operationally relevant

Older cases are stored separately as "Evergreen."

They are not used to inflate frequency counts.

---

# 7. Data Sources

Primary Sources:

- National Transportation Safety Board (NTSB)
- NASA Aviation Safety Reporting System (ASRS)

Supporting Sources:

- FAA SAFOs, InFOs, Airworthiness Directives
- International investigation agencies (English-language only)

Disallowed Sources:

- Blogs
- YouTube
- Forums
- Social media
- Opinion commentary

All evidence must be stored in the Google Drive Evidence Vault.

---

# 8. Data Structure Principles

Each dataset follows strict structural rules:

- One aircraft, one occurrence = one row.
- Structured event records are the source of truth.
- Master CSV files are generated from structured records.
- Contributing factors are coded using fixed taxonomy.
- Maximum of three primary contributing factors per event.
- Unknown is allowed but must be explicit.

Severity is stored separately from contributing factors.

---

# 9. Analytical Boundaries

This project:

- Identifies recurring contributing factors.
- Identifies phase-of-flight clustering.
- Identifies co-occurring hazard patterns.
- Separates severity from frequency.
- Highlights interruptible decision points.

This project does NOT:

- Infer accident rates without exposure data.
- Assign blame.
- Replace official probable cause findings.
- Declare causal certainty where evidence is ambiguous.

All conclusions must be traceable to coded evidence.

---

# 10. Governance

Taxonomy versioning is tracked in:

docs/taxonomy/taxonomy-change-log.md

Schema definitions are tracked in:

data/master/data_dictionary.md

Scope changes require:

- Documentation
- Version update
- Explicit notation of impact on prior records

Silent drift is not permitted.

---

# 11. Evidence Handling

Raw evidence is stored exclusively in Google Drive.

Structured data and analysis reside in Git.

Every structured event record must include:

- Report number
- Drive file path
- Download date
- Taxonomy version

If traceability cannot be established,
the record is invalid.

---

# 12. North Star

The project exists to answer:

"What specific, repeatable hazards across Twin Cessna operations are most likely to be mitigated through better standardization, training, or maintenance practices?"

All analytical work must move toward answering that question.

If it does not, it is outside scope.
