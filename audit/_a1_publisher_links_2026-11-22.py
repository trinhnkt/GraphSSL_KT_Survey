# -*- coding: utf-8 -*-
import json
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
DOIS = [
    "10.1109/TLT.2024.3386750",
    "10.1016/j.eswa.2025.128840",
    "10.1016/j.asoc.2024.112194",
]


def get(url, accept="application/json"):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.geturl(), resp.read()


def main():
    for doi in DOIS:
        msg = json.loads(get("https://api.crossref.org/works/" + urllib.parse.quote(doi))[1])["message"]
        print("=" * 20, doi)
        print("type", msg.get("type"), "page", msg.get("page"), "issued", msg.get("issued"))
        print("author", [a.get("family") for a in (msg.get("author") or [])])
        print("alts", msg.get("alternative-id"))
        for link in msg.get("link") or []:
            print("link", link.get("content-type"), link.get("URL"))
        print("resource", (msg.get("resource") or {}).get("primary"))
        abs_ = msg.get("abstract") or ""
        print("abstract_len", len(abs_))
        if abs_:
            print(abs_[:800])


if __name__ == "__main__":
    main()
