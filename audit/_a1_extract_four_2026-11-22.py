# -*- coding: utf-8 -*-
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
pairs = [
    ("CoSKT A Collaborative Self-Supervised Learning Method for Knowledge Tracing.pdf", "CoSKT_fulltext_2026-11-22.txt"),
    ("Self-paced contrastive learning for knowledge tracing.pdf", "SPCLKT_fulltext_2026-11-22.txt"),
    ("Tracing Knowledge Instead of Patterns Stable Knowledge Tracing with Diagnostic Transformer.pdf", "DTransformer_pdf_2026-11-22.txt"),
    ("A Dual-Encoder Contrastive Learning Model for Knowledge Tracing (DECKT).pdf", "DECKT_pdf_head_2026-11-22.txt"),
]
needles = (
    "contrastive", "infonce", "self-supervised", "self supervised", "consistency",
    "graph", "bipartite", "gnn", "gcn", "gat", "cold-start", "cold start",
    "brier", "ece", "auc", "rmse",
)
out_dir = ROOT / "audit" / "_a1_evidence"
for src_name, dst_name in pairs:
    reader = PdfReader(str(ROOT / "14_references" / src_name))
    pages = reader.pages if "DECKT" not in dst_name else reader.pages[:2]
    chunks = []
    hits = []
    for i, page in enumerate(pages, start=1):
        text = page.extract_text() or ""
        text = "".join(ch if not (0xD800 <= ord(ch) <= 0xDFFF) else " " for ch in text)
        chunks.append(f"\n\n===== PAGE {i} =====\n")
        chunks.append(text)
        low = text.lower()
        found = [n for n in needles if n in low]
        if found:
            hits.append(f"p{i}: {', '.join(found)}")
    dst = out_dir / dst_name
    dst.write_text("".join(chunks), encoding="utf-8")
    (out_dir / (dst.stem + "_index.txt")).write_text(
        f"pages_read {len(pages)} of {len(reader.pages)} chars {dst.stat().st_size}\n" + "\n".join(hits),
        encoding="utf-8",
    )
    print(dst_name, len(pages), "of", len(reader.pages), dst.stat().st_size)
