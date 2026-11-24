from pathlib import Path
from pypdf import PdfReader

path = Path(r"12_manuscript/TLT/main_tlt_anonymous.pdf")
text = "\n".join((p.extract_text() or "") for p in PdfReader(str(path)).pages)
idx = text.upper().find("METHODOLOGY")
print("methodology idx", idx)
print(repr(text[max(0, idx-80):idx+120]) if idx >= 0 else "none")
print("--- PRISMA-STYLE count", text.upper().count("PRISMA-STYLE"))
