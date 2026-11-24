from pathlib import Path
from pypdf import PdfReader
path = Path(r"12_manuscript/TLT/main_tlt_anonymous.pdf")
text = "\n".join((p.extract_text() or "") for p in PdfReader(str(path)).pages)
for needle in ["Twelve of the 37", "0/37", "unverified in this corpus", "0.0361"]:
    print(needle, text.count(needle), "pages", len(PdfReader(str(path)).pages))
