# KT026 PEBG — S-criterion lock (v1.1)

**Status:** ADJUDICATED  
**Date:** 2026-09-13  
**Supersedes:** `KT026_CODING_v0.4.md` / `KT026_FIELD_EVIDENCE_v0.4.md` fields `S_criterion` and `ssl_family` only.  
**Does not edit:** locked protocol files.

## Identity

| Field | Value |
|---|---|
| `paper_id` | KT026 |
| model | PEBG / Pre-train Q-Emb |
| title | Improving Knowledge Tracing via Pre-Training Question Embeddings |
| venue | IJCAI 2020 |
| DOI | 10.24963/ijcai.2020/219 |

## Locked codes

| Field | Value |
|---|---|
| `S_criterion` | `Y` |
| `G_criterion` | `Y` (unchanged) |
| `corpus_tier` | `PRIMARY_CORE` (unchanged; now G and S) |
| locked `ssl_family` | `GRAPH_RECONSTRUCTION` |
| display alias (manuscript CSV only) | `GRAPH_EMBEDDING_PRETRAINING` |
| `self_generated_target` | `EXPLICIT_QS_RELATION` + `IMPLICIT_QQ_SIMILARITY` + `IMPLICIT_SS_SIMILARITY` |
| `pretext_objective` | `BIPARTITE_RELATION_RECONSTRUCTION` |
| `training_mode` | `TWO_STAGE_PRETRAIN` |
| `masked_autoencoding` | `N` |
| `masked_concept_prediction` | `N` |
| `coding_basis` | `LIT_REPORTED` + `ADJUDICATED` |
| `adjudication_status` | `ADJUDICATED` |

\(L_4\) difficulty regression may be recorded as an **auxiliary side-information loss**. It is **not** used to justify SSL; \(L_1\)–\(L_3\) already suffice. Downstream DKT/DKVMN is supervised KT after pretraining.

## Codebook gap (do not invent a new family)

`coding_codebook_v1.0_LOCKED.md` §14 allows `GRAPH_RECONSTRUCTION` and `RELATION_EDGE_PREDICTION`. It does **not** list `GRAPH_EMBEDDING_PRETRAINING` or `GRAPH_RELATION_RECONSTRUCTION`.

Those two strings are therefore **not** coded as `ssl_family`. The locked value is `GRAPH_RECONSTRUCTION` (SCOPE §5 lists graph reconstruction as an eligible SSL family). L1 edge recovery is noted as `RELATION_EDGE_PREDICTION` in evidence, not as a second mutually exclusive family.

## Why this overrides pilot `S=NO`

Previous pilot coding classified PEBG as generic pretraining. Final adjudication overturned this decision because PEBG reconstructs explicit and implicit relations generated from the observed question–skill bipartite graph, satisfying the frozen SCOPE graph-reconstruction criterion.

This is a coding correction / adjudication. It is not a SCOPE change and does not require editing `_LOCKED` files.

PEBG is one of the locked \(N_S=9\) SSL papers.

## Companion files

- `KT026_CODING_v1.1.md`
- `KT026_FIELD_EVIDENCE_v1.1.md`
