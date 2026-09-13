# GRAPH-KT TAXONOMY AUDIT REPORT (Task A4)

**Target Journal:** IEEE Transactions on Learning Technologies (IEEE TLT)  
**Audit Date:** 2026-09-12  
**Status:** **AUDITED & CODING-RECONCILED**  

---

## 1. Corpus Categorization Totals

- **Total Primary Core Papers:** **37**
- **Graph-Based KT Papers ($):** **31**
- **Self-Supervised KT Papers ($):** **14**
- **Dual Graph + SSL KT Papers ({G \cap S}$):** **8**
- **Non-Graph SSL Papers (e.g., CL4KT):** **1** (Correctly categorized with gnn_encoder = NONE, graph_source = NONE)

---

## 2. Mandatory Adjudicated Corrections Applied

- **KT004 (GKT):** Dense and Transition variants explicitly represented as separate model entries (MODEL_DEFINED_FIXED, SEQUENTIAL_TRANSITION).
- **KT014 (PDKT-C):** Corrected to EXPERT_PREREQUISITE, EXTERNAL_FIXED, KC_KC, gnn_encoder = NONE, 	emporal_backbone = RNN_LSTM_GRU, usion_type = REGULARIZATION_ONLY.
- **KT039 (CL4KT):** Corrected to graph_source = NONE, graph_provenance = NA, graph_representation = NONE, gnn_encoder = NONE, 	emporal_backbone = SELF_ATTENTION_TRANSFORMER.
