# -*- coding: utf-8 -*-
from pathlib import Path
from pypdf import PdfReader
pdf = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references") / "Model Generalization - A Sharpness Aware Optimization Perspective.pdf"
reader = PdfReader(str(pdf))
text = reader.pages[0].extract_text() or ""
text = "".join(ch for ch in text if not (0xD800 <= ord(ch) <= 0xDFFF))
out = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_example_sam_p1.txt")
out.write_text(f"pages {len(reader.pages)}\n\n{text[:1200]}", encoding="utf-8", newline="\n")
