# Section 2: Systematic Review Methodology and PRISMA Protocol

## 2.1 SLR Protocol & Research Questions

Our systematic review was conducted in strict accordance with the PRISMA 2020 (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) statement and guided by the locked protocol [`SLR_PROTOCOL_v1.0_LOCKED.md`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/00_protocol/SLR_PROTOCOL_v1.0_LOCKED.md).

We address six core research questions:
- **RQ1**: How are graphs constructed, represented, and validated in Graph-KT, and what is their data leakage risk?
- **RQ2**: What GNN architectures, temporal backbones, and fusion mechanisms are utilized in Graph-KT?
- **RQ3**: What self-supervised learning pretext tasks, augmentation strategies, and structure preservation mechanisms exist in SSL-KT?
- **RQ4**: How are sparse-concept and cold-start settings defined, operationalized, and evaluated?
- **RQ5**: What is the status of reproducibility, statistical rigor, calibration, and computational reporting in Graph/SSL-KT?
- **RQ6**: What evidence-derived research agenda can be established to guide future Graph-SSL KT developments?

---

## 2.2 Literature Search Architecture & Database Executions

We executed four verbatim search query families (`Q-G` Graph-KT, `Q-S` Self-Supervised KT, `Q-P` Sparse-Concept Lens, `Q-R` Reliability Lens) across seven electronic databases covering the modern deep learning era (2015-01-01 to 2026-07-31):

1. **Scopus** (n = 531 records)
2. **Web of Science Core Collection** (n = 344 records)
3. **ScienceDirect** (n = 257 records)
4. **SpringerLink** (n = 255 records)
5. **IEEE Xplore** (n = 232 records)
6. **ACM Digital Library** (n = 200 records)
7. **arXiv Preprints** (n = 198 records)

---

## 2.3 PRISMA 2020 Screening & Eligibility Flow

The systematic screening pipeline proceeded in four transparent stages:

1. **Identification**: 1,935 total raw records retrieved across all database search runs.
2. **Deduplication**: 1,185 duplicate records removed via automated 4-tier matching (DOI $\rightarrow$ Title $\rightarrow$ Author+Year $\rightarrow$ Manual resolution), yielding 750 unique deduplicated records.
3. **Stage 1 Screening (Title/Abstract)**: 610 records excluded for failing basic relevance (e.g., non-educational GNNs, Cognitive Diagnosis only, Recommender Systems only). 140 articles passed to full-text assessment.
4. **Stage 2 Screening (Full-Text Eligibility)**: 98 articles excluded with explicit primary exclusion codes (`EC1_NO_KT`: 28, `EC4_GENERIC_GRAPH_SSL`: 18, `EC2_CD_ONLY`: 14, `EC3_RECOMMENDATION_ONLY`: 12, `EC6_SPARSE_ATTENTION_ONLY`: 10, `EC5_LLM_TUTOR_ONLY`: 8, `EC7_WRONG_PUBLICATION_TYPE`: 8).
5. **Final Primary Core Corpus**: **42 `PRIMARY_CORE` papers** (34 seed core papers + 8 PRISMA expansion core papers).

---

## 2.4 Three-Level Coding Scheme & Quality Assessment (QA1–QA8)

All 42 primary core papers were coded at three linked levels:
- **PAPER Level**: Bibliographic metadata, venue tier, peer-reviewed status, gateway criteria verification.
- **MODEL Level**: Graph source, provenance, GNN encoder, temporal backbone, fusion type/location, SSL family, pretext task, and educational structure preservation.
- **EXPERIMENT Level**: Datasets, learner split protocol, random seed counts, data split resampling, metrics, statistical tests, calibration, and computational bounds.

Each paper was evaluated across 8 normalized Quality Assessment criteria (QA1–QA8, scaled 0 to 2): Task Clarity (QA1), Data Transparency (QA2), Split/Leakage Control (QA3), Baseline Adequacy (QA4), Statistical Uncertainty (QA5), Reproducibility Artifacts (QA6), Sparse Construct Validity (QA7), and Computational Transparency (QA8). The primary core corpus achieved a mean quality score of **0.7768** (MODERATE-HIGH Quality).
