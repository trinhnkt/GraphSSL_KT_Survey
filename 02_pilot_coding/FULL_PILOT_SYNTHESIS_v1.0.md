# FULL_PILOT_SYNTHESIS_v1.0

## Executive Summary

This document synthesizes the completed **15-Paper Pilot Corpus** for the systematic survey:
**"Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda"**.

The pilot execution was conducted across three iterative waves (Wave A, Wave B, Wave C) under Codebook v0.3 and Codebook v0.4 (`coding_codebook_v0.4_PILOT.md`), establishing 100% methodological auditability across PAPER, MODEL, and EXPERIMENT levels with field-level evidence tables.

---

## 1. Master Pilot Corpus Summary (15 Papers)

| # | Paper ID | Title / Venue | Target Tier | G-Crit | S-Crit | Completeness | QA Score | Primary Pilot Mechanism / Boundary Tested |
|---:|---|---|---|:---:|:---:|---|---|---|
| 1 | **KT004** | Graph-Based Knowledge Tracing (WI 2019) | `PRIMARY_CORE` | `Y` | `N` | `FULLTEXT_CODED` | 10/16 (0.6250) | Seminal Graph-KT; tests GKT-Dense vs GKT-Transition model entries. |
| 2 | **KT010** | GIKT (ECML-PKDD 2021) | `PRIMARY_CORE` | `Y` | `N` | `FULLTEXT_CODED` | 11/16 (0.6875) | Question-concept bipartite graph + GCN propagation. |
| 3 | **KT014** | PDKT-C (ICDM 2018) | `PRIMARY_CORE` | `Y` | `N` | `FULLTEXT_CODED` | 12/16 (0.7500) | Expert prerequisite DAG; tests Graph-KT without GNN message passing (CB14). |
| 4 | **KT026** | Pre-Training Question Embeddings (IJCAI 2020) | `PRIMARY_CORE` | `Y` | `N` | `FULLTEXT_CODED` | 11/16 (0.6875) | Pre-training question embeddings from bipartite graph vs SSL pretext boundary. |
| 5 | **KT035** | HHSKT (ESWA 2023) | `PRIMARY_CORE` | `Y` | `N` | `FULLTEXT_REQUIRED` | 8/16 (0.5000) | Heterogeneous multi-node graph; tests partial text coding status (CB16). |
| 6 | **KT037** | CMKT (IEEE TLT 2022) | `PRIMARY_CORE` | `Y` | `N` | `FULLTEXT_CODED` | 12/16 (0.7500) | External concept map topology + ordering pair loss constraint (`gnn_encoder = NONE`). |
| 7 | **KT038** | DyGKT (KDD 2024) | `PRIMARY_CORE` | `Y` | `N` | `FULLTEXT_CODED` | 14/16 (0.8750) | Continuous-time dynamic question-answering graph (`DYNAMIC_TEMPORAL`, `TEMPORAL_DYNAMIC_GNN`). |
| 8 | **KT039** | CL4KT (WWW 2022) | `PRIMARY_CORE` | `N` | `Y` | `FULLTEXT_CODED` | 13/16 (0.8125) | Pure sequence-level contrastive SSL (`graph_source = NONE`). |
| 9 | **KT011** | Bi-CLKT (KBS 2022) | `PRIMARY_CORE` | `Y` | `Y` | `FULLTEXT_CODED` | 11/16 (0.6875) | Dual-graph framing + dual-level graph contrastive SSL. |
| 10 | **KT042** | S2-HHN (InfoSci 2023) | `PRIMARY_CORE` | `Y` | `Y` | `FULLTEXT_CODED` | 11/16 (0.6875) | Heterogeneous hypergraph + hypergraph view contrastive SSL. |
| 11 | **KT066** | HyperKT (IEEE TNNLS 2025) | `PRIMARY_CORE` | `Y` | `Y` | `FULLTEXT_CODED` | 11/16 (0.6875) | Dual-channel hypergraph + cross-view contrastive SSL. |
| 12 | **KT044** | SINKT (CIKM 2024) | `PRIMARY_CORE` | `Y` | `N` | `FULLTEXT_CODED` | 14/16 (0.8750) | LLM-assisted heterogeneous graph + strict inductive KC cold-start (`STRICT_KC_COLD_START`). |
| 13 | **KT049** | Cold-Start LLM (CIKM 2024) | `PRIMARY_ADJACENT_SPARSE` | `N` | `N` | `FULLTEXT_CODED` | 13/16 (0.8125) | LLM attribute-aware cold-start context for RQ4 without Graph/SSL gateway. |
| 14 | **KT041** | k-Sparse Attention (SIGIR 2023) | `BACKGROUND` | `N` | `N` | `FULLTEXT_CODED` | 10/16 (0.6250) | Term ambiguity boundary: architectural $k$-sparse attention is NOT sparse-concept KC evidence. |
| 15 | **KT055** | GKT-CD (IJCNN 2021) | `EXCLUDE_FULLTEXT` | `Y` | `N` | `FULLTEXT_CODED` | 11/16 (0.6875) | Task eligibility exclusion: Cognitive Diagnosis enhanced by Graph-KT (`kt_central_task = NO`). |

---

## 2. Resolved Methodological Codebook Candidates (CB13–CB17)

1. **CB13 (Repeated runs vs Random seeds):** Separated `resampling_repeats` (data split re-runs) from `n_seeds` (model initialization seeds) and added `repeated_run_unit` (`SEED_REPETITION`, `SPLIT_RESAMPLING`, `CROSS_VALIDATION_FOLD`).
2. **CB14 (Graph-KT Gateway without GNN):** Established that an explicit graph satisfies `G_criterion = Y` even when `gnn_encoder = NONE` if the graph serves as a central structural mechanism (regularization constraint or structural embedding input, as in KT014 PDKT-C and KT037 CMKT).
3. **CB15 (Evidence Source Type):** Added `evidence_source_type` (`PAPER_FULLTEXT`, `PUBLISHER_METADATA`, `AUTHOR_CODE`, `AUTHOR_SUPPLEMENT`, `SECONDARY`, `REPRODUCED`) to field evidence tables.
4. **CB16 (Coding Completeness):** Added `coding_completeness` (`FULLTEXT_CODED`, `PARTIAL_SOURCE_ONLY`, `FULLTEXT_REQUIRED`, `METADATA_ONLY`) to track source availability.
5. **CB17 (Evidence Scope Isolation):** Prohibited inferring paper-stated evaluation protocols or reported metrics solely from author code repository defaults.

---

## 3. Core Corpus Distribution & Recommendations for Codebook v1.0 Freezing

### Distribution Across Corpus Tiers
- **`PRIMARY_CORE`**: 12 papers (11 fulltext coded + 1 fulltext required).
- **`PRIMARY_ADJACENT_SPARSE`**: 1 paper (KT049).
- **`BACKGROUND`**: 1 paper (KT041).
- **`EXCLUDE_FULLTEXT`**: 1 paper (KT055).

### Codebook Status
Codebook v0.4 (`coding_codebook_v0.4_PILOT.md`) has successfully passed all 15 boundary stress-tests without generating unresolved ambiguity. It is ready for official freezing to **`coding_codebook_v1.0_LOCKED.md`** for full-corpus coding execution.
