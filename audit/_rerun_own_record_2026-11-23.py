# -*- coding: utf-8 -*-
"""Own-record check: DOI or title field, not an abstract mention."""
import csv
import re
from pathlib import Path

root = Path(r"D:\TRINH\GraphSSL_KT_Survey\03_search\exports")
papers = [
    ("DECKT", "10.3390/e27070685", "dual-encoder contrastive learning model for knowledge tracing"),
    ("DTransformer", "10.1145/3543507.3583255", "tracing knowledge instead of patterns"),
    ("SPCLKT", "10.1016/j.neucom.2024.128366", "self-paced contrastive learning for knowledge tracing"),
    ("Han", "10.1016/j.asoc.2024.112194", "dynamic heterogeneous graph contrastive networks for knowledge tracing"),
    ("HCMKT", "10.1016/j.eswa.2025.128840", "heterogeneous graph knowledge tracing with novel contrastive view"),
    ("CLBG", "10.1007/978-981-96-0821-8_14", "contrastive learning based on bipartite graphs for interpretable"),
    ("CoSKT", "10.1109/tlt.2024.3386750", "collaborative self-supervised learning method for knowledge tracing"),
]

def own(title, doi):
    blob = f"{title} {doi}".lower()
    return [name for name, d, t in papers if d in blob or t in blob]

for path in sorted(root.iterdir()):
    if path.suffix.lower() == ".csv":
        with path.open(encoding="utf-8", errors="replace", newline="") as fh:
            rows = list(csv.DictReader(fh))
        found = set()
        for row in rows:
            title = row.get("Document Title") or row.get("Title") or row.get("Item Title") or ""
            doi = row.get("DOI") or row.get("Item DOI") or ""
            found.update(own(title, doi))
        print(path.name, "OWN", ";".join(sorted(found)) or "-")
    elif path.suffix.lower() == ".bib":
        text = path.read_text(encoding="utf-8", errors="replace")
        entries = re.split(r"(?m)^@", text)[1:]
        found = set()
        for entry in entries:
            title_m = re.search(r"(?is)title\s*=\s*\{(.*?)\}", entry)
            doi_m = re.search(r"(?is)doi\s*=\s*\{(.*?)\}", entry)
            found.update(own(title_m.group(1) if title_m else "", doi_m.group(1) if doi_m else ""))
        print(path.name, "OWN", ";".join(sorted(found)) or "-")
    elif path.suffix.lower() == ".xml":
        text = path.read_text(encoding="utf-8", errors="replace")
        titles = re.findall(r"<title>(.*?)</title>", text, flags=re.S)
        found = set()
        for title in titles:
            found.update(own(title, ""))
        print(path.name, "OWN", ";".join(sorted(found)) or "-", "titles", len(titles))
