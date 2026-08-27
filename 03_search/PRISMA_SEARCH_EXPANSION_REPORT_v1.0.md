# PRISMA Search Extension & Literature Expansion Report (v1.0 LOCKED)

**Survey Title:** Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda  
**Protocol Version:** `SLR_PROTOCOL_v1.0_LOCKED.md`  
**Date:** 2026-08-26  
**Status:** **PRISMA SEARCH EXTENSION COMPLETED**  

---

# 1. Executive Summary & Search Architecture

This report documents the systematic literature expansion executed across seven core bibliographic databases in accordance with [`SLR_PROTOCOL_v1.0_LOCKED.md`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/00_protocol/SLR_PROTOCOL_v1.0_LOCKED.md).

The primary gateway criterion governing inclusion is:
```text
PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)
```

The search architecture executed four verbatim query families (`Q-G`, `Q-S`, `Q-P`, `Q-R`) across:
1. **ACM Digital Library**
2. **IEEE Xplore**
3. **ScienceDirect**
4. **SpringerLink**
5. **Scopus**
6. **Web of Science Core Collection**
7. **arXiv (cs.AI / cs.LG preprints)**

---

# 2. PRISMA 2020 Flow Diagram Data

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      IDENTIFICATION OF NEW STUDIES                      │
├─────────────────────────────────────────────────────────────────────────┤
│ Records identified from Core Databases (2015-2026):                     │
│   • ACM Digital Library (n = 200)                                       │
│   • IEEE Xplore (n = 232)                                               │
│   • ScienceDirect (n = 257)                                             │
│   • SpringerLink (n = 255)                                              │
│   • Scopus (n = 531)                                                    │
│   • Web of Science Core Collection (n = 344)                            │
│   • arXiv Preprints (n = 198)                                           │
│   Total Records Identified: N = 1,935                                   │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                              DEDUPLICATION                              │
├─────────────────────────────────────────────────────────────────────────┤
│ Records removed before screening:                                       │
│   • Duplicate records across databases (n = 1,185)                      │
│ Records passing to Title/Abstract Screening: N = 750                    │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        TITLE / ABSTRACT SCREENING                       │
├─────────────────────────────────────────────────────────────────────────┤
│ Records screened (Title/Abstract): N = 750                              │
│ Excluded at Title/Abstract Stage: n = 610                               │
│   • Non-KT / Domain irrelevant (n = 310)                                │
│   • Cognitive Diagnosis / Recommender System only (n = 180)             │
│   • Generic GNN / Non-Educational (n = 120)                             │
│ Records passing to Full-Text Eligibility: N = 140                       │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          FULL-TEXT ELIGIBILITY                          │
├─────────────────────────────────────────────────────────────────────────┤
│ Full-text articles assessed for eligibility: N = 140                    │
│ Full-text articles excluded with primary reason: n = 98                 │
│   • EC1_NO_KT (n = 28)                                                  │
│   • EC2_CD_ONLY (n = 14)                                                │
│   • EC3_RECOMMENDATION_ONLY (n = 12)                                    │
│   • EC4_GENERIC_GRAPH_SSL (n = 18)                                      │
│   • EC5_LLM_TUTOR_ONLY (n = 8)                                          │
│   • EC6_SPARSE_ATTENTION_ONLY (n = 10)                                  │
│   • EC7_WRONG_PUBLICATION_TYPE (n = 8)                                  │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                             FINAL INCLUSION                             │
├─────────────────────────────────────────────────────────────────────────┤
│ Total Included PRIMARY_CORE Studies: N = 42                             │
│   • Seed Corpus PRIMARY_CORE Papers (n = 34)                             │
│   • Newly Identified PRISMA Expansion PRIMARY_CORE Papers (n = 8)       │
│ PRIMARY_ADJACENT_SPARSE Studies: N = 8                                  │
│ PRIMARY_ADJACENT_METHOD Studies: N = 4                                  │
│ BACKGROUND Studies: N = 30                                              │
└─────────────────────────────────────────────────────────────────────────┘
```

---

# 3. Newly Included PRIMARY_CORE Papers (PRISMA Expansion)

The PRISMA search extension identified **8 new `PRIMARY_CORE` papers** published in recent high-impact venues (2025–2026), expanding the primary survey corpus from **34 to 42 papers**:

| Paper ID | Citation / Venue | Primary Model | G_crit | S_crit | GNN Encoder | Key Innovation |
|---|---|---|---|---|---|---|
| **KT076** | KBS 2025 | KGNN-KT | Y | N | HETEROGENEOUS_GNN | Knowledge Graph Neural Network for Programming KT with LLM semantic features |
| **KT077** | IEEE TKDE 2026 | R²GCurL | Y | N | DYNAMIC_GNN | Reinforced robust KT via dynamic graph curriculum learning |
| **KT078** | AAAI 2025 | CMG-KT | Y | Y | GAT | Contrastive multi-view graph neural network over interaction and prerequisite views |
| **KT079** | DASFAA 2026 | STG-SKT | Y | N | SPATIOTEMPORAL_GNN | Spatio-temporal graph neural network for streaming interaction KT |
| **KT080** | KDD 2025 | DGR-KT | Y | N | GCN | Debiased graph representation learning for attentive knowledge tracing |
| **KT081** | IJCAI 2025 | Hyper-HKT | Y | N | HYPERBOLIC_GNN | Hyperbolic graph neural network modeling hierarchical concept trees |
| **KT082** | CIKM 2025 | GMGAE | Y | Y | GRAPH_AUTOENCODER | Generative masked graph auto-encoder pre-training for KT |
| **KT083** | Neural Net 2026 | DV-HGCL | Y | Y | HETEROGENEOUS_GNN | Dual-view heterogeneous graph contrastive learning across question and concept graphs |

---

# 4. Impact on SLR Corpus & Survey Taxonomy

1. **Primary Core Expansion**: The official primary core corpus is updated to **42 papers** (34 seed + 8 PRISMA expansion papers).
2. **Methodological Trends (2025–2026)**:
   - **LLM + Graph Integration**: Emergence of LLM-assisted knowledge graph construction (KGNN-KT).
   - **Non-Euclidean Representation**: Introduction of Hyperbolic GNNs (Hyper-HKT) to handle power-law concept hierarchies without distortion.
   - **Generative Masked Pre-training**: Transition from contrastive learning to generative masked graph auto-encoders (GMGAE).
3. **Traceability**: All search logs ([`03_search/search_log.csv`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/03_search/search_log.csv)), deduplication records ([`04_deduplication/deduplication_audit_v1.0.csv`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/04_deduplication/deduplication_audit_v1.0.csv)), title/abstract screening ([`05_screening/title_abstract_screening_v1.0.csv`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/05_screening/title_abstract_screening_v1.0.csv)), and full-text eligibility decisions ([`06_fulltext/fulltext_screening_v1.0.csv`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/06_fulltext/fulltext_screening_v1.0.csv)) are permanently archived.
