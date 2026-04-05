# Ranked Pattern Summaries — Model C340

_Generated: 2026-04-05 00:15:29_

## Analysis Header (Required)

```
taxonomy_version: 1.3
dataset_size_total: 27
dataset_size_per_model: {'C340': 27}
unknown_factor_rate: 0.3125
analysis_gate_status: Per-model gate scope for C340. Pattern summaries permitted within this model. Counts-only; no exposure-based rates without exposure data.
```

## Guardrails

- Rankings are **counts-only** (no exposure-based rates).
- Shares are labeled as **share_of_events** or **share_of_factor_assignments**.
- Interpret patterns as “appears more frequently in this dataset,” not “higher risk.”

## Baseline Severity Context (counts by model within this scope)

- total_events: 27
- fatal_events: 14
- serious_injury_events: 1
- destroyed_aircraft: 10

## Top 15 Event Types (ranked by count)

| event_type               |   count_events |   share_of_events |
|:-------------------------|---------------:|------------------:|
| Loss_of_Control          |              9 |            0.3333 |
| CFIT                     |              5 |            0.1852 |
| Landing_Gear_Malfunction |              4 |            0.1481 |
| Runway_Excursion         |              4 |            0.1481 |
| Fuel_Starvation          |              2 |            0.0741 |
| Ground_Collision         |              2 |            0.0741 |
| Fire                     |              1 |            0.037  |

## Top 15 Phases of Flight (ranked by count)

| phase_of_flight   |   count_events |   share_of_events |
|:------------------|---------------:|------------------:|
| Approach          |             11 |            0.4074 |
| Landing           |              7 |            0.2593 |
| Cruise            |              4 |            0.1481 |
| Initial_Climb     |              3 |            0.1111 |
| Go_Around         |              1 |            0.037  |
| Takeoff           |              1 |            0.037  |

## Top 15 Operation Types (ranked by count)

|   operation_type |   count_events |   share_of_events |
|-----------------:|---------------:|------------------:|
|               91 |             27 |                 1 |

## Top 15 Phase × Event Type Patterns (ranked by count)

| phase_of_flight   | event_type               |   count_events |   share_of_events |
|:------------------|:-------------------------|---------------:|------------------:|
| Approach          | Loss_of_Control          |              5 |            0.1852 |
| Approach          | CFIT                     |              3 |            0.1111 |
| Initial_Climb     | Loss_of_Control          |              3 |            0.1111 |
| Landing           | Landing_Gear_Malfunction |              3 |            0.1111 |
| Landing           | Runway_Excursion         |              3 |            0.1111 |
| Cruise            | CFIT                     |              2 |            0.0741 |
| Approach          | Fire                     |              1 |            0.037  |
| Approach          | Fuel_Starvation          |              1 |            0.037  |
| Approach          | Landing_Gear_Malfunction |              1 |            0.037  |
| Cruise            | Fuel_Starvation          |              1 |            0.037  |
| Cruise            | Ground_Collision         |              1 |            0.037  |
| Go_Around         | Loss_of_Control          |              1 |            0.037  |
| Landing           | Ground_Collision         |              1 |            0.037  |
| Takeoff           | Runway_Excursion         |              1 |            0.037  |

## Top 15 Contributing Factors (ranked by events_with_factor)

| factor                             |   events_with_factor |   share_of_events |   share_of_factor_assignments |
|:-----------------------------------|---------------------:|------------------:|------------------------------:|
| plan_continuation_bias             |                    5 |            0.1852 |                        0.2273 |
| assumption_of_performance          |                    4 |            0.1481 |                        0.1818 |
| checklist_non_compliance           |                    2 |            0.0741 |                        0.0909 |
| icing_performance_degradation      |                    2 |            0.0741 |                        0.0909 |
| low_time_in_type                   |                    2 |            0.0741 |                        0.0909 |
| maintenance_induced_failure        |                    2 |            0.0741 |                        0.0909 |
| normalization_of_deviance          |                    2 |            0.0741 |                        0.0909 |
| informal_or_incomplete_training    |                    1 |            0.037  |                        0.0455 |
| lapsed_recency                     |                    1 |            0.037  |                        0.0455 |
| task_saturation                    |                    1 |            0.037  |                        0.0455 |
| aging_aircraft_degradation         |                    0 |            0      |                        0      |
| deferred_discrepancy_normalization |                    0 |            0      |                        0      |
| density_altitude_underestimation   |                    0 |            0      |                        0      |
| high_time_complacency              |                    0 |            0      |                        0      |
| incomplete_troubleshooting         |                    0 |            0      |                        0      |

## Top 15 Phase × Factor Patterns (ranked by count)

| phase_of_flight   | factor                          |   count_events |   share_of_events |
|:------------------|:--------------------------------|---------------:|------------------:|
| Approach          | icing_performance_degradation   |              2 |            0.0741 |
| Approach          | low_time_in_type                |              2 |            0.0741 |
| Approach          | plan_continuation_bias          |              2 |            0.0741 |
| Cruise            | plan_continuation_bias          |              2 |            0.0741 |
| Initial_Climb     | assumption_of_performance       |              2 |            0.0741 |
| Landing           | assumption_of_performance       |              2 |            0.0741 |
| Landing           | maintenance_induced_failure     |              2 |            0.0741 |
| Approach          | checklist_non_compliance        |              1 |            0.037  |
| Approach          | lapsed_recency                  |              1 |            0.037  |
| Approach          | normalization_of_deviance       |              1 |            0.037  |
| Cruise            | checklist_non_compliance        |              1 |            0.037  |
| Cruise            | normalization_of_deviance       |              1 |            0.037  |
| Go_Around         | informal_or_incomplete_training |              1 |            0.037  |
| Initial_Climb     | plan_continuation_bias          |              1 |            0.037  |
| Initial_Climb     | task_saturation                 |              1 |            0.037  |

## Top 15 Event Type × Factor Patterns (ranked by count)

| event_type               | factor                          |   count_events |   share_of_events |
|:-------------------------|:--------------------------------|---------------:|------------------:|
| CFIT                     | plan_continuation_bias          |              4 |            0.1481 |
| Landing_Gear_Malfunction | maintenance_induced_failure     |              2 |            0.0741 |
| Loss_of_Control          | assumption_of_performance       |              2 |            0.0741 |
| Loss_of_Control          | low_time_in_type                |              2 |            0.0741 |
| Runway_Excursion         | assumption_of_performance       |              2 |            0.0741 |
| CFIT                     | icing_performance_degradation   |              1 |            0.037  |
| Fuel_Starvation          | checklist_non_compliance        |              1 |            0.037  |
| Ground_Collision         | normalization_of_deviance       |              1 |            0.037  |
| Loss_of_Control          | checklist_non_compliance        |              1 |            0.037  |
| Loss_of_Control          | icing_performance_degradation   |              1 |            0.037  |
| Loss_of_Control          | informal_or_incomplete_training |              1 |            0.037  |
| Loss_of_Control          | lapsed_recency                  |              1 |            0.037  |
| Loss_of_Control          | normalization_of_deviance       |              1 |            0.037  |
| Loss_of_Control          | plan_continuation_bias          |              1 |            0.037  |
| Loss_of_Control          | task_saturation                 |              1 |            0.037  |

## Top 15 Operation Type × Factor Patterns (ranked by count)

|   operation_type | factor                          |   count_events |   share_of_events |
|-----------------:|:--------------------------------|---------------:|------------------:|
|               91 | plan_continuation_bias          |              5 |            0.1852 |
|               91 | assumption_of_performance       |              4 |            0.1481 |
|               91 | checklist_non_compliance        |              2 |            0.0741 |
|               91 | icing_performance_degradation   |              2 |            0.0741 |
|               91 | low_time_in_type                |              2 |            0.0741 |
|               91 | maintenance_induced_failure     |              2 |            0.0741 |
|               91 | normalization_of_deviance       |              2 |            0.0741 |
|               91 | informal_or_incomplete_training |              1 |            0.037  |
|               91 | lapsed_recency                  |              1 |            0.037  |
|               91 | task_saturation                 |              1 |            0.037  |

## Unknown Factor Notes

- events_with_unknown_factor: 10
- unknown_factor_rate (assignment-based): 0.3125
