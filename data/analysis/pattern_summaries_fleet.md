# Ranked Pattern Summaries — Fleet (C310/C340/C402)

_Generated: 2026-04-05 00:15:29_

## Analysis Header (Required)

```
taxonomy_version: 1.3
dataset_size_total: 143
dataset_size_per_model: {'C310': 89, 'C340': 27, 'C402': 27}
unknown_factor_rate: 0.2524
analysis_gate_status: Fleet gate OPEN (>= 75 total). Cross-model comparisons permitted. Counts-only; no exposure-based rates without exposure data.
```

## Guardrails

- Rankings are **counts-only** (no exposure-based rates).
- Shares are labeled as **share_of_events** or **share_of_factor_assignments**.
- Interpret patterns as “appears more frequently in this dataset,” not “higher risk.”

## Baseline Severity Context (counts by model within this scope)

| model   |   total_events |   fatal_events |   serious_injury_events |   destroyed_aircraft |
|:--------|---------------:|---------------:|------------------------:|---------------------:|
| C310    |             89 |             33 |                       6 |                   21 |
| C340    |             27 |             14 |                       1 |                   10 |
| C402    |             27 |              2 |                       2 |                    1 |

## Top 15 Event Types (ranked by count)

| event_type               |   count_events |   share_of_events |
|:-------------------------|---------------:|------------------:|
| Landing_Gear_Malfunction |             42 |            0.2937 |
| Loss_of_Control          |             36 |            0.2517 |
| CFIT                     |             14 |            0.0979 |
| Runway_Excursion         |             10 |            0.0699 |
| Ground_Collision         |              8 |            0.0559 |
| Fuel_Starvation          |              7 |            0.049  |
| Fuel_Exhaustion          |              7 |            0.049  |
| Fire                     |              4 |            0.028  |
| Hard_Landing             |              4 |            0.028  |
| Other                    |              4 |            0.028  |
| Engine_Failure           |              3 |            0.021  |
| Midair_Collision         |              2 |            0.014  |
| System_Malfunction       |              2 |            0.014  |

## Top 15 Phases of Flight (ranked by count)

| phase_of_flight   |   count_events |   share_of_events |
|:------------------|---------------:|------------------:|
| Landing           |             47 |            0.3287 |
| Approach          |             29 |            0.2028 |
| Cruise            |             25 |            0.1748 |
| Initial_Climb     |             13 |            0.0909 |
| Taxi              |             10 |            0.0699 |
| Takeoff           |              8 |            0.0559 |
| Go_Around         |              5 |            0.035  |
| Descent           |              3 |            0.021  |
| Unknown           |              3 |            0.021  |

## Top 15 Operation Types (ranked by count)

|   operation_type |   count_events |   share_of_events |
|-----------------:|---------------:|------------------:|
|               91 |            117 |            0.8182 |
|              135 |             26 |            0.1818 |

## Top 15 Phase × Event Type Patterns (ranked by count)

| phase_of_flight   | event_type               |   count_events |   share_of_events |
|:------------------|:-------------------------|---------------:|------------------:|
| Landing           | Landing_Gear_Malfunction |             34 |            0.2378 |
| Approach          | Loss_of_Control          |             13 |            0.0909 |
| Initial_Climb     | Loss_of_Control          |              9 |            0.0629 |
| Approach          | CFIT                     |              8 |            0.0559 |
| Landing           | Runway_Excursion         |              6 |            0.042  |
| Cruise            | CFIT                     |              5 |            0.035  |
| Cruise            | Fuel_Exhaustion          |              5 |            0.035  |
| Cruise            | Loss_of_Control          |              5 |            0.035  |
| Taxi              | Landing_Gear_Malfunction |              5 |            0.035  |
| Go_Around         | Loss_of_Control          |              4 |            0.028  |
| Landing           | Hard_Landing             |              4 |            0.028  |
| Takeoff           | Runway_Excursion         |              4 |            0.028  |
| Cruise            | Fuel_Starvation          |              3 |            0.021  |
| Descent           | Loss_of_Control          |              3 |            0.021  |
| Taxi              | Ground_Collision         |              3 |            0.021  |

## Top 15 Contributing Factors (ranked by events_with_factor)

| factor                               |   events_with_factor |   share_of_events |   share_of_factor_assignments |
|:-------------------------------------|---------------------:|------------------:|------------------------------:|
| plan_continuation_bias               |                   30 |            0.2098 |                        0.1948 |
| checklist_non_compliance             |                   23 |            0.1608 |                        0.1494 |
| maintenance_induced_failure          |                   17 |            0.1189 |                        0.1104 |
| low_time_in_type                     |                   14 |            0.0979 |                        0.0909 |
| assumption_of_performance            |                   11 |            0.0769 |                        0.0714 |
| informal_or_incomplete_training      |                   11 |            0.0769 |                        0.0714 |
| aging_aircraft_degradation           |                    9 |            0.0629 |                        0.0584 |
| task_saturation                      |                    9 |            0.0629 |                        0.0584 |
| icing_performance_degradation        |                    8 |            0.0559 |                        0.0519 |
| incomplete_troubleshooting           |                    7 |            0.049  |                        0.0455 |
| lapsed_recency                       |                    6 |            0.042  |                        0.039  |
| deferred_discrepancy_normalization   |                    3 |            0.021  |                        0.0195 |
| normalization_of_deviance            |                    3 |            0.021  |                        0.0195 |
| single_engine_performance_assumption |                    2 |            0.014  |                        0.013  |
| weight_balance_misjudgment           |                    1 |            0.007  |                        0.0065 |

## Top 15 Phase × Factor Patterns (ranked by count)

| phase_of_flight   | factor                          |   count_events |   share_of_events |
|:------------------|:--------------------------------|---------------:|------------------:|
| Landing           | maintenance_induced_failure     |             11 |            0.0769 |
| Approach          | plan_continuation_bias          |              9 |            0.0629 |
| Cruise            | plan_continuation_bias          |              9 |            0.0629 |
| Landing           | checklist_non_compliance        |              7 |            0.049  |
| Cruise            | checklist_non_compliance        |              6 |            0.042  |
| Approach          | checklist_non_compliance        |              5 |            0.035  |
| Approach          | low_time_in_type                |              5 |            0.035  |
| Landing           | incomplete_troubleshooting      |              5 |            0.035  |
| Approach          | icing_performance_degradation   |              4 |            0.028  |
| Cruise            | assumption_of_performance       |              4 |            0.028  |
| Cruise            | informal_or_incomplete_training |              4 |            0.028  |
| Initial_Climb     | plan_continuation_bias          |              4 |            0.028  |
| Landing           | aging_aircraft_degradation      |              4 |            0.028  |
| Landing           | plan_continuation_bias          |              4 |            0.028  |
| Approach          | lapsed_recency                  |              3 |            0.021  |

## Top 15 Event Type × Factor Patterns (ranked by count)

| event_type               | factor                          |   count_events |   share_of_events |
|:-------------------------|:--------------------------------|---------------:|------------------:|
| Landing_Gear_Malfunction | maintenance_induced_failure     |             13 |            0.0909 |
| Loss_of_Control          | plan_continuation_bias          |             12 |            0.0839 |
| Landing_Gear_Malfunction | checklist_non_compliance        |              8 |            0.0559 |
| CFIT                     | plan_continuation_bias          |              7 |            0.049  |
| Landing_Gear_Malfunction | aging_aircraft_degradation      |              7 |            0.049  |
| Loss_of_Control          | low_time_in_type                |              7 |            0.049  |
| Landing_Gear_Malfunction | incomplete_troubleshooting      |              6 |            0.042  |
| Loss_of_Control          | informal_or_incomplete_training |              5 |            0.035  |
| Loss_of_Control          | task_saturation                 |              5 |            0.035  |
| CFIT                     | informal_or_incomplete_training |              4 |            0.028  |
| Fuel_Exhaustion          | checklist_non_compliance        |              4 |            0.028  |
| Fuel_Starvation          | checklist_non_compliance        |              4 |            0.028  |
| Loss_of_Control          | assumption_of_performance       |              4 |            0.028  |
| Loss_of_Control          | icing_performance_degradation   |              4 |            0.028  |
| Loss_of_Control          | lapsed_recency                  |              4 |            0.028  |

## Top 15 Operation Type × Factor Patterns (ranked by count)

|   operation_type | factor                          |   count_events |   share_of_events |
|-----------------:|:--------------------------------|---------------:|------------------:|
|               91 | plan_continuation_bias          |             23 |            0.1608 |
|               91 | checklist_non_compliance        |             18 |            0.1259 |
|               91 | low_time_in_type                |             13 |            0.0909 |
|               91 | maintenance_induced_failure     |             13 |            0.0909 |
|               91 | informal_or_incomplete_training |             11 |            0.0769 |
|               91 | assumption_of_performance       |              9 |            0.0629 |
|               91 | aging_aircraft_degradation      |              8 |            0.0559 |
|              135 | plan_continuation_bias          |              7 |            0.049  |
|               91 | icing_performance_degradation   |              7 |            0.049  |
|               91 | task_saturation                 |              7 |            0.049  |
|               91 | incomplete_troubleshooting      |              6 |            0.042  |
|               91 | lapsed_recency                  |              6 |            0.042  |
|              135 | checklist_non_compliance        |              5 |            0.035  |
|              135 | maintenance_induced_failure     |              4 |            0.028  |
|               91 | normalization_of_deviance       |              3 |            0.021  |

## Unknown Factor Notes

- events_with_unknown_factor: 52
- unknown_factor_rate (assignment-based): 0.2524
