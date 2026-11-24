# -*- coding: utf-8 -*-
"""Build the expanded primary-core file from deposited 37-paper rows plus seven PDF-coded papers.

Does not edit the manuscript, the blind screening sheet, or the deposited 37-paper tables.
"""
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
INV = ROOT / "12_manuscript/TLT/supplementary/supplementary_corpus_inventory.csv"
SSL = ROOT / "12_manuscript/TLT/supplementary/supplementary_ssl_taxonomy_Ns9.csv"
QA = ROOT / "12_manuscript/TLT/supplementary/supplementary_quality_scores.csv"
OUT_DIR = ROOT / "data"
OUT = OUT_DIR / "PRIMARY_CORE_EXPANDED_2026-11-23.csv"
EVID = OUT_DIR / "PRIMARY_CORE_EXPANDED_2026-11-23_FIELD_EVIDENCE.csv"

RMSE_YES = {
    "KT037", "KT039", "KT070", "KT047", "KT056", "KT065",
    "KT035", "KT068", "KT063", "KT014", "KT077", "KT042",
}

COLS = [
    "paper_id", "ext_id", "row_origin", "title", "year", "doi", "corpus_tier",
    "kt_central_task", "G_criterion", "S_criterion", "graph_source", "graph_provenance",
    "graph_nodes", "encoder", "temporal_backbone", "fusion", "ssl_paradigm",
    "ssl_view_source", "ssl_pretext_or_consistency_target", "augmentation",
    "augmentation_structure_constraint", "interaction_drop", "item_cold_start",
    "learner_cold_start", "strict_KC_cold_start", "ECE_reported", "Brier_reported",
    "RMSE_reported", "calibration_plot_reported", "QA1", "QA2", "QA3", "QA4", "QA5",
    "QA6", "QA7", "QA8", "evidence_locator", "evidence_note",
]


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def join_unique(values):
    out = []
    for v in values:
        if v not in out:
            out.append(v)
    return "|".join(out)


def base_paper_id(raw):
    return raw.split("_", 1)[0]


inv_rows = read_csv(INV)
ssl_rows = {r["paper_id"]: r for r in read_csv(SSL)}
qa_rows = {r["paper_id"]: r for r in read_csv(QA)}

grouped = {}
order = []
for r in inv_rows:
    pid = base_paper_id(r["paper_id"])
    if pid not in grouped:
        grouped[pid] = []
        order.append(pid)
    grouped[pid].append(r)

old = []
for pid in order:
    rows = grouped[pid]
    g_sources = [r["graph_source"] for r in rows]
    g_yes = any(s != "NONE" for s in g_sources)
    s_row = ssl_rows.get(pid)
    s_yes = s_row is not None and s_row.get("S_criterion") == "Y"
    qa = qa_rows.get(pid, {})
    venue_year = rows[0]["venue_year"]
    year = venue_year.split()[-1]
    old.append({
        "paper_id": pid,
        "ext_id": "",
        "row_origin": "DEPOSITED_37",
        "title": join_unique(r["model_entry"] for r in rows),
        "year": year,
        "doi": "NR",
        "corpus_tier": "PRIMARY_CORE",
        "kt_central_task": "YES",
        "G_criterion": "YES" if g_yes else "NO",
        "S_criterion": "YES" if s_yes else "NO",
        "graph_source": join_unique(g_sources),
        "graph_provenance": join_unique(r["graph_provenance"] for r in rows),
        "graph_nodes": join_unique(r["graph_representation"] for r in rows),
        "encoder": join_unique(r["gnn_encoder"] for r in rows),
        "temporal_backbone": join_unique(r["temporal_backbone"] for r in rows),
        "fusion": join_unique(r["fusion_type"] for r in rows),
        "ssl_paradigm": s_row["ssl_family"] if s_row else "NONE",
        "ssl_view_source": s_row["target_level"] if s_row else "NA",
        "ssl_pretext_or_consistency_target": s_row["mechanism_note"] if s_row else "NA",
        "augmentation": s_row["augmentation_strategy"] if s_row else "NA",
        "augmentation_structure_constraint": s_row["educational_structure_preservation"] if s_row else "NA",
        "interaction_drop": "YES" if pid == "KT035" else "NO",
        "item_cold_start": "YES" if pid == "KT044" else "NO",
        "learner_cold_start": "NO",
        "strict_KC_cold_start": "NO",
        "ECE_reported": "NO",
        "Brier_reported": "NO",
        "RMSE_reported": "YES" if pid in RMSE_YES else "NO",
        "calibration_plot_reported": "YES" if pid == "KT039" else "NO",
        "QA1": qa.get("QA1_task_clarity", "NR"),
        "QA2": qa.get("QA2_data_transparency", "NR"),
        "QA3": qa.get("QA3_split_control", "NR"),
        "QA4": qa.get("QA4_baseline_adequacy", "NR"),
        "QA5": qa.get("QA5_statistical_rigor", "NR"),
        "QA6": qa.get("QA6_author_artifacts_capped", "NR"),
        "QA7": qa.get("QA7_sparse_construct", "NR"),
        "QA8": qa.get("QA8_computational_reporting", "NR"),
        "evidence_locator": "12_manuscript/TLT/supplementary/supplementary_corpus_inventory.csv; supplementary_ssl_taxonomy_Ns9.csv; supplementary_quality_scores.csv; calibration_rmse_textlayer_v1.10.csv",
        "evidence_note": "Deposited 37-paper row carried forward. Not re-read from the PDF in this expansion. Cold-start flags follow the deposited itemized claims: strict KC NO, item cold-start YES only for KT044, interaction-drop YES only for KT035.",
    })

NEW = [
    {
        "paper_id": "KT084", "ext_id": "EXT01", "row_origin": "PDF_CODED_2026-11-23",
        "title": "A Dual-Encoder Contrastive Learning Model for Knowledge Tracing",
        "year": "2025", "doi": "10.3390/e27070685", "corpus_tier": "PRIMARY_CORE",
        "kt_central_task": "YES", "G_criterion": "YES", "S_criterion": "YES",
        "graph_source": "Q_MATRIX", "graph_provenance": "PRECOMPUTED_UNCLEAR_SPLIT",
        "graph_nodes": "ITEM_KC_BIPARTITE", "encoder": "GAT",
        "temporal_backbone": "RNN_LSTM_GRU", "fusion": "GRAPH_INITIALIZATION",
        "ssl_paradigm": "GRAPH_CONTRASTIVE",
        "ssl_view_source": "PRIMARY_VS_MOMENTUM_ENCODER",
        "ssl_pretext_or_consistency_target": "InfoNCE between primary-encoder and momentum-encoder embeddings of the same question node and the same concept node; plus a graph-structure constraint on connected question-concept pairs",
        "augmentation": "NO_EXPLICIT_AUGMENTATION",
        "augmentation_structure_constraint": "YES_EXPLICIT",
        "interaction_drop": "NO", "item_cold_start": "NO", "learner_cold_start": "NO",
        "strict_KC_cold_start": "NO", "ECE_reported": "NO", "Brier_reported": "NO",
        "RMSE_reported": "NO", "calibration_plot_reported": "NO",
        "QA1": "UNCLEAR", "QA2": "UNCLEAR", "QA3": "UNCLEAR", "QA4": "UNCLEAR",
        "QA5": "UNCLEAR", "QA6": "UNCLEAR", "QA7": "UNCLEAR", "QA8": "UNCLEAR",
        "evidence_locator": "audit/_a1_evidence/DECKT_fulltext_PMC12294018.txt Sec 3.1; Sec 3.2; Sec 3.3; Sec 3.3.1; Sec 3.4; Sec 3.5; Figure 4",
        "evidence_note": "Sec 3.1 builds bipartite G=(V,E) from question-concept adjacency A and predicts r_{T+1}. Sec 3.3.1 uses multi-layer GAT. Sec 3.4 uses LSTM. Sec 3.2 feeds the learned representations into the sequence module. Contrastive views come from the intact graph, not edge deletion or feature masking. A later adversarial perturbation stage is stated and is not coded as the contrastive augmentation. Figure 4 is a prediction heatmap described as predictive calibration; it is not a reliability diagram and reports no ECE or Brier. No RMSE string in the extract. Cold-start strings in the extract are citations of other papers. ssl_view_source is a description, not a locked codebook token.",
    },
    {
        "paper_id": "KT085", "ext_id": "EXT02", "row_origin": "PDF_CODED_2026-11-23",
        "title": "Dynamic Heterogeneous Graph Contrastive Networks for Knowledge Tracing",
        "year": "2024", "doi": "10.1016/j.asoc.2024.112194", "corpus_tier": "PRIMARY_CORE",
        "kt_central_task": "YES", "G_criterion": "YES", "S_criterion": "YES",
        "graph_source": "HYBRID_MULTI_SOURCE", "graph_provenance": "UNCLEAR",
        "graph_nodes": "HETEROGENEOUS_MULTI_NODE", "encoder": "GCN",
        "temporal_backbone": "RNN_LSTM_GRU", "fusion": "UNCLEAR",
        "ssl_paradigm": "GRAPH_CONTRASTIVE",
        "ssl_view_source": "NODE_EMBEDDING_VS_GRAPH_SUMMARY",
        "ssl_pretext_or_consistency_target": "Mutual information between a node embedding and the graph embedding, with corrupted negatives",
        "augmentation": "UNCLEAR",
        "augmentation_structure_constraint": "UNCLEAR",
        "interaction_drop": "NO", "item_cold_start": "NO", "learner_cold_start": "NO",
        "strict_KC_cold_start": "NO", "ECE_reported": "NO", "Brier_reported": "NO",
        "RMSE_reported": "NO", "calibration_plot_reported": "NO",
        "QA1": "UNCLEAR", "QA2": "UNCLEAR", "QA3": "UNCLEAR", "QA4": "UNCLEAR",
        "QA5": "UNCLEAR", "QA6": "UNCLEAR", "QA7": "UNCLEAR", "QA8": "UNCLEAR",
        "evidence_locator": "audit/_a1_evidence/Han2024_fulltext_2026-11-22.txt abstract; Definition 1-2; Sec 4.2; Sec 4.2.1; Sec 4.3; experiment metrics AUROC and Recall",
        "evidence_note": "Model name in the paper is KT-Deeper. Definition 1 defines a temporal heterogeneous graph over students, exercises, and skills. Sec 4.2.1 trains a two-layer GCN. Sec 4.2 maximizes mutual information against corrupted negatives. Sec 4.3 uses LSTM. The extract does not state that the adjacency matrices were fit on the training split only, and Sec 4.1 generates missing future snapshots, so provenance stays UNCLEAR. The corruption operator is not named, so augmentation stays UNCLEAR. No RMSE, ECE, or Brier string in the extract. Comparison metrics named are AUROC and Recall.",
    },
    {
        "paper_id": "KT086", "ext_id": "EXT03", "row_origin": "PDF_CODED_2026-11-23",
        "title": "Heterogeneous Graph Knowledge Tracing with Novel Contrastive View and Meta-Path Contexts",
        "year": "2026", "doi": "10.1016/j.eswa.2025.128840", "corpus_tier": "PRIMARY_CORE",
        "kt_central_task": "YES", "G_criterion": "YES", "S_criterion": "YES",
        "graph_source": "HYBRID_MULTI_SOURCE", "graph_provenance": "PRECOMPUTED_UNCLEAR_SPLIT",
        "graph_nodes": "HETEROGENEOUS_MULTI_NODE", "encoder": "GCN",
        "temporal_backbone": "RNN_LSTM_GRU", "fusion": "UNCLEAR",
        "ssl_paradigm": "MULTIVIEW_CONTRASTIVE",
        "ssl_view_source": "COARSE_VIEW_VS_FINE_VIEW",
        "ssl_pretext_or_consistency_target": "Contrastive loss between coarse-view and fine-grained-view embeddings of the same question, plus a prototype contrastive loss",
        "augmentation": "EDGE_DROP",
        "augmentation_structure_constraint": "UNCLEAR",
        "interaction_drop": "NO", "item_cold_start": "NO", "learner_cold_start": "NO",
        "strict_KC_cold_start": "NO", "ECE_reported": "NO", "Brier_reported": "NO",
        "RMSE_reported": "YES", "calibration_plot_reported": "NO",
        "QA1": "UNCLEAR", "QA2": "UNCLEAR", "QA3": "UNCLEAR", "QA4": "UNCLEAR",
        "QA5": "UNCLEAR", "QA6": "UNCLEAR", "QA7": "UNCLEAR", "QA8": "UNCLEAR",
        "evidence_locator": "audit/_a1_evidence/HCMKT_fulltext_2026-11-22.txt abstract; Definition 1-3; Sec 4.1 Eqs (3)-(6); Sec 4.2; Sec 4.4 Eqs (15)-(16); Table 4",
        "evidence_note": "Definition 1 predicts the next answer. Definition 2 is a heterogeneous information network and Definition 3 instantiates meta-path Qu-Sk-Qu. Two-layer GCNs encode coarse and fine views. Those representations are input into an LSTM. The combination operator is not named, so fusion stays UNCLEAR. The extract states feature masking and edge masking. Edge masking is coded EDGE_DROP. Feature masking has no locked augmentation token and is not coded as NODE_MASK. The extract does not state that this masking preserves prerequisite structure. Table 4 reports AUC, ACC, and RMSE. No ECE or Brier string. A 20/40/60 percent training-rate comparison is reduced data, not a zero-exposure KC split. The network is not stated to be built from the training split only.",
    },
    {
        "paper_id": "KT087", "ext_id": "EXT04", "row_origin": "PDF_CODED_2026-11-23",
        "title": "CoSKT: A Collaborative Self-Supervised Learning Method for Knowledge Tracing",
        "year": "2024", "doi": "10.1109/TLT.2024.3386750", "corpus_tier": "PRIMARY_CORE",
        "kt_central_task": "YES", "G_criterion": "NO", "S_criterion": "YES",
        "graph_source": "NONE", "graph_provenance": "NA",
        "graph_nodes": "NONE", "encoder": "NONE",
        "temporal_backbone": "RNN_LSTM_GRU", "fusion": "GATE",
        "ssl_paradigm": "SEQUENCE_CONTRASTIVE",
        "ssl_view_source": "INDIVIDUAL_STATE_VS_SIMILAR_STUDENT_STATE",
        "ssl_pretext_or_consistency_target": "InfoNCE between the target student's individual knowledge state and the common knowledge state of similar students",
        "augmentation": "NO_EXPLICIT_AUGMENTATION",
        "augmentation_structure_constraint": "NO_AUGMENTATION",
        "interaction_drop": "NO", "item_cold_start": "NO", "learner_cold_start": "NO",
        "strict_KC_cold_start": "NO", "ECE_reported": "NO", "Brier_reported": "NO",
        "RMSE_reported": "NO", "calibration_plot_reported": "NO",
        "QA1": "UNCLEAR", "QA2": "UNCLEAR", "QA3": "UNCLEAR", "QA4": "UNCLEAR",
        "QA5": "UNCLEAR", "QA6": "UNCLEAR", "QA7": "UNCLEAR", "QA8": "UNCLEAR",
        "evidence_locator": "audit/_a1_evidence/CoSKT_fulltext_2026-11-22.txt p.1; Sec III-A; Sec III-D Eq (13); Sec IV metrics; Sec IV-H p.11",
        "evidence_note": "Graph, GCN, and bipartite wording in this PDF is in the related-work discussion of other models. The model is an LSTM over the student's sequence, attention over similar students, and a gate. Sec IV names AUC and ACC. No RMSE, ECE, or Brier string in the extract. Sec IV-H discusses cold start as few similar students and sequence length below 50. That discussion is not a zero-exposure KC split, an item hold-out, or a learner hold-out. Author code URL is printed: https://github.com/lucky7-code/CoSKT. QA6 is not scored because the 0/1/2 cut is not defined in the locked codebook.",
    },
    {
        "paper_id": "KT040", "ext_id": "EXT05", "row_origin": "PDF_CODED_2026-11-23",
        "title": "Tracing Knowledge Instead of Patterns: Stable Knowledge Tracing with Diagnostic Transformer",
        "year": "2023", "doi": "10.1145/3543507.3583255", "corpus_tier": "PRIMARY_CORE",
        "kt_central_task": "YES", "G_criterion": "NO", "S_criterion": "YES",
        "graph_source": "NONE", "graph_provenance": "NA",
        "graph_nodes": "NONE", "encoder": "NONE",
        "temporal_backbone": "SELF_ATTENTION_TRANSFORMER", "fusion": "NONE",
        "ssl_paradigm": "SEQUENCE_CONTRASTIVE",
        "ssl_view_source": "TWO_AUGMENTED_SEQUENCES_OF_THE_SAME_LEARNER",
        "ssl_pretext_or_consistency_target": "Contrastive loss so knowledge states from two augmented sequences of the same learner stay close",
        "augmentation": "INTERACTION_REPLACE|INTERACTION_CROP|INTERACTION_REORDER",
        "augmentation_structure_constraint": "NO_EXPLICIT_CONSTRAINT",
        "interaction_drop": "NO", "item_cold_start": "NO", "learner_cold_start": "NO",
        "strict_KC_cold_start": "NO", "ECE_reported": "NO", "Brier_reported": "NO",
        "RMSE_reported": "YES", "calibration_plot_reported": "NO",
        "QA1": "UNCLEAR", "QA2": "UNCLEAR", "QA3": "UNCLEAR", "QA4": "UNCLEAR",
        "QA5": "UNCLEAR", "QA6": "UNCLEAR", "QA7": "UNCLEAR", "QA8": "UNCLEAR",
        "evidence_locator": "audit/_a1_evidence/DTransformer_fulltext_yin2023.txt abstract; Sec 3.3.1 Eq (17); Eq (20)-(22); RMSE rows in the result tables",
        "evidence_note": "Existing inventory ID KT040 is reused. The seed file still labels KT040 BACKGROUND; this expanded file does not edit that seed file. Graph sentences in the PDF cite other papers. Sec 3.3.1 augments a sequence by flipping a response, dropping an item, and swapping adjacent items. Dropping an item is an augmentation, not an interaction-drop evaluation. Result tables report RMSE beside the other prediction metrics. No ECE or Brier string. Author code URL is printed: https://github.com/yxonic/DTransformer. The internal prediction head uses concatenation; fusion here is the graph-fusion field and is NONE because no graph is coded.",
    },
    {
        "paper_id": "KT088", "ext_id": "EXT06", "row_origin": "PDF_CODED_2026-11-23",
        "title": "Self-paced contrastive learning for knowledge tracing",
        "year": "2024", "doi": "10.1016/j.neucom.2024.128366", "corpus_tier": "PRIMARY_CORE",
        "kt_central_task": "YES", "G_criterion": "NO", "S_criterion": "YES",
        "graph_source": "NONE", "graph_provenance": "NA",
        "graph_nodes": "NONE", "encoder": "NONE",
        "temporal_backbone": "RNN_LSTM_GRU", "fusion": "NONE",
        "ssl_paradigm": "SEQUENCE_CONTRASTIVE",
        "ssl_view_source": "LOCAL_AND_GLOBAL_SEQUENCE_SAMPLES",
        "ssl_pretext_or_consistency_target": "Contrastive loss on student answer sequences balancing local and global samples",
        "augmentation": "INTERACTION_REPLACE|INTERACTION_REORDER",
        "augmentation_structure_constraint": "YES_EXPLICIT",
        "interaction_drop": "NO", "item_cold_start": "NO", "learner_cold_start": "NO",
        "strict_KC_cold_start": "NO", "ECE_reported": "NO", "Brier_reported": "NO",
        "RMSE_reported": "NO", "calibration_plot_reported": "NO",
        "QA1": "UNCLEAR", "QA2": "UNCLEAR", "QA3": "UNCLEAR", "QA4": "UNCLEAR",
        "QA5": "UNCLEAR", "QA6": "UNCLEAR", "QA7": "UNCLEAR", "QA8": "UNCLEAR",
        "evidence_locator": "audit/_a1_evidence/SPCLKT_fulltext_2026-11-22.txt abstract; Sec 3.3; Sec 3.4 Eq (7)-(8)",
        "evidence_note": "Sec 3.3 says a chain-like directed acyclic graph is assumed for simplicity, then implements a difficulty order ranked by the training-set probability of a correct answer. That order chooses replacement questions. The paper does not construct an adjacency matrix or run a graph encoder, so G_criterion stays NO. This is a boundary: the word graph appears as that assumption. Sec 3.3 says the replacement maintains the student's mastery and overall knowledge level. Sec 3.4 is the contrastive objective. The extract has no RMSE, ECE, or Brier string. Sparse student-skill interactions are the paper's sparsity claim and are not a zero-exposure KC split.",
    },
    {
        "paper_id": "KT089", "ext_id": "EXT07", "row_origin": "PDF_CODED_2026-11-23",
        "title": "Contrastive Learning Based on Bipartite Graphs for Interpretable Knowledge Tracing",
        "year": "2025", "doi": "10.1007/978-981-96-0821-8_14", "corpus_tier": "PRIMARY_CORE",
        "kt_central_task": "YES", "G_criterion": "YES", "S_criterion": "YES",
        "graph_source": "HYBRID_MULTI_SOURCE", "graph_provenance": "PRECOMPUTED_UNCLEAR_SPLIT",
        "graph_nodes": "ITEM_KC_BIPARTITE", "encoder": "GAT",
        "temporal_backbone": "RNN_LSTM_GRU", "fusion": "GRAPH_INITIALIZATION",
        "ssl_paradigm": "GRAPH_CONTRASTIVE",
        "ssl_view_source": "ORIGINAL_GRAPH_VS_EDGE_AUGMENTED_GRAPH",
        "ssl_pretext_or_consistency_target": "InfoNCE-style loss between a node and the same node in the edge-augmented graph, summed over G1, G2, and G3",
        "augmentation": "EDGE_ADD|EDGE_DROP",
        "augmentation_structure_constraint": "NO_EXPLICIT_CONSTRAINT",
        "interaction_drop": "NO", "item_cold_start": "NO", "learner_cold_start": "NO",
        "strict_KC_cold_start": "NO", "ECE_reported": "NO", "Brier_reported": "NO",
        "RMSE_reported": "NO", "calibration_plot_reported": "NO",
        "QA1": "UNCLEAR", "QA2": "UNCLEAR", "QA3": "UNCLEAR", "QA4": "UNCLEAR",
        "QA5": "UNCLEAR", "QA6": "UNCLEAR", "QA7": "UNCLEAR", "QA8": "UNCLEAR",
        "evidence_locator": "audit/_a1_evidence/BipartiteKT_fulltext_2026-11-23.txt Sec 3.1; Sec 3.3; Sec 3.4; Sec 3.5; Sec 4",
        "evidence_note": "Sec 3.3 defines exercise-concept bipartite graph G1 plus exercise correlation graph G2 and concept correlation graph G3. graph_nodes records the prediction graph G1. G2 and G3 are same-type correlation graphs; their edge rule is stated only as whether related. Sec 3.4 uses a bipartite graph attention network on G1 and passes exercise vectors to the LSTM predictor. Sec 3.5 randomly adds or deletes edges with probability p, then applies an InfoNCE-style loss. The extract does not state that this augmentation preserves prerequisite structure. Sec 4 reports AUC and ACC. No ECE, Brier, or RMSE string in the extract. The graphs are not stated to be built from the training split only.",
    },
]

# Field-level evidence for the seven papers, one row per nontrivial field.
fields_for_evidence = [
    "kt_central_task", "G_criterion", "S_criterion", "graph_source", "graph_provenance",
    "graph_nodes", "encoder", "temporal_backbone", "fusion", "ssl_paradigm",
    "ssl_view_source", "ssl_pretext_or_consistency_target", "augmentation",
    "augmentation_structure_constraint", "interaction_drop", "item_cold_start",
    "learner_cold_start", "strict_KC_cold_start", "ECE_reported", "Brier_reported",
    "RMSE_reported", "calibration_plot_reported", "QA1",
]
evid_rows = []
for rec in NEW:
    for field in fields_for_evidence:
        evid_rows.append({
            "paper_id": rec["paper_id"],
            "field_name": field,
            "coded_value": rec[field],
            "coding_basis": "PDF_TEXT" if not str(rec[field]).startswith("UNCLEAR") else "PDF_TEXT_INSUFFICIENT",
            "evidence_locator": rec["evidence_locator"],
            "evidence_note": rec["evidence_note"],
            "source": "14_references PDF text layer extracted to the locator file",
        })

rows = old + NEW
assert len(old) == 37, len(old)
assert len(rows) == 44, len(rows)
ids = [r["paper_id"] for r in rows]
assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]

OUT_DIR.mkdir(exist_ok=True)
with OUT.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=COLS, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
with EVID.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["paper_id", "field_name", "coded_value", "coding_basis", "evidence_locator", "evidence_note", "source"],
        lineterminator="\n",
    )
    w.writeheader()
    w.writerows(evid_rows)


def yes(rows_, field):
    return sum(1 for r in rows_ if r[field] == "YES")


def both(rows_):
    return sum(1 for r in rows_ if r["G_criterion"] == "YES" and r["S_criterion"] == "YES")


n = len(rows)
ng = yes(rows, "G_criterion")
ns = yes(rows, "S_criterion")
ngs = both(rows)
old_n = len(old)
old_ng = yes(old, "G_criterion")
old_ns = yes(old, "S_criterion")
old_ngs = both(old)
check = ng + ns - ngs

print("OLD", old_n, old_ng, old_ns, old_ngs)
print("NEW", n, ng, ns, ngs)
print("CHECK", check, "equals N" if check == n else "DISCREPANCY")
print("STRICT", yes(rows, "strict_KC_cold_start"))
print("ITEM", yes(rows, "item_cold_start"))
print("LEARNER", yes(rows, "learner_cold_start"))
print("DROP", yes(rows, "interaction_drop"))
print("ECE", yes(rows, "ECE_reported"))
print("BRIER", yes(rows, "Brier_reported"))
print("RMSE", yes(rows, "RMSE_reported"))
print("CALPLOT", yes(rows, "calibration_plot_reported"))
print("PROVENANCE_NEW")
for rec in NEW:
    if rec["G_criterion"] == "YES":
        print(rec["paper_id"], rec["graph_provenance"], rec["encoder"], rec["ssl_paradigm"])
print("QA_UNCLEAR", sum(1 for r in NEW if r["QA1"] == "UNCLEAR"))
print("QA_OLD_HIGH", sum(1 for r in old if qa_rows.get(r["paper_id"], {}).get("quality_tier") == "HIGH"))
print("QA_OLD_MOD", sum(1 for r in old if qa_rows.get(r["paper_id"], {}).get("quality_tier") == "MODERATE"))
print("QA_MISSING", [r["paper_id"] for r in old if r["paper_id"] not in qa_rows])
print("QA_EXTRA", sorted(set(qa_rows) - set(order)))
print("SEQ_ONLY", [r["paper_id"] for r in rows if r["G_criterion"] == "NO" and r["S_criterion"] == "YES"])
print("PROV", Counter(r["graph_provenance"] for r in rows if r["G_criterion"] == "YES"))
print("ENC", Counter(r["encoder"] for r in rows if r["G_criterion"] == "YES"))
print("SSL", Counter(r["ssl_paradigm"] for r in rows if r["S_criterion"] == "YES"))
