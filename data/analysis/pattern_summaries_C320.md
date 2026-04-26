# Ranked Pattern Summaries — Model C320

_Generated: 2026-04-26 00:45:21_

## Analysis Header (Required)

```
taxonomy_version: 1.3
dataset_size_total: 15
dataset_size_per_model: {'C320': 15}
unknown_factor_rate: 0.1
analysis_gate_status: Per-model gate scope for C320. Pattern summaries permitted within this model. Counts-only; no exposure-based rates without exposure data.
```

## Guardrails

- Rankings are **counts-only** (no exposure-based rates).
- Shares are labeled as **share_of_events** or **share_of_factor_assignments**.
- Interpret patterns as “appears more frequently in this dataset,” not “higher risk.”

## Baseline Severity Context (counts by model within this scope)

- total_events: 15
- fatal_events: 9
- serious_injury_events: 1
- destroyed_aircraft: 5

## Top 15 Event Types (ranked by count)

| event_type               |   count_events |   share_of_events |
|:-------------------------|---------------:|------------------:|
| Loss_of_Control          |              8 |            0.5333 |
| Landing_Gear_Malfunction |              4 |            0.2667 |
| Engine_Failure           |              2 |            0.1333 |
| CFIT                     |              1 |            0.0667 |

## Top 15 Phases of Flight (ranked by count)

| phase_of_flight   |   count_events |   share_of_events |
|:------------------|---------------:|------------------:|
| Approach          |              4 |            0.2667 |
| Initial_Climb     |              3 |            0.2    |
| Landing           |              3 |            0.2    |
| Cruise            |              3 |            0.2    |
| Takeoff           |              1 |            0.0667 |
| Taxi              |              1 |            0.0667 |

## Top 15 Operation Types (ranked by count)

|   operation_type |   count_events |   share_of_events |
|-----------------:|---------------:|------------------:|
|               91 |             15 |                 1 |

## Top 15 Phase × Event Type Patterns (ranked by count)

| phase_of_flight   | event_type               |   count_events |   share_of_events |
|:------------------|:-------------------------|---------------:|------------------:|
| Approach          | Loss_of_Control          |              4 |            0.2667 |
| Initial_Climb     | Loss_of_Control          |              2 |            0.1333 |
| Landing           | Landing_Gear_Malfunction |              2 |            0.1333 |
| Cruise            | CFIT                     |              1 |            0.0667 |
| Cruise            | Engine_Failure           |              1 |            0.0667 |
| Cruise            | Loss_of_Control          |              1 |            0.0667 |
| Initial_Climb     | Landing_Gear_Malfunction |              1 |            0.0667 |
| Landing           | Engine_Failure           |              1 |            0.0667 |
| Takeoff           | Loss_of_Control          |              1 |            0.0667 |
| Taxi              | Landing_Gear_Malfunction |              1 |            0.0667 |

## Top 15 Contributing Factors (ranked by events_with_factor)

| factor                               |   events_with_factor |   share_of_events |   share_of_factor_assignments |
|:-------------------------------------|---------------------:|------------------:|------------------------------:|
| plan_continuation_bias               |                    5 |            0.3333 |                        0.1852 |
| informal_or_incomplete_training      |                    4 |            0.2667 |                        0.1481 |
| aging_aircraft_degradation           |                    3 |            0.2    |                        0.1111 |
| maintenance_induced_failure          |                    3 |            0.2    |                        0.1111 |
| lapsed_recency                       |                    2 |            0.1333 |                        0.0741 |
| low_time_in_type                     |                    2 |            0.1333 |                        0.0741 |
| single_engine_performance_assumption |                    2 |            0.1333 |                        0.0741 |
| assumption_of_performance            |                    1 |            0.0667 |                        0.037  |
| checklist_non_compliance             |                    1 |            0.0667 |                        0.037  |
| density_altitude_underestimation     |                    1 |            0.0667 |                        0.037  |
| incomplete_troubleshooting           |                    1 |            0.0667 |                        0.037  |
| task_saturation                      |                    1 |            0.0667 |                        0.037  |
| weight_balance_misjudgment           |                    1 |            0.0667 |                        0.037  |
| deferred_discrepancy_normalization   |                    0 |            0      |                        0      |
| high_time_complacency                |                    0 |            0      |                        0      |

## Top 15 Phase × Factor Patterns (ranked by count)

| phase_of_flight   | factor                               |   count_events |   share_of_events |
|:------------------|:-------------------------------------|---------------:|------------------:|
| Landing           | aging_aircraft_degradation           |              3 |            0.2    |
| Approach          | plan_continuation_bias               |              2 |            0.1333 |
| Cruise            | informal_or_incomplete_training      |              2 |            0.1333 |
| Cruise            | plan_continuation_bias               |              2 |            0.1333 |
| Approach          | checklist_non_compliance             |              1 |            0.0667 |
| Approach          | incomplete_troubleshooting           |              1 |            0.0667 |
| Approach          | informal_or_incomplete_training      |              1 |            0.0667 |
| Approach          | single_engine_performance_assumption |              1 |            0.0667 |
| Approach          | task_saturation                      |              1 |            0.0667 |
| Cruise            | lapsed_recency                       |              1 |            0.0667 |
| Initial_Climb     | assumption_of_performance            |              1 |            0.0667 |
| Initial_Climb     | density_altitude_underestimation     |              1 |            0.0667 |
| Initial_Climb     | informal_or_incomplete_training      |              1 |            0.0667 |
| Initial_Climb     | lapsed_recency                       |              1 |            0.0667 |
| Initial_Climb     | low_time_in_type                     |              1 |            0.0667 |

## Top 15 Event Type × Factor Patterns (ranked by count)

| event_type               | factor                               |   count_events |   share_of_events |
|:-------------------------|:-------------------------------------|---------------:|------------------:|
| Loss_of_Control          | plan_continuation_bias               |              4 |            0.2667 |
| Loss_of_Control          | informal_or_incomplete_training      |              3 |            0.2    |
| Landing_Gear_Malfunction | aging_aircraft_degradation           |              2 |            0.1333 |
| Landing_Gear_Malfunction | maintenance_induced_failure          |              2 |            0.1333 |
| CFIT                     | informal_or_incomplete_training      |              1 |            0.0667 |
| CFIT                     | plan_continuation_bias               |              1 |            0.0667 |
| Engine_Failure           | aging_aircraft_degradation           |              1 |            0.0667 |
| Engine_Failure           | maintenance_induced_failure          |              1 |            0.0667 |
| Engine_Failure           | single_engine_performance_assumption |              1 |            0.0667 |
| Landing_Gear_Malfunction | lapsed_recency                       |              1 |            0.0667 |
| Landing_Gear_Malfunction | low_time_in_type                     |              1 |            0.0667 |
| Loss_of_Control          | assumption_of_performance            |              1 |            0.0667 |
| Loss_of_Control          | checklist_non_compliance             |              1 |            0.0667 |
| Loss_of_Control          | density_altitude_underestimation     |              1 |            0.0667 |
| Loss_of_Control          | incomplete_troubleshooting           |              1 |            0.0667 |

## Top 15 Operation Type × Factor Patterns (ranked by count)

|   operation_type | factor                               |   count_events |   share_of_events |
|-----------------:|:-------------------------------------|---------------:|------------------:|
|               91 | plan_continuation_bias               |              5 |            0.3333 |
|               91 | informal_or_incomplete_training      |              4 |            0.2667 |
|               91 | aging_aircraft_degradation           |              3 |            0.2    |
|               91 | maintenance_induced_failure          |              3 |            0.2    |
|               91 | lapsed_recency                       |              2 |            0.1333 |
|               91 | low_time_in_type                     |              2 |            0.1333 |
|               91 | single_engine_performance_assumption |              2 |            0.1333 |
|               91 | assumption_of_performance            |              1 |            0.0667 |
|               91 | checklist_non_compliance             |              1 |            0.0667 |
|               91 | density_altitude_underestimation     |              1 |            0.0667 |
|               91 | incomplete_troubleshooting           |              1 |            0.0667 |
|               91 | task_saturation                      |              1 |            0.0667 |
|               91 | weight_balance_misjudgment           |              1 |            0.0667 |

## Unknown Factor Notes

- events_with_unknown_factor: 3
- unknown_factor_rate (assignment-based): 0.1
