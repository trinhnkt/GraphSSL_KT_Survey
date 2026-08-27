# WAVE_C_REVIEW_v0.4

## Executive Summary

Wave C pilot coding evaluated the remaining **6 frontier & boundary papers** under `coding_codebook_v0.4_PILOT.md`:
1. **KT038** (DyGKT): Dynamic Graph Learning (`PRIMARY_CORE`)
2. **KT044** (SINKT): Structure-Aware Inductive KT with LLM (`PRIMARY_CORE`)
3. **KT026** (Pre-Training Question Embeddings): Graph pre-training vs SSL boundary (`PRIMARY_CORE`)
4. **KT049** (Cold-Start LLM): Primary adjacent sparse case (`PRIMARY_ADJACENT_SPARSE`)
5. **KT041** (k-Sparse Attention): Sparse-attention term ambiguity boundary (`BACKGROUND`)
6. **KT055** (GKT-CD): Cognitive Diagnosis task eligibility exclusion boundary (`EXCLUDE_FULLTEXT`)

All 6 papers were coded with complete PAPER, MODEL, EXPERIMENT levels and field-level evidence tables. Wave C successfully resolved all remaining protocol boundaries and completed the 15-paper pilot corpus.

---

## 1. Paper-by-Paper Summary

### KT038 — DyGKT
* **Title:** DyGKT: Dynamic Graph Learning for Knowledge Tracing (KDD 2024)
* **Status:** `PRIMARY_CODED` (`FULLTEXT_CODED`)
* **Classification:** `PRIMARY_CORE` (`G_criterion = Y`, `S_criterion = N`)
* **Core Mechanisms:** Continuous-time dynamic question-answering graph (`DYNAMIC_TEMPORAL`) + dynamic GNN encoder (`TEMPORAL_DYNAMIC_GNN`) + dual time encoder & multiset indicator.
* **QA Score:** 14/16 (HIGH 0.8750). Verified author repository: `https://github.com/PengLinzhi/DyGKT`.

### KT044 — SINKT
* **Title:** SINKT: A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model (CIKM 2024)
* **Status:** `PRIMARY_CODED` (`FULLTEXT_CODED`)
* **Classification:** `PRIMARY_CORE` (`G_criterion = Y`, `S_criterion = N`)
* **Core Mechanisms:** LLM-assisted heterogeneous question-concept graph (`LLM_ASSISTED`) + heterogeneous GNN (`HETEROGENEOUS_GNN`) + Transformer backbone + strict inductive cold-start evaluation (`STRICT_KC_COLD_START`).
* **QA Score:** 14/16 (HIGH 0.8750). Verified author repository: `https://github.com/tubehao/SINKT`.

### KT026 — Pre-Training Question Embeddings
* **Title:** Improving Knowledge Tracing via Pre-Training Question Embeddings (IJCAI 2020)
* **Status:** `PRIMARY_CODED` (`FULLTEXT_CODED`)
* **Classification:** `PRIMARY_CORE` (`G_criterion = Y`, `S_criterion = N`)
* **Core Mechanisms:** Question-skill bipartite graph (`ITEM_KC_BIPARTITE`) + product-based neural network (PNN) matrix factorization for question pretraining + LSTM backbone (`fusion_type = GRAPH_INITIALIZATION`).
* **QA Score:** 11/16 (MODERATE 0.6875).

### KT049 — Cold-Start LLM
* **Title:** Mitigating Cold-Start Problems in Knowledge Tracing with Large Language Models: An Attribute-Aware Approach (CIKM 2024)
* **Status:** `PRIMARY_CODED` (`FULLTEXT_CODED`)
* **Classification:** `PRIMARY_ADJACENT_SPARSE` (`G_criterion = N`, `S_criterion = N`)
* **Core Mechanisms:** LLM text attribute encoding injected into RNN sequence tracing for zero-exposure cold-start items (`ITEM_COLD_START`).
* **QA Score:** 13/16 (HIGH 0.8125).

### KT041 — k-Sparse Attention
* **Title:** Towards Robust Knowledge Tracing Models via k-Sparse Attention (SIGIR 2023)
* **Status:** `PRIMARY_CODED` (`FULLTEXT_CODED`)
* **Classification:** `BACKGROUND` (`G_criterion = N`, `S_criterion = N`)
* **Core Mechanisms:** Transformer sequence model with top-$k$ sparse attention softmax for noise reduction.
* **Protocol Rule Enforcement:** Enforces rule that architectural $k$-sparse attention is NOT sparse-concept educational KC evidence (`sparse_concept_ontology = SPARSE_ATTENTION_ARCHITECTURE`).
* **QA Score:** 10/16 (MODERATE 0.6250).

### KT055 — GKT-CD
* **Title:** GKT-CD: Make Cognitive Diagnosis Model Enhanced by Graph-Based Knowledge Tracing (IJCNN 2021)
* **Status:** `PRIMARY_CODED` (`FULLTEXT_CODED`)
* **Classification:** `EXCLUDE_FULLTEXT` (`kt_central_task = NO`)
* **Core Mechanisms:** Exercise-concept graph + Gated GNN for static Cognitive Diagnosis profiling.
* **Protocol Rule Enforcement:** Enforces rule that Cognitive Diagnosis enhanced by Graph-KT is excluded because its primary prediction target is static student proficiency state profiling rather than sequential KT performance prediction.
* **QA Score:** 11/16 (MODERATE 0.6875).

---

## 2. Key Methodological Patterns Identified in Wave C

| Paper ID | Corpus Tier | Graph Representation | GNN Encoder | Temporal Backbone | SSL Family | QA Score |
|---|---|---|---|---|---|---|
| KT038 | `PRIMARY_CORE` | `DYNAMIC_TEMPORAL` | `TEMPORAL_DYNAMIC_GNN` | `TEMPORAL_GRAPH_NATIVE` | `NONE` | 14/16 (0.8750) |
| KT044 | `PRIMARY_CORE` | `HETEROGENEOUS_MULTI_NODE` | `HETEROGENEOUS_GNN` | `SELF_ATTENTION_TRANSFORMER` | `NONE` | 14/16 (0.8750) |
| KT026 | `PRIMARY_CORE` | `ITEM_KC_BIPARTITE` | `NONE` | `RNN_LSTM_GRU` | `NONE` | 11/16 (0.6875) |
| KT049 | `PRIMARY_ADJACENT_SPARSE` | `NONE` | `NONE` | `RNN_LSTM_GRU` | `NONE` | 13/16 (0.8125) |
| KT041 | `BACKGROUND` | `NONE` | `NONE` | `SELF_ATTENTION_TRANSFORMER` | `NONE` | 10/16 (0.6250) |
| KT055 | `EXCLUDE_FULLTEXT` | `ITEM_KC_BIPARTITE` | `GCN` | `NONE` | `NONE` | 11/16 (0.6875) |

---

## 3. Conclusion

Wave C successfully validated all frontier boundaries of the survey scope. All 15 papers of the pilot corpus are now fully coded and synthesized. Proceed to create the **Full 15-Paper Pilot Synthesis Report** (`FULL_PILOT_SYNTHESIS_v1.0.md`).
