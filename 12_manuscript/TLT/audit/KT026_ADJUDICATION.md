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

- **Satisfies S-Criterion?** **YES** (ADJUDICATED 2026-09-13).
- **Locked `ssl_family`:** `GRAPH_RECONSTRUCTION` (`coding_codebook_v1.0_LOCKED.md` §14).
- **Not coded:** `GRAPH_EMBEDDING_PRETRAINING`, `GRAPH_RELATION_RECONSTRUCTION`, `MASKED_PRETRAINING` (none of these are locked tokens; the last is also factually wrong).
- **Targets:** `EXPLICIT_QS_RELATION` + `IMPLICIT_QQ_SIMILARITY` + `IMPLICIT_SS_SIMILARITY`.
- **Pretext:** `BIPARTITE_RELATION_RECONSTRUCTION`. **Training:** `TWO_STAGE_PRETRAIN`.
- **`masked_autoencoding=N`.** **`masked_concept_prediction=N`.**
- **Prose:** PEBG is bipartite relation reconstruction (\(L_1\)–\(L_3\)), not InfoNCE and not masked concept prediction. \(L_4\) is an auxiliary side-information loss and is not used to justify SSL.

Canonical lock: `02_pilot_coding/wave_C/KT026/KT026_S_CRITERION_ADJUDICATION_v1.1.md`.
