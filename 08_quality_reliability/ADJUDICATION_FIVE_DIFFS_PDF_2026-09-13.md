# Five-diff PDF re-read (2026-09-13)

Primary PDFs in `14_references/`. Page = PDF page.  
This is **adjudication evidence**, not a new locked count and not \(\kappa\).

Codebook: item CS = new item/exercise protocol; strict KC = zero training-interaction exposure for a KC. Motivation prose ≠ YES.

| # | Paper | Field | Locked A | Adopted draft | **PDF-strict** |
|---|---|---|---|---|---|
| 1 | KT026 | item_cold_start | YES | NO | **NO** |
| 2 | KT031 | gnn_encoder | GCN | OTHER | **OTHER** |
| 3 | KT044 | gnn_encoder | GCN | GAT | **GAT** |
| 4 | KT044 | strict_kc_cold_start | YES | NO | **NO** (item CS stays **YES**) |
| 5 | KT076 | item_cold_start | YES | NO | **NO** |

---

## 1. KT026 PEBG — item CS

File: `Improving Knowledge Tracing via Pre-training Question Embeddings.pdf`

- p.1–2: student–question interactions “extremely sparse”; PEBG does **question-level** prediction vs skill-level.
- p.5 §5.4: DKT-Q / DKVMN-Q “suffer from question interactions sparsity”; PEBG+DKT AUC on ASSIST09/12/EdNet.
- `[no hit]`: `cold-start`, `unseen question` hold-out, zero-exposure item split.

**PDF-strict: NO.** Question-level sparsity is not an item hold-out. Locked `ITEM_COLD_START` is a looser overlay.

## 2. KT031 KSG-AKT — encoder

File: `Knowledge Structure Enhanced Graph Representation Learning Model for Attentive Knowledge Tracing.pdf`

- p.7 / Algorithm: `Q, S ← Metapath2Vec`; then “Convolutional question representation” (§4.3) — CNN-style fusion of embeddings, not graph convolution.
- p.20: “GIKT … using a GCN” is a **baseline**. “To embed the nodes … using Metapath2Vec…”
- Table: “Our model / Metapath2Vec / Convolutional dense embedding.”

**PDF-strict: OTHER** (or keep a note `Metapath2Vec`). Locked `GCN` does not match this paper’s encoder.

## 3–4. KT044 SINKT — GAT vs GCN; strict KC

File: `SINKT - A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model.pdf`

**Encoder**

- p.4: “We apply three different Graph Attention Networks (GAT)…”
- Fig. SIEnc: C-C GAT / C-Q GAT / Q-C GAT.
- p.8: ablation `SINKT-GAT` “removes GAT layers in the SIEnc”.

**PDF-strict: GAT.** Locked `GCN` is a coarse table token.

**Cold-start**

- p.2–3 claim: “new concept c4 and a new question q5”; “Q_train ≠ Q_test” defined on **questions**.
- p.6 Fig. 4: pipeline when a teacher adds a new concept/question (LLM graph), not a numbered KC hold-out table.
- p.7 §5.5: “we remove 1/4 of the question from the training set and evaluate … on these questions.” Table 3: Inductive KT. Fig. 5: “Cold start analysis” = unseen **questions** + fewer students.

**PDF-strict: item CS = YES; strict KC = NO.**  
No experiment withholds every training interaction of a KC. A’s `strict_kc=YES` follows the new-concept *claim/pipeline*, not §5.5.

## 5. KT076 KGNN-KT — item CS

File: `KGNN-KT - Enhancing Knowledge Tracing...pdf` (scan; `_kt076_pages/`)

- p.7 §4.1–4.2: merge three programming datasets; **7:2:1** student-interaction split; metrics AUC/F1 by Easy/Medium/Hard.
- p.8–9: ablation removes knowledge graph / text / history — component ablation.
- Related work (p.3) mentions cold-start of **other** LLM-KT papers.
- `[no hit]` on rendered pages: unseen-problem hold-out, new-item split, zero-exposure item protocol.

**PDF-strict: NO.** Locked `ITEM_COLD_START` is not supported by the executed split on the pages read.

---

If these five PDF-strict values are accepted as the adopted B row, S/family/provenance still match A on all 20; remaining A–B diffs are exactly these five (plus none if A is later recoded). Still **not** manuscript \(\kappa\).

---

## Applied to CSVs (2026-09-13)

PDF-strict values written into:

- `08_quality_reliability/inter_rater_coderA_locked_v1.0.csv`
- `12_manuscript/TLT/tables/sparse_coldstart_audit.csv`
- `12_manuscript/TLT/tables/graph_taxonomy.csv`
- `12_manuscript/TLT/tables/H2_qa7_two_variables.csv`
- `12_manuscript/TLT/supplementary/supplementary_corpus_inventory.csv` (KT031 / KT044 encoder only)

Manuscript / figures / cover letter / `LOCKED_COUNTS_v1.5.md` follow those CSVs. Still **not** human–human \(\kappa\).
