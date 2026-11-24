# -*- coding: utf-8 -*-
import csv
from collections import Counter
from pathlib import Path

root = Path(r"D:\TRINH\GraphSSL_KT_Survey")
ta = list(csv.DictReader((root / "05_screening/title_abstract_screening_v1.0.csv").open(encoding="utf-8")))
ft = list(csv.DictReader((root / "06_fulltext/fulltext_screening_v1.0.csv").open(encoding="utf-8")))
px = list(csv.DictReader((root / "12_manuscript/TLT/supplementary/supplementary_prisma_exclusions.csv").open(encoding="utf-8")))
print("TA", len(ta), "cols", list(ta[0]))
print("TA decision", Counter(r["decision"] for r in ta))
print("TA screener", Counter(r["screener_id"] for r in ta))
print("TA uncertain", [r["record_id"] for r in ta if r["decision"] == "UNCERTAIN"])
print("--- exclude TA ---")
for r in ta:
    if r["decision"] != "INCLUDE_FULLTEXT":
        print(r)
print("FT", len(ft), "cols", list(ft[0]))
print("FT tier", Counter(r["final_tier"] for r in ft))
print("FT reviewer", Counter(r["reviewer_id"] for r in ft))
print("FT excl code", Counter(r["primary_exclusion_code"] for r in ft))
print("--- non core ---")
for r in ft:
    if r["final_tier"] != "PRIMARY_CORE":
        print(r["record_id"], r["final_tier"], r["primary_exclusion_code"], r["title"], r["secondary_notes"][:120])
print("PRISMA rows", len(px), "same ids", {r["record_id"] for r in px} == {r["record_id"] for r in ft})
print("TA ids", len({r["record_id"] for r in ta}), "FT ids", len({r["record_id"] for r in ft}))
print("TA not in FT", sorted({r["record_id"] for r in ta} - {r["record_id"] for r in ft}))
print("FT not in TA", sorted({r["record_id"] for r in ft} - {r["record_id"] for r in ta}))
