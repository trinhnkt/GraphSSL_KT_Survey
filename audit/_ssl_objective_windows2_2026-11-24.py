# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader

REF = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
OUT = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\ssl_objective_windows2_2026-11-24.txt")

PDFS = {
    "KT011": "Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf",
    "KT039": "Contrastive Learning for Knowledge Tracing.pdf",
    "KT042": "Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf",
    "KT047": "Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing.pdf",
    "KT050": "GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf",
    "KT066": "Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing.pdf",
    "KT026": "Improving Knowledge Tracing via Pre-training Question Embeddings.pdf",
}

KEYS = ["positive", "negative sample", "InfoNCE", "edge drop", "remove edges", "reconstruct", "prerequisite", "preserve", "augment", "hard negative", "counterfactual", "line graph", "meta-path", "channel"]

parts = []
for pid, name in PDFS.items():
    reader = PdfReader(str(REF / name))
    parts.append(f"\n######## {pid} n={len(reader.pages)} ########\n")
    n = 0
    for i, page in enumerate(reader.pages, start=1):
        if i < 4 or i > len(reader.pages) - 2:
            continue
        text = re.sub(r"\s+", " ", page.extract_text() or "")
        low = text.lower()
        for key in KEYS:
            pos = low.find(key)
            if pos < 0:
                continue
            parts.append(f"p.{i} [{key}]: {text[max(0,pos-140):pos+320]}\n")
            n += 1
            if n >= 7:
                break
        if n >= 7:
            break
    if n == 0:
        parts.append("NO_HIT\n")

text = "".join(parts).encode("utf-8", "replace").decode("utf-8")
OUT.write_text(text, encoding="utf-8")
print("wrote", len(text))
