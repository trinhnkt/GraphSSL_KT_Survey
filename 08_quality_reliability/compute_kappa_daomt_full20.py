"""Merge DaoMT first10 + REST, freeze FULL20, compute kappa vs Coder A."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIELDS = [
    ("S_criterion", "coderA_S_criterion", "coderB_S_criterion"),
    ("ssl_family", "coderA_ssl_family", "coderB_ssl_family"),
    ("graph_provenance", "coderA_graph_provenance", "coderB_graph_provenance"),
    ("gnn_encoder", "coderA_gnn_encoder", "coderB_gnn_encoder"),
    ("strict_kc_cold_start", "coderA_strict_kc_cold_start", "coderB_strict_kc_cold_start"),
    ("item_cold_start", "coderA_item_cold_start", "coderB_item_cold_start"),
    ("learner_cold_start", "coderA_learner_cold_start", "coderB_learner_cold_start"),
    ("ece_reported", "coderA_ece_reported", "coderB_ece_reported"),
]
ORDER = [
    "KT004", "KT011", "KT014", "KT026", "KT031", "KT035", "KT037", "KT038",
    "KT039", "KT042", "KT043", "KT044", "KT047", "KT050", "KT066", "KT068",
    "KT070", "KT076", "KT077", "KT079",
]


def kappa(pairs: list[tuple[str, str]]):
    n = len(pairs)
    agree = sum(1 for a, b in pairs if a == b)
    po = agree / n
    ca = Counter(a for a, _ in pairs)
    cb = Counter(b for _, b in pairs)
    pe = sum((ca[k] / n) * (cb[k] / n) for k in set(ca) | set(cb))
    if po == 1.0 and pe == 1.0:
        k = 1.0
    elif pe == 1.0:
        k = 0.0
    else:
        k = (po - pe) / (1.0 - pe)
    return agree, po, pe, k


def main() -> None:
    first_path = ROOT / "inter_rater_coding_sample_BLIND_EMPTY_v1.4_DaoMT_AS_SUBMITTED.csv"
    rest_path = ROOT / "inter_rater_coding_sample_BLIND_EMPTY_v1.4_DaoMT_REST.csv"
    rest_as = ROOT / "inter_rater_coding_sample_BLIND_EMPTY_v1.4_DaoMT_REST_AS_SUBMITTED.csv"
    full_as = ROOT / "inter_rater_coding_sample_BLIND_EMPTY_v1.4_DaoMT_FULL20_AS_SUBMITTED.csv"
    out_md = ROOT / "KAPPA_A_vs_DaoMT_FULL20_2026-09-14.md"

    rest_as.write_text(rest_path.read_text(encoding="utf-8"), encoding="utf-8")

    with first_path.open(encoding="utf-8-sig", newline="") as f:
        first = list(csv.DictReader(f))
    with rest_path.open(encoding="utf-8-sig", newline="") as f:
        rest = list(csv.DictReader(f))

    by = {r["paper_id"]: r for r in first + rest}
    missing = [p for p in ORDER if p not in by or not (by[p].get("coderB_S_criterion") or "").strip()]
    if missing:
        raise SystemExit(f"incomplete: {missing}")

    fieldnames = list(first[0].keys())
    rows = [by[pid] for pid in ORDER]
    with full_as.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    (ROOT / "inter_rater_coding_sample_BLIND_EMPTY_v1.4.csv").write_text(
        full_as.read_text(encoding="utf-8"), encoding="utf-8"
    )

    with (ROOT / "inter_rater_coderA_locked_v1.0.csv").open(encoding="utf-8-sig", newline="") as f:
        a_rows = {r["paper_id"]: r for r in csv.DictReader(f)}

    lines = [
        "# Cohen's kappa — Coder A vs DaoMT FULL 20 (independent, no locator)",
        "",
        "**Date:** 2026-09-14",
        f"**A:** `inter_rater_coderA_locked_v1.0.csv`",
        f"**B:** `{full_as.name}` (`coderB_id=DaoMT`)",
        "",
        "Independent 20-paper sample (subset 10 + REST 10). Not pooled with locator-assisted NguyenKT.",
        "N = 20 papers × 8 fields = 160 cells.",
        r"$\kappa=(p_o-p_e)/(1-p_e)$. If $p_o=p_e=1$, $\kappa=1$ by convention.",
        "",
        "| Field | Agree | $p_o$ | $p_e$ | $\\kappa$ |",
        "|---|---:|---:|---:|---:|",
    ]
    ks = []
    diffs = []
    for name, acol, bcol in FIELDS:
        pairs = [(a_rows[r["paper_id"]][acol].strip(), r[bcol].strip()) for r in rows]
        agree, po, pe, k = kappa(pairs)
        ks.append(k)
        note = ""
        if all(a == b == pairs[0][0] for a, b in pairs) and pairs[0][0] in {"NO", "N"}:
            note = " (all NO)" if pairs[0][0] == "NO" else " (all N)"
        lines.append(f"| {name} | {agree}/20 | {po:.3f} | {pe:.3f} | {k:.2f}{note} |")
        for r in rows:
            av = a_rows[r["paper_id"]][acol].strip()
            bv = r[bcol].strip()
            if av != bv:
                diffs.append(f"{r['paper_id']} `{name}` A={av} / B={bv}")

    mean_k = sum(ks) / len(ks)
    agree_all = 160 - len(diffs)
    lines += [
        f"| Unweighted mean of 8 | — | — | — | **{mean_k:.2f}** |",
        "",
        f"Pre-adjudication agreement: **{agree_all}/160**.",
        "",
    ]
    if diffs:
        lines.append("Pre-adjudication diffs:")
        lines.extend(f"- {d}" for d in diffs)
    else:
        lines.append("No pre-adjudication diffs.")
    lines += ["", "Do not merge with the locator-assisted NguyenKT kappa.", ""]
    out_md.write_text("\n".join(lines), encoding="utf-8")
    print("Wrote", full_as)
    print("Wrote", out_md)
    print(f"agree {agree_all}/160 mean_k {mean_k:.2f}")
    for d in diffs:
        print("DIFF", d)


if __name__ == "__main__":
    main()
