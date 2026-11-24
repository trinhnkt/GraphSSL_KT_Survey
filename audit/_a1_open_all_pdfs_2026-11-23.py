# -*- coding: utf-8 -*-
"""Open every PDF in 14_references and record identity plus result strings.
Does not edit the manuscript.
"""
import csv
import os
import re

from pypdf import PdfReader

ROOT = r"D:\TRINH\GraphSSL_KT_Survey\14_references"
OUT = r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\pdf_open_2026-11-23.csv"
PATTERNS = {
    "ece": re.compile(r"\bECE\b|expected calibration error", re.I),
    "brier": re.compile(r"\bBrier\b", re.I),
    "reliability": re.compile(r"reliability diagram|calibration plot|calibration curve", re.I),
    "cold": re.compile(r"cold[- ]start", re.I),
    "rmse": re.compile(r"\bRMSE\b|root[- ]mean[- ]square", re.I),
}


def clean(text):
    if not text:
        return ""
    return "".join(ch for ch in text if not 0xD800 <= ord(ch) <= 0xDFFF)


def main():
    rows = []
    names = sorted(
        name for name in os.listdir(ROOT)
        if name.lower().endswith(".pdf")
    )
    for name in names:
        path = os.path.join(ROOT, name)
        row = {
            "file": name,
            "bytes": os.path.getsize(path),
            "pages": "",
            "chars": 0,
            "page1": "",
            "ece": 0,
            "brier": 0,
            "reliability": 0,
            "cold": 0,
            "rmse": 0,
            "error": "",
        }
        try:
            reader = PdfReader(path)
            row["pages"] = len(reader.pages)
            parts = []
            for page in reader.pages:
                parts.append(clean(page.extract_text() or ""))
            text = "\n".join(parts)
            row["chars"] = len(text)
            row["page1"] = " ".join(parts[0].split())[:400] if parts else ""
            for key, pat in PATTERNS.items():
                row[key] = len(pat.findall(text))
        except Exception as exc:
            row["error"] = str(exc)
        rows.append(row)
        print(f"{row['pages']:>3} p  chars={row['chars']:>7}  ECE={row['ece']} Brier={row['brier']} rel={row['reliability']} cold={row['cold']} RMSE={row['rmse']}  {name[:70]}")
    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
