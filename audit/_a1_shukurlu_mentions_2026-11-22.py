# -*- coding: utf-8 -*-
from pathlib import Path
from pypdf import PdfReader

pdf = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references\Survey of Loss Augmented Knowledge Tracing.pdf")
out = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_2026-11-22\shukurlu_mentions.txt")
reader = PdfReader(str(pdf))
needles = ("coskt", "hcmkt", "meta-path", "112194", "han et", "dynamic heterogeneous", "collaborative self")
lines = []
for i, page in enumerate(reader.pages, start=1):
    text = page.extract_text() or ""
    low = text.lower()
    if any(n in low for n in needles):
        lines.append(f"\n===== PAGE {i} =====\n")
        lines.append(text)
out.write_text("".join(lines), encoding="utf-8")
print("pages", len(reader.pages), "matched_chars", len("".join(lines)))
