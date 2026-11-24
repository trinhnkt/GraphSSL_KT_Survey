# -*- coding: utf-8 -*-
"""Read Crossref and OpenAlex for the DGMN DOI. Does not edit the bibliography."""
import json
import urllib.request

DOI = "10.1109/TKDE.2022.3206447"
UA = "GraphSSL-KT-Survey-B11/2026-11-22 (mailto:survey-audit@localhost)"
OUT = r"D:\TRINH\GraphSSL_KT_Survey\audit\_b11_dgmn_2026-11-22.json"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return json.loads(resp.read().decode("utf-8"))


payload = {"doi": DOI}
try:
    cr = get("https://api.crossref.org/works/" + DOI)
    msg = cr.get("message", {})
    payload["crossref"] = {
        "title": (msg.get("title") or [None])[0],
        "container": (msg.get("container-title") or [None])[0],
        "volume": msg.get("volume"),
        "issue": msg.get("issue"),
        "page": msg.get("page"),
        "issued": msg.get("issued"),
        "published-print": msg.get("published-print"),
        "published-online": msg.get("published-online"),
        "type": msg.get("type"),
        "author": [
            " ".join(filter(None, [a.get("given"), a.get("family")]))
            for a in (msg.get("author") or [])
        ],
    }
except Exception as exc:
    payload["crossref_error"] = repr(exc)

try:
    oa = get("https://api.openalex.org/works/https://doi.org/" + DOI)
    loc = (oa.get("primary_location") or {}).get("source") or {}
    payload["openalex"] = {
        "title": oa.get("display_name"),
        "publication_year": oa.get("publication_year"),
        "publication_date": oa.get("publication_date"),
        "biblio": oa.get("biblio"),
        "source": loc.get("display_name"),
        "type": oa.get("type"),
    }
except Exception as exc:
    payload["openalex_error"] = repr(exc)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(payload, fh, ensure_ascii=False, indent=2)
print("wrote", OUT)
