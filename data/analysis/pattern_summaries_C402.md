# Ranked Pattern Summaries — Model C402

_Generated: 2026-02-22 14:44:10_

## Analysis Header (Required)

```
taxonomy_version: 1.3
dataset_size_total: 27
dataset_size_per_model: {'C402': 27}
unknown_factor_rate: 0.4375
analysis_gate_status: Per-model gate scope for C402. Pattern summaries permitted within this model. Counts-only; no exposure-based rates without exposure data.
```

## Guardrails

- Rankings are **counts-only** (no exposure-based rates).
- Shares are labeled as **share_of_events** or **share_of_factor_assignments**.
- Interpret patterns as “appears more frequently in this dataset,” not “higher risk.”

## Baseline Severity Context (counts by model within this scope)

- total_events: 27
- fatal_events: 2
- serious_injury_events: 2
- destroyed_aircraft: 1

## Top 15 Event Types (ranked by count)

| event_type               |   count_events |   share_of_events |
|:-------------------------|---------------:|------------------:|
| Landing_Gear_Malfunction |             11 |            0.4074 |
| Runway_Excursion         |              3 |            0.1111 |
| Fuel_Starvation          |              3 |            0.1111 |
| Ground_Collision         |              2 |            0.0741 |
| Engine_Failure           |              2 |            0.0741 |
| Loss_of_Control          |              2 |            0.0741 |
| Other                    |              1 |            0.037  |
| Fuel_Exhaustion          |              1 |            0.037  |
| Hard_Landing             |              1 |            0.037  |
| System_Malfunction       |              1 |            0.037  |

## Top 15 Phases of Flight (ranked by count)

| phase_of_flight   |   count_events |   share_of_events |
|:------------------|---------------:|------------------:|
| Landing           |             14 |            0.5185 |
| Cruise            |              3 |            0.1111 |
| Taxi              |              2 |            0.0741 |
| Initial_Climb     |              2 |            0.0741 |
| Approach          |              2 |            0.0741 |
| Takeoff           |              2 |            0.0741 |
| Unknown           |              2 |            0.0741 |

## Top 15 Operation Types (ranked by count)

|   operation_type |   count_events |   share_of_events |
|-----------------:|---------------:|------------------:|
|              135 |             17 |            0.6296 |
|               91 |             10 |            0.3704 |

## Top 15 Phase × Event Type Patterns (ranked by count)

| phase_of_flight   | event_type               |   count_events |   share_of_events |
|:------------------|:-------------------------|---------------:|------------------:|
| Landing           | Landing_Gear_Malfunction |             11 |            0.4074 |
| Landing           | Runway_Excursion         |              2 |            0.0741 |
| Taxi              | Ground_Collision         |              2 |            0.0741 |
| Approach          | Fuel_Exhaustion          |              1 |            0.037  |
| Approach          | Loss_of_Control          |              1 |            0.037  |
| Cruise            | Engine_Failure           |              1 |            0.037  |
| Cruise            | Fuel_Starvation          |              1 |            0.037  |
| Cruise            | Other                    |              1 |            0.037  |
| Initial_Climb     | Fuel_Starvation          |              1 |            0.037  |
| Initial_Climb     | Loss_of_Control          |              1 |            0.037  |
| Landing           | Hard_Landing             |              1 |            0.037  |
| Takeoff           | Engine_Failure           |              1 |            0.037  |
| Takeoff           | Runway_Excursion         |              1 |            0.037  |
| Unknown           | Fuel_Starvation          |              1 |            0.037  |
| Unknown           | System_Malfunction       |              1 |            0.037  |

## Top 15 Contributing Factors (ranked by events_with_factor)

| factor                             |   events_with_factor |   share_of_events |   share_of_factor_assignments |
|:-----------------------------------|---------------------:|------------------:|------------------------------:|
| plan_continuation_bias             |                    6 |            0.2222 |                        0.3333 |
| maintenance_induced_failure        |                    3 |            0.1111 |                        0.1667 |
| aging_aircraft_degradation         |                    2 |            0.0741 |                        0.1111 |
| checklist_non_compliance           |                    2 |            0.0741 |                        0.1111 |
| deferred_discrepancy_normalization |                    1 |            0.037  |                        0.0556 |
| icing_performance_degradation      |                    1 |            0.037  |                        0.0556 |
| incomplete_troubleshooting         |                    1 |            0.037  |                        0.0556 |
| low_time_in_type                   |                    1 |            0.037  |                        0.0556 |
| task_saturation                    |                    1 |            0.037  |                        0.0556 |
| assumption_of_performance          |                    0 |            0      |                        0      |
| density_altitude_underestimation   |                    0 |            0      |                        0      |
| high_time_complacency              |                    0 |            0      |                        0      |
| informal_or_incomplete_training    |                    0 |            0      |                        0      |
| lapsed_recency                     |                    0 |            0      |                        0      |
| normalization_of_deviance          |                    0 |            0      |                        0      |

## Top 15 Phase × Factor Patterns (ranked by count)

| phase_of_flight   | factor                             |   count_events |   share_of_events |
|:------------------|:-----------------------------------|---------------:|------------------:|
| Landing           | plan_continuation_bias             |              3 |            0.1111 |
| Landing           | aging_aircraft_degradation         |              2 |            0.0741 |
| Landing           | maintenance_induced_failure        |              2 |            0.0741 |
| Approach          | plan_continuation_bias             |              1 |            0.037  |
| Cruise            | checklist_non_compliance           |              1 |            0.037  |
| Cruise            | maintenance_induced_failure        |              1 |            0.037  |
| Cruise            | plan_continuation_bias             |              1 |            0.037  |
| Landing           | checklist_non_compliance           |              1 |            0.037  |
| Landing           | deferred_discrepancy_normalization |              1 |            0.037  |
| Landing           | icing_performance_degradation      |              1 |            0.037  |
| Landing           | incomplete_troubleshooting         |              1 |            0.037  |
| Landing           | low_time_in_type                   |              1 |            0.037  |
| Landing           | task_saturation                    |              1 |            0.037  |
| Takeoff           | plan_continuation_bias             |              1 |            0.037  |

## Top 15 Event Type × Factor Patterns (ranked by count)

| event_type               | factor                             |   count_events |   share_of_events |
|:-------------------------|:-----------------------------------|---------------:|------------------:|
| Runway_Excursion         | plan_continuation_bias             |              3 |            0.1111 |
| Landing_Gear_Malfunction | aging_aircraft_degradation         |              2 |            0.0741 |
| Landing_Gear_Malfunction | maintenance_induced_failure        |              2 |            0.0741 |
| Fuel_Exhaustion          | plan_continuation_bias             |              1 |            0.037  |
| Fuel_Starvation          | checklist_non_compliance           |              1 |            0.037  |
| Fuel_Starvation          | maintenance_induced_failure        |              1 |            0.037  |
| Hard_Landing             | icing_performance_degradation      |              1 |            0.037  |
| Hard_Landing             | low_time_in_type                   |              1 |            0.037  |
| Hard_Landing             | plan_continuation_bias             |              1 |            0.037  |
| Landing_Gear_Malfunction | checklist_non_compliance           |              1 |            0.037  |
| Landing_Gear_Malfunction | deferred_discrepancy_normalization |              1 |            0.037  |
| Landing_Gear_Malfunction | incomplete_troubleshooting         |              1 |            0.037  |
| Other                    | plan_continuation_bias             |              1 |            0.037  |
| Runway_Excursion         | task_saturation                    |              1 |            0.037  |

## Top 15 Operation Type × Factor Patterns (ranked by count)

|   operation_type | factor                             |   count_events |   share_of_events |
|-----------------:|:-----------------------------------|---------------:|------------------:|
|              135 | plan_continuation_bias             |              4 |            0.1481 |
|              135 | maintenance_induced_failure        |              3 |            0.1111 |
|              135 | checklist_non_compliance           |              2 |            0.0741 |
|               91 | plan_continuation_bias             |              2 |            0.0741 |
|              135 | aging_aircraft_degradation         |              1 |            0.037  |
|              135 | deferred_discrepancy_normalization |              1 |            0.037  |
|              135 | icing_performance_degradation      |              1 |            0.037  |
|              135 | incomplete_troubleshooting         |              1 |            0.037  |
|              135 | low_time_in_type                   |              1 |            0.037  |
|              135 | task_saturation                    |              1 |            0.037  |
|               91 | aging_aircraft_degradation         |              1 |            0.037  |

## Unknown Factor Notes

- events_with_unknown_factor: 14
- unknown_factor_rate (assignment-based): 0.4375
