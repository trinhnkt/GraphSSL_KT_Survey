# Human-assisted PDF read check (2026-11-24)

Sources checked with `pdftotext` + `pdfinfo`:
- `12_manuscript/TLT/main_tlt_anonymous.pdf` — **18 pages**
- `12_manuscript/TLT/COVER_LETTER.pdf` — **2 pages**

## Anonymous PDF — pass notes

| Check | Result |
|---|---|
| Running header | IEEE TRANSACTIONS ON LEARNING TECHNOLOGIES |
| Title | Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Critical Survey |
| Blind authorship | Anonymous Authors; names/ORCID omitted |
| Abstract | Present; codes **44** PDFs; $N_G=40$, $N_S=16$, $N_{G\cap S}=12$; cold-start / ECE claims match freeze |
| Keywords | Knowledge Tracing, EDM, GNN, SSL, ITS |
| Page count | 18 (at Survey/Tutorial cap) |
| Double-column IEEEtran look | Yes (page-1 layout) |

No stale “37 primary-core” / ECE $0/37$ found on page 1. Full human visual pass of all 18 pages still recommended once on screen (figures/tables spacing).

## Cover letter — pass notes

| Check | Result |
|---|---|
| Corresponding author | Van-Hau Nguyen; Faculty of IT; **Hung Yen University of Technology and Engineering** |
| Article type | Survey and Tutorial |
| Pages stated | 18 anonymous + 18 full |
| Portal | IEEE TLT Author Portal (not ScholarOne) |
| Corpus facts | N=44; NG/NS/intersection; provenance 24/7/9; cold-start; ECE 0/44 |
| Screening honesty | Deposited subset only |
| Originality / ORCID statement | Present |

## Consistency anonymous ↔ cover

Aligned on N=44, 18 pages, dual-bar TLT framing, and locked counts. Safe to use as the portal pair.
