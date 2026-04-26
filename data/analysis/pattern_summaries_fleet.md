# Ranked Pattern Summaries — Fleet (C310/C340/C402)

_Generated: 2026-04-26 00:45:21_

## Analysis Header (Required)

```
taxonomy_version: 1.3
dataset_size_total: 286
dataset_size_per_model: {'C310': 137, 'C402': 49, 'C340': 48, 'C414': 37, 'C320': 15}
unknown_factor_rate: 0.2536
analysis_gate_status: Fleet gate OPEN (>= 75 total). Cross-model comparisons permitted. Counts-only; no exposure-based rates without exposure data.
```

## Guardrails

- Rankings are **counts-only** (no exposure-based rates).
- Shares are labeled as **share_of_events** or **share_of_factor_assignments**.
- Interpret patterns as “appears more frequently in this dataset,” not “higher risk.”

## Baseline Severity Context (counts by model within this scope)

| model   |   total_events |   fatal_events |   serious_injury_events |   destroyed_aircraft |
|:--------|---------------:|---------------:|------------------------:|---------------------:|
| C310    |            137 |             50 |                      10 |                   31 |
| C320    |             15 |              9 |                       1 |                    5 |
| C340    |             48 |             20 |                       2 |                   15 |
| C402    |             49 |              2 |                       4 |                    1 |
| C414    |             37 |             14 |                       5 |                   12 |

## Top 15 Event Types (ranked by count)

| event_type               |   count_events |   share_of_events |
|:-------------------------|---------------:|------------------:|
| Landing_Gear_Malfunction |             73 |            0.2552 |
| Loss_of_Control          |             73 |            0.2552 |
| Runway_Excursion         |             28 |            0.0979 |
| CFIT                     |             22 |            0.0769 |
| Fuel_Starvation          |             17 |            0.0594 |
| Other                    |             13 |            0.0455 |
| Ground_Collision         |             12 |            0.042  |
| Fuel_Exhaustion          |             12 |            0.042  |
| Engine_Failure           |             12 |            0.042  |
| Hard_Landing             |              9 |            0.0315 |
| Fire                     |              6 |            0.021  |
| System_Malfunction       |              6 |            0.021  |
| Midair_Collision         |              3 |            0.0105 |

## Top 15 Phases of Flight (ranked by count)

| phase_of_flight   |   count_events |   share_of_events |
|:------------------|---------------:|------------------:|
| Landing           |             92 |            0.3217 |
| Approach          |             65 |            0.2273 |
| Initial_Climb     |             35 |            0.1224 |
| Cruise            |             34 |            0.1189 |
| Takeoff           |             23 |            0.0804 |
| Taxi              |             16 |            0.0559 |
| Go_Around         |             10 |            0.035  |
| Descent           |              7 |            0.0245 |
| Unknown           |              4 |            0.014  |

## Top 15 Operation Types (ranked by count)

|   operation_type |   count_events |   share_of_events |
|-----------------:|---------------:|------------------:|
|               91 |            247 |            0.8636 |
|              135 |             39 |            0.1364 |

## Top 15 Phase × Event Type Patterns (ranked by count)

| phase_of_flight   | event_type               |   count_events |   share_of_events |
|:------------------|:-------------------------|---------------:|------------------:|
| Landing           | Landing_Gear_Malfunction |             60 |            0.2098 |
| Approach          | Loss_of_Control          |             30 |            0.1049 |
| Initial_Climb     | Loss_of_Control          |             18 |            0.0629 |
| Landing           | Runway_Excursion         |             17 |            0.0594 |
| Approach          | CFIT                     |             13 |            0.0455 |
| Takeoff           | Runway_Excursion         |              9 |            0.0315 |
| Cruise            | Loss_of_Control          |              8 |            0.028  |
| Landing           | Hard_Landing             |              8 |            0.028  |
| Approach          | Fuel_Exhaustion          |              7 |            0.0245 |
| Taxi              | Landing_Gear_Malfunction |              7 |            0.0245 |
| Cruise            | CFIT                     |              6 |            0.021  |
| Go_Around         | Loss_of_Control          |              6 |            0.021  |
| Takeoff           | Loss_of_Control          |              6 |            0.021  |
| Cruise            | Fuel_Exhaustion          |              5 |            0.0175 |
| Taxi              | Ground_Collision         |              5 |            0.0175 |

## Top 15 Contributing Factors (ranked by events_with_factor)

| factor                               |   events_with_factor |   share_of_events |   share_of_factor_assignments |
|:-------------------------------------|---------------------:|------------------:|------------------------------:|
| plan_continuation_bias               |                   60 |            0.2098 |                        0.1905 |
| checklist_non_compliance             |                   52 |            0.1818 |                        0.1651 |
| low_time_in_type                     |                   29 |            0.1014 |                        0.0921 |
| maintenance_induced_failure          |                   29 |            0.1014 |                        0.0921 |
| aging_aircraft_degradation           |                   23 |            0.0804 |                        0.073  |
| informal_or_incomplete_training      |                   19 |            0.0664 |                        0.0603 |
| task_saturation                      |                   19 |            0.0664 |                        0.0603 |
| assumption_of_performance            |                   17 |            0.0594 |                        0.054  |
| icing_performance_degradation        |                   12 |            0.042  |                        0.0381 |
| incomplete_troubleshooting           |                   12 |            0.042  |                        0.0381 |
| lapsed_recency                       |                   12 |            0.042  |                        0.0381 |
| single_engine_performance_assumption |                   11 |            0.0385 |                        0.0349 |
| normalization_of_deviance            |                    6 |            0.021  |                        0.019  |
| deferred_discrepancy_normalization   |                    5 |            0.0175 |                        0.0159 |
| density_altitude_underestimation     |                    4 |            0.014  |                        0.0127 |

## Top 15 Phase × Factor Patterns (ranked by count)

| phase_of_flight   | factor                          |   count_events |   share_of_events |
|:------------------|:--------------------------------|---------------:|------------------:|
| Approach          | plan_continuation_bias          |             23 |            0.0804 |
| Approach          | checklist_non_compliance        |             18 |            0.0629 |
| Landing           | maintenance_induced_failure     |             16 |            0.0559 |
| Landing           | aging_aircraft_degradation      |             14 |            0.049  |
| Landing           | checklist_non_compliance        |             12 |            0.042  |
| Cruise            | plan_continuation_bias          |             11 |            0.0385 |
| Approach          | low_time_in_type                |              9 |            0.0315 |
| Initial_Climb     | plan_continuation_bias          |              9 |            0.0315 |
| Landing           | plan_continuation_bias          |              9 |            0.0315 |
| Approach          | informal_or_incomplete_training |              7 |            0.0245 |
| Initial_Climb     | checklist_non_compliance        |              7 |            0.0245 |
| Approach          | icing_performance_degradation   |              6 |            0.021  |
| Approach          | task_saturation                 |              6 |            0.021  |
| Cruise            | checklist_non_compliance        |              6 |            0.021  |
| Cruise            | informal_or_incomplete_training |              6 |            0.021  |

## Top 15 Event Type × Factor Patterns (ranked by count)

| event_type               | factor                          |   count_events |   share_of_events |
|:-------------------------|:--------------------------------|---------------:|------------------:|
| Loss_of_Control          | plan_continuation_bias          |             26 |            0.0909 |
| Landing_Gear_Malfunction | maintenance_induced_failure     |             19 |            0.0664 |
| Landing_Gear_Malfunction | aging_aircraft_degradation      |             15 |            0.0524 |
| Landing_Gear_Malfunction | checklist_non_compliance        |             14 |            0.049  |
| CFIT                     | plan_continuation_bias          |             12 |            0.042  |
| Loss_of_Control          | informal_or_incomplete_training |             12 |            0.042  |
| Loss_of_Control          | low_time_in_type                |             11 |            0.0385 |
| Loss_of_Control          | checklist_non_compliance        |             10 |            0.035  |
| Fuel_Starvation          | checklist_non_compliance        |              9 |            0.0315 |
| Fuel_Exhaustion          | checklist_non_compliance        |              8 |            0.028  |
| Loss_of_Control          | task_saturation                 |              8 |            0.028  |
| Runway_Excursion         | plan_continuation_bias          |              8 |            0.028  |
| Loss_of_Control          | assumption_of_performance       |              7 |            0.0245 |
| Loss_of_Control          | icing_performance_degradation   |              7 |            0.0245 |
| Loss_of_Control          | lapsed_recency                  |              7 |            0.0245 |

## Top 15 Operation Type × Factor Patterns (ranked by count)

|   operation_type | factor                               |   count_events |   share_of_events |
|-----------------:|:-------------------------------------|---------------:|------------------:|
|               91 | plan_continuation_bias               |             51 |            0.1783 |
|               91 | checklist_non_compliance             |             43 |            0.1503 |
|               91 | low_time_in_type                     |             27 |            0.0944 |
|               91 | maintenance_induced_failure          |             25 |            0.0874 |
|               91 | aging_aircraft_degradation           |             20 |            0.0699 |
|               91 | informal_or_incomplete_training      |             19 |            0.0664 |
|               91 | task_saturation                      |             17 |            0.0594 |
|               91 | assumption_of_performance            |             14 |            0.049  |
|               91 | lapsed_recency                       |             12 |            0.042  |
|               91 | icing_performance_degradation        |             11 |            0.0385 |
|               91 | incomplete_troubleshooting           |             11 |            0.0385 |
|               91 | single_engine_performance_assumption |             11 |            0.0385 |
|              135 | checklist_non_compliance             |              9 |            0.0315 |
|              135 | plan_continuation_bias               |              9 |            0.0315 |
|               91 | normalization_of_deviance            |              6 |            0.021  |

## Unknown Factor Notes

- events_with_unknown_factor: 107
- unknown_factor_rate (assignment-based): 0.2536
