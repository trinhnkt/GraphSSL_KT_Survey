# Mathematical Equations & Technical Definitions Audit
**Survey Protocol Version:** v1.0 LOCKED  
**Audit Target:** `12_manuscript/TLT/manuscript_TLT_WORKING_v0.1.tex`  
**Date:** 2026-09-12  

---

## 1. Executive Summary

This audit documents the mathematical verification and correction of all formal equations, symbol definitions, and technical formulations across the manuscript in accordance with Task A11 instructions. All equations have been audited to ensure:
1. Strict interaction-level cold-start definition.
2. Standard temperature scaling validation NLL fitting procedure.
3. Backdoor adjustment causal identification framing.
4. Immediate symbol definitions for every mathematical variable.

---

## 2. Detailed Equation Audit & Correction Log

### Equation 1: Primary Gateway Criteria (Section 1.2)
$$\text{PRIMARY\_CORE} = \text{KT} \land (\text{GRAPH\_BASED} \lor \text{SELF\_SUPERVISED})$$
- **Audit Status**: **VERIFIED**
- **Symbol Check**: $\text{KT}$ (Knowledge Tracing as primary prediction task), $\text{GRAPH\_BASED}$ (explicit graph mechanism), $\text{SELF\_SUPERVISED}$ (auxiliary SSL objective). All symbols defined in prose.

---

### Equation 2: Graph Convolutional Network Propagation (Section 3.1)
$$\mathbf{H}^{(l+1)} = \sigma\left(\tilde{\mathbf{D}}^{-\frac{1}{2}} \tilde{\mathbf{A}} \tilde{\mathbf{D}}^{-\frac{1}{2}} \mathbf{H}^{(l)} \mathbf{W}^{(l)}\right)$$
- **Audit Status**: **VERIFIED**
- **Symbol Check**: $\tilde{\mathbf{A}} = \mathbf{A} + \mathbf{I}_{|\mathcal{K}|}$ (adjacency with self-loops), $\tilde{\mathbf{D}}_{ii} = \sum_j \tilde{\mathbf{A}}_{ij}$ (degree matrix), $\mathbf{W}^{(l)} \in \mathbb{R}^{d_l \times d_{l+1}}$ (layer weight matrix), $\sigma(\cdot)$ (non-linear activation).

---

### Equation 3: InfoNCE Contrastive Objective (Section 4.1)
$$\mathcal{L}_{\text{InfoNCE}} = -\log \frac{\exp\left(\text{sim}(\mathbf{z}_i^{(1)}, \mathbf{z}_i^{(2)}) / \tau\right)}{\sum_{j=1}^B \exp\left(\text{sim}(\mathbf{z}_i^{(1)}, \mathbf{z}_j^{(2)}) / \tau\right)}$$
- **Audit Status**: **VERIFIED**
- **Symbol Check**: $\mathbf{z}_i^{(1)}, \mathbf{z}_i^{(2)}$ (normalized embeddings from augmented views 1 and 2), $\text{sim}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u}^T \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$ (cosine similarity), $\tau > 0$ (temperature hyperparameter), $B$ (mini-batch size).

---

### Equation 4: Expected Calibration Error (ECE) (Section 6.4)
$$\text{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{N} \left| \text{acc}(B_m) - \text{conf}(B_m) \right|$$
- **Audit Status**: **VERIFIED**
- **Symbol Check**: $N$ (total test predictions), $M$ (number of confidence bins, $M=10$), $B_m$ (set of prediction samples in bin interval $((m-1)/M, m/M]$), $\text{acc}(B_m)$ (empirical accuracy in bin $m$), $\text{conf}(B_m)$ (mean predicted confidence in bin $m$).

---

### Equation 5: Multimodal Cross-Attention Alignment (Section 7, Pillar 1)
$$\mathbf{Z}_{\text{aligned}} = \text{Softmax}\left(\frac{(\mathbf{E}_{\text{LLM}}\mathbf{W}_Q)(\mathbf{H}_{\text{GNN}}\mathbf{W}_K)^T}{\sqrt{d}}\right) (\mathbf{H}_{\text{GNN}}\mathbf{W}_V)$$
- **Audit Status**: **VERIFIED & ENRICHED**
- **Symbol Check**: $\mathbf{E}_{\text{LLM}} \in \mathbb{R}^{|\mathcal{K}| \times d_{\text{text}}}$ (LLM text embedding matrix), $\mathbf{H}_{\text{GNN}} \in \mathbb{R}^{|\mathcal{K}| \times d_{\text{graph}}}$ (GNN topological representation matrix), $\mathbf{W}_Q, \mathbf{W}_K, \mathbf{W}_V$ (learnable projection weight matrices), $d$ (hidden feature dimension scaling factor).

---

### Equation 6: Poincaré Hyperbolic Distance Metric (Section 7, Pillar 2)
$$d_{\mathbb{B}}(u, v) = \text{arcosh}\left(1 + 2 \frac{\|u - v\|^2}{(1 - \|u\|^2)(1 - \|v\|^2)}\right)$$
- **Audit Status**: **VERIFIED & ENRICHED**
- **Symbol Check**: $u, v \in \mathbb{B}^d$ (node embedding vectors residing in Poincaré unit ball $\mathbb{B}^d = \{x \in \mathbb{R}^d \mid \|x\| < 1\}$), $\text{arcosh}(\cdot)$ (inverse hyperbolic cosine function), $\|\cdot\|$ (Euclidean vector norm).

---

### Equation 7: Interaction-Level Zero-Exposure Cold-Start Protocol (Section 7, Pillar 3)
$$\mathcal{D}_{\text{train}}^{\text{cold}} = \{(x_t, r_t) \in \mathcal{D}_{\text{train}} \mid \text{KC}(x_t) \notin \mathcal{K}_{\text{cold}}\}$$
- **Audit Status**: **CORRECTED PER TASK A11**
- **Correction Applied**: Replaced raw matrix-column zeroing ($\mathbf{X}_{\text{train}} = \mathbf{X} \odot (\mathbf{1} - \mathbf{M}_{\text{cold}})$) with explicit interaction-level filtering.
- **Symbol Check**: $\mathcal{K}_{\text{cold}} \subset \mathcal{K}$ (held-out cold concept set satisfying $n_{\text{train}}(k) = 0, \forall k \in \mathcal{K}_{\text{cold}}$), $\text{KC}(x_t)$ (mapping function assigning exercise $x_t$ to its Knowledge Components), $\mathcal{D}_{\text{train}}^{\text{cold}}$ (filtered training interaction set).

---

### Equation 8: Temperature Scaling Post-Hoc Calibration (Section 7, Pillar 4)
$$\hat{p}_i = \sigma\left(\frac{z_i}{T}\right)$$
- **Audit Status**: **CORRECTED PER TASK A11**
- **Correction Applied**: Clarified fitting procedure: scalar temperature $T > 0$ is optimized on a validation set by minimizing negative log-likelihood (NLL / log-loss), after which ECE and Brier score are evaluated on the test set (avoiding claims that temperature scaling directly optimizes ECE).
- **Symbol Check**: $z_i \in \mathbb{R}$ (raw model logit output for prediction $i$), $T > 0$ (scalar temperature parameter), $\sigma(\cdot)$ (standard logistic sigmoid function), $\hat{p}_i \in (0, 1)$ (calibrated prediction probability).

---

### Equation 9: Continuous-Time Neural ODE Knowledge Evolution (Section 7, Pillar 5)
$$\frac{dh(t)}{dt} = f_\theta(h(t), t), \quad h(t_{n+1}) = h(t_n) + \int_{t_n}^{t_{n+1}} f_\theta(h(\tau), \tau) d\tau$$
- **Audit Status**: **VERIFIED & ENRICHED**
- **Symbol Check**: $h(t) \in \mathbb{R}^d$ (continuous latent student knowledge state at time $t$), $f_\theta(\cdot)$ (neural network parameterized by weights $\theta$ representing continuous state trajectory derivative), $t_n, t_{n+1}$ (consecutive interaction timestamps).

---

### Equation 10: Backdoor Adjustment Causal Identification (Section 7, Pillar 6)
$$P(Y \mid do(X = x)) = \sum_{z} P(Y \mid X = x, Z = z) P(Z = z)$$
- **Audit Status**: **CORRECTED PER TASK A11**
- **Correction Applied**: Framed as backdoor adjustment under valid causal identification assumptions (sufficiency of confounder set $Z$ blocking spurious paths) rather than a universal do-calculus identity.
- **Symbol Check**: $Y \in \{0, 1\}$ (target student response accuracy), $X$ (treatment variable e.g., item popularity / historical exposure), $Z$ (sufficient set of observed confounding variables e.g., student prior ability and concept difficulty).

---
*End of Equation Audit Report.*
