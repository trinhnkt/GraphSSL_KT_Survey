# Meta-Analysis Quantitative Statistics Report (v1.0 LOCKED)

**Survey Title:** Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda  
**Scope Version:** `SCOPE_v1.0_LOCKED.md`  
**Protocol Version:** `SLR_PROTOCOL_v1.0_LOCKED.md`  
**Date:** 2026-08-26  
**Status:** **SYNTHESIZED OVER ALL 42 `PRIMARY_CORE` PAPERS**  

---

# 1. Corpus Distribution & Gateway Classification

| Category | Count | Percentage | Key Exemplars |
|---|---|---|---|
| **Graph-Based ONLY (`G=Y, S=N`)** | 26 | 61.9% | GKT, GIKT, PDKT-C, JKT, SKT, SGKT, DGEKT, DyGKT, SINKT, STHKT, Coda, KGNN-KT, R²GCurL, STG-SKT, DGR-KT, Hyper-HKT |
| **Self-Supervised ONLY (`G=N, S=Y`)** | 0 | 0.0% | *(All SSL papers in primary core leverage graph structures)* |
| **Dual Graph + SSL (`G=Y, S=Y`)** | 16 | 38.1% | CL4KT, Bi-CLKT, S2-HHN, Pre-train Q-Emb, HyperKT, 3V-CLKT, DC-SSL, GraphCA, HKT, CMG-KT, GMGAE, DV-HGCL |
| **Total Primary Core Corpus** | **42** | **100.0%** | Comprehensive Systematic Core Corpus |

---

# 2. Graph Neural Network (GNN) Encoder Distribution (RQ1)

| GNN Encoder Architecture | Count | Percentage | Model Instances |
|---|---|---|---|
| **Graph Convolutional Network (GCN)** | 17 | 40.5% | Bi-CLKT, JKT, Pre-train Q-Emb, DGEKT, KSG-AKT, CL4KT, SINKT, GASKT, STHKT, LGS-KT, MG-Ensemble, CS-GKT, SKM-GKT, Coda, DGR-KT |
| **Heterogeneous GNN** | 10 | 23.8% | HHSKT, TSKT, 3V-CLKT, DC-SSL, GraphCA, MAHKT, HKT, KGNN-KT, DV-HGCL |
| **Graph Attention Network (GAT)** | 5 | 11.9% | GIKT, SKT, LST-Graph, CMG-KT |
| **Hypergraph Neural Network** | 2 | 4.8% | S2-HHN, HyperKT |
| **Dynamic / Spatiotemporal GNN** | 3 | 7.1% | DyGKT, R²GCurL, STG-SKT |
| **Hyperbolic GNN** | 1 | 2.4% | Hyper-HKT |
| **Graph Auto-Encoder (GAE)** | 1 | 2.4% | GMGAE |
| **Graph Memory / Optimal Transport** | 2 | 4.8% | DGMN, AEGOT-CDKT |
| **Explicit Graph Matrix (No GNN)** | 1 | 2.4% | PDKT-C, CMKT |

---

# 3. Temporal Backbone Architecture Distribution (RQ2)

| Temporal Backbone | Count | Percentage | Model Instances |
|---|---|---|---|
| **Recurrent Neural Networks (RNN / LSTM / GRU)** | 27 | 64.3% | GKT, GIKT, JKT, PDKT-C, SKT, SGKT, Pre-train Q-Emb, DGEKT, HHSKT, TSKT, CMKT, DyGKT, S2-HHN, 3V-CLKT, GraphCA, Capsule GNN, LST-Graph, LGS-KT, MAHKT, MG-Ensemble, CS-GKT, SKM-GKT, AEGOT-CDKT, Coda, KGNN-KT, R²GCurL, STG-SKT, Hyper-HKT, DV-HGCL |
| **Self-Attention Transformer** | 13 | 31.0% | Bi-CLKT, KSG-AKT, CL4KT, SINKT, DC-SSL, GASKT, HyperKT, HKT, CMG-KT, DGR-KT, GMGAE |
| **Memory Network** | 1 | 2.4% | DGMN |
| **Continuous Hawkes Process** | 1 | 2.4% | STHKT |

---

# 4. Self-Supervised Learning (SSL) Taxonomy Distribution (RQ3)

| SSL Family / Objective | Count | Percentage | Model Instances |
|---|---|---|---|
| **Multi-View Contrastive Learning** | 6 | 37.5% | Bi-CLKT, 3V-CLKT, HyperKT, CMG-KT, DV-HGCL |
| **Graph Structural Contrastive Learning** | 5 | 31.3% | DC-SSL, GraphCA, HKT, DV-HGCL |
| **Hypergraph Contrastive Learning** | 2 | 12.5% | S2-HHN, HyperKT |
| **Sequence-Level Contrastive Learning** | 1 | 6.3% | CL4KT |
| **Masked Pre-training / Generative GAE** | 2 | 12.5% | Pre-train Q-Embed, GMGAE |
| **Total SSL-Enhanced Models** | **16** | **100.0%** | 38.1% of entire Primary Core Corpus |

---

# 5. Sparse-Concept & Cold-Start Protocol Distribution (RQ4)

| Sparsity Evaluation Protocol | Count | Percentage | Methodological Evaluation Notes |
|---|---|---|---|
| **Strict Zero-Exposure KC Cold-Start Split** | 2 | 4.8% | SINKT, HHSKT (Isolates unobserved Knowledge Components) |
| **Generic Interaction Data Sparsity Split** | 40 | 95.2% | Random learner/interaction split without zero-exposure KC isolation |

---

# 6. Quality Assessment (QA1–QA8) & Reliability Statistics (RQ5)

| QA Score Metric | Score Distribution | Percentage |
|---|---|---|
| **HIGH Quality ($\ge 0.80$)** | 18 papers | 42.9% |
| **MODERATE Quality ($0.55 - 0.79$)** | 24 papers | 57.1% |
| **LIMITED Quality ($< 0.55$)** | 0 papers | 0.0% |
| **Mean Normalized Quality Score** | **0.7768** | **MODERATE-HIGH Quality** |

---

# 7. Public Dataset Usage Distribution

| Educational Benchmark Dataset | Usage Count | Percentage of Papers |
|---|---|---|
| **ASSISTments2009** | 34 | 81.0% |
| **ASSISTments2017** | 22 | 52.4% |
| **EdNet** | 16 | 38.1% |
| **Statics2011** | 12 | 28.6% |
| **Junyi Academy** | 9 | 21.4% |
| **CodeNet / OJ Programming** | 5 | 11.9% |
