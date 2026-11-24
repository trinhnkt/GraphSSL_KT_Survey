# Han et al. 2024 and HCMKT — full-text screen 2026-11-22

Both PDFs are the publisher articles in `14_references`. Both decisions are `INCLUDE_PRIMARY_CORE`. Neither paper is in the printed 37. CoSKT is unchanged: its PDF is not in `14_references`, and `audit/A1_THREE_SCREEN_2026-11-22.md` still marks it `FULLTEXT_REQUIRED`.

## A1-C04 Han et al. 2024 — INCLUDE_PRIMARY_CORE

**Identity.** Yehong Han, Hailiang Tang, Wenxiao Zhang, Lin Du, Jun Zhao, and Minglai Shao. “Dynamic heterogeneous graph contrastive networks for knowledge tracing.” Applied Soft Computing 166 (2024) 112194. DOI 10.1016/j.asoc.2024.112194, printed on p. 1. Available online 5 September 2024. The PDF author is Jun Zhao. Inside the search window. Model name in the paper: KT-Deeper. Text: `audit/_a1_evidence/Han2024_fulltext_2026-11-22.txt`.

**KT.** Yes. Definition 2, p. 4, defines the task as predicting student–skill relations at time \(t+n\) from the graph sequence. A new student–skill edge means the student will master that skill. This is sequential learner-state estimation.

**G-criterion.** Yes. Definition 1, p. 4, defines a temporal heterogeneous graph \(\mathcal{G}_t=(V_t,E_t)\) over students, exercises, and skills. The same page constructs five adjacency matrices, including skill–exercise, exercise–skill, student–exercise, student–skill, and skill–skill. Section 4.2.1, Eqs. (6)–(7), runs a two-layer GCN on meta-path graphs. `graph_source=HYBRID_MULTI_SOURCE`. `gnn_encoder=GCN`. The text does not say these matrices are fit on the training split only, and Section 4.1 generates missing future snapshots by reinforcement learning. `graph_provenance=UNCLEAR`.

**S-criterion.** Yes. Section 4.2, Eq. (4), maximizes mutual information between a node embedding and the graph embedding and subtracts the same term on corrupted negatives. The abstract calls this a self-supervised heterogeneous graph embedding. `ssl_family=GRAPH_CONTRASTIVE`.

**Temporal backbone.** LSTM, Section 4.3, Eqs. (12)–(14). The output is the predicted graph \(\hat{\mathcal{G}}_{t+n}\).

**Sparse-concept setting.** The paper’s own target is an incomplete long-term graph sequence and missing edges. No passage states a zero-training-exposure KC split. Strict KC cold-start is not coded yes. The text extract contains no ECE or Brier score. Reported comparison metrics named in the experiment section are AUROC and Recall; a separate table reports accuracy of graph generation under missing edges.

## A1-C05 HCMKT — INCLUDE_PRIMARY_CORE

**Identity.** Jie Liu, Zheng Guan, Xue Wang, and Zhijun Yang. “Heterogeneous graph knowledge tracing with novel contrastive view and meta-path contexts.” Expert Systems With Applications 295 (2026) 128840. DOI 10.1016/j.eswa.2025.128840, printed on p. 1. Received 7 March 2025; accepted 28 June 2025; available online 29 June 2025. Crossref’s issued date remains 2026-01. Both dates are inside the search window. Text: `audit/_a1_evidence/HCMKT_fulltext_2026-11-22.txt`.

**KT.** Yes. Definition 1, p. 3, predicts whether the next answer is correct.

**G-criterion.** Yes. Definition 2, p. 3, defines a heterogeneous information network. Definition 3 instantiates the meta-path \(Qu-Sk-Qu\). Section 4.1 derives an adjacency matrix from each meta-path and encodes the coarse and fine views with two-layer GCNs, Eqs. (3)–(6). `graph_source=HYBRID_MULTI_SOURCE` because the network uses question, skill, bundle, and template attributes. `gnn_encoder=GCN`. The text does not say the network is built from the training split only. `graph_provenance=PRECOMPUTED_UNCLEAR_SPLIT`.

**S-criterion.** Yes. Section 4.4, Eq. (15), is a contrastive loss whose positive pair is the coarse-view and fine-grained-view embedding of the same question node. Eq. (16) adds a prototype contrastive loss. Section 4.1 also masks features and edges to perturb the fine view. `ssl_family=MULTIVIEW_CONTRASTIVE`.

**Temporal backbone.** LSTM, Section 4.2, Eq. (10). The reported split is 6:2:2. Table 4 reports AUC, ACC, and RMSE. The text extract contains no ECE or Brier score and no zero-exposure KC split. The 20/40/60 percent training-rate figure is a reduced-data comparison, not a strict KC cold-start protocol. The paper’s sparsity wording is sparse learning records, coded `GENERIC_DATA_SPARSITY`.

## Count effect if these two decisions and the DECKT decision are later entered

\(N\) 37→40, \(N_G\) 36→39, \(N_S\) 9→12, \(N_{G \cap S}\) 8→11. ECE and strict KC cold-start would be recomputed on the new denominator. CoSKT is not in this arithmetic. The three live tex files were not edited.
