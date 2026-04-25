# Ranked Pattern Summaries — Model C310

_Generated: 2026-04-25 16:12:54_

## Analysis Header (Required)

```
taxonomy_version: 1.3
dataset_size_total: 137
dataset_size_per_model: {'C310': 137}
unknown_factor_rate: 0.2476
analysis_gate_status: Per-model gate scope for C310. Pattern summaries permitted within this model. Counts-only; no exposure-based rates without exposure data.
```

## Guardrails

- Rankings are **counts-only** (no exposure-based rates).
- Shares are labeled as **share_of_events** or **share_of_factor_assignments**.
- Interpret patterns as “appears more frequently in this dataset,” not “higher risk.”

## Baseline Severity Context (counts by model within this scope)

- total_events: 137
- fatal_events: 50
- serious_injury_events: 10
- destroyed_aircraft: 31

## Top 15 Event Types (ranked by count)

| event_type               |   count_events |   share_of_events |
|:-------------------------|---------------:|------------------:|
| Landing_Gear_Malfunction |             40 |            0.292  |
| Loss_of_Control          |             36 |            0.2628 |
| CFIT                     |             12 |            0.0876 |
| Fuel_Starvation          |              8 |            0.0584 |
| Fuel_Exhaustion          |              7 |            0.0511 |
| Hard_Landing             |              6 |            0.0438 |
| Ground_Collision         |              6 |            0.0438 |
| Runway_Excursion         |              6 |            0.0438 |
| Engine_Failure           |              5 |            0.0365 |
| Fire                     |              4 |            0.0292 |
| Other                    |              4 |            0.0292 |
| Midair_Collision         |              2 |            0.0146 |
| System_Malfunction       |              1 |            0.0073 |

## Top 15 Phases of Flight (ranked by count)

| phase_of_flight   |   count_events |   share_of_events |
|:------------------|---------------:|------------------:|
| Landing           |             45 |            0.3285 |
| Approach          |             25 |            0.1825 |
| Cruise            |             22 |            0.1606 |
| Initial_Climb     |             16 |            0.1168 |
| Taxi              |             10 |            0.073  |
| Takeoff           |              8 |            0.0584 |
| Go_Around         |              5 |            0.0365 |
| Descent           |              4 |            0.0292 |
| Unknown           |              2 |            0.0146 |

## Top 15 Operation Types (ranked by count)

|   operation_type |   count_events |   share_of_events |
|-----------------:|---------------:|------------------:|
|               91 |            128 |            0.9343 |
|              135 |              9 |            0.0657 |

## Top 15 Phase × Event Type Patterns (ranked by count)

| phase_of_flight   | event_type               |   count_events |   share_of_events |
|:------------------|:-------------------------|---------------:|------------------:|
| Landing           | Landing_Gear_Malfunction |             31 |            0.2263 |
| Approach          | Loss_of_Control          |             10 |            0.073  |
| Initial_Climb     | Loss_of_Control          |              9 |            0.0657 |
| Approach          | CFIT                     |              7 |            0.0511 |
| Cruise            | Loss_of_Control          |              6 |            0.0438 |
| Landing           | Hard_Landing             |              6 |            0.0438 |
| Taxi              | Landing_Gear_Malfunction |              6 |            0.0438 |
| Cruise            | Fuel_Exhaustion          |              5 |            0.0365 |
| Cruise            | CFIT                     |              3 |            0.0219 |
| Descent           | Loss_of_Control          |              3 |            0.0219 |
| Go_Around         | Loss_of_Control          |              3 |            0.0219 |
| Initial_Climb     | Engine_Failure           |              3 |            0.0219 |
| Landing           | Ground_Collision         |              3 |            0.0219 |
| Landing           | Runway_Excursion         |              3 |            0.0219 |
| Takeoff           | Loss_of_Control          |              3 |            0.0219 |

## Top 15 Contributing Factors (ranked by events_with_factor)

| factor                               |   events_with_factor |   share_of_events |   share_of_factor_assignments |
|:-------------------------------------|---------------------:|------------------:|------------------------------:|
| checklist_non_compliance             |                   26 |            0.1898 |                        0.1677 |
| plan_continuation_bias               |                   22 |            0.1606 |                        0.1419 |
| low_time_in_type                     |                   17 |            0.1241 |                        0.1097 |
| maintenance_induced_failure          |                   16 |            0.1168 |                        0.1032 |
| informal_or_incomplete_training      |                   11 |            0.0803 |                        0.071  |
| task_saturation                      |                   11 |            0.0803 |                        0.071  |
| aging_aircraft_degradation           |                   10 |            0.073  |                        0.0645 |
| incomplete_troubleshooting           |                    9 |            0.0657 |                        0.0581 |
| assumption_of_performance            |                    7 |            0.0511 |                        0.0452 |
| single_engine_performance_assumption |                    7 |            0.0511 |                        0.0452 |
| icing_performance_degradation        |                    6 |            0.0438 |                        0.0387 |
| lapsed_recency                       |                    6 |            0.0438 |                        0.0387 |
| deferred_discrepancy_normalization   |                    3 |            0.0219 |                        0.0194 |
| normalization_of_deviance            |                    2 |            0.0146 |                        0.0129 |
| density_altitude_underestimation     |                    1 |            0.0073 |                        0.0065 |

## Top 15 Phase × Factor Patterns (ranked by count)

| phase_of_flight   | factor                               |   count_events |   share_of_events |
|:------------------|:-------------------------------------|---------------:|------------------:|
| Landing           | checklist_non_compliance             |              9 |            0.0657 |
| Landing           | maintenance_induced_failure          |              8 |            0.0584 |
| Approach          | checklist_non_compliance             |              7 |            0.0511 |
| Approach          | plan_continuation_bias               |              7 |            0.0511 |
| Cruise            | plan_continuation_bias               |              6 |            0.0438 |
| Landing           | low_time_in_type                     |              5 |            0.0365 |
| Approach          | low_time_in_type                     |              4 |            0.0292 |
| Cruise            | assumption_of_performance            |              4 |            0.0292 |
| Cruise            | checklist_non_compliance             |              4 |            0.0292 |
| Cruise            | informal_or_incomplete_training      |              4 |            0.0292 |
| Initial_Climb     | checklist_non_compliance             |              4 |            0.0292 |
| Initial_Climb     | maintenance_induced_failure          |              4 |            0.0292 |
| Initial_Climb     | single_engine_performance_assumption |              4 |            0.0292 |
| Landing           | incomplete_troubleshooting           |              4 |            0.0292 |
| Landing           | task_saturation                      |              4 |            0.0292 |

## Top 15 Event Type × Factor Patterns (ranked by count)

| event_type               | factor                               |   count_events |   share_of_events |
|:-------------------------|:-------------------------------------|---------------:|------------------:|
| Loss_of_Control          | plan_continuation_bias               |             12 |            0.0876 |
| Landing_Gear_Malfunction | checklist_non_compliance             |             10 |            0.073  |
| Landing_Gear_Malfunction | maintenance_induced_failure          |             10 |            0.073  |
| Loss_of_Control          | low_time_in_type                     |              6 |            0.0438 |
| Fuel_Exhaustion          | checklist_non_compliance             |              5 |            0.0365 |
| Landing_Gear_Malfunction | aging_aircraft_degradation           |              5 |            0.0365 |
| Landing_Gear_Malfunction | incomplete_troubleshooting           |              5 |            0.0365 |
| Loss_of_Control          | informal_or_incomplete_training      |              5 |            0.0365 |
| Loss_of_Control          | maintenance_induced_failure          |              5 |            0.0365 |
| CFIT                     | informal_or_incomplete_training      |              4 |            0.0292 |
| CFIT                     | low_time_in_type                     |              4 |            0.0292 |
| Fuel_Starvation          | checklist_non_compliance             |              4 |            0.0292 |
| Landing_Gear_Malfunction | task_saturation                      |              4 |            0.0292 |
| Loss_of_Control          | lapsed_recency                       |              4 |            0.0292 |
| Loss_of_Control          | single_engine_performance_assumption |              4 |            0.0292 |

## Top 15 Operation Type × Factor Patterns (ranked by count)

|   operation_type | factor                               |   count_events |   share_of_events |
|-----------------:|:-------------------------------------|---------------:|------------------:|
|               91 | checklist_non_compliance             |             23 |            0.1679 |
|               91 | plan_continuation_bias               |             20 |            0.146  |
|               91 | low_time_in_type                     |             17 |            0.1241 |
|               91 | maintenance_induced_failure          |             15 |            0.1095 |
|               91 | informal_or_incomplete_training      |             11 |            0.0803 |
|               91 | aging_aircraft_degradation           |             10 |            0.073  |
|               91 | task_saturation                      |             10 |            0.073  |
|               91 | incomplete_troubleshooting           |              9 |            0.0657 |
|               91 | single_engine_performance_assumption |              7 |            0.0511 |
|               91 | icing_performance_degradation        |              6 |            0.0438 |
|               91 | lapsed_recency                       |              6 |            0.0438 |
|               91 | assumption_of_performance            |              5 |            0.0365 |
|              135 | checklist_non_compliance             |              3 |            0.0219 |
|               91 | deferred_discrepancy_normalization   |              3 |            0.0219 |
|              135 | assumption_of_performance            |              2 |            0.0146 |

## Unknown Factor Notes

- events_with_unknown_factor: 51
- unknown_factor_rate (assignment-based): 0.2476
