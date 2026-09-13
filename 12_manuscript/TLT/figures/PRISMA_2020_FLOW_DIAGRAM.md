# PRISMA 2020 Flow Diagram & Chart Data Specifications

This document presents the official **PRISMA 2020 Flow Diagram** in Mermaid format and exact chart data specifications for manuscript preparation.

---

## 1. Mermaid PRISMA 2020 Flowchart

```mermaid
flowchart TD
    subgraph Identification ["Identification of New Studies"]
        A["Core Databases Searches (N = 2,017)<br/>• Scopus: 531<br/>• Web of Science: 344<br/>• ScienceDirect: 257<br/>• SpringerLink: 255<br/>• IEEE Xplore: 232<br/>• ACM Digital Library: 200<br/>• arXiv Preprints: 198"]
    end

    subgraph Deduplication ["Deduplication Stage"]
        B["Duplicate Records Removed<br/>(n = 1,267)"]
        C["Unique Records Screened<br/>(N = 750)"]
    end

    subgraph Screening ["Title / Abstract Screening Stage"]
        D["Records Excluded at Title/Abstract<br/>(n = 610)"]
        E["Full-Text Articles Assessed for Eligibility<br/>(N = 140)"]
    end

    subgraph Eligibility ["Full-Text Eligibility Stage"]
        F["Full-Text Articles Excluded (n = 98)<br/>• EC1_NO_KT: 28<br/>• EC4_GENERIC_GRAPH_SSL: 18<br/>• EC2_CD_ONLY: 14<br/>• EC3_RECOMMENDATION_ONLY: 12<br/>• EC6_SPARSE_ATTENTION_ONLY: 10<br/>• EC5_LLM_TUTOR_ONLY: 8<br/>• EC7_WRONG_PUBLICATION_TYPE: 8"]
        G["Newly Included PRISMA Expansion Core Studies<br/>(n = 8)"]
    end

    subgraph FinalCorpus ["Final Included Corpus"]
        H["Seed Corpus Primary Core Papers (n = 34)"]
        I["Total Integrated PRIMARY_CORE Corpus<br/>(N = 42 Papers)"]
        J["PRIMARY_ADJACENT_SPARSE Studies (N = 8)<br/>PRIMARY_ADJACENT_METHOD Studies (N = 4)"]
    end

    A --> B
    A --> C
    C --> D
    C --> E
    E --> F
    E --> G
    H --> I
    G --> I
    I --> J
```

---

## 2. Summary Chart Metrics

- **Total Primary Core Papers**: **42 papers**
- **Graph-Based ONLY (`G=Y, S=N`)**: 26 papers (61.9%)
- **Dual Graph + SSL (`G=Y, S=Y`)**: 16 papers (38.1%)
- **Dominant GNN Architectures**: GCN (40.5%), Heterogeneous GNN (23.8%), GAT (11.9%), Dynamic GNN (7.1%), Hypergraph GNN (4.8%).
- **Dominant Temporal Backbones**: Recurrent RNN/LSTM/GRU (64.3%), Transformer Self-Attention (31.0%).
- **Strict Cold-Start Isolation Ratio**: Only 4.8% of primary core papers isolate zero-exposure KC cold-start splits.
