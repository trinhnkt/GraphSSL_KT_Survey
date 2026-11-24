# -*- coding: utf-8 -*-
import json
import urllib.parse
import urllib.request

UA = "GraphSSL-KT-Survey-A1/2026-11-22 (mailto:survey-audit@localhost)"
TITLES = [
    "Heterogeneous graph knowledge tracing with novel contrastive view and meta-path contexts",
    "Dynamic heterogeneous graph contrastive networks for knowledge tracing",
    "CoSKT: A Collaborative Self-Supervised Learning Method for Knowledge Tracing",
]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    for title in TITLES:
        url = (
            "https://api.openalex.org/works?search="
            + urllib.parse.quote(title)
            + "&per-page=5&select=id,display_name,doi,publication_date,open_access,best_oa_location"
        )
        data = get(url)
        print("=" * 12, title[:48])
        for work in data.get("results") or []:
            oa = work.get("open_access") or {}
            best = work.get("best_oa_location") or {}
            print(work.get("publication_date"), work.get("doi"), oa.get("oa_status"), best.get("pdf_url") or best.get("landing_page_url"))
            print(" ", work.get("display_name"))


if __name__ == "__main__":
    main()
