# Ranked Pattern Summaries — Model C340

_Generated: 2026-04-26 00:45:21_

## Analysis Header (Required)

```
taxonomy_version: 1.3
dataset_size_total: 48
dataset_size_per_model: {'C340': 48}
unknown_factor_rate: 0.2647
analysis_gate_status: Per-model gate scope for C340. Pattern summaries permitted within this model. Counts-only; no exposure-based rates without exposure data.
```

## Guardrails

- Rankings are **counts-only** (no exposure-based rates).
- Shares are labeled as **share_of_events** or **share_of_factor_assignments**.
- Interpret patterns as “appears more frequently in this dataset,” not “higher risk.”

## Baseline Severity Context (counts by model within this scope)

- total_events: 48
- fatal_events: 20
- serious_injury_events: 2
- destroyed_aircraft: 15

## Top 15 Event Types (ranked by count)

| event_type               |   count_events |   share_of_events |
|:-------------------------|---------------:|------------------:|
| Loss_of_Control          |             15 |            0.3125 |
| Landing_Gear_Malfunction |              7 |            0.1458 |
| CFIT                     |              6 |            0.125  |
| Runway_Excursion         |              6 |            0.125  |
| Fuel_Starvation          |              4 |            0.0833 |
| Ground_Collision         |              4 |            0.0833 |
| Fire                     |              1 |            0.0208 |
| System_Malfunction       |              1 |            0.0208 |
| Hard_Landing             |              1 |            0.0208 |
| Midair_Collision         |              1 |            0.0208 |
| Other                    |              1 |            0.0208 |
| Fuel_Exhaustion          |              1 |            0.0208 |

## Top 15 Phases of Flight (ranked by count)

| phase_of_flight   |   count_events |   share_of_events |
|:------------------|---------------:|------------------:|
| Approach          |             17 |            0.3542 |
| Landing           |             11 |            0.2292 |
| Cruise            |              5 |            0.1042 |
| Initial_Climb     |              5 |            0.1042 |
| Takeoff           |              4 |            0.0833 |
| Taxi              |              3 |            0.0625 |
| Go_Around         |              2 |            0.0417 |
| Descent           |              1 |            0.0208 |

## Top 15 Operation Types (ranked by count)

|   operation_type |   count_events |   share_of_events |
|-----------------:|---------------:|------------------:|
|               91 |             48 |                 1 |

## Top 15 Phase × Event Type Patterns (ranked by count)

| phase_of_flight   | event_type               |   count_events |   share_of_events |
|:------------------|:-------------------------|---------------:|------------------:|
| Approach          | Loss_of_Control          |              8 |            0.1667 |
| Landing           | Landing_Gear_Malfunction |              6 |            0.125  |
| Approach          | CFIT                     |              4 |            0.0833 |
| Initial_Climb     | Loss_of_Control          |              4 |            0.0833 |
| Landing           | Runway_Excursion         |              4 |            0.0833 |
| Cruise            | CFIT                     |              2 |            0.0417 |
| Takeoff           | Runway_Excursion         |              2 |            0.0417 |
| Taxi              | Ground_Collision         |              2 |            0.0417 |
| Approach          | Fire                     |              1 |            0.0208 |
| Approach          | Fuel_Exhaustion          |              1 |            0.0208 |
| Approach          | Fuel_Starvation          |              1 |            0.0208 |
| Approach          | Landing_Gear_Malfunction |              1 |            0.0208 |
| Approach          | Midair_Collision         |              1 |            0.0208 |
| Cruise            | Fuel_Starvation          |              1 |            0.0208 |
| Cruise            | Ground_Collision         |              1 |            0.0208 |

## Top 15 Contributing Factors (ranked by events_with_factor)

| factor                               |   events_with_factor |   share_of_events |   share_of_factor_assignments |
|:-------------------------------------|---------------------:|------------------:|------------------------------:|
| plan_continuation_bias               |                   12 |            0.25   |                          0.24 |
| checklist_non_compliance             |                    7 |            0.1458 |                          0.14 |
| assumption_of_performance            |                    5 |            0.1042 |                          0.1  |
| low_time_in_type                     |                    4 |            0.0833 |                          0.08 |
| normalization_of_deviance            |                    4 |            0.0833 |                          0.08 |
| icing_performance_degradation        |                    3 |            0.0625 |                          0.06 |
| informal_or_incomplete_training      |                    3 |            0.0625 |                          0.06 |
| maintenance_induced_failure          |                    3 |            0.0625 |                          0.06 |
| task_saturation                      |                    3 |            0.0625 |                          0.06 |
| density_altitude_underestimation     |                    2 |            0.0417 |                          0.04 |
| aging_aircraft_degradation           |                    1 |            0.0208 |                          0.02 |
| lapsed_recency                       |                    1 |            0.0208 |                          0.02 |
| single_engine_performance_assumption |                    1 |            0.0208 |                          0.02 |
| weight_balance_misjudgment           |                    1 |            0.0208 |                          0.02 |
| deferred_discrepancy_normalization   |                    0 |            0      |                          0    |

## Top 15 Phase × Factor Patterns (ranked by count)

| phase_of_flight   | factor                           |   count_events |   share_of_events |
|:------------------|:---------------------------------|---------------:|------------------:|
| Approach          | plan_continuation_bias           |              7 |            0.1458 |
| Approach          | checklist_non_compliance         |              4 |            0.0833 |
| Approach          | icing_performance_degradation    |              3 |            0.0625 |
| Approach          | low_time_in_type                 |              3 |            0.0625 |
| Landing           | maintenance_induced_failure      |              3 |            0.0625 |
| Approach          | informal_or_incomplete_training  |              2 |            0.0417 |
| Approach          | normalization_of_deviance        |              2 |            0.0417 |
| Cruise            | plan_continuation_bias           |              2 |            0.0417 |
| Initial_Climb     | assumption_of_performance        |              2 |            0.0417 |
| Initial_Climb     | plan_continuation_bias           |              2 |            0.0417 |
| Landing           | assumption_of_performance        |              2 |            0.0417 |
| Takeoff           | density_altitude_underestimation |              2 |            0.0417 |
| Approach          | lapsed_recency                   |              1 |            0.0208 |
| Approach          | task_saturation                  |              1 |            0.0208 |
| Cruise            | checklist_non_compliance         |              1 |            0.0208 |

## Top 15 Event Type × Factor Patterns (ranked by count)

| event_type               | factor                          |   count_events |   share_of_events |
|:-------------------------|:--------------------------------|---------------:|------------------:|
| CFIT                     | plan_continuation_bias          |              5 |            0.1042 |
| Loss_of_Control          | plan_continuation_bias          |              4 |            0.0833 |
| Landing_Gear_Malfunction | maintenance_induced_failure     |              3 |            0.0625 |
| Loss_of_Control          | assumption_of_performance       |              3 |            0.0625 |
| Loss_of_Control          | informal_or_incomplete_training |              3 |            0.0625 |
| Loss_of_Control          | low_time_in_type                |              3 |            0.0625 |
| Loss_of_Control          | normalization_of_deviance       |              3 |            0.0625 |
| Fuel_Starvation          | checklist_non_compliance        |              2 |            0.0417 |
| Loss_of_Control          | checklist_non_compliance        |              2 |            0.0417 |
| Loss_of_Control          | icing_performance_degradation   |              2 |            0.0417 |
| Runway_Excursion         | assumption_of_performance       |              2 |            0.0417 |
| CFIT                     | icing_performance_degradation   |              1 |            0.0208 |
| CFIT                     | task_saturation                 |              1 |            0.0208 |
| Fuel_Exhaustion          | checklist_non_compliance        |              1 |            0.0208 |
| Fuel_Exhaustion          | plan_continuation_bias          |              1 |            0.0208 |

## Top 15 Operation Type × Factor Patterns (ranked by count)

|   operation_type | factor                               |   count_events |   share_of_events |
|-----------------:|:-------------------------------------|---------------:|------------------:|
|               91 | plan_continuation_bias               |             12 |            0.25   |
|               91 | checklist_non_compliance             |              7 |            0.1458 |
|               91 | assumption_of_performance            |              5 |            0.1042 |
|               91 | low_time_in_type                     |              4 |            0.0833 |
|               91 | normalization_of_deviance            |              4 |            0.0833 |
|               91 | icing_performance_degradation        |              3 |            0.0625 |
|               91 | informal_or_incomplete_training      |              3 |            0.0625 |
|               91 | maintenance_induced_failure          |              3 |            0.0625 |
|               91 | task_saturation                      |              3 |            0.0625 |
|               91 | density_altitude_underestimation     |              2 |            0.0417 |
|               91 | aging_aircraft_degradation           |              1 |            0.0208 |
|               91 | lapsed_recency                       |              1 |            0.0208 |
|               91 | single_engine_performance_assumption |              1 |            0.0208 |
|               91 | weight_balance_misjudgment           |              1 |            0.0208 |

## Unknown Factor Notes

- events_with_unknown_factor: 18
- unknown_factor_rate (assignment-based): 0.2647
