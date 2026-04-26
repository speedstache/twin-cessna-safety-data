# Ranked Pattern Summaries — Model C402

_Generated: 2026-04-26 00:45:21_

## Analysis Header (Required)

```
taxonomy_version: 1.3
dataset_size_total: 49
dataset_size_per_model: {'C402': 49}
unknown_factor_rate: 0.3548
analysis_gate_status: Per-model gate scope for C402. Pattern summaries permitted within this model. Counts-only; no exposure-based rates without exposure data.
```

## Guardrails

- Rankings are **counts-only** (no exposure-based rates).
- Shares are labeled as **share_of_events** or **share_of_factor_assignments**.
- Interpret patterns as “appears more frequently in this dataset,” not “higher risk.”

## Baseline Severity Context (counts by model within this scope)

- total_events: 49
- fatal_events: 2
- serious_injury_events: 4
- destroyed_aircraft: 1

## Top 15 Event Types (ranked by count)

| event_type               |   count_events |   share_of_events |
|:-------------------------|---------------:|------------------:|
| Landing_Gear_Malfunction |             15 |            0.3061 |
| Runway_Excursion         |              9 |            0.1837 |
| Other                    |              6 |            0.1224 |
| Fuel_Starvation          |              4 |            0.0816 |
| Engine_Failure           |              3 |            0.0612 |
| Fuel_Exhaustion          |              3 |            0.0612 |
| System_Malfunction       |              3 |            0.0612 |
| Ground_Collision         |              2 |            0.0408 |
| Loss_of_Control          |              2 |            0.0408 |
| Hard_Landing             |              1 |            0.0204 |
| Fire                     |              1 |            0.0204 |

## Top 15 Phases of Flight (ranked by count)

| phase_of_flight   |   count_events |   share_of_events |
|:------------------|---------------:|------------------:|
| Landing           |             21 |            0.4286 |
| Approach          |              7 |            0.1429 |
| Initial_Climb     |              6 |            0.1224 |
| Takeoff           |              5 |            0.102  |
| Cruise            |              4 |            0.0816 |
| Taxi              |              2 |            0.0408 |
| Unknown           |              2 |            0.0408 |
| Descent           |              1 |            0.0204 |
| Go_Around         |              1 |            0.0204 |

## Top 15 Operation Types (ranked by count)

|   operation_type |   count_events |   share_of_events |
|-----------------:|---------------:|------------------:|
|              135 |             29 |            0.5918 |
|               91 |             20 |            0.4082 |

## Top 15 Phase × Event Type Patterns (ranked by count)

| phase_of_flight   | event_type               |   count_events |   share_of_events |
|:------------------|:-------------------------|---------------:|------------------:|
| Landing           | Landing_Gear_Malfunction |             14 |            0.2857 |
| Landing           | Runway_Excursion         |              6 |            0.1224 |
| Approach          | Fuel_Exhaustion          |              3 |            0.0612 |
| Approach          | Other                    |              2 |            0.0408 |
| Cruise            | Other                    |              2 |            0.0408 |
| Initial_Climb     | Fuel_Starvation          |              2 |            0.0408 |
| Takeoff           | Engine_Failure           |              2 |            0.0408 |
| Takeoff           | Runway_Excursion         |              2 |            0.0408 |
| Taxi              | Ground_Collision         |              2 |            0.0408 |
| Approach          | Fire                     |              1 |            0.0204 |
| Approach          | Loss_of_Control          |              1 |            0.0204 |
| Cruise            | Engine_Failure           |              1 |            0.0204 |
| Cruise            | Fuel_Starvation          |              1 |            0.0204 |
| Descent           | Other                    |              1 |            0.0204 |
| Go_Around         | Runway_Excursion         |              1 |            0.0204 |

## Top 15 Contributing Factors (ranked by events_with_factor)

| factor                             |   events_with_factor |   share_of_events |   share_of_factor_assignments |
|:-----------------------------------|---------------------:|------------------:|------------------------------:|
| checklist_non_compliance           |                   10 |            0.2041 |                         0.25  |
| plan_continuation_bias             |                    9 |            0.1837 |                         0.225 |
| aging_aircraft_degradation         |                    6 |            0.1224 |                         0.15  |
| maintenance_induced_failure        |                    5 |            0.102  |                         0.125 |
| low_time_in_type                   |                    3 |            0.0612 |                         0.075 |
| assumption_of_performance          |                    2 |            0.0408 |                         0.05  |
| deferred_discrepancy_normalization |                    1 |            0.0204 |                         0.025 |
| icing_performance_degradation      |                    1 |            0.0204 |                         0.025 |
| incomplete_troubleshooting         |                    1 |            0.0204 |                         0.025 |
| lapsed_recency                     |                    1 |            0.0204 |                         0.025 |
| task_saturation                    |                    1 |            0.0204 |                         0.025 |
| density_altitude_underestimation   |                    0 |            0      |                         0     |
| high_time_complacency              |                    0 |            0      |                         0     |
| informal_or_incomplete_training    |                    0 |            0      |                         0     |
| normalization_of_deviance          |                    0 |            0      |                         0     |

## Top 15 Phase × Factor Patterns (ranked by count)

| phase_of_flight   | factor                      |   count_events |   share_of_events |
|:------------------|:----------------------------|---------------:|------------------:|
| Landing           | plan_continuation_bias      |              5 |            0.102  |
| Landing           | aging_aircraft_degradation  |              4 |            0.0816 |
| Initial_Climb     | checklist_non_compliance    |              3 |            0.0612 |
| Landing           | maintenance_induced_failure |              3 |            0.0612 |
| Approach          | checklist_non_compliance    |              2 |            0.0408 |
| Takeoff           | checklist_non_compliance    |              2 |            0.0408 |
| Approach          | aging_aircraft_degradation  |              1 |            0.0204 |
| Approach          | low_time_in_type            |              1 |            0.0204 |
| Approach          | plan_continuation_bias      |              1 |            0.0204 |
| Cruise            | checklist_non_compliance    |              1 |            0.0204 |
| Cruise            | maintenance_induced_failure |              1 |            0.0204 |
| Cruise            | plan_continuation_bias      |              1 |            0.0204 |
| Go_Around         | assumption_of_performance   |              1 |            0.0204 |
| Go_Around         | checklist_non_compliance    |              1 |            0.0204 |
| Go_Around         | plan_continuation_bias      |              1 |            0.0204 |

## Top 15 Event Type × Factor Patterns (ranked by count)

| event_type               | factor                        |   count_events |   share_of_events |
|:-------------------------|:------------------------------|---------------:|------------------:|
| Runway_Excursion         | plan_continuation_bias        |              6 |            0.1224 |
| Landing_Gear_Malfunction | aging_aircraft_degradation    |              5 |            0.102  |
| Landing_Gear_Malfunction | maintenance_induced_failure   |              3 |            0.0612 |
| Fuel_Exhaustion          | checklist_non_compliance      |              2 |            0.0408 |
| Fuel_Starvation          | checklist_non_compliance      |              2 |            0.0408 |
| Landing_Gear_Malfunction | checklist_non_compliance      |              2 |            0.0408 |
| Runway_Excursion         | assumption_of_performance     |              2 |            0.0408 |
| Runway_Excursion         | checklist_non_compliance      |              2 |            0.0408 |
| System_Malfunction       | checklist_non_compliance      |              2 |            0.0408 |
| Fire                     | aging_aircraft_degradation    |              1 |            0.0204 |
| Fuel_Exhaustion          | low_time_in_type              |              1 |            0.0204 |
| Fuel_Exhaustion          | plan_continuation_bias        |              1 |            0.0204 |
| Fuel_Starvation          | low_time_in_type              |              1 |            0.0204 |
| Fuel_Starvation          | maintenance_induced_failure   |              1 |            0.0204 |
| Hard_Landing             | icing_performance_degradation |              1 |            0.0204 |

## Top 15 Operation Type × Factor Patterns (ranked by count)

|   operation_type | factor                             |   count_events |   share_of_events |
|-----------------:|:-----------------------------------|---------------:|------------------:|
|              135 | plan_continuation_bias             |              7 |            0.1429 |
|              135 | checklist_non_compliance           |              6 |            0.1224 |
|               91 | checklist_non_compliance           |              4 |            0.0816 |
|              135 | aging_aircraft_degradation         |              3 |            0.0612 |
|              135 | maintenance_induced_failure        |              3 |            0.0612 |
|               91 | aging_aircraft_degradation         |              3 |            0.0612 |
|              135 | low_time_in_type                   |              2 |            0.0408 |
|               91 | maintenance_induced_failure        |              2 |            0.0408 |
|               91 | plan_continuation_bias             |              2 |            0.0408 |
|              135 | assumption_of_performance          |              1 |            0.0204 |
|              135 | deferred_discrepancy_normalization |              1 |            0.0204 |
|              135 | icing_performance_degradation      |              1 |            0.0204 |
|              135 | incomplete_troubleshooting         |              1 |            0.0204 |
|              135 | task_saturation                    |              1 |            0.0204 |
|               91 | assumption_of_performance          |              1 |            0.0204 |

## Unknown Factor Notes

- events_with_unknown_factor: 22
- unknown_factor_rate (assignment-based): 0.3548
