#!/usr/bin/env python3
"""Live Crossref audit of TLT references.bib (2026-09-15)."""
from __future__ import annotations

import html
import json
import re
import time
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT")
bib_path = ROOT / "references.bib"
tex_path = ROOT / "manuscript_TLT_FORMATTED_v1.3.tex"
out_json = ROOT / "audit" / "REFERENCE_LIVE_CHECK_2026-09-15.json"
out_md = ROOT / "audit" / "REFERENCE_FULL_CHECK_2026-09-15.md"

bib = bib_path.read_text(encoding="utf-8")
tex = tex_path.read_text(encoding="utf-8")

cites: set[str] = set()
for m in re.finditer(r"\\cite[a-zA-Z]*\{([^}]+)\}", tex):
    for k in m.group(1).split(","):
        k = k.strip()
        if k and not k.startswith("IEEEtran"):
            cites.add(k)

entries = []
for m in re.finditer(r"@(\w+)\{([^,]+),\s*(.*?)(?=\n@|\Z)", bib, re.S):
    etype, key, body = m.group(1), m.group(2).strip(), m.group(3)
    if etype.lower() == "ieeetranbstctl":
        continue
    fields = {}
    for fm in re.finditer(
        r"(\w+)\s*=\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", body, re.S
    ):
        fields[fm.group(1).lower()] = re.sub(r"\s+", " ", fm.group(2).strip())
    entries.append(
        {"key": key, "type": etype.lower(), "fields": fields, "cited": key in cites}
    )


def norm_title(t: str) -> str:
    if not t:
        return ""
    t = html.unescape(t)
    t = re.sub(r"<[^>]+>", "", t)
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def family_names_bib(author: str) -> list[str]:
    if not author:
        return []
    fam = []
    for p in [x.strip() for x in author.split(" and ")]:
        if "," in p:
            fam.append(p.split(",")[0].strip().lower())
        else:
            toks = p.split()
            fam.append(toks[-1].lower() if toks else "")
    return fam


KNOWN_CR_TYPOS = {"hunag": "huang"}  # Crossref typo for Zhenya Huang


def fetch_crossref(doi: str) -> dict:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "GraphSSL-KT-Survey/1.0 (mailto:trinhnk@utehy.edu.vn)"
        },
    )
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)["message"]


results = []
for e in entries:
    f = e["fields"]
    doi = f.get("doi", "").strip()
    row = {
        "key": e["key"],
        "type": e["type"],
        "cited": e["cited"],
        "bib_title": f.get("title", ""),
        "bib_year": f.get("year", ""),
        "bib_authors": f.get("author", ""),
        "bib_venue": f.get("journal") or f.get("booktitle") or "",
        "bib_volume": f.get("volume", ""),
        "bib_number": f.get("number", ""),
        "bib_pages": f.get("pages", ""),
        "doi": doi,
        "status": "",
        "issues": [],
        "crossref": None,
    }
    if not doi:
        row["status"] = "NO_DOI"
        row["issues"].append("No DOI — verify via official proceedings URL")
        results.append(row)
        print(e["key"], row["status"])
        continue
    try:
        msg = fetch_crossref(doi)
        time.sleep(0.4)
        issued = (
            msg.get("published-print")
            or msg.get("published-online")
            or msg.get("issued")
            or {}
        )
        year = ""
        if issued.get("date-parts"):
            year = str(issued["date-parts"][0][0] or "")
        row["crossref"] = {
            "title": (msg.get("title") or [""])[0],
            "year": year,
            "container": (msg.get("container-title") or [""])[0],
            "volume": msg.get("volume") or "",
            "issue": msg.get("issue") or "",
            "page": msg.get("page") or "",
            "authors": [
                f"{a.get('given', '')} {a.get('family', '')}".strip()
                for a in (msg.get("author") or [])
            ],
            "type": msg.get("type", ""),
        }
        bt, ct = norm_title(row["bib_title"]), norm_title(row["crossref"]["title"])
        ratio = SequenceMatcher(None, bt, ct).ratio() if bt and ct else 0.0
        if ratio < 0.85:
            row["issues"].append(f"TITLE mismatch (sim={ratio:.2f}): bib vs Crossref")

        bf = family_names_bib(row["bib_authors"])
        cf = [(a.get("family") or "").lower() for a in (msg.get("author") or [])]
        cf_fix = [KNOWN_CR_TYPOS.get(x, x) for x in cf]
        miss = [x for x in bf if x not in cf_fix and KNOWN_CR_TYPOS.get(x, x) not in cf_fix]
        if miss:
            row["issues"].append(f"AUTHOR family in bib not in Crossref: {miss}")

        by, cy = row["bib_year"], row["crossref"]["year"]
        if by and cy and by != cy:
            row["issues"].append(f"YEAR differ: bib={by} Crossref={cy}")

        if (
            row["bib_volume"]
            and row["crossref"]["volume"]
            and row["bib_volume"] != row["crossref"]["volume"]
        ):
            row["issues"].append(
                f"VOLUME differ: bib={row['bib_volume']} Crossref={row['crossref']['volume']}"
            )

        # pages soft check (normalize en-dash)
        bp = row["bib_pages"].replace("--", "-").replace("–", "-")
        cp = (row["crossref"]["page"] or "").replace("--", "-").replace("–", "-")
        if bp and cp and bp != cp and not cp.startswith(bp.split("-")[0]):
            # only flag if clearly different start page
            if bp.split("-")[0] != cp.split("-")[0]:
                row["issues"].append(f"PAGES differ: bib={bp} Crossref={cp}")

        row["status"] = "OK" if not row["issues"] else "CHECK"
    except Exception as ex:  # noqa: BLE001
        row["status"] = "DOI_FAIL"
        row["issues"].append(f"Crossref fetch failed: {ex}")
        time.sleep(0.6)
    results.append(row)
    print(e["key"], row["status"], "; ".join(row["issues"]) if row["issues"] else "")

out_json.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")

ok = sum(1 for r in results if r["status"] == "OK")
chk = sum(1 for r in results if r["status"] == "CHECK")
nod = sum(1 for r in results if r["status"] == "NO_DOI")
fail = sum(1 for r in results if r["status"] == "DOI_FAIL")

lines = [
    "# Full bibliography live check — 2026-09-15",
    "",
    f"Source: `12_manuscript/TLT/references.bib` ({len(entries)} bibliographic works; {len(cites)} cited in manuscript).",
    "Method: Crossref works API for every DOI; no-DOI rows flagged for proceedings verification.",
    "Raw JSON: `REFERENCE_LIVE_CHECK_2026-09-15.json`.",
    "",
    "## Summary",
    "",
    "| Status | Count |",
    "|---|---:|",
    f"| OK (Crossref match) | {ok} |",
    f"| CHECK (difference to review) | {chk} |",
    f"| NO_DOI | {nod} |",
    f"| DOI_FAIL | {fail} |",
    "",
    "## CHECK / FAIL / NO_DOI details",
    "",
]
for r in results:
    if r["status"] in ("CHECK", "DOI_FAIL", "NO_DOI"):
        lines += [
            f"### `{r['key']}` — {r['status']}",
            "",
            f"- Bib title: {r['bib_title']}",
            f"- Bib year / venue: {r['bib_year']} / {r['bib_venue']}",
            f"- Bib authors: {r['bib_authors']}",
            f"- DOI: `{r['doi'] or 'NONE'}`",
        ]
        cr = r.get("crossref")
        if cr:
            lines += [
                f"- Crossref title: {cr['title']}",
                f"- Crossref year / container: {cr['year']} / {cr['container']}",
                f"- Crossref volume/issue/page: {cr['volume']}/{cr['issue']}/{cr['page']}",
                f"- Crossref authors: {'; '.join(cr['authors'][:12])}",
            ]
        for iss in r["issues"]:
            lines.append(f"- Issue: {iss}")
        lines.append("")

lines += [
    "## All cited keys",
    "",
    "| Key | Status | DOI |",
    "|---|---|---|",
]
for r in sorted(results, key=lambda x: x["key"]):
    if not r["cited"]:
        continue
    lines.append(f"| `{r['key']}` | {r['status']} | `{r['doi'] or '—'}` |")

out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("WROTE", out_md)
print("OK", ok, "CHECK", chk, "NO_DOI", nod, "FAIL", fail)
