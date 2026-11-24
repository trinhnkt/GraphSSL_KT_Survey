# -*- coding: utf-8 -*-
"""Extract the bipartite-graph chapter. Does not edit the manuscript."""
from pathlib import Path
from pypdf import PdfReader

pdf = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references") / (
    "Contrastive Learning Based on Bipartite Graphs for Interpretable Knowledge Tracing.pdf"
)
out_dir = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence")
out_dir.mkdir(parents=True, exist_ok=True)
reader = PdfReader(str(pdf))
parts = []
index_lines = [f"pages={len(reader.pages)}", f"bytes={pdf.stat().st_size}"]
for i, page in enumerate(reader.pages, start=1):
    text = page.extract_text() or ""
    text = "".join(ch for ch in text if not (0xD800 <= ord(ch) <= 0xDFFF))
    parts.append(f"\n\n===== PAGE {i} =====\n\n{text}")
    head = " ".join(text.split())[:240]
    index_lines.append(f"p{i:02d}: {head}")
text_path = out_dir / "BipartiteKT_fulltext_2026-11-23.txt"
index_path = out_dir / "BipartiteKT_index_2026-11-23.txt"
text_path.write_text("".join(parts), encoding="utf-8", newline="\n")
index_path.write_text("\n".join(index_lines), encoding="utf-8", newline="\n")
print(f"pages={len(reader.pages)} chars={text_path.stat().st_size}")
