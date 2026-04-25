# Ranked Pattern Summaries — Fleet (C310/C340/C402)

_Generated: 2026-04-25 16:12:54_

## Analysis Header (Required)

```
taxonomy_version: 1.3
dataset_size_total: 227
dataset_size_per_model: {'C310': 137, 'C340': 48, 'C402': 27, 'C320': 15}
unknown_factor_rate: 0.256
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
| C402    |             27 |              2 |                       2 |                    1 |

## Top 15 Event Types (ranked by count)

| event_type               |   count_events |   share_of_events |
|:-------------------------|---------------:|------------------:|
| Landing_Gear_Malfunction |             62 |            0.2731 |
| Loss_of_Control          |             61 |            0.2687 |
| CFIT                     |             19 |            0.0837 |
| Fuel_Starvation          |             15 |            0.0661 |
| Runway_Excursion         |             15 |            0.0661 |
| Ground_Collision         |             12 |            0.0529 |
| Fuel_Exhaustion          |              9 |            0.0396 |
| Engine_Failure           |              9 |            0.0396 |
| Hard_Landing             |              8 |            0.0352 |
| Other                    |              6 |            0.0264 |
| Fire                     |              5 |            0.022  |
| Midair_Collision         |              3 |            0.0132 |
| System_Malfunction       |              3 |            0.0132 |

## Top 15 Phases of Flight (ranked by count)

| phase_of_flight   |   count_events |   share_of_events |
|:------------------|---------------:|------------------:|
| Landing           |             73 |            0.3216 |
| Approach          |             48 |            0.2115 |
| Cruise            |             33 |            0.1454 |
| Initial_Climb     |             26 |            0.1145 |
| Taxi              |             16 |            0.0705 |
| Takeoff           |             15 |            0.0661 |
| Go_Around         |              7 |            0.0308 |
| Descent           |              5 |            0.022  |
| Unknown           |              4 |            0.0176 |

## Top 15 Operation Types (ranked by count)

|   operation_type |   count_events |   share_of_events |
|-----------------:|---------------:|------------------:|
|               91 |            200 |            0.8811 |
|              135 |             27 |            0.1189 |

## Top 15 Phase × Event Type Patterns (ranked by count)

| phase_of_flight   | event_type               |   count_events |   share_of_events |
|:------------------|:-------------------------|---------------:|------------------:|
| Landing           | Landing_Gear_Malfunction |             50 |            0.2203 |
| Approach          | Loss_of_Control          |             23 |            0.1013 |
| Initial_Climb     | Loss_of_Control          |             16 |            0.0705 |
| Approach          | CFIT                     |             11 |            0.0485 |
| Landing           | Runway_Excursion         |              9 |            0.0396 |
| Cruise            | Loss_of_Control          |              8 |            0.0352 |
| Landing           | Hard_Landing             |              7 |            0.0308 |
| Taxi              | Landing_Gear_Malfunction |              7 |            0.0308 |
| Cruise            | CFIT                     |              6 |            0.0264 |
| Cruise            | Fuel_Exhaustion          |              5 |            0.022  |
| Takeoff           | Loss_of_Control          |              5 |            0.022  |
| Takeoff           | Runway_Excursion         |              5 |            0.022  |
| Taxi              | Ground_Collision         |              5 |            0.022  |
| Approach          | Fuel_Exhaustion          |              4 |            0.0176 |
| Cruise            | Fuel_Starvation          |              4 |            0.0176 |

## Top 15 Contributing Factors (ranked by events_with_factor)

| factor                               |   events_with_factor |   share_of_events |   share_of_factor_assignments |
|:-------------------------------------|---------------------:|------------------:|------------------------------:|
| plan_continuation_bias               |                   45 |            0.1982 |                         0.18  |
| checklist_non_compliance             |                   36 |            0.1586 |                         0.144 |
| maintenance_induced_failure          |                   25 |            0.1101 |                         0.1   |
| low_time_in_type                     |                   24 |            0.1057 |                         0.096 |
| informal_or_incomplete_training      |                   18 |            0.0793 |                         0.072 |
| aging_aircraft_degradation           |                   16 |            0.0705 |                         0.064 |
| task_saturation                      |                   16 |            0.0705 |                         0.064 |
| assumption_of_performance            |                   13 |            0.0573 |                         0.052 |
| incomplete_troubleshooting           |                   11 |            0.0485 |                         0.044 |
| icing_performance_degradation        |                   10 |            0.0441 |                         0.04  |
| single_engine_performance_assumption |                   10 |            0.0441 |                         0.04  |
| lapsed_recency                       |                    9 |            0.0396 |                         0.036 |
| normalization_of_deviance            |                    6 |            0.0264 |                         0.024 |
| deferred_discrepancy_normalization   |                    4 |            0.0176 |                         0.016 |
| density_altitude_underestimation     |                    4 |            0.0176 |                         0.016 |

## Top 15 Phase × Factor Patterns (ranked by count)

| phase_of_flight   | factor                          |   count_events |   share_of_events |
|:------------------|:--------------------------------|---------------:|------------------:|
| Approach          | plan_continuation_bias          |             17 |            0.0749 |
| Landing           | maintenance_induced_failure     |             14 |            0.0617 |
| Approach          | checklist_non_compliance        |             12 |            0.0529 |
| Cruise            | plan_continuation_bias          |             11 |            0.0485 |
| Landing           | checklist_non_compliance        |             11 |            0.0485 |
| Landing           | aging_aircraft_degradation      |              9 |            0.0396 |
| Approach          | low_time_in_type                |              7 |            0.0308 |
| Approach          | informal_or_incomplete_training |              6 |            0.0264 |
| Cruise            | checklist_non_compliance        |              6 |            0.0264 |
| Cruise            | informal_or_incomplete_training |              6 |            0.0264 |
| Initial_Climb     | plan_continuation_bias          |              6 |            0.0264 |
| Landing           | low_time_in_type                |              6 |            0.0264 |
| Landing           | plan_continuation_bias          |              6 |            0.0264 |
| Approach          | icing_performance_degradation   |              5 |            0.022  |
| Initial_Climb     | maintenance_induced_failure     |              5 |            0.022  |

## Top 15 Event Type × Factor Patterns (ranked by count)

| event_type               | factor                          |   count_events |   share_of_events |
|:-------------------------|:--------------------------------|---------------:|------------------:|
| Loss_of_Control          | plan_continuation_bias          |             20 |            0.0881 |
| Landing_Gear_Malfunction | maintenance_induced_failure     |             17 |            0.0749 |
| Landing_Gear_Malfunction | checklist_non_compliance        |             12 |            0.0529 |
| Loss_of_Control          | informal_or_incomplete_training |             11 |            0.0485 |
| Landing_Gear_Malfunction | aging_aircraft_degradation      |             10 |            0.0441 |
| Loss_of_Control          | low_time_in_type                |             10 |            0.0441 |
| CFIT                     | plan_continuation_bias          |              9 |            0.0396 |
| Fuel_Starvation          | checklist_non_compliance        |              7 |            0.0308 |
| Fuel_Exhaustion          | checklist_non_compliance        |              6 |            0.0264 |
| Landing_Gear_Malfunction | incomplete_troubleshooting      |              6 |            0.0264 |
| Loss_of_Control          | assumption_of_performance       |              6 |            0.0264 |
| Loss_of_Control          | checklist_non_compliance        |              6 |            0.0264 |
| Loss_of_Control          | lapsed_recency                  |              6 |            0.0264 |
| Loss_of_Control          | task_saturation                 |              6 |            0.0264 |
| CFIT                     | informal_or_incomplete_training |              5 |            0.022  |

## Top 15 Operation Type × Factor Patterns (ranked by count)

|   operation_type | factor                               |   count_events |   share_of_events |
|-----------------:|:-------------------------------------|---------------:|------------------:|
|               91 | plan_continuation_bias               |             38 |            0.1674 |
|               91 | checklist_non_compliance             |             31 |            0.1366 |
|               91 | low_time_in_type                     |             23 |            0.1013 |
|               91 | maintenance_induced_failure          |             21 |            0.0925 |
|               91 | informal_or_incomplete_training      |             18 |            0.0793 |
|               91 | aging_aircraft_degradation           |             15 |            0.0661 |
|               91 | task_saturation                      |             14 |            0.0617 |
|               91 | assumption_of_performance            |             11 |            0.0485 |
|               91 | incomplete_troubleshooting           |             10 |            0.0441 |
|               91 | single_engine_performance_assumption |             10 |            0.0441 |
|               91 | icing_performance_degradation        |              9 |            0.0396 |
|               91 | lapsed_recency                       |              9 |            0.0396 |
|              135 | plan_continuation_bias               |              7 |            0.0308 |
|               91 | normalization_of_deviance            |              6 |            0.0264 |
|              135 | checklist_non_compliance             |              5 |            0.022  |

## Unknown Factor Notes

- events_with_unknown_factor: 86
- unknown_factor_rate (assignment-based): 0.256
