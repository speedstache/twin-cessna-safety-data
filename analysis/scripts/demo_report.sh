#!/usr/bin/env bash
# analysis/scripts/demo_report.sh
#
# Demo report runner (governance + capability demonstration; NOT analysis)
#
# Run:
#   bash analysis/scripts/demo_report.sh
#
# Optional:
#   --csv <path-to-csv>
#   --out <output-dir>

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

OUT_ROOT_DEFAULT="${PROJECT_ROOT}/out"
OUT_ROOT="$OUT_ROOT_DEFAULT"
CSV_PATH=""

# -------- args --------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --csv)
      CSV_PATH="${2:-}"
      shift 2
      ;;
    --out)
      OUT_ROOT="${2:-}"
      shift 2
      ;;
    -h|--help)
      cat <<EOF
Usage:
  bash analysis/scripts/demo_report.sh [--csv <path>] [--out <dir>]

If --csv is not provided, the script will auto-discover from common locations:
  data/master/accidents_master.csv
  data/master/accident_master.csv
  data/master/accidents_master.csv
  data/master/accident_master.csv
EOF
      exit 0
      ;;
    *)
      echo "Unknown argument: $1"
      exit 2
      ;;
  esac
done

# -------- auto-discover CSV if not provided --------
if [[ -z "${CSV_PATH}" ]]; then
  CANDIDATES=(
    "${PROJECT_ROOT}/data/master/accidents_master.csv"
    "${PROJECT_ROOT}/data/master/accident_master.csv"
    "${PROJECT_ROOT}/data/master/accidents_master.csv"
    "${PROJECT_ROOT}/data/master/accident_master.csv"
    "${PROJECT_ROOT}/data/structured/accidents_master.csv"
    "${PROJECT_ROOT}/data/structured/accident_master.csv"
    "${PROJECT_ROOT}/data/accidents_master.csv"
    "${PROJECT_ROOT}/data/accident_master.csv"
  )

  for c in "${CANDIDATES[@]}"; do
    if [[ -f "$c" ]]; then
      CSV_PATH="$c"
      break
    fi
  done
fi

# -------- preflight --------
if [[ -z "${CSV_PATH}" ]]; then
  echo "ERROR: Could not auto-discover master CSV."
  echo "Tried these locations:"
  echo "  - ${PROJECT_ROOT}/data/master/accidents_master.csv"
  echo "  - ${PROJECT_ROOT}/data/master/accident_master.csv"
  echo "  - ${PROJECT_ROOT}/data/structured/accidents_master.csv"
  echo "  - ${PROJECT_ROOT}/data/structured/accident_master.csv"
  echo "  - ${PROJECT_ROOT}/data/accidents_master.csv"
  echo "  - ${PROJECT_ROOT}/data/accident_master.csv"
  echo
  echo "Fix: run with --csv <full_path_to_csv>"
  exit 1
fi

if [[ ! -f "$CSV_PATH" ]]; then
  echo "ERROR: CSV not found at: $CSV_PATH"
  echo "Fix: provide the correct path via --csv <path>"
  exit 1
fi

TS="$(date +"%Y%m%d_%H%M%S")"
OUT_DIR="${OUT_ROOT%/}/demo_${TS}"
mkdir -p "$OUT_DIR"

echo "======================================="
echo "Twin Cessna Safety Data Demo Report"
echo "======================================="
echo "Project root: $PROJECT_ROOT"
echo "CSV:          $CSV_PATH"
echo "Output dir:   $OUT_DIR"
echo

run_step () {
  local name="$1"
  shift
  local logfile="$OUT_DIR/${name}.log"
  echo "---- $name ----"
  echo "\$ $*" | tee "$logfile"
  "$@" 2>&1 | tee -a "$logfile"
  echo | tee -a "$logfile"
}

PYTHON_BIN="${PROJECT_ROOT}/venv/bin/python"

# 1) Validate + rebuild (if present)
if [[ -f "${PROJECT_ROOT}/analysis/scripts/validate_records.py" ]]; then
  run_step "01_validate_records" \
    $PYTHON_BIN "${PROJECT_ROOT}/analysis/scripts/validate_records.py"
else
  echo "WARN: validate_records.py not found; skipping." | tee "$OUT_DIR/01_validate_records.log"
fi

if [[ -f "${PROJECT_ROOT}/analysis/scripts/build_master.py" ]]; then
  run_step "02_build_master" \
    $PYTHON_BIN "${PROJECT_ROOT}/analysis/scripts/build_master.py"
else
  echo "WARN: build_master.py not found; skipping." | tee "$OUT_DIR/02_build_master.log"
fi

# 2) Descriptive snapshot
run_step "03_dataset_snapshot" \
  $PYTHON_BIN "${PROJECT_ROOT}/analysis/scripts/dataset_snapshot.py" \
  --csv "$CSV_PATH" \
  --out-json "$OUT_DIR/dataset_snapshot.json" \
  --out-dir "$OUT_DIR/dataset_snapshot_tables"

# 3) Governance metrics
run_step "04_governance_metrics" \
  $PYTHON_BIN "${PROJECT_ROOT}/analysis/scripts/governance_metrics.py" \
  --csv "$CSV_PATH" \
  --out-json "$OUT_DIR/governance_metrics.json" \
  --out-dir "$OUT_DIR/governance_tables"

# 4) Gate status
run_step "05_analysis_gate_status" \
  $PYTHON_BIN "${PROJECT_ROOT}/analysis/scripts/analysis_gate_status.py" \
  --csv "$CSV_PATH" \
  --json-out "$OUT_DIR/analysis_gate_status.json"

# 5) Unknown monitor
run_step "06_unknown_monitor" \
  $PYTHON_BIN "${PROJECT_ROOT}/analysis/scripts/unknown_monitor.py" \
  --csv "$CSV_PATH" \
  --threshold 0.4 \
  --out-json "$OUT_DIR/unknown_monitor.json" \
  --out-dir "$OUT_DIR/unknown_tables"

# Index
INDEX="$OUT_DIR/README_demo_outputs.txt"
cat > "$INDEX" <<EOF
Twin Cessna Safety Data Demo Outputs
===================================

Generated: ${TS}
Project root: ${PROJECT_ROOT}
CSV: ${CSV_PATH}

Demonstrates:
- Validation
- Deterministic rebuild
- Descriptive snapshot
- Governance metrics
- Gate status enforcement
- Unknown monitoring

NOTE: Demonstration only (no analysis / no pattern claims).
EOF

echo
echo "Demo complete."
echo "Outputs written to: $OUT_DIR"
echo "Index file: $INDEX"
