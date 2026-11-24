# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader

REF = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
OUT = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\provenance_seven_pages_2026-11-24.txt")
JOBS = [
    ("LGS-KT - Integrating Logical and Grammatical Skills for Effective Programming Knowledge Tracing.pdf", [5, 6]),
    ("Multi-Granularity Ensemble Interaction Graph Modeling for Knowledge Tracing.pdf", [5, 6]),
    ("Graph Knowledge Tracing in Cognitive Situation - Validation of Classic Assertions in Cognitive Psychology.pdf", [5, 6, 7, 8]),
    ("A Cross-Domain Knowledge Tracing Model Based on Graph Optimal Transport.pdf", [5, 6, 7]),
    ("GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf", [5, 6]),
    ("HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf", [5, 6]),
    ("SGKT - Session Graph-Based Knowledge Tracing for Student Performance Prediction.pdf", [3, 4]),
]
parts = []
for name, pages in JOBS:
    reader = PdfReader(str(REF / name))
    parts.append(f"\n\n######## {name} ########\n")
    for p in pages:
        if p > len(reader.pages):
            parts.append(f"missing p.{p}\n")
            continue
        text = reader.pages[p - 1].extract_text() or ""
        text = re.sub(r"[ \t]+", " ", text)
        parts.append(f"\n----- p.{p} -----\n{text}\n")
OUT.write_text("".join(parts), encoding="utf-8")
print("chars", OUT.stat().st_size)
