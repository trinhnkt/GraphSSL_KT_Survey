"""B11: resolve each bibliography DOI against the Crossref API. No invented metadata."""
import csv, json, re, time, urllib.request, urllib.parse
from pathlib import Path

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
bib = (ROOT / "12_manuscript/TLT/references.bib").read_text(encoding="utf-8")
# split entries
parts = re.split(r"\n(?=@)", bib)
entries = []
for p in parts:
    m = re.match(r"@(\w+)\{([^,]+),", p)
    if not m:
        continue
    def field(name):
        fm = re.search(rf"\n\s*{name}\s*=\s*\{{", p)
        if not fm:
            fm = re.search(rf"\n\s*{name}\s*=\s*", p)
            if not fm:
                return ""
        # brace-balanced or quoted
        i = p.find("{", fm.end() - 1)
        if i < 0:
            return ""
        depth = 0
        for j in range(i, len(p)):
            if p[j] == "{":
                depth += 1
            elif p[j] == "}":
                depth -= 1
                if depth == 0:
                    return re.sub(r"\s+", " ", p[i + 1:j]).strip()
        return ""
    entries.append({
        "key": m.group(2),
        "type": m.group(1),
        "title": field("title"),
        "author": field("author"),
        "year": field("year"),
        "doi": field("doi"),
        "journal": field("journal") or field("booktitle"),
        "volume": field("volume"),
        "number": field("number"),
        "pages": field("pages"),
    })

# printed order from the anonymous bbl
bbl = (ROOT / "12_manuscript/TLT/main_tlt_anonymous.bbl").read_text(encoding="utf-8")
order = re.findall(r"\\bibitem\{([^}]+)\}", bbl)
rank = {k: i + 1 for i, k in enumerate(order)}

def norm(s):
    s = re.sub(r"[{}\\]", "", s or "")
    s = s.replace("exttwosuperior", "2").replace("textsuperscript", "")
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s

out_rows = []
raw_dir = ROOT / "audit" / "_b11_crossref"
raw_dir.mkdir(exist_ok=True)
for e in entries:
    rec = {
        "ref_no": rank.get(e["key"], ""),
        "bib_key": e["key"],
        "title": e["title"],
        "doi": e["doi"],
        "doi_resolves": "",
        "official_publisher": "",
        "authors_match": "",
        "title_match": "",
        "year_match": "",
        "venue_match": "",
        "volume_issue_match": "",
        "pages_match": "",
        "final_status": "",
        "notes": "",
        "official_title": "",
        "official_year": "",
        "official_container": "",
        "official_volume": "",
        "official_issue": "",
        "official_page": "",
    }
    if not e["doi"]:
        rec["doi_resolves"] = "NO_DOI"
        rec["final_status"] = "NEEDS_EXTERNAL_VERIFICATION"
        rec["notes"] = "No DOI in references.bib; not sent to Crossref."
        out_rows.append(rec)
        continue
    url = "https://api.crossref.org/works/" + urllib.parse.quote(e["doi"])
    req = urllib.request.Request(url, headers={"User-Agent": "GraphSSL-KT-Survey-B11 (mailto:local)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        msg = data["message"]
        (raw_dir / (e["key"] + ".json")).write_text(json.dumps({
            "title": msg.get("title"),
            "author": msg.get("author"),
            "issued": msg.get("issued"),
            "container-title": msg.get("container-title"),
            "volume": msg.get("volume"),
            "issue": msg.get("issue"),
            "page": msg.get("page"),
            "publisher": msg.get("publisher"),
            "DOI": msg.get("DOI"),
            "type": msg.get("type"),
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        ot = (msg.get("title") or [""])[0]
        rec["official_title"] = ot
        rec["official_publisher"] = msg.get("publisher") or ""
        rec["official_container"] = (msg.get("container-title") or [""])[0]
        parts_y = (msg.get("issued") or {}).get("date-parts") or [[""]]
        rec["official_year"] = str(parts_y[0][0])
        rec["official_volume"] = msg.get("volume") or ""
        rec["official_issue"] = msg.get("issue") or ""
        rec["official_page"] = msg.get("page") or ""
        rec["doi_resolves"] = "YES"
        rec["title_match"] = "YES" if norm(ot) == norm(e["title"]).split(":")[0][:40] and norm(ot)[:40] == norm(e["title"])[:40] else ("YES" if norm(ot) == norm(e["title"]) else "CHECK")
        # tighter title compare
        def squash(s):
            return re.sub(r"[^a-z0-9]", "", norm(s))
        rec["title_match"] = "YES" if squash(ot) == squash(e["title"]) else "NO"
        rec["year_match"] = "YES" if rec["official_year"] == e["year"] else "NO"
        # authors: compare last names
        bib_last = [a.strip().split()[-1].lower() for a in e["author"].replace(" and ", "|").split("|") if a.strip()]
        off_last = [((a.get("family") or "") ).lower() for a in (msg.get("author") or [])]
        rec["authors_match"] = "YES" if bib_last == off_last else ("YES_PREFIX" if off_last and bib_last[:len(off_last)] == off_last else "NO")
        # venue: loose containment of a distinctive token
        rec["venue_match"] = "YES" if squash(rec["official_container"]) and squash(rec["official_container"])[:12] in squash(e["journal"]) or squash(e["journal"])[:12] in squash(rec["official_container"]) else "CHECK"
        vol_ok = (not e["volume"]) or e["volume"] == rec["official_volume"]
        iss_ok = (not e["number"]) or e["number"] == rec["official_issue"] or rec["official_issue"] == ""
        rec["volume_issue_match"] = "YES" if vol_ok and iss_ok else "NO"
        pg = e["pages"].replace("--", "-").replace(" ", "")
        op = (rec["official_page"] or "").replace(" ", "")
        rec["pages_match"] = "YES" if (not pg or pg == op or op == "") else "NO"
        flags = [rec[k] for k in ("title_match", "year_match", "authors_match", "volume_issue_match", "pages_match")]
        rec["final_status"] = "PASS" if all(x in ("YES", "YES_PREFIX") for x in flags) and rec["venue_match"] == "YES" else "MISMATCH"
        if rec["title_match"] == "NO":
            rec["notes"] = "Official title: " + ot[:180]
    except Exception as ex:
        rec["doi_resolves"] = "NO"
        rec["final_status"] = "NEEDS_EXTERNAL_VERIFICATION"
        rec["notes"] = type(ex).__name__ + ": " + str(ex)[:200]
    out_rows.append(rec)
    time.sleep(0.2)

out_rows.sort(key=lambda r: (r["ref_no"] == "", r["ref_no"] or 999))
dest = ROOT / "tables" / "B11_REFERENCE_VERIFICATION.csv"
with dest.open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
    w.writeheader()
    w.writerows(out_rows)
from collections import Counter
print(Counter(r["final_status"] for r in out_rows))
print("mismatches:")
for r in out_rows:
    if r["final_status"] != "PASS":
        print(r["ref_no"], r["bib_key"], r["final_status"], r["doi_resolves"], r["title_match"], r["year_match"], r["authors_match"], r["venue_match"], r["volume_issue_match"], r["pages_match"], r["notes"][:120])
