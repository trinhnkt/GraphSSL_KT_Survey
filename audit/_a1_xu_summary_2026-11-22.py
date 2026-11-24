# -*- coding: utf-8 -*-
"""Append the Xu survey snowball and write a deduplicated in-window list."""
import csv
import json
import time
from collections import defaultdict
from pathlib import Path

import importlib.util

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
spec = importlib.util.spec_from_file_location(
    "a1", ROOT / "audit" / "_a1_open_coverage_2026-11-22.py"
)
a1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a1)

SNOW = ROOT / "tables" / "A1_SNOWBALL_OPENALEX_2026-11-22.csv"
UNIQUE = ROOT / "tables" / "A1_SNOWBALL_NEW_IN_WINDOW_2026-11-22.csv"
XU_ID = "W7169714148"
XU_DOI = "10.5281/zenodo.21443287"


def main():
    known = a1.bib_dois()
    candidate_dois = {doi.lower() for _, _, doi in a1.CANDIDATES}
    work = a1.get(
        "https://api.openalex.org/works/"
        + XU_ID
        + "?select=id,display_name,doi,publication_date,referenced_works,cited_by_count"
    )
    (a1.OUT_DIR / "XU.json").write_text(json.dumps(work, ensure_ascii=False)[:2000000], encoding="utf-8")
    refs = a1.batch_works(work.get("referenced_works") or [])
    cites = a1.citing_works(work["id"])
    extra = []
    for direction, items in (("BACKWARD", refs.values()), ("FORWARD", cites)):
        for item in items:
            title = item.get("display_name") or ""
            if not a1.keep(title):
                continue
            cdoi = a1.norm_doi(item.get("doi"))
            date = item.get("publication_date") or ""
            extra.append({
                "source_id": "XU2026",
                "source_name": "Xu survey",
                "direction": direction,
                "candidate_title": title,
                "candidate_doi": cdoi,
                "publication_date": date,
                "in_search_window": a1.window(date),
                "already_in_37": "YES" if cdoi and cdoi in known else "NO",
                "named_a1_candidate": "YES" if cdoi in candidate_dois else "NO",
                "screened": "NO",
                "decision": "NOT_ADDED",
                "note": "OpenAlex 2026-11-22; Xu work " + XU_ID + "; not the 2026-08-26 search",
            })
    print("xu_cited_by", work.get("cited_by_count"), "xu_refs", len(work.get("referenced_works") or []))
    print("xu_kept_rows", len(extra), "xu_forward", sum(1 for r in extra if r["direction"] == "FORWARD"))

    fields = [
        "source_id", "source_name", "direction", "candidate_title", "candidate_doi",
        "publication_date", "in_search_window", "already_in_37", "named_a1_candidate",
        "screened", "decision", "note",
    ]
    with SNOW.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writerows(extra)

    with SNOW.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    grouped = defaultdict(list)
    for row in rows:
        if row.get("already_in_37") != "NO" or row.get("in_search_window") != "YES":
            continue
        key = (row.get("candidate_doi") or "").lower() or ("TITLE:" + row.get("candidate_title", "").lower())
        grouped[key].append(row)

    unique_rows = []
    for key, items in grouped.items():
        dates = sorted(d for d in (r["publication_date"] for r in items) if d)
        unique_rows.append({
            "candidate_doi": items[0]["candidate_doi"],
            "candidate_title": items[0]["candidate_title"],
            "publication_date": dates[0] if dates else "",
            "n_links": len(items),
            "sources": ";".join(sorted({r["source_id"] for r in items})),
            "directions": ";".join(sorted({r["direction"] for r in items})),
            "named_a1_candidate": "YES" if any(r["named_a1_candidate"] == "YES" for r in items) else "NO",
            "already_in_37": "NO",
            "screened": "NO",
            "decision": "NOT_ADDED",
        })
    unique_rows.sort(key=lambda r: (r["named_a1_candidate"] != "YES", r["candidate_title"].lower()))
    with UNIQUE.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(unique_rows[0].keys()) if unique_rows else ["candidate_doi"])
        writer.writeheader()
        writer.writerows(unique_rows)
    named = [r for r in unique_rows if r["named_a1_candidate"] == "YES"]
    print("snow_rows", len(rows))
    print("unique_new_in_window", len(unique_rows))
    print("named_recovered", len(named))
    for row in named:
        print("NAMED", row["candidate_doi"], row["sources"], row["candidate_title"])
    ssl_hits = [r for r in unique_rows if r["named_a1_candidate"] == "NO" and any(
        token in r["candidate_title"].lower()
        for token in ("contrastive", "self-supervised", "self supervised", "pretext")
    )]
    print("extra_ssl_title_hits", len(ssl_hits))
    for row in ssl_hits:
        print("SSL", row["publication_date"], row["candidate_doi"], row["candidate_title"])


if __name__ == "__main__":
    main()
