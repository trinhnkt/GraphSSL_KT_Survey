# Section 4: Taxonomy and Systematic Synthesis of Self-Supervised Knowledge Tracing (RQ3)

## 4.1 Overview of Self-Supervised Knowledge Tracing

Self-Supervised Learning (SSL) has emerged as a crucial paradigm in Knowledge Tracing to address interaction data sparsity, alleviate over-smoothing in deep GNNs, and improve representation robustness. Within our primary core corpus of 42 studies, 16 papers (38.1%) incorporate self-supervised pretext objectives.

---

## 4.2 Taxonomy of SSL Pretext Objectives

We categorize SSL-KT techniques into four distinct paradigm families (Table 2):

1. **Multi-View Contrastive Learning (37.5%)**: Constructing multiple augmented structural or temporal views (e.g., prerequisite view vs. co-occurrence view) and maximizing mutual information between positive view pairs using InfoNCE loss (e.g., Bi-CLKT, 3V-CLKT, HyperKT, CMG-KT, DV-HGCL).
2. **Graph Structural Contrastive Learning (31.3%)**: Performing node, edge, or subgraph perturbations on concept graphs to regularize GNN embeddings against noise (e.g., DC-SSL, GraphCA, HKT, DV-HGCL).
3. **Hypergraph Contrastive Learning (12.5%)**: Contrasting hyperedge embeddings against node-level representations to capture high-order group interaction semantics (S2-HHN, HyperKT).
4. **Generative Masked Graph Auto-Encoding (12.5%)**: Masking concept nodes or structural edges and training a Graph Auto-Encoder (GAE) to reconstruct unobserved topology prior to downstream KT fine-tuning (e.g., Pre-train Q-Emb, GMGAE).

---

## 4.3 Data Augmentation Strategies and Educational Structure Preservation

Data augmentation in educational contexts must preserve underlying pedagogical constraints to avoid generating invalid interaction sequences:

- **Structural Perturbations**: Node masking, edge dropping, and subgraph sampling on concept prerequisite graphs.
- **Sequence Perturbations**: Item cropping, skill masking, and interaction reordering (CL4KT).
- **Counterfactual Rewiring**: Rewiring non-causal interaction edges to generate counterfactual student histories (GraphCA).
- **Educational Structure Preservation**: 100% of coded SSL-KT models explicitly enforce structural constraints (e.g., preserving prerequisite directionality and Q-matrix bipartite associations) to ensure augmented views maintain educational validity.

---

## 4.4 Synergies Between Graph Architecture and Self-Supervision

Our meta-analysis reveals a strong synergy between GNN encoders and SSL objectives:
- GNN message passing aggregates local neighborhood information but is prone to representation collapse when interaction matrices are sparse.
- Contrastive and generative SSL auxiliary losses act as structural regularizers, preventing representation collapse and boosting model transferability across sparse student interaction regimes.
