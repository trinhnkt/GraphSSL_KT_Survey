# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
REF = ROOT / "14_references"
OUT = ROOT / "audit" / "_a1_evidence" / "rq1_windows4_2026-11-24.txt"

JOBS = [
    ("KT036", "Heterogeneous Graph-Based Knowledge Tracing with Spatiotemporal Evolution.pdf", r"correlation|same concept|co-occur|edge exists|adjacent"),
    ("KT056", "Exploring Long- and Short-Term Knowledge State Graph Representations with Adaptive Fusion for Knowledge Tracing.pdf", r"edge|connect|co-occur|window|construct"),
    ("KT063", "MAHKT - Knowledge Tracing with Multi-Association Heterogeneous Graph Embedding Based on Knowledge Transfer.pdf", r"co-occur|cosine|similarity is|we define|prerequisite relation|computed"),
    ("KT089", "Contrastive Learning Based on Bipartite Graphs for Interpretable Knowledge Tracing.pdf", r"if related|how|obtain r|correlation is|co-occur"),
    ("KT067", "Graph-Based Effective Knowledge Tracing via Subject Knowledge Mapping.pdf", r"question relation|similarity|co-occur|adjacency"),
    ("KT052", "Modeling Knowledge Proficiency Using Multi-Hierarchical Capsule Graph Neural Network.pdf", r"prior relationship|adjacency|connect two|edge between"),
]

parts = []
for pid, name, pat in JOBS:
    rx = re.compile(r".{0,100}(" + pat + r").{0,220}", re.I)
    reader = PdfReader(str(REF / name))
    parts.append(f"\n######## {pid} ########\n")
    n = 0
    for i, page in enumerate(reader.pages, start=1):
        if i > len(reader.pages) - 2:
            continue
        text = re.sub(r"\s+", " ", page.extract_text() or "")
        for m in rx.finditer(text):
            frag = m.group(0)
            if frag.lower().count("et al") >= 1 and "we " not in frag.lower():
                continue
            parts.append(f"p.{i}: {frag}\n")
            n += 1
            if n >= 4:
                break
        if n >= 4:
            break
    if n == 0:
        parts.append("NO_HIT\n")

text = "".join(parts).encode("utf-8", "replace").decode("utf-8")
OUT.write_text(text, encoding="utf-8")
print("wrote", OUT.stat().st_size)
