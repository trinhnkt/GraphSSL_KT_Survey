# KT026 (PEBG) ADJUDICATION REPORT (Task A5)

**Paper:** *Improving Knowledge Tracing via Pre-training Question Embeddings* (Liu et al., IJCAI 2020)  
**Model Name:** PEBG (Pre-trained Exercise Embeddings via Bipartite Graph)  
**Audit Date:** 2026-09-12  

---

## 1. Full-Text Mathematical Objective Analysis

PEBG pre-trains dense question embeddings $e_q$ using a question-skill bipartite graph $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ prior to downstream DKT/DKVMN sequence training. Its joint pre-training loss is:

$$\mathcal{L}_{\text{PEBG}} = \lambda \mathcal{L}_1(Q, S) + \lambda \mathcal{L}_2(Q, Q) + \lambda \mathcal{L}_3(S, S) + (1-\lambda) \mathcal{L}_4(Q, S, \theta)$$

Where:
- $\mathcal{L}_1$: Cross-entropy loss recovering explicit question-skill bipartite edges.
- $\mathcal{L}_2$: First/second-order question neighborhood similarity preservation.
- $\mathcal{L}_3$: First/second-order skill neighborhood similarity preservation.
- $\mathcal{L}_4$: MSE regression error predicting question difficulty $d_q$.

---

## 2. S-Criterion & Taxonomy Classification

- **Satisfies S-Criterion?** **YES** (Unsupervised pre-training objective on graph structure prior to downstream KT sequence modeling).
- **SSL Family Classification:** `GRAPH_EMBEDDING_PRETRAINING` / `MASKED_PRETRAINING`.
- **Prose Correction:** PEBG does **NOT** use contrastive InfoNCE loss or masked concept prediction. Any manuscript text asserting "masked concept prediction" or "contrastive learning" for KT026 has been corrected to: *bipartite graph representation pre-training preserving local topological similarity and difficulty regression*.
