from pathlib import Path
from pypdf import PdfReader

root = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
files = [
    "Deep Knowledge Tracing.pdf",
    "A Self-Attentive Model for Knowledge Tracing.pdf",
    "pyKT - A Python Library to Benchmark Deep Learning based Knowledge Tracing Models.pdf",
]
needles = ["505", "513", "384", "389", "18542", "18555", "NeurIPS", "volume"]
lines = []
for name in files:
    reader = PdfReader(str(root / name))
    lines.append(f"\n== {name} n={len(reader.pages)}")
    for i, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        for needle in needles:
            if needle in text:
                j = text.find(needle)
                snippet = text[max(0, j - 60):j + 80].replace("\n", " ")
                lines.append(f"p{i} {needle}: {snippet}")
Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_pdf_pages.txt").write_text("\n".join(lines), encoding="utf-8")
print("hits", len(lines))
