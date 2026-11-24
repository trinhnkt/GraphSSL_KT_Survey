# -*- coding: utf-8 -*-
import csv
from collections import Counter
from pathlib import Path

root = Path(r"D:\TRINH\GraphSSL_KT_Survey")
audit = list(csv.DictReader((root / "12_manuscript/TLT/supplementary/graph_provenance_8way_audit_v1.9.csv").open(encoding="utf-8-sig")))
exp = list(csv.DictReader((root / "data/PRIMARY_CORE_EXPANDED_2026-11-23.csv").open(encoding="utf-8")))

final = {
    "KT023": "MODEL_DEFINED_FIXED",
    "KT035": "MODEL_DEFINED_FIXED",
    "KT050": "MODEL_DEFINED_FIXED",
    "KT062": "MODEL_DEFINED_FIXED",
    "KT064": "MODEL_DEFINED_FIXED",
    "KT065": "MODEL_DEFINED_FIXED",
    "KT069": "MODEL_DEFINED_FIXED",
}
# four expansion graph papers: collapse already-coded provenance, not a new PDF pass
expansion_display = {
    "KT084": "MODEL_DEFINED_FIXED",
    "KT085": "UNCLEAR",
    "KT086": "MODEL_DEFINED_FIXED",
    "KT089": "MODEL_DEFINED_FIXED",
}

def norm(tok):
    if tok == "DYNAMIC_LEARNED":
        return "DYNAMICALLY_LEARNED"
    return tok

counts = Counter()
for row in audit:
    pid = row["paper_id"]
    tok = final[pid] if pid in final else norm(row["display_3token_graph_taxonomy_v1.8"])
    counts[tok] += 1
for pid, tok in expansion_display.items():
    counts[tok] += 1

graph_ids = {r["paper_id"] for r in exp if r["G_criterion"] == "YES"}
covered = {r["paper_id"] for r in audit} | set(expansion_display)
print("graph papers", len(graph_ids))
print("covered", len(covered & graph_ids), "missing", sorted(graph_ids - covered), "extra", sorted(covered - graph_ids))
print(dict(counts), "sum", sum(counts.values()))
