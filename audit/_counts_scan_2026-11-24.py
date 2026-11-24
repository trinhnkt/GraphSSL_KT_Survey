# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader

REF = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
OUT = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\counts_scan_2026-11-24.txt")

# expanded corpus PDFs: reuse the G=YES map and add sequence-only papers
PDFS = {
    "KT004": "Graph-based Knowledge Tracing - Modeling Student Proficiency Using Graph Neural Network.pdf",
    "KT010": "GIKT - A Graph-Based Interaction Model for Knowledge Tracing.pdf",
    "KT011": "Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf",
    "KT012": "JKT - A Joint Graph Convolutional Network Based Deep Knowledge Tracing.pdf",
    "KT014": "Prerequisite-Driven Deep Knowledge Tracing.pdf",
    "KT016": "Structure-Based Knowledge Tracing - An Influence Propagation View.pdf",
    "KT023": "SGKT - Session Graph-Based Knowledge Tracing for Student Performance Prediction.pdf",
    "KT026": "Improving Knowledge Tracing via Pre-training Question Embeddings.pdf",
    "KT029": "DGEKT - A Dual Graph Ensemble Learning Method for Knowledge Tracing.pdf",
    "KT031": "Knowledge Structure Enhanced Graph Representation Learning Model for Attentive Knowledge Tracing.pdf",
    "KT033": "Deep Graph Memory Networks for Forgetting-Robust Knowledge Tracing.pdf",
    "KT035": "HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf",
    "KT036": "Heterogeneous Graph-Based Knowledge Tracing with Spatiotemporal Evolution.pdf",
    "KT037": "CMKT - Concept Map Driven Knowledge Tracing.pdf",
    "KT038": "DyGKT - Dynamic Graph Learning for Knowledge Tracing.pdf",
    "KT039": "Contrastive Learning for Knowledge Tracing.pdf",
    "KT040": "Tracing Knowledge Instead of Patterns Stable Knowledge Tracing with Diagnostic Transformer.pdf",
    "KT042": "Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf",
    "KT043": "Weighted Heterogeneous Graph-Based Three-View Contrastive Learning for Knowledge Tracing in Personalized e-Learning Systems.pdf",
    "KT044": "SINKT - A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model.pdf",
    "KT047": "Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing.pdf",
    "KT050": "GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf",
    "KT052": "Modeling Knowledge Proficiency Using Multi-Hierarchical Capsule Graph Neural Network.pdf",
    "KT053": "GASKT - A Graph-Based Attentive Knowledge-Search Model for Knowledge Tracing.pdf",
    "KT056": "Exploring Long- and Short-Term Knowledge State Graph Representations with Adaptive Fusion for Knowledge Tracing.pdf",
    "KT060": "STHKT - Spatiotemporal Knowledge Tracing with Topological Hawkes Process.pdf",
    "KT062": "LGS-KT - Integrating Logical and Grammatical Skills for Effective Programming Knowledge Tracing.pdf",
    "KT063": "MAHKT - Knowledge Tracing with Multi-Association Heterogeneous Graph Embedding Based on Knowledge Transfer.pdf",
    "KT064": "Multi-Granularity Ensemble Interaction Graph Modeling for Knowledge Tracing.pdf",
    "KT065": "Graph Knowledge Tracing in Cognitive Situation - Validation of Classic Assertions in Cognitive Psychology.pdf",
    "KT066": "Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing.pdf",
    "KT067": "Graph-Based Effective Knowledge Tracing via Subject Knowledge Mapping.pdf",
    "KT068": "HKT - Hierarchical Structure-Based Knowledge Tracing.pdf",
    "KT069": "A Cross-Domain Knowledge Tracing Model Based on Graph Optimal Transport.pdf",
    "KT070": "Denoising Programming Knowledge Tracing with a Code Graph-based Tuning Adaptor.pdf",
    "KT076": "KGNN-KT - Enhancing Knowledge Tracing in Programming Education Through LLM-Extracted Knowledge Graphs.pdf",
    "KT077": "R2GCurL - Reinforced Robust Knowledge Tracing via Dynamic Graph Curriculum Learning.pdf",
    "KT079": "Spatio-Temporal Fusion in Graph Neural Network for Streaming Knowledge Tracing.pdf",
    "KT084": "A Dual-Encoder Contrastive Learning Model for Knowledge Tracing (DECKT).pdf",
    "KT085": "Dynamic heterogeneous graph contrastive networks for knowledge tracing.pdf",
    "KT086": "Heterogeneous graph knowledge tracing with novel contrastive view and meta-path contexts.pdf",
    "KT087": "CoSKT A Collaborative Self-Supervised Learning Method for Knowledge Tracing.pdf",
    "KT088": "Self-paced contrastive learning for knowledge tracing.pdf",
    "KT089": "Contrastive Learning Based on Bipartite Graphs for Interpretable Knowledge Tracing.pdf",
}
PAT = re.compile(
    r".{0,80}(cold[- ]start|unseen (question|skill|concept|kc)|zero[- ]shot|"
    r"training rate|drop ratio|interaction drop|removed? \d+\s*%|"
    r"hold[- ]?out|new (student|learner|question)|"
    r"\bECE\b|Brier|reliability diagram|calibration plot|"
    r"negative log|log-loss|log loss|\bNLL\b|\bRMSE\b).{0,120}",
    re.I,
)
parts = []
for pid, name in PDFS.items():
    path = REF / name
    parts.append(f"\n## {pid} exists={path.exists()}\n")
    if not path.exists():
        continue
    reader = PdfReader(str(path))
    chars = 0
    n = 0
    for i, page in enumerate(reader.pages, start=1):
        raw = page.extract_text() or ""
        chars += len(raw)
        text = re.sub(r"\s+", " ", raw)
        for m in PAT.finditer(text):
            frag = m.group(0)
            if "et al" in frag.lower() and "we " not in frag.lower():
                continue
            parts.append(f"p.{i}: {frag}\n")
            n += 1
            if n >= 6:
                break
        if n >= 6:
            break
    parts.append(f"HITS {n} CHARS {chars}\n")
text = "".join(parts).encode("utf-8", "replace").decode("utf-8")
OUT.write_text(text, encoding="utf-8")
print("wrote", OUT.stat().st_size)
