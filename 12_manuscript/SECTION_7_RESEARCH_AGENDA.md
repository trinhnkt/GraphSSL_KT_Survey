# Section 7: Evidence-Derived Research Agenda & Future Directions (RQ6)

Based on our meta-analysis and systematic synthesis of 42 primary core studies, we formulate six evidence-derived research agenda pillars to guide future developments in Graph-Based and Self-Supervised Knowledge Tracing:

---

## Pillar 1: LLM-GNN Multimodal Fusion for Open-Domain Knowledge Graphs
* **Evidence Baseline**: Initial frontier models (`SINKT`, `KGNN-KT`) demonstrate that Large Language Models (LLMs) can extract rich semantic concept nodes and AST syntax trees.
* **Agenda Priority**: Move beyond pre-extracted static LLM embeddings toward end-to-end multimodal alignment, where LLMs generate open-domain concept graphs dynamically while GNNs propagate learner mastery states.

---

## Pillar 2: Non-Euclidean & Hyperbolic Knowledge State Manifolds
* **Evidence Baseline**: `Hyper-HKT` proves that Riemannian hyperbolic geometry eliminates representation distortion when modeling deep hierarchical concept trees compared to standard Euclidean spaces.
* **Agenda Priority**: Expand hyperbolic and mixed-curvature GNNs to model dynamic, time-evolving concept spaces where curvature adapts to local graph density.

---

## Pillar 3: Standardized Zero-Exposure KC Cold-Start Benchmarks
* **Evidence Baseline**: Our audit revealed that 95.2% of studies make sparsity claims but evaluate on generic random splits.
* **Agenda Priority**: Establish a standardized benchmark suite (e.g., *pyKT-ColdStart*) with explicit zero-exposure KC, exercise, and domain transfer splits to rigorously evaluate inductive KT capability.

---

## Pillar 4: Calibrated & Trustworthy Knowledge Tracing
* **Evidence Baseline**: 0 out of 42 primary core papers evaluate Expected Calibration Error (ECE).
* **Agenda Priority**: Integrate conformal prediction, uncertainty estimation, and temperature scaling into GNN/SSL KT backbones to provide well-calibrated, risk-aware mastery probabilities for pedagogical decision-making.

---

## Pillar 5: Continuous-Time Spatiotemporal Modeling
* **Evidence Baseline**: `STHKT` and `STG-SKT` show that interaction time intervals contain critical memory retention decay signals.
* **Agenda Priority**: Combine Continuous-Time Neural ODEs and Hawkes Processes with heterogeneous GNNs to model non-uniform learning intervals and forgetting curves continuous in time.

---

## Pillar 6: Graph Counterfactual Augmentation & Causal Debiasing
* **Evidence Baseline**: `GraphCA` and `DGR-KT` demonstrate that interaction popularity bias degrades generalizability.
* **Agenda Priority**: Develop causal counterfactual graph augmentation frameworks that disentangle student learning capacity from item popularity confounders.
