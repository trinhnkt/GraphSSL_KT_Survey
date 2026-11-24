# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader
REF = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
jobs = {
 "KT042": "Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf",
 "KT066": "Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing.pdf",
 "KT050": "GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf",
 "KT011": "Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf",
 "KT068": "HKT - Hierarchical Structure-Based Knowledge Tracing.pdf",
}
out = []
for pid, name in jobs.items():
    reader = PdfReader(str(REF / name))
    out.append(f"\n## {pid}\n")
    n = 0
    for i, page in enumerate(reader.pages, start=1):
        if i < 6:
            continue
        text = re.sub(r"\s+", " ", page.extract_text() or "")
        for key in ["positive pair", "positive sample", "InfoNCE", "contrastive loss", "we preserve", "prerequisite"]:
            pos = text.lower().find(key.lower())
            if pos < 0:
                continue
            out.append(f"p.{i} [{key}]: {text[max(0,pos-100):pos+280]}\n")
            n += 1
            if n >= 3:
                break
        if n >= 3:
            break
Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\ssl_pairs_2026-11-24.txt").write_text("".join(out).encode("utf-8","replace").decode("utf-8"), encoding="utf-8")
print("ok", len(out))
