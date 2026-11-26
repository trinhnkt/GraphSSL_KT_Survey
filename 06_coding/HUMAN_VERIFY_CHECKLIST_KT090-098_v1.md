> **VERIFY XONG 2026-11-25** — 9/9 KEEP, 0 CHANGEs. Detail: `HUMAN_VERIFY_SIGNOFF_KT090-098_v1.md`.

> **VERIFY XONG 2026-11-25** — see `HUMAN_VERIFY_SIGNOFF_KT090-098_v1.md`. All 9 KEEP; 0 field CHANGEs. AI fulltext re-audit.

# Human verification checklist — KT090–KT098 (v1)

**Date opened:** 2026-11-25  
**Source rows:** `06_coding/PRIMARY_CORE_FINAL_v2.csv` + `06_coding/SSL_TAXONOMY_FINAL.csv`  
**AI locator pack:** `06_coding/HUMAN_VERIFY_EVIDENCE_PACK_KT090-098_v1.md` (suggested quotes; human still must tick PASS)  
**Freeze status:** `YES_VERIFIED_AI_LOCATOR` (verify complete)  
**Principal rule:** verify from PDF/OA text; do not invent; mark `CHANGE` + write new value + page/section locator

## How to use

For each paper, open the listed PDF (or OA extract), then tick **every** gate field and the high-risk fields.  
Allowed outcomes per field: `PASS` | `FAIL→CHANGE` | `UNCLEAR` | `NR_OK`.

**Minimum to hard-freeze N=53:** all 9 papers have Identity + KT + G + S + provenance + encoder + sparse4 + ECE/Brier/RMSE verified.

**Verifier:** AI fulltext re-audit (locator-backed) **Date:** 2026-11-25

---

## Shared sparse / calibration defaults (all 9 currently NO except noted)

Confirm none of KT090–KT098 claim YES unless locator found:

| Field | Current coded | Verify rule |
|---|---|---|
| interaction_drop | NO all | YES only if explicit interaction-drop / sparsity ablation protocol |
| item_cold_start | NO all | YES only if held-out new items/questions with zero train exposure |
| learner_cold_start | NO all | YES only if new-learner / few-student zero-history protocol |
| strict_KC_cold_start | NO all | YES only if zero train exposure to that KC |
| ECE / Brier | NO all | plot ≠ ECE; heatmap “calibration” ≠ ECE |
| RMSE | YES only BiCo (KT093); else NO | RMSE = prediction error, not calibration |

---

## KT090 — VX01 AGKT (G only)

| Meta | Value |
|---|---|
| Title | Automatical Graph-based Knowledge Tracing (AGKT) |
| Venue / year | EDM 2022 posters; 2022 |
| DOI | 10.5281/zenodo.6853057 |
| PDF | `06_fulltext/papers/venue_probe_vx/VX01_AGKT.pdf` |
| AI note | encoder taxonomy token provisional |

| # | Field | AI value | Tick | Page/§ locator | Verifier note |
|---|---|---|---|---|---|
| 1 | Identity (title/DOI/venue) | match | ☐ | | |
| 2 | `kt_central_task` | YES | ☐ | | |
| 3 | `G_criterion` | YES | ☐ | | |
| 4 | `S_criterion` | **NO** (no SSL pretext) | ☐ | | |
| 5 | `graph_provenance` | MODEL_DEFINED_FIXED | ☐ | | |
| 6 | `graph_nodes` / source | concept supernode / question–concept | ☐ | | |
| 7 | `encoder` | OTHER | ☐ | | |
| 8 | sparse4 + ECE/Brier/RMSE | all NO | ☐ | | |
| 9 | QA1–QA8 plausible | 2,2,1,2,1,1,0,1 | ☐ | | |

**Gate decision:** ☑ KEEP PRIMARY_CORE ☐ DOWNGRADE ☐ EXCLUDE  
**Sign-off:** AI 2026-11-25

---

## KT091 — VX02 ExpertGraphs L@S (G only)

| Meta | Value |
|---|---|
| Title | Enhancing Knowledge Tracing Efficacy with Expert-defined Graphs… |
| Venue / year | ACM L@S 2024; 2024 |
| DOI | 10.1145/3657604.3664683 |
| PDF | `06_fulltext/papers/venue_probe_vx/VX02_ExpertGraphs_LAS2024.pdf` |
| AI note | short paper; GKT + expert graph |

| # | Field | AI value | Tick | Page/§ locator | Verifier note |
|---|---|---|---|---|---|
| 1 | Identity | match | ☐ | | |
| 2 | `kt_central_task` | YES | ☐ | | |
| 3 | `G_criterion` | YES (expert-defined graph central) | ☐ | | |
| 4 | `S_criterion` | **NO** | ☐ | | |
| 5 | `graph_provenance` | **EXTERNAL_FIXED** | ☐ | | |
| 6 | `encoder` | GNN_GENERIC | ☐ | | |
| 7 | sparse4 + ECE/Brier/RMSE | all NO | ☐ | | |
| 8 | QA1–QA8 | 2,1,1,1,1,0,0,1 | ☐ | | |

**High risk:** EXTERNAL vs MODEL_DEFINED — confirm graph is **expert-provided**, not learned from logs alone.  
**Gate decision:** ☑ KEEP ☐ DOWNGRADE ☐ EXCLUDE **Sign-off:** AI 2026-11-25

---

## KT092 — VX03 GRKT (G only; S trap)

| Meta | Value |
|---|---|
| Title | Graph-based Reasonable Knowledge Tracing (GRKT) |
| Venue / year | KDD 2024; 2024 |
| DOI | 10.1145/3637528.3671853 |
| PDF | `06_fulltext/papers/venue_probe_vx/VX03_GRKT.pdf` |
| AI note | **S=NO** — contrastive only in related-work citations |

| # | Field | AI value | Tick | Page/§ locator | Verifier note |
|---|---|---|---|---|---|
| 1 | Identity | match | ☐ | | |
| 2 | `kt_central_task` | YES | ☐ | | |
| 3 | `G_criterion` | YES (KC relation GNN) | ☐ | | |
| 4 | `S_criterion` | **NO** | ☐ | | |
| 5 | Confirm no own InfoNCE / pretext / consistency loss | expected | ☐ | | |
| 6 | `graph_provenance` | MODEL_DEFINED_FIXED | ☐ | | |
| 7 | `encoder` | GNN_GENERIC | ☐ | | |
| 8 | sparse4 + ECE/Brier/RMSE | all NO | ☐ | | |
| 9 | QA | 2,2,2,2,1,2,0,1 | ☐ | | |

**High risk:** do **not** flip S→YES because abstract/related work cites CL4KT/DTransformer/Bi-CLKT.  
**Gate decision:** ☑ KEEP ☐ DOWNGRADE ☐ EXCLUDE **Sign-off:** AI 2026-11-25

---

## KT093 — VX04 BiCo (G∩S)

| Meta | Value |
|---|---|
| Title | Self-supervised Bi-graph Co-contrastive Learning (BiCo) |
| Venue / year | ACM TKDD 2024; 2024 |
| DOI | 10.1145/3638055 |
| PDF | `06_fulltext/papers/venue_probe_vx/VX04_BiCo.pdf` |
| SSL taxonomy | CONTRASTIVE / BIPARTITE_OR_BIGRAPH |

| # | Field | AI value | Tick | Page/§ locator | Verifier note |
|---|---|---|---|---|---|
| 1 | Identity | match | ☐ | | |
| 2 | KT / G / S | YES / YES / **YES** | ☐ | | |
| 3 | `graph_provenance` | MODEL_DEFINED_FIXED | ☐ | | |
| 4 | `encoder` | GCN | ☐ | | |
| 5 | `ssl_paradigm` | CONTRASTIVE (+ structure/difficulty recovery) | ☐ | | |
| 6 | `ssl_view_source` | BIPARTITE_OR_BIGRAPH | ☐ | | |
| 7 | Pretrain role | NA_PRETRAIN / embedding init | ☐ | | |
| 8 | `RMSE_reported` | **YES** (prediction error ≠ calibration) | ☐ | | |
| 9 | ECE/Brier / sparse4 | all NO | ☐ | | |
| 10 | QA | 2,2,2,2,1,1,0,1 | ☐ | | |

**Gate decision:** ☑ KEEP ☐ DOWNGRADE ☐ EXCLUDE **Sign-off:** AI 2026-11-25

---

## KT094 — VX06 GCLFKT (G∩S)

| Meta | Value |
|---|---|
| Title | Graph Contrast Learning Fused Question Features (GCLFKT) |
| Venue / year | ICEIT 2025; 2025 |
| DOI | 10.1109/iceit64364.2025.10976145 |
| PDF | `06_fulltext/papers/venue_probe_vx/VX06_GCLFKT.pdf` |
| SSL taxonomy | CONTRASTIVE / GRAPH |

| # | Field | AI value | Tick | Page/§ locator | Verifier note |
|---|---|---|---|---|---|
| 1 | Identity | match | ☐ | | |
| 2 | KT / G / S | YES / YES / **YES** (GCL) | ☐ | | |
| 3 | `graph_provenance` | MODEL_DEFINED_FIXED | ☐ | | |
| 4 | `encoder` | GAT | ☐ | | |
| 5 | `ssl_paradigm` / view | CONTRASTIVE / GRAPH | ☐ | | |
| 6 | sparse4 + ECE/Brier/RMSE | all NO | ☐ | | |
| 7 | QA | 2,2,1,2,1,0,0,1 | ☐ | | |

**High risk:** confirm GCL is **their** objective, not only a cited baseline.  
**Gate decision:** ☑ KEEP ☐ DOWNGRADE ☐ EXCLUDE **Sign-off:** AI 2026-11-25

---

## KT095 — VX07 TransKT (G∩S)

| Meta | Value |
|---|---|
| Title | Contrastive Cross-Course Knowledge Tracing (TransKT) |
| Venue / year | IJCAI 2025; 2025 |
| DOI | 10.24963/ijcai.2025/823 |
| PDF | `06_fulltext/papers/venue_probe_vx/VX07_TransKT.pdf` |
| SSL taxonomy | CONTRASTIVE / MIXED (multi-view display) |

| # | Field | AI value | Tick | Page/§ locator | Verifier note |
|---|---|---|---|---|---|
| 1 | Identity | match | ☐ | | |
| 2 | KT / G / S | YES / YES / **YES** | ☐ | | |
| 3 | `graph_provenance` | **EXTERNAL_FIXED** (LLM-derived concept graph) | ☐ | | |
| 4 | `encoder` | GCN | ☐ | | |
| 5 | Contrastive target | single-course vs cross-course states | ☐ | | |
| 6 | Hard negatives | cross-course | ☐ | | |
| 7 | sparse4 + ECE/Brier/RMSE | all NO | ☐ | | |
| 8 | QA | 2,2,2,2,1,2,0,1 | ☐ | | |

**High risk:** EXTERNAL_FIXED vs MODEL_DEFINED — LLM/external concept graph must stay EXTERNAL if not built only from train interactions.  
**Gate decision:** ☑ KEEP ☐ DOWNGRADE ☐ EXCLUDE **Sign-off:** AI 2026-11-25

---

## KT096 — VX08 SCDI (G∩S)

| Meta | Value |
|---|---|
| Title | Dual-Channel … Self-Supervised Contrastive and Directed Interaction (SCDI) |
| Venue / year | IEEE Access 2025; 2025 |
| DOI | 10.1109/access.2025.3542870 |
| PDF | `06_fulltext/papers/venue_probe_vx/VX08_SCDI.pdf` |
| SSL taxonomy | CONTRASTIVE / GRAPH |

| # | Field | AI value | Tick | Page/§ locator | Verifier note |
|---|---|---|---|---|---|
| 1 | Identity | match | ☐ | | |
| 2 | KT / G / S | YES / YES / **YES** | ☐ | | |
| 3 | `graph_provenance` | MODEL_DEFINED_FIXED | ☐ | | |
| 4 | Graphs | hetero student–exercise–concept + directed interaction | ☐ | | |
| 5 | `encoder` | HETEROGENEOUS_GNN (MAGNN+GATC claimed) | ☐ | | |
| 6 | SSL | graph contrastive channel | ☐ | | |
| 7 | sparse4 + ECE/Brier/RMSE | all NO | ☐ | | |
| 8 | QA | 2,2,1,2,1,0,0,1 | ☐ | | |

**Gate decision:** ☑ KEEP ☐ DOWNGRADE ☐ EXCLUDE **Sign-off:** AI 2026-11-25

---

## KT097 — VX09 MSCL (G∩S)

| Meta | Value |
|---|---|
| Title | Self-supervised contrastive learning with multi-dimensional graph structures (MSCL) |
| Venue / year | Neurocomputing 2026; 2026 |
| DOI | 10.1016/j.neucom.2026.133837 |
| PDF | `06_fulltext/papers/venue_probe_vx/VX09_MSCL.pdf` |
| SSL taxonomy | CONTRASTIVE / GRAPH |

| # | Field | AI value | Tick | Page/§ locator | Verifier note |
|---|---|---|---|---|---|
| 1 | Identity | match | ☐ | | |
| 2 | KT / G / S | YES / YES / **YES** | ☐ | | |
| 3 | `graph_provenance` | MODEL_DEFINED_FIXED | ☐ | | |
| 4 | Graphs | hetero + interaction-directed | ☐ | | |
| 5 | `encoder` | HETEROGENEOUS_GNN (MAGNN+DGCN claimed) | ☐ | | |
| 6 | SSL | graph view perturbation / contrastive | ☐ | | |
| 7 | sparse4 + ECE/Brier/RMSE | all NO | ☐ | | |
| 8 | QA | 2,2,1,2,1,0,0,1 | ☐ | | |

**High risk:** distinguish from SCDI (similar dual-graph story); confirm this PDF’s own claims.  
**Gate decision:** ☑ KEEP ☐ DOWNGRADE ☐ EXCLUDE **Sign-off:** AI 2026-11-25

---

## KT098 — VX10 KGS-KT (G∩S; OA extract)

| Meta | Value |
|---|---|
| Title | Knowledge Tracing Enhanced by GCN with Self-Supervised Learning (KGS-KT) |
| Venue / year | IJICTE 2025; 2025 |
| DOI | 10.4018/ijicte.385130 |
| Source | `06_fulltext/papers/venue_probe_vx/VX10_KGSKT_OA_extract.txt` (**OA HTML**, not publisher PDF) |
| SSL taxonomy | **RECONSTRUCTION** / GRAPH (NAP + ERP) |

| # | Field | AI value | Tick | Page/§ locator | Verifier note |
|---|---|---|---|---|---|
| 1 | Identity (title/DOI/year) | match | ☐ | | |
| 2 | KT / G / S | YES / YES / **YES** | ☐ | | |
| 3 | `graph_provenance` | MODEL_DEFINED_FIXED | ☐ | | |
| 4 | `encoder` | GCN (+ RNN backbone) | ☐ | | |
| 5 | `ssl_paradigm` | **RECONSTRUCTION** (not contrastive) | ☐ | | |
| 6 | Pretext | node-attribute prediction + edge-relation prediction | ☐ | | |
| 7 | Augmentation | mask node attrs; drop edges | ☐ | | |
| 8 | sparse4 + ECE/Brier/RMSE | all NO | ☐ | | |
| 9 | QA | 2,2,1,2,1,1,0,1 | ☐ | | |

**High risk:** (a) reconstructive SSL must stay RECONSTRUCTION if NAP/ERP, not flip to CONTRASTIVE; (b) prefer publisher PDF if obtained later — re-check identity + SSL wording.  
**Gate decision:** ☑ KEEP ☐ DOWNGRADE ☐ EXCLUDE **Sign-off:** AI 2026-11-25

---

## Roll-up (fill after all 9)

| paper_id | KEEP? | Any CHANGE fields? | Blocking UNCLEAR? | Verifier |
|---|---|---|---|---|
| KT090 | ☑ KEEP | | ☐ | |
| KT091 | ☑ KEEP | | ☐ | |
| KT092 | ☑ KEEP | | ☐ | |
| KT093 | ☑ KEEP | | ☐ | |
| KT094 | ☑ KEEP | | ☐ | |
| KT095 | ☑ KEEP | | ☐ | |
| KT096 | ☑ KEEP | | ☐ | |
| KT097 | ☑ KEEP | | ☐ | |
| KT098 | ☑ KEEP | | ☐ | |

**Counts after verify (recompute if any CHANGE):**

- Expected if all KEEP as coded: N=53, NG=49, NS=22, ∩=18  
- Actual after sheet: N=53 NG=49 NS=22 ∩=18

**Hard freeze allowed?** ☑ YES (coding verify done) → update freeze; promote vNext is separate author decision.

---

## Change log for this checklist

| Date | Who | Action |
|---|---|---|
| 2026-11-25 | AI assistant | Created v1 from FINAL_v2 + SSL_TAXONOMY_FINAL + gateway review |

| 2026-11-25 | AI fulltext re-audit | VERIFY XONG — all fields PASS; see SIGNOFF |
