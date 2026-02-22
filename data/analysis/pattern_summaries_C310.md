# Ranked Pattern Summaries — Model C310

_Generated: 2026-02-22 14:44:10_

## Analysis Header (Required)

```
taxonomy_version: 1.3
dataset_size_total: 39
dataset_size_per_model: {'C310': 39}
unknown_factor_rate: 0.0563
analysis_gate_status: Per-model gate scope for C310. Pattern summaries permitted within this model. Counts-only; no exposure-based rates without exposure data.
```

## Guardrails

- Rankings are **counts-only** (no exposure-based rates).
- Shares are labeled as **share_of_events** or **share_of_factor_assignments**.
- Interpret patterns as “appears more frequently in this dataset,” not “higher risk.”

## Baseline Severity Context (counts by model within this scope)

- total_events: 39
- fatal_events: 14
- serious_injury_events: 3
- destroyed_aircraft: 12

## Top 15 Event Types (ranked by count)

| event_type               |   count_events |   share_of_events |
|:-------------------------|---------------:|------------------:|
| Landing_Gear_Malfunction |             15 |            0.3846 |
| Loss_of_Control          |             11 |            0.2821 |
| CFIT                     |              3 |            0.0769 |
| Fuel_Exhaustion          |              3 |            0.0769 |
| Ground_Collision         |              2 |            0.0513 |
| Fire                     |              1 |            0.0256 |
| Hard_Landing             |              1 |            0.0256 |
| Fuel_Starvation          |              1 |            0.0256 |
| Runway_Excursion         |              1 |            0.0256 |
| Midair_Collision         |              1 |            0.0256 |

## Top 15 Phases of Flight (ranked by count)

| phase_of_flight   |   count_events |   share_of_events |
|:------------------|---------------:|------------------:|
| Landing           |             12 |            0.3077 |
| Cruise            |              9 |            0.2308 |
| Approach          |              7 |            0.1795 |
| Taxi              |              4 |            0.1026 |
| Takeoff           |              2 |            0.0513 |
| Initial_Climb     |              2 |            0.0513 |
| Descent           |              2 |            0.0513 |
| Go_Around         |              1 |            0.0256 |

## Top 15 Operation Types (ranked by count)

|   operation_type |   count_events |   share_of_events |
|-----------------:|---------------:|------------------:|
|               91 |             32 |            0.8205 |
|              135 |              7 |            0.1795 |

## Top 15 Phase × Event Type Patterns (ranked by count)

| phase_of_flight   | event_type               |   count_events |   share_of_events |
|:------------------|:-------------------------|---------------:|------------------:|
| Landing           | Landing_Gear_Malfunction |             10 |            0.2564 |
| Approach          | Loss_of_Control          |              3 |            0.0769 |
| Taxi              | Landing_Gear_Malfunction |              3 |            0.0769 |
| Cruise            | CFIT                     |              2 |            0.0513 |
| Cruise            | Fuel_Exhaustion          |              2 |            0.0513 |
| Cruise            | Loss_of_Control          |              2 |            0.0513 |
| Descent           | Loss_of_Control          |              2 |            0.0513 |
| Initial_Climb     | Loss_of_Control          |              2 |            0.0513 |
| Approach          | CFIT                     |              1 |            0.0256 |
| Approach          | Fuel_Exhaustion          |              1 |            0.0256 |
| Approach          | Ground_Collision         |              1 |            0.0256 |
| Approach          | Landing_Gear_Malfunction |              1 |            0.0256 |
| Cruise            | Fire                     |              1 |            0.0256 |
| Cruise            | Fuel_Starvation          |              1 |            0.0256 |
| Cruise            | Midair_Collision         |              1 |            0.0256 |

## Top 15 Contributing Factors (ranked by events_with_factor)

| factor                               |   events_with_factor |   share_of_events |   share_of_factor_assignments |
|:-------------------------------------|---------------------:|------------------:|------------------------------:|
| checklist_non_compliance             |                   12 |            0.3077 |                        0.1791 |
| plan_continuation_bias               |                   11 |            0.2821 |                        0.1642 |
| maintenance_induced_failure          |                    7 |            0.1795 |                        0.1045 |
| task_saturation                      |                    7 |            0.1795 |                        0.1045 |
| aging_aircraft_degradation           |                    5 |            0.1282 |                        0.0746 |
| assumption_of_performance            |                    5 |            0.1282 |                        0.0746 |
| incomplete_troubleshooting           |                    4 |            0.1026 |                        0.0597 |
| low_time_in_type                     |                    4 |            0.1026 |                        0.0597 |
| icing_performance_degradation        |                    3 |            0.0769 |                        0.0448 |
| informal_or_incomplete_training      |                    3 |            0.0769 |                        0.0448 |
| lapsed_recency                       |                    3 |            0.0769 |                        0.0448 |
| normalization_of_deviance            |                    1 |            0.0256 |                        0.0149 |
| single_engine_performance_assumption |                    1 |            0.0256 |                        0.0149 |
| weight_balance_misjudgment           |                    1 |            0.0256 |                        0.0149 |
| deferred_discrepancy_normalization   |                    0 |            0      |                        0      |

## Top 15 Phase × Factor Patterns (ranked by count)

| phase_of_flight   | factor                        |   count_events |   share_of_events |
|:------------------|:------------------------------|---------------:|------------------:|
| Approach          | plan_continuation_bias        |              5 |            0.1282 |
| Approach          | checklist_non_compliance      |              4 |            0.1026 |
| Landing           | maintenance_induced_failure   |              4 |            0.1026 |
| Cruise            | plan_continuation_bias        |              3 |            0.0769 |
| Landing           | checklist_non_compliance      |              3 |            0.0769 |
| Landing           | incomplete_troubleshooting    |              3 |            0.0769 |
| Approach          | task_saturation               |              2 |            0.0513 |
| Cruise            | assumption_of_performance     |              2 |            0.0513 |
| Cruise            | checklist_non_compliance      |              2 |            0.0513 |
| Landing           | aging_aircraft_degradation    |              2 |            0.0513 |
| Landing           | low_time_in_type              |              2 |            0.0513 |
| Taxi              | aging_aircraft_degradation    |              2 |            0.0513 |
| Approach          | aging_aircraft_degradation    |              1 |            0.0256 |
| Approach          | assumption_of_performance     |              1 |            0.0256 |
| Approach          | icing_performance_degradation |              1 |            0.0256 |

## Top 15 Event Type × Factor Patterns (ranked by count)

| event_type               | factor                          |   count_events |   share_of_events |
|:-------------------------|:--------------------------------|---------------:|------------------:|
| Landing_Gear_Malfunction | maintenance_induced_failure     |              6 |            0.1538 |
| Loss_of_Control          | plan_continuation_bias          |              6 |            0.1538 |
| Landing_Gear_Malfunction | aging_aircraft_degradation      |              5 |            0.1282 |
| Landing_Gear_Malfunction | checklist_non_compliance        |              5 |            0.1282 |
| Landing_Gear_Malfunction | incomplete_troubleshooting      |              4 |            0.1026 |
| Loss_of_Control          | task_saturation                 |              4 |            0.1026 |
| Fuel_Exhaustion          | assumption_of_performance       |              2 |            0.0513 |
| Fuel_Exhaustion          | checklist_non_compliance        |              2 |            0.0513 |
| Ground_Collision         | checklist_non_compliance        |              2 |            0.0513 |
| Landing_Gear_Malfunction | low_time_in_type                |              2 |            0.0513 |
| Loss_of_Control          | icing_performance_degradation   |              2 |            0.0513 |
| Loss_of_Control          | lapsed_recency                  |              2 |            0.0513 |
| CFIT                     | checklist_non_compliance        |              1 |            0.0256 |
| CFIT                     | icing_performance_degradation   |              1 |            0.0256 |
| CFIT                     | informal_or_incomplete_training |              1 |            0.0256 |

## Top 15 Operation Type × Factor Patterns (ranked by count)

|   operation_type | factor                          |   count_events |   share_of_events |
|-----------------:|:--------------------------------|---------------:|------------------:|
|               91 | checklist_non_compliance        |              9 |            0.2308 |
|               91 | plan_continuation_bias          |              9 |            0.2308 |
|               91 | maintenance_induced_failure     |              6 |            0.1538 |
|               91 | task_saturation                 |              6 |            0.1538 |
|               91 | aging_aircraft_degradation      |              5 |            0.1282 |
|               91 | incomplete_troubleshooting      |              4 |            0.1026 |
|               91 | low_time_in_type                |              4 |            0.1026 |
|              135 | checklist_non_compliance        |              3 |            0.0769 |
|               91 | assumption_of_performance       |              3 |            0.0769 |
|               91 | icing_performance_degradation   |              3 |            0.0769 |
|               91 | informal_or_incomplete_training |              3 |            0.0769 |
|               91 | lapsed_recency                  |              3 |            0.0769 |
|              135 | assumption_of_performance       |              2 |            0.0513 |
|              135 | plan_continuation_bias          |              2 |            0.0513 |
|              135 | maintenance_induced_failure     |              1 |            0.0256 |

## Unknown Factor Notes

- events_with_unknown_factor: 4
- unknown_factor_rate (assignment-based): 0.0563
