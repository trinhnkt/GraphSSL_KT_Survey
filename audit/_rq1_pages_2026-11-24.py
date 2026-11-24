# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
REF = ROOT / "14_references"
OUT = ROOT / "audit" / "_a1_evidence" / "rq1_selected_pages_2026-11-24.txt"

JOBS = [
    ("KT035", "HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf", [5, 6, 7]),
    ("KT036", "Heterogeneous Graph-Based Knowledge Tracing with Spatiotemporal Evolution.pdf", [5]),
    ("KT042", "Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf", [3, 4, 5]),
    ("KT047", "Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing.pdf", [4, 5]),
    ("KT052", "Modeling Knowledge Proficiency Using Multi-Hierarchical Capsule Graph Neural Network.pdf", [4, 5]),
    ("KT060", "STHKT - Spatiotemporal Knowledge Tracing with Topological Hawkes Process.pdf", [3, 4]),
    ("KT063", "MAHKT - Knowledge Tracing with Multi-Association Heterogeneous Graph Embedding Based on Knowledge Transfer.pdf", [3, 4, 5]),
    ("KT066", "Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing.pdf", [3, 4, 5]),
    ("KT085", "Dynamic heterogeneous graph contrastive networks for knowledge tracing.pdf", [3, 4, 5]),
    ("KT086", "Heterogeneous graph knowledge tracing with novel contrastive view and meta-path contexts.pdf", [3, 4]),
    ("KT089", "Contrastive Learning Based on Bipartite Graphs for Interpretable Knowledge Tracing.pdf", [3, 4, 5]),
    ("KT004", "Graph-based Knowledge Tracing - Modeling Student Proficiency Using Graph Neural Network.pdf", [4]),
    ("KT068", "HKT - Hierarchical Structure-Based Knowledge Tracing.pdf", [3, 4]),
    ("KT011", "Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf", [4, 5]),
    ("KT029", "DGEKT - A Dual Graph Ensemble Learning Method for Knowledge Tracing.pdf", [4, 5]),
]

parts = []
for pid, name, pages in JOBS:
    reader = PdfReader(str(REF / name))
    parts.append(f"\n######## {pid} n={len(reader.pages)} ########\n")
    for i in pages:
        raw = reader.pages[i - 1].extract_text() or ""
        text = re.sub(r"\s+", " ", raw)
        parts.append(f"\n----- p.{i} len={len(text)} -----\n{text[:3500]}\n")

text = "".join(parts).encode("utf-8", "replace").decode("utf-8")
OUT.write_text(text, encoding="utf-8")
print("wrote", OUT.stat().st_size)
