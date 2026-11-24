# -*- coding: utf-8 -*-
"""Locate open full texts for the three unscreened A1 candidates."""
import json
import urllib.parse
import urllib.request
from pathlib import Path

UA = "GraphSSL-KT-Survey-A1/2026-11-22 (mailto:survey-audit@localhost)"
DOIS = [
    "10.1016/j.eswa.2025.128840",
    "10.1109/TLT.2024.3386750",
    "10.1016/j.asoc.2024.112194",
]
OUT = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_2026-11-22")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    for doi in DOIS:
        url = (
            "https://api.openalex.org/works/https://doi.org/"
            + urllib.parse.quote(doi)
            + "?select=id,display_name,publication_date,doi,open_access,best_oa_location,locations,authorships"
        )
        work = get(url)
        authors = []
        for row in (work.get("authorships") or [])[:8]:
            authors.append((row.get("author") or {}).get("display_name"))
        slim = {
            "doi": doi,
            "title": work.get("display_name"),
            "date": work.get("publication_date"),
            "authors": authors,
            "open_access": work.get("open_access"),
            "best_oa": work.get("best_oa_location"),
            "locations": [
                {
                    "landing": (loc or {}).get("landing_page_url"),
                    "pdf": (loc or {}).get("pdf_url"),
                    "version": (loc or {}).get("version"),
                    "source": ((loc or {}).get("source") or {}).get("display_name"),
                }
                for loc in (work.get("locations") or [])
            ],
        }
        name = doi.split("/")[-1]
        (OUT / f"oa_{name}.json").write_text(json.dumps(slim, ensure_ascii=False, indent=2), encoding="utf-8")
        print(doi)
        print(" ", slim["date"], slim["title"])
        print(" ", authors)
        print(" ", slim["open_access"])
        for loc in slim["locations"]:
            if loc["pdf"] or loc["landing"]:
                print(" ", loc["version"], loc["source"], loc["pdf"] or loc["landing"])


if __name__ == "__main__":
    main()
