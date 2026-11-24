# -*- coding: utf-8 -*-
"""Context lines for cold-start and RMSE in the seven gateway PDFs."""
import os
import re
from pypdf import PdfReader

ROOT = r"D:\TRINH\GraphSSL_KT_Survey\14_references"
OUT = r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\seven_result_context_2026-11-23.txt"
FILES = [
    "A Dual-Encoder Contrastive Learning Model for Knowledge Tracing (DECKT).pdf",
    "Dynamic heterogeneous graph contrastive networks for knowledge tracing.pdf",
    "Heterogeneous graph knowledge tracing with novel contrastive view and meta-path contexts.pdf",
    "Contrastive Learning Based on Bipartite Graphs for Interpretable Knowledge Tracing.pdf",
    "CoSKT A Collaborative Self-Supervised Learning Method for Knowledge Tracing.pdf",
    "Tracing Knowledge Instead of Patterns Stable Knowledge Tracing with Diagnostic Transformer.pdf",
    "Self-paced contrastive learning for knowledge tracing.pdf",
]
PAT = re.compile(r"cold[- ]start|\bRMSE\b|root[- ]mean[- ]square|expected calibration|\bECE\b|\bBrier\b|calibration", re.I)


def clean(text):
    return "".join(ch for ch in text if not 0xD800 <= ord(ch) <= 0xDFFF)


parts = []
for name in FILES:
    reader = PdfReader(os.path.join(ROOT, name))
    text = "\n".join(clean(p.extract_text() or "") for p in reader.pages)
    flat = " ".join(text.split())
    hits = list(PAT.finditer(flat))
    parts.append("FILE " + name)
    parts.append("hits " + str(len(hits)))
    for hit in hits[:8]:
        start = max(0, hit.start() - 160)
        end = min(len(flat), hit.end() + 160)
        parts.append(" - " + flat[start:end])
    parts.append("")
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(parts))
print("wrote", OUT)
