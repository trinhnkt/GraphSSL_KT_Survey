# -*- coding: utf-8 -*-
"""Extract graph-construction windows from the seven deposited PDFs."""
import re
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
REF = ROOT / "14_references"
OUT = ROOT / "audit" / "_a1_evidence" / "provenance_seven_windows_2026-11-24.txt"

FILES = [
    "SGKT - Session Graph-Based Knowledge Tracing for Student Performance Prediction.pdf",
    "HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf",
    "GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf",
    "LGS-KT - Integrating Logical and Grammatical Skills for Effective Programming Knowledge Tracing.pdf",
    "Multi-Granularity Ensemble Interaction Graph Modeling for Knowledge Tracing.pdf",
    "Graph Knowledge Tracing in Cognitive Situation - Validation of Classic Assertions in Cognitive Psychology.pdf",
    "A Cross-Domain Knowledge Tracing Model Based on Graph Optimal Transport.pdf",
]

KEYS = re.compile(
    r"session graph|adjacency|construct|prerequisite|co-occurr|cooccurr|interaction graph|"
    r"knowledge graph|concept graph|expert|curriculum|updated during|learnable|"
    r"edge weight|transition|heterogeneous|optimal transport|logical|grammatical|"
    r"ensemble|counterfactual|cognitive|Q-matrix|q-matrix|skill map|fixed graph|"
    r"dynamic graph|training set|from the training",
    re.I,
)

parts = []
for name in FILES:
    path = REF / name
    reader = PdfReader(str(path))
    parts.append(f"\n\n===== {name} pages={len(reader.pages)} =====\n")
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        text = text.replace("\x00", "")
        if not KEYS.search(text):
            continue
        # keep a shortened page if very long
        snippet = re.sub(r"\s+", " ", text)
        parts.append(f"\n--- p.{i} chars={len(text)} ---\n")
        parts.append(snippet[:4500])
        parts.append("\n")

OUT.parent.mkdir(exist_ok=True)
OUT.write_text("".join(parts), encoding="utf-8")
print("wrote", OUT, "chars", OUT.stat().st_size)
