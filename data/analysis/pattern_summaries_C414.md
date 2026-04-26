# Ranked Pattern Summaries — Model C414

_Generated: 2026-04-26 00:45:22_

## Analysis Header (Required)

```
taxonomy_version: 1.3
dataset_size_total: 37
dataset_size_per_model: {'C414': 37}
unknown_factor_rate: 0.2321
analysis_gate_status: Per-model gate scope for C414. Pattern summaries permitted within this model. Counts-only; no exposure-based rates without exposure data.
```

## Guardrails

- Rankings are **counts-only** (no exposure-based rates).
- Shares are labeled as **share_of_events** or **share_of_factor_assignments**.
- Interpret patterns as “appears more frequently in this dataset,” not “higher risk.”

## Baseline Severity Context (counts by model within this scope)

- total_events: 37
- fatal_events: 14
- serious_injury_events: 5
- destroyed_aircraft: 12

## Top 15 Event Types (ranked by count)

| event_type               |   count_events |   share_of_events |
|:-------------------------|---------------:|------------------:|
| Loss_of_Control          |             12 |            0.3243 |
| Landing_Gear_Malfunction |              7 |            0.1892 |
| Runway_Excursion         |              7 |            0.1892 |
| CFIT                     |              3 |            0.0811 |
| Other                    |              2 |            0.0541 |
| Engine_Failure           |              2 |            0.0541 |
| Fuel_Exhaustion          |              1 |            0.027  |
| Fuel_Starvation          |              1 |            0.027  |
| Hard_Landing             |              1 |            0.027  |
| System_Malfunction       |              1 |            0.027  |

## Top 15 Phases of Flight (ranked by count)

| phase_of_flight   |   count_events |   share_of_events |
|:------------------|---------------:|------------------:|
| Approach          |             12 |            0.3243 |
| Landing           |             12 |            0.3243 |
| Initial_Climb     |              5 |            0.1351 |
| Takeoff           |              5 |            0.1351 |
| Go_Around         |              2 |            0.0541 |
| Descent           |              1 |            0.027  |

## Top 15 Operation Types (ranked by count)

|   operation_type |   count_events |   share_of_events |
|-----------------:|---------------:|------------------:|
|               91 |             36 |             0.973 |
|              135 |              1 |             0.027 |

## Top 15 Phase × Event Type Patterns (ranked by count)

| phase_of_flight   | event_type               |   count_events |   share_of_events |
|:------------------|:-------------------------|---------------:|------------------:|
| Approach          | Loss_of_Control          |              7 |            0.1892 |
| Landing           | Landing_Gear_Malfunction |              7 |            0.1892 |
| Landing           | Runway_Excursion         |              4 |            0.1081 |
| Takeoff           | Runway_Excursion         |              3 |            0.0811 |
| Approach          | CFIT                     |              2 |            0.0541 |
| Go_Around         | Loss_of_Control          |              2 |            0.0541 |
| Initial_Climb     | Loss_of_Control          |              2 |            0.0541 |
| Approach          | Fuel_Exhaustion          |              1 |            0.027  |
| Approach          | Fuel_Starvation          |              1 |            0.027  |
| Approach          | Other                    |              1 |            0.027  |
| Descent           | Engine_Failure           |              1 |            0.027  |
| Initial_Climb     | CFIT                     |              1 |            0.027  |
| Initial_Climb     | Engine_Failure           |              1 |            0.027  |
| Initial_Climb     | Other                    |              1 |            0.027  |
| Landing           | Hard_Landing             |              1 |            0.027  |

## Top 15 Contributing Factors (ranked by events_with_factor)

| factor                               |   events_with_factor |   share_of_events |   share_of_factor_assignments |
|:-------------------------------------|---------------------:|------------------:|------------------------------:|
| plan_continuation_bias               |                   12 |            0.3243 |                        0.2791 |
| checklist_non_compliance             |                    8 |            0.2162 |                        0.186  |
| aging_aircraft_degradation           |                    3 |            0.0811 |                        0.0698 |
| low_time_in_type                     |                    3 |            0.0811 |                        0.0698 |
| task_saturation                      |                    3 |            0.0811 |                        0.0698 |
| assumption_of_performance            |                    2 |            0.0541 |                        0.0465 |
| icing_performance_degradation        |                    2 |            0.0541 |                        0.0465 |
| lapsed_recency                       |                    2 |            0.0541 |                        0.0465 |
| maintenance_induced_failure          |                    2 |            0.0541 |                        0.0465 |
| deferred_discrepancy_normalization   |                    1 |            0.027  |                        0.0233 |
| high_time_complacency                |                    1 |            0.027  |                        0.0233 |
| incomplete_troubleshooting           |                    1 |            0.027  |                        0.0233 |
| informal_or_incomplete_training      |                    1 |            0.027  |                        0.0233 |
| single_engine_performance_assumption |                    1 |            0.027  |                        0.0233 |
| weight_balance_misjudgment           |                    1 |            0.027  |                        0.0233 |

## Top 15 Phase × Factor Patterns (ranked by count)

| phase_of_flight   | factor                               |   count_events |   share_of_events |
|:------------------|:-------------------------------------|---------------:|------------------:|
| Approach          | plan_continuation_bias               |              6 |            0.1622 |
| Approach          | checklist_non_compliance             |              4 |            0.1081 |
| Initial_Climb     | plan_continuation_bias               |              3 |            0.0811 |
| Landing           | aging_aircraft_degradation           |              3 |            0.0811 |
| Approach          | task_saturation                      |              2 |            0.0541 |
| Initial_Climb     | low_time_in_type                     |              2 |            0.0541 |
| Takeoff           | checklist_non_compliance             |              2 |            0.0541 |
| Approach          | assumption_of_performance            |              1 |            0.027  |
| Approach          | high_time_complacency                |              1 |            0.027  |
| Approach          | icing_performance_degradation        |              1 |            0.027  |
| Approach          | informal_or_incomplete_training      |              1 |            0.027  |
| Approach          | lapsed_recency                       |              1 |            0.027  |
| Approach          | low_time_in_type                     |              1 |            0.027  |
| Approach          | single_engine_performance_assumption |              1 |            0.027  |
| Approach          | weight_balance_misjudgment           |              1 |            0.027  |

## Top 15 Event Type × Factor Patterns (ranked by count)

| event_type               | factor                             |   count_events |   share_of_events |
|:-------------------------|:-----------------------------------|---------------:|------------------:|
| Loss_of_Control          | plan_continuation_bias             |              6 |            0.1622 |
| Loss_of_Control          | checklist_non_compliance           |              4 |            0.1081 |
| CFIT                     | plan_continuation_bias             |              3 |            0.0811 |
| Landing_Gear_Malfunction | aging_aircraft_degradation         |              2 |            0.0541 |
| Loss_of_Control          | icing_performance_degradation      |              2 |            0.0541 |
| Loss_of_Control          | task_saturation                    |              2 |            0.0541 |
| CFIT                     | checklist_non_compliance           |              1 |            0.027  |
| CFIT                     | low_time_in_type                   |              1 |            0.027  |
| Fuel_Starvation          | checklist_non_compliance           |              1 |            0.027  |
| Hard_Landing             | lapsed_recency                     |              1 |            0.027  |
| Landing_Gear_Malfunction | checklist_non_compliance           |              1 |            0.027  |
| Landing_Gear_Malfunction | deferred_discrepancy_normalization |              1 |            0.027  |
| Landing_Gear_Malfunction | maintenance_induced_failure        |              1 |            0.027  |
| Landing_Gear_Malfunction | plan_continuation_bias             |              1 |            0.027  |
| Landing_Gear_Malfunction | task_saturation                    |              1 |            0.027  |

## Top 15 Operation Type × Factor Patterns (ranked by count)

|   operation_type | factor                               |   count_events |   share_of_events |
|-----------------:|:-------------------------------------|---------------:|------------------:|
|               91 | plan_continuation_bias               |             12 |            0.3243 |
|               91 | checklist_non_compliance             |              8 |            0.2162 |
|               91 | aging_aircraft_degradation           |              3 |            0.0811 |
|               91 | low_time_in_type                     |              3 |            0.0811 |
|               91 | task_saturation                      |              3 |            0.0811 |
|               91 | assumption_of_performance            |              2 |            0.0541 |
|               91 | icing_performance_degradation        |              2 |            0.0541 |
|               91 | lapsed_recency                       |              2 |            0.0541 |
|               91 | maintenance_induced_failure          |              2 |            0.0541 |
|               91 | deferred_discrepancy_normalization   |              1 |            0.027  |
|               91 | high_time_complacency                |              1 |            0.027  |
|               91 | incomplete_troubleshooting           |              1 |            0.027  |
|               91 | informal_or_incomplete_training      |              1 |            0.027  |
|               91 | single_engine_performance_assumption |              1 |            0.027  |
|               91 | weight_balance_misjudgment           |              1 |            0.027  |

## Unknown Factor Notes

- events_with_unknown_factor: 13
- unknown_factor_rate (assignment-based): 0.2321
