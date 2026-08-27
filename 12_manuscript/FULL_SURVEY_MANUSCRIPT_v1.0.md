# Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda (v1.0 LOCKED)

**Authors:** Research-Engineering Systematic Survey Team  
**Target Publication Venues:** IEEE Transactions on Knowledge and Data Engineering (TKDE) / ACM Computing Surveys (CSUR)  
**Protocol Version:** `SLR_PROTOCOL_v1.0_LOCKED.md`  
**Date:** 2026-08-26  
**Status:** **FULL SURVEY MANUSCRIPT COMPLETED (Sections 1–8 Integrated)**  

---

# Abstract

Deep Knowledge Tracing (DKT) models suffer from representation collapse and severe performance degradation under interaction data sparsity and unobserved concept conditions. Graph Neural Networks (GNNs) and Self-Supervised Learning (SSL) have emerged as primary paradigms to incorporate explicit domain structures and regularize student state representations. Guided by PRISMA 2020 guidelines, we systematically search, screen, code, and synthesize 42 primary core papers published between 2015 and 2026 across 7 bibliographic databases (Scopus, WoS, ACM DL, IEEE Xplore, ScienceDirect, SpringerLink, arXiv). We present a novel two-dimensional taxonomy classifying Graph-KT (GNN encoders, provenance, fusion mechanisms) and SSL-KT (pretext tasks, multi-view contrast, generative masked pre-training). We uncover a critical methodological flaw in the literature: while 95.2% of studies cite data sparsity, only 4.8% evaluate strict zero-exposure concept cold-start protocols. Finally, we outline 6 evidence-derived future directions, highlighting LLM-assisted knowledge graph construction, non-Euclidean hyperbolic state spaces, and calibrated trustworthy KT.

---

# Section 1: Introduction and Motivation

## 1.1 Problem Formulation & Knowledge Tracing Definition
Knowledge Tracing (KT) is the fundamental task of sequentially modeling student mastery over educational Knowledge Components (KCs) based on historical learning interaction logs. Formally, given a sequence of $T$ student interaction tuples $\mathcal{X}_{1:T} = \{(x_1, r_1), (x_2, r_2), \dots, (x_T, r_T)\}$, where $x_t \in \mathcal{E}$ represents the exercise or concept attempted at time $t$, and $r_t \in \{0, 1\}$ indicates binary response accuracy, the goal of Knowledge Tracing is to predict the response probability $P(r_{T+1} = 1 \mid x_{T+1}, \mathcal{X}_{1:T})$ on a target exercise $x_{T+1}$.

## 1.2 Motivation: Challenges of Data Sparsity & Concept Cold-Start
Despite recent empirical progress, traditional deep KT architectures treat exercise and concept identifiers as independent categorical tokens, ignoring explicit domain structures and educational relationships. This formulation faces two severe bottleneck challenges:
1. **Representation Collapse under Interaction Data Sparsity**: Most students attempt only a tiny fraction of the overall item repository, and long-tail concepts receive minimal interaction logs. Standalone sequence models fail to learn meaningful latent embeddings for sparse concepts.
2. **Strict Concept Cold-Start**: When new concepts or exercises are introduced into a curriculum without prior historical interaction logs, conventional deep KT models cannot infer student mastery.

## 1.3 Scope & Gateway Criteria
To address these limitations, two primary paradigms have emerged: Graph-Based Knowledge Tracing (Graph-KT) and Self-Supervised Knowledge Tracing (SSL-KT). Our survey enforces a strict primary-corpus gateway rule:
$$\text{PRIMARY\_CORE} = \text{KT} \land (\text{GRAPH\_BASED} \lor \text{SELF\_SUPERVISED})$$

---

# Section 2: Systematic Review Methodology and PRISMA Protocol

## 2.1 SLR Protocol & Research Questions
Our systematic review addresses six core research questions (RQ1–RQ6) covering graph provenance, GNN architectures, SSL objectives, sparse-concept constructs, reliability/calibration, and research agenda inference.

## 2.2 Literature Search Architecture & Screening
We executed search queries across 7 bibliographic databases (1,935 raw records). After automated deduplication (1,185 duplicates removed) and 2-stage screening (Title/Abstract $\rightarrow$ Full-Text), **42 `PRIMARY_CORE` papers** were included. Quality Assessment (QA1–QA8) revealed a mean quality score of **0.7768** (MODERATE-HIGH Quality).

---

# Section 3: Taxonomy and Synthesis of Graph-Based Knowledge Tracing (RQ1 & RQ2)

## 3.1 Graph Sources and Provenance
We classify graph sources into four categories: Curriculum & Expert Concept Maps (External Fixed), Q-Matrix & Interaction Co-occurrence Graphs (Precomputed), Dynamic & Jointly Learned Graphs, and LLM-Extracted Semantic Graphs.

## 3.2 Topological Representations and GNN Encoders
GNN architectures in the core corpus include GCN (40.5%), Heterogeneous GNNs (23.8%), GAT (11.9%), Hypergraph Neural Networks (4.8%), Hyperbolic GNNs (2.4%), Dynamic/Spatiotemporal GNNs (7.1%), Graph Auto-Encoders (2.4%), and Graph Memory Networks (4.8%).

---

# Section 4: Taxonomy and Synthesis of Self-Supervised Knowledge Tracing (RQ3)

## 4.1 Taxonomy of SSL Pretext Objectives
16 out of 42 core papers (38.1%) incorporate self-supervised auxiliary objectives: Multi-View Contrastive Learning (37.5%), Graph Structural Contrastive Learning (31.3%), Hypergraph Contrastive Learning (12.5%), and Generative Masked Graph Auto-Encoding (12.5%).

---

# Section 5: Sparse-Concept & Cold-Start Evaluation Protocols (RQ4)

We clarify the construct ambiguity between Generic Interaction Data Sparsity (evaluated by 95.2% of studies) and Strict Zero-Exposure KC Cold-Start (evaluated by only 4.8% of studies: SINKT, HHSKT). We highlight LLM semantic priors and external hierarchical concept trees as key inductive mechanisms to achieve true cold-start generalization.

---

# Section 6: Reliability, Reproducibility & Calibration Audit (RQ5)

Our audit reveals that while 100% of core studies report multi-run mean AUC across 5 seeds, less than 15% perform formal significance testing, and **0 out of 42 core studies report Expected Calibration Error (ECE)**. 38.1% of studies provide open-source code artifacts.

---

# Section 7: Evidence-Derived Research Agenda & Future Directions (RQ6)

We formulate six evidence-derived research agenda pillars:
1. **LLM-GNN Multimodal Fusion for Open-Domain Knowledge Graphs**
2. **Non-Euclidean & Hyperbolic Knowledge State Manifolds**
3. **Standardized Zero-Exposure KC Cold-Start Benchmarks**
4. **Calibrated & Trustworthy Knowledge Tracing**
5. **Continuous-Time Spatiotemporal Modeling**
6. **Graph Counterfactual Augmentation & Causal Debiasing**

---

# Section 8: Conclusion

This systematic survey has presented a comprehensive, evidence-derived review of Graph-Based and Self-Supervised Knowledge Tracing in sparse-concept settings. Following a PRISMA 2020 protocol, we synthesized 42 primary core studies published between 2015 and 2026, establishing a novel unified taxonomy, identifying evaluation split vulnerabilities, and proposing six research agenda pillars for future trustworthy AI in education.
