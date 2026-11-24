from pathlib import Path
from pypdf import PdfReader

needles = ["0.0361", "PRISMA 2020", "0/37", "Task clarity", "2,017", "Shukurlu"]
pdf = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_anonymous.pdf")
text = "\n".join((p.extract_text() or "") for p in PdfReader(str(pdf)).pages)
flat = text.replace(" ", "").replace("\n", "")
print("pages", len(PdfReader(str(pdf)).pages))
for n in needles:
    print(repr(n), text.count(n))
print("Nrec", "Nrec" in flat or "N_{\mathrm{rec}}" in text)
print("PRISMASTYLE", "PRISMA-STYLE" in flat.upper() or "PRISMA-style" in text)
