# Master Survey Manuscript Outline (v1.0 LOCKED)

**Working Title:** Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda  
**Target Venues:** IEEE Transactions on Knowledge and Data Engineering (TKDE) / ACM Computing Surveys (CSUR)  
**Protocol Version:** `SLR_PROTOCOL_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# Abstract
- **Background & Motivation**: Deep Knowledge Tracing (DKT) models suffer from representation collapse and performance degradation under data sparsity and unobserved concept conditions. Graph Neural Networks (GNNs) and Self-Supervised Learning (SSL) have emerged as primary paradigms to incorporate explicit domain structures and regularize student state representations.
- **Methodology**: Guided by PRISMA 2020 guidelines, we systematically search, screen, code, and synthesize 42 primary core papers published between 2015 and 2026 across 7 bibliographic databases.
- **Key Findings**: We present a novel unified taxonomy classifying Graph-KT (GNN encoders, provenance, fusion mechanisms) and SSL-KT (pretext tasks, multi-view contrast, generative masked pre-training). We uncover a critical methodological flaw in the literature: while 95.2% of studies cite data sparsity, only 4.8% evaluate strict zero-exposure concept cold-start protocols.
- **Research Agenda**: We outline 6 evidence-derived future directions, highlighting LLM-assisted knowledge graph construction, non-Euclidean hyperbolic state spaces, and rigorous calibration benchmarks.

---

# Table of Contents & Section Structure

1. **Section 1: Introduction**
   - 1.1 Problem Formulation & Knowledge Tracing Definition
   - 1.2 Motivation: Challenges of Data Sparsity & Cold-Start Concepts
   - 1.3 Scope & Key Gateway Criteria (`PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)`)
   - 1.4 Primary Survey Contributions & Comparison with Prior Surveys

2. **Section 2: Review Methodology & PRISMA Search Protocol**
   - 2.1 SLR Protocol & Research Questions (RQ1–RQ6)
   - 2.2 Literature Search Architecture & 7 Database Executions
   - 2.3 PRISMA 2020 Flow Diagram & Study Eligibility Screening
   - 2.4 Three-Level Coding Scheme & Quality Assessment (QA1–QA8)

3. **Section 3: Taxonomy & Synthesis of Graph-Based Knowledge Tracing (RQ1 & RQ2)**
   - 3.1 Graph Sources & Provenance (Curriculum Trees, Co-occurrence, LLM Semantic Graphs)
   - 3.2 Graph Representation & Topological Properties (Homogeneous, Heterogeneous, Hypergraph, Hyperbolic)
   - 3.3 Graph Neural Network Encoders (GCN, GAT, Dynamic GNN, Graph Memory, Optimal Transport)
   - 3.4 Temporal Backbones & Graph–Sequence Fusion Mechanisms

4. **Section 4: Taxonomy & Synthesis of Self-Supervised Knowledge Tracing (RQ3)**
   - 4.1 Pretext Tasks & Auxiliary Loss Objectives
   - 4.2 Multi-View & Graph Structural Contrastive Learning
   - 4.3 Generative Masked Graph Auto-Encoders
   - 4.4 Data Augmentation & Educational Structure Preservation

5. **Section 5: Sparse-Concept & Cold-Start Evaluation Protocols (RQ4)**
   - 5.1 Construct Definitions: Generic Interaction Sparsity vs Strict Zero-Exposure KC Cold-Start
   - 5.2 Methodological Audit: Evaluation Split Vulnerabilities in Existing Literature
   - 5.3 Benchmarking Inductive Knowledge Tracing with LLM & Graph Priors

6. **Section 6: Reliability, Reproducibility & Calibration (RQ5)**
   - 6.1 Quality Assessment & QA Score Distribution
   - 6.2 Statistical Rigor, Multi-Seed Reporting & Data Split Resampling
   - 6.3 Open-Source Code Artifacts & Computational Complexity Benchmarking

7. **Section 7: Evidence-Derived Research Agenda & Future Directions (RQ6)**
   - 7.1 LLM-GNN Multimodal Fusion for Semantic Graph Construction
   - 7.2 Non-Euclidean & Hyperbolic Knowledge State Embeddings
   - 7.3 Standardized Zero-Exposure Cold-Start Benchmarks
   - 7.4 Calibrated & Trustworthy Knowledge Tracing

8. **Section 8: Conclusion**
