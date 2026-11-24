from pathlib import Path
from pypdf import PdfReader
text = "\n".join((p.extract_text() or "") for p in PdfReader(r"12_manuscript/TLT/main_tlt_anonymous.pdf").pages)
for needle in ["node dropout", "PageRank", "Line-graph", "InfoNCE", "Recover bipartite"]:
    print(repr(needle), text.lower().count(needle.lower()))
