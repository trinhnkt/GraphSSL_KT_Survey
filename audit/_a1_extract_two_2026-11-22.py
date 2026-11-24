# -*- coding: utf-8 -*-
from pathlib import Path
from pypdf import PdfReader

pairs = [
    (
        Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references\Dynamic heterogeneous graph contrastive networks for knowledge tracing.pdf"),
        Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\Han2024_fulltext_2026-11-22.txt"),
    ),
    (
        Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references\Heterogeneous graph knowledge tracing with novel contrastive view and meta-path contexts.pdf"),
        Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\HCMKT_fulltext_2026-11-22.txt"),
    ),
]
needles = (
    "contrastive", "infoNCE", "infonce", "self-supervised", "self supervised",
    "bipartite", "meta-path", "metapath", "heterogeneous", "graph attention",
    "cold-start", "cold start", "ECE", "Brier", "AUC", "accuracy",
)
for src, dst in pairs:
    reader = PdfReader(str(src))
    chunks = []
    hits = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        chunks.append(f"\n\n===== PAGE {i} =====\n")
        chunks.append(text)
        low = text.lower()
        found = [n for n in needles if n.lower() in low]
        if found:
            hits.append(f"p{i}: {', '.join(found)}")
    dst.write_text("".join(chunks), encoding="utf-8")
    summary = dst.with_name(dst.stem + "_index.txt")
    summary.write_text(
        src.name + "\n"
        + f"pages {len(reader.pages)} chars {dst.stat().st_size}\n"
        + "HEAD " + " ".join((chunks[1] or "").split())[:500] + "\n"
        + "\n".join(hits),
        encoding="utf-8",
    )
    print(src.name, len(reader.pages), dst.stat().st_size)
