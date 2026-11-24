import csv
from pathlib import Path

files = [
    Path("05_screening/title_abstract_screening_v1.0.csv"),
    Path("06_fulltext/fulltext_screening_v1.0.csv"),
    Path("04_deduplication/deduplication_audit_v1.0.csv"),
    Path("12_manuscript/TLT/supplementary/supplementary_prisma_exclusions.csv"),
]
for path in files:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    print(f"\n{path} rows={len(rows)} cols={list(rows[0]) if rows else []}")
    for key in ("decision", "final_tier", "screener_id", "reviewer_id", "primary_exclusion_code"):
        if rows and key in rows[0]:
            counts = {}
            for row in rows:
                counts[row[key]] = counts.get(row[key], 0) + 1
            print(f"  {key}: {counts}")
