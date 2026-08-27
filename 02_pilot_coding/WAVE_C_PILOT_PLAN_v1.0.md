# WAVE_C_PILOT_PLAN_v1.0

## Status
**Approved Pilot Wave C Plan — Active for Execution**

---

## 1. Objectives of Wave C

Pilot Wave C focuses on the remaining difficult frontiers of the systematic survey protocol (`SCOPE_v1.0_LOCKED.md` & `coding_codebook_v0.4_PILOT.md`):
1. **Sparse-Concept Lens & Strict KC Cold-Start:** Stress-testing the separation between zero-exposure training interaction history and external graph/semantic/LLM information.
2. **LLM-Enhanced Graph/SSL-KT:** Coding LLM semantic auxiliary features without confusing them with temporal backbone or GNN encoders.
3. **Dynamic Graph Learning:** Coding temporal edge evolution and temporal split leakage risk.
4. **Boundary & Exclusion Adjudication:** Enforcing the gateway rules for `PRIMARY_ADJACENT`, `BACKGROUND` (sparse-attention ambiguity), and `EXCLUDE` (cognitive diagnosis task eligibility).

---

## 2. Selected Papers for Wave C

| # | Paper ID | Title / Venue | Target Corpus Tier | Primary Pilot Role | Key Dimensions to Stress-Test |
|---:|---|---|---|---|---|
| 1 | **KT038** | DyGKT: Dynamic Graph Learning for Knowledge Tracing (KDD 2024) | `PRIMARY_CORE` | Dynamic Graph | `DYNAMIC_TEMPORAL` graph representation, `TEMPORAL_DYNAMIC_GNN`, metadata conflict workflow, temporal split isolation. |
| 2 | **KT044** | SINKT: A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model (CIKM 2024) | `PRIMARY_CORE` | Strict KC Cold-Start + LLM | `STRICT_KC_COLD_START` construct validity, `LLM_ASSISTED` graph source, inductive graph representation for unseen KCs. |
| 3 | **KT026** | Improving Knowledge Tracing via Pre-Training Question Embeddings (IJCAI 2020) | `PRIMARY_CORE` | Graph Gateway vs Generic Pretraining | Pretraining vs SSL rule, graph-derived question pretraining, bipartite graph boundary. |
| 4 | **KT049** | Mitigating Cold-Start Problems in Knowledge Tracing with Large Language Models (CIKM 2024) | `PRIMARY_ADJACENT` | Adjacent Sparse / Cold-Start Case | `PRIMARY_ADJACENT_SPARSE` classification, zero-train exposure context without forcing Graph/SSL gateway. |
| 5 | **KT041** | Towards Robust Knowledge Tracing Models via k-Sparse Attention (SIGIR 2023) | `BACKGROUND` | Sparse-Attention Ambiguity Boundary | Rule enforcement: `k-sparse attention` architecture is NOT sparse-concept KC evidence (`BACKGROUND`). |
| 6 | **KT055** | GKT-CD: Make Cognitive Diagnosis Model Enhanced by Graph-Based Knowledge Tracing (IJCNN 2021) | `EXCLUDE_FULLTEXT` | Task Eligibility Boundary | Rule enforcement: Cognitive Diagnosis with Graph-KT enhancement is NOT a KT central task (`EXCLUDE`). |

---

## 3. Execution Sequence & Roadmap

```text
KT038 (Dynamic Graph) 
  └── KT044 (Strict Cold-Start + LLM) 
        └── KT026 (Graph Gateway vs Pretraining) 
              └── KT049 (Primary Adjacent Sparse) 
                    └── KT041 (Sparse Attention Boundary) 
                          └── KT055 (Task Eligibility Exclusion)
```

---

## 4. Specific Protocol Rules & Safeguards to Stress-Test in Wave C

### Rule 1: Strict KC Cold-Start vs External LLM Semantics (KT044 & KT049)
* **Rule:** Strict KC cold-start requires **zero training-interaction exposure** for target KCs.
* **Coding Requirement:** External semantic descriptions, text embeddings, or LLM prompt structures supplied for cold-start KCs must be coded in `graph_source = LLM_ASSISTED, SEMANTIC_TEXT` or auxiliary inputs, **not** as interaction history exposure.

### Rule 2: LLM Feature Provider vs Temporal Backbone
* **Rule:** LLM modules that provide text/concept representations are static/auxiliary feature providers, **not** the `temporal_backbone`.
* **Coding Requirement:** Specify `temporal_backbone` as `RNN_LSTM_GRU` or `SELF_ATTENTION_TRANSFORMER` as used for time-series state tracking, placing LLMs in auxiliary encoder slots.

### Rule 3: Sparse Attention Architecture Ambiguity (KT041)
* **Rule:** Sparse attention mechanisms (e.g., $k$-sparse attention, sparse softmax) are architectural sparsity constraints, **not** sparse-concept (long-tail KC / cold-start) educational evidence.
* **Coding Requirement:** Classify KT041 as `BACKGROUND` with `sparse_concept_ontology = SPARSE_ATTENTION_ARCHITECTURE`.

### Rule 4: Task Eligibility Exclusion (KT055)
* **Rule:** The primary target task must be Knowledge Tracing (predicting sequential student performance). Cognitive diagnosis (static proficiency profiling) enhanced by KT is excluded.
* **Coding Requirement:** Classify KT055 as `EXCLUDE_FULLTEXT` with `kt_central_task = NO`.

---

## 5. Expected Artifacts for Wave C

For each paper:
1. `02_pilot_coding/wave_C/<PAPER_ID>/<PAPER_ID>_CODING_v0.4.md`
2. `02_pilot_coding/wave_C/<PAPER_ID>/<PAPER_ID>_FIELD_EVIDENCE_v0.4.md`

Upon completion of all 6 papers:
- `02_pilot_coding/WAVE_C_REVIEW_v0.4.md`
- `02_pilot_coding/FULL_PILOT_SYNTHESIS_v1.0.md` (15-paper pilot synthesis report preparing codebook freezing `coding_codebook_v1.0_LOCKED.md`).
