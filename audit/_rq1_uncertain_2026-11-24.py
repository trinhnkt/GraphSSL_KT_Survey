# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
REF = ROOT / "14_references"
OUT = ROOT / "audit" / "_a1_evidence" / "rq1_uncertain_windows_2026-11-24.txt"

PDFS = {
    "KT004": ("Graph-based Knowledge Tracing - Modeling Student Proficiency Using Graph Neural Network.pdf", r"transition|statistics-based|adjacency matrix"),
    "KT010": ("GIKT - A Graph-Based Interaction Model for Knowledge Tracing.pdf", r"question-skill|skill relation|bipartite|Q-matrix|exercise-concept"),
    "KT016": ("Structure-Based Knowledge Tracing - An Influence Propagation View.pdf", r"similarity relation|co-occur|transition|we construct|adjacency"),
    "KT035": ("HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf", r"basic graph|BG\s*=|heterogeneous graph|learner-question"),
    "KT036": ("Heterogeneous Graph-Based Knowledge Tracing with Spatiotemporal Evolution.pdf", r"we first construct|edge type|heterogeneous graph network"),
    "KT038": ("DyGKT - Dynamic Graph Learning for Knowledge Tracing.pdf", r"dynamic graph|interaction graph|we construct|continuous-time"),
    "KT042": ("Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf", r"hyperedge|hypergraph|we construct|co-occur"),
    "KT044": ("SINKT - A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model.pdf", r"concept graph|GPT-4|knowledge graph|we construct|prerequisite"),
    "KT047": ("Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing.pdf", r"heterogeneous graph|edge|co-occur|similarity|we construct"),
    "KT052": ("Modeling Knowledge Proficiency Using Multi-Hierarchical Capsule Graph Neural Network.pdf", r"Q-matrix|expert|concept relation|we construct|heterogeneous graph"),
    "KT053": ("GASKT - A Graph-Based Attentive Knowledge-Search Model for Knowledge Tracing.pdf", r"concept|skill|graph|relation|question"),
    "KT060": ("STHKT - Spatiotemporal Knowledge Tracing with Topological Hawkes Process.pdf", r"Hawkes|graph is|we construct|topology|adjacency"),
    "KT062": ("LGS-KT - Integrating Logical and Grammatical Skills for Effective Programming Knowledge Tracing.pdf", r"logical graph|submission|code order|grammar"),
    "KT063": ("MAHKT - Knowledge Tracing with Multi-Association Heterogeneous Graph Embedding Based on Knowledge Transfer.pdf", r"we construct|multi-association|heterogeneous graph|co-occur|prerequisite"),
    "KT065": ("Graph Knowledge Tracing in Cognitive Situation - Validation of Classic Assertions in Cognitive Psychology.pdf", r"transition|count\(|learning sequence|co-occur"),
    "KT066": ("Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing.pdf", r"hyperedge|hypergraph|response|we construct|question"),
    "KT084": ("A Dual-Encoder Contrastive Learning Model for Knowledge Tracing (DECKT).pdf", r"bipartite|Q-matrix|exercise-concept|question-concept|we construct"),
    "KT085": ("Dynamic heterogeneous graph contrastive networks for knowledge tracing.pdf", r"heterogeneous graph|transition graph|interaction|we construct|generated"),
    "KT086": ("Heterogeneous graph knowledge tracing with novel contrastive view and meta-path contexts.pdf", r"meta-path|heterogeneous information|question-skill|interaction|we construct"),
    "KT089": ("Contrastive Learning Based on Bipartite Graphs for Interpretable Knowledge Tracing.pdf", r"correlation|bipartite|whether related|G2|co-occur"),
}

parts = []
for pid, (name, pat) in PDFS.items():
    rx = re.compile(r".{0,70}(" + pat + r").{0,160}", re.I)
    reader = PdfReader(str(REF / name))
    parts.append(f"\n######## {pid} ########\n")
    n = 0
    for i, page in enumerate(reader.pages, start=1):
        text = re.sub(r"\s+", " ", page.extract_text() or "")
        # skip reference-heavy tail
        if i > len(reader.pages) - 2:
            continue
        for m in rx.finditer(text):
            frag = m.group(0)
            if "et al" in frag and "we " not in frag.lower() and "our " not in frag.lower():
                continue
            parts.append(f"p.{i}: {frag}\n")
            n += 1
            if n >= 5:
                break
        if n >= 5:
            break
    if n == 0:
        parts.append("NO_HIT\n")

text = "".join(parts).encode("utf-8", "replace").decode("utf-8")
OUT.write_text(text, encoding="utf-8")
print("wrote", OUT.stat().st_size)
