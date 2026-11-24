# Expanded-corpus counts: sparse/cold-start, calibration, and QA

Date: 2026-11-24. Counts below were computed for the expanded corpus and are locked into `data/PRIMARY_CORE_EXPANDED_2026-11-24.csv` (`CORPUS_EXPANDED_AND_FROZEN = YES`). The prior row file `data/PRIMARY_CORE_EXPANDED_2026-11-23.csv` is retained and was not overwritten.
Denominator for every count below is 44, or the subset named in the sentence.
The live manuscript was not edited in the counts pass. Deposited 37-row tables were not overwritten.
Thresholds were not changed: HIGH is at least 0.80, MODERATE is 0.55 to 0.79, LIMITED is below 0.55. Normalized score is raw/16. QA6 is capped at 2.

## A. Sparse and cold-start

Codes follow the decision table. A sentence that only says cold start or sparsity is not YES. A random 80/20 or 6:2:2 split is not YES. An external graph is not strict KC cold-start. RMSE is not a cold-start code.

| Construct | YES | Papers |
|---|---:|---|
| interaction_drop | 1 | KT086 HCMKT |
| item_cold_start | 1 | KT044 SINKT |
| learner_cold_start | 2 | KT023 SGKT; KT087 CoSKT |
| strict_KC_cold_start | 0 | none |

HCMKT Figure 5 trains on 20%, 40%, and 60% of ASSISTments2009, ASSISTments2017, Junyi, and YMath and reports AUC, ACC, and RMSE at each rate. That is interaction-drop. It is not item, learner, or strict KC cold-start. The separate 6:2:2 split is the main evaluation split and is not a second YES.

SINKT remains the item cold-start paper: a question hold-out scored as prediction for unseen questions. No second item hold-out was found.

SGKT Section 5.5 builds eight training-sequence groups with intercepted lengths (0, 5] through (0, 100] and compares model performance on those groups. That is learner cold-start (truncated history, scored by length). It is not an interaction-drop and not a zero-exposure KC split.

CoSKT Section IV-H and Figure 6 report performance for learning sequences shorter than 50, including length 5. That is a scored truncated-history condition, so learner cold-start is YES. The section title alone was not the code.

HHSKT is NO on all four constructs. Its own protocol is 5-fold cross-validation with 60% training, 20% validation, and 20% testing (experiment section). The sentence about AUC declining until 50% of the data cites Lee (2019) as background for TrueSkill. It is not an HHSKT results-by-drop-level table. The printed claim that interaction-drop is YES for HHSKT does not meet the decision table.

Also NO, after the PDF sentences were read: DyGKT discusses a difficulty assessment for unseen questions and does not report a withheld-item split. DGMN says the model can operate in cold-start scenarios and does not report a qualifying split. S2-HHN and AEGOT mention cold start as a problem property. DECKT's cold-start sentences cite other papers. KT-Deeper's 5/10/15/20/25% edge-removal ratios are a graph-generation probe (Precision@K, MAP), not an interaction-drop knowledge-tracing evaluation. PEBG's new-question wording is the next-question prediction task. KGNN-KT has an empty text layer; its four codes stay NO and were not re-read.

Full coding:

| paper_id | interaction_drop | item_cold_start | learner_cold_start | strict_KC_cold_start |
|---|---|---|---|---|
| KT004 | NO | NO | NO | NO |
| KT010 | NO | NO | NO | NO |
| KT011 | NO | NO | NO | NO |
| KT012 | NO | NO | NO | NO |
| KT014 | NO | NO | NO | NO |
| KT016 | NO | NO | NO | NO |
| KT023 | NO | NO | YES | NO |
| KT026 | NO | NO | NO | NO |
| KT029 | NO | NO | NO | NO |
| KT031 | NO | NO | NO | NO |
| KT033 | NO | NO | NO | NO |
| KT035 | NO | NO | NO | NO |
| KT036 | NO | NO | NO | NO |
| KT037 | NO | NO | NO | NO |
| KT038 | NO | NO | NO | NO |
| KT039 | NO | NO | NO | NO |
| KT042 | NO | NO | NO | NO |
| KT043 | NO | NO | NO | NO |
| KT044 | NO | YES | NO | NO |
| KT047 | NO | NO | NO | NO |
| KT050 | NO | NO | NO | NO |
| KT052 | NO | NO | NO | NO |
| KT053 | NO | NO | NO | NO |
| KT056 | NO | NO | NO | NO |
| KT060 | NO | NO | NO | NO |
| KT062 | NO | NO | NO | NO |
| KT063 | NO | NO | NO | NO |
| KT064 | NO | NO | NO | NO |
| KT065 | NO | NO | NO | NO |
| KT066 | NO | NO | NO | NO |
| KT067 | NO | NO | NO | NO |
| KT068 | NO | NO | NO | NO |
| KT069 | NO | NO | NO | NO |
| KT070 | NO | NO | NO | NO |
| KT076 | NO | NO | NO | NO |
| KT077 | NO | NO | NO | NO |
| KT079 | NO | NO | NO | NO |
| KT084 | NO | NO | NO | NO |
| KT085 | NO | NO | NO | NO |
| KT086 | YES | NO | NO | NO |
| KT087 | NO | NO | YES | NO |
| KT040 | NO | NO | NO | NO |
| KT088 | NO | NO | NO | NO |
| KT089 | NO | NO | NO | NO |

## B. Calibration

File: `tables/CALIBRATION_EXPANDED.csv` (44 rows).

| Field | YES |
|---|---:|
| ECE_reported | 0 |
| Brier_reported | 0 |
| RMSE_reported | 14 |
| NLL_or_logloss_evaluation_reported | 1 |
| reliability_or_calibration_plot_reported | 1 |

RMSE is an overall prediction error. It is not counted as calibration. The 14 RMSE papers are KT014, KT035, KT037, KT039, KT040, KT042, KT056, KT063, KT065, KT066, KT068, KT070, KT077, and KT086. HCMKT reports RMSE in Table 4 and Figure 5. DTransformer reports MAE and RMSE in Table 2.

The one reliability plot is CL4KT (KT039), Figure 7, binned by predictions, with no ECE or Brier summary.

DECKT Figure 4 is not a reliability plot. The body says the heatmap shows predictive calibration. The caption is Prediction visualization analysis of one student's predicted probabilities. ECE and Brier are not reported.

The one evaluation NLL is KT-Deeper Table 5: an NLL gap between training and test data for the graph-generation model. It is not ECE, not Brier, and not a next-response calibration score. Training-loss NLL in GKT, JKT, HHSKT, the capsule model, HyperKT, and SKM-GKT is coded NO for the evaluation column.

KGNN-KT (KT076) has an empty text layer. Its five calibration fields are NO and are not a fresh keyword hit.

## C. QA

The 37 deposited scores were not changed. QA1-QA8 were coded for the seven papers that are outside that file. QA6 = 0 when no author artifact was found. The EdNet dataset repository is not an author artifact. Author repositories found in the papers: CoSKT `https://github.com/lucky7-code/CoSKT`; DTransformer `https://github.com/yxonic/DTransformer`.

| paper_id | model | QA1 | QA2 | QA3 | QA4 | QA5 | QA6 | QA7 | QA8 | raw | norm | tier |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KT084 | DECKT | 2 | 2 | 1 | 2 | 1 | 0 | 0 | 2 | 10 | 0.6250 | MODERATE |
| KT085 | KT-Deeper | 2 | 2 | 2 | 2 | 1 | 0 | 0 | 2 | 11 | 0.6875 | MODERATE |
| KT086 | HCMKT | 2 | 2 | 2 | 2 | 1 | 0 | 2 | 1 | 12 | 0.7500 | MODERATE |
| KT087 | CoSKT | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 14 | 0.8750 | HIGH |
| KT040 | DTransformer | 2 | 2 | 2 | 2 | 1 | 2 | 0 | 2 | 13 | 0.8125 | HIGH |
| KT088 | SP-CLKT | 2 | 2 | 1 | 2 | 1 | 0 | 0 | 1 | 9 | 0.5625 | MODERATE |
| KT089 | CLBG | 2 | 2 | 1 | 2 | 1 | 0 | 0 | 1 | 9 | 0.5625 | MODERATE |

QA3 is 1 for DECKT, SP-CLKT, and CLBG because a validation procedure or implementation section is present and a train/test ratio is not stated. QA3 is 2 where the paper states 5-fold cross-validation (KT-Deeper), a 6:2:2 split (HCMKT), an 80/20 split (CoSKT), or an 80/20 student split (DTransformer).

QA7 is 2 only when one of the four cold-start constructs is an evaluation: HCMKT (interaction-drop) and CoSKT (learner cold-start). The other five new papers are 0.

QA8 is 2 when the paper reports a GPU model or a complexity formula (DECKT A100 and complexity; KT-Deeper Tesla K80; DTransformer TITAN V100). QA8 is 1 when implementation settings are reported without a GPU model or complexity formula (HCMKT, CoSKT, SP-CLKT, CLBG).

### Item distribution on 44 papers

| Item | 0 | 1 | 2 |
|---|---:|---:|---:|
| QA1 Task clarity | 0 | 0 | 44 |
| QA2 Data and preprocessing | 0 | 0 | 44 |
| QA3 Split, provenance, leakage | 0 | 9 | 35 |
| QA4 Baselines and ablations | 0 | 0 | 44 |
| QA5 Statistical uncertainty | 0 | 44 | 0 |
| QA6 Author artifacts | 5 | 26 | 13 |
| QA7 Sparse and cold-start construct | 40 | 0 | 4 |
| QA8 Computational reporting | 0 | 9 | 35 |

### Tiers on 44 papers

- HIGH: 13
- MODERATE: 31
- LIMITED: 0
- Corpus mean of normalized scores: 0.7472

HIGH paper codes: KT029, KT033, KT035, KT038, KT044, KT050, KT060, KT064, KT066, KT070, KT077, KT087, KT040.

Two new HIGH papers are KT040 (raw 13, 0.8125) and KT087 (raw 14, 0.8750). The other five new papers are MODERATE. LIMITED stays empty.

The deposited QA7 scores for the original 37 were initially carried forward. On 2026-11-24 those two cells were aligned to the locked cold-start fields: HHSKT QA7 = 0; SGKT QA7 = 2 (`audit/QA7_COLDSTART_ALIGNMENT_2026-11-24.md`; DEV-20261124-01). HIGH/MODERATE counts and the corpus mean remain 13 / 31 / 0.7472; the HIGH identifier list replaces KT035 with KT023.

## Manuscript statistics that must change

These are printed analysis denominators and claims. This file does not edit the manuscript. Search-log identification is separate: `N_rec = 2,017` and the PRISMA stage arithmetic are not replaced by the 44-paper coding, because this pass does not show that the seven added papers were inside the original identification set.

| Printed statistic | Where it is used | Expanded result |
|---|---|---|
| Surveys 37 primary-core PDFs | Abstract; highlights; corpus section | 44 primary-core papers |
| `N_G = 36` (97.3%); only CL4KT is sequence-only inside that coding | Abstract; taxonomy; Graph-KT section | `N_G = 40`. Sequence-only SSL papers in the 44: KT039, KT040, KT087, KT088 |
| `N_S = 9` | Abstract; SSL section | `N_S = 16` |
| `N_{G cap S} = 8`; four exclusive pretext families; SSL table of 9 | Abstract; SSL table caption | `N_{G cap S} = 12`. The four-family table does not cover the expanded SSL set (15 contrastive, 1 generative reconstruction; view source is a second axis) |
| Provenance 19 / 8 / 9 among 36 graph papers | Taxonomy caption | Among 40 graph papers: model-defined fixed 24, external fixed 7, dynamically learned 8, unclear 1 (KT085). This provenance tally is not locked |
| Interaction-drop YES 1/37 (HHSKT) | Cold-start table and body; go/no-go row | 1/44, and the paper is HCMKT (KT086), not HHSKT |
| Strict KC cold-start 0/37 | Abstract-level claims; cold-start table; go/no-go | 0/44 |
| Item cold-start YES 1/37 (SINKT) | Cold-start table; go/no-go | 1/44 (KT044 SINKT) |
| Learner cold-start YES 0/37 | Cold-start table and body | 2/44 (KT023 SGKT, KT087 CoSKT) |
| ECE 0/37 | Abstract comparison table; ECE audit; go/no-go | 0/44 |
| Brier 0/36 scanned text layers | ECE audit; go/no-go | 0/44 |
| RMSE in 12 of 37, as prediction error | ECE audit; go/no-go | 14/44. Added HCMKT and DTransformer. Still not calibration |
| One calibration plot (CL4KT); no evaluation-time NLL | ECE audit | Reliability plot 1/44 (KT039). Evaluation NLL 1/44 (KT085 graph-generation NLL gap, not response calibration) |
| None of the seven report ECE, Brier, or a zero-exposure KC split, and they are outside the tables | Gateway extension paragraph | ECE, Brier, and strict KC remain zero after they are included. The sentence that they are outside the coding tables does not survive a 44-row rewrite |
| QA HIGH 11, MODERATE 26, LIMITED 0, mean 0.76 | QA section | HIGH 13, MODERATE 31, LIMITED 0, mean 0.7472 |
| QA item counts on 37: QA1 0/0/37, QA2 0/0/37, QA3 0/6/31, QA4 0/0/37, QA5 0/37/0, QA6 0/26/11, QA7 35/0/2, QA8 0/5/32 | QA distribution table | See the 44-paper item table above. QA1, QA2, QA4, and QA5 stay uniform. QA3, QA6, QA7, and QA8 change |
| QA7 is 2 only for HHSKT and SINKT | QA distribution paragraph | On the 44-paper score, QA7 is 2 for KT035, KT044, KT086, and KT087. KT035 is carried from the deposited file |
| QA7-not-applicable sensitivity: 31 HIGH, 6 MODERATE, mean 0.86, and only HHSKT and SINKT make a sparse claim | Sensitivity paragraph | That paragraph is a 37-paper sensitivity. It is not the expanded primary score, and its premise (only two papers make a sparse/cold-start claim) is no longer true |
| Graph-KT coding tables of 18 + 18 = 36, and SSL augmentation table of 9 | Table captions | Row counts become 40 graph papers and 16 SSL papers |

Check that still holds from the expanded gateway file, and that this pass did not change: `N_G + N_S - N_{G cap S} = 40 + 16 - 12 = 44`.

Not changed by this pass, and not to be rewritten as a 44-paper identification total: search-log `N_rec = 2,017`, and the PRISMA-style stage counts that end at 37.

