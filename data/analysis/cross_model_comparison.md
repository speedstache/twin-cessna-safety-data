# Cross-Model Comparison (Accidents)

_Generated: 2026-04-25 13:28:00_

## Analysis Header

```
input_dataset: data/master/accident_master.csv
dataset_size_total: 191
models_compared: ['C310', 'C340', 'C402']
model_min_events_gate: 8
unknown_factor_rate: 0.2778
analysis_guardrail: counts-only; no exposure-based risk inference
```

## Baseline by Model

| model   |   events |   share_of_dataset |   fatal_events |   fatal_share_of_model_events |   serious_injury_events |   destroyed_aircraft |
|:--------|---------:|-------------------:|---------------:|------------------------------:|------------------------:|---------------------:|
| C310    |      137 |             0.7173 |             50 |                        0.365  |                      10 |                   31 |
| C340    |       27 |             0.1414 |             14 |                        0.5185 |                       1 |                   10 |
| C402    |       27 |             0.1414 |              2 |                        0.0741 |                       2 |                    1 |

## Over-Indexed Event Types by Model

| model   | value                    |   count_events |   share_in_model |   share_in_fleet |   delta_share |   index_vs_fleet |
|:--------|:-------------------------|---------------:|-----------------:|-----------------:|--------------:|-----------------:|
| C310    | Loss_of_Control          |             36 |           0.2628 |           0.2461 |        0.0167 |            1.068 |
| C310    | Fuel_Exhaustion          |              7 |           0.0511 |           0.0419 |        0.0092 |            1.22  |
| C310    | Hard_Landing             |              6 |           0.0438 |           0.0366 |        0.0071 |            1.195 |
| C310    | Midair_Collision         |              2 |           0.0146 |           0.0105 |        0.0041 |            1.394 |
| C310    | Landing_Gear_Malfunction |             40 |           0.292  |           0.288  |        0.004  |            1.014 |
| C310    | Fire                     |              4 |           0.0292 |           0.0262 |        0.003  |            1.115 |
| C310    | Other                    |              4 |           0.0292 |           0.0262 |        0.003  |            1.115 |
| C340    | CFIT                     |              5 |           0.1852 |           0.089  |        0.0962 |            2.081 |
| C340    | Loss_of_Control          |              9 |           0.3333 |           0.2461 |        0.0873 |            1.355 |
| C340    | Runway_Excursion         |              4 |           0.1481 |           0.0681 |        0.0801 |            2.177 |
| C340    | Ground_Collision         |              2 |           0.0741 |           0.0524 |        0.0217 |            1.415 |
| C340    | Fire                     |              1 |           0.037  |           0.0262 |        0.0109 |            1.415 |
| C340    | Fuel_Starvation          |              2 |           0.0741 |           0.0681 |        0.006  |            1.088 |
| C402    | Landing_Gear_Malfunction |             11 |           0.4074 |           0.288  |        0.1194 |            1.415 |
| C402    | Fuel_Starvation          |              3 |           0.1111 |           0.0681 |        0.043  |            1.632 |
| C402    | Runway_Excursion         |              3 |           0.1111 |           0.0681 |        0.043  |            1.632 |
| C402    | Engine_Failure           |              2 |           0.0741 |           0.0366 |        0.0374 |            2.021 |
| C402    | System_Malfunction       |              1 |           0.037  |           0.0105 |        0.0266 |            3.537 |
| C402    | Ground_Collision         |              2 |           0.0741 |           0.0524 |        0.0217 |            1.415 |
| C402    | Other                    |              1 |           0.037  |           0.0262 |        0.0109 |            1.415 |
| C402    | Hard_Landing             |              1 |           0.037  |           0.0366 |        0.0004 |            1.011 |

## Over-Indexed Phases by Model

| model   | value         |   count_events |   share_in_model |   share_in_fleet |   delta_share |   index_vs_fleet |
|:--------|:--------------|---------------:|-----------------:|-----------------:|--------------:|-----------------:|
| C310    | Taxi          |             10 |           0.073  |           0.0628 |        0.0102 |            1.162 |
| C310    | Cruise        |             22 |           0.1606 |           0.1518 |        0.0088 |            1.058 |
| C310    | Descent       |              4 |           0.0292 |           0.0209 |        0.0083 |            1.394 |
| C310    | Initial_Climb |             16 |           0.1168 |           0.1099 |        0.0068 |            1.062 |
| C310    | Go_Around     |              5 |           0.0365 |           0.0314 |        0.0051 |            1.162 |
| C310    | Takeoff       |              8 |           0.0584 |           0.0576 |        0.0008 |            1.014 |
| C340    | Approach      |             11 |           0.4074 |           0.199  |        0.2085 |            2.048 |
| C340    | Go_Around     |              1 |           0.037  |           0.0314 |        0.0056 |            1.179 |
| C340    | Initial_Climb |              3 |           0.1111 |           0.1099 |        0.0012 |            1.011 |
| C402    | Landing       |             14 |           0.5185 |           0.3455 |        0.173  |            1.501 |
| C402    | Unknown       |              2 |           0.0741 |           0.0209 |        0.0531 |            3.537 |
| C402    | Takeoff       |              2 |           0.0741 |           0.0576 |        0.0165 |            1.286 |
| C402    | Taxi          |              2 |           0.0741 |           0.0628 |        0.0112 |            1.179 |

## Over-Indexed Operation Types by Model

| model   |   value |   count_events |   share_in_model |   share_in_fleet |   delta_share |   index_vs_fleet |
|:--------|--------:|---------------:|-----------------:|-----------------:|--------------:|-----------------:|
| C310    |      91 |            128 |           0.9343 |           0.8586 |        0.0757 |            1.088 |
| C340    |      91 |             27 |           1      |           0.8586 |        0.1414 |            1.165 |
| C402    |     135 |             18 |           0.6667 |           0.1414 |        0.5253 |            4.716 |

## Over-Indexed Contributing Factors by Model

| model   | factor                               |   events_with_factor |   share_in_model |   share_in_fleet |   delta_share |   index_vs_fleet |
|:--------|:-------------------------------------|---------------------:|-----------------:|-----------------:|--------------:|-----------------:|
| C310    | checklist_non_compliance             |                   26 |           0.1898 |           0.1571 |        0.0327 |            1.208 |
| C310    | low_time_in_type                     |                   17 |           0.1241 |           0.1047 |        0.0194 |            1.185 |
| C310    | informal_or_incomplete_training      |                   11 |           0.0803 |           0.0628 |        0.0175 |            1.278 |
| C310    | single_engine_performance_assumption |                    7 |           0.0511 |           0.0366 |        0.0144 |            1.394 |
| C310    | incomplete_troubleshooting           |                    9 |           0.0657 |           0.0524 |        0.0133 |            1.255 |
| C310    | task_saturation                      |                   11 |           0.0803 |           0.0681 |        0.0122 |            1.18  |
| C310    | aging_aircraft_degradation           |                   10 |           0.073  |           0.0628 |        0.0102 |            1.162 |
| C310    | lapsed_recency                       |                    6 |           0.0438 |           0.0366 |        0.0071 |            1.195 |
| C310    | maintenance_induced_failure          |                   16 |           0.1168 |           0.1099 |        0.0068 |            1.062 |
| C310    | density_altitude_underestimation     |                    1 |           0.0073 |           0.0052 |        0.0021 |            1.394 |
| C340    | assumption_of_performance            |                    4 |           0.1481 |           0.0576 |        0.0906 |            2.572 |
| C340    | normalization_of_deviance            |                    2 |           0.0741 |           0.0209 |        0.0531 |            3.537 |
| C340    | icing_performance_degradation        |                    2 |           0.0741 |           0.0471 |        0.027  |            1.572 |
| C340    | plan_continuation_bias               |                    5 |           0.1852 |           0.1728 |        0.0124 |            1.072 |
| C340    | lapsed_recency                       |                    1 |           0.037  |           0.0366 |        0.0004 |            1.011 |
| C402    | plan_continuation_bias               |                    6 |           0.2222 |           0.1728 |        0.0494 |            1.286 |
| C402    | deferred_discrepancy_normalization   |                    1 |           0.037  |           0.0209 |        0.0161 |            1.769 |
| C402    | aging_aircraft_degradation           |                    2 |           0.0741 |           0.0628 |        0.0112 |            1.179 |
| C402    | maintenance_induced_failure          |                    3 |           0.1111 |           0.1099 |        0.0012 |            1.011 |

## Notes

- `delta_share` is model share minus fleet share for the same pattern.
- `index_vs_fleet > 1` means the pattern appears more often in that model's dataset slice.
- Results are descriptive frequency comparisons, not risk estimates.
