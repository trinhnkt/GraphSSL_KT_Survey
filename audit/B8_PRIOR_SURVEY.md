# B8 — Prior-survey positioning

**Date:** 2026-11-17
**B8_SHUKURLU_COLUMN_ADDED = YES**
**Xu page locators:** read from the local JEDM PDF. Existing Xu cell wording was not rewritten.

## Shukurlu

Source: `audit/_a1_evidence/Shukurlu_LossAugmentedKT_arXiv2504.15163.txt`, identified in `audit/A1_CORPUS_DECISION.md` as arXiv:2504.15163. Author and title are on the first lines of that extract. Bib key `Shukurlu_LossKT_2025` was added to `12_manuscript/TLT/references.bib`. No DOI was invented.

The survey is close enough to position, because Sec. 4 and Table 1 review the contrastive losses of Bi-CLKT, SP-CLKT, CL4KT, and CoSKT. It is not a graph-provenance or ECE audit. A column was added to Table II. Cell locators:

| Row | Cell | Locator in the saved text |
|---|---|---|
| Protocol | Loss review; five models | Sec. 4; Sec. 6 says five key papers |
| Graph-KT | GKT named only | Sec. 2, one paragraph on graph-based KT, citing Nakagawa et al. 2019 |
| SSL-KT | Four contrastive losses | Sec. 4, Table 1 (Bi-CLKT, SP-CLKT, CLKT, CoSKT) |
| Sparse / cold-start | Data sparsity named | Sec. 1, sparsity and noise as a data challenge. No zero-exposure KC split |
| Provenance / split | Not a provenance audit | Section list is Sec. 1–6. No provenance or leakage section |
| ECE / trust | No ECE section | No ECE, Brier, or calibration section in the extract |
| Learning-technology use | Deployment named | Abstract and Sec. 6 name real-world deployment |
| Artifacts | Table 1 loss summary | Sec. 4, Table 1. No code-release statement was used |

The comparison prose states that the 0/37 ECE count is the manuscript-reporting result inside this Graph/SSL corpus and that calibration studies outside the corpus are not coded here. No outside calibration paper was named, because no such paper was read in this package.

## Xu

Local PDF: `14_references/A Survey of Graph-Based Knowledge Tracing from Structural and Propagation Perspectives - Models, Applications, and Future Directions.pdf` (47 pages). PDF page 1 is JEDM Volume 18, No. 2, 2026, page 41. Structure sentence on PDF page 3:

- Sec. 2 methodology and screening (PDF p. 4; about 184 results, 73 retained)
- Sec. 3 preliminaries and propagation paradigms
- Sec. 4 graph-construction strategies
- Sec. 5 educational applications
- Sec. 6 datasets (17 public datasets; PDF p. 27)
- Sec. 7 future directions

The existing Xu cells match that structure: structure times propagation (Sec. 3–4), not an SSL survey (no SSL section), dataset catalogue rather than a zero-exposure ontology (Sec. 6; Sec. 7.1.2 mentions cold-start only as a long-tail transfer idea), not an ECE audit (no ECE section), dataset guidance (Sec. 6). Those cells were left as written.

## Counts

N, N_G = 36, N_S = 9, and ECE 0/37 were not changed. The new sentence repeats the existing 0/37 claim.

## Stop

The `.bbl` files and the compiled PDFs were not rebuilt, so an opened PDF does not yet show the Shukurlu citation. No submission.
