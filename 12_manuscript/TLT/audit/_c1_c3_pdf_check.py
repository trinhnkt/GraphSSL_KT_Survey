from pathlib import Path
from pypdf import PdfReader

checks = {
    "Nrec": "Nrec",
    "qa_task": "Task clarity",
    "qa7": "35",
    "generic_old": "Generic sparsity only",
    "generic_new": "Interaction sparsity only",
    "ece": "0/37",
    "edge": "Edge dropout",
}
# text search strings that survive extraction
needles = [
    "2,017",
    "Task clarity",
    "Interaction sparsity only",
    "Generic sparsity only",
    "0/37",
    "Expected calibration error",
]
pdfs = [
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_anonymous.pdf"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_full.pdf"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\manuscript_TLT_FORMATTED_v1.3.pdf"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\COVER_LETTER.pdf"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\COVER_LETTER.pdf"),
]
out = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\audit\_c1_c3_pdf_check.txt")
lines = []
for pdf in pdfs:
    reader = PdfReader(str(pdf))
    text = "\n".join((p.extract_text() or "") for p in reader.pages)
    lines.append(f"==== {pdf.name} pages={len(reader.pages)} chars={len(text)}")
    for n in needles:
        lines.append(f"  {n!r} {text.count(n)}")
    lines.append(f"  N_rec-ish {'Nrec' in text.replace(' ', '')} raw_N_mathrm {text.count('N')}")
out.write_text("\n".join(lines), encoding="utf-8")
print("\n".join(lines))
