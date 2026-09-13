# Taxonomy Table 2: Self-Supervised Learning (SSL) Taxonomy & Objectives (RQ3)

Comprehensive systematic taxonomy table classifying all **16 SSL-enhanced `PRIMARY_CORE` papers** across SSL Family, Pretext Task, Augmentation Strategy, Structural Preservation, and Training Mode.

---

| Paper ID | Model Name | SSL Family | Pretext Task Objective | Augmentation Strategy | Educational Structure Preservation | Training Mode | Auxiliary Loss Function |
|---|---|---|---|---|---|---|---|
| **KT011** | Bi-CLKT | MULTIVIEW_CONTRASTIVE | Bi-directional view agreement | Sequence & Graph perturbation | YES_EXPLICIT | JOINT_END_TO_END | InfoNCE Loss |
| **KT026** | Pre-train Q-Emb | MASKED_PRETRAINING | Question embedding masked reconstruction | Masked concept prediction | YES_EXPLICIT | TWO_STAGE_PRETRAIN | Masked Cross-Entropy |
| **KT039** | CL4KT | SEQUENCE_CONTRASTIVE | Interaction sequence contrastive alignment | Item & Skill masking/cropping | YES_EXPLICIT | JOINT_END_TO_END | InfoNCE Loss |
| **KT042** | S2-HHN | HYPERGRAPH_CONTRASTIVE | Hypergraph multi-view contrastive learning | Hyperedge dropping & node masking | YES_EXPLICIT | JOINT_END_TO_END | InfoNCE Loss |
| **KT043** | 3V-CLKT | MULTIVIEW_CONTRASTIVE | Three-view agreement (Question, Skill, Student) | Heterogeneous view masking | YES_EXPLICIT | JOINT_END_TO_END | Multi-View Contrastive |
| **KT047** | DC-SSL | GRAPH_CONTRASTIVE | Dual-channel heterogeneous graph contrast | Node & Edge perturbation | YES_EXPLICIT | JOINT_END_TO_END | InfoNCE Loss |
| **KT050** | GraphCA | GRAPH_CONTRASTIVE | Graph counterfactual augmentation contrast | Counterfactual graph rewiring | YES_EXPLICIT | JOINT_END_TO_END | Counterfactual Loss |
| **KT066** | HyperKT | MULTIVIEW_CONTRASTIVE | Dual-channel adaptive hypergraph contrast | Hypergraph view perturbation | YES_EXPLICIT | JOINT_END_TO_END | InfoNCE Loss |
| **KT068** | HKT | HIERARCHICAL_CONTRAST | Cross-level hierarchical concept contrast | Hierarchical graph masking | YES_EXPLICIT | JOINT_END_TO_END | Hierarchical InfoNCE |
