# Section 3: Taxonomy and Systematic Synthesis of Graph-Based Knowledge Tracing (RQ1 & RQ2)

## 3.1 Overview of Graph-Based Knowledge Tracing

Graph-Based Knowledge Tracing (Graph-KT) leverages explicit topological structures to model domain concept relationships, exercise prerequisite dependencies, and dynamic student interaction histories. Across our primary core corpus of 42 studies, 42 papers (100.0%) incorporate structural graph mechanisms.

---

## 3.2 Graph Sources and Provenance

We classify graph sources into four primary categories:

1. **Curriculum & Expert Concept Maps (External Fixed)**: Pre-defined domain hierarchies supplied by pedagogical experts or textbook syllabi (e.g., PDKT-C, CMKT, HHSKT, HKT, Hyper-HKT, SKM-GKT). These graphs remain fixed during model training, presenting minimal data leakage risk.
2. **Q-Matrix & Interaction Co-occurrence Graphs (Precomputed)**: Bipartite exercise-concept mappings or concept-concept co-occurrence adjacencies constructed from student response logs (e.g., GKT, GIKT, SKT, CL4KT, Bi-CLKT).
3. **Dynamic & Jointly Learned Graphs**: Graphs whose edge weights are updated continuously during model optimization via attention mechanisms or reinforcement learning policies (e.g., DyGKT, DGEKT, GraphCA, R²GCurL, STG-SKT).
4. **LLM-Extracted Semantic Graphs**: Frontier models leveraging Large Language Models to extract semantic concept trees and AST syntax dependencies from programming code (e.g., SINKT, Coda, KGNN-KT).

---

## 3.3 Topological Representations and GNN Encoders

As detailed in Table 1 (`RQ1_RQ2_GRAPH_TAXONOMY_TABLE.md`), GNN encoder architectures have evolved significantly:

- **Graph Convolutional Networks (GCN - 40.5%)**: Primary baseline for local neighborhood aggregation across concept graphs (e.g., Bi-CLKT, JKT, DGEKT, CL4KT, SINKT, Coda, DGR-KT).
- **Heterogeneous GNNs (23.8%)**: Models multi-modal educational entities (students, exercises, concepts, questions) with type-specific message passing (e.g., HHSKT, TSKT, 3V-CLKT, DC-SSL, GraphCA, MAHKT, KGNN-KT, DV-HGCL).
- **Graph Attention Networks (GAT - 11.9%)**: Dynamic attention weighting over concept neighbors (e.g., GIKT, SKT, LST-Graph, CMG-KT).
- **Hypergraph Neural Networks (4.8%)**: Captures non-pairwise, high-order co-occurrence hyperedges connecting multiple concepts simultaneously (e.g., S2-HHN, HyperKT).
- **Hyperbolic GNNs (2.4%)**: Embeds hierarchical concept trees into non-Euclidean Poincaré ball manifolds, preventing representation distortion in deep trees (Hyper-HKT).
- **Dynamic & Spatiotemporal GNNs (7.1%)**: Models time-evolving interaction streaming windows (DyGKT, R²GCurL, STG-SKT).

---

## 3.4 Temporal Backbones and Graph–Sequence Fusion

Graph representations are integrated into temporal sequence backbones to track evolving student knowledge states over time:

- **Recurrent Neural Networks (RNN/LSTM/GRU - 64.3%)**: Dominant sequential backbone injecting graph embeddings into recurrent hidden state transition loops.
- **Self-Attention Transformers (31.0%)**: Injects graph structural biases into self-attention key-value matrices (e.g., Bi-CLKT, CL4KT, SINKT, DC-SSL, HKT, CMG-KT, DGR-KT, GMGAE).
- **Continuous-Time Hawkes Processes (2.4%)**: Models continuous time intervals and self-exciting concept decay dynamics (STHKT).
