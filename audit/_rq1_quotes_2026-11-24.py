# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pypdf import PdfReader

REF = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
OUT = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\rq1_quotes_2026-11-24.txt")

def page_text(name, page):
    reader = PdfReader(str(REF / name))
    return re.sub(r"\s+", " ", reader.pages[page - 1].extract_text() or "")

parts = []
t = page_text("Heterogeneous Graph-Based Knowledge Tracing with Spatiotemporal Evolution.pdf", 5)
i = t.lower().find("highest frequency")
parts.append("KT036 p.5\n" + t[max(0, i - 500): i + 300] + "\n\n")

t = page_text("Multi-Granularity Ensemble Interaction Graph Modeling for Knowledge Tracing.pdf", 6)
i = t.find("𝐀(𝑠𝑚)")
if i < 0:
    i = t.lower().find("sigmoid")
parts.append("KT064 p.6\n" + t[max(0, i - 450): i + 400] + "\n\n")

t = page_text("Exploring Long- and Short-Term Knowledge State Graph Representations with Adaptive Fusion for Knowledge Tracing.pdf", 7)
i = t.lower().find("adjacency")
parts.append("KT056 p.7\n" + t[max(0, i - 400): i + 350] + "\n\n")

# KT076 alternate extractor
name = "KGNN-KT - Enhancing Knowledge Tracing in Programming Education Through LLM-Extracted Knowledge Graphs.pdf"
note = "pypdf chars " + str(sum(len(p.extract_text() or "") for p in PdfReader(str(REF / name)).pages))
try:
    import fitz
    doc = fitz.open(REF / name)
    chars = sum(len(p.get_text() or "") for p in doc)
    note += f"; pymupdf chars {chars}; pages {doc.page_count}"
    if chars:
        sample = doc[0].get_text()[:500]
        note += "\n" + sample
except Exception as e:
    note += f"; pymupdf error {type(e).__name__}: {e}"
parts.append("KT076\n" + note + "\n")

text = "".join(parts).encode("utf-8", "replace").decode("utf-8")
OUT.write_text(text, encoding="utf-8")
print("wrote", OUT.stat().st_size)
