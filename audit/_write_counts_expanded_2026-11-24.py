# -*- coding: utf-8 -*-
"""Recompute expanded-corpus cold-start, calibration, and QA counts.

Does not edit the manuscript or the deposited 37-row tables.
"""
import csv
from pathlib import Path

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
EXPANDED = ROOT / "data" / "PRIMARY_CORE_EXPANDED_2026-11-23.csv"
QA37 = ROOT / "12_manuscript" / "TLT" / "supplementary" / "supplementary_quality_scores.csv"
CAL_OUT = ROOT / "tables" / "CALIBRATION_EXPANDED.csv"
AUDIT_OUT = ROOT / "audit" / "COUNTS_EXPANDED_FINAL.md"

RMSE_YES = {
    "KT014", "KT035", "KT037", "KT039", "KT042", "KT056",
    "KT063", "KT065", "KT066", "KT068", "KT070", "KT077",
    "KT040", "KT086",
}
NLL_EVAL_YES = {"KT085"}
PLOT_YES = {"KT039"}
TRAINING_NLL = {"KT004", "KT012", "KT035", "KT052", "KT066", "KT067"}

# Decision-table codes. Prose mentions are not YES.
INTERACTION_DROP = {"KT086"}
ITEM_CS = {"KT044"}
LEARNER_CS = {"KT023", "KT087"}
STRICT_KC = set()

# QA1-QA8 for the seven papers that were not in the deposited score file.
# Thresholds unchanged: HIGH >= 0.80, MODERATE 0.55-0.79, LIMITED < 0.55.
# QA6 uses the locked anchors: 0 no author artifact, 1 partial, 2 substantial.
# A dataset repository is not an author artifact.
NEW_QA = {
    "KT084": (2, 2, 1, 2, 1, 0, 0, 2),  # DECKT
    "KT085": (2, 2, 2, 2, 1, 0, 0, 2),  # KT-Deeper
    "KT086": (2, 2, 2, 2, 1, 0, 2, 1),  # HCMKT
    "KT087": (2, 2, 2, 2, 1, 2, 2, 1),  # CoSKT
    "KT040": (2, 2, 2, 2, 1, 2, 0, 2),  # DTransformer
    "KT088": (2, 2, 1, 2, 1, 0, 0, 1),  # SP-CLKT
    "KT089": (2, 2, 1, 2, 1, 0, 0, 1),  # CLBG
}

QA_NAMES = [
    "QA1 Task clarity",
    "QA2 Data and preprocessing",
    "QA3 Split, provenance, leakage",
    "QA4 Baselines and ablations",
    "QA5 Statistical uncertainty",
    "QA6 Author artifacts",
    "QA7 Sparse and cold-start construct",
    "QA8 Computational reporting",
]


def tier(norm):
    if norm >= 0.80:
        return "HIGH"
    if norm >= 0.55:
        return "MODERATE"
    return "LIMITED"


def yn(flag):
    return "YES" if flag else "NO"


def main():
    with EXPANDED.open(encoding="utf-8", newline="") as f:
        papers = list(csv.DictReader(f))
    assert len(papers) == 44, len(papers)
    ids = [r["paper_id"] for r in papers]
    assert len(set(ids)) == 44
    title = {r["paper_id"]: r["title"] for r in papers}

    with QA37.open(encoding="utf-8", newline="") as f:
        qa_rows = list(csv.DictReader(f))
    assert len(qa_rows) == 37, len(qa_rows)
    qa_ids = {r["paper_id"] for r in qa_rows}
    assert "KT040" not in qa_ids
    missing_new = [i for i in NEW_QA if i not in ids]
    assert not missing_new, missing_new
    overlap = qa_ids & set(NEW_QA)
    assert not overlap, overlap

    # Calibration table
    CAL_OUT.parent.mkdir(parents=True, exist_ok=True)
    cal_fields = [
        "paper_id", "model",
        "ECE_reported", "Brier_reported", "RMSE_reported",
        "NLL_or_logloss_evaluation_reported",
        "reliability_or_calibration_plot_reported",
        "evidence_note",
    ]
    n_ece = n_brier = n_rmse = n_nll = n_plot = 0
    with CAL_OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cal_fields)
        w.writeheader()
        for pid in ids:
            ece = False
            brier = False
            rmse = pid in RMSE_YES
            nll = pid in NLL_EVAL_YES
            plot = pid in PLOT_YES
            n_ece += ece
            n_brier += brier
            n_rmse += rmse
            n_nll += nll
            n_plot += plot
            if pid == "KT084":
                note = (
                    "No ECE, Brier, or RMSE evaluation metric. "
                    "Figure 4 is a one-student prediction heatmap. "
                    "The body calls it predictive calibration; the caption is "
                    "Prediction visualization analysis. Not a reliability diagram."
                )
            elif pid == "KT085":
                note = (
                    "Table 5 reports an NLL gap between training and test data "
                    "for the graph-generation model, with KL divergence. "
                    "That is an evaluation of generated-graph distributions, "
                    "not a response-probability calibration score and not ECE or Brier. "
                    "No RMSE."
                )
            elif pid == "KT039":
                note = (
                    "RMSE is an overall prediction error beside AUC. "
                    "Figure 7 is a calibration plot binned by predictions on ASSIST09 "
                    "and reports no ECE or Brier."
                )
            elif pid == "KT040":
                note = (
                    "Table 2 reports MAE, RMSE, ACC, and AUC as next-response "
                    "evaluation metrics. RMSE is prediction error, not calibration. "
                    "No ECE, Brier, or reliability diagram."
                )
            elif pid == "KT086":
                note = (
                    "Table 4 and Figure 5 report AUC, ACC, and RMSE. "
                    "RMSE is prediction error, not calibration. "
                    "No ECE, Brier, or reliability diagram."
                )
            elif pid in TRAINING_NLL and rmse:
                note = (
                    "RMSE is an overall prediction error beside AUC or accuracy, not calibration. "
                    "Negative log-likelihood appears as a training objective, not as an evaluation metric. "
                    "No ECE, Brier, or reliability diagram."
                )
            elif pid in TRAINING_NLL:
                note = (
                    "Negative log-likelihood appears as a training objective, not as an evaluation metric. "
                    "No ECE, Brier, RMSE evaluation metric, or reliability diagram."
                )
            elif rmse:
                note = (
                    "RMSE is an overall prediction error beside AUC or accuracy, not calibration. "
                    "No ECE, Brier, evaluation NLL, or reliability diagram."
                )
            elif pid == "KT076":
                note = (
                    "PDF text layer is empty, so this row is not a fresh keyword hit. "
                    "No ECE, Brier, RMSE, evaluation NLL, or reliability diagram is recorded."
                )
            else:
                note = (
                    "No ECE, Brier, RMSE evaluation metric, evaluation NLL, "
                    "or reliability diagram in the text-layer scan."
                )
            w.writerow({
                "paper_id": pid,
                "model": title[pid],
                "ECE_reported": yn(ece),
                "Brier_reported": yn(brier),
                "RMSE_reported": yn(rmse),
                "NLL_or_logloss_evaluation_reported": yn(nll),
                "reliability_or_calibration_plot_reported": yn(plot),
                "evidence_note": note,
            })
    assert n_ece == 0 and n_brier == 0 and n_rmse == 14 and n_nll == 1 and n_plot == 1

    # QA
    scores = {}
    for r in qa_rows:
        vec = tuple(int(r[c]) for c in [
            "QA1_task_clarity", "QA2_data_transparency", "QA3_split_control",
            "QA4_baseline_adequacy", "QA5_statistical_rigor",
            "QA6_author_artifacts_capped", "QA7_sparse_construct",
            "QA8_computational_reporting",
        ])
        scores[r["paper_id"]] = vec
    scores.update(NEW_QA)
    assert set(scores) == set(ids)

    item_counts = [[0, 0, 0] for _ in range(8)]
    norms = []
    tiers = {"HIGH": [], "MODERATE": [], "LIMITED": []}
    for pid in ids:
        vec = scores[pid]
        assert len(vec) == 8
        for i, v in enumerate(vec):
            assert v in (0, 1, 2)
            item_counts[i][v] += 1
        raw = sum(vec)
        norm = raw / 16
        norms.append(norm)
        tiers[tier(norm)].append(pid)
    mean_norm = sum(norms) / len(norms)

    n_drop = sum(pid in INTERACTION_DROP for pid in ids)
    n_item = sum(pid in ITEM_CS for pid in ids)
    n_learn = sum(pid in LEARNER_CS for pid in ids)
    n_kc = sum(pid in STRICT_KC for pid in ids)
    assert (n_drop, n_item, n_learn, n_kc) == (1, 1, 2, 0)

    lines = []
    a = lines.append
    a("# Expanded-corpus counts: sparse/cold-start, calibration, and QA")
    a("")
    a("Date: 2026-11-24. Corpus file: `data/PRIMARY_CORE_EXPANDED_2026-11-23.csv` (44 papers).")
    a("Denominator for every count below is 44, or the subset named in the sentence.")
    a("The live manuscript was not edited. Deposited 37-row tables were not overwritten.")
    a("Thresholds were not changed: HIGH is at least 0.80, MODERATE is 0.55 to 0.79, LIMITED is below 0.55. Normalized score is raw/16. QA6 is capped at 2.")
    a("")
    a("## A. Sparse and cold-start")
    a("")
    a("Codes follow the decision table. A sentence that only says cold start or sparsity is not YES. A random 80/20 or 6:2:2 split is not YES. An external graph is not strict KC cold-start. RMSE is not a cold-start code.")
    a("")
    a("| Construct | YES | Papers |")
    a("|---|---:|---|")
    a("| interaction_drop | 1 | KT086 HCMKT |")
    a("| item_cold_start | 1 | KT044 SINKT |")
    a("| learner_cold_start | 2 | KT023 SGKT; KT087 CoSKT |")
    a("| strict_KC_cold_start | 0 | none |")
    a("")
    a("HCMKT Figure 5 trains on 20%, 40%, and 60% of ASSISTments2009, ASSISTments2017, Junyi, and YMath and reports AUC, ACC, and RMSE at each rate. That is interaction-drop. It is not item, learner, or strict KC cold-start. The separate 6:2:2 split is the main evaluation split and is not a second YES.")
    a("")
    a("SINKT remains the item cold-start paper: a question hold-out scored as prediction for unseen questions. No second item hold-out was found.")
    a("")
    a("SGKT Section 5.5 builds eight training-sequence groups with intercepted lengths (0, 5] through (0, 100] and compares model performance on those groups. That is learner cold-start (truncated history, scored by length). It is not an interaction-drop and not a zero-exposure KC split.")
    a("")
    a("CoSKT Section IV-H and Figure 6 report performance for learning sequences shorter than 50, including length 5. That is a scored truncated-history condition, so learner cold-start is YES. The section title alone was not the code.")
    a("")
    a("HHSKT is NO on all four constructs. Its own protocol is 5-fold cross-validation with 60% training, 20% validation, and 20% testing (experiment section). The sentence about AUC declining until 50% of the data cites Lee (2019) as background for TrueSkill. It is not an HHSKT results-by-drop-level table. The printed claim that interaction-drop is YES for HHSKT does not meet the decision table.")
    a("")
    a("Also NO, after the PDF sentences were read: DyGKT discusses a difficulty assessment for unseen questions and does not report a withheld-item split. DGMN says the model can operate in cold-start scenarios and does not report a qualifying split. S2-HHN and AEGOT mention cold start as a problem property. DECKT's cold-start sentences cite other papers. KT-Deeper's 5/10/15/20/25% edge-removal ratios are a graph-generation probe (Precision@K, MAP), not an interaction-drop knowledge-tracing evaluation. PEBG's new-question wording is the next-question prediction task. KGNN-KT has an empty text layer; its four codes stay NO and were not re-read.")
    a("")
    a("Full coding:")
    a("")
    a("| paper_id | interaction_drop | item_cold_start | learner_cold_start | strict_KC_cold_start |")
    a("|---|---|---|---|---|")
    for pid in ids:
        a(
            f"| {pid} | {yn(pid in INTERACTION_DROP)} | {yn(pid in ITEM_CS)} | "
            f"{yn(pid in LEARNER_CS)} | {yn(pid in STRICT_KC)} |"
        )
    a("")
    a("## B. Calibration")
    a("")
    a("File: `tables/CALIBRATION_EXPANDED.csv` (44 rows).")
    a("")
    a("| Field | YES |")
    a("|---|---:|")
    a("| ECE_reported | 0 |")
    a("| Brier_reported | 0 |")
    a("| RMSE_reported | 14 |")
    a("| NLL_or_logloss_evaluation_reported | 1 |")
    a("| reliability_or_calibration_plot_reported | 1 |")
    a("")
    a("RMSE is an overall prediction error. It is not counted as calibration. The 14 RMSE papers are KT014, KT035, KT037, KT039, KT040, KT042, KT056, KT063, KT065, KT066, KT068, KT070, KT077, and KT086. HCMKT reports RMSE in Table 4 and Figure 5. DTransformer reports MAE and RMSE in Table 2.")
    a("")
    a("The one reliability plot is CL4KT (KT039), Figure 7, binned by predictions, with no ECE or Brier summary.")
    a("")
    a("DECKT Figure 4 is not a reliability plot. The body says the heatmap shows predictive calibration. The caption is Prediction visualization analysis of one student's predicted probabilities. ECE and Brier are not reported.")
    a("")
    a("The one evaluation NLL is KT-Deeper Table 5: an NLL gap between training and test data for the graph-generation model. It is not ECE, not Brier, and not a next-response calibration score. Training-loss NLL in GKT, JKT, HHSKT, the capsule model, HyperKT, and SKM-GKT is coded NO for the evaluation column.")
    a("")
    a("KGNN-KT (KT076) has an empty text layer. Its five calibration fields are NO and are not a fresh keyword hit.")
    a("")
    a("## C. QA")
    a("")
    a("The 37 deposited scores were not changed. QA1-QA8 were coded for the seven papers that are outside that file. QA6 = 0 when no author artifact was found. The EdNet dataset repository is not an author artifact. Author repositories found in the papers: CoSKT `https://github.com/lucky7-code/CoSKT`; DTransformer `https://github.com/yxonic/DTransformer`.")
    a("")
    a("| paper_id | model | QA1 | QA2 | QA3 | QA4 | QA5 | QA6 | QA7 | QA8 | raw | norm | tier |")
    a("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|")
    labels = {
        "KT084": "DECKT",
        "KT085": "KT-Deeper",
        "KT086": "HCMKT",
        "KT087": "CoSKT",
        "KT040": "DTransformer",
        "KT088": "SP-CLKT",
        "KT089": "CLBG",
    }
    for pid in ["KT084", "KT085", "KT086", "KT087", "KT040", "KT088", "KT089"]:
        vec = NEW_QA[pid]
        raw = sum(vec)
        norm = raw / 16
        cells = " | ".join(str(v) for v in vec)
        a(f"| {pid} | {labels[pid]} | {cells} | {raw} | {norm:.4f} | {tier(norm)} |")
    a("")
    a("QA3 is 1 for DECKT, SP-CLKT, and CLBG because a validation procedure or implementation section is present and a train/test ratio is not stated. QA3 is 2 where the paper states 5-fold cross-validation (KT-Deeper), a 6:2:2 split (HCMKT), an 80/20 split (CoSKT), or an 80/20 student split (DTransformer).")
    a("")
    a("QA7 is 2 only when one of the four cold-start constructs is an evaluation: HCMKT (interaction-drop) and CoSKT (learner cold-start). The other five new papers are 0.")
    a("")
    a("QA8 is 2 when the paper reports a GPU model or a complexity formula (DECKT A100 and complexity; KT-Deeper Tesla K80; DTransformer TITAN V100). QA8 is 1 when implementation settings are reported without a GPU model or complexity formula (HCMKT, CoSKT, SP-CLKT, CLBG).")
    a("")
    a("### Item distribution on 44 papers")
    a("")
    a("| Item | 0 | 1 | 2 |")
    a("|---|---:|---:|---:|")
    for name, counts in zip(QA_NAMES, item_counts):
        a(f"| {name} | {counts[0]} | {counts[1]} | {counts[2]} |")
    a("")
    a("### Tiers on 44 papers")
    a("")
    a(f"- HIGH: {len(tiers['HIGH'])}")
    a(f"- MODERATE: {len(tiers['MODERATE'])}")
    a(f"- LIMITED: {len(tiers['LIMITED'])}")
    a(f"- Corpus mean of normalized scores: {mean_norm:.4f}")
    a("")
    a("HIGH paper codes: " + ", ".join(tiers["HIGH"]) + ".")
    a("")
    a("Two new HIGH papers are KT040 (raw 13, 0.8125) and KT087 (raw 14, 0.8750). The other five new papers are MODERATE. LIMITED stays empty.")
    a("")
    a("The deposited QA7 scores for the original 37 were not recomputed. HHSKT remains QA7 = 2 in that file even though its cold-start fields are now all NO. SGKT remains QA7 = 0 in that file even though learner cold-start is now YES. Those two QA7 cells are a carry-forward, not a new adjudication.")
    a("")
    a("## Manuscript statistics that must change")
    a("")
    a("These are printed analysis denominators and claims. This file does not edit the manuscript. Search-log identification is separate: `N_rec = 2,017` and the PRISMA stage arithmetic are not replaced by the 44-paper coding, because this pass does not show that the seven added papers were inside the original identification set.")
    a("")
    a("| Printed statistic | Where it is used | Expanded result |")
    a("|---|---|---|")
    a("| Surveys 37 primary-core PDFs | Abstract; highlights; corpus section | 44 primary-core papers |")
    a("| `N_G = 36` (97.3%); only CL4KT is sequence-only inside that coding | Abstract; taxonomy; Graph-KT section | `N_G = 40`. Sequence-only SSL papers in the 44: KT039, KT040, KT087, KT088 |")
    a("| `N_S = 9` | Abstract; SSL section | `N_S = 16` |")
    a("| `N_{G cap S} = 8`; four exclusive pretext families; SSL table of 9 | Abstract; SSL table caption | `N_{G cap S} = 12`. The four-family table does not cover the expanded SSL set (15 contrastive, 1 generative reconstruction; view source is a second axis) |")
    a("| Provenance 19 / 8 / 9 among 36 graph papers | Taxonomy caption | Among 40 graph papers: model-defined fixed 24, external fixed 7, dynamically learned 8, unclear 1 (KT085). This provenance tally is not locked |")
    a("| Interaction-drop YES 1/37 (HHSKT) | Cold-start table and body; go/no-go row | 1/44, and the paper is HCMKT (KT086), not HHSKT |")
    a("| Strict KC cold-start 0/37 | Abstract-level claims; cold-start table; go/no-go | 0/44 |")
    a("| Item cold-start YES 1/37 (SINKT) | Cold-start table; go/no-go | 1/44 (KT044 SINKT) |")
    a("| Learner cold-start YES 0/37 | Cold-start table and body | 2/44 (KT023 SGKT, KT087 CoSKT) |")
    a("| ECE 0/37 | Abstract comparison table; ECE audit; go/no-go | 0/44 |")
    a("| Brier 0/36 scanned text layers | ECE audit; go/no-go | 0/44 |")
    a("| RMSE in 12 of 37, as prediction error | ECE audit; go/no-go | 14/44. Added HCMKT and DTransformer. Still not calibration |")
    a("| One calibration plot (CL4KT); no evaluation-time NLL | ECE audit | Reliability plot 1/44 (KT039). Evaluation NLL 1/44 (KT085 graph-generation NLL gap, not response calibration) |")
    a("| None of the seven report ECE, Brier, or a zero-exposure KC split, and they are outside the tables | Gateway extension paragraph | ECE, Brier, and strict KC remain zero after they are included. The sentence that they are outside the coding tables does not survive a 44-row rewrite |")
    a("| QA HIGH 11, MODERATE 26, LIMITED 0, mean 0.76 | QA section | HIGH 13, MODERATE 31, LIMITED 0, mean " + f"{mean_norm:.4f} |")
    a("| QA item counts on 37: QA1 0/0/37, QA2 0/0/37, QA3 0/6/31, QA4 0/0/37, QA5 0/37/0, QA6 0/26/11, QA7 35/0/2, QA8 0/5/32 | QA distribution table | See the 44-paper item table above. QA1, QA2, QA4, and QA5 stay uniform. QA3, QA6, QA7, and QA8 change |")
    a("| QA7 is 2 only for HHSKT and SINKT | QA distribution paragraph | On the 44-paper score, QA7 is 2 for KT035, KT044, KT086, and KT087. KT035 is carried from the deposited file |")
    a("| QA7-not-applicable sensitivity: 31 HIGH, 6 MODERATE, mean 0.86, and only HHSKT and SINKT make a sparse claim | Sensitivity paragraph | That paragraph is a 37-paper sensitivity. It is not the expanded primary score, and its premise (only two papers make a sparse/cold-start claim) is no longer true |")
    a("| Graph-KT coding tables of 18 + 18 = 36, and SSL augmentation table of 9 | Table captions | Row counts become 40 graph papers and 16 SSL papers |")
    a("")
    a("Check that still holds from the expanded gateway file, and that this pass did not change: `N_G + N_S - N_{G cap S} = 40 + 16 - 12 = 44`.")
    a("")
    a("Not changed by this pass, and not to be rewritten as a 44-paper identification total: search-log `N_rec = 2,017`, and the PRISMA-style stage counts that end at 37.")
    a("")
    AUDIT_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("papers", len(ids))
    print("mean", round(mean_norm, 4))
    print("tiers", {k: len(v) for k, v in tiers.items()})
    print("HIGH", ",".join(tiers["HIGH"]))
    print("items")
    for name, counts in zip(QA_NAMES, item_counts):
        print(name, counts)


if __name__ == "__main__":
    main()
