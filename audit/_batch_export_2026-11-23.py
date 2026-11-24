# -*- coding: utf-8 -*-
"""One-batch search on 2026-11-23.

Saves arXiv Q-G and Q-S from the official API.
Probes the other fourteen queries without inventing records.
Does not edit the manuscript or the 26 August search log.
"""
import csv
import json
import time
import urllib.parse
import urllib.request
from xml.etree import ElementTree

OUT_DIR = r"D:\TRINH\GraphSSL_KT_Survey\03_search\exports"
LOG = r"D:\TRINH\GraphSSL_KT_Survey\03_search\search_log_batch_2026-11-23.csv"
UA = "GraphSSL-KT-Survey-batch/2026-11-23 (mailto:survey-audit@localhost)"
CUTOFF = "submittedDate:[201501010000 TO 202611232359]"
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
    "arxiv": "http://arxiv.org/schemas/atom",
}

QUERIES = {
    "SRCH_013": 'ti:"knowledge tracing" OR ti:"student knowledge tracing" OR (abs:"knowledge tracing" AND (abs:graph OR abs:GNN OR abs:GCN OR abs:GAT))',
    "SRCH_014": 'ti:"knowledge tracing" OR ti:"student knowledge tracing" OR (abs:"knowledge tracing" AND (abs:"self-supervised" OR abs:contrastive))',
}
FILES = {
    "SRCH_013": "arxiv_qg_20261123",
    "SRCH_014": "arxiv_qs_20261123",
}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as resp:
        return resp.status, resp.read()


def arxiv_pages(search_query):
    pages = []
    start = 0
    total = None
    while total is None or start < total:
        params = {
            "search_query": f"({search_query}) AND {CUTOFF}",
            "start": start,
            "max_results": 100,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
        status, body = fetch(url)
        root = ElementTree.fromstring(body)
        if total is None:
            total = int(root.findtext("opensearch:totalResults", default="0", namespaces=NS))
        pages.append(body)
        got = len(root.findall("atom:entry", NS))
        start += got
        if got == 0:
            break
        time.sleep(3)
    return total, pages


def entry_rows(xml_bytes):
    root = ElementTree.fromstring(xml_bytes)
    rows = []
    for entry in root.findall("atom:entry", NS):
        arxiv_id = (entry.findtext("atom:id", default="", namespaces=NS) or "").rsplit("/abs/", 1)[-1]
        doi = ""
        for link in entry.findall("atom:link", NS):
            if link.get("title") == "doi":
                doi = link.get("href") or ""
        rows.append({
            "arxiv_id": arxiv_id,
            "title": " ".join((entry.findtext("atom:title", default="", namespaces=NS) or "").split()),
            "published": entry.findtext("atom:published", default="", namespaces=NS),
            "updated": entry.findtext("atom:updated", default="", namespaces=NS),
            "doi": doi,
            "primary_category": (entry.find("arxiv:primary_category", NS).get("term") if entry.find("arxiv:primary_category", NS) is not None else ""),
        })
    return rows


def save_arxiv(search_id):
    total, pages = arxiv_pages(QUERIES[search_id])
    stem = FILES[search_id]
    xml_path = OUT_DIR + "\\" + stem + ".xml"
    csv_path = OUT_DIR + "\\" + stem + ".csv"
    with open(xml_path, "wb") as fh:
        fh.write(b"<?xml version='1.0' encoding='UTF-8'?>\n")
        fh.write(b"<batch>\n")
        for page in pages:
            fh.write(page)
            fh.write(b"\n")
        fh.write(b"</batch>\n")
    rows = []
    for page in pages:
        rows.extend(entry_rows(page))
    with open(csv_path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["arxiv_id", "title", "published", "updated", "doi", "primary_category"])
        writer.writeheader()
        writer.writerows(rows)
    return total, len(rows), stem + ".xml"


def probe(url):
    try:
        status, body = fetch(url)
        return status, len(body)
    except Exception as exc:
        return type(exc).__name__ + " " + str(exc), 0


def main():
    saved = {}
    for search_id in ("SRCH_013", "SRCH_014"):
        total, nrows, filename = save_arxiv(search_id)
        saved[search_id] = (total, nrows, filename)
        print(search_id, "api_total", total, "rows", nrows)
        time.sleep(3)
    probes = {
        "SRCH_001": probe("https://dl.acm.org/action/doSearch?AllField=knowledge+tracing"),
        "SRCH_009": probe("https://api.elsevier.com/content/search/scopus?query=TITLE-ABS-KEY(knowledge%20tracing)&count=1"),
        "SRCH_005": probe("https://api.elsevier.com/content/search/sciencedirect?query=title(knowledge%20tracing)&count=1"),
        "SRCH_007": probe("https://api.springernature.com/meta/v2/json?q=name:knowledge&p=1"),
        "SRCH_003": probe("https://ieeexplore.ieee.org/rest/search"),
        "SRCH_011": probe("https://www.webofscience.com/api/wosnx/"),
    }
    print("PROBES")
    print(json.dumps({k: v[0] if isinstance(v, tuple) else v for k, v in probes.items()}, ensure_ascii=False))
    blocked = "NOT_EXPORTED. No library API key in this session. An unauthenticated request does not return the record file."
    rows = [
        ["SRCH_001", "ACM_DL", "Q-G", "2015-01-01", "2026-11-23", "", "", "NOT_EXPORTED", blocked + " Probe: " + str(probes["SRCH_001"][0])],
        ["SRCH_002", "ACM_DL", "Q-S", "2015-01-01", "2026-11-23", "", "", "NOT_EXPORTED", blocked],
        ["SRCH_003", "IEEE_Xplore", "Q-G", "2015-01-01", "2026-11-23", "", "", "NOT_EXPORTED", blocked + " Probe: " + str(probes["SRCH_003"][0])],
        ["SRCH_004", "IEEE_Xplore", "Q-S", "2015-01-01", "2026-11-23", "", "", "NOT_EXPORTED", blocked],
        ["SRCH_005", "ScienceDirect", "Q-G", "2015-01-01", "2026-11-23", "", "", "NOT_EXPORTED", blocked + " Probe: " + str(probes["SRCH_005"][0])],
        ["SRCH_006", "ScienceDirect", "Q-S", "2015-01-01", "2026-11-23", "", "", "NOT_EXPORTED", blocked],
        ["SRCH_007", "SpringerLink", "Q-G", "2015-01-01", "2026-11-23", "", "", "NOT_EXPORTED", blocked + " Probe: " + str(probes["SRCH_007"][0])],
        ["SRCH_008", "SpringerLink", "Q-S", "2015-01-01", "2026-11-23", "", "", "NOT_EXPORTED", blocked],
        ["SRCH_009", "Scopus", "Q-G", "2015-01-01", "2026-11-23", "", "", "NOT_EXPORTED", blocked + " Probe: " + str(probes["SRCH_009"][0])],
        ["SRCH_010", "Scopus", "Q-S", "2015-01-01", "2026-11-23", "", "", "NOT_EXPORTED", blocked],
        ["SRCH_011", "WebOfScience", "Q-G", "2015-01-01", "2026-11-23", "", "", "NOT_EXPORTED", blocked + " Probe: " + str(probes["SRCH_011"][0])],
        ["SRCH_012", "WebOfScience", "Q-S", "2015-01-01", "2026-11-23", "", "", "NOT_EXPORTED", blocked],
        ["SRCH_013", "arXiv", "Q-G", "2015-01-01", "2026-11-23", saved["SRCH_013"][1], saved["SRCH_013"][2], "EXPORTED", "Official export.arxiv.org API. API totalResults=" + str(saved["SRCH_013"][0]) + ". Cutoff is submittedDate through 2026-11-23. This file does not replace arxiv_qg_20260826.csv."],
        ["SRCH_014", "arXiv", "Q-S", "2015-01-01", "2026-11-23", saved["SRCH_014"][1], saved["SRCH_014"][2], "EXPORTED", "Official export.arxiv.org API. API totalResults=" + str(saved["SRCH_014"][0]) + ". Cutoff is submittedDate through 2026-11-23. This file does not replace arxiv_qs_20260826.csv."],
        ["SRCH_015", "Scopus", "Q-P", "2015-01-01", "2026-11-23", "", "", "NOT_EXPORTED", blocked],
        ["SRCH_016", "Scopus", "Q-R", "2015-01-01", "2026-11-23", "", "", "NOT_EXPORTED", blocked],
    ]
    with open(LOG, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["search_id", "database", "query_family", "cutoff_start", "cutoff_end", "records_in_saved_file", "saved_filename", "status", "note"])
        writer.writerows(rows)
    print("log", LOG)


if __name__ == "__main__":
    main()
