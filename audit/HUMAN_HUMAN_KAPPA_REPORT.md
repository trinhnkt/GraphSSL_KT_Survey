# Human–human coding reliability (NguyenKT vs DaoMT)

**Date:** 2026-11-25

## Sources (pre-adjudication)

- NguyenKT: `08_quality_reliability\inter_rater_coding.csv` (`coderB_submitted`, locator-assisted)
- DaoMT: `08_quality_reliability\inter_rater_coding_sample_BLIND_EMPTY_v1.4_DaoMT_FULL20_AS_SUBMITTED.csv` (independent, no locator)
- **Not used as a human coder:** `inter_rater_coderA_locked_v1.0.csv` (AI/reference locked A).

## Scope

- Overlapping papers: **20** (`KT004, KT011, KT014, KT026, KT031, KT035, KT037, KT038, KT039, KT042, KT043, KT044, KT047, KT050, KT066, KT068, KT070, KT076, KT077, KT079`)
- Paired cells: **160**
- Raw cell agreement: **155/160**
- Nominal, unweighted Cohen’s κ per field.
- If \(p_e=1\): κ = **NA** (not replaced by 1).
- Macro-average only over **defined** field-wise κ.
- Do **not** pool with screening κ or AI–human κ.

## Field-wise results

| Field | n | agree | raw | pe | κ | status |
|---|---:|---:|---:|---:|---:|---|
| S-criterion (`S_criterion`) | 20 | 20/20 | 1.0000 | 0.5050 | 1.0000 | DEFINED |
| pretext family (`ssl_family`) | 20 | 18/20 | 0.9000 | 0.3700 | 0.8413 | DEFINED |
| graph provenance (`graph_provenance`) | 20 | 18/20 | 0.9000 | 0.3375 | 0.8491 | DEFINED |
| GNN encoder (`gnn_encoder`) | 20 | 19/20 | 0.9500 | 0.1575 | 0.9407 | DEFINED |
| item cold-start (`item_cold_start`) | 20 | 20/20 | 1.0000 | 0.9050 | 1.0000 | DEFINED |
| learner cold-start (`learner_cold_start`) | 20 | 20/20 | 1.0000 | 1.0000 | NA | NA_PE_EQ_1 |
| strict KC cold-start (`strict_kc_cold_start`) | 20 | 20/20 | 1.0000 | 1.0000 | NA | NA_PE_EQ_1 |
| ECE reported (`ece_reported`) | 20 | 20/20 | 1.0000 | 1.0000 | NA | NA_PE_EQ_1 |

**Macro-average κ (defined fields only, n=5):** **0.9262**

## Disagreements

| paper | field | NguyenKT | DaoMT |
|---|---|---|---|
| KT011 | ssl_family | GRAPH_CONTRASTIVE | MULTIVIEW_CONTRASTIVE |
| KT047 | ssl_family | MULTIVIEW_CONTRASTIVE | GRAPH_CONTRASTIVE |
| KT026 | graph_provenance | EXTERNAL_FIXED | MODEL_DEFINED_FIXED |
| KT070 | graph_provenance | DYNAMIC_LEARNED | MODEL_DEFINED_FIXED |
| KT068 | gnn_encoder | GNN_GENERIC | HETEROGENEOUS_GNN |

## Manuscript implication

Main-text reliability should prioritize this NguyenKT↔DaoMT analysis.
AI/reference vs human comparisons remain supplementary secondary validation.

Outputs: `06_coding\inter_rater_human_human_20papers.csv`; `tables\HUMAN_HUMAN_CODING_RELIABILITY.csv`.
