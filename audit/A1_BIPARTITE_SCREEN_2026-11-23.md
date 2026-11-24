# Bipartite-graph chapter — screen 2026-11-23

**Decision:** `INCLUDE_PRIMARY_CORE`. Both the graph criterion and the self-supervised criterion are met. The paper is not a row in the printed 37-paper tables.

**Identity.** Kai Chen, Shun Mao, Qiwen Zheng, and Yuncheng Jiang. “Contrastive Learning Based on Bipartite Graphs for Interpretable Knowledge Tracing.” The PDF first page prints ADMA 2024, LNAI 15389, pp. 206–220, 2025, and DOI `10.1007/978-981-96-0821-8_14`. Crossref, read on 23 November 2026, gives the same authors, title, and pages; online date 15 December 2024; print year 2025. Crossref names the container Lecture Notes in Computer Science; the PDF prints LNAI 15389. Both the online date and the print year are inside 1 January 2015–31 July 2026. Text: `audit/_a1_evidence/BipartiteKT_fulltext_2026-11-23.txt` (15 pages).

**KT.** Yes. Section 3.1 defines the task as predicting the next response. The final score is Eq. (14).

**G-criterion.** Yes. Section 3.3 defines an exercise–concept bipartite graph \(G_1\) from the dataset’s exercise–concept links, plus an exercise correlation graph \(G_2\) and a concept correlation graph \(G_3\). Section 3.4 runs a bipartite graph attention network, a modified GAT, on \(G_1\) and uses the resulting exercise vectors in the LSTM predictor. `graph_source=HYBRID_MULTI_SOURCE` because \(G_1\) is the exercise–concept relation and \(G_2\)/\(G_3\) are additional same-type graphs. The initial rule for an edge in \(G_2\) or \(G_3\) is stated only as “whether related”; no formula is given, so those two graphs are not coded as co-occurrence or similarity. `gnn_encoder=GAT` for the named prediction encoder. The contrastive stack in Eq. (6) is written as an unnamed GNN. `graph_provenance=PRECOMPUTED_UNCLEAR_SPLIT`: the graphs are built from the dataset structure, and the paper does not state that they were built from the training split only.

**S-criterion.** Yes. Section 3.5 randomly adds or deletes edges, then applies an InfoNCE-style loss, Eq. (8), between a node and the same node in the augmented graph. Eq. (9) sums that loss over \(G_1\), \(G_2\), and \(G_3\). Eq. (18) adds it to the response losses. `ssl_family=GRAPH_CONTRASTIVE`. The paper also calls the inter-class and intra-class graphs two views; the positive pair itself is an augmented graph of the same node, so the exclusive family code stays graph contrastive.

**Sparse-concept and calibration.** Section 2 discusses inherent data sparsity, and Section 3.5 discusses sparse intra-class matrices. Neither is a zero-training-exposure KC split, an item cold-start split, or a learner cold-start split. Section 4 reports AUC and ACC. The extracted text contains no ECE, Brier, RMSE, or reliability diagram.

## Count effect if this chapter is later entered with the six already screened

The six earlier inclusions plus this chapter would make \(N\) 37→44, \(N_G\) 36→40, \(N_S\) 9→16, and \(N_{G \cap S}\) 8→12. That arithmetic is not applied. The chapter was not shown to be one of the \(N_{\mathrm{rec}}=2{,}017\) search records.
