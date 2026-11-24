# -*- coding: utf-8 -*-
import json
import urllib.parse
import urllib.request
from pathlib import Path

UA = "GraphSSL-KT-Survey-A1/2026-11-22 (mailto:survey-audit@localhost)"
DOIS = [
    "10.1109/TLT.2024.3386750",
    "10.1016/j.eswa.2025.128840",
    "10.1016/j.asoc.2024.112194",
]
OUT = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_2026-11-22")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def invert(index):
    if not index:
        return ""
    pairs = []
    for word, positions in index.items():
        for pos in positions:
            pairs.append((pos, word))
    pairs.sort()
    return " ".join(word for _, word in pairs)


def main():
    for doi in DOIS:
        cross = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))["message"]
        abstract = cross.get("abstract") or ""
        oa = get(
            "https://api.openalex.org/works/https://doi.org/"
            + urllib.parse.quote(doi)
            + "?select=display_name,publication_date,abstract_inverted_index,biblio"
        )
        text = invert(oa.get("abstract_inverted_index"))
        name = doi.split("/")[-1]
        (OUT / f"abs_{name}.txt").write_text(
            "CROSSREF\n" + abstract + "\n\nOPENALEX\n" + text + "\n\nBIBLIO\n" + json.dumps(oa.get("biblio"), ensure_ascii=False),
            encoding="utf-8",
        )
        print(name, "cross_abs", len(abstract), "oa_abs", len(text), oa.get("biblio"))


if __name__ == "__main__":
    main()
