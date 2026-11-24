# -*- coding: utf-8 -*-
import os
from pypdf import PdfReader

src = r"D:\TRINH\GraphSSL_KT_Survey\15. Check list\2026.11.13\NhanXet_Survey_GraphSSLKT_Trinh_2026Nov13.pdf"
out = r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\reviewer_2026-11-13_extract.txt"
reader = PdfReader(src)
parts = []
for i, page in enumerate(reader.pages, 1):
    text = page.extract_text() or ""
    text = "".join(ch for ch in text if not 0xD800 <= ord(ch) <= 0xDFFF)
    parts.append(f"\n\n===== PAGE {i} =====\n")
    parts.append(text)
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    fh.write("".join(parts))
print("pages", len(reader.pages), "chars", sum(len(p) for p in parts))
