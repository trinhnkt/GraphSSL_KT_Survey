# KT035 (HHSKT) FULL-TEXT AUDIT REPORT (Task A5)

**Paper:** *HHSKT: A learner-question interactions based heterogeneous graph neural network model for knowledge tracing* (Zhou et al., ESWA 2023)  
**Model Name:** HHSKT  
**Audit Date:** 2026-09-12  

---

## 1. Full-Text Architectural Coding Verification

- **Graph Source:** `HETEROGENEOUS_SCHEMA` (Learner-Question-Concept 3-node schema)
- **Graph Provenance:** `MODEL_DEFINED_FIXED`
- **Graph Representation:** `STUDENT_EXERCISE_KC` (Tripartite heterogeneous graph)
- **Node & Edge Types:** 3 Node types (Student, Question, Concept); Multiple edge types (attempts, belongs-to)
- **GNN Encoder:** `HETEROGENEOUS_GNN` (Relation-level attention)
- **Temporal Backbone:** `RNN_LSTM_GRU`
- **Fusion Type:** `ATTENTIVE_FUSION`
- **Evaluation Datasets:** ASSISTments2009, ASSISTments2017, Junyi

---

## 2. Sparse-Concept & Cold-Start Protocol Audit

- **Interaction Sparsity Evaluation:** HHSKT evaluates performance under interaction sparsity by dropping percentage of interaction records ($20\%, 40\%, 60\%, 80\%$).
- **Strict Zero-Exposure Concept Cold-Start Evaluation:** **NO**. HHSKT does NOT isolate zero-exposure unobserved concept split protocols.
- **Taxonomy Protocol Classification:** `SPARSE_INTERACTION_ONLY` (not strict zero-exposure).
