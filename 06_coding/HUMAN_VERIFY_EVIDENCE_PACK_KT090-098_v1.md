> **VERIFY XONG 2026-11-25** — human/AI checklist ticks complete; 0 CHANGEs.

# Human-verify evidence pack — KT090–KT098 (v1)

**Role:** AI-suggested locators from text-layer extracts. **Not** a substitute for human PASS.  
**Paired checklist:** `06_coding/HUMAN_VERIFY_CHECKLIST_KT090-098_v1.md`  
**Extracts:** `06_fulltext/papers/venue_probe_vx/*.txt` (+ `VX10_KGSKT_OA_extract.txt`)  
**Date:** 2026-11-25

Use: open PDF → jump to suggested §/quote → tick PASS or CHANGE on checklist.

---

## Priority order (risk)

1. KT092 GRKT — S=NO trap  
2. KT091 ExpertGraphs — EXTERNAL_FIXED  
3. KT095 TransKT — EXTERNAL_FIXED (LLM concept graph)  
4. KT098 KGS-KT — OA + RECONSTRUCTION  
5. KT093 BiCo → KT094 GCLFKT → KT096 SCDI → KT097 MSCL → KT090 AGKT  

---

## KT092 — GRKT (`VX03_GRKT.pdf` / `.txt`)

| Field | AI coded | Suggested locator (txt line ≈) | Quote / note | Human |
|---|---|---|---|---|
| KT central | YES | title + §4 Methodology ~L195 | “GRKT conducts a recurrent modeling… KC relation-based graph neural networks” | ☐ |
| G | YES | §4.1 ~L205–214 | “KC Relation-based Graph Neural Networks” / “utilizing GNNs to model the mutual effects of KCs” | ☐ |
| **S** | **NO** | Related-work cites only | DTransformer “employs a contrastive learning framework” (~L171–173); Bi-CLKT “applied contrastive learning…” (~L204–206). **Not GRKT loss.** Method claims GNN + three-stage process only (~L181–185). | ☐ |
| provenance | MODEL_DEFINED_FIXED | §4.1 | KC relation graph used inside model (prerequisite/similarity focus ~L177–179); not expert-curated external curriculum graph | ☐ |
| encoder | GNN_GENERIC | §4.1 | “KC relation-based GNNs” | ☐ |
| SSL in method? | none found | full contrastive grep | only related-work / citation contexts | ☐ |
| ECE/Brier/RMSE/sparse4 | NO | metrics grep | no ECE/Brier/cold-start YES protocol located | ☐ |

**AI recommendation:** KEEP PRIMARY_CORE; keep S=NO.  
**Human:** ☐ agree ☐ change S→YES (must cite own pretext loss) ☐ other

---

## KT091 — ExpertGraphs L@S (`VX02_*.pdf` / `.txt`)

| Field | AI coded | Locator | Quote / note | Human |
|---|---|---|---|---|
| KT | YES | title/abstract | “Enhancing Knowledge Tracing Efficacy…”; GKT improvements AUC/ACC | ☐ |
| G | YES | §2.2.1 ~L84–89 | “Adoption of Explicit Graph Structure… Subject matter experts… This explicit structure” | ☐ |
| S | NO | SSL grep | no self-supervised / contrastive pretext for this model | ☐ |
| **provenance** | **EXTERNAL_FIXED** | abstract ~L18; §2.2.1; Fig caption ~L154 | “expert-defined graph structure”; “1.Expert-defined Graph Structure” | ☐ |
| encoder | GNN_GENERIC | GKT + 2nd-order aggregation | enhanced GKT; not claimed as a new named GNN family | ☐ |
| sparse4/ECE/RMSE | NO | metrics | AUC/ACC only located | ☐ |

**Caveat:** graph “undergoes automatic” update language (~L331) — still originated as expert-defined; keep EXTERNAL unless human finds train-only learned graph as the *primary* structure.  
**AI recommendation:** KEEP; EXTERNAL_FIXED.  
**Human:** ☐ agree ☐ → MODEL_DEFINED ☐ other

---

## KT095 — TransKT (`VX07_TransKT.pdf` / `.txt`)

| Field | AI coded | Locator | Quote / note | Human |
|---|---|---|---|---|
| KT | YES | title/abstract | “Contrastive Cross-Course Knowledge Tracing…” | ☐ |
| G | YES | abstract ~L32–34, L78 | “cross-course concept graph”; “concept graph guided knowledge transfer” | ☐ |
| S | YES | abstract ~L26–28, L95; §4.4 | “contrastive objective that aligns single-course and …”; “cross-course contrastive objective with hybrid hard negative sampling” | ☐ |
| **provenance** | **EXTERNAL_FIXED** | abstract ~L32–34, L126–129 | “cross-course concept graph by leveraging zero-shot … Large Language Model (LLM) prompts”; “LLM-to-LM pipeline” | ☐ |
| encoder | GCN | abstract ~L44–46; §4.2 | “Graph Convolutional Networks (GCNs)” | ☐ |
| SSL taxonomy | CONTRASTIVE / MIXED | abstract + §4.4 | single- vs cross-course state contrast | ☐ |
| cold-start YES? | NO | “cold-start” ~L558 | bibliography only (“learning in cold-start scenarios”), not their protocol | ☐ |
| ECE/Brier/RMSE | NO | metrics grep | not located as reported metrics | ☐ |

**AI recommendation:** KEEP; EXTERNAL_FIXED; S=YES.  
**Human:** ☐ agree ☐ provenance change ☐ other

---

## KT098 — KGS-KT (`VX10_KGSKT_OA_extract.txt` only)

| Field | AI coded | Locator | Quote / note | Human |
|---|---|---|---|---|
| Identity | IJICTE 21(1) 2025 | L1–9 | title + “With Self-Supervised Learning” | ☐ |
| KT/G/S | YES/YES/YES | L20–24 | KG + GCN + SSL; NAP + ERP | ☐ |
| provenance | MODEL_DEFINED_FIXED | L21–22 | “constructs a knowledge graph from learners' performance data” | ☐ |
| encoder | GCN (+RNN) | L20–23, L62–63 | GCN encoder for KC embeddings | ☐ |
| **ssl_paradigm** | **RECONSTRUCTION** | L23–24, L68–78 | NAP reconstructs masked node attributes; ERP deletes edges / predicts relations — **not InfoNCE contrastive** | ☐ |
| view/aug | GRAPH; mask + drop edges | L70–78 | “randomly masks… reconstruct”; “randomly deleting edges” | ☐ |
| sparse4/ECE/RMSE | NO | extract scan | no ECE/Brier/cold-start protocol located in OA extract | ☐ |

**Caveat:** OA HTML extract ≠ publisher PDF. If PDF obtained later, re-check SSL wording.  
**AI recommendation:** KEEP; RECONSTRUCTION.  
**Human:** ☐ agree ☐ flip to CONTRASTIVE (must cite contrastive loss) ☐ other

---

## KT093 — BiCo (`VX04_BiCo.pdf` / `.txt`)

| Field | AI coded | Locator | Quote / note | Human |
|---|---|---|---|---|
| KT/G/S | YES/YES/YES | title; keywords ~L27 | “self-supervised Bi-graph Co-contrastive Learning” | ☐ |
| provenance | MODEL_DEFINED_FIXED | ~L149–160 | Q2C / bi-graph views built for pretraining | ☐ |
| encoder | GCN | method (graph mining CL) | GCN-family question embedding pretrain (confirm page in PDF) | ☐ |
| SSL | CONTRASTIVE / BIPARTITE | abstract + contributions | Bi-graph co-contrastive + structure/difficulty recovery auxiliaries | ☐ |
| **RMSE** | **YES** | Table header ~L701; text ~L745 | “Methods RMSE ACC AUC…”; “Root Mean Square Error (RMSE…” — **prediction error, not calibration** | ☐ |
| ECE/Brier/sparse4 | NO | grep | not located | ☐ |

**AI recommendation:** KEEP.  
**Human:** ☐ agree ☐ change

---

## KT094 — GCLFKT (`VX06_GCLFKT.pdf` / `.txt`)

| Field | AI coded | Locator | Quote / note | Human |
|---|---|---|---|---|
| KT/G/S | YES/YES/YES | title; abstract ~L46–51 | GAT + “Graph Contrastive Learning (GCL)” | ☐ |
| provenance | MODEL_DEFINED_FIXED | abstract | question graph for GAT aggregation | ☐ |
| encoder | GAT | abstract ~L48 | “Graph Attention Networks (GAT)” | ☐ |
| SSL | CONTRASTIVE / GRAPH | §B GCL ~L173–191 | own GCL section; positive/negative graph views | ☐ |
| metrics | AUC/ACC | Table II ~L467+ | no ECE/Brier/RMSE located | ☐ |
| sparse4 | NO | — | “data sparsity” prose ≠ interaction-drop YES | ☐ |

**AI recommendation:** KEEP.  
**Human:** ☐ agree ☐ change

---

## KT096 — SCDI (`VX08_SCDI.pdf` / `.txt`)

| Field | AI coded | Locator | Quote / note | Human |
|---|---|---|---|---|
| KT/G/S | YES/YES/YES | title; abstract ~L23–30 | MAGNN hetero graph + “self-supervised graph contrastive” + GATC directed channel | ☐ |
| provenance | MODEL_DEFINED_FIXED | abstract | student/exercise/concept + directed interaction graphs from data | ☐ |
| encoder | HETEROGENEOUS_GNN | abstract | MAGNN (+ GATC) | ☐ |
| SSL | CONTRASTIVE / GRAPH | abstract; contrib 1–2 | self-supervised graph contrastive mechanism | ☐ |
| sparse4/ECE/RMSE | NO | metrics grep | not located as YES constructs | ☐ |

**AI recommendation:** KEEP.  
**Human:** ☐ agree ☐ change

---

## KT097 — MSCL (`VX09_MSCL.pdf` / `.txt`)

| Field | AI coded | Locator | Quote / note | Human |
|---|---|---|---|---|
| KT/G/S | YES/YES/YES | highlights ~L24–25; abstract ~L35–40 | MAGNN + DGCN + “self-supervised graph contrastive learning” | ☐ |
| provenance | MODEL_DEFINED_FIXED | abstract | student–exercise–skill hetero + interaction-directed graphs | ☐ |
| encoder | HETEROGENEOUS_GNN | highlights | MAGNN + DGCNs | ☐ |
| SSL | CONTRASTIVE / GRAPH | abstract; contrib | graph contrastive mechanism / view perturbation | ☐ |
| Distinguish from SCDI | — | venue/title | Neurocomputing MSCL ≠ IEEE Access SCDI; verify this PDF’s claims independently | ☐ |
| sparse4/ECE/RMSE | NO | metrics grep | not located as YES | ☐ |

**AI recommendation:** KEEP.  
**Human:** ☐ agree ☐ change

---

## KT090 — AGKT (`VX01_AGKT.pdf` / `.txt`)

| Field | AI coded | Locator | Quote / note | Human |
|---|---|---|---|---|
| KT/G | YES/YES | title; ~L33–34, L78–82 | “Automatical Graph-based Knowledge Tracing (AGKT)” updates states like graph-based methods | ☐ |
| **S** | **NO** | SSL grep | no self-supervised/contrastive pretext in extract | ☐ |
| provenance | MODEL_DEFINED_FIXED | ~L72–82 | “automatical graph” / supernode constructed for state update (not expert curriculum dump) | ☐ |
| encoder | OTHER | method figures ~L88+ | supernode message-passing; not cleanly GCN/GAT/HGNN — OTHER provisional | ☐ |
| metrics | AUC | ~L249 | AUC comparisons; no ECE/Brier/RMSE/cold-start YES | ☐ |

**High risk for human:** confirm encoder token OTHER vs GNN_GENERIC.  
**AI recommendation:** KEEP; S=NO; encoder OTHER pending human.  
**Human:** ☐ agree ☐ encoder→GNN_GENERIC ☐ other

---

## Roll-up (AI side — provisional)

| ID | KEEP? | S | Provenance | SSL paradigm | Blocking human focus |
|---|---|---|---|---|---|
| KT090 | YES | NO | MODEL_DEFINED | — | encoder OTHER |
| KT091 | YES | NO | EXTERNAL | — | EXTERNAL vs auto-update wording |
| KT092 | YES | **NO** | MODEL_DEFINED | — | do not flip S from citations |
| KT093 | YES | YES | MODEL_DEFINED | CONTRASTIVE | RMSE ≠ calibration |
| KT094 | YES | YES | MODEL_DEFINED | CONTRASTIVE | GCL is theirs |
| KT095 | YES | YES | **EXTERNAL** | CONTRASTIVE | LLM concept graph |
| KT096 | YES | YES | MODEL_DEFINED | CONTRASTIVE | — |
| KT097 | YES | YES | MODEL_DEFINED | CONTRASTIVE | ≠ SCDI |
| KT098 | YES | YES | MODEL_DEFINED | **RECONSTRUCTION** | OA extract; NAP/ERP |

If human agrees all KEEP with no field CHANGE → counts stay **N=53 / NG=49 / NS=22 / ∩=18**.

---

## Next after human ticks

1. Record CHANGEs in a dated note (do not silent-edit FINAL_v2 without version bump).  
2. If all PASS → set freeze `YES` (drop PROVISIONAL_AI) in `audit/CORPUS_FINAL_FREEZE_v2.md`.  
3. Author decide promote vNext → live `main_tlt_*` + cover + portal.
