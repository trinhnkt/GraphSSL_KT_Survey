# A1 — read of every PDF in `14_references`

**Date:** 2026-11-13. **Method:** PyMuPDF text layer of all 48 PDFs. Page 1–2 identity plus a full-text search for the seven A1 candidate titles and DOIs. This is not a screening decision and does not change N, N_G, or N_S.

## What the folder is

`14_references/README.md` lists 46 cited PDFs: 37 primary-core papers, four baselines (DKT, SAKT, AKT, DKVMN), and five prior surveys or benchmarks (Abdelrahman, pyKT, Shen, Xu, Liu DLKT). The disk has 48 PDFs. The two extras are not knowledge-tracing papers:

- `Convolutional Neural Network for Trajectory Prediction.pdf` (Nikhil and Morris; 11 pages; text extracts).
- `Model Generalization - A Sharpness Aware Optimization Perspective.pdf` (Coldenhoff; 4 pages; text extracts).

Row-level identity is in `tables/A1_LOCAL_PDF_INVENTORY_2026-11-13.csv`.

## The seven A1 candidates

None of the seven is stored here as its own PDF.

| Candidate | Own PDF in `14_references` | Mentioned inside another local PDF |
|---|---|---|
| DECKT `10.3390/e27070685` | No | No |
| DTransformer `10.1145/3543507.3583255` | No | Yes, as a citation. See below |
| Self-paced contrastive KT / SP-CLKT | No | No |
| CoSKT `10.1109/TLT.2024.3386750` | No | No |
| HCMKT `10.1016/j.eswa.2025.128840` | No | No |
| Bipartite-graph contrastive chapter `10.1007/978-981-96-0821-8_14` | No | No. The word "bipartite" in the Xu survey is the general graph type |
| Han et al. 2024, dynamic heterogeneous graph contrastive networks | No | Yes, one citation. See below |

## Citations found in the local text

DTransformer (Yin et al., WWW 2023) is cited from these deposited files:

- HKT, page 10. The paper's own sentence: "DTransformer (Yin et al., 2023) builds a hierarchical framework from the question level to the knowledge level, explicitly diagnosing learners' knowledge proficiency for each question and incorporates contrastive learning to enhance performance." The reference list on page 18 repeats the WWW 2023 entry.
- Coda (KT070), reference [47], pages 855–864.
- Multi-Granularity Ensemble (KT064), reference [36], pages 855–864.
- Shen et al. survey, reference [54], pages 855–864.
- Liu et al. DLKT survey, reference [100], pages 855–864.

Han, Tang, Zhang, Du, Zhao, and Shao, "Dynamic heterogeneous graph contrastive networks for knowledge tracing," Appl. Soft Comput. 112194 (2024), is reference [30] on page 24 of the local KT069 PDF (`A Cross-Domain Knowledge Tracing Model Based on Graph Optimal Transport.pdf`). That citation does not supply the abstract or the method section, so G and S for this paper stay `NEEDS_EVIDENCE`.

The deposited Xu survey PDF (47 pages) was searched for DECKT, DTransformer, CoSKT, HCMKT, self-paced contrastive KT, the bipartite-graph chapter, and the Han title. None of those strings occur.

## Identity flags, not bibliography edits

- KGNN-KT: 11 pages, zero extractable characters. Filename only.
- Abdelrahman survey, pages 1–2, prints the placeholder DOI `10.1145/nnnnnnn.nnnnnnn`.
- GraphCA, pages 1–2, prints `10.1109/JAS.2023.123678`. That string was not written into `references.bib`.
- Coda's file prints both `arXiv:2506.11107v1` and `10.1145/3690624.3709172`.

## What this does not close

The 2,017 search records are still absent. A local PDF, and a citation inside a local PDF, do not show whether a candidate was retrieved on 2026-08-26. `A1_CORPUS_FROZEN` stays `NO`.
