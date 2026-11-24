# -*- coding: utf-8 -*-
"""Crossref record for the bipartite chapter. Does not edit the bibliography."""
import json
import urllib.request

DOI = "10.1007/978-981-96-0821-8_14"
UA = "GraphSSL-KT-Survey-A1/2026-11-23 (mailto:survey-audit@localhost)"
url = "https://api.crossref.org/works/" + DOI
req = urllib.request.Request(url, headers={"User-Agent": UA})
with urllib.request.urlopen(req, timeout=45) as resp:
    msg = json.loads(resp.read().decode("utf-8"))["message"]
keep = {
    "title": (msg.get("title") or [None])[0],
    "container": (msg.get("container-title") or [None])[0],
    "author": [
        " ".join(x for x in [a.get("given"), a.get("family")] if x)
        for a in (msg.get("author") or [])
    ],
    "issued": msg.get("issued"),
    "published-print": msg.get("published-print"),
    "published-online": msg.get("published-online"),
    "page": msg.get("page"),
    "volume": msg.get("volume"),
    "publisher": msg.get("publisher"),
    "type": msg.get("type"),
}
out = r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\BipartiteKT_crossref_2026-11-23.json"
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(keep, fh, ensure_ascii=False, indent=2)
print(json.dumps(keep, ensure_ascii=False, indent=2))
