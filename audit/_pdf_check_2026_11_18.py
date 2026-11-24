from pathlib import Path
from pypdf import PdfReader

files = [
    Path(r"12_manuscript/TLT/main_tlt_anonymous.pdf"),
    Path(r"12_manuscript/TLT/main_tlt_full.pdf"),
    Path(r"12_manuscript/TLT/manuscript_TLT_FORMATTED_v1.3.pdf"),
]
needles = ["0.0361", "0.1770", "Shukurlu", "Scope of Claims", "DyGKT", "0/37"]
for path in files:
    reader = PdfReader(str(path))
    text = "\n".join((page.extract_text() or "") for page in reader.pages)
    print(f"\n{path.name} pages={len(reader.pages)} bytes={path.stat().st_size}")
    for needle in needles:
        print(f"  {needle!r}: {text.count(needle)}")
