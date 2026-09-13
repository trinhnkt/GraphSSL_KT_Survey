# Section 1: Introduction and Motivation

## 1.1 Problem Formulation & Knowledge Tracing Definition

Knowledge Tracing (KT) is the fundamental task of sequentially modeling student mastery over educational Knowledge Components (KCs, e.g., concepts, skills, rules) based on historical learning interaction logs. Formally, given a sequence of $T$ student interaction tuples $\mathcal{X}_{1:T} = \{(x_1, r_1), (x_2, r_2), \dots, (x_T, r_T)\}$, where $x_t \in \mathcal{E}$ represents the exercise or concept attempted at time $t$, and $r_t \in \{0, 1\}$ indicates the binary response accuracy (incorrect or correct), the goal of Knowledge Tracing is to predict the response probability $P(r_{T+1} = 1 \mid x_{T+1}, \mathcal{X}_{1:T})$ on a target exercise $x_{T+1}$.

Since the seminal Deep Knowledge Tracing (DKT) model introduced Recurrent Neural Networks (RNNs) to sequence modeling in education, deep learning models—including Attention-based KT (SAKT, AKT) and Memory Network KT (DKVMN)—have dramatically improved predictive accuracy over classic psychometric baselines such as Bayesian Knowledge Tracing (BKT) and Item Response Theory (IRT).

---

## 1.2 Motivation: Challenges of Data Sparsity & Concept Cold-Start

Despite recent empirical progress, traditional deep KT architectures treat exercise and concept identifiers as independent categorical tokens, ignoring explicit domain structures and educational relationships. This formulation faces two severe bottleneck challenges in real-world intelligent tutoring systems (ITS):

1. **Representation Collapse under Interaction Data Sparsity**: In realistic educational platforms, interaction matrices are extremely sparse. Most students attempt only a tiny fraction of the overall item repository, and long-tail concepts receive minimal interaction logs. Standalone sequence models fail to learn meaningful latent embeddings for sparse concepts, leading to severe representation collapse.
2. **Strict Concept Cold-Start**: When new concepts or exercises are introduced into a curriculum without prior historical interaction logs, conventional deep KT models cannot infer student mastery. Handling zero-exposure concepts requires incorporating external structural, pedagogical, or semantic knowledge graph priors.

---

## 1.3 Scope & Gateway Criteria

To address these fundamental limitations, two primary methodological paradigms have rapidly expanded:
- **Graph-Based Knowledge Tracing (Graph-KT)**: Incorporating explicit topological structures—such as prerequisite concept trees, question-KC bipartite maps, or dynamic co-occurrence graphs—via Graph Neural Networks (GNNs).
- **Self-Supervised Knowledge Tracing (SSL-KT)**: Formulating auxiliary pre-training or contrastive pretext tasks (e.g., multi-view graph contrast, masked auto-encoding) to regularize student state representations.

Our systematic survey enforces a strict, frozen primary-corpus gateway rule:
```text
PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)
```
Only studies where Knowledge Tracing is the central prediction task AND that leverage explicit Graph-Based or Self-Supervised mechanisms are included in our primary synthesis corpus.

---

## 1.4 Primary Survey Contributions

This systematic survey provides four primary contributions to the educational data mining and machine learning literature:
1. **PRISMA 2020 Systematic Protocol**: We execute a comprehensive, transparent literature search across 7 bibliographic databases (Scopus, WoS, ACM DL, IEEE Xplore, ScienceDirect, SpringerLink, arXiv), auditing 2,017 candidate records to establish an integrated core corpus of 42 primary studies published between 2015 and 2026.
2. **Unified Taxonomy Framework**: We propose a two-dimensional structural taxonomy covering Graph-KT (GNN encoders, provenance, fusion mechanisms) and SSL-KT (pretext tasks, multi-view contrast, generative masked pre-training).
3. **Critical Audit of Sparse-Concept Protocols**: We uncover a critical methodological gap: while 95.2% of core studies motivate their models via "data sparsity", only 4.8% evaluate strict zero-exposure concept cold-start protocols.
4. **Evidence-Derived Research Agenda**: We outline 6 concrete future research pillars, highlighting LLM-GNN multimodal fusion, non-Euclidean hyperbolic state spaces, and calibrated trustworthy KT.
