# -*- coding: utf-8 -*-
import json
import urllib.parse
import urllib.request

UA = "GraphSSL-KT-Survey-A1/2026-11-22 (mailto:survey-audit@localhost)"
DOIS = [
    "10.1109/TLT.2024.3386750",
    "10.1016/j.eswa.2025.128840",
    "10.1016/j.asoc.2024.112194",
]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    for doi in DOIS:
        url = (
            "https://api.semanticscholar.org/graph/v1/paper/DOI:"
            + urllib.parse.quote(doi)
            + "?fields=title,year,abstract,openAccessPdf,externalIds,tldr"
        )
        try:
            data = get(url)
        except Exception as exc:
            print("ERR", doi, exc)
            continue
        pdf = (data.get("openAccessPdf") or {}).get("url")
        abstract = data.get("abstract") or ""
        print("=" * 20, doi)
        print(data.get("title"), data.get("year"), pdf)
        print(abstract[:1500])
        print("---TLDR", data.get("tldr"))


if __name__ == "__main__":
    main()
