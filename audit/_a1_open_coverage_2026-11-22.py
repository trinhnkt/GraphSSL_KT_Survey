# -*- coding: utf-8 -*-
"""Dated open-source coverage check for A1. Does not edit the manuscript or counts."""
import csv
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
OUT_DIR = ROOT / "audit" / "_a1_2026-11-22"
OUT_DIR.mkdir(parents=True, exist_ok=True)
BIB = ROOT / "12_manuscript" / "TLT" / "references.bib"
UA = "GraphSSL-KT-Survey-A1/2026-11-22 (mailto:survey-audit@localhost)"

CANDIDATES = [
    ("A1-C01", "DECKT", "10.3390/e27070685"),
    ("A1-C02", "DTransformer", "10.1145/3543507.3583255"),
    ("A1-C03", "SP-CLKT", "10.1016/j.neucom.2024.128366"),
    ("A1-C04", "Han2024", "10.1016/j.asoc.2024.112194"),
    ("A1-C05", "HCMKT", "10.1016/j.eswa.2025.128840"),
    ("A1-C06", "BipartiteCL", "10.1007/978-981-96-0821-8_14"),
    ("A1-C07", "CoSKT", "10.1109/TLT.2024.3386750"),
]

SSL = [
    ("KT011", "Bi-CLKT", "10.1016/j.knosys.2022.108274"),
    ("KT026", "PEBG", "10.24963/ijcai.2020/219"),
    ("KT039", "CL4KT", "10.1145/3485447.3512105"),
    ("KT042", "S2-HHN", "10.1016/j.ins.2022.12.075"),
    ("KT043", "3V-CLKT", "10.1109/TCE.2023.3293953"),
    ("KT047", "DC-SSL", "10.1016/j.eswa.2023.120212"),
    ("KT050", "GraphCA", "10.1109/JAS.2023.123678"),
    ("KT066", "HyperKT", "10.1109/TNNLS.2024.3386810"),
    ("KT068", "HKT", "10.1016/j.ipm.2025.104206"),
]

KT_RE = re.compile(r"knowledge[\s-]*tracing", re.I)
FOCUS_RE = re.compile(
    r"graph|contrastive|self[\s-]*supervised|pretext|ssl|hypergraph|bipartite",
    re.I,
)


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def window(date_str):
    if not date_str:
        return "UNKNOWN"
    if re.fullmatch(r"\d{4}", date_str):
        year = int(date_str)
        if year < 2015 or year > 2026:
            return "NO"
        if year == 2026:
            return "YEAR_ONLY_2026"
        return "YES"
    if date_str < "2015-01-01":
        return "NO"
    if date_str > "2026-07-31":
        return "NO"
    return "YES"


def bib_dois():
    text = BIB.read_text(encoding="utf-8")
    return {m.group(1).lower() for m in re.finditer(r"doi\s*=\s*\{([^}]+)\}", text, re.I)}


def crossref_one(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    msg = get(url)["message"]
    issued = msg.get("issued", {}).get("date-parts", [[]])[0]
    date = "-".join(f"{part:02d}" if i else str(part) for i, part in enumerate(issued)) if issued else ""
    title = " ".join(msg.get("title") or [])
    container = " ".join(msg.get("container-title") or [])
    return {
        "crossref_title": title,
        "crossref_container": container,
        "crossref_date": date,
        "crossref_type": msg.get("type", ""),
        "in_search_window": window(date),
    }


def openalex_by_doi(doi):
    url = (
        "https://api.openalex.org/works/https://doi.org/"
        + urllib.parse.quote(doi)
        + "?select=id,display_name,referenced_works,cited_by_count,publication_date"
    )
    try:
        return get(url)
    except Exception as exc:
        return {"error": str(exc)}


def batch_works(ids):
    found = {}
    short = []
    for item in ids:
        if not item:
            continue
        short.append(str(item).rstrip("/").split("/")[-1])
    for i in range(0, len(short), 50):
        chunk = short[i:i + 50]
        filt = "openalex_id:" + "|".join(chunk)
        url = (
            "https://api.openalex.org/works?filter="
            + urllib.parse.quote(filt)
            + "&per-page=50&select=id,display_name,doi,publication_date,type"
        )
        data = get(url)
        for work in data.get("results", []):
            found[work["id"]] = work
        time.sleep(0.2)
    return found


def citing_works(openalex_id):
    short = openalex_id.rstrip("/").split("/")[-1]
    rows = []
    for page in range(1, 6):
        url = (
            "https://api.openalex.org/works?filter="
            + urllib.parse.quote(f"cites:{short}")
            + f"&per-page=100&page={page}&select=id,display_name,doi,publication_date"
        )
        data = get(url)
        batch = data.get("results") or []
        rows.extend(batch)
        time.sleep(0.25)
        if len(batch) < 100:
            break
    return rows


def keep(title):
    return bool(title and KT_RE.search(title) and FOCUS_RE.search(title))


def norm_doi(doi):
    if not doi:
        return ""
    return doi.lower().replace("https://doi.org/", "").strip()


def main():
    known = bib_dois()
    candidate_dois = {doi.lower() for _, _, doi in CANDIDATES}
    coverage = []
    for cid, name, doi in CANDIDATES:
        row = {"candidate_id": cid, "short_name": name, "doi": doi, "checked_on": "2026-11-22"}
        try:
            row.update(crossref_one(doi))
        except Exception as exc:
            row["crossref_error"] = str(exc)
        row["present_in_original_2017"] = "NEEDS_EVIDENCE"
        row["added_to_corpus"] = "NO"
        row["decision"] = "NOT_ADDED_NEEDS_HUMAN_SCREEN"
        coverage.append(row)
        time.sleep(0.3)
        print("crossref", cid, row.get("in_search_window"), row.get("crossref_date"))

    cov_path = ROOT / "tables" / "A1_COVERAGE_OPEN_2026-11-22.csv"
    with cov_path.open("w", encoding="utf-8", newline="") as f:
        fields = sorted({k for row in coverage for k in row})
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(coverage)
    print("coverage_written", cov_path)

    snow = []
    for pid, name, doi in SSL:
        print("snowball", pid)
        work = openalex_by_doi(doi)
        (OUT_DIR / f"{pid}.json").write_text(json.dumps(work, ensure_ascii=False)[:2000000], encoding="utf-8")
        if "error" in work and "id" not in work:
            snow.append({
                "source_id": pid, "source_name": name, "direction": "SOURCE",
                "candidate_title": "", "candidate_doi": "", "publication_date": "",
                "in_search_window": "", "already_in_37": "", "named_a1_candidate": "",
                "note": work["error"],
            })
            continue
        ref_ids = work.get("referenced_works") or []
        try:
            refs = batch_works(ref_ids)
            cites = citing_works(work["id"])
        except Exception as exc:
            snow.append({
                "source_id": pid, "source_name": name, "direction": "SOURCE",
                "candidate_title": work.get("display_name") or "", "candidate_doi": doi,
                "publication_date": work.get("publication_date") or "",
                "in_search_window": "", "already_in_37": "", "named_a1_candidate": "",
                "screened": "NO", "decision": "NOT_ADDED",
                "note": "OpenAlex lookup failed: " + str(exc),
            })
            continue
        for direction, items in (("BACKWARD", refs.values()), ("FORWARD", cites)):
            for item in items:
                title = item.get("display_name") or ""
                if not keep(title):
                    continue
                cdoi = norm_doi(item.get("doi"))
                date = item.get("publication_date") or ""
                snow.append({
                    "source_id": pid,
                    "source_name": name,
                    "direction": direction,
                    "candidate_title": title,
                    "candidate_doi": cdoi,
                    "publication_date": date,
                    "in_search_window": window(date),
                    "already_in_37": "YES" if cdoi and cdoi in known else "NO",
                    "named_a1_candidate": "YES" if cdoi in candidate_dois else "NO",
                    "screened": "NO",
                    "decision": "NOT_ADDED",
                    "note": "OpenAlex 2026-11-22; not the 2026-08-26 search",
                })
        time.sleep(0.3)

    snow_path = ROOT / "tables" / "A1_SNOWBALL_OPENALEX_2026-11-22.csv"
    with snow_path.open("w", encoding="utf-8", newline="") as f:
        fields = [
            "source_id", "source_name", "direction", "candidate_title", "candidate_doi",
            "publication_date", "in_search_window", "already_in_37", "named_a1_candidate",
            "screened", "decision", "note",
        ]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(snow)

    new_in_window = [
        row for row in snow
        if row.get("already_in_37") == "NO" and row.get("in_search_window") == "YES"
    ]
    dois = sorted({row["candidate_doi"] for row in new_in_window if row.get("candidate_doi")})
    print("coverage_rows", len(coverage))
    print("snow_rows", len(snow))
    print("new_in_window_rows", len(new_in_window))
    print("new_in_window_dois", len(dois))


if __name__ == "__main__":
    main()
