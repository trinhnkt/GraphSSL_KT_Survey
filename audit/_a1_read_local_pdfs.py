"""Read every PDF in 14_references for the A1 local-library check.

Writes text extracts and a JSON inventory. Does not decide inclusion.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import fitz

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
OUT = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_local_pdfs")
OUT.mkdir(parents=True, exist_ok=True)

NEEDLES = {
    "DECKT": ["10.3390/e27070685", "dual-encoder contrastive", "deckt"],
    "DTransformer": ["10.1145/3543507.3583255", "diagnostic transformer", "dtransformer"],
    "SelfPaced": ["10.1016/j.neucom.2024.128366", "self-paced contrastive"],
    "CoSKT": ["10.1109/tlt.2024.3386750", "coskt"],
    "HCMKT": ["10.1016/j.eswa.2025.128840", "meta-path contexts", "hcmkt"],
    "BipartiteCL": ["10.1007/978-981-96-0821-8_14", "bipartite graphs for interpretable"],
    "DynHet": ["10.1016/j.asoc.2024.112194", "dynamic heterogeneous graph contrastive"],
}

DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)


def page_text(doc, i):
    return doc[i].get_text("text") or ""


def first_title_lines(text):
    lines = []
    for raw in text.splitlines():
        s = " ".join(raw.split())
        if len(s) < 8:
            continue
        if s.lower() in {"abstract", "introduction", "keywords"}:
            break
        lines.append(s)
        if len(lines) >= 8:
            break
    return lines


inventory = []
needle_hits = {k: [] for k in NEEDLES}

for pdf in sorted(ROOT.glob("*.pdf")):
    doc = fitz.open(pdf)
    n = doc.page_count
    first = page_text(doc, 0)
    second = page_text(doc, 1) if n > 1 else ""
    head = first + "\n" + second
    dois = []
    for m in DOI_RE.findall(head):
        d = m.rstrip(".)")
        if d not in dois:
            dois.append(d)
    # full-text search for the seven candidates only
    blob_parts = [head.lower()]
    # scan remaining pages in chunks; stop early per needle once found
    remaining = []
    for i in range(2, n):
        remaining.append(page_text(doc, i))
    full_l = ("\n".join(blob_parts + [p.lower() for p in remaining]))
    hits = []
    for name, needles in NEEDLES.items():
        for needle in needles:
            if needle.lower() in full_l:
                hits.append(f"{name}:{needle}")
                needle_hits[name].append(pdf.name)
                break
    # reference-section start: last occurrence of a references heading
    ref_start = None
    for i in range(n - 1, max(-1, n - 25), -1):
        t = page_text(doc, i)
        if re.search(r"\n\s*references\s*\n", "\n" + t.lower()):
            ref_start = i
            break
    ref_excerpt = ""
    if ref_start is not None:
        ref_excerpt = "\n".join(page_text(doc, i) for i in range(ref_start, n))
        (OUT / (pdf.stem[:80] + "_refs.txt")).write_text(ref_excerpt, encoding="utf-8")
    (OUT / (pdf.stem[:80] + "_p1.txt")).write_text(head, encoding="utf-8")
    inventory.append(
        {
            "file": pdf.name,
            "pages": n,
            "chars_page1": len(first.strip()),
            "dois_page1_2": dois[:8],
            "title_lines": first_title_lines(first),
            "candidate_hits": hits,
            "ref_start_page_1indexed": None if ref_start is None else ref_start + 1,
        }
    )
    doc.close()

(OUT / "inventory.json").write_text(
    json.dumps({"files": inventory, "needle_files": needle_hits}, indent=2),
    encoding="utf-8",
)
print(f"pdfs={len(inventory)}")
for name, files in needle_hits.items():
    uniq = sorted(set(files))
    print(f"{name}: {len(uniq)} files")
    for f in uniq:
        print(f"  - {f}")
