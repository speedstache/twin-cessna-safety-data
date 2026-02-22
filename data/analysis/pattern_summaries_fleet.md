# Ranked Pattern Summaries — Fleet (C310/C340/C402)

_Generated: 2026-02-22 14:44:10_

## Analysis Header (Required)

```
taxonomy_version: 1.3
dataset_size_total: 93
dataset_size_per_model: {'C310': 39, 'C340': 27, 'C402': 27}
unknown_factor_rate: 0.2074
analysis_gate_status: Fleet gate OPEN (>= 75 total). Cross-model comparisons permitted. Counts-only; no exposure-based rates without exposure data.
```

## Guardrails

- Rankings are **counts-only** (no exposure-based rates).
- Shares are labeled as **share_of_events** or **share_of_factor_assignments**.
- Interpret patterns as “appears more frequently in this dataset,” not “higher risk.”

## Baseline Severity Context (counts by model within this scope)

| model   |   total_events |   fatal_events |   serious_injury_events |   destroyed_aircraft |
|:--------|---------------:|---------------:|------------------------:|---------------------:|
| C310    |             39 |             14 |                       3 |                   12 |
| C340    |             27 |             14 |                       1 |                   10 |
| C402    |             27 |              2 |                       2 |                    1 |

## Top 15 Event Types (ranked by count)

| event_type               |   count_events |   share_of_events |
|:-------------------------|---------------:|------------------:|
| Landing_Gear_Malfunction |             30 |            0.3226 |
| Loss_of_Control          |             22 |            0.2366 |
| CFIT                     |              8 |            0.086  |
| Runway_Excursion         |              8 |            0.086  |
| Fuel_Starvation          |              6 |            0.0645 |
| Ground_Collision         |              6 |            0.0645 |
| Fuel_Exhaustion          |              4 |            0.043  |
| Fire                     |              2 |            0.0215 |
| Hard_Landing             |              2 |            0.0215 |
| Engine_Failure           |              2 |            0.0215 |
| Midair_Collision         |              1 |            0.0108 |
| Other                    |              1 |            0.0108 |
| System_Malfunction       |              1 |            0.0108 |

## Top 15 Phases of Flight (ranked by count)

| phase_of_flight   |   count_events |   share_of_events |
|:------------------|---------------:|------------------:|
| Landing           |             33 |            0.3548 |
| Approach          |             20 |            0.2151 |
| Cruise            |             16 |            0.172  |
| Initial_Climb     |              7 |            0.0753 |
| Taxi              |              6 |            0.0645 |
| Takeoff           |              5 |            0.0538 |
| Descent           |              2 |            0.0215 |
| Go_Around         |              2 |            0.0215 |
| Unknown           |              2 |            0.0215 |

## Top 15 Operation Types (ranked by count)

|   operation_type |   count_events |   share_of_events |
|-----------------:|---------------:|------------------:|
|               91 |             69 |            0.7419 |
|              135 |             24 |            0.2581 |

## Top 15 Phase × Event Type Patterns (ranked by count)

| phase_of_flight   | event_type               |   count_events |   share_of_events |
|:------------------|:-------------------------|---------------:|------------------:|
| Landing           | Landing_Gear_Malfunction |             24 |            0.2581 |
| Approach          | Loss_of_Control          |              9 |            0.0968 |
| Initial_Climb     | Loss_of_Control          |              6 |            0.0645 |
| Landing           | Runway_Excursion         |              6 |            0.0645 |
| Approach          | CFIT                     |              4 |            0.043  |
| Cruise            | CFIT                     |              4 |            0.043  |
| Cruise            | Fuel_Starvation          |              3 |            0.0323 |
| Taxi              | Ground_Collision         |              3 |            0.0323 |
| Taxi              | Landing_Gear_Malfunction |              3 |            0.0323 |
| Approach          | Fuel_Exhaustion          |              2 |            0.0215 |
| Approach          | Landing_Gear_Malfunction |              2 |            0.0215 |
| Cruise            | Fuel_Exhaustion          |              2 |            0.0215 |
| Cruise            | Loss_of_Control          |              2 |            0.0215 |
| Descent           | Loss_of_Control          |              2 |            0.0215 |
| Go_Around         | Loss_of_Control          |              2 |            0.0215 |

## Top 15 Contributing Factors (ranked by events_with_factor)

| factor                               |   events_with_factor |   share_of_events |   share_of_factor_assignments |
|:-------------------------------------|---------------------:|------------------:|------------------------------:|
| plan_continuation_bias               |                   22 |            0.2366 |                        0.2056 |
| checklist_non_compliance             |                   16 |            0.172  |                        0.1495 |
| maintenance_induced_failure          |                   12 |            0.129  |                        0.1121 |
| assumption_of_performance            |                    9 |            0.0968 |                        0.0841 |
| task_saturation                      |                    9 |            0.0968 |                        0.0841 |
| aging_aircraft_degradation           |                    7 |            0.0753 |                        0.0654 |
| low_time_in_type                     |                    7 |            0.0753 |                        0.0654 |
| icing_performance_degradation        |                    6 |            0.0645 |                        0.0561 |
| incomplete_troubleshooting           |                    5 |            0.0538 |                        0.0467 |
| informal_or_incomplete_training      |                    4 |            0.043  |                        0.0374 |
| lapsed_recency                       |                    4 |            0.043  |                        0.0374 |
| normalization_of_deviance            |                    3 |            0.0323 |                        0.028  |
| deferred_discrepancy_normalization   |                    1 |            0.0108 |                        0.0093 |
| single_engine_performance_assumption |                    1 |            0.0108 |                        0.0093 |
| weight_balance_misjudgment           |                    1 |            0.0108 |                        0.0093 |

## Top 15 Phase × Factor Patterns (ranked by count)

| phase_of_flight   | factor                        |   count_events |   share_of_events |
|:------------------|:------------------------------|---------------:|------------------:|
| Approach          | plan_continuation_bias        |              8 |            0.086  |
| Landing           | maintenance_induced_failure   |              8 |            0.086  |
| Cruise            | plan_continuation_bias        |              6 |            0.0645 |
| Approach          | checklist_non_compliance      |              5 |            0.0538 |
| Cruise            | checklist_non_compliance      |              4 |            0.043  |
| Landing           | aging_aircraft_degradation    |              4 |            0.043  |
| Landing           | checklist_non_compliance      |              4 |            0.043  |
| Landing           | incomplete_troubleshooting    |              4 |            0.043  |
| Landing           | plan_continuation_bias        |              4 |            0.043  |
| Approach          | icing_performance_degradation |              3 |            0.0323 |
| Landing           | low_time_in_type              |              3 |            0.0323 |
| Approach          | lapsed_recency                |              2 |            0.0215 |
| Approach          | low_time_in_type              |              2 |            0.0215 |
| Approach          | task_saturation               |              2 |            0.0215 |
| Cruise            | assumption_of_performance     |              2 |            0.0215 |

## Top 15 Event Type × Factor Patterns (ranked by count)

| event_type               | factor                        |   count_events |   share_of_events |
|:-------------------------|:------------------------------|---------------:|------------------:|
| Landing_Gear_Malfunction | maintenance_induced_failure   |             10 |            0.1075 |
| Landing_Gear_Malfunction | aging_aircraft_degradation    |              7 |            0.0753 |
| Loss_of_Control          | plan_continuation_bias        |              7 |            0.0753 |
| Landing_Gear_Malfunction | checklist_non_compliance      |              6 |            0.0645 |
| CFIT                     | plan_continuation_bias        |              5 |            0.0538 |
| Landing_Gear_Malfunction | incomplete_troubleshooting    |              5 |            0.0538 |
| Loss_of_Control          | task_saturation               |              5 |            0.0538 |
| Fuel_Starvation          | checklist_non_compliance      |              3 |            0.0323 |
| Loss_of_Control          | assumption_of_performance     |              3 |            0.0323 |
| Loss_of_Control          | icing_performance_degradation |              3 |            0.0323 |
| Loss_of_Control          | lapsed_recency                |              3 |            0.0323 |
| Loss_of_Control          | low_time_in_type              |              3 |            0.0323 |
| Runway_Excursion         | plan_continuation_bias        |              3 |            0.0323 |
| CFIT                     | icing_performance_degradation |              2 |            0.0215 |
| Fuel_Exhaustion          | assumption_of_performance     |              2 |            0.0215 |

## Top 15 Operation Type × Factor Patterns (ranked by count)

|   operation_type | factor                          |   count_events |   share_of_events |
|-----------------:|:--------------------------------|---------------:|------------------:|
|               91 | plan_continuation_bias          |             16 |            0.172  |
|               91 | checklist_non_compliance        |             11 |            0.1183 |
|               91 | maintenance_induced_failure     |              8 |            0.086  |
|               91 | assumption_of_performance       |              7 |            0.0753 |
|               91 | task_saturation                 |              7 |            0.0753 |
|              135 | plan_continuation_bias          |              6 |            0.0645 |
|               91 | aging_aircraft_degradation      |              6 |            0.0645 |
|               91 | low_time_in_type                |              6 |            0.0645 |
|              135 | checklist_non_compliance        |              5 |            0.0538 |
|               91 | icing_performance_degradation   |              5 |            0.0538 |
|              135 | maintenance_induced_failure     |              4 |            0.043  |
|               91 | incomplete_troubleshooting      |              4 |            0.043  |
|               91 | informal_or_incomplete_training |              4 |            0.043  |
|               91 | lapsed_recency                  |              4 |            0.043  |
|               91 | normalization_of_deviance       |              3 |            0.0323 |

## Unknown Factor Notes

- events_with_unknown_factor: 28
- unknown_factor_rate (assignment-based): 0.2074
