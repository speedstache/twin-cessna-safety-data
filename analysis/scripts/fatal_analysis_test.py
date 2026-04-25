#!/usr/bin/env python3
"""
Hypothesis Test: Pilot Experience vs Fatal Outcome

Counts-only severity association test.
Does NOT estimate accident risk or exposure-adjusted rates.
"""

import pandas as pd
from scipy.stats import fisher_exact


CSV_PATH = "data/master/accident_master.csv"

LESS_EXPERIENCED = ["<50", "50-200"]
MORE_EXPERIENCED = ["200-1000", ">1000"]


def main():
    df = pd.read_csv(CSV_PATH)

    df = df[df["time_in_type_band"].isin(LESS_EXPERIENCED + MORE_EXPERIENCED)].copy()

    df["experience_group"] = df["time_in_type_band"].apply(
        lambda x: "less" if x in LESS_EXPERIENCED else "more"
    )

    # Normalize fatal values in case CSV stores booleans as strings
    df["fatal"] = df["fatal"].astype(str).str.upper().map({
        "TRUE": True,
        "FALSE": False,
        "1": True,
        "0": False,
    })

    df = df[df["fatal"].isin([True, False])].copy()

    counts = pd.crosstab(df["experience_group"], df["fatal"])

    # Force a clean 2x2 table with stable row/column order
    counts = counts.reindex(index=["less", "more"], columns=[True, False], fill_value=0)

    a = int(counts.loc["less", True])
    b = int(counts.loc["less", False])
    c = int(counts.loc["more", True])
    d = int(counts.loc["more", False])

    matrix = [[a, b], [c, d]]

    oddsratio, p_greater = fisher_exact(matrix, alternative="greater")
    _, p_less = fisher_exact(matrix, alternative="less")
    _, p_two_sided = fisher_exact(matrix, alternative="two-sided")

    less_rate = a / (a + b) if (a + b) else 0
    more_rate = c / (c + d) if (c + d) else 0

    print("\nFatal Outcome by Time-in-Type Experience Group")
    print("================================================")
    print("taxonomy_version: derived from accident_master.csv")
    print(f"dataset_size_tested: {len(df)}")
    print("experience_definition:")
    print(f"  less_experienced: {LESS_EXPERIENCED}")
    print(f"  more_experienced: {MORE_EXPERIENCED}")
    print("excluded: time_in_type_band == Unknown or blank")
    print()

    print("2x2 table:")
    print("                fatal  non_fatal")
    print(f"less_experienced {a:5d} {b:10d}")
    print(f"more_experienced {c:5d} {d:10d}")
    print()

    print("Observed fatal share within accidents:")
    print(f"less_experienced: {less_rate:.3f}")
    print(f"more_experienced: {more_rate:.3f}")
    print()

    print("Fisher Exact Test:")
    print(f"odds_ratio: {oddsratio:.4f}")
    print(f"p_value_one_sided_less_more: {p_greater:.6f}")
    print(f"p_value_one_sided_more_greater: {p_less:.6f}")
    print(f"p_value_two_sided: {p_two_sided:.6f}")
    print()

    print("Interpretation guardrail:")
    print("- This is a severity association test within accidents only.")
    print("- It is not an exposure-adjusted accident risk test.")
    print("- Do not infer that one group is more likely to have an accident.")
    print("- Interpret only as fatal share among accidents in this dataset.")


if __name__ == "__main__":
    main()