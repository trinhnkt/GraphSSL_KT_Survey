# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
REF = ROOT / "14_references"
OUT = ROOT / "audit" / "_a1_evidence" / "rq1_windows3_2026-11-24.txt"

JOBS = [
    ("KT036", "Heterogeneous Graph-Based Knowledge Tracing with Spatiotemporal Evolution.pdf", ["homogeneous graph", "knowledge space", "similarity"]),
    ("KT056", "Exploring Long- and Short-Term Knowledge State Graph Representations with Adaptive Fusion for Knowledge Tracing.pdf", ["construct graphs", "long-term", "adjacency"]),
    ("KT063", "MAHKT - Knowledge Tracing with Multi-Association Heterogeneous Graph Embedding Based on Knowledge Transfer.pdf", ["Association", "prerequisite", "co-occur", "similarity"]),
    ("KT086", "Heterogeneous graph knowledge tracing with novel contrastive view and meta-path contexts.pdf", ["HIN", "constructed", "skill", "interaction"]),
    ("KT089", "Contrastive Learning Based on Bipartite Graphs for Interpretable Knowledge Tracing.pdf", ["related", "co-occur", "similarity", "G 2", "G2"]),
    ("KT064", "Multi-Granularity Ensemble Interaction Graph Modeling for Knowledge Tracing.pdf", ["I^T", "sigmoid", "interaction matrix", "similarity"]),
    ("KT052", "Modeling Knowledge Proficiency Using Multi-Hierarchical Capsule Graph Neural Network.pdf", ["capsule graph", "adjacency", "edge"]),
    ("KT076", "KGNN-KT - Enhancing Knowledge Tracing in Programming Education Through LLM-Extracted Knowledge Graphs.pdf", ["graph", "LLM", "knowledge"]),
]

parts = []
for pid, name, keys in JOBS:
    reader = PdfReader(str(REF / name))
    parts.append(f"\n######## {pid} pages={len(reader.pages)} chars0={len(reader.pages[0].extract_text() or '')} ########\n")
    n = 0
    for i, page in enumerate(reader.pages, start=1):
        text = re.sub(r"\s+", " ", page.extract_text() or "")
        low = text.lower()
        for key in keys:
            pos = low.find(key.lower())
            if pos < 0:
                continue
            start = max(0, pos - 120)
            end = min(len(text), pos + 360)
            parts.append(f"p.{i} [{key}]: {text[start:end]}\n")
            n += 1
            if n >= 6:
                break
        if n >= 6:
            break
    if n == 0:
        parts.append("NO_HIT\n")

text = "".join(parts).encode("utf-8", "replace").decode("utf-8")
OUT.write_text(text, encoding="utf-8")
print("wrote", OUT.stat().st_size)
