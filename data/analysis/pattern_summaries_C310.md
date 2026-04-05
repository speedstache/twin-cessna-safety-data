# Ranked Pattern Summaries — Model C310

_Generated: 2026-04-05 00:15:29_

## Analysis Header (Required)

```
taxonomy_version: 1.3
dataset_size_total: 89
dataset_size_per_model: {'C310': 89}
unknown_factor_rate: 0.1972
analysis_gate_status: Per-model gate scope for C310. Pattern summaries permitted within this model. Counts-only; no exposure-based rates without exposure data.
```

## Guardrails

- Rankings are **counts-only** (no exposure-based rates).
- Shares are labeled as **share_of_events** or **share_of_factor_assignments**.
- Interpret patterns as “appears more frequently in this dataset,” not “higher risk.”

## Baseline Severity Context (counts by model within this scope)

- total_events: 89
- fatal_events: 33
- serious_injury_events: 6
- destroyed_aircraft: 21

## Top 15 Event Types (ranked by count)

| event_type               |   count_events |   share_of_events |
|:-------------------------|---------------:|------------------:|
| Landing_Gear_Malfunction |             27 |            0.3034 |
| Loss_of_Control          |             25 |            0.2809 |
| CFIT                     |              9 |            0.1011 |
| Fuel_Exhaustion          |              6 |            0.0674 |
| Ground_Collision         |              4 |            0.0449 |
| Fire                     |              3 |            0.0337 |
| Hard_Landing             |              3 |            0.0337 |
| Runway_Excursion         |              3 |            0.0337 |
| Other                    |              3 |            0.0337 |
| Fuel_Starvation          |              2 |            0.0225 |
| Midair_Collision         |              2 |            0.0225 |
| Engine_Failure           |              1 |            0.0112 |
| System_Malfunction       |              1 |            0.0112 |

## Top 15 Phases of Flight (ranked by count)

| phase_of_flight   |   count_events |   share_of_events |
|:------------------|---------------:|------------------:|
| Landing           |             26 |            0.2921 |
| Cruise            |             18 |            0.2022 |
| Approach          |             16 |            0.1798 |
| Initial_Climb     |              8 |            0.0899 |
| Taxi              |              8 |            0.0899 |
| Takeoff           |              5 |            0.0562 |
| Go_Around         |              4 |            0.0449 |
| Descent           |              3 |            0.0337 |
| Unknown           |              1 |            0.0112 |

## Top 15 Operation Types (ranked by count)

|   operation_type |   count_events |   share_of_events |
|-----------------:|---------------:|------------------:|
|               91 |             81 |            0.9101 |
|              135 |              8 |            0.0899 |

## Top 15 Phase × Event Type Patterns (ranked by count)

| phase_of_flight   | event_type               |   count_events |   share_of_events |
|:------------------|:-------------------------|---------------:|------------------:|
| Landing           | Landing_Gear_Malfunction |             20 |            0.2247 |
| Approach          | Loss_of_Control          |              7 |            0.0787 |
| Approach          | CFIT                     |              5 |            0.0562 |
| Cruise            | Fuel_Exhaustion          |              5 |            0.0562 |
| Cruise            | Loss_of_Control          |              5 |            0.0562 |
| Initial_Climb     | Loss_of_Control          |              5 |            0.0562 |
| Taxi              | Landing_Gear_Malfunction |              5 |            0.0562 |
| Cruise            | CFIT                     |              3 |            0.0337 |
| Descent           | Loss_of_Control          |              3 |            0.0337 |
| Go_Around         | Loss_of_Control          |              3 |            0.0337 |
| Landing           | Hard_Landing             |              3 |            0.0337 |
| Cruise            | Midair_Collision         |              2 |            0.0225 |
| Takeoff           | Runway_Excursion         |              2 |            0.0225 |
| Taxi              | Fire                     |              2 |            0.0225 |
| Approach          | Fuel_Exhaustion          |              1 |            0.0112 |

## Top 15 Contributing Factors (ranked by events_with_factor)

| factor                               |   events_with_factor |   share_of_events |   share_of_factor_assignments |
|:-------------------------------------|---------------------:|------------------:|------------------------------:|
| checklist_non_compliance             |                   19 |            0.2135 |                        0.1667 |
| plan_continuation_bias               |                   19 |            0.2135 |                        0.1667 |
| maintenance_induced_failure          |                   12 |            0.1348 |                        0.1053 |
| low_time_in_type                     |                   11 |            0.1236 |                        0.0965 |
| informal_or_incomplete_training      |                   10 |            0.1124 |                        0.0877 |
| aging_aircraft_degradation           |                    7 |            0.0787 |                        0.0614 |
| assumption_of_performance            |                    7 |            0.0787 |                        0.0614 |
| task_saturation                      |                    7 |            0.0787 |                        0.0614 |
| incomplete_troubleshooting           |                    6 |            0.0674 |                        0.0526 |
| icing_performance_degradation        |                    5 |            0.0562 |                        0.0439 |
| lapsed_recency                       |                    5 |            0.0562 |                        0.0439 |
| deferred_discrepancy_normalization   |                    2 |            0.0225 |                        0.0175 |
| single_engine_performance_assumption |                    2 |            0.0225 |                        0.0175 |
| normalization_of_deviance            |                    1 |            0.0112 |                        0.0088 |
| weight_balance_misjudgment           |                    1 |            0.0112 |                        0.0088 |

## Top 15 Phase × Factor Patterns (ranked by count)

| phase_of_flight   | factor                          |   count_events |   share_of_events |
|:------------------|:--------------------------------|---------------:|------------------:|
| Landing           | maintenance_induced_failure     |              7 |            0.0787 |
| Approach          | plan_continuation_bias          |              6 |            0.0674 |
| Cruise            | plan_continuation_bias          |              6 |            0.0674 |
| Landing           | checklist_non_compliance        |              6 |            0.0674 |
| Approach          | checklist_non_compliance        |              4 |            0.0449 |
| Cruise            | assumption_of_performance       |              4 |            0.0449 |
| Cruise            | checklist_non_compliance        |              4 |            0.0449 |
| Cruise            | informal_or_incomplete_training |              4 |            0.0449 |
| Landing           | incomplete_troubleshooting      |              4 |            0.0449 |
| Approach          | low_time_in_type                |              3 |            0.0337 |
| Cruise            | low_time_in_type                |              3 |            0.0337 |
| Initial_Climb     | checklist_non_compliance        |              3 |            0.0337 |
| Initial_Climb     | plan_continuation_bias          |              3 |            0.0337 |
| Taxi              | aging_aircraft_degradation      |              3 |            0.0337 |
| Approach          | icing_performance_degradation   |              2 |            0.0225 |

## Top 15 Event Type × Factor Patterns (ranked by count)

| event_type               | factor                          |   count_events |   share_of_events |
|:-------------------------|:--------------------------------|---------------:|------------------:|
| Loss_of_Control          | plan_continuation_bias          |             11 |            0.1236 |
| Landing_Gear_Malfunction | maintenance_induced_failure     |              9 |            0.1011 |
| Landing_Gear_Malfunction | checklist_non_compliance        |              7 |            0.0787 |
| Landing_Gear_Malfunction | aging_aircraft_degradation      |              5 |            0.0562 |
| Landing_Gear_Malfunction | incomplete_troubleshooting      |              5 |            0.0562 |
| Loss_of_Control          | low_time_in_type                |              5 |            0.0562 |
| CFIT                     | informal_or_incomplete_training |              4 |            0.0449 |
| Fuel_Exhaustion          | checklist_non_compliance        |              4 |            0.0449 |
| Loss_of_Control          | informal_or_incomplete_training |              4 |            0.0449 |
| Loss_of_Control          | task_saturation                 |              4 |            0.0449 |
| CFIT                     | low_time_in_type                |              3 |            0.0337 |
| CFIT                     | plan_continuation_bias          |              3 |            0.0337 |
| Fuel_Exhaustion          | assumption_of_performance       |              3 |            0.0337 |
| Ground_Collision         | checklist_non_compliance        |              3 |            0.0337 |
| Loss_of_Control          | icing_performance_degradation   |              3 |            0.0337 |

## Top 15 Operation Type × Factor Patterns (ranked by count)

|   operation_type | factor                             |   count_events |   share_of_events |
|-----------------:|:-----------------------------------|---------------:|------------------:|
|               91 | plan_continuation_bias             |             17 |            0.191  |
|               91 | checklist_non_compliance           |             16 |            0.1798 |
|               91 | low_time_in_type                   |             11 |            0.1236 |
|               91 | maintenance_induced_failure        |             11 |            0.1236 |
|               91 | informal_or_incomplete_training    |             10 |            0.1124 |
|               91 | aging_aircraft_degradation         |              7 |            0.0787 |
|               91 | incomplete_troubleshooting         |              6 |            0.0674 |
|               91 | task_saturation                    |              6 |            0.0674 |
|               91 | assumption_of_performance          |              5 |            0.0562 |
|               91 | icing_performance_degradation      |              5 |            0.0562 |
|               91 | lapsed_recency                     |              5 |            0.0562 |
|              135 | checklist_non_compliance           |              3 |            0.0337 |
|              135 | assumption_of_performance          |              2 |            0.0225 |
|              135 | plan_continuation_bias             |              2 |            0.0225 |
|               91 | deferred_discrepancy_normalization |              2 |            0.0225 |

## Unknown Factor Notes

- events_with_unknown_factor: 28
- unknown_factor_rate (assignment-based): 0.1972
