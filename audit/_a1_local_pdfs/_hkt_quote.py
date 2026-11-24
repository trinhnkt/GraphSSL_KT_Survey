import fitz
from pathlib import Path

doc = fitz.open(
    Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
    / "HKT - Hierarchical Structure-Based Knowledge Tracing.pdf"
)
text = doc[9].get_text("text")
low = text.lower()
pos = low.find("dtransformer")
Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_local_pdfs\hkt_quote.txt").write_text(
    text[max(0, pos - 80) : pos + 900], encoding="utf-8"
)
doc.close()
