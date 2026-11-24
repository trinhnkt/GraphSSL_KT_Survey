# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader

REF = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
OUT = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\ssl_objective_windows_2026-11-24.txt")

PDFS = {
    "KT011": "Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf",
    "KT026": "Improving Knowledge Tracing via Pre-training Question Embeddings.pdf",
    "KT039": "CL4KT - Contrastive Learning for Knowledge Tracing.pdf",
    "KT042": "Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf",
    "KT043": "Weighted Heterogeneous Graph-Based Three-View Contrastive Learning for Knowledge Tracing in Personalized e-Learning Systems.pdf",
    "KT047": "Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing.pdf",
    "KT050": "GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf",
    "KT066": "Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing.pdf",
    "KT068": "HKT - Hierarchical Structure-Based Knowledge Tracing.pdf",
}

# CL4KT filename may differ
if not (REF / PDFS["KT039"]).exists():
    cands = list(REF.glob("*CL4KT*")) + list(REF.glob("*Contrastive Learning for Knowledge Tracing*"))
    PDFS["KT039"] = cands[0].name if cands else PDFS["KT039"]

PAT = re.compile(
    r".{0,90}(InfoNCE|contrastive loss|positive pair|negative pair|negative sample|reconstruct|"
    r"augmentation|edge drop|dropout|mask|prerequisite|preserve|momentum|mutual information|"
    r"self-supervised|self supervised).{0,220}",
    re.I,
)

parts = []
for pid, name in PDFS.items():
    path = REF / name
    parts.append(f"\n######## {pid} exists={path.exists()} {name} ########\n")
    if not path.exists():
        continue
    reader = PdfReader(str(path))
    n = 0
    for i, page in enumerate(reader.pages, start=1):
        if i > len(reader.pages) - 2:
            continue
        text = re.sub(r"\s+", " ", page.extract_text() or "")
        for m in PAT.finditer(text):
            frag = m.group(0)
            if frag.lower().count("et al") and "we " not in frag.lower() and "our " not in frag.lower():
                continue
            parts.append(f"p.{i}: {frag}\n")
            n += 1
            if n >= 8:
                break
        if n >= 8:
            break
    if n == 0:
        parts.append("NO_HIT\n")

text = "".join(parts).encode("utf-8", "replace").decode("utf-8")
OUT.write_text(text, encoding="utf-8")
print("KT039 file", PDFS["KT039"])
print("wrote", OUT.stat().st_size)
