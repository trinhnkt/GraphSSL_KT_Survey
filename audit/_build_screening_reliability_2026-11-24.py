# -*- coding: utf-8 -*-
"""Build deposited-subset screening reliability package.

Does not invent adjudication, reconstruct 750/103, or treat HIDDEN as a decision.
"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
TA_PRIMARY = ROOT / "05_screening" / "title_abstract_screening_v1.0.csv"
FT_PRIMARY = ROOT / "06_fulltext" / "fulltext_screening_v1.0.csv"
TA_SECOND = ROOT / "05_screening" / "HUMAN_SECOND_SCREEN_TITLE_ABSTRACT_PHUONG1_UPDATED.csv"
FT_SECOND = ROOT / "05_screening" / "HUMAN_SECOND_SCREEN_FULLTEXT_PHUONG1.csv"
SEVEN = ROOT / "05_screening" / "inter_rater_fulltext_SEVEN_PHUONG_2026-11-23.csv"

OUT_TA = ROOT / "05_screening" / "inter_rater_screening.csv"
OUT_TA_UNP = ROOT / "05_screening" / "inter_rater_screening_unpaired.csv"
OUT_FT = ROOT / "05_screening" / "inter_rater_fulltext.csv"
OUT_FT_UNP = ROOT / "05_screening" / "inter_rater_fulltext_unpaired.csv"
OUT_ADJ = ROOT / "05_screening" / "fulltext_adjudication.csv"
OUT_SUM = ROOT / "tables" / "SCREENING_RELIABILITY_SUMMARY.csv"

WRONG_PDF = (
    "Graph Knowledge Tracing in Cognitive Situation - "
    "Validation of Classic Assertions in Cognitive Psychology.pdf"
)


def load(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fieldnames, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def exact_agree(a, b):
    return "YES" if a == b else "NO"


def cohen_kappa_nominal(pairs):
    """Return (kappa_or_None, status, pe, po). NA when undefined or no variation."""
    n = len(pairs)
    if n == 0:
        return None, "UNDEFINED_EMPTY", None, None
    labels_a = [a for a, _ in pairs]
    labels_b = [b for _, b in pairs]
    if len(set(labels_a)) < 2 or len(set(labels_b)) < 2:
        agrees = sum(1 for a, b in pairs if a == b)
        po = agrees / n
        return None, "UNDEFINED_NO_CODER_VARIATION", None, po
    cats = sorted(set(labels_a) | set(labels_b))
    agrees = sum(1 for a, b in pairs if a == b)
    po = agrees / n
    ca = Counter(labels_a)
    cb = Counter(labels_b)
    pe = sum((ca[c] / n) * (cb[c] / n) for c in cats)
    if abs(1.0 - pe) < 1e-12:
        return None, "UNDEFINED_PE_EQUALS_1", pe, po
    kappa = (po - pe) / (1.0 - pe)
    return kappa, "DEFINED", pe, po


def confusion(pairs):
    cats = sorted(set(a for a, _ in pairs) | set(b for _, b in pairs))
    matrix = {a: {b: 0 for b in cats} for a in cats}
    for a, b in pairs:
        matrix[a][b] += 1
    return cats, matrix


def main():
    refs = ROOT / "14_references"
    wrong_present = (refs / WRONG_PDF).exists()
    # Correct PDF search: any pdf whose name suggests GKT-CD / the DOI suffix.
    correct_hits = []
    for p in refs.rglob("*.pdf"):
        name = p.name.lower()
        if "9533298" in name or "gkt-cd" in name or "make cognitive diagnosis model enhanced" in name:
            correct_hits.append(str(p.relative_to(ROOT)))
    # Also scan a shallow set of project dirs without walking huge trees of backups excessively.
    for folder in [ROOT / "06_fulltext", ROOT / "08_quality_reliability", ROOT / "audit"]:
        if folder.exists():
            for p in folder.rglob("*.pdf"):
                name = p.name.lower()
                if "9533298" in name or "gkt-cd" in name or "make cognitive diagnosis model enhanced" in name:
                    correct_hits.append(str(p.relative_to(ROOT)))

    pdf_available = len(correct_hits) > 0

    # --- A1 status files ---
    if not pdf_available:
        (ROOT / "audit" / "REC_0047_CORRECT_PDF_STATUS.md").write_text(
            "\n".join(
                [
                    "# REC_0047 correct PDF status",
                    "",
                    "Date: 2026-11-24.",
                    "",
                    "Target DOI: `10.1109/IJCNN52387.2021.9533298`",
                    "Target title: Make Cognitive Diagnosis Model Enhanced by Graph KT (GKT-CD).",
                    "",
                    "**REC_0047_CORRECT_PDF_AVAILABLE = NO**",
                    "**NEEDS_HUMAN_FULLTEXT_VERIFICATION = YES**",
                    "",
                    "No project PDF was found whose filename or deposited path matches the DOI or the GKT-CD title.",
                    f"The file `{WRONG_PDF}` is present under `14_references/` and is a different paper. It was not used.",
                    "",
                    "Full-text content was not inferred from title or abstract.",
                    "No `HUMAN_SECOND_SCREEN_FULLTEXT_PHUONG1_VERIFIED.csv` was created.",
                    "The blank sheet `05_screening/HUMAN_SECOND_SCREEN_FULLTEXT.csv` was not overwritten.",
                    "",
                ]
            ),
            encoding="utf-8",
        )

    (ROOT / "audit" / "REC_0047_PDF_VERIFICATION.md").write_text(
        "\n".join(
            [
                "# REC_0047 PDF verification",
                "",
                "Date: 2026-11-24.",
                "",
                f"- correct PDF found: {'YES' if pdf_available else 'NO'}",
                f"- filename: {correct_hits[0] if pdf_available else 'NONE'}",
                f"- DOI match: {'YES' if pdf_available else 'NO'}",
                f"- title match: {'YES' if pdf_available else 'NO'}",
                "- full-text human verification completed: NO",
                "",
                f"Wrong file present and not used: `{WRONG_PDF}` = {'YES' if wrong_present else 'NO'}.",
                "",
                "Phương 1 note already states that IEEE Xplore provided metadata/abstract only in that environment.",
                "That note was not rewritten as a completed full-text verification.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    # --- A2 adjudication shell ---
    adj_fields = [
        "record_id",
        "primary_decision",
        "second_decision",
        "disagreement",
        "adjudicator_name",
        "final_decision",
        "final_exclusion_code",
        "rationale",
        "evidence_locator",
        "adjudication_status",
    ]
    write_csv(
        OUT_ADJ,
        adj_fields,
        [
            {
                "record_id": "REC_0047",
                "primary_decision": "EXCLUDE_FULLTEXT",
                "second_decision": "PRIMARY_ADJACENT_METHOD",
                "disagreement": "YES",
                "adjudicator_name": "",
                "final_decision": "",
                "final_exclusion_code": "",
                "rationale": "",
                "evidence_locator": "doi:10.1109/IJCNN52387.2021.9533298",
                "adjudication_status": "NEEDS_HUMAN_ADJUDICATION",
            }
        ],
    )
    (ROOT / "audit" / "REC_0047_ADJUDICATION_STATUS.md").write_text(
        "\n".join(
            [
                "# REC_0047 adjudication status",
                "",
                "Date: 2026-11-24.",
                "",
                "Primary/original decision: `EXCLUDE_FULLTEXT` (`06_fulltext/fulltext_screening_v1.0.csv`, code `EC2_CD_ONLY`).",
                "Phương 1 decision: `PRIMARY_ADJACENT_METHOD` (`05_screening/HUMAN_SECOND_SCREEN_FULLTEXT_PHUONG1.csv`).",
                "",
                "This is a real disagreement. No human adjudicator name, final decision, exclusion code, or rationale was present in the project, so those fields were left blank.",
                "",
                "File: `05_screening/fulltext_adjudication.csv`",
                "Status on the row: `NEEDS_HUMAN_ADJUDICATION`",
                "",
                "**REC_0047_ADJUDICATED = NO**",
                "",
            ]
        ),
        encoding="utf-8",
    )

    # --- A3.1 title/abstract pairs ---
    ta_pri = {r["record_id"]: r for r in load(TA_PRIMARY)}
    ta_sec = load(TA_SECOND)
    titled_pool = [r for r in ta_pri.values() if r["record_id"] != "REC_0043-REC_0140"]
    assert len(titled_pool) == 42

    ta_fields = [
        "record_id",
        "title",
        "decision_A",
        "decision_B",
        "exact_agreement",
        "decision_A_source",
        "decision_B_source",
        "adjudicated_decision",
        "adjudication_note",
    ]
    ta_unp_fields = ["record_id", "title", "reason", "detail"]
    ta_rows = []
    ta_unp = []
    for r in ta_sec:
        rid = r["record_id"]
        b = (r.get("human_second_decision") or "").strip()
        if not b or b == "HIDDEN":
            ta_unp.append(
                {
                    "record_id": rid,
                    "title": r["title"],
                    "reason": "MISSING_SECOND_DECISION",
                    "detail": "human_second_decision empty or HIDDEN",
                }
            )
            continue
        if rid not in ta_pri:
            ta_unp.append(
                {
                    "record_id": rid,
                    "title": r["title"],
                    "reason": "MISSING_PRIMARY_DECISION",
                    "detail": "record_id not in title_abstract_screening_v1.0.csv",
                }
            )
            continue
        a = (ta_pri[rid].get("decision") or "").strip()
        if not a or a == "HIDDEN":
            ta_unp.append(
                {
                    "record_id": rid,
                    "title": r["title"],
                    "reason": "MISSING_PRIMARY_DECISION",
                    "detail": "primary decision empty or HIDDEN",
                }
            )
            continue
        note = ""
        if rid == "REC_0040":
            note = (
                "Second screener marked UNCERTAIN because the deposited DOI resolves "
                "to Discrete Budget Aggregation, not a knowledge-tracing paper."
            )
        ta_rows.append(
            {
                "record_id": rid,
                "title": r["title"],
                "decision_A": a,
                "decision_B": b,
                "exact_agreement": exact_agree(a, b),
                "decision_A_source": "05_screening/title_abstract_screening_v1.0.csv",
                "decision_B_source": "05_screening/HUMAN_SECOND_SCREEN_TITLE_ABSTRACT_PHUONG1_UPDATED.csv",
                "adjudicated_decision": "",
                "adjudication_note": note,
            }
        )
    write_csv(OUT_TA, ta_fields, ta_rows)
    write_csv(OUT_TA_UNP, ta_unp_fields, ta_unp)

    # --- A3.2 full-text pairs ---
    ft_pri = {r["record_id"]: r for r in load(FT_PRIMARY)}
    ft_sec_rows = load(FT_SECOND)
    # Also log seven-paper second decisions that lack a deposited primary REC id.
    seven = load(SEVEN)
    ft_rows = []
    ft_unp = []
    for r in ft_sec_rows:
        rid = r["record_id"]
        b = (r.get("human_second_decision") or "").strip()
        if not b or b == "HIDDEN":
            ft_unp.append(
                {
                    "record_id": rid,
                    "title": r["title"],
                    "reason": "MISSING_SECOND_DECISION",
                    "detail": "human_second_decision empty or HIDDEN",
                }
            )
            continue
        if rid not in ft_pri:
            ft_unp.append(
                {
                    "record_id": rid,
                    "title": r["title"],
                    "reason": "MISSING_PRIMARY_DECISION",
                    "detail": "record_id not in fulltext_screening_v1.0.csv",
                }
            )
            continue
        a = (ft_pri[rid].get("final_tier") or "").strip()
        if not a or a == "HIDDEN":
            ft_unp.append(
                {
                    "record_id": rid,
                    "title": r["title"],
                    "reason": "MISSING_PRIMARY_DECISION",
                    "detail": "primary final_tier empty or HIDDEN",
                }
            )
            continue
        adj_note = "PENDING_HUMAN_ADJUDICATION" if rid == "REC_0047" else ""
        ft_rows.append(
            {
                "record_id": rid,
                "title": r["title"],
                "decision_A": a,
                "decision_B": b,
                "exact_agreement": exact_agree(a, b),
                "decision_A_source": "06_fulltext/fulltext_screening_v1.0.csv",
                "decision_B_source": "05_screening/HUMAN_SECOND_SCREEN_FULLTEXT_PHUONG1.csv",
                "adjudicated_decision": "",
                "adjudication_note": adj_note,
            }
        )
    for r in seven:
        rid = r["record_id"]
        ft_unp.append(
            {
                "record_id": rid,
                "title": r["title"],
                "reason": "MISSING_PRIMARY_DECISION",
                "detail": (
                    "Human second decision exists in inter_rater_fulltext_SEVEN_PHUONG_2026-11-23.csv, "
                    "but no matching primary full-text decision exists under that id in "
                    "fulltext_screening_v1.0.csv. Not paired."
                ),
            }
        )
    write_csv(OUT_FT, ta_fields, ft_rows)  # same column schema
    write_csv(OUT_FT_UNP, ta_unp_fields, ft_unp)

    # --- A4 stats ---
    def summarize(stage, rows, pool_note):
        pairs = [(r["decision_A"], r["decision_B"]) for r in rows]
        n = len(pairs)
        n_agree = sum(1 for a, b in pairs if a == b)
        n_disagree = n - n_agree
        raw = (n_agree / n) if n else None
        kappa, status, pe, po = cohen_kappa_nominal(pairs)
        cats, matrix = confusion(pairs) if n else ([], {})
        return {
            "stage": stage,
            "n_paired": n,
            "n_agree": n_agree,
            "n_disagree": n_disagree,
            "raw_agreement": raw,
            "cohen_kappa": kappa,
            "kappa_status": status,
            "pe": pe,
            "po": po,
            "cats": cats,
            "matrix": matrix,
            "count_a": Counter(a for a, _ in pairs),
            "count_b": Counter(b for _, b in pairs),
            "pool_note": pool_note,
            "scope": "deposited independently double-screened subset only",
        }

    ta_stats = summarize(
        "title_abstract",
        ta_rows,
        "11/42 = 26.2% of the deposited/available titled title/abstract screening subset",
    )
    ft_stats = summarize(
        "fulltext",
        ft_rows,
        "1 paired deposited full-text exclusion/eligibility row with an independent human second decision",
    )

    write_csv(
        OUT_SUM,
        [
            "stage",
            "n_paired",
            "n_agree",
            "n_disagree",
            "raw_agreement",
            "cohen_kappa",
            "kappa_status",
            "scope",
        ],
        [
            {
                "stage": s["stage"],
                "n_paired": s["n_paired"],
                "n_agree": s["n_agree"],
                "n_disagree": s["n_disagree"],
                "raw_agreement": f"{s['raw_agreement']:.6f}" if s["raw_agreement"] is not None else "",
                "cohen_kappa": (
                    f"{s['cohen_kappa']:.6f}" if s["cohen_kappa"] is not None else "NA"
                ),
                "kappa_status": s["kappa_status"],
                "scope": s["scope"],
            }
            for s in (ta_stats, ft_stats)
        ],
    )

    def matrix_md(stats):
        if not stats["cats"]:
            return "_empty_"
        cats = stats["cats"]
        lines = ["| decision_A \\ decision_B | " + " | ".join(cats) + " |", "|---|" + "|".join(["---:"] * len(cats)) + "|"]
        for a in cats:
            cells = [str(stats["matrix"][a][b]) for b in cats]
            lines.append(f"| {a} | " + " | ".join(cells) + " |")
        return "\n".join(lines)

    # --- A5 audit ---
    subset_complete = (
        len(ta_rows) == 11
        and len(ft_rows) == 1
        and all(r["decision_A"] != "HIDDEN" and r["decision_B"] != "HIDDEN" for r in ta_rows + ft_rows)
    )
    audit_lines = [
        "# Screening reliability — deposited independently double-screened subset",
        "",
        "Date: 2026-11-24.",
        "",
        "## 1. Historical limitation",
        "",
        "A complete historical record-level ledger for all reported screening stages is not available.",
        "The printed stage counts 750 title/abstract records and 103 full-text exclusions were not reconstructed.",
        "",
        "## 2. Available paired subset",
        "",
        "### Title/abstract",
        "",
        f"- n paired: {ta_stats['n_paired']}",
        f"- denominator of available/deposited titled pool: 42",
        f"- share of that deposited pool: {ta_stats['pool_note']}",
        f"- n agree: {ta_stats['n_agree']}; n disagree: {ta_stats['n_disagree']}",
        f"- raw agreement: {ta_stats['raw_agreement']:.6f}",
        f"- Cohen's kappa: NA",
        f"- kappa_status: {ta_stats['kappa_status']}",
        "",
        "Coder A category counts: " + ", ".join(f"{k}={v}" for k, v in sorted(ta_stats['count_a'].items())) + ".",
        "",
        "Coder B category counts: " + ", ".join(f"{k}={v}" for k, v in sorted(ta_stats['count_b'].items())) + ".",
        "",
        "Confusion matrix (rows = decision_A, columns = decision_B):",
        "",
        matrix_md(ta_stats),
        "",
        "Kappa is NA because Coder A has no category variation on this subset (all `INCLUDE_FULLTEXT`).",
        "A numeric kappa is not forced. Raw agreement remains reportable at n = 11.",
        "",
        "This is **not** 11/750 and is **not** described as 25% of the historical screening population.",
        "",
        "### Full-text",
        "",
        f"- n paired: {ft_stats['n_paired']}",
        f"- n agree: {ft_stats['n_agree']}; n disagree: {ft_stats['n_disagree']}",
        f"- raw agreement: {ft_stats['raw_agreement']:.6f}",
        f"- Cohen's kappa: NA",
        f"- kappa_status: {ft_stats['kappa_status']}",
        "",
        "Coder A category counts: " + ", ".join(f"{k}={v}" for k, v in sorted(ft_stats['count_a'].items())) + ".",
        "",
        "Coder B category counts: " + ", ".join(f"{k}={v}" for k, v in sorted(ft_stats['count_b'].items())) + ".",
        "",
        "Confusion matrix:",
        "",
        matrix_md(ft_stats),
        "",
        "Kappa is NA because n = 1 provides no usable category variation for either coder.",
        "Raw agreement is 0/1 on the single paired exclusion row.",
        "",
        "## 3. REC_0047 disagreement",
        "",
        "`EXCLUDE_FULLTEXT` versus `PRIMARY_ADJACENT_METHOD`.",
        "Adjudication is **not** complete (`REC_0047_ADJUDICATED = NO`).",
        "Correct GKT-CD PDF is **not** in the repository (`REC_0047_CORRECT_PDF_AVAILABLE = NO`).",
        "The wrong Cognitive Situation PDF was not used.",
        "",
        "## 4. Scope limitation",
        "",
        "These coefficients characterize the deposited independently double-screened subset and are not estimates of reliability for the full historical 750-record title/abstract stage or the 103 reported full-text exclusions.",
        "",
        "## 5. Distinguish screening from coding reliability",
        "",
        "Screening reliability concerns inclusion/exclusion decisions. The existing 20-paper coding reliability concerns agreement on coded study attributes. The two analyses are separate and their kappas must not be pooled.",
        "",
        "## 6. Missing evidence",
        "",
        "- missing historical ledger for 750 / 610 / 103 stages",
        f"- unpaired title/abstract rows in this pass: {len(ta_unp)}",
        f"- unpaired full-text / extension rows logged: {len(ft_unp)} (includes seven EXT ids with second labels but no deposited primary REC decision)",
        "- pending human adjudication for REC_0047",
        "- correct-PDF full-text verification for REC_0047 still pending",
        "",
        "Pair files:",
        "",
        "- `05_screening/inter_rater_screening.csv`",
        "- `05_screening/inter_rater_fulltext.csv`",
        "- `05_screening/inter_rater_screening_unpaired.csv`",
        "- `05_screening/inter_rater_fulltext_unpaired.csv`",
        "- `tables/SCREENING_RELIABILITY_SUMMARY.csv`",
        "",
        f"**SCREENING_RELIABILITY_SUBSET_COMPLETE = {'YES' if subset_complete else 'NO'}**",
        "",
        "YES here means the paired files are valid, the calculations are reproducible, and the scope wording is the deposited subset only.",
        "It does **not** mean the historical 750/103 screening reliability has been recovered,",
        "and it does **not** mean REC_0047 adjudication or PDF verification is finished.",
        "",
    ]
    (ROOT / "audit" / "SCREENING_RELIABILITY_DEPOSITED_SUBSET.md").write_text(
        "\n".join(audit_lines), encoding="utf-8"
    )

    print("pdf_available", pdf_available)
    print("ta_paired", len(ta_rows), "ta_unp", len(ta_unp))
    print("ft_paired", len(ft_rows), "ft_unp", len(ft_unp))
    print("ta", ta_stats["n_agree"], ta_stats["n_disagree"], ta_stats["raw_agreement"], ta_stats["kappa_status"])
    print("ft", ft_stats["n_agree"], ft_stats["n_disagree"], ft_stats["raw_agreement"], ft_stats["kappa_status"])
    print("subset_complete", subset_complete)


if __name__ == "__main__":
    main()
