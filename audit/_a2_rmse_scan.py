import csv
import re
from pathlib import Path

import fitz

root = Path(r"D:\TRINH\GraphSSL_KT_Survey")
src = root / "12_manuscript" / "TLT" / "supplementary" / "calibration_keyword_scan_v1.9.csv"
pdf_dir = root / "14_references"
out_txt = root / "audit" / "_a2_rmse_contexts.txt"
out_csv = root / "audit" / "_a2_rmse_counts.csv"

pat = re.compile(r"\bRMSE\b|root[- ]mean[- ]square", re.I)

rows_out = []
chunks = []
with src.open(encoding="utf-8-sig", newline="") as handle:
    for row in csv.DictReader(handle):
        if row["in_primary_core_37"] != "YES":
            continue
        pdf = pdf_dir / row["pdf"]
        if not pdf.exists():
            chunks.append(f"\nMISSING {row['pdf']}\n")
            continue
        doc = fitz.open(pdf)
        text = " ".join(page.get_text() for page in doc)
        doc.close()
        text = re.sub(r"\s+", " ", text)
        hits = list(pat.finditer(text))
        rows_out.append({"pdf": row["pdf"], "rmse_strings": len(hits), "pages": row["pages"]})
        if hits:
            chunks.append(f"\n===== {row['pdf']} n={len(hits)} =====\n")
            for match in hits[:6]:
                start = max(0, match.start() - 110)
                end = min(len(text), match.end() + 110)
                chunks.append(text[start:end] + "\n")

with out_csv.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["pdf", "rmse_strings", "pages"])
    writer.writeheader()
    writer.writerows(rows_out)
out_txt.write_text("".join(chunks), encoding="utf-8")
nonzero = [r for r in rows_out if r["rmse_strings"]]
print("primary", len(rows_out), "with_rmse", len(nonzero), "string_sum", sum(r["rmse_strings"] for r in rows_out))
