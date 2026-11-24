# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
OUT = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\provenance_seven_sentences_2026-11-24.txt")
FILES = [
    "SGKT - Session Graph-Based Knowledge Tracing for Student Performance Prediction.pdf",
    "HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf",
    "GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf",
    "LGS-KT - Integrating Logical and Grammatical Skills for Effective Programming Knowledge Tracing.pdf",
    "Multi-Granularity Ensemble Interaction Graph Modeling for Knowledge Tracing.pdf",
    "Graph Knowledge Tracing in Cognitive Situation - Validation of Classic Assertions in Cognitive Psychology.pdf",
    "A Cross-Domain Knowledge Tracing Model Based on Graph Optimal Transport.pdf",
]
PAT = re.compile(
    r".{0,180}(session graph|construct(?:ed|s|ing)? (?:a |the )?(?:graph|heterogeneous|session|concept|skill)|"
    r"adjacency (?:matrix|matrices)|edge weight|prerequisite|co-occurrence|cooccurrence|"
    r"interaction graph|optimal transport|logical graph|grammatical|counterfactual graph|"
    r"knowledge structure|concept map|updated (?:during|in) training|learnable adjacency|"
    r"from (?:the )?training (?:set|data|interactions)|expert[- ]defined|curriculum).{0,220}",
    re.I,
)
parts = []
for name in FILES:
    reader = PdfReader(str(ROOT / name))
    parts.append(f"\n\n######## {name} ########\n")
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        text = re.sub(r"\s+", " ", text)
        hits = PAT.findall(text)
        # findall with one group returns only the group. Use finditer.
    # redo properly
    reader = PdfReader(str(ROOT / name))
    for i, page in enumerate(reader.pages, start=1):
        text = re.sub(r"\s+", " ", page.extract_text() or "")
        for m in PAT.finditer(text):
            parts.append(f"p.{i}: {m.group(0)}\n")

OUT.write_text("".join(parts), encoding="utf-8")
print("chars", OUT.stat().st_size, "lines", OUT.read_text(encoding="utf-8").count("\n"))
