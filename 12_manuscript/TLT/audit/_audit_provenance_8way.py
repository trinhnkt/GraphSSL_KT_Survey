"""Audit: per-paper 8-way graph_provenance in coding files vs 3-token display in graph_taxonomy.csv.

Read-only on evidence. Writes a new versioned CSV only.
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TAX = ROOT / "12_manuscript" / "TLT" / "tables" / "graph_taxonomy.csv"
OUT = ROOT / "12_manuscript" / "TLT" / "supplementary" / "graph_provenance_8way_audit_v1.9.csv"

# Highest-version coding file per paper.
files = {}
for p in list((ROOT / "07_coding").rglob("KT*_CODING_*.md")) + list((ROOT / "02_pilot_coding").rglob("KT*_CODING_*.md")):
    m = re.match(r"(KT\d+)_CODING_v([\d.]+)\.md", p.name)
    if not m:
        continue
    kt, ver = m.group(1), tuple(int(x) for x in m.group(2).split("."))
    if kt not in files or ver > files[kt][0]:
        files[kt] = (ver, p)

row_re = re.compile(r"\|\s*`?(graph_provenance|graph_source)`?\s*\|\s*`?([A-Z_]+)`?\s*\|")


def read8(path):
    vals = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = row_re.search(line)
        if m and m.group(1) not in vals:
            vals[m.group(1)] = m.group(2)
    return vals


# Display (graph_taxonomy.csv): collapse KT004 two rows to one paper token.
disp = {}
src_disp = {}
with open(TAX, encoding="utf-8") as f:
    for r in csv.DictReader(f):
        pid = r["paper_id"].split("_")[0]
        disp.setdefault(pid, set()).add(r["graph_provenance"])
        src_disp.setdefault(pid, []).append(r["graph_source"])

RULE = {
    "EXTERNAL_FIXED": "EXTERNAL_FIXED",
    "MODEL_DEFINED_FIXED": "MODEL_DEFINED_FIXED",
    "TRAIN_ONLY_INFERRED": "MODEL_DEFINED_FIXED",
    "FULL_DATA_INFERRED": "MODEL_DEFINED_FIXED",
    "PRECOMPUTED_UNCLEAR_SPLIT": "MODEL_DEFINED_FIXED",
    "JOINTLY_LEARNED_TRAINING": "DYNAMIC_LEARNED",
    "PRETRAINED_TWO_STAGE": "DYNAMIC_LEARNED",
    "MIXED_PROVENANCE": "UNMAPPED",
    "NA": "NA",
    "UNCLEAR": "UNMAPPED",
}

rows = []
for pid in sorted(disp):
    if pid == "KT039":
        continue
    ver, path = files.get(pid, (None, None))
    v8 = read8(path) if path else {}
    p8 = v8.get("graph_provenance", "NOT_FOUND")
    mapped = RULE.get(p8, "NOT_FOUND")
    d = "|".join(sorted(disp[pid]))
    rows.append(
        {
            "paper_id": pid,
            "display_3token_graph_taxonomy_v1.8": d,
            "coding_file_8way_graph_provenance": p8,
            "rule_mapped_3token": mapped,
            "agrees_with_display": "YES" if mapped == d else "NO",
            "graph_source_display": "|".join(sorted(set(src_disp[pid]))),
            "coding_file": str(path.relative_to(ROOT)) if path else "NONE",
        }
    )

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

n = len(rows)
agree = sum(r["agrees_with_display"] == "YES" for r in rows)
nf = sum(r["coding_file_8way_graph_provenance"] == "NOT_FOUND" for r in rows)
print(f"papers={n} agree={agree} disagree={n-agree} not_found={nf}")
from collections import Counter

print("8way counts:", Counter(r["coding_file_8way_graph_provenance"] for r in rows))
print("display counts:", Counter(r["display_3token_graph_taxonomy_v1.8"] for r in rows))
print("rule-mapped counts:", Counter(r["rule_mapped_3token"] for r in rows))
for r in rows:
    if r["agrees_with_display"] == "NO":
        print(
            r["paper_id"],
            "| display:", r["display_3token_graph_taxonomy_v1.8"],
            "| 8way:", r["coding_file_8way_graph_provenance"],
            "| mapped:", r["rule_mapped_3token"],
            "|", r["graph_source_display"],
        )
