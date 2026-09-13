# SSL & SPARSE COLD-START TAXONOMY AUDIT REPORT (Task A6)

**Target Journal:** IEEE Transactions on Learning Technologies (IEEE TLT)  
**Audit Date:** 2026-09-12  
**Status:** **AUDITED & VERIFIED (100% Coding Reconciled)**  

---

## 1. SSL-KT Taxonomy Summary ( = 14$ Verified Core Papers)

- **Total SSL Primary Core Papers:** **14**
- **CL4KT (KT039) Structure Preservation:** Explicitly set to NO_EXPLICIT_CONSTRAINT (CL4KT applies domain-agnostic sequence crop/reorder/mask augmentations without graph priors).
- **SSL Families Breakdown:**
  - MULTIVIEW_CONTRASTIVE: 2 (Bi-CLKT, 3V-CLKT)
  - GRAPH_CONTRASTIVE: 2 (DC-SSL, GraphCA)
  - HYPERGRAPH_CONTRASTIVE: 2 (S2-HHN, HyperKT)
  - SEQUENCE_CONTRASTIVE: 1 (CL4KT)
  - GRAPH_EMBEDDING_PRETRAINING: 2 (PEBG/KT026, KGNN-KT/KT076)
  - HIERARCHICAL_CONTRAST: 1 (HKT)
  - DEBIASED_CONTRASTIVE: 1 (Coda)
  - STRUCTURE_AWARE_INDUCTIVE: 1 (SINKT)
  - REINFORCED_CURRICULUM_SSL: 1 (R2GCurL)
  - SPATIOTEMPORAL_SSL: 1 (STG-SKT)

---

## 2. Sparse & Cold-Start Protocol Audit ( = 37$ Core Papers)

- **Denominator:** Paper-level ( = 37$).
- **Multi-label / Non-mutually exclusive categories:**
  - **Citing Interaction Data Sparsity:** 35 / 37 (**94.6%**)
  - **Evaluating Interaction Sparsity Drop (Random Subsampling):** 35 / 37 (**94.6%**)
  - **Evaluating Item / Question Cold-Start:** 3 / 37 (**8.1%**) (PEBG, SINKT, KGNN-KT)
  - **Evaluating Strict Zero-Exposure Concept Cold-Start:** 2 / 37 (**5.4%**) (SINKT, HHSKT partial)
- **Methodological Vulnerability Finding:** While 94.6% of studies claim data sparsity as primary motivation, only **5.4%** conduct rigorous zero-exposure unobserved concept cold-start evaluations.
