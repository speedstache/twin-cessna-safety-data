# Cross-Model Comparison (Accidents)

_Generated: 2026-02-22 15:02:18_

## Analysis Header

```
input_dataset: data/master/accident_master.csv
dataset_size_total: 93
models_compared: ['C310', 'C340', 'C402']
model_min_events_gate: 8
unknown_factor_rate: 0.2074
analysis_guardrail: counts-only; no exposure-based risk inference
```

## Baseline by Model

| model   |   events |   share_of_dataset |   fatal_events |   fatal_share_of_model_events |   serious_injury_events |   destroyed_aircraft |
|:--------|---------:|-------------------:|---------------:|------------------------------:|------------------------:|---------------------:|
| C310    |       39 |             0.4194 |             14 |                        0.359  |                       3 |                   12 |
| C340    |       27 |             0.2903 |             14 |                        0.5185 |                       1 |                   10 |
| C402    |       27 |             0.2903 |              2 |                        0.0741 |                       2 |                    1 |

## Over-Indexed Event Types by Model

| model   | value                    |   count_events |   share_in_model |   share_in_fleet |   delta_share |   index_vs_fleet |
|:--------|:-------------------------|---------------:|-----------------:|-----------------:|--------------:|-----------------:|
| C310    | Landing_Gear_Malfunction |             15 |           0.3846 |           0.3226 |        0.062  |            1.192 |
| C310    | Loss_of_Control          |             11 |           0.2821 |           0.2366 |        0.0455 |            1.192 |
| C310    | Fuel_Exhaustion          |              3 |           0.0769 |           0.043  |        0.0339 |            1.788 |
| C310    | Midair_Collision         |              1 |           0.0256 |           0.0108 |        0.0149 |            2.385 |
| C310    | Fire                     |              1 |           0.0256 |           0.0215 |        0.0041 |            1.192 |
| C310    | Hard_Landing             |              1 |           0.0256 |           0.0215 |        0.0041 |            1.192 |
| C340    | CFIT                     |              5 |           0.1852 |           0.086  |        0.0992 |            2.153 |
| C340    | Loss_of_Control          |              9 |           0.3333 |           0.2366 |        0.0968 |            1.409 |
| C340    | Runway_Excursion         |              4 |           0.1481 |           0.086  |        0.0621 |            1.722 |
| C340    | Fire                     |              1 |           0.037  |           0.0215 |        0.0155 |            1.722 |
| C340    | Fuel_Starvation          |              2 |           0.0741 |           0.0645 |        0.0096 |            1.148 |
| C340    | Ground_Collision         |              2 |           0.0741 |           0.0645 |        0.0096 |            1.148 |
| C402    | Landing_Gear_Malfunction |             11 |           0.4074 |           0.3226 |        0.0848 |            1.263 |
| C402    | Engine_Failure           |              2 |           0.0741 |           0.0215 |        0.0526 |            3.444 |
| C402    | Fuel_Starvation          |              3 |           0.1111 |           0.0645 |        0.0466 |            1.722 |
| C402    | Other                    |              1 |           0.037  |           0.0108 |        0.0263 |            3.444 |
| C402    | System_Malfunction       |              1 |           0.037  |           0.0108 |        0.0263 |            3.444 |
| C402    | Runway_Excursion         |              3 |           0.1111 |           0.086  |        0.0251 |            1.292 |
| C402    | Hard_Landing             |              1 |           0.037  |           0.0215 |        0.0155 |            1.722 |
| C402    | Ground_Collision         |              2 |           0.0741 |           0.0645 |        0.0096 |            1.148 |

## Over-Indexed Phases by Model

| model   | value         |   count_events |   share_in_model |   share_in_fleet |   delta_share |   index_vs_fleet |
|:--------|:--------------|---------------:|-----------------:|-----------------:|--------------:|-----------------:|
| C310    | Cruise        |              9 |           0.2308 |           0.172  |        0.0587 |            1.341 |
| C310    | Taxi          |              4 |           0.1026 |           0.0645 |        0.038  |            1.59  |
| C310    | Descent       |              2 |           0.0513 |           0.0215 |        0.0298 |            2.385 |
| C310    | Go_Around     |              1 |           0.0256 |           0.0215 |        0.0041 |            1.192 |
| C340    | Approach      |             11 |           0.4074 |           0.2151 |        0.1924 |            1.894 |
| C340    | Initial_Climb |              3 |           0.1111 |           0.0753 |        0.0358 |            1.476 |
| C340    | Go_Around     |              1 |           0.037  |           0.0215 |        0.0155 |            1.722 |
| C402    | Landing       |             14 |           0.5185 |           0.3548 |        0.1637 |            1.461 |
| C402    | Unknown       |              2 |           0.0741 |           0.0215 |        0.0526 |            3.444 |
| C402    | Takeoff       |              2 |           0.0741 |           0.0538 |        0.0203 |            1.378 |
| C402    | Taxi          |              2 |           0.0741 |           0.0645 |        0.0096 |            1.148 |

## Over-Indexed Operation Types by Model

| model   |   value |   count_events |   share_in_model |   share_in_fleet |   delta_share |   index_vs_fleet |
|:--------|--------:|---------------:|-----------------:|-----------------:|--------------:|-----------------:|
| C310    |      91 |             32 |           0.8205 |           0.7419 |        0.0786 |            1.106 |
| C340    |      91 |             27 |           1      |           0.7419 |        0.2581 |            1.348 |
| C402    |     135 |             17 |           0.6296 |           0.2581 |        0.3716 |            2.44  |

## Over-Indexed Contributing Factors by Model

| model   | factor                             |   events_with_factor |   share_in_model |   share_in_fleet |   delta_share |   index_vs_fleet |
|:--------|:-----------------------------------|---------------------:|-----------------:|-----------------:|--------------:|-----------------:|
| C310    | checklist_non_compliance           |                   12 |           0.3077 |           0.172  |        0.1356 |            1.788 |
| C310    | task_saturation                    |                    7 |           0.1795 |           0.0968 |        0.0827 |            1.855 |
| C310    | aging_aircraft_degradation         |                    5 |           0.1282 |           0.0753 |        0.0529 |            1.703 |
| C310    | maintenance_induced_failure        |                    7 |           0.1795 |           0.129  |        0.0505 |            1.391 |
| C310    | incomplete_troubleshooting         |                    4 |           0.1026 |           0.0538 |        0.0488 |            1.908 |
| C310    | plan_continuation_bias             |                   11 |           0.2821 |           0.2366 |        0.0455 |            1.192 |
| C310    | informal_or_incomplete_training    |                    3 |           0.0769 |           0.043  |        0.0339 |            1.788 |
| C310    | lapsed_recency                     |                    3 |           0.0769 |           0.043  |        0.0339 |            1.788 |
| C310    | assumption_of_performance          |                    5 |           0.1282 |           0.0968 |        0.0314 |            1.325 |
| C310    | low_time_in_type                   |                    4 |           0.1026 |           0.0753 |        0.0273 |            1.363 |
| C340    | assumption_of_performance          |                    4 |           0.1481 |           0.0968 |        0.0514 |            1.531 |
| C340    | normalization_of_deviance          |                    2 |           0.0741 |           0.0323 |        0.0418 |            2.296 |
| C340    | icing_performance_degradation      |                    2 |           0.0741 |           0.0645 |        0.0096 |            1.148 |
| C402    | deferred_discrepancy_normalization |                    1 |           0.037  |           0.0108 |        0.0263 |            3.444 |

## Notes

- `delta_share` is model share minus fleet share for the same pattern.
- `index_vs_fleet > 1` means the pattern appears more often in that model's dataset slice.
- Results are descriptive frequency comparisons, not risk estimates.
