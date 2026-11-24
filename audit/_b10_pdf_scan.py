from pathlib import Path
from pypdf import PdfReader

pdf = Path(r"15. Check list/2026.11.13/NhanXet_Survey_GraphSSLKT_Trinh_2026Nov13.pdf")
reader = PdfReader(str(pdf))
out = []
out.append(f"pages={len(reader.pages)}")
for i, page in enumerate(reader.pages, start=1):
    text = page.extract_text() or ""
    out.append(f"\n===== PAGE {i} =====\n")
    out.append(text)
Path("audit/_b10_reviewer_extract.txt").write_text("".join(out), encoding="utf-8")
print("pages", len(reader.pages), "chars", sum(len(p.extract_text() or "") for p in reader.pages))
