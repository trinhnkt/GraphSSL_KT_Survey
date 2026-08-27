# Section 5: Sparse-Concept & Cold-Start Evaluation Protocols (RQ4)

## 5.1 Construct Definitions: Generic Data Sparsity vs. Strict Zero-Exposure KC Cold-Start

A central contribution of our survey is clarifying the construct ambiguity surrounding "sparsity" in Knowledge Tracing literature. We distinguish between two fundamentally different evaluation settings:

1. **Generic Interaction Data Sparsity**: Evaluation splits where student interaction logs are randomly partitioned (e.g., 80/20 train/test learner split or random response masking). While the overall interaction matrix is sparse, **every Knowledge Component (KC) and exercise appears multiple times in the training split**. 40 out of 42 core studies (95.2%) evaluate exclusively under generic interaction data sparsity (Table 3).
2. **Strict Zero-Exposure KC Cold-Start**: Evaluation splits where a subset of Knowledge Components or exercises is **completely withheld from training interaction logs** (zero training exposure). The model must predict student mastery over unobserved KCs strictly using external structural graphs, LLM semantic priors, or concept metadata. Only 2 core studies (**SINKT**, **HHSKT**) and 1 primary-adjacent paper (**KT049**) isolate strict zero-exposure cold-start protocols.

---

## 5.2 Methodological Audit of Evaluation Split Vulnerabilities

Our audit reveals a pervasive methodological vulnerability in existing Graph/SSL KT literature:

- **Data Leakage in Co-Occurrence Graphs**: Many studies construct concept co-occurrence or item similarity graphs using the *entire interaction dataset* before partitioning student logs into train/test sets (e.g., SKT, CL4KT, Bi-CLKT, GASKT). This introduces subtle data leakage, as test set co-occurrence patterns influence graph adjacency weights during GNN propagation.
- **Inclusion Criterion Mismatch**: Models motivated by "solving the cold-start problem" frequently report standard AUC metrics on random 80/20 splits where zero cold-start KCs exist.

---

## 5.3 Benchmarking Inductive Knowledge Tracing with LLM & Graph Priors

To achieve true zero-exposure cold-start capability, frontier Graph-KT models employ two primary inductive mechanisms:

1. **External Hierarchical Knowledge Maps**: HHSKT utilizes domain concept hierarchies to map zero-exposure KCs to parent/sibling nodes in a heterogeneous GNN, inferring initial mastery states through structural message passing.
2. **LLM Semantic Embedding Priors**: SINKT and KGNN-KT leverage Large Language Models (e.g., GPT-4, Llama) to convert exercise text descriptions and code AST syntax into continuous semantic embeddings. When a new exercise is introduced, its LLM embedding is projected into the trained GNN state space without requiring historical student interaction logs.
