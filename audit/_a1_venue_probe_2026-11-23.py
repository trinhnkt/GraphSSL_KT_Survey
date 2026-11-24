# -*- coding: utf-8 -*-
"""Dates, abstracts, and November-export hits for venue-probe VX01–VX10.
Does not edit the manuscript, the bibliography, or any locked file.
"""
import csv
import json
import os
import urllib.parse
import urllib.request

UA = "GraphSSL-KT-Survey-A1/2026-11-23 (mailto:survey-audit@localhost)"
OUT = r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_evidence\venue_probe_2026-11-23.json"
EXPORTS = r"D:\TRINH\GraphSSL_KT_Survey\03_search\exports"

CANDIDATES = [
    {
        "id": "VX01",
        "doi": None,
        "title": "Automatical Graph-based Knowledge Tracing",
        "needles": ["automatical graph-based knowledge tracing", "edm-posters.87"],
    },
    {
        "id": "VX02",
        "doi": "10.1145/3657604.3664683",
        "title": "Enhancing Knowledge Tracing Efficacy with Expert-defined Graphs",
        "needles": ["expert-defined graphs", "10.1145/3657604.3664683"],
    },
    {
        "id": "VX03",
        "doi": "10.1145/3637528.3671853",
        "title": "Graph-based Reasonable Knowledge Tracing",
        "needles": ["reasonable knowledge tracing", "10.1145/3637528.3671853", "grkt"],
    },
    {
        "id": "VX04",
        "doi": "10.1145/3638055",
        "title": "Pre-training Question Embeddings for Improving Knowledge Tracing with Self-supervised Bi-graph Co-contrastive Learning",
        "needles": ["bi-graph co-contrastive", "10.1145/3638055", "bico"],
    },
    {
        "id": "VX05",
        "doi": "10.1016/j.eswa.2025.128840",
        "title": "Heterogeneous graph knowledge tracing with novel contrastive view and meta-path contexts",
        "needles": ["10.1016/j.eswa.2025.128840", "meta-path contexts"],
    },
    {
        "id": "VX06",
        "doi": "10.1109/iceit64364.2025.10976145",
        "title": "Graph Contrast Learning Fused Question Features Based Knowledge Tracing",
        "needles": ["10.1109/iceit64364.2025.10976145", "fused question features"],
    },
    {
        "id": "VX07",
        "doi": "10.24963/ijcai.2025/823",
        "title": "Contrastive cross-course knowledge tracing via concept graph guided knowledge transfer",
        "needles": ["10.24963/ijcai.2025/823", "cross-course knowledge tracing"],
    },
    {
        "id": "VX08",
        "doi": "10.1109/access.2025.3542870",
        "title": "Dual-Channel Knowledge Tracing With Self-Supervised Contrastive and Directed Interaction Learning",
        "needles": ["10.1109/access.2025.3542870", "directed interaction learning"],
    },
    {
        "id": "VX09",
        "doi": "10.1016/j.neucom.2026.133837",
        "title": "Self-supervised contrastive learning with multi-dimensional graph structures for knowledge tracing",
        "needles": ["10.1016/j.neucom.2026.133837", "multi-dimensional graph structures"],
    },
    {
        "id": "VX10",
        "doi": None,
        "title": "Knowledge Tracing Enhanced by Graph Convolutional Networks with Self-Supervised Learning",
        "needles": ["enhanced by graph convolutional networks with self-supervised", "kgs-kt"],
    },
]


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def abstract_from_inverted(inv):
    if not inv:
        return None
    pairs = []
    for word, positions in inv.items():
        for pos in positions:
            pairs.append((pos, word))
    pairs.sort()
    return " ".join(word for _, word in pairs)


def date_parts(block):
    if not block:
        return None
    parts = (block.get("date-parts") or [None])[0]
    return parts


def crossref_record(doi):
    msg = fetch_json("https://api.crossref.org/works/" + urllib.parse.quote(doi))["message"]
    return {
        "title": (msg.get("title") or [None])[0],
        "container": (msg.get("container-title") or [None])[0],
        "author": [
            " ".join(x for x in [a.get("given"), a.get("family")] if x)
            for a in (msg.get("author") or [])
        ],
        "issued": date_parts(msg.get("issued")),
        "published_print": date_parts(msg.get("published-print")),
        "published_online": date_parts(msg.get("published-online")),
        "created": date_parts(msg.get("created")),
        "page": msg.get("page"),
        "volume": msg.get("volume"),
        "issue": msg.get("issue"),
        "publisher": msg.get("publisher"),
        "type": msg.get("type"),
        "abstract": msg.get("abstract"),
    }


def openalex_by_doi(doi):
    msg = fetch_json("https://api.openalex.org/works/https://doi.org/" + urllib.parse.quote(doi))
    return {
        "id": msg.get("id"),
        "display_name": msg.get("display_name"),
        "publication_date": msg.get("publication_date"),
        "type": msg.get("type"),
        "abstract": abstract_from_inverted(msg.get("abstract_inverted_index")),
    }


def openalex_by_title(title):
    url = "https://api.openalex.org/works?search=" + urllib.parse.quote(title) + "&per-page=3"
    msg = fetch_json(url)
    rows = []
    for item in msg.get("results") or []:
        rows.append({
            "id": item.get("id"),
            "display_name": item.get("display_name"),
            "publication_date": item.get("publication_date"),
            "doi": item.get("doi"),
            "type": item.get("type"),
            "abstract": abstract_from_inverted(item.get("abstract_inverted_index")),
        })
    return rows


def export_hits():
    hits = {c["id"]: [] for c in CANDIDATES}
    for name in sorted(os.listdir(EXPORTS)):
        path = os.path.join(EXPORTS, name)
        if not os.path.isfile(path):
            continue
        raw = open(path, "r", encoding="utf-8", errors="replace").read().lower()
        for cand in CANDIDATES:
            for needle in cand["needles"]:
                if needle.lower() in raw:
                    hits[cand["id"]].append({"file": name, "needle": needle})
                    break
    return hits


def main():
    records = []
    for cand in CANDIDATES:
        row = {"id": cand["id"], "query_title": cand["title"], "doi": cand["doi"]}
        if cand["doi"]:
            try:
                row["crossref"] = crossref_record(cand["doi"])
            except Exception as exc:
                row["crossref_error"] = str(exc)
            try:
                row["openalex"] = openalex_by_doi(cand["doi"])
            except Exception as exc:
                row["openalex_error"] = str(exc)
        else:
            try:
                row["openalex_search"] = openalex_by_title(cand["title"])
            except Exception as exc:
                row["openalex_error"] = str(exc)
        records.append(row)
    payload = {"candidates": records, "november_export_hits": export_hits()}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
    for row in records:
        cr = row.get("crossref") or {}
        oa = row.get("openalex") or {}
        issued = cr.get("issued") or oa.get("publication_date")
        print(row["id"], issued, (cr.get("title") or oa.get("display_name") or "")[:90])
    print("--- hits ---")
    for key, vals in payload["november_export_hits"].items():
        print(key, [(v["file"], v["needle"]) for v in vals])


if __name__ == "__main__":
    main()
