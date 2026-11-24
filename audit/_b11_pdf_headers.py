from pathlib import Path
from pypdf import PdfReader

files = [
    Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references\Deep Knowledge Tracing.pdf"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references\A Self-Attentive Model for Knowledge Tracing.pdf"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references\pyKT - A Python Library to Benchmark Deep Learning based Knowledge Tracing Models.pdf"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references\Deep Graph Memory Networks for Forgetting-Robust Knowledge Tracing.pdf"),
]
out = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_b11_pdf_headers.txt")
lines = []
for path in files:
    reader = PdfReader(str(path))
    n = len(reader.pages)
    first = (reader.pages[0].extract_text() or "")[:1500]
    last = (reader.pages[-1].extract_text() or "")[:800]
    lines.append(f"==== {path.name} pages={n}")
    lines.append("--- first ---")
    lines.append(first)
    lines.append("--- last ---")
    lines.append(last)
    lines.append("")
out.write_text("\n".join(lines), encoding="utf-8")
print("wrote", out, "chars", out.stat().st_size)
