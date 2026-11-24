# -*- coding: utf-8 -*-
"""Sync expanded corpus rows to audited cold-start/QA/provenance and freeze docs.

Does not overwrite data/PRIMARY_CORE_EXPANDED_2026-11-23.csv.
Creates a versioned 2026-11-24 file.
"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
SRC = ROOT / "data" / "PRIMARY_CORE_EXPANDED_2026-11-23.csv"
OUT = ROOT / "data" / "PRIMARY_CORE_EXPANDED_2026-11-24.csv"
QA37 = ROOT / "12_manuscript" / "TLT" / "supplementary" / "supplementary_quality_scores.csv"
CAL = ROOT / "tables" / "CALIBRATION_EXPANDED.csv"
PROV8 = ROOT / "12_manuscript" / "TLT" / "supplementary" / "graph_provenance_8way_audit_v1.9.csv"

INTERACTION_DROP = {"KT086"}
ITEM_CS = {"KT044"}
LEARNER_CS = {"KT023", "KT087"}

# Display provenance for all G=YES papers in the expanded corpus.
# Deposited displays come from graph_provenance_8way_audit_v1.9.csv unless overridden
# by the seven-PDF re-read. Expansion graph papers are set explicitly.
PROVENANCE_FINAL = {
    "KT023": "MODEL_DEFINED_FIXED",
    "KT035": "MODEL_DEFINED_FIXED",
    "KT050": "MODEL_DEFINED_FIXED",
    "KT062": "MODEL_DEFINED_FIXED",
    "KT064": "MODEL_DEFINED_FIXED",
    "KT065": "MODEL_DEFINED_FIXED",
    "KT069": "MODEL_DEFINED_FIXED",
    "KT084": "MODEL_DEFINED_FIXED",
    "KT085": "DYNAMICALLY_LEARNED",  # PDF Sec 4.1 RL updates edges; was wrongly UNCLEAR via split gap
    "KT086": "MODEL_DEFINED_FIXED",
    "KT089": "MODEL_DEFINED_FIXED",
}

NEW_QA = {
    "KT084": (2, 2, 1, 2, 1, 0, 0, 2),
    "KT085": (2, 2, 2, 2, 1, 0, 0, 2),
    "KT086": (2, 2, 2, 2, 1, 0, 2, 1),
    "KT087": (2, 2, 2, 2, 1, 2, 2, 1),
    "KT040": (2, 2, 2, 2, 1, 2, 0, 2),
    "KT088": (2, 2, 1, 2, 1, 0, 0, 1),
    "KT089": (2, 2, 1, 2, 1, 0, 0, 1),
}


def yn(flag: bool) -> str:
    return "YES" if flag else "NO"


def load(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def norm_display(tok: str) -> str:
    if tok == "DYNAMIC_LEARNED":
        return "DYNAMICALLY_LEARNED"
    return tok


def main():
    rows = load(SRC)
    assert len(rows) == 44

    qa37 = {
        r["paper_id"]: (
            int(r["QA1_task_clarity"]),
            int(r["QA2_data_transparency"]),
            int(r["QA3_split_control"]),
            int(r["QA4_baseline_adequacy"]),
            int(r["QA5_statistical_rigor"]),
            int(r["QA6_author_artifacts_capped"]),
            int(r["QA7_sparse_construct"]),
            int(r["QA8_computational_reporting"]),
        )
        for r in load(QA37)
    }
    assert len(qa37) == 37 and "KT040" not in qa37

    cal = {r["paper_id"]: r for r in load(CAL)}
    assert len(cal) == 44

    prov8 = {
        r["paper_id"]: norm_display(r["display_3token_graph_taxonomy_v1.8"])
        for r in load(PROV8)
    }

    for r in rows:
        pid = r["paper_id"]
        r["interaction_drop"] = yn(pid in INTERACTION_DROP)
        r["item_cold_start"] = yn(pid in ITEM_CS)
        r["learner_cold_start"] = yn(pid in LEARNER_CS)
        r["strict_KC_cold_start"] = "NO"

        c = cal[pid]
        r["ECE_reported"] = c["ECE_reported"]
        r["Brier_reported"] = c["Brier_reported"]
        r["RMSE_reported"] = c["RMSE_reported"]
        r["calibration_plot_reported"] = c["reliability_or_calibration_plot_reported"]

        if r["G_criterion"] == "YES":
            if pid in PROVENANCE_FINAL:
                r["graph_provenance"] = PROVENANCE_FINAL[pid]
            elif pid in prov8:
                r["graph_provenance"] = prov8[pid]
            else:
                raise SystemExit(f"Missing provenance for graph paper {pid}")
        else:
            r["graph_provenance"] = "NA"

        q = NEW_QA[pid] if pid in NEW_QA else qa37[pid]
        for i, key in enumerate(["QA1", "QA2", "QA3", "QA4", "QA5", "QA6", "QA7", "QA8"]):
            r[key] = str(q[i])

        note = (r.get("evidence_note") or "").strip()
        extra = (
            " Synced 2026-11-24 to COUNTS_EXPANDED_FINAL cold-start/QA; "
            "provenance display locked (KT085=DYNAMICALLY_LEARNED from Sec 4.1 RL edge updates)."
        )
        if "Synced 2026-11-24" not in note:
            r["evidence_note"] = (note + extra).strip()

    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    g = sum(r["G_criterion"] == "YES" for r in rows)
    s = sum(r["S_criterion"] == "YES" for r in rows)
    both = sum(r["G_criterion"] == "YES" and r["S_criterion"] == "YES" for r in rows)
    assert g + s - both == 44

    prov = Counter(
        r["graph_provenance"] for r in rows if r["G_criterion"] == "YES"
    )
    assert sum(prov.values()) == 40
    assert prov.get("UNCLEAR", 0) == 0
    assert dict(prov) == {
        "MODEL_DEFINED_FIXED": 24,
        "EXTERNAL_FIXED": 7,
        "DYNAMICALLY_LEARNED": 9,
    }, dict(prov)

    print("wrote", OUT)
    print("N,G,S,both", 44, g, s, both)
    print("prov", dict(prov))
    print(
        "drop/item/learn/kc",
        sum(r["interaction_drop"] == "YES" for r in rows),
        sum(r["item_cold_start"] == "YES" for r in rows),
        sum(r["learner_cold_start"] == "YES" for r in rows),
        sum(r["strict_KC_cold_start"] == "YES" for r in rows),
    )


if __name__ == "__main__":
    main()
