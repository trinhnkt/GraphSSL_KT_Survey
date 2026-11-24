# TLT Supplementary Evidence Tables

Date: 2026-09-13. Sources are locked CSVs and `00_protocol/SLR_PROTOCOL_v1.0_LOCKED.md`.
No new screening, coding, QA, or reliability numbers are invented here.

**Locked identity (do not use N_S=14):** $N=37$, $N_G=36$, $N_S=9$, $N_{G\cap S}=8$ ($36+9-8=37$).
Historical 14-row SSL lists are superseded by `audit/H1_SSL_CRITERION_DECISION.md`.

## 1. Search strings by query family

Copied from locked protocol §6–7 (`SLR_PROTOCOL_v1.0_LOCKED.md`). Database runs may use adapted syntax; exact adapted strings are in §2.

### Q-G Graph-KT

```
("knowledge tracing" OR "student knowledge tracing") AND (graph OR "graph neural network" OR GNN OR GCN OR GAT OR hypergraph OR heterogeneous OR "dynamic graph" OR "temporal graph" OR prerequisite OR "prerequisite graph" OR "concept map" OR "skill graph" OR "knowledge graph" OR "concept graph" OR "knowledge structure" OR "multi-relational" OR "multi relational")
```

### Q-S Self-Supervised KT

```
("knowledge tracing" OR "student knowledge tracing") AND ("self-supervised" OR "self supervised" OR contrastive OR "masked modeling" OR "masked prediction" OR "masked interaction" OR "masked concept" OR reconstruction OR "pretext task" OR "self-distillation" OR "self distillation" OR "teacher student" OR "teacher-student" OR "consistency learning")
```

### Q-P Sparse-Concept Lens

```
("knowledge tracing" OR "student knowledge tracing") AND (sparse OR sparsity OR "low frequency" OR "low-frequency" OR "long tail" OR long-tail OR few-shot OR "few shot" OR "cold start" OR cold-start OR unseen OR inductive) AND (concept OR skill OR "knowledge component" OR item OR exercise OR learner)
```

### Q-R Reliability Lens

```
("knowledge tracing" OR "student knowledge tracing") AND (calibration OR reproducibility OR leakage OR "temporal split" OR "learner split" OR "cold start" OR cold-start OR "confidence interval" OR bootstrap OR "statistical significance" OR "multiple comparison" OR "effect size" OR scalability OR "training time" OR memory)
```

## 2. Database execution table

Per-query rows: `03_search/search_log.csv` (search date 2026-08-26).
Locked identification totals (`tables/corpus_counts.csv`): Scopus 531, WoS 344, ScienceDirect 257, SpringerLink 255, IEEE Xplore 232, ACM DL 200, arXiv 198; sum $N_{\mathrm{IDENTIFIED}}=2{,}017$.

| search_id | database | family | date | records_returned | notes |
|---|---|---|---|---:|---|
| SRCH_001 | ACM_DL | Q-G | 2026-08-26 | 142 | Core Graph-KT search in ACM DL |
| SRCH_002 | ACM_DL | Q-S | 2026-08-26 | 58 | Core SSL-KT search in ACM DL |
| SRCH_003 | IEEE_Xplore | Q-G | 2026-08-26 | 168 | Core Graph-KT search in IEEE Xplore |
| SRCH_004 | IEEE_Xplore | Q-S | 2026-08-26 | 64 | Core SSL-KT search in IEEE Xplore |
| SRCH_005 | ScienceDirect | Q-G | 2026-08-26 | 185 | Core Graph-KT search in ScienceDirect |
| SRCH_006 | ScienceDirect | Q-S | 2026-08-26 | 72 | Core SSL-KT search in ScienceDirect |
| SRCH_007 | SpringerLink | Q-G | 2026-08-26 | 194 | Core Graph-KT search in SpringerLink |
| SRCH_008 | SpringerLink | Q-S | 2026-08-26 | 61 | Core SSL-KT search in SpringerLink |
| SRCH_009 | Scopus | Q-G | 2026-08-26 | 286 | Core Graph-KT search in Scopus |
| SRCH_010 | Scopus | Q-S | 2026-08-26 | 112 | Core SSL-KT search in Scopus |
| SRCH_011 | WebOfScience | Q-G | 2026-08-26 | 248 | Core Graph-KT search in Web of Science |
| SRCH_012 | WebOfScience | Q-S | 2026-08-26 | 96 | Core SSL-KT search in Web of Science |
| SRCH_013 | arXiv | Q-G | 2026-08-26 | 135 | Core Graph-KT search in arXiv cs.AI/cs.LG |
| SRCH_014 | arXiv | Q-S | 2026-08-26 | 63 | Core SSL-KT search in arXiv cs.AI/cs.LG |
| SRCH_015 | Scopus | Q-P | 2026-08-26 | 88 | Supplementary sparse lens search in Scopus |
| SRCH_016 | Scopus | Q-R | 2026-08-26 | 45 | Supplementary reliability lens search in Scopus |

Exact adapted queries are in `03_search/search_log.csv` column `exact_query`.

## 3. Inclusion / exclusion

- Gateway: `PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)` (`SCOPE_v1.0_LOCKED.md` §5; protocol §12.1).
- EC1_NO_KT; EC2_CD_ONLY; EC3_RECOMMENDATION_ONLY; EC4_GENERIC_GRAPH_SSL; EC5_LLM_TUTOR_ONLY; EC6_SPARSE_ATTENTION_ONLY; EC7_WRONG_PUBLICATION_TYPE (`SLR_PROTOCOL_v1.0_LOCKED.md` §13).
- Also defined: EC10_NON_ENGLISH; EC11_PERFORMANCE_PREDICTION_NOT_KT; EC12_OUTSIDE_DATE_WINDOW; EC13_OTHER.
- PRISMA arithmetic: $2{,}017-1{,}267=750$; $750-610=140$; $140-103=37$.

## 4. Full 37-paper corpus

Graph fields: `tables/graph_taxonomy.csv` (KT004 is one paper; Dense/Trans are model entries).
SSL: `tables/ssl_taxonomy.csv` ($N_S=9$). Sparse: `tables/sparse_coldstart_audit.csv`.
ECE reporting is a corpus-level audit ($0/37$); there is no per-paper ECE locator file beyond that locked claim.

| paper_id | cite key | year | venue | Graph | SSL | provenance | encoder | sparse/cold-start | ECE reported |
|---|---|---|---|---|---|---|---|---|---|
| KT004 | KT004_GKT_2019 | 2019 | WI 2019 | YES | NO | MODEL_DEFINED_FIXED | GNN_GENERIC | SPARSE_INTERACTION_ONLY | NO |
| KT010 | KT010_GIKT_2021 | 2021 | ECML-PKDD 2021 | YES | NO | MODEL_DEFINED_FIXED | GAT | SPARSE_INTERACTION_ONLY | NO |
| KT011 | KT011_BiCLKT_2022 | 2022 | KBS 2022 | YES | YES | MODEL_DEFINED_FIXED | GCN | SPARSE_INTERACTION_ONLY | NO |
| KT012 | KT012_JKT_2021 | 2021 | InfoSci 2021 | YES | NO | MODEL_DEFINED_FIXED | GCN | SPARSE_INTERACTION_ONLY | NO |
| KT014 | KT014_PDKTC_2018 | 2018 | ICDM 2018 | YES | NO | EXTERNAL_FIXED | NONE | SPARSE_INTERACTION_ONLY | NO |
| KT016 | KT016_SKT_2020 | 2020 | ICDM 2020 | YES | NO | MODEL_DEFINED_FIXED | GAT | SPARSE_INTERACTION_ONLY | NO |
| KT023 | KT023_SGKT_2022 | 2022 | ESWA 2022 | YES | NO | MODEL_DEFINED_FIXED | GGNN | SPARSE_INTERACTION_ONLY | NO |
| KT026 | KT026_PretrainQ_2020 | 2020 | IJCAI 2020 | YES | YES | MODEL_DEFINED_FIXED | NONE | SPARSE_INTERACTION_ONLY | NO |
| KT029 | KT029_DGEKT_2024 | 2024 | TOIS 2024 | YES | NO | DYNAMIC_LEARNED | GCN | SPARSE_INTERACTION_ONLY | NO |
| KT031 | KT031_KSGAKT_2022 | 2022 | IJIS 2022 | YES | NO | EXTERNAL_FIXED | OTHER | SPARSE_INTERACTION_ONLY | NO |
| KT033 | KT033_DGMN_2023 | 2023 | IEEE TKDE 2023 | YES | NO | DYNAMIC_LEARNED | GRAPH_MEMORY | SPARSE_INTERACTION_ONLY | NO |
| KT035 | KT035_HHSKT_2023 | 2023 | ESWA 2023 | YES | NO | MODEL_DEFINED_FIXED | HETEROGENEOUS_GNN | SPARSE_INTERACTION_ONLY | NO |
| KT036 | KT036_TSKT_2024 | 2024 | ESWA 2024 | YES | NO | MODEL_DEFINED_FIXED | HETEROGENEOUS_GNN | SPARSE_INTERACTION_ONLY | NO |
| KT037 | KT037_CMKT_2022 | 2022 | IEEE TLT 2022 | YES | NO | EXTERNAL_FIXED | NONE | SPARSE_INTERACTION_ONLY | NO |
| KT038 | KT038_DyGKT_2024 | 2024 | KDD 2024 | YES | NO | DYNAMIC_LEARNED | DYNAMIC_GNN | SPARSE_INTERACTION_ONLY | NO |
| KT039 | KT039_CL4KT_2022 | 2022 | WWW 2022 | NO | YES | NA | NONE | SPARSE_INTERACTION_ONLY | NO |
| KT042 | KT042_S2HHN_2023 | 2023 | InfoSci 2023 | YES | YES | MODEL_DEFINED_FIXED | HYPERGRAPH_GNN | SPARSE_INTERACTION_ONLY | NO |
| KT043 | KT043_3VCLKT_2024 | 2024 | IEEE TCE 2024 | YES | YES | MODEL_DEFINED_FIXED | HETEROGENEOUS_GNN | SPARSE_INTERACTION_ONLY | NO |
| KT044 | KT044_SINKT_2024 | 2024 | CIKM 2024 | YES | NO | EXTERNAL_FIXED | GAT | ITEM_COLD_START | NO |
| KT047 | KT047_DCSSL_2023 | 2023 | ESWA 2023 | YES | YES | MODEL_DEFINED_FIXED | HETEROGENEOUS_GNN | SPARSE_INTERACTION_ONLY | NO |
| KT050 | KT050_GraphCA_2023 | 2023 | JAS 2023 | YES | YES | MODEL_DEFINED_FIXED | HETEROGENEOUS_GNN | SPARSE_INTERACTION_ONLY | NO |
| KT052 | KT052_CapsuleGNN_2022 | 2022 | Appl Intell 2022 | YES | NO | MODEL_DEFINED_FIXED | CAPSULE_GNN | SPARSE_INTERACTION_ONLY | NO |
| KT053 | KT053_GASKT_2021 | 2021 | KSEM 2021 | YES | NO | MODEL_DEFINED_FIXED | GCN | SPARSE_INTERACTION_ONLY | NO |
| KT056 | KT056_LSTGraph_2025 | 2025 | IP&M 2025 | YES | NO | DYNAMIC_LEARNED | GAT | SPARSE_INTERACTION_ONLY | NO |
| KT060 | KT060_STHKT_2025 | 2025 | ESWA 2025 | YES | NO | DYNAMIC_LEARNED | GCN | SPARSE_INTERACTION_ONLY | NO |
| KT062 | KT062_LGSKT_2025 | 2025 | Neural Net 2025 | YES | NO | EXTERNAL_FIXED | GCN | SPARSE_INTERACTION_ONLY | NO |
| KT063 | KT063_MAHKT_2025 | 2025 | KBS 2025 | YES | NO | MODEL_DEFINED_FIXED | HETEROGENEOUS_GNN | SPARSE_INTERACTION_ONLY | NO |
| KT064 | KT064_MGEnsemble_2025 | 2025 | KBS 2025 | YES | NO | MODEL_DEFINED_FIXED | GCN | SPARSE_INTERACTION_ONLY | NO |
| KT065 | KT065_CSGKT_2025 | 2025 | KBS 2025 | YES | NO | MODEL_DEFINED_FIXED | GCN | SPARSE_INTERACTION_ONLY | NO |
| KT066 | KT066_HyperKT_2025 | 2025 | IEEE TNNLS 2025 | YES | YES | MODEL_DEFINED_FIXED | HYPERGRAPH_GNN | SPARSE_INTERACTION_ONLY | NO |
| KT067 | KT067_SKMGKT_2025 | 2025 | EAIT 2025 | YES | NO | EXTERNAL_FIXED | GCN | SPARSE_INTERACTION_ONLY | NO |
| KT068 | KT068_HKT_2025 | 2025 | IP&M 2025 | YES | YES | EXTERNAL_FIXED | GNN_GENERIC | SPARSE_INTERACTION_ONLY | NO |
| KT069 | KT069_AEGOTCDKT_2025 | 2025 | WWW 2025 | YES | NO | DYNAMIC_LEARNED | GRAPH_OPTIMAL_TRANS | SPARSE_INTERACTION_ONLY | NO |
| KT070 | KT070_Coda_2025 | 2025 | KDD 2025 | YES | NO | DYNAMIC_LEARNED | GCN | SPARSE_INTERACTION_ONLY | NO |
| KT076 | KT076_KGNNKT_2025 | 2025 | ICIC 2025 | YES | NO | EXTERNAL_FIXED | HETEROGENEOUS_GNN | SPARSE_INTERACTION_ONLY | NO |
| KT077 | KT077_R2GCurL_2026 | 2026 | IEEE TKDE 2026 | YES | NO | DYNAMIC_LEARNED | DYNAMIC_GNN | SPARSE_INTERACTION_ONLY | NO |
| KT079 | KT079_STGSKT_2026 | 2026 | DASFAA 2026 | YES | NO | DYNAMIC_LEARNED | SPATIOTEMPORAL_GNN | SPARSE_INTERACTION_ONLY | NO |

Row count in this table: 37 (must be 37).

## 5. Field-level evidence for locked claims

### Strict KC cold-start YES = 0/37; item cold-start YES = 1/37

| paper_id | strict_kc_cold_start | item_cold_start | learner_cold_start | source |
|---|---|---|---|---|
| KT044 | NO | YES | NO | tables/sparse_coldstart_audit.csv |

All other primary-core rows are NO / NO / NO for those three fields (see the same CSV).

### ECE reporting = 0/37

Locked statement in `audit/LOCKED_COUNTS_v1.5.md`. No manuscript in the 37-paper set is coded as reporting ECE.
That **manuscript-reporting** claim is unchanged.

### Survey-computed REPRODUCED ECE overlay (Path A; lab record, not a reported result)

Withdrawn from the main manuscript on 2026-11-16. The author decision is to keep DyGKT in the 37-paper corpus and not to report these run numbers in the paper. The rows below stay as the lab record. They are not cited from the main text, and they do not change manuscript ECE reporting \(0/37\).

Source: `09_benchmark/path_a_ece/results/dygkt_assist17_ece.json` and `RUN_LOG_DyGKT_assist17.md`.
Author code: DyGKT (`KT038`); dataset ASSIST17; seed 0; equal-width $M=10$ on the transductive test split.

| paper_id | model | dataset | split | n | ECE (M=10) | Brier | test AUC (author metric) | evidence_source_type |
|---|---|---|---|---:|---:|---:|---:|---|
| KT038 | DyGKT | assist17 | test | 94156 | 0.0361 | 0.1770 | 0.8025 | REPRODUCED |

Do **not** rewrite the $0/37$ manuscript-reported ECE cell to YES. Do **not** pool this overlay into a cross-paper ECE ranking.

### H1 S-criterion (why N_S=9, not 14)

| paper_id | S_criterion | note |
|---|---|---|
| KT011 | Y | Paper states joint contrastive loss for representations. |
| KT026 | Y | Previous pilot coding classified PEBG as generic pretraining. Final adjudication overturned this decision because PEBG reconstructs explicit and implicit relati |
| KT039 | Y | Self-supervised signals from the observed sequence; graph_source=NONE. |
| KT042 | Y | Authors add an auxiliary self-supervised contrastive task. |
| KT043 | Y | Explicit pretext-task wording and contrastive losses. |
| KT044 | N | Inductive + LLM structure extraction is not an SSL pretext. Removed from N_S. |
| KT047 | Y | Official title is the dual-channel heterogeneous-graph paper. |
| KT050 | Y | InfoNCE stated as learning objective. |
| KT066 | Y | Authors call this a self-supervised signal. |
| KT068 | Y | Caption states reconstruction + hierarchical contrastive learning. |
| KT070 | N | Masking only sparsifies the code graph. Denoising/regularization is not a pretext target. |
| KT076 | N | LLM KG construction is G-criterion evidence; no SSL objective on the title page or in the coding record. |
| KT077 | N | Curriculum learning and RL are excluded as SSL-alone cues. |
| KT079 | N | Dynamic/streaming graph is G-criterion only. |

## 6. QA1–QA8 scores

Source file: `supplementary/supplementary_quality_scores.csv`.
Manuscript tiers use `audit/LOCKED_COUNTS_v1.5.md`: drop KT078 and KT080–KT083; cap QA6 at 2; HIGH 11 / MODERATE 26 / mean 0.76.
HIGH IDs (locked): KT029, KT033, KT035, KT038, KT044, KT050, KT060, KT064, KT066, KT070, KT077.
Some `raw_score` cells in the CSV do not equal the arithmetic sum of QA1–QA8; **do not invent a corrected score**. Use the locked HIGH list for manuscript claims.

| paper_id | QA1 | QA2 | QA3 | QA4 | QA5 | QA6 | QA7 | QA8 | raw_score (file) | norm (file) | tier (file) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KT004 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT010 | 2 | 2 | 1 | 2 | 1 | 1 | 0 | 1 | 11 | 0.6875 | MODERATE |
| KT011 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT012 | 2 | 2 | 1 | 2 | 1 | 1 | 0 | 1 | 11 | 0.6875 | MODERATE |
| KT014 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT016 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT023 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT026 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT029 | 2 | 2 | 2 | 2 | 1 | 2 | 0 | 2 | 13 | 0.8125 | HIGH |
| KT031 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT033 | 2 | 2 | 2 | 2 | 1 | 2 | 0 | 2 | 13 | 0.8125 | HIGH |
| KT035 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 13 | 0.8125 | HIGH |
| KT036 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT037 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT038 | 2 | 2 | 2 | 2 | 1 | 3 | 0 | 2 | 14 | 0.8750 | HIGH |
| KT039 | 2 | 2 | 2 | 2 | 1 | 2 | 0 | 1 | 12 | 0.7500 | MODERATE |
| KT042 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT043 | 2 | 2 | 1 | 2 | 1 | 1 | 0 | 2 | 11 | 0.6875 | MODERATE |
| KT044 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 14 | 0.8750 | HIGH |
| KT047 | 2 | 2 | 1 | 2 | 1 | 1 | 0 | 2 | 11 | 0.6875 | MODERATE |
| KT050 | 2 | 2 | 2 | 2 | 1 | 2 | 0 | 2 | 13 | 0.8125 | HIGH |
| KT052 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT053 | 2 | 2 | 1 | 2 | 1 | 1 | 0 | 2 | 11 | 0.6875 | MODERATE |
| KT056 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT060 | 2 | 2 | 2 | 2 | 1 | 2 | 0 | 2 | 13 | 0.8125 | HIGH |
| KT062 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT063 | 2 | 2 | 1 | 2 | 1 | 1 | 0 | 2 | 11 | 0.6875 | MODERATE |
| KT064 | 2 | 2 | 2 | 2 | 1 | 2 | 0 | 2 | 13 | 0.8125 | HIGH |
| KT065 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT066 | 2 | 2 | 2 | 2 | 1 | 3 | 0 | 2 | 14 | 0.8750 | HIGH |
| KT067 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT068 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 12 | 0.7500 | MODERATE |
| KT069 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 13 | 0.8125 | HIGH |
| KT070 | 2 | 2 | 2 | 2 | 1 | 2 | 0 | 2 | 14 | 0.8750 | HIGH |
| KT076 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 13 | 0.8125 | HIGH |
| KT077 | 2 | 2 | 2 | 2 | 1 | 2 | 0 | 2 | 14 | 0.8750 | HIGH |
| KT078 | 2 | 2 | 1 | 2 | 1 | 2 | 0 | 1 | 12 | 0.7500 | MODERATE |
| KT079 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 13 | 0.8125 | HIGH |

Excluded from the 37-paper QA claim (present in the raw file only): KT078, KT080, KT081, KT082, KT083.

## 7. Coder reliability / adjudication

Coding-sample pair table: `supplementary/inter_rater_coding.csv` (20 papers × 8 fields; locator-assisted NguyenKT).
B as submitted: `08_quality_reliability/inter_rater_coding_sample_BLIND_EMPTY_v1.3_AS_SUBMITTED.csv` (`coderB_id=NguyenKT`).
**Recomputed κ (2026-09-15):** `audit/KAPPA_RECOMPUTATION.md` and `tables/reliability_kappa_recomputed.csv`.
Invariant all-NO fields (`strict_kc_cold_start`, `learner_cold_start`, `ece_reported`): percent agreement 100%; Cohen's κ **NA** (\(p_e=1\)); excluded from macro-average.
Locator-assisted mean over **5 defined** κ: **0.97** (158/160). Independent DaoMT mean over **5 defined** κ: **0.96** (157/160). Not pooled.
Prior 8-field means 0.98 / 0.97 (which treated undefined κ as 1) are withdrawn.
Do **not** use `08_quality_reliability/INTER_RATER_RELIABILITY_REPORT_v1.0.md` (no pair table; $N=42$).

Still absent (protocol §20–21): `inter_rater_screening.csv`, `inter_rater_fulltext.csv`.

| Item | Status |
|---|---|
| Double-coded primary-core papers | 20/37 coding sample |
| Pre-adjudication (NguyenKT, locator) | 158/160; macro-κ **0.97** over 5 defined fields (3 invariant = NA) |
| Pre-adjudication (DaoMT, independent) | 157/160; macro-κ **0.96** over 5 defined fields (3 invariant = NA) |
| Adjudicated cells | KT011/KT047 family → MULTIVIEW; KT026 provenance → MODEL_DEFINED; KT070 provenance → DYNAMIC; KT068 encoder → GNN_GENERIC |
| Screening / full-text pair files | Not present |

## 8. Supplementary Table S-PRISMA-5 (five verification removals)

**Upload-facing filename:** `supplementary/Table_S-PRISMA-5.csv`  
(identical content also kept as `supplementary/supplementary_prisma_five_unverified.csv`).

These five expansion IDs were previously screened `INCLUDE_FULLTEXT` / coded as candidates but removed when freezing \(N=37\) (legacy \(N=42\)). Exclusion reasons are DOI non-resolution or DOI→wrong-paper identity mismatch (Crossref check 2026-09-15); no matching PDFs in `14_references/`.

| Record ID | Claimed title | Verification problem | Final exclusion reason |
|---|---|---|---|
| KT078 | Contrastive Multi-View Graph Neural Network for Sequential Knowledge Tracing | DOI `10.1609/aaai.v39i1.30500` → Crossref 404 | Corpus verification failure — DOI does not resolve |
| KT080 | Debiased Graph Representation Learning for Attentive Knowledge Tracing | DOI `10.1145/3690624.3709500` → Crossref 404 | Corpus verification failure — DOI does not resolve |
| KT081 | Hyperbolic Graph Neural Network for Hierarchical Knowledge Tracing | DOI `10.24963/ijcai.2025/450` resolves to a different paper | Corpus verification failure — DOI identity mismatch |
| KT082 | Generative Masked Graph Auto-Encoder for Knowledge Tracing | DOI `10.1145/3627673.3679900` resolves to a different paper | Corpus verification failure — DOI identity mismatch |
| KT083 | Dual-View Heterogeneous Graph Contrastive Learning for Knowledge Tracing | DOI `10.1016/j.neunet.2026.107500` → Crossref 404 | Corpus verification failure — DOI does not resolve |

## 8b. Supplementary Table S-Search (16 logged searches)

**Upload-facing filename:** `supplementary/Table_S-Search.csv`

Copied from `03_search/search_log.csv` on 2026-11-13. Sixteen rows, SRCH_001–SRCH_016. Logged record counts sum to 2,017. Run date for every row is 2026-08-26. On 23 November 2026 a check of all 1,522 project files did not find the 16 named export files. These counts were not re-counted from raw records.

The `notes` column records two construction facts already in `audit/A1_QUERY_GAP_ANALYSIS.md`: the Q-G and Q-S term lists differ across databases, and the two arXiv strings use `OR`, so a title containing "knowledge tracing" matches without a graph or self-supervised term.

## 8c. Supplementary Table S-Search-Rerun (files saved 14–16 November 2026)

**Upload-facing filename:** `supplementary/Table_S-Search-Rerun_2026-11-16.csv`

Counted on 23 November 2026 from the twelve files in `03_search/exports`. IEEE 112 and 27; ScienceDirect 66 and 25 BibTeX entries; Springer 558 and 546; Scopus 381, 192, 85 and 38; arXiv 273 and 199 entry elements. ACM SRCH_001, ACM SRCH_002, Web of Science SRCH_011 and SRCH_012 have no file. These counts are not added to \(N_{\mathrm{rec}}=2{,}017\).

Own-record matches, by title or DOI, for the seven papers read by 23 November 2026: every one of the seven appears in at least one saved file. Scopus Q-S contains all seven. The arXiv files contain none of the seven as an own title. A publication-year value of 2026 in a saved file is not a 31 July cutoff.


## 9. Path A REPRODUCED ECE (DyGKT/ASSIST17)

Withdrawn from the main manuscript on 2026-11-16. This section is a lab record, not a result reported in the paper. DyGKT remains in the 37-paper corpus. Manuscript ECE reporting stays \(0/37\).

Manifest: `supplementary/DYGKT_ASSIST17_REPRODUCTION_MANIFEST.md`.  
Bins: `supplementary/dygkt_assist17_ece_bins.csv`.  
Audit: `audit/DYGKT_REPRODUCTION_AUDIT.md` (CASE A).  
Does not change manuscript ECE reporting \(0/37\).
