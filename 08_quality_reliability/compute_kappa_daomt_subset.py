"""Cohen's kappa for the DaoMT 10-paper subset vs locked Coder A.

Refuses to write a kappa report if any of the 80 cells is empty.
Does not invent codes. Do not pool with NguyenKT.
"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
A_PATH = ROOT / "inter_rater_coderA_locked_v1.0.csv"
B_PATH = ROOT / "inter_rater_coding_sample_BLIND_EMPTY_v1.4_DaoMT.csv"
OUT = ROOT / "KAPPA_A_vs_DaoMT_SUBSET_2026-09-14.md"

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


def kappa(pairs: list[tuple[str, str]]) -> tuple[int, float, float, float]:
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
    with A_PATH.open(encoding="utf-8-sig", newline="") as f:
        a_rows = {r["paper_id"]: r for r in csv.DictReader(f)}
    with B_PATH.open(encoding="utf-8-sig", newline="") as f:
        b_rows = list(csv.DictReader(f))

    missing = []
    for r in b_rows:
        pid = r["paper_id"]
        if pid not in a_rows:
            missing.append(f"{pid}: not in Coder A")
            continue
        for _, _, bcol in FIELDS:
            if not (r.get(bcol) or "").strip():
                missing.append(f"{pid}.{bcol}")
        if (r.get("coderB_id") or "").strip() != "DaoMT":
            missing.append(f"{pid}.coderB_id != DaoMT")

    if missing:
        print("INCOMPLETE — no kappa file written.")
        for m in missing:
            print(" ", m)
        raise SystemExit(2)

    lines = [
        "# Cohen's kappa — Coder A vs DaoMT subset",
        "",
        "**Date:** 2026-09-14",
        f"**A:** `{A_PATH.name}`",
        f"**B:** `{B_PATH.name}` (`coderB_id=DaoMT`)",
        "",
        "Independent 10-paper subset. Not pooled with locator-assisted NguyenKT.",
        "N = 10 papers × 8 fields = 80 cells.",
        r"$\kappa=(p_o-p_e)/(1-p_e)$. If $p_o=p_e=1$, $\kappa=1$ by convention.",
        "",
        "| Field | Agree | $p_o$ | $p_e$ | $\\kappa$ |",
        "|---|---:|---:|---:|---:|",
    ]
    ks = []
    diffs = []
    for name, acol, bcol in FIELDS:
        pairs = [(a_rows[r["paper_id"]][acol].strip(), r[bcol].strip()) for r in b_rows]
        agree, po, pe, k = kappa(pairs)
        ks.append(k)
        note = ""
        if all(a == b == pairs[0][0] for a, b in pairs) and pairs[0][0] in {"NO", "N"}:
            note = " (all NO)" if pairs[0][0] == "NO" else " (all N)"
        lines.append(f"| {name} | {agree}/10 | {po:.3f} | {pe:.3f} | {k:.2f}{note} |")
        for r in b_rows:
            av = a_rows[r["paper_id"]][acol].strip()
            bv = r[bcol].strip()
            if av != bv:
                diffs.append(f"{r['paper_id']} `{name}` A={av} / B={bv}")

    mean_k = sum(ks) / len(ks)
    agree_all = 80 - len(diffs)
    lines += [
        f"| Unweighted mean of 8 | — | — | — | **{mean_k:.2f}** |",
        "",
        f"Pre-adjudication agreement: **{agree_all}/80**.",
        "",
    ]
    if diffs:
        lines.append("Pre-adjudication diffs:")
        lines.extend(f"- {d}" for d in diffs)
    else:
        lines.append("No pre-adjudication diffs.")
    lines += [
        "",
        "Do not merge this coefficient with the 20-paper locator-assisted kappa.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("Wrote", OUT)
    print(f"agree {agree_all}/80 mean_k {mean_k:.2f}")


if __name__ == "__main__":
    main()
