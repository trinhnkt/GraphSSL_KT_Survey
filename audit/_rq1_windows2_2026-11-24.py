# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
REF = ROOT / "14_references"
OUT = ROOT / "audit" / "_a1_evidence" / "rq1_windows2_2026-11-24.txt"

JOBS = [
    ("KT035", "HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf", "basic graph"),
    ("KT036", "Heterogeneous Graph-Based Knowledge Tracing with Spatiotemporal Evolution.pdf", "correlation between exercises"),
    ("KT042", "Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf", "share a common skill"),
    ("KT047", "Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing.pdf", "heterogeneous graph consists"),
    ("KT052", "Modeling Knowledge Proficiency Using Multi-Hierarchical Capsule Graph Neural Network.pdf", "construct the learning material"),
    ("KT063", "MAHKT - Knowledge Tracing with Multi-Association Heterogeneous Graph Embedding Based on Knowledge Transfer.pdf", "five associations"),
    ("KT066", "Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing.pdf", "pattern-aware"),
    ("KT085", "Dynamic heterogeneous graph contrastive networks for knowledge tracing.pdf", "temporal heterogeneous"),
    ("KT086", "Heterogeneous graph knowledge tracing with novel contrastive view and meta-path contexts.pdf", "meta-path"),
    ("KT089", "Contrastive Learning Based on Bipartite Graphs for Interpretable Knowledge Tracing.pdf", "correlation graph"),
    ("KT068", "HKT - Hierarchical Structure-Based Knowledge Tracing.pdf", "co-occurrence"),
    ("KT004", "Graph-based Knowledge Tracing - Modeling Student Proficiency Using Graph Neural Network.pdf", "number of times concept"),
    ("KT011", "Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf", "co-correctness"),
    ("KT029", "DGEKT - A Dual Graph Ensemble Learning Method for Knowledge Tracing.pdf", "Directed transition"),
    ("KT064", "Multi-Granularity Ensemble Interaction Graph Modeling for Knowledge Tracing.pdf", "similarity"),
    ("KT012", "JKT - A Joint Graph Convolutional Network Based Deep Knowledge Tracing.pdf", "co-correctness"),
    ("KT023", "SGKT - Session Graph-Based Knowledge Tracing for Student Performance Prediction.pdf", "Definition 3"),
    ("KT033", "Deep Graph Memory Networks for Forgetting-Robust Knowledge Tracing.pdf", "construct a graph"),
    ("KT038", "DyGKT - Dynamic Graph Learning for Knowledge Tracing.pdf", "question-answering graph"),
    ("KT043", "Weighted Heterogeneous Graph-Based Three-View Contrastive Learning for Knowledge Tracing in Personalized e-Learning Systems.pdf", "according to our training data"),
    ("KT050", "GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf", "student-question-concept"),
    ("KT056", "Exploring Long- and Short-Term Knowledge State Graph Representations with Adaptive Fusion for Knowledge Tracing.pdf", "exercise records"),
    ("KT062", "LGS-KT - Integrating Logical and Grammatical Skills for Effective Programming Knowledge Tracing.pdf", "logical"),
    ("KT065", "Graph Knowledge Tracing in Cognitive Situation - Validation of Classic Assertions in Cognitive Psychology.pdf", "immediately"),
    ("KT067", "Graph-Based Effective Knowledge Tracing via Subject Knowledge Mapping.pdf", "learning interactions"),
    ("KT069", "A Cross-Domain Knowledge Tracing Model Based on Graph Optimal Transport.pdf", "co_correct"),
    ("KT070", "Denoising Programming Knowledge Tracing with a Code Graph-based Tuning Adaptor.pdf", "entire training data"),
    ("KT077", "R2GCurL - Reinforced Robust Knowledge Tracing via Dynamic Graph Curriculum Learning.pdf", "dynamic graphs"),
    ("KT079", "Spatio-Temporal Fusion in Graph Neural Network for Streaming Knowledge Tracing.pdf", "Collaboration"),
    ("KT084", "A Dual-Encoder Contrastive Learning Model for Knowledge Tracing (DECKT).pdf", "bipartite graph"),
]

parts = []
for pid, name, key in JOBS:
    reader = PdfReader(str(REF / name))
    parts.append(f"\n######## {pid} ########\n")
    n = 0
    for i, page in enumerate(reader.pages, start=1):
        text = re.sub(r"\s+", " ", page.extract_text() or "")
        pos = text.lower().find(key.lower())
        if pos < 0:
            continue
        start = max(0, pos - 180)
        end = min(len(text), pos + 420)
        parts.append(f"p.{i}: {text[start:end]}\n")
        n += 1
        if n >= 2:
            break
    if n == 0:
        parts.append("NO_HIT\n")

text = "".join(parts).encode("utf-8", "replace").decode("utf-8")
OUT.write_text(text, encoding="utf-8")
print("wrote", OUT.stat().st_size)
