# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader

p = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references\HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf")
reader = PdfReader(str(p))
rx = re.compile(
    r".{0,90}(50%|percent of|proportion|sparsity level|data were|we remove|dropped).{0,180}",
    re.I,
)
out = []
for i, page in enumerate(reader.pages, start=1):
    if i < 8:
        continue
    text = re.sub(r"\s+", " ", page.extract_text() or "")
    for m in rx.finditer(text):
        frag = m.group(0)
        out.append(f"p.{i}: {frag}\n")
        if len(out) >= 8:
            break
    if len(out) >= 8:
        break
Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\hhskt_drop_2026-11-24.txt").write_text(
    "".join(out).encode("utf-8", "replace").decode("utf-8"), encoding="utf-8"
)
print("hits", len(out), "pages", len(reader.pages))
