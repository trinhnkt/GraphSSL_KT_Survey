# -*- coding: utf-8 -*-
"""Confirm two DOIs and whether November hits are own records."""
import json
import urllib.parse
import urllib.request

UA = "GraphSSL-KT-Survey-A1/2026-11-23 (mailto:survey-audit@localhost)"
OUT = r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\venue_probe_checks_2026-11-23.json"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def date_parts(block):
    if not block:
        return None
    return (block.get("date-parts") or [None])[0]


def crossref(doi):
    msg = fetch("https://api.crossref.org/works/" + urllib.parse.quote(doi))["message"]
    return {
        "doi": doi,
        "title": (msg.get("title") or [None])[0],
        "issued": date_parts(msg.get("issued")),
        "published_print": date_parts(msg.get("published-print")),
        "published_online": date_parts(msg.get("published-online")),
        "created": date_parts(msg.get("created")),
        "container": (msg.get("container-title") or [None])[0],
        "page": msg.get("page"),
        "author": [
            " ".join(x for x in [a.get("given"), a.get("family")] if x)
            for a in (msg.get("author") or [])
        ],
    }


def own_lines(path, needles):
    found = []
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for i, line in enumerate(fh, 1):
            low = line.lower()
            if any(n in low for n in needles):
                found.append({"line": i, "text": line.strip()[:400]})
                if len(found) >= 3:
                    break
    return found


def safe_crossref(doi):
    try:
        return crossref(doi)
    except Exception as exc:
        return {"doi": doi, "error": str(exc)}


checks = {
    "VX01_zenodo": safe_crossref("10.5281/zenodo.6853056"),
    "VX10_igi": safe_crossref("10.4018/ijicte.385130"),
    "ieee_grkt": own_lines(
        r"D:\TRINH\GraphSSL_KT_Survey\03_search\exports\ieee_qg_20261114.csv",
        ["grkt"],
    ),
    "arxiv_grkt": own_lines(
        r"D:\TRINH\GraphSSL_KT_Survey\03_search\exports\arxiv_qg_20261114.xml",
        ["reasonable knowledge tracing"],
    ),
    "arxiv_transkt": own_lines(
        r"D:\TRINH\GraphSSL_KT_Survey\03_search\exports\arxiv_qg_20261114.xml",
        ["cross-course knowledge tracing"],
    ),
}
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(checks, fh, ensure_ascii=False, indent=2)
print(json.dumps({k: v if k.endswith(("zenodo", "igi")) else v for k, v in checks.items()}, ensure_ascii=False, indent=2)[:6000])
