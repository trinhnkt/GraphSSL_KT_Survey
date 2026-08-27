# Benchmark Specification: pyKT-ColdStart Suite (v1.0 LOCKED)

**Specification Title:** pyKT-ColdStart: Standardized Benchmark Suite for Inductive Knowledge Tracing under Zero-Exposure Concepts  
**Date:** 2026-08-26  
**Status:** **PROPOSED BENCHMARK SPECIFICATION**  

---

# 1. Benchmark Motivation & Objectives

Our systematic survey revealed that **95.2% of primary core studies** fail to evaluate strict zero-exposure concept cold-start splits despite citing data sparsity. Current benchmarks (pyKT, EKT) evaluate exclusively on generic random learner splits where every concept appears in the training interaction log.

The *pyKT-ColdStart* benchmark suite addresses this gap by defining standard, reproducible split protocols for inductive zero-exposure Knowledge Tracing.

---

# 2. Benchmark Split Protocols

The benchmark provides three standard split protocols:

1. **Protocol A: Zero-Exposure KC Split (`KC-ColdStart`)**:
   - $20\%$ of domain Knowledge Components are held out entirely from the training interaction set.
   - Models must predict student response accuracy on held-out KCs using external concept hierarchy graphs or LLM semantic embeddings.
2. **Protocol B: Zero-Exposure Question Split (`Question-ColdStart`)**:
   - $25\%$ of exercises/questions are held out entirely from training.
   - Models must infer question difficulty and skill mapping via bipartite Q-matrix GNN message passing or text content embeddings.
3. **Protocol C: Cross-Domain Curriculum Split (`Domain-ColdStart`)**:
   - Student performance is evaluated across a completely unobserved course module or domain using Graph Optimal Transport or transfer GNNs.

---

# 3. Evaluation Metrics & Baseline Models

- **Predictive Metrics**: ROC-AUC, Accuracy, F1-Score, Root Mean Squared Error (RMSE).
- **Calibration Metrics**: Expected Calibration Error (ECE), Maximum Calibration Error (MCE), Reliability Diagrams.
- **Computational Metrics**: GPU Memory Footprint (MB), Training Time per Epoch (s), Inference Throughput (sequences/sec).
- **Standard Baseline Suite**: DKT, SAKT, AKT, GKT, GIKT, SINKT, HHSKT, DyGKT, HyperKT, GMGAE.
