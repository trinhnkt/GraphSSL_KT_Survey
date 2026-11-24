# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
REF = ROOT / "14_references"
OUT = ROOT / "audit" / "_a1_evidence" / "rq1_construct_locators_2026-11-24.txt"

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
    "KT042": "Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf",
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
    "KT077": "R2GCurL - Reinforced Robust Knowledge Tracing via Dynamic Graph Curriculum Learning.pdf",
    "KT079": "Spatio-Temporal Fusion in Graph Neural Network for Streaming Knowledge Tracing.pdf",
    "KT084": "A Dual-Encoder Contrastive Learning Model for Knowledge Tracing (DECKT).pdf",
    "KT085": "Dynamic heterogeneous graph contrastive networks for knowledge tracing.pdf",
    "KT086": "Heterogeneous graph knowledge tracing with novel contrastive view and meta-path contexts.pdf",
    "KT089": "Contrastive Learning Based on Bipartite Graphs for Interpretable Knowledge Tracing.pdf",
}

PAT = re.compile(
    r".{0,40}(co-?occurr|transition graph|session graph|construct(?:ed|s|ing)? (?:a |the )?(?:weighted |heterogeneous |dynamic |interaction )?(?:graph|hypergraph)|adjacency|question[- ]concept|Q-matrix|prerequisite|knowledge graph|similarity graph|interaction graph|from the (?:training|entire|full)).{0,180}",
    re.I,
)

parts = []
for pid, name in PDFS.items():
    reader = PdfReader(str(REF / name))
    parts.append(f"\n######## {pid} pages={len(reader.pages)} ########\n")
    n = 0
    for i, page in enumerate(reader.pages, start=1):
        text = re.sub(r"\s+", " ", page.extract_text() or "")
        for m in PAT.finditer(text):
            parts.append(f"p.{i}: {m.group(0)}\n")
            n += 1
            if n >= 4:
                break
        if n >= 4:
            break
    if n == 0:
        parts.append("NO_CONSTRUCT_PHRASE\n")

text = "".join(parts).encode("utf-8", "replace").decode("utf-8")
OUT.write_text(text, encoding="utf-8")
print("wrote", OUT.stat().st_size)
