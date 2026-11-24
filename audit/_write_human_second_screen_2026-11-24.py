# -*- coding: utf-8 -*-
"""Build empty human second-screen sheets from deposited rows only.

Does not fill decisions, copy primary labels into the human columns, or compute kappa.
"""
import csv
import math
import random
from pathlib import Path

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
TA_PATH = ROOT / "05_screening" / "title_abstract_screening_v1.0.csv"
FT_PATH = ROOT / "06_fulltext" / "fulltext_screening_v1.0.csv"
DEDUP_PATH = ROOT / "04_deduplication" / "deduplication_audit_v1.0.csv"
VENUE_PATH = ROOT / "03_search" / "venue_extension_candidates_v1.9.csv"
TA_OUT = ROOT / "05_screening" / "HUMAN_SECOND_SCREEN_TITLE_ABSTRACT.csv"
FT_OUT = ROOT / "05_screening" / "HUMAN_SECOND_SCREEN_FULLTEXT.csv"
AUDIT = ROOT / "audit" / "HUMAN_SECOND_SCREENING_REQUIRED.md"

SEED = 20261113
AGGREGATE_ID = "REC_0043-REC_0140"
COLS = [
    "record_id",
    "title",
    "abstract_or_locator",
    "primary_decision_HIDDEN_OR_SEPARATE",
    "human_second_decision",
    "human_exclusion_code",
    "human_screener_name",
    "note",
]


def load(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_rows(path, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for row in rows:
            w.writerow(row)


def human_row(record_id, title, locator):
    return {
        "record_id": record_id,
        "title": title,
        "abstract_or_locator": locator,
        "primary_decision_HIDDEN_OR_SEPARATE": "HIDDEN",
        "human_second_decision": "",
        "human_exclusion_code": "",
        "human_screener_name": "",
        "note": "",
    }


def main():
    ta = load(TA_PATH)
    ft = load(FT_PATH)
    dedup = load(DEDUP_PATH)
    venue = load(VENUE_PATH)
    search_log = load(ROOT / "03_search" / "search_log.csv")
    doi = {r["record_id"]: (r.get("doi") or "").strip() for r in ft}

    aggregate = [r for r in ta if r["record_id"] == AGGREGATE_ID]
    titled = [r for r in ta if r["record_id"] != AGGREGATE_ID]
    assert len(ta) == 43 and len(aggregate) == 1 and len(titled) == 42
    assert aggregate[0]["title"] == "Various candidate titles"

    ids = sorted(r["record_id"] for r in titled)
    k = math.ceil(0.25 * len(ids))
    rng = random.Random(SEED)
    drawn = sorted(rng.sample(ids, k))
    by_id = {r["record_id"]: r for r in titled}

    ta_rows = []
    for rid in drawn:
        rec = by_id[rid]
        locator_doi = doi.get(rid, "")
        if locator_doi:
            locator = "doi:" + locator_doi
        else:
            locator = "no abstract text in the deposited title/abstract row; no DOI on a matching full-text row"
        ta_rows.append(human_row(rid, rec["title"], locator))

    exclusions = [r for r in ft if r["final_tier"] == "EXCLUDE_FULLTEXT"]
    uncertain_ft = [r for r in ft if r["final_tier"] == "UNCERTAIN"]
    assert len(exclusions) == 1 and len(uncertain_ft) == 0
    ex = exclusions[0]
    ft_rows = [
        human_row(
            ex["record_id"],
            ex["title"],
            "doi:" + ex["doi"].strip() if ex["doi"].strip() else "no DOI in the deposited full-text row",
        )
    ]
    write_rows(TA_OUT, ta_rows)
    write_rows(FT_OUT, ft_rows)

    # Confirm the human files do not contain primary labels.
    for path in (TA_OUT, FT_OUT):
        text = path.read_text(encoding="utf-8")
        for banned in (
            "INCLUDE_FULLTEXT",
            "EXCLUDE_TITLE_ABSTRACT",
            "EXCLUDE_FULLTEXT",
            "PRIMARY_CORE",
            "AI_ASSISTANT",
            "EC2_CD_ONLY",
        ):
            assert banned not in text, (path.name, banned)

    lines = []
    a = lines.append
    a("# Human second screening required")
    a("")
    a("Date: 2026-11-24.")
    a("This package prepares empty sheets. It does not fill a human decision, does not copy a primary decision into the human columns, and does not compute Cohen's kappa.")
    a("")
    a("**SELECTION_RELIABILITY_COMPLETE = NO**")
    a("")
    a("## Records available")
    a("")
    a("| File | Rows | What it is |")
    a("|---|---:|---|")
    a("| `05_screening/title_abstract_screening_v1.0.csv` | 43 | One screener label, `AI_ASSISTANT`, on every row. 42 rows have a title. 1 row is a collapsed note. |")
    a("| `06_fulltext/fulltext_screening_v1.0.csv` | 48 | One screener label, `AI_ASSISTANT`, on every row. Tiers: PRIMARY_CORE 42, PRIMARY_ADJACENT_SPARSE 3, PRIMARY_ADJACENT_METHOD 1, EXCLUDE_FULLTEXT 1, BACKGROUND 1. |")
    a("| `12_manuscript/TLT/supplementary/supplementary_prisma_exclusions.csv` | 48 | Same record ids as the full-text file. Not a separate exclusion ledger. |")
    a("| `04_deduplication/deduplication_audit_v1.0.csv` | %d | Duplicate-group notes. Not the deduplicated record list. |" % len(dedup))
    a("| `03_search/search_log.csv` | %d search rows | Query totals. Not title/abstract decisions. |" % len(search_log))
    a("| `03_search/venue_extension_candidates_v1.9.csv` | %d | Candidates marked `TITLE_ABSTRACT_CANDIDATE_NOT_CODED` and `screening_record_found_in_repo = NO`. Not screened rows. |" % len(venue))
    a("| `05_screening/inter_rater_fulltext_SEVEN_BLIND_EMPTY_2026-11-23.csv` | 7 | Empty full-text sheet for seven later papers. Not the protocol sample. Decision cells are still empty. |")
    a("| `05_screening/inter_rater_fulltext_SEVEN_PHUONG_2026-11-23.csv` | 7 | A filled sheet for those same seven papers. It is not the 25 percent sample and it is not the full-text exclusion list. Its labels were not copied into the human files below. |")
    a("| `12_manuscript/TLT/supplementary/Table_S-PRISMA-5.csv` | 5 | Corpus-verification removals (KT078, KT080–KT083). Not title/abstract screening rows and not the full-text exclusion ledger. |")
    a("")
    a("The 42 titled title/abstract rows are `INCLUDE_FULLTEXT`. The collapsed row is `REC_0043-REC_0140`, title `Various candidate titles`, note `Excluded 610 non-matching title/abstract records`. That note is not 610 records. It was not expanded.")
    a("")
    a("The one full-text exclusion row is `REC_0047` (`EXCLUDE_FULLTEXT`). `REC_0048` is `BACKGROUND`, not `EXCLUDE_FULLTEXT`. No deposited full-text row has tier `UNCERTAIN`.")
    a("")
    a("Deposited title/abstract rows do not contain abstract text. The human sheets use a DOI locator where the full-text file has a DOI for that record id. They do not contain the primary decision, the exclusion code, the screener id, or the notes that state a decision.")
    a("")
    a("## Records missing")
    a("")
    a("The complete 750-row record-level title/abstract ledger does not exist.")
    a("")
    a("Also absent:")
    a("")
    a("- `records_deduplicated.csv`")
    a("- a row list of 610 title/abstract exclusions")
    a("- a row list of 103 full-text exclusions")
    a("- `inter_rater_screening.csv`")
    a("- `inter_rater_fulltext.csv`")
    a("- any deposited title/abstract row labeled `UNCERTAIN`")
    a("")
    a("The printed stage counts 750, 610, 140, and 103 are report arithmetic. They were not turned into rows.")
    a("")
    a("## Sample size required")
    a("")
    a("Protocol section 20.1 requires a second coder to screen 25 percent of the deduplicated records, plus every record the first coder marked `UNCERTAIN`.")
    a("")
    a("That deduplicated ledger is missing, so the historical 25 percent sample was not drawn. The figure 750 was not used as a denominator and was not reconstructed.")
    a("")
    a("From the records that do exist, the screenable title/abstract pool is the 42 rows that have a title. `REC_0043-REC_0140` was left out of the draw because it has no title to screen.")
    a("")
    a("Prepared sample: **11** rows, which is `ceil(0.25 × 42)`. Random seed **20261113**. Draw: `random.Random(20261113).sample` on the 42 record ids sorted alphabetically, then the chosen ids written in sorted order. Uncertain rows in this file: **0**, so none were added.")
    a("")
    a("File: `05_screening/HUMAN_SECOND_SCREEN_TITLE_ABSTRACT.csv`.")
    a("")
    a("Record ids in that file: " + ", ".join(drawn) + ".")
    a("")
    a("This 11-row sheet is not a 25 percent sample of a 750-row ledger. Every titled row in the source file carries the same primary label, so the sheet cannot represent exclusion decisions that were never stored as rows.")
    a("")
    a("## Full-text exclusions requiring second review")
    a("")
    a("Protocol section 20.2 requires a second review of every `EXCLUDE_FULLTEXT` and every full-text `UNCERTAIN`, and at least 25 percent of all full-text eligibility decisions.")
    a("")
    a("Deposited `EXCLUDE_FULLTEXT` rows: **1** (`REC_0047`). Deposited full-text `UNCERTAIN` rows: **0**.")
    a("")
    a("File: `05_screening/HUMAN_SECOND_SCREEN_FULLTEXT.csv` (that one row).")
    a("")
    a("The 103-row full-text exclusion list is missing and was not reconstructed. One exclusion row does not meet the rule that at least 25 percent of all full-text eligibility decisions are double-screened. A 25 percent sample of the 48 deposited full-text rows was not added, because those other rows are not exclusion records and the historical eligibility ledger is absent.")
    a("")
    a("## Human sheets")
    a("")
    a("Both sheets use these columns:")
    a("")
    a("`record_id`, `title`, `abstract_or_locator`, `primary_decision_HIDDEN_OR_SEPARATE`, `human_second_decision`, `human_exclusion_code`, `human_screener_name`, `note`.")
    a("")
    a("`primary_decision_HIDDEN_OR_SEPARATE` is the token `HIDDEN` on every row. The primary label stays in `title_abstract_screening_v1.0.csv` and `fulltext_screening_v1.0.csv`.")
    a("")
    a("`human_second_decision`, `human_exclusion_code`, `human_screener_name`, and `note` are empty.")
    a("")
    a("Give the screener only the two human CSV files. Do not send this audit, the two source screening CSVs, the Prisma exclusion copy, or the seven-row Phương sheet. Those files show primary labels or other decisions.")
    a("")
    a("The person who fills the sheets must not be an author of the survey. This assistant does not fill them.")
    a("")
    a("## Whether selection reliability can be computed")
    a("")
    a("No. The human decision columns are empty. Cohen's kappa was not calculated.")
    a("")
    a("**SELECTION_RELIABILITY_COMPLETE = NO**")
    a("")
    AUDIT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("ta_sample", k, drawn)
    print("ft_exclusion", ex["record_id"])
    print("dedup", len(dedup), "venue", len(venue))


if __name__ == "__main__":
    main()
