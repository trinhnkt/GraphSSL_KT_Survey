# -*- coding: utf-8 -*-
"""Count saved 14-16 Nov 2026 search exports and locate the seven screened papers."""
import csv
import re
from pathlib import Path

root = Path(r"D:\TRINH\GraphSSL_KT_Survey\03_search\exports")
papers = {
    "DECKT": ["10.3390/e27070685", "dual-encoder contrastive learning model for knowledge tracing"],
    "DTransformer": ["10.1145/3543507.3583255", "tracing knowledge instead of patterns"],
    "SPCLKT": ["10.1016/j.neucom.2024.128366", "self-paced contrastive learning for knowledge tracing"],
    "Han": ["10.1016/j.asoc.2024.112194", "dynamic heterogeneous graph contrastive networks for knowledge tracing"],
    "HCMKT": ["10.1016/j.eswa.2025.128840", "heterogeneous graph knowledge tracing with novel contrastive view"],
    "CLBG": ["10.1007/978-981-96-0821-8_14", "contrastive learning based on bipartite graphs for interpretable"],
    "CoSKT": ["10.1109/tlt.2024.3386750", "collaborative self-supervised learning method for knowledge tracing"],
}

def hits(text):
    low = text.lower()
    found = []
    for name, keys in papers.items():
        if any(k in low for k in keys):
            found.append(name)
    return found

def year_after_cutoff(year_text):
    years = [int(y) for y in re.findall(r"\b(20\d\d)\b", year_text or "")]
    return any(y > 2026 for y in years)

rows_out = []
for path in sorted(root.iterdir()):
    if path.name == ".gitkeep":
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    kind = path.suffix.lower()
    n = None
    late = None
    if kind == ".csv":
        with path.open(encoding="utf-8", errors="replace", newline="") as fh:
            reader = csv.DictReader(fh)
            data = list(reader)
        n = len(data)
        year_fields = [c for c in (reader.fieldnames or []) if c and "year" in c.lower()]
        if year_fields:
            late = sum(1 for row in data if any(year_after_cutoff(row.get(c, "")) for c in year_fields))
        found = hits("\n".join(" ".join(row.values()) for row in data))
    elif kind == ".bib":
        n = len(re.findall(r"(?m)^@", text))
        late = sum(1 for y in re.findall(r"(?m)^year\s*=\s*\{(\d{4})\}", text, flags=re.I) if int(y) > 2026)
        found = hits(text)
    elif kind == ".xml":
        n = len(re.findall(r"<entry>", text))
        dates = re.findall(r"<published>(\d{4}-\d{2}-\d{2})", text)
        late = sum(1 for d in dates if d > "2026-07-31")
        found = hits(text)
    else:
        continue
    rows_out.append({
        "file": path.name,
        "records": n,
        "records_after_2026": late if late is not None else "",
        "papers": ";".join(found),
    })

out = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_rerun_file_counts_2026-11-23.csv")
with out.open("w", encoding="utf-8", newline="\n") as fh:
    writer = csv.DictWriter(fh, fieldnames=["file", "records", "records_after_2026", "papers"])
    writer.writeheader()
    writer.writerows(rows_out)
for row in rows_out:
    print(f"{row['file']}\t{row['records']}\tlate={row['records_after_2026']}\t{row['papers']}")
