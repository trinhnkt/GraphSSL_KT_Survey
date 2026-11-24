from pathlib import Path
from pypdf import PdfReader

path = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references\Survey of Loss Augmented Knowledge Tracing.pdf")
reader = PdfReader(str(path))
print("pages", len(reader.pages))
print("size", path.stat().st_size)
text = "\n".join((p.extract_text() or "") for p in reader.pages[:2])
out = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_shukurlu_pdf_head.txt")
out.write_text(text[:2500], encoding="utf-8")
print(text[:1200])
