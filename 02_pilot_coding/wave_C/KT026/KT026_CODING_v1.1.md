# KT026 — PEBG / Pre-train Q-Emb Coding Record (v1.1)

**Paper ID:** PAPER_KT026  
**Legacy ID:** KT026  
**Title:** Improving Knowledge Tracing via Pre-Training Question Embeddings  
**Venue:** IJCAI 2020  
**DOI:** 10.24963/ijcai.2020/219  
**Codebook:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-09-13  
**Supersedes v0.4 on:** `S_criterion`, `ssl_family`, SSL target/pretext/training fields.  
**Other PAPER/MODEL/EXPERIMENT/QA rows:** unchanged from v0.4 unless listed below.

---

# 1. PAPER (changed fields)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `S_criterion` | `YES` | LIT_REPORTED + ADJUDICATED | PAPER_FULLTEXT | Previous pilot coding classified PEBG as generic pretraining. Final adjudication overturned this decision because PEBG reconstructs explicit and implicit relations generated from the observed question–skill bipartite graph, satisfying the frozen SCOPE graph-reconstruction criterion. |
| `corpus_tier` | `PRIMARY_CORE` | ADJUDICATED | PROTOCOL | `KT AND (GRAPH_BASED OR SELF_SUPERVISED)` — now G and S |

# 2. MODEL (`MODEL_KT026_PRETRAIN`, changed fields)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `ssl_family` | `GRAPH_RECONSTRUCTION` | LIT_REPORTED + ADJUDICATED | PAPER_FULLTEXT | Locked codebook §14. Not `GRAPH_EMBEDDING_PRETRAINING` (not a locked token). |
| `ssl_family_note` | L1 also matches `RELATION_EDGE_PREDICTION`; not a second exclusive family | ADJUDICATED | CODEBOOK | Gap logged in `KT026_S_CRITERION_ADJUDICATION_v1.1.md` |
| `self_generated_target` | `EXPLICIT_QS_RELATION` + `IMPLICIT_QQ_SIMILARITY` + `IMPLICIT_SS_SIMILARITY` | LIT_REPORTED + ADJUDICATED | PAPER_FULLTEXT | PEBG L1 / L2 / L3 |
| `pretext_objective` | `BIPARTITE_RELATION_RECONSTRUCTION` | LIT_REPORTED + ADJUDICATED | PAPER_FULLTEXT | Product-based recovery of side information |
| `training_mode` | `TWO_STAGE_PRETRAIN` | LIT_REPORTED | PAPER_FULLTEXT | Pretrain embeddings, then DKT/DKVMN |
| `masked_autoencoding` | `N` | LIT_REPORTED + ADJUDICATED | PAPER_FULLTEXT | No masked AE objective |
| `masked_concept_prediction` | `N` | LIT_REPORTED + ADJUDICATED | PAPER_FULLTEXT | Not masked concept prediction |
| `gnn_encoder` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | PNN pretrain; unchanged from v0.4 |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | Reconstruction, not view dropout |

# 3. Unchanged (v0.4)

`G_criterion=YES`, `gnn_encoder=NONE`, graph/Q-matrix fields, EXPERIMENT rows, QA scores (raw 11/16, MODERATE).
