# KT026 Field-Level Evidence (v1.1) — current S-criterion lock

**Current `S_criterion`:** `YES`  
**Historical pilot rows:** kept in `KT026_FIELD_EVIDENCE_v0.4.md` (`E026_005=NO`, generic pretraining). Those rows are not deleted.  
**Type of change:** coding correction / adjudication. Not a SCOPE change. `_LOCKED` files not edited.

Schema: `entity_id + field_name + coded_value + coding_basis + evidence_locator + evidence_note + source`.

## Historical decision (retained)

| evidence_id | status | field_name | coded_value | evidence_note |
|---|---|---|---|---|
| E026_005 | SUPERSEDED | S_criterion | NO | Generic question embedding pretraining on bipartite graph, NOT a self-supervised pretext task loss during KT sequence tracing. Full row remains in v0.4. |
| E026_016 | SUPERSEDED | ssl_family | NONE | Generic graph feature pre-training; no self-supervised pretext task loss during KT sequence tracing. Full row remains in v0.4. |

## Current decision (2026-09-13)

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_locator | evidence_note | source | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|
| E026_005b | PAPER | PAPER_KT026 | S_criterion | YES | LIT_REPORTED + ADJUDICATED | IJCAI 2020 Sec. 4; \(L_1\)–\(L_3\) | Previous pilot coding classified PEBG as generic pretraining. Final adjudication overturned this decision because PEBG reconstructs explicit and implicit relations generated from the observed question–skill bipartite graph, satisfying the frozen SCOPE graph-reconstruction criterion. | 10.24963/ijcai.2020/219 | ADJUDICATED |
| E026_016b | MODEL | MODEL_KT026_PRETRAIN | ssl_family | GRAPH_RECONSTRUCTION | LIT_REPORTED + ADJUDICATED | Codebook v1.0 §14; \(L_1\)–\(L_3\) | Locked codebook token. Earlier manuscript display alias `GRAPH_EMBEDDING_PRETRAINING` is retired; Table IV now prints `GRAPH_RECONSTRUCTION`. | 10.24963/ijcai.2020/219 | ADJUDICATED |
| E026_021 | MODEL | MODEL_KT026_PRETRAIN | self_generated_target | EXPLICIT_QS_RELATION + IMPLICIT_QQ_SIMILARITY + IMPLICIT_SS_SIMILARITY | LIT_REPORTED + ADJUDICATED | PEBG \(L_1\), \(L_2\), \(L_3\) | These three reconstruction terms are sufficient for S=Y. | 10.24963/ijcai.2020/219 | ADJUDICATED |
| E026_022 | MODEL | MODEL_KT026_PRETRAIN | pretext_objective | BIPARTITE_RELATION_RECONSTRUCTION | LIT_REPORTED + ADJUDICATED | Sec. 4 joint pretrain loss | Product-based reconstruction of observed relations, then downstream KT. | 10.24963/ijcai.2020/219 | ADJUDICATED |
| E026_023 | MODEL | MODEL_KT026_PRETRAIN | training_mode | TWO_STAGE_PRETRAIN | LIT_REPORTED | Sec. 4–5 | Embedding pretrain, then DKT/DKVMN. | 10.24963/ijcai.2020/219 | ADJUDICATED |
| E026_024 | MODEL | MODEL_KT026_PRETRAIN | masked_autoencoding | N | LIT_REPORTED + ADJUDICATED | Method | Not masked autoencoding. | 10.24963/ijcai.2020/219 | ADJUDICATED |
| E026_025 | MODEL | MODEL_KT026_PRETRAIN | masked_concept_prediction | N | LIT_REPORTED + ADJUDICATED | Method | Not masked concept prediction. | 10.24963/ijcai.2020/219 | ADJUDICATED |
| E026_026 | MODEL | MODEL_KT026_PRETRAIN | difficulty_loss | AUXILIARY_SIDE_INFORMATION | LIT_REPORTED + ADJUDICATED | PEBG \(L_4\) | Difficulty MSE may be recorded as an auxiliary side-information loss. It is **not** used to justify SSL. \(L_1\)–\(L_3\) already suffice. | 10.24963/ijcai.2020/219 | ADJUDICATED |
