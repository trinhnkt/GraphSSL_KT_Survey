# H1 five-paper PDF recheck (S-criterion)

**Date:** 2026-09-13  
**Rule:** `SCOPE_v1.0_LOCKED.md` §5 / §5.1  
**Not a protocol change.** Does not edit `_LOCKED` files.  
**Working extracts:** `12_manuscript/TLT/audit/_pdf_extract_tmp/` (`pdftotext`; KGNN-KT pages rendered because the deposit is image-only).

Verdict: all five remain `S=N`. They stay Graph-KT in \(N=37\). \(N_S=9\) unchanged.

| ID | PDF opened | Stated training objective | S-criterion |
|---|---|---|---|
| KT044 SINKT | Text PDF | Cross-entropy log loss Eq. (19) on \(y_{t}\) vs \(r_{t}\) | NO |
| KT070 Coda | Text PDF | Eq. (14) = PKT CE + adaptor KL + navigational regularizer | NO |
| KT076 KGNN-KT | Image-only scan, pages 1 and 4–7 read | Sec. 3.5 binary CE + L2 (Eq. 4) | NO |
| KT077 R²GCurL | Text PDF | Dynamic-graph KT + curriculum/RL scheduler; keywords: CL + RL | NO |
| KT079 STSKT | Text PDF | Eq. (16) binary CE + \(\beta\|\Theta\|_2^2\) | NO |

## Locators

**KT044.** “To train all parameters in SINKT, we choose the cross-entropy log loss between the predicted response \(y_{t+1}\) and the ground-truth response \(r_{t+1}\) as the objective function” → Eq. (19). LLM builds the concept–question graph (G). Contrastive learning appears only as a CL4KT citation.

**KT070.** Sec. 3.3 Optimization: \(\mathcal{L}_{Coda}=\sum(\mathcal{L}^{pkt}+\mathcal{L}^{adaptor})+\mathcal{L}^{nav}\). \(\mathcal{L}^{pkt}\) is BCE (Eq. 2). Adaptor terms are KL constraints on knowledge states (Eqs. 9–11). Navigation is a batch-wise regularizer (Eq. 12–13). Code graph is used for noise typing / sparsification, not as an SSL pretext target. Paper does not call this self-supervised.

**KT076.** Title page keywords: KT, programming education, LLM, GNN, interpretable AI — no SSL. Sec. 3.1 / 3.5: end-to-end binary cross-entropy + L2. BERT/CodeBERT are generic pretrained encoders (§5.1: generic pretraining / embedding initialization ≠ SSL). GPT-4 extracts the KG (G).

**KT077.** Abstract and keywords: dynamic graph, **curriculum learning**, **reinforcement learning**. Fig. 2 / Sec. 5–6: CL schedules samples; RL selects batches; KT model is the predictor. No contrastive/pretext/InfoNCE objective. “CL” in this paper is curriculum, not contrastive.

**KT079.** Abstract: incremental dynamic heterogeneous graph + three-channel fusion + supervised prediction. Eq. (16): binary CE + L2. “Contrastive learning” appears only in a bibliography entry.

## Decision for the manuscript

Keep \(N_S=9\). Do not add these five papers back to Table IV.
