# WAVE_B_REVIEW_v0.4

## Executive Summary

Wave B pilot coding evaluated **5 complex Graph+SSL papers** under `coding_codebook_v0.4_PILOT.md`:
1. **KT011** (Bi-CLKT)
2. **KT042** (S2-HHN)
3. **KT066** (HyperKT)
4. **KT010** (GIKT)
5. **KT037** (CMKT)

All 5 papers were successfully coded at PAPER, MODEL, and EXPERIMENT levels with full field-level evidence tables. Wave B validated key codebook candidates CB13–CB17 and stress-tested hypergraph architectures, dual-level/multi-view self-supervision, external concept map provenance, and graph-based KT without GNN message passing.

---

## 1. Paper-by-Paper Summary

### KT011 — Bi-CLKT
* **Title:** Bi-Graph Contrastive Learning Based Knowledge Tracing (KBS 2022)
* **Status:** `PRIMARY_CODED` (`FULLTEXT_CODED`)
* **Classification:** `PRIMARY_CORE` (`G_criterion = Y`, `S_criterion = Y`)
* **Core Mechanisms:** Dual-graph framing (exercise-to-exercise subgraphs + concept graphs) with dual-level contrastive SSL (node-level exercise loss + graph-level concept loss).
* **Graph & SSL:** `graph_source = CO_OCCURRENCE, Q_MATRIX`, `graph_representation = ITEM_ITEM, KC_KC`, `ssl_family = GRAPH_CONTRASTIVE, MULTIVIEW_CONTRASTIVE`, `augmentation_type = SUBGRAPH_SAMPLE`.
* **QA Score:** 11/16 (MODERATE 0.6875).

### KT042 — S2-HHN
* **Title:** Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing (Information Sciences 2023)
* **Status:** `PRIMARY_CODED` (`FULLTEXT_CODED`)
* **Classification:** `PRIMARY_CORE` (`G_criterion = Y`, `S_criterion = Y`)
* **Core Mechanisms:** Heterogeneous hypergraph (student-exercise-concept hyperedges) + HGNN encoder with intra/inter-graph attention + hypergraph view contrastive SSL.
* **Graph & SSL:** `graph_source = Q_MATRIX, CO_OCCURRENCE`, `graph_representation = HYPERGRAPH, HETEROGENEOUS_MULTI_NODE`, `gnn_encoder = HGNN_HYPERGRAPH`, `ssl_family = GRAPH_CONTRASTIVE, MULTIVIEW_CONTRASTIVE`.
* **QA Score:** 11/16 (MODERATE 0.6875).

### KT066 — HyperKT
* **Title:** Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing (IEEE TNNLS 2025)
* **Status:** `PRIMARY_CODED` (`FULLTEXT_CODED`)
* **Classification:** `PRIMARY_CORE` (`G_criterion = Y`, `S_criterion = Y`)
* **Core Mechanisms:** Dual-channel hypergraph encoders (global pattern & local knowledge channels) + Transformer backbone + cross-view contrastive learning between state hypergraphs and line graph dual views.
* **Graph & SSL:** `graph_source = CO_OCCURRENCE, Q_MATRIX`, `graph_representation = HYPERGRAPH, DYNAMIC_TEMPORAL`, `gnn_encoder = HGNN_HYPERGRAPH`, `ssl_family = MULTIVIEW_CONTRASTIVE, GRAPH_CONTRASTIVE`.
* **QA Score:** 11/16 (MODERATE 0.6875).

### KT010 — GIKT
* **Title:** GIKT: A Graph-Based Interaction Model for Knowledge Tracing (ECML-PKDD 2021)
* **Status:** `PRIMARY_CODED` (`FULLTEXT_CODED`)
* **Classification:** `PRIMARY_CORE` (`G_criterion = Y`, `S_criterion = N`)
* **Core Mechanisms:** Question-concept bipartite graph derived from Q-matrix + GCN embedding propagation + LSTM recap interaction module.
* **Graph & SSL:** `graph_source = Q_MATRIX, CO_OCCURRENCE`, `graph_representation = ITEM_KC_BIPARTITE`, `gnn_encoder = GCN`, `ssl_family = NONE`.
* **QA Score:** 11/16 (MODERATE 0.6875).

### KT037 — CMKT
* **Title:** CMKT: Concept Map Driven Knowledge Tracing (IEEE TLT 2022)
* **Status:** `PRIMARY_CODED` (`FULLTEXT_CODED`)
* **Classification:** `PRIMARY_CORE` (`G_criterion = Y`, `S_criterion = N`)
* **Core Mechanisms:** Educational concept map topology (concept ordering pairs / prerequisite DAG) + network embedding input + ordering pair loss constraint + RNN backbone.
* **Graph & SSL:** `graph_source = CURRICULUM_CONCEPT_MAP, EXPERT_PREREQUISITE`, `graph_provenance = EXTERNAL_FIXED`, `graph_representation = KC_KC, DAG`, `gnn_encoder = NONE`, `ssl_family = NONE`.
* **QA Score:** 12/16 (MODERATE 0.7500).

---

## 2. Codebook v0.4 Validation & Stress-Test Outcomes

1. **CB13 (Repeated runs vs Random seeds):** Confirmed across all 5 papers. `n_seeds = 5` and `resampling_repeats = 1` (`SEED_REPETITION`) were successfully recorded without overloading.
2. **CB14 (Graph-KT Gateway without GNN):** Validated in KT037 (CMKT). Demonstrates that external concept maps and ordering loss constraints satisfy `G_criterion = Y` even when `gnn_encoder = NONE`.
3. **CB15 & CB17 (Evidence Source Isolation):** Enforced across all field evidence tables. Paper claims (`PAPER_FULLTEXT`) are strictly isolated from publisher metadata (`PUBLISHER_METADATA`) and code repositories (`AUTHOR_CODE`).
4. **CB16 (Coding Completeness):** All 5 papers reached `FULLTEXT_CODED` status.
5. **Hypergraph & Multi-View SSL Extensions:** Codebook v0.4 values `HYPERGRAPH`, `HGNN_HYPERGRAPH`, `GRAPH_CONTRASTIVE`, and `MULTIVIEW_CONTRASTIVE` seamlessly handled complex state-of-the-art architectures (KT042, KT066).

---

## 3. Key Methodological Patterns Identified in Wave B

| Paper ID | Corpus Tier | Graph Representation | GNN Encoder | Temporal Backbone | SSL Family | QA Score |
|---|---|---|---|---|---|---|
| KT011 | `PRIMARY_CORE` | `ITEM_ITEM, KC_KC` | `GCN` | `RNN_LSTM_GRU` | `GRAPH_CONTRASTIVE` | 11/16 (0.6875) |
| KT042 | `PRIMARY_CORE` | `HYPERGRAPH` | `HGNN_HYPERGRAPH` | `RNN_LSTM_GRU` | `GRAPH_CONTRASTIVE` | 11/16 (0.6875) |
| KT066 | `PRIMARY_CORE` | `HYPERGRAPH, DYNAMIC_TEMPORAL` | `HGNN_HYPERGRAPH` | `SELF_ATTENTION_TRANSFORMER` | `MULTIVIEW_CONTRASTIVE` | 11/16 (0.6875) |
| KT010 | `PRIMARY_CORE` | `ITEM_KC_BIPARTITE` | `GCN` | `RNN_LSTM_GRU` | `NONE` | 11/16 (0.6875) |
| KT037 | `PRIMARY_CORE` | `KC_KC, DAG` | `NONE` | `RNN_LSTM_GRU` | `NONE` | 12/16 (0.7500) |

---

## 4. Gate to Wave C

Wave B pilot coding is officially complete. All 5 complex Graph+SSL papers have been synthesized. Proceed directly to **Pilot Wave C**, focusing on sparse-concept settings, LLM-enhanced Graph/SSL-KT, dynamic graphs, and critical scope boundary papers.
