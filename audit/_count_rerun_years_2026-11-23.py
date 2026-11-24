# -*- coding: utf-8 -*-
import csv
from pathlib import Path

root = Path(r"D:\TRINH\GraphSSL_KT_Survey\03_search\exports")

def load(name):
    with (root / name).open(encoding="utf-8", errors="replace", newline="") as fh:
        return list(csv.DictReader(fh))

for name in ["ieee_qg_20261114.csv", "ieee_qs_20261114.csv"]:
    rows = load(name)
    late = [r for r in rows if (r.get("Online Date") or "") > "2026-07-31" or (r.get("Publication Year") or "") > "2026"]
    y2026 = sum(1 for r in rows if r.get("Publication Year") == "2026")
    print(name, "rows", len(rows), "year2026", y2026, "online_after_cutoff_or_year_gt", len(late))

for name in ["scopus_qg_20261114.csv", "scopus_qs_20261114.csv", "scopus_qp_20261114.csv", "scopus_qr_20261114.csv"]:
    rows = load(name)
    y2026 = sum(1 for r in rows if r.get("Year") == "2026")
    print(name, "rows", len(rows), "year2026", y2026)

for name in ["springer_qg_20261114.csv", "springer_qs_20261114.csv"]:
    rows = load(name)
    y2026 = sum(1 for r in rows if r.get("Publication Year") == "2026")
    print(name, "rows", len(rows), "year2026", y2026)
