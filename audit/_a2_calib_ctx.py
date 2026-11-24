import csv
import re
from pathlib import Path
import fitz

root = Path(r"D:\TRINH\GraphSSL_KT_Survey")
src = root / "12_manuscript" / "TLT" / "supplementary" / "calibration_keyword_scan_v1.9.csv"
pdf_dir = root / "14_references"
pat = re.compile(r"\bcalibrat\w*|\breliability (diagram|curve|plot)|calibration (curve|plot)", re.I)
out = []
with src.open(encoding="utf-8-sig", newline="") as handle:
    for row in csv.DictReader(handle):
        if row["in_primary_core_37"] != "YES":
            continue
        if int(row["calibration_strings"]) == 0 and int(row["reliability_diagram_or_plot"]) == 0:
            continue
        pdf = pdf_dir / row["pdf"]
        doc = fitz.open(pdf)
        text = re.sub(r"\s+", " ", " ".join(page.get_text() for page in doc))
        doc.close()
        hits = list(pat.finditer(text))
        out.append(f"\n===== {row['pdf']} n={len(hits)} =====\n")
        for match in hits[:8]:
            start = max(0, match.start() - 90)
            end = min(len(text), match.end() + 90)
            out.append(text[start:end] + "\n")
Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a2_calib_contexts.txt").write_text("".join(out), encoding="utf-8")
print("papers", out.count("====="))
