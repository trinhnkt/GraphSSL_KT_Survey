# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader

pdf = Path(
    r"D:\TRINH\GraphSSL_KT_Survey\14_references"
    r"\GKT-CD Make Cognitive Diagnosis Model Enhanced by Graph-based Knowledge Tracing.pdf"
)
reader = PdfReader(str(pdf))
meta = reader.metadata or {}
pages = []
for i, page in enumerate(reader.pages[:3], start=1):
    text = re.sub(r"\s+", " ", page.extract_text() or "")
    pages.append(f"===== PAGE {i} =====\n{text[:2500]}\n")

out = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\GKTCD_pdf_head_2026-11-24.txt")
out.parent.mkdir(parents=True, exist_ok=True)
blob = (
    f"file={pdf.name}\n"
    f"bytes={pdf.stat().st_size}\n"
    f"n_pages={len(reader.pages)}\n"
    f"meta_title={meta.get('/Title')}\n"
    f"meta_author={meta.get('/Author')}\n"
    f"meta_subject={meta.get('/Subject')}\n\n"
    + "\n".join(pages)
)
out.write_text(blob.encode("utf-8", "replace").decode("utf-8"), encoding="utf-8")

# keyword checks
full = " ".join(re.sub(r"\s+", " ", (p.extract_text() or "")) for p in reader.pages[:4])
checks = {
    "doi_string": "10.1109/IJCNN52387.2021.9533298" in full.replace(" ", ""),
    "doi_loose": "9533298" in full,
    "title_gktcd": "GKT-CD" in full or "Make Cognitive Diagnosis Model Enhanced" in full,
    "ijcnn": "IJCNN" in full or "International Joint Conference on Neural Networks" in full,
    "wrong_cognitive_situation": "Cognitive Situation" in full and "Classic Assertions" in full,
}
print("pages", len(reader.pages))
print("checks", checks)
print("wrote", out)
