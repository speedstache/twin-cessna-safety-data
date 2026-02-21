
# run the carol export summary 
python analysis/scripts/summarize_carol_export.py "/path/to/CAROL_ACC_TwinCessna_2006-Present_2026-02-21.csv" \
  --out analysis/outputs/carol_export_summary.md

# run the carol export summary and generate a weekly snippet
python analysis/scripts/summarize_carol_export.py "06_Archived_Queries/CAROL_Exports/CAROL_ACC_TwinCessna_2006-Present_2026-02-21.csv" \
  --out analysis/outputs/carol_export_summary.md \
  --weekly-snippet

# run the carol export summary and output the weekly snippet to a file
python analysis/scripts/summarize_carol_export.py "..." \
  --weekly-snippet \
  --weekly-snippet-out analysis/outputs/weekly_snippet.md

# run validate_records.py on the accidents folder only
python analysis/scripts/validate_records.py --path data/structured/accidents

# run validate_records.py on the accidents folder only and treat warnings as errors (strict mode)
python analysis/scripts/validate_records.py --path data/structured/accidents --warnings-as-errors

  This will fail the run if:

    Any enum drift occurs

    event_type formatting is sloppy

    drive_path prefix looks wrong

    Duplicate contributing factors exist

    This is helpful before committing.

    example successful run
    Files scanned: 3
    Errors: 0
    Warnings: 0
    Validation PASSED.

    example failed run
    data/structured/accidents/c310/C310-ACC-2016-CO-002.md
    ERROR: Invalid phase_of_flight='InitialClimb'. Allowed: [...]
    ERROR: contributing_factors must contain 1–3 items (or ['unknown']).

    ---
    Files scanned: 3
    Errors: 2
    Warnings: 0
    Validation FAILED (errors present).


# run build_master.py
python analysis/scripts/build_master.py

# run demo_report.sh
bash analysis/scripts/demo_report.sh