# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader
REF = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
jobs = [
 ("KT023", "SGKT - Session Graph-Based Knowledge Tracing for Student Performance Prediction.pdf", 9, "eight groups"),
 ("KT035", "HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf", 0, "drop"),
 ("KT038", "DyGKT - Dynamic Graph Learning for Knowledge Tracing.pdf", 5, "unseen"),
]
out = []
for pid, name, page, key in jobs:
    reader = PdfReader(str(REF / name))
    if page:
        pages = [page]
    else:
        pages = range(1, len(reader.pages)+1)
    n = 0
    for i in pages:
        text = re.sub(r"\s+", " ", reader.pages[i-1].extract_text() or "")
        pos = text.lower().find(key)
        if pos < 0:
            continue
        out.append(f"{pid} p.{i}: {text[max(0,pos-200):pos+500]}\n")
        n += 1
        if n >= 2:
            break
Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\counts_quotes_2026-11-24.txt").write_text("".join(out).encode("utf-8","replace").decode("utf-8"), encoding="utf-8")
print("n", len(out))
