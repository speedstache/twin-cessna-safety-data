#!/usr/bin/env python3

import os
import pandas as pd
from datetime import datetime

MASTER_PATH = "data/master/accident_master.csv"
OUTPUT_DIR = "data/analysis"

TAXONOMY_VERSION = "1.3"
UNKNOWN_THRESHOLD = 0.40


def load_data():
    df = pd.read_csv(MASTER_PATH)
    return df


def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def compute_header(df):
    dataset_size_total = len(df)
    dataset_size_per_model = df["model"].value_counts().to_dict()

    # unknown factor rate computed from boolean column
    factor_cols = [c for c in df.columns if c.startswith("cf_") and c != "cf_unknown"]
    total_factor_assignments = df[factor_cols].sum().sum()
    unknown_count = df["cf_unknown"].sum() if "cf_unknown" in df.columns else 0

    unknown_rate = (
        unknown_count / (unknown_count + total_factor_assignments)
        if (unknown_count + total_factor_assignments) > 0
        else 0
    )

    return {
        "taxonomy_version": TAXONOMY_VERSION,
        "dataset_size_total": dataset_size_total,
        "dataset_size_per_model": dataset_size_per_model,
        "unknown_factor_rate": round(unknown_rate, 4),
        "analysis_gate_status": "Fleet gate OPEN (>=75 total)"
    }


def baseline_summary(df):
    summary = df.groupby("model").agg(
        total_events=("model", "count"),
        fatal_events=("fatal", "sum"),
        serious_injury_events=("serious_injury", "sum"),
        destroyed_aircraft=("aircraft_destroyed", "sum")
    )
    return summary.reset_index()


def operation_split(df):
    return (
        df.groupby(["model", "operation_type"])
        .size()
        .reset_index(name="count")
    )


def factor_by_model(df):
    factor_cols = [c for c in df.columns if c.startswith("cf_") and c != "cf_unknown"]

    rows = []
    for model, group in df.groupby("model"):
        for col in factor_cols:
            count = group[col].sum()
            rows.append({
                "model": model,
                "factor": col.replace("cf_", ""),
                "count": int(count)
            })

    result = pd.DataFrame(rows)
    return result.sort_values(["model", "count"], ascending=[True, False])


def factor_by_operation(df):
    factor_cols = [c for c in df.columns if c.startswith("cf_") and c != "cf_unknown"]

    rows = []
    for op, group in df.groupby("operation_type"):
        for col in factor_cols:
            count = group[col].sum()
            rows.append({
                "operation_type": op,
                "factor": col.replace("cf_", ""),
                "count": int(count)
            })

    result = pd.DataFrame(rows)
    return result.sort_values(["operation_type", "count"], ascending=[True, False])


def phase_factor_matrix(df):
    factor_cols = [c for c in df.columns if c.startswith("cf_") and c != "cf_unknown"]

    rows = []
    for phase, group in df.groupby("phase_of_flight"):
        for col in factor_cols:
            rows.append({
                "phase_of_flight": phase,
                "factor": col.replace("cf_", ""),
                "count": int(group[col].sum())
            })

    result = pd.DataFrame(rows)
    return result.sort_values(["phase_of_flight", "count"], ascending=[True, False])


def main():
    ensure_output_dir()
    df = load_data()

    header = compute_header(df)

    print("taxonomy_version:", header["taxonomy_version"])
    print("dataset_size_total:", header["dataset_size_total"])
    print("dataset_size_per_model:", header["dataset_size_per_model"])
    print("unknown_factor_rate:", header["unknown_factor_rate"])
    print("analysis_gate_status:", header["analysis_gate_status"])
    print()

    baseline_summary(df).to_csv(f"{OUTPUT_DIR}/baseline_summary.csv", index=False)
    operation_split(df).to_csv(f"{OUTPUT_DIR}/operation_split.csv", index=False)
    factor_by_model(df).to_csv(f"{OUTPUT_DIR}/factor_by_model.csv", index=False)
    factor_by_operation(df).to_csv(f"{OUTPUT_DIR}/factor_by_operation.csv", index=False)
    phase_factor_matrix(df).to_csv(f"{OUTPUT_DIR}/phase_factor_matrix.csv", index=False)

    print("Analysis files written to data/analysis/")


if __name__ == "__main__":
    main()