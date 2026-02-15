# Twin Cessna Safety Data & Research Project

## Purpose

This repository contains the structured safety data, taxonomy framework, and analytical outputs for the Twin Cessna Safety Data & Research initiative.

The objective is to identify repeatable, evidence-based hazards across Twin Cessna aircraft that are most likely to be mitigated through improved standardization, training, and maintenance practices.

This project is strictly data-driven and does not produce training curricula, regulatory advocacy, or cultural messaging.

---

## Aircraft Scope

This project covers all piston twin Cessna aircraft including:

Primary fleet focus:
- Cessna 310 (all variants)
- Cessna 320
- Cessna 340
- Cessna 402
- Cessna 414
- Cessna 421

Additional twin Cessna models may be included if relevant to recurring hazard patterns.

All models are analyzed separately unless explicitly performing cross-type comparison.

---

## Operational Scope

Operations included:

- Part 91
- Owner-flown emphasis
- Personal and business use

Operations excluded unless explicitly labeled:
- Scheduled Part 135 commuter assumptions
- Military operations
- Non-piston turbine conversions (unless separately analyzed)

---

## Event Types Included

- Accidents
- Incidents
- Voluntary hazard/precursor reports (e.g., ASRS)

Accident and ASRS data are never merged for frequency analysis.

---

## Geographic Scope

Primary:
- United States

Secondary:
- English-language international investigation agencies (AAIB UK, TSB Canada, ATSB Australia)

International data are used for pattern comparison, not pooled rate analysis.

---

## Time Horizon

Core analysis:
- Most recent 20 years

Older cases included only if representing recurring "evergreen" hazards.

---

## System Architecture

This project uses a hybrid model:

--------------------------------------------

Git Repository = Structured Intelligence  
Google Drive = Evidence Vault

--------------------------------------------

### Git Repository Contains:

- Contributing-factor taxonomy
- Coding rules and methodology
- Structured event records (one aircraft, one occurrence)
- Master datasets (separate for accidents, incidents, ASRS)
- Analytical reports
- Taxonomy version history
- Project worklog

Git tracks:
- Coding changes
- Taxonomy evolution
- Analytical refinement
- Data corrections

---

### Google Drive Contains:

- Raw NTSB PDFs
- CAROL exports
- ASRS reports
- FAA publications
- Supporting documentation

Raw evidence is never modified.

Each structured event record must reference:
- Report number or accession ID
- Drive file path
- Download date

No structured record is considered complete without an evidence pointer.

---

## Core Operating Rules

1. One aircraft, one occurrence = one event record.
2. Accident and ASRS datasets are never merged for frequency analysis.
3. Outcomes are separated from contributing factors.
4. No accident rate inference without verified exposure data.
5. Each record must include taxonomy_version.
6. All analytical conclusions must trace back to coded evidence.
7. Separate cross-type comparisons from single-type findings.

---

## Event ID Format

Format:

[Model]-[Source]-[Year]-[State]-[Sequential ID]

Examples:

C310-ACC-2012-FL-001  
C340-ACC-2018-TX-004  
C421-ASRS-2020-CA-012  

Model codes used in event IDs:

C310  
C320  
C340  
C402  
C414  
C421  

---

## Data Flow

Raw Evidence (Google Drive)
        ↓
Structured Event Record (data/structured/)
        ↓
Model-Specific Master Dataset (data/master/)
        ↓
Cross-Type Analysis (analysis/reports/)

Structured event records are the source of truth.

Master CSV files are derived from structured records.

Cross-type comparisons must explicitly identify:

- Model sample sizes
- Phase-of-flight clustering differences
- Mechanical vs operational dominance differences

---

## Taxonomy Governance

Each structured event must include:

taxonomy_version: X.X

Taxonomy updates must be logged in:

docs/taxonomy/taxonomy-change-log.md

If taxonomy definitions change materially:
- Prior records must be reviewed
- Changes must be documented
- Re-coded files must preserve prior Git history

---

## Analytical Standards

All outputs must:

- Separate severity from frequency
- Identify co-occurring factors
- Avoid hindsight bias language
- Focus on interruptible decision points
- Explicitly label uncertainty
- Flag small sample limitations
- Distinguish between model-specific and fleet-wide findings

No speculation may be presented as fact.

---

## Primary Research Question

“What specific, repeatable hazards across Twin Cessna operations are most likely to be mitigated through better standardization, training, or maintenance practices?”

If an output does not move the project toward answering this question, it should not be produced.

---

## Long-Term Objective

To produce evidence-backed insight that:

- Identifies recurring cognitive traps
- Highlights aging-aircraft mechanical patterns
- Clarifies single-engine performance misconceptions
- Surfaces maintenance normalization behaviors
- Differentiates hazards by model when appropriate

This repository is intended to be durable, auditable, and reproducible.
