# DECKT full-text screen — 2026-11-22

**Decision:** `INCLUDE_PRIMARY_CORE`. Not yet added to the printed corpus. No KT inventory number is assigned in this note.

**Identity:** Yanhong Bai, Xingjiao Wu, Tingjiang Wei, Liang He. “A Dual-Encoder Contrastive Learning Model for Knowledge Tracing.” Entropy 27(7):685. Published 2025-06-26. DOI 10.3390/e27070685. PMC12294018. The text used is `audit/_a1_evidence/DECKT_fulltext_PMC12294018.txt`, the PMC full text. Crossref on 2026-11-22 returned the same title, container, and date. The date is inside 2015-01-01–2026-07-31. Language is English.

**KT:** yes. Section 3.1 predicts the next response \(r_{T+1}\) from the interaction history.

**G-criterion:** yes. Section 3.1 constructs a question–concept bipartite graph \(G=(V,E)\) from the adjacency matrix \(A\). Section 3.3.1 uses a multi-layer GAT on that matrix. `graph_source=Q_MATRIX`. `gnn_encoder=GAT`. The text does not say the graph is built from training interactions only, so `graph_provenance=PRECOMPUTED_UNCLEAR_SPLIT`.

**S-criterion:** yes. Section 3.5 uses InfoNCE between the primary-encoder embedding and the momentum-encoder embedding of the same question node, and the same form for concept nodes. The supervision is the paired view, not an extra human label. Section 3.3 says the views come from the intact graph, not from edge deletion or feature masking. `ssl_family=GRAPH_CONTRASTIVE`. The printed four-family table has no separate augmentation-free cell; this note does not add one.

**Temporal backbone:** LSTM. Section 3.4 writes \(h_t=\mathrm{LSTM}(x_t,h_{t-1})\) and trains the response prediction with binary cross-entropy.

**Sparse-concept setting:** `LOW_FREQUENCY_KC` and `LONG_TAIL_KC`, as the paper’s own sparsity claim. No passage states a zero-training-exposure KC split, an item cold-start split, or a learner cold-start split. The word “cold-start” in this text is a citation to another paper. Strict KC cold-start is not coded yes.

**Calibration:** the PMC text reports AUC and ACC. It does not report ECE or Brier. Section 4’s Figure 4 sentence uses “predictive calibration” for one 27-question sequence and gives 22/27 accuracy. That sentence is not an ECE or Brier statistic.

**Reported AUC, as printed:** 0.7901, 0.7817, 0.7845, 0.7740, and 0.7893 on ASSIST09, ASSIST12, Slepemapy.cz, EdNet, and Statics2011. Experiments are repeated 5 times and the average is reported. These values are not a comparison with the 37-paper tables.

**Coding completeness:** full text inspected for the inclusion gate. Dataset-level experiment rows are not coded yet.

**Count effect if this decision is later entered:** \(N\) 37→38, \(N_G\) 36→37, \(N_S\) 9→10, \(N_{G \cap S}\) 8→9. ECE and strict KC cold-start would be recomputed on the new denominator. Those replacements are not made in this step.
