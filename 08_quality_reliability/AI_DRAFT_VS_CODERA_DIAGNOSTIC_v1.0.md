# Diagnostic only — AI-adopted draft vs locked Coder A

**Not Cohen's κ for the manuscript.** Not human–human IRR.

Date: 2026-09-13  
B file: `inter_rater_coding_sample_BLIND_v1.0.csv` (`coderB_id=HUMAN_ADOPTED_AI_DRAFT_2026-09-13`)  
A file: `inter_rater_coderA_locked_v1.0.csv`

## Field agreement (20 papers)

| Field | Agree | Disagree |
|---|---:|---:|
| S_criterion | 20 | 0 |
| ssl_family | 20 | 0 |
| graph_provenance | 20 | 0 |
| gnn_encoder | 18 | 2 |
| strict_kc_cold_start | 19 | 1 |
| item_cold_start | 18 | 2 |
| learner_cold_start | 20 | 0 |
| ece_reported | 20 | 0 |

## Disagreements (do not auto-resolve)

| Paper | Field | A (locked) | Adopted draft | Why the draft differed |
|---|---|---|---|---|
| KT026 | item_cold_start | YES | NO | Locator: next-item “new question” + no hold-out string. Locked CSV marks item CS YES. |
| KT031 | gnn_encoder | GCN | OTHER | Paper names Metapath2Vec; GCN is related work (GIKT). |
| KT044 | gnn_encoder | GCN | GAT | Method uses three GAT layers; locked display token is GCN. |
| KT044 | strict_kc_cold_start | YES | NO | §5.5 removes 1/4 *questions*. Figure 1 also discusses a new concept. Locked YES = zero-exposure KC. |
| KT076 | item_cold_start | YES | NO | Rendered experiments: 7:2:1 + graph ablation, no explicit new-item split in extract. |

Do **not** write a κ into §II from this table.

If a future independent human recodes the 20 papers without this draft, then compute κ.
