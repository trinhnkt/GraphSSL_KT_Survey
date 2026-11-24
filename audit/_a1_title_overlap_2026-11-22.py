# -*- coding: utf-8 -*-
import csv
import re
from pathlib import Path

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
bib = (ROOT / "12_manuscript" / "TLT" / "references.bib").read_text(encoding="utf-8")
raw = re.findall(r"title\s*=\s*(\{(?:[^{}]|\{[^{}]*\})*\})", bib)


def norm(text):
    text = text.lower().replace("{", "").replace("}", "")
    text = re.sub(r"[^a-z0-9 ]", " ", text)
    stop = {"a", "an", "the", "for", "of", "and", "with", "via", "to", "in", "on", "from", "based"}
    return [w for w in text.split() if w not in stop and len(w) > 1]


bib_t = [(set(norm(t)), re.sub(r"\s+", " ", t)[:160]) for t in raw]
rows = list(csv.DictReader((ROOT / "tables" / "A1_SNOWBALL_NEW_IN_WINDOW_2026-11-22.csv").open(encoding="utf-8")))
print("unique", len(rows), "bib_titles", len(bib_t))
close = 0
for row in rows:
    words = set(norm(row["candidate_title"]))
    best = 0.0
    best_t = ""
    for bib_words, bib_title in bib_t:
        if not words or not bib_words:
            continue
        score = len(words & bib_words) / len(words | bib_words)
        if score > best:
            best = score
            best_t = bib_title
    if best >= 0.55:
        close += 1
        print(f"{best:.2f} | {row['candidate_title']}")
        print(f"   BIB {best_t}")
print("close", close)
