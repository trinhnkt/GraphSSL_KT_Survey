# -*- coding: utf-8 -*-
import json
import urllib.parse
import urllib.request

UA = "GraphSSL-KT-Survey-A1/2026-11-22 (mailto:survey-audit@localhost)"
DOIS = [
    "10.1109/TLT.2024.3386750",
    "10.3390/e27070685",
    "10.1145/3543507.3583255",
    "10.1016/j.neucom.2024.128366",
    "10.1007/978-981-96-0821-8_14",
]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    for doi in DOIS:
        msg = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))["message"]
        title = " ".join(msg.get("title") or [])
        print("=" * 16)
        print(doi)
        print(title)
        print("page", msg.get("page"), "container", " ".join(msg.get("container-title") or []))
        print("alts", msg.get("alternative-id"))
        print("resource", (msg.get("resource") or {}).get("primary"))
        for link in msg.get("link") or []:
            print("link", link.get("content-type"), link.get("URL"))
        oa = get(
            "https://api.openalex.org/works/https://doi.org/"
            + urllib.parse.quote(doi)
            + "?select=open_access,best_oa_location"
        )
        best = oa.get("best_oa_location") or {}
        access = oa.get("open_access") or {}
        print("oa", access.get("oa_status"), access.get("oa_url"))
        print("pdf", best.get("pdf_url"))
        print("landing", best.get("landing_page_url"))


if __name__ == "__main__":
    main()
