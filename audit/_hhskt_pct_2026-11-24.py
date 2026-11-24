# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader
p = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references\HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf")
reader = PdfReader(str(p))
rx = re.compile(r".{0,70}(\d+\s*%|sparse interaction|interaction spars).{0,140}", re.I)
out = []
for i, page in enumerate(reader.pages, start=1):
    text = re.sub(r"\s+", " ", page.extract_text() or "")
    for m in rx.finditer(text):
        out.append(f"p.{i}: {m.group(0)}\n")
Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\hhskt_pct_2026-11-24.txt").write_text(
    "".join(out).encode("utf-8","replace").decode("utf-8"), encoding="utf-8")
print("hits", len(out))
