# KT076 identity correction (v1.1)

**Date:** 2026-09-13  
**Does not overwrite:** `KT076_CODING_v1.0.md`, `KT076_FIELD_EVIDENCE_v1.0.md`

## Binding identity for the live TLT package

The deposited primary PDF and `references.bib` key `KT076_KGNNKT_2025` are:

- **Title:** KGNN-KT: Enhancing Knowledge Tracing in Programming Education Through LLM-Extracted Knowledge Graphs
- **Authors:** Di Zhang, Qiang Niu, Tianshi Wang, Yuntian Hou, Jinheng Wu, Chao Zhang, Angelos Stefanidis
- **Venue:** 21st International Conference on Intelligent Computing (ICIC 2025), Springer CCIS, pp. 137–147
- **DOI:** `10.1007/978-981-96-9986-5_12`
- **File:** `14_references/KGNN-KT - Enhancing Knowledge Tracing in Programming Education Through LLM-Extracted Knowledge Graphs.pdf`

Live `venue_year` strings: **ICIC 2025** (not KBS 2025).

## What v1.0 coded instead

`KT076_CODING_v1.0.md` and `KT076_FIELD_EVIDENCE_v1.0.md` record a **different** article:

- Chen et al., Knowledge-Based Systems, Vol. 312, Article 113400
- DOI `10.1016/j.knosys.2025.113400`

That KBS article remains a historical screening record (`REC_0035` in `supplementary_prisma_exclusions.csv`). It is **not** the deposited KT076 PDF.

## Live tables updated 2026-09-13

`venue_year` KBS 2025 → ICIC 2025 on the KT076 row only:

- `12_manuscript/TLT/tables/graph_taxonomy.csv`
- `12_manuscript/TLT/tables/sparse_coldstart_audit.csv`
- `12_manuscript/TLT/supplementary/supplementary_corpus_inventory.csv`
- `12_manuscript/TLT/supplementary/supplementary_coding_matrix.csv`

`supplementary_doi_audit.csv` already listed ICIC / Springer DOI.
