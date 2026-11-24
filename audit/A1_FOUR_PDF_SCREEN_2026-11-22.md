# Four supplied PDFs — screen 2026-11-22

The bipartite-graph chapter, 10.1007/978-981-96-0821-8_14, is still absent from `14_references`. Printed counts stay at 37. None of the decisions below is entered in the live tex files.

## DECKT — identity confirmed, decision unchanged

`14_references/A Dual-Encoder Contrastive Learning Model for Knowledge Tracing (DECKT).pdf` is the MDPI article. Page 1 prints DOI 10.3390/e27070685, Entropy 2025, 27, 685, published 26 June 2025, authors Yanhong Bai, Xingjiao Wu, Tingjiang Wei, and Liang He. This is the same paper already screened `INCLUDE_PRIMARY_CORE` in `audit/A1_DECKT_SCREEN_2026-11-22.md`.

## CoSKT — INCLUDE_PRIMARY_CORE through S only

Chunyun Zhang, Hebo Ma, Chaoran Cui, Yumo Yao, Weiran Xu, Yunfeng Zhang, and Yuling Ma. IEEE Transactions on Learning Technologies, vol. 17, pp. 1476–1488, 2024. DOI 10.1109/TLT.2024.3386750, printed on p. 1. Date of publication 9 April 2024. Inside the search window. Text: `audit/_a1_evidence/CoSKT_fulltext_2026-11-22.txt`.

**KT.** Yes. Section III-A predicts the next response \(a_{t+1}\).

**G-criterion.** No. The model is an LSTM over the student’s own sequence, multi-head attention over similar students, and a gate, Sections III-C through III-E. Graph, GCN, and bipartite wording in this PDF is in the related-work discussion of other models. `gnn_encoder=NONE`. `graph_source=NONE`.

**S-criterion.** Yes. Section III-D, Eq. (13), is an InfoNCE loss. The positive pair is the student’s individual knowledge state and the common knowledge state of similar students. `ssl_family=SEQUENCE_CONTRASTIVE`.

**Sparse-concept and calibration.** Section IV-H discusses short sequences and a small number of similar students. It does not report a zero-training-exposure KC split, an item cold-start split, or a learner cold-start split. Evaluation metrics named in Section IV are AUC and ACC. The text contains no ECE or Brier score.

## DTransformer — INCLUDE_PRIMARY_CORE through S only

Yu Yin, Le Dai, Zhenya Huang, Shuanghong Shen, Fei Wang, Qi Liu, Enhong Chen, and Xin Li. “Tracing Knowledge Instead of Patterns: Stable Knowledge Tracing with Diagnostic Transformer.” WWW ’23, 30 April–4 May 2023, Austin. DOI 10.1145/3543507.3583255, printed on p. 1. Inside the search window. The seed list labeled this paper KT040 `BACKGROUND`. That label is not the full-text decision. Text: `audit/_a1_evidence/DTransformer_pdf_2026-11-22.txt`.

**KT.** Yes. Section 3.3.2 predicts the next response from the current knowledge state.

**G-criterion.** No. The architecture goes from question mastery to knowledge-concept state with attention. The graph sentences in the PDF cite other papers, including Bi-CLKT. `gnn_encoder=NONE`. `graph_source=NONE`.

**S-criterion.** Yes. Section 3.3.1 augments a learner sequence by flipping responses, dropping items, and swapping adjacent items, then applies a contrastive loss, Eq. (17), so that knowledge states from the same learner stay close. Eq. (22) adds that loss to the response cross-entropy. `ssl_family=SEQUENCE_CONTRASTIVE`.

**Calibration.** The experiment reports AUC and RMSE. The text contains no ECE or Brier score and no strict KC cold-start split.

## SP-CLKT — INCLUDE_PRIMARY_CORE through S only

Huan Dai, Yue Yun, Yupei Zhang, Rui An, Wenxin Zhang, and Xuequn Shang. “Self-paced contrastive learning for knowledge tracing.” Neurocomputing 609 (2024) 128366. DOI 10.1016/j.neucom.2024.128366, printed on p. 1. Available online 13 August 2024. Inside the search window. Text: `audit/_a1_evidence/SPCLKT_fulltext_2026-11-22.txt`.

**KT.** Yes. The model predicts later responses. The temporal backbone described in the introduction and Section 2 is LSTM.

**G-criterion.** No. Section 3.3 says a chain-like directed acyclic graph is assumed for simplicity, then replaces that assumption with a difficulty order of questions, ranked by the training-set probability of a correct answer. The order chooses replacement questions. The paper does not construct an adjacency matrix or run a graph encoder. `gnn_encoder=NONE`. `graph_source=NONE`.

**S-criterion.** Yes. Section 3.4, Eq. (7), is a contrastive loss on student answer sequences, with local and global samples. Eq. (8) adds it to the prediction loss. The abstract calls the objective self-supervised contrastive learning. `ssl_family=SEQUENCE_CONTRASTIVE`.

**Sparse-concept and calibration.** The paper’s sparsity claim is sparse student–skill interactions. It does not report a strict KC cold-start split. Table results are AUC, ACC, and F1. The text contains no ECE or Brier score.

## Count effect if every full-text inclusion so far is later entered

Included and not yet printed: DECKT, Han et al. 2024, and HCMKT are graph and self-supervised; CoSKT, DTransformer, and SP-CLKT are self-supervised only. That arithmetic is \(N\) 37→43, \(N_G\) 36→39, \(N_S\) 9→15, \(N_{G \cap S}\) 8→11. ECE and strict KC cold-start would be recomputed on the new denominator. The bipartite chapter is not in this arithmetic.
