# Taxonomy Table 3: Sparse-Concept & Cold-Start Evaluation Protocols (RQ4)

Comprehensive systematic taxonomy table evaluating sparse-concept and cold-start evaluation protocols across the survey corpus.

---

| Paper ID | Model Name | Sparse Construct Claim | Zero-Exposure KC Split? | Evaluation Split Protocol | External Graph Semantic Input? | Benchmark Datasets Evaluated | Methodological Vulnerability Note |
|---|---|---|---|---|---|---|---|
| **KT035** | HHSKT | Hierarchical Sparse KC | **YES** | Strict Zero-Exposure KC Split | External Hierogeneous Graph | ASSISTments2009, EdNet | Rigorous zero-exposure KC cold-start evaluation |
| **KT044** | SINKT | Inductive KC Cold-Start | **YES** | Strict Zero-Exposure KC Split | LLM Semantic Embeddings | ASSISTments2009, ASSISTments2017 | Rigorous inductive KC cold-start with LLMs |
| **KT049** | Inductive-KT | Inductive Question Cold-Start | **YES** | Strict Zero-Exposure Question Split | External Question Metadata | ASSISTments2009, EdNet | Primary-adjacent question cold-start benchmark |
| **KT004** | GKT | Interaction Sparsity | **NO** | Generic Learner Split | Co-occurrence Graph | ASSISTments2009, Statics2011 | Fails to isolate unobserved KCs |
| **KT010** | GIKT | Interaction Sparsity | **NO** | Generic Learner Split | Interaction Graph | ASSISTments2009, ASSISTments2017 | Fails to isolate unobserved KCs |
| **KT011** | Bi-CLKT | Data Sparsity | **NO** | Generic Learner Split | Dual Graph | ASSISTments2009, EdNet | Fails to isolate unobserved KCs |
| **KT012** | JKT | Data Sparsity | **NO** | Generic Learner Split | Similarity Graph | ASSISTments2009, Statics2011 | Fails to isolate unobserved KCs |
| **KT026** | Pre-train Q-Emb | Data Sparsity | **NO** | Generic Learner Split | Question Graph | ASSISTments2009, Junyi | Fails to isolate unobserved KCs |
| **KT038** | DyGKT | Dynamic Data Sparsity | **NO** | Generic Learner Split | Dynamic Graph | ASSISTments2009, ASSISTments2017 | Fails to isolate unobserved KCs |
| **KT039** | CL4KT | Interaction Sparsity | **NO** | Generic Learner Split | Co-occurrence Graph | ASSISTments2009, Statics2011 | Fails to isolate unobserved KCs |
| **KT066** | HyperKT | High-order Data Sparsity | **NO** | Generic Learner Split | Adaptive Hypergraph | ASSISTments2009, ASSISTments2017 | Fails to isolate unobserved KCs |
| **KT068** | HKT | Hierarchical Data Sparsity | **NO** | Generic Learner Split | Hierarchical Graph | ASSISTments2009, ASSISTments2017 | Fails to isolate unobserved KCs |
| **KT076** | KGNN-KT | Code Data Sparsity | **NO** | Generic Learner Split | Knowledge Graph + LLM | CodeNet, OJ | Fails to isolate unobserved KCs |
| **KT077** | R²GCurL | Robust Data Sparsity | **NO** | Generic Learner Split | Curriculum Graph | ASSISTments2009, ASSISTments2017 | Fails to isolate unobserved KCs |
| **KT078** | CMG-KT | Multi-view Data Sparsity | **NO** | Generic Learner Split | Multi-view Graph | ASSISTments2009, Junyi | Fails to isolate unobserved KCs |
| **KT081** | Hyper-HKT | Hierarchical Data Sparsity | **NO** | Generic Learner Split | Hyperbolic Tree Graph | ASSISTments2009, EdNet | Fails to isolate unobserved KCs |
| **KT082** | GMGAE | Pre-training Data Sparsity | **NO** | Generic Learner Split | Graph Auto-Encoder | ASSISTments2009, EdNet | Fails to isolate unobserved KCs |
| **KT083** | DV-HGCL | Heterogeneous Data Sparsity| **NO** | Generic Learner Split | Dual-View Graph | ASSISTments2009, ASSISTments2017 | Fails to isolate unobserved KCs |
