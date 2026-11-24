# -*- coding: utf-8 -*-
import json
import urllib.parse
import urllib.request
from pathlib import Path

UA = "GraphSSL-KT-Survey-A1/2026-11-22 (mailto:survey-audit@localhost)"
TITLES = [
    "CoSKT: A Collaborative Self-Supervised Learning Method for Knowledge Tracing",
    "Heterogeneous graph knowledge tracing with novel contrastive view and meta-path contexts",
    "Dynamic heterogeneous graph contrastive networks for knowledge tracing",
]
DOIS = [
    "10.1109/TLT.2024.3386750",
    "10.1016/j.eswa.2025.128840",
    "10.1016/j.asoc.2024.112194",
]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def main():
    for title in TITLES:
        query = 'ti:"' + title + '"'
        url = "https://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(query) + "&max_results=2"
        raw = get(url).decode("utf-8", "replace")
        print("ARXIV", title[:50], "entries", raw.count("<entry>"))
        start = raw.find("<title>")
        if start >= 0:
            print(raw[start:start + 220].replace("\n", " ")[:220])
    for doi in DOIS:
        url = "https://api.unpaywall.org/v2/" + urllib.parse.quote(doi) + "?email=survey-audit@localhost"
        try:
            data = json.loads(get(url).decode("utf-8"))
        except Exception as exc:
            print("UNPAY", doi, exc)
            continue
        loc = data.get("best_oa_location") or {}
        print("UNPAY", doi, data.get("is_oa"), loc.get("url_for_pdf") or loc.get("url"), data.get("oa_status"))


if __name__ == "__main__":
    main()
