# IEEE TLT Manuscript Changelog

All notable changes to the IEEE Transactions on Learning Technologies (IEEE TLT) manuscript preparation package are documented in this file.

---

## [Full quality pass: facts + style] - 2026-11-25

- Fixed provenance percentages ($63.3/18.4/18.4$), venue-probe/gateway $N=53$ narrative, 49/22-row captions, sparse overlay $49+1+1+2$, appendix KT090–098.
- Clarified ICR: principal κ human–human; 0.97/0.96 Supplementary AI–human only.
- Light scientific style rewrite (Intro/sparse/synthesis). Report: `TLT/audit/MS_QUALITY_PASS_2026-11-25.md`. Still 16 pp.

## [AI disclosure align] - 2026-11-25

- `sec:ai_role`: principal coding $\kappa$ stated as human--human NguyenKT↔DaoMT; removed “κ vs AI-generated reference” wording.
- Documented step (vi) KT090–KT098 locator-backed verify; Acknowledgment clarified AI-locator ± author countersign.
- Cover letter: explicit AI primary screening/coding sentence. PDFs still 16+2 pp.

## [N=53 figure rebuild] - 2026-11-25

- Rebuilt five TikZ figures to locked N=53 counts: taxonomy, SSL framework, meta encoder bars, PRISMA, provenance pipeline ($31/9/9$; encoder $19/9/7/7/2/2/3$; $N_S=22$, $∩=18$).
- Live PDFs recompiled 16 pp; root `12_manuscript/` copies refreshed.

## [N=53 QA residual fix] - 2026-11-25

- Cleared post-promote N=44 wording: Graph-KT opener, agenda $53/53$, Acknowledgment 53 PDFs.
- QA tiers recomputed on FINAL_v2: HIGH/MOD/LIM $13/39/1$ (KT091 LIMITED), mean $0.73$; table counts synced (QA1--QA8 histograms).
- Live PDFs rebuilt 16 pp; portal pack PDFs refreshed.

## [Promote N=53 vNext to live] - 2026-11-25

- Locator verify KT090–KT098 complete (`HUMAN_VERIFY_SIGNOFF_KT090-098_v1.md`); freeze `YES_VERIFIED_AI_LOCATOR`.
- Promoted `Graph_SSL_KT_TLT_REVISED_vNext_{anonymous,full}` → live `main_tlt_*` and `manuscript_TLT_FORMATTED_v1.3`.
- Cover letter rewritten to $N=53$, $N_G=49$, $N_S=22$, $N_{G\cap S}=18$, provenance $31/9/9$, principal NguyenKT↔DaoMT κ, Zanellati complementary.
- N=44 live files archived under `_pre_promote_N44_2026-11-25/`. Portal pack: `_portal_pack_2026-11-25_N53/`. Submission still NO.

## [N=53 revised vNext MS] - 2026-11-25

- Built versioned revised package from live N=44 body: `Graph_SSL_KT_TLT_REVISED_vNext_{anonymous,full}.{tex,pdf}` (16 pp each).
- Counts synced to provisional freeze: $N=53$, $N_G=49$, $N_S=22$, $N_{G\cap S}=18$, provenance $31/9/9$.
- Related work + survey-comparison table now include Zanellati hybrid/informed KT (complementary scope).
- SSL Coding section uses final $N_S=22$ paradigm × view taxonomy; legacy 9-paper exclusive families stay Supplementary-only.
- Principal coding reliability stated as NguyenKT ↔ DaoMT (macro $\kappa\approx0.93$); AI–human kept Supplementary.
- Live `main_tlt_*` / cover / portal pack remain N=44 until author promotes vNext. Freeze: `audit/CORPUS_FINAL_FREEZE_v2.md` (`YES_PROVISIONAL_AI`).

## [QA7 align + SSL/threats residual fix] - 2026-11-24

- Aligned QA7 to locked cold-start: KT035 HHSKT $=0$, KT023 SGKT $=2$; HIGH IDs swap KT035→KT023; tiers stay 13/31 and mean $0.7472$.
- SSL section now leads with paradigm × view for $N_S=16$; four exclusive families labeled as pre-expansion historical coding.
- Threats/deviations updated (DEV-20261124-01). Evidence: `audit/QA7_COLDSTART_ALIGNMENT_2026-11-24.md`.

## [TLT review-recommendation fixes] - 2026-11-24

- Recounted GNN encoder display tallies on $N_G=40$ from locked CSV: GCN/generic 14, heterogeneous 7, Other 6, GAT 6, hypergraph 2, dynamic 2, NONE 3; rebuilt `fig_meta_analysis_charts` and `fig_taxonomy_2d`.
- Rewrote `COVER_LETTER.tex` to N=44 / 18 pages / screening subset / seven papers integrated (not outside tables).
- Shortened abstract to ~207 words on the three live tex files; synced body encoder `$n=/40$` claims.
- Gate residuals updated in `audit/TLT_FINAL_PRE_SUBMISSION_GATE.md`. Submission still NO.

## [N=44 rewrite + pre-submission gate] - 2026-11-24

- Corpus/provenance freezes already YES; manuscript abstract, contributions, methods, cold-start, QA, ECE, discussion, and figures synced to $N=44$, $N_G=40$, $N_S=16$, $N_{G\cap S}=12$, provenance $24/7/9$.
- Interaction-drop YES is HCMKT (not HHSKT); learner cold-start YES is SGKT + CoSKT; ECE/Brier $0/44$; RMSE $14/44$; QA $13/31/0$, mean $0.7472$.
- PRISMA stage arithmetic remains $750/140/103$ with original-path $140-103=37$; coded core after gateway update is $N=44$.
- Anonymous, full, and formatted PDFs rebuild at 18 pages. Gate: `audit/TLT_FINAL_PRE_SUBMISSION_GATE.md` (`READY_FOR_TLT_FINAL_REVIEW=YES`; submission=NO).

## [26 August exports confirmed absent] - 2026-11-23

- A check of all 1,522 files in this project did not find the 16 export files named in the 26 August 2026 search log. Git history contains only `03_search/exports/.gitkeep`. Identification stays 2,017. No recall fraction is reported. The PRISMA figure no longer says the 34-record seed list was used for recall.

## [Reference PDFs opened] - 2026-11-23

- Every PDF in `14_references` was opened. No text layer contains ECE or Brier. KGNN-KT remains image-only. DECKT Figure 4 uses the word calibration for a prediction heatmap and does not report ECE or Brier. HCMKT and DTransformer report RMSE; those reports stay outside the twelve-of-37 count. CoSKT's cold-start discussion is short sequences and few students, not a zero-exposure KC split. Itemized counts stay at 37. Detail: `audit/_a1_evidence/pdf_open_2026-11-23.csv`.

## [Eligibility date moved to 23 November 2026] - 2026-11-23

- Author decision: papers read for this revision are eligible through 23 November 2026. The logged search that produced 2,017 records stays 2015-01-01 to 2026-07-31. The new date is not a completed database boundary. Itemized counts stay at 37. Locked scope text was not edited. Detail: `00_protocol/protocol_deviations.md`, DEV-20261123-01.

## [November rerun files counted] - 2026-11-23

- Twelve export files saved on 14 and 16 November 2026 were counted from the files and written to Supplementary Table S-Search-Rerun. The twelve counts are not added to 2,017. Each of the seven full-text papers is an own record in at least one of those files. ACM and Web of Science still have no file.

## [Missing 26 August exports] - 2026-11-23

- The 16 export files named in the search log were not recovered. The identification total stays the logged sum, 2,017. The November rerun files are not used in its place. No recall fraction for the 34 seed records is reported. Detail: `audit/A1_EXPORTS_NOT_RECOVERED_2026-11-23.md`.

## [Bipartite chapter read] - 2026-11-23

- The ADMA chapter CLBG (DOI 10.1007/978-981-96-0821-8_14) meets both the graph criterion and the self-supervised criterion. It reports AUC and ACC, and it reports no ECE and no zero-exposure KC split. The gateway paragraph now covers seven papers. The itemized tables stay at 37. Entering all seven as rows would make N=44, N_G=40, N_S=16, and N_G∩S=12. Detail: `audit/A1_BIPARTITE_SCREEN_2026-11-23.md`.

## [Threats and agenda aligned with the gateway check] - 2026-11-22

- The scope paragraph, the search-completeness threat, conclusion contribution 4, and agenda items A1 and A2 now point at the six papers in the gateway check. Those papers stay outside the printed 37, the \(0/37\) ECE count, and the \(37/37\) cold-start count. The ten venue-probe candidates remain unread in full.

## [Gateway check in the manuscript] - 2026-11-22

- The three live manuscripts now record the 22 November 2026 full-text gateway check. DECKT, KT-Deeper, and HCMKT meet both criteria. CoSKT, DTransformer, and SP-CLKT meet the self-supervised criterion only. None of the six reports ECE or a zero-exposure KC split. The PRISMA count and the itemized tables stay at 37 because the six are not rows in those tables and were not shown to be among the 2,017 search records. The bipartite chapter remains unread.

## [A1 four supplied PDFs] - 2026-11-22

- CoSKT, DTransformer, and SP-CLKT meet the self-supervised criterion and do not meet the graph criterion. DECKT’s new PDF matches the paper already screened. All four remain outside the printed 37. The bipartite chapter still has no PDF. Detail: `audit/A1_FOUR_PDF_SCREEN_2026-11-22.md`.

## [A1 Han and HCMKT screen] - 2026-11-22

- The publisher PDFs of Han et al. 2024 and HCMKT meet both the graph criterion and the self-supervised criterion. Both are `INCLUDE_PRIMARY_CORE` and are not yet in the printed 37. CoSKT’s PDF is still absent. Live tex files were not edited. Detail: `audit/A1_HAN_HCMKT_SCREEN_2026-11-22.md`.

## [A1 three-paper screen attempt] - 2026-11-22

- HCMKT, CoSKT, and Han et al. 2024 were not added. No open full text was found, ScienceDirect blocked the request, and the three PDFs are not in `14_references`. CoSKT’s own abstract describes a consistency objective, which is not a final graph or SSL code. Detail: `audit/A1_THREE_SCREEN_2026-11-22.md`.

## [A1 reopen, DECKT screen] - 2026-11-22

- The author reopened the primary core. DECKT (10.3390/e27070685) meets KT, the graph criterion, and the self-supervised criterion on the PMC full text. It is not yet added to the printed 37. HCMKT, CoSKT, and Han et al. 2024 remain unscreened. Live tex files were not edited. Detail: `audit/A1_DECKT_SCREEN_2026-11-22.md`.

## [A1 open-source coverage] - 2026-11-22

- Crossref dates for the seven out-of-corpus candidates are all inside 1 January 2015–31 July 2026. OpenAlex citation links from the nine included SSL papers recover DECKT, CoSKT, Han et al. 2024, and HCMKT. The Xu survey’s reference list also contains Han et al. 2024. No paper was added. Printed counts are unchanged, and the live tex files were not edited. Detail: `audit/A1_OPEN_SOURCE_COVERAGE_2026-11-22.md`.

## [B11 recheck] - 2026-11-22

- Opened external records for the five unverified references. The printed pages for Piech, SAKT, and pyKT match those records. DGMN is still only an early-access Crossref record, and the Cursor site was not opened. The bibliography was not edited. `READY_FOR_SUBMISSION` stays NO.

## [Final gate] - 2026-11-22

- Clean-built the three live manuscripts with BibTeX. Anonymous PDF remains 17 pages; full and formatted PDFs remain 18 pages. No sentence was changed. The pre-submission gate is `audit/FINAL_TLT_PRE_SUBMISSION_GATE.md`: `READY_FOR_SUBMISSION = NO` because A1 and A3 do not pass.

## [C1--C3] - 2026-11-22

- Removed the paired provenance and encoder count figure from the main text. The taxonomy figure stays. The provenance-by-encoder table stays and is the encoder display. The encoder bar chart remains a supplementary figure because it repeats that table.
- Notation: \(N_{\mathrm{rec}}\) is the search-log record count (2,017), \(N\) is the number of primary-core papers, and \(n\) is a stated sample or the prediction count in the ECE sum. Unused symbols were removed from the notation table. The ECE row no longer repeats the 0/37 audit result. Counts are unchanged.
- Added the QA1--QA8 score distribution (counts of 0, 1, and 2) from the deposited quality-score file. Thresholds are unchanged: 11 HIGH, 26 MODERATE, 0 LIMITED, mean 0.76. Generic data sparsity is YES on all 37 deposited rows and is not used as a synthesis variable.

## [A4] - 2026-11-22

- Re-read the augmentation passages of the eight Graph+SSL papers and replaced the main-text phrases that the PDFs do not use (edge dropout, channel masking, hyperedge masking, three-view perturbation, dual-view masking, hierarchical perturbation). Family codes and the counts \(N_S=9\) and \(N_{G \cap S}=8\) are unchanged. The eight passages do not state that a prerequisite edge is kept or removed. The older token file was not rewritten.

## [A2] - 2026-11-20

- Narrowed the calibration conclusion to the scanned metrics. Manuscript ECE stays 0/37. The text-layer scan still finds no Brier score and one CL4KT calibration plot. A follow-up scan finds RMSE in 12 of the 37 PDFs, each time as an overall prediction error beside AUC or accuracy. T3 no longer treats “no ECE” as a statement that every calibration report is absent. The locked codebook was not given a new field. P0 was not cited.

## [Headings] - 2026-11-18

- Aligned the methodology headings with the existing limitation. The section is now “Review Methodology and PRISMA-Style Flow,” and the flow subsection and figure caption say PRISMA-style. The statement that no screening pair file is deposited, and that no screening κ is claimed, is unchanged. Counts are unchanged.

## [A3] - 2026-11-18

- Screening reliability was audited and not computed. The deposited title/abstract file has 43 rows and the full-text file has 48 rows, every row labeled `AI_ASSISTANT`. The protocol pair files `inter_rater_screening.csv` and `inter_rater_fulltext.csv` are absent. No screening κ was written into the manuscript.

## [Corpus retained] - 2026-11-18

- Author decision: the submitted primary core stays the 37 deposited papers. DECKT, DTransformer, self-paced contrastive KT, Han et al. 2024, HCMKT, the bipartite-graph chapter, and CoSKT are not added. Counts are unchanged. The missing 2026-08-26 exports and the missing screening ledger stay recorded in `audit/A1_CORPUS_FREEZE_2026-11-18.md`. No manuscript sentence was edited.

## [PDF rebuild] - 2026-11-18

- Rebuilt the five figure PDFs and the three live manuscript PDFs. BibTeX now includes Shukurlu, arXiv:2504.15163. The opened PDFs no longer contain the withdrawn DyGKT ECE 0.0361 or Brier 0.1770. DyGKT remains KT038. Manuscript ECE reporting remains 0/37. Each manuscript PDF is 17 pages. Title-named copies and both cover-letter PDFs were refreshed from these sources.

## [B10] - 2026-11-18

- Author decision: submit this survey in parallel with P0. The survey does not cite P0. Agenda A2 stays the current recommendation to report ECE and Brier. The three live tex files, cover letters, and highlights already matched that decision, so no sentence was changed.

## [B7 and B8] - 2026-11-17

- Added one Scope of Claims paragraph at the end of the Introduction and removed repeated disclaimer sentences. The methodological-limitations subsection was removed because Threats to Validity already states those points. Threats itself was not shortened.
- Added Shukurlu, arXiv:2504.15163, as a column in the prior-survey table, with section locators from the saved full text. Stated that the 0/37 ECE count is inside this Graph/SSL corpus. Xu cell wording was not changed. BibTeX and PDFs were not rebuilt.

## [B1 and B9] - 2026-11-16

- Author decision: remove the DyGKT/ASSIST17 numeric overlay from the main manuscript. DyGKT stays in the 37-paper corpus as KT038. Manuscript ECE reporting stays 0/37. The reproduction manifest and bin table remain a lab record and are marked withdrawn from the main text.
- Group B was already one paragraph with no hyperbolic, continuous-time, or causal formula. No rewrite.
- Compiled PDFs were not rebuilt in this pass.

---

## [v1.6.27] - 2026-11-11 (reviewer-response revisions 1-10)

- Sparse/cold-start: new `tables/sparse_coldstart_audit_v1.9.csv` (`sparse_interaction_drop_eval` YES for KT035 only; constant generic-sparsity column dropped; deposited v1 file unchanged). Generic sparsity removed from Contribution 3 and conclusion. One-sentence learner cold-start definition plus decision table.
- Contribution 4 renamed ECE reporting audit; keyword scan of 36 PDFs (ECE 0, Brier 0, one calibration plot in CL4KT; KGNN-KT has no text layer). Output: `supplementary/calibration_keyword_scan_v1.9.csv`.
- Provenance: sub-bins of the displayed model-defined code (Q-matrix 3 / log-derived 10 / architecture-defined 6), provenance x encoder cross-tab (35 cells, 15 empty, no outcome per cell), per-paper eight-value records in Appendix A. Disclosed that 24/36 records map to the display, 5 differ with PDF-level adjudication, 7 differ without (sensitivity 16/8/11 + 1 unclassified). Headline 19/8/9 unchanged.
- T1/T3 verdicts changed from NO-GO to "not enough evidence to GO"; T2 "pedagogical object" claim softened; worked SINKT example added.
- New subsections: Role of the AI Research Assistant, Venue-Extension Probe, Deviations from the Locked Protocol. Acknowledgment rewritten to match records (41/45 coding files name the AI assistant as coder; screening files list AI_ASSISTANT).
- DyGKT overlay: convenience choice and transductive setting stated.
- Venue probe logged in `03_search/search_log_venue_extension_v1.9.csv` and `03_search/venue_extension_candidates_v1.9.csv` (10 candidates, none coded; N=37 unchanged).
- Rebuilt PDFs: anonymous 17 pages; author-identified 17 pages (cap 18). Sources backed up in `12_manuscript/TLT/_backup_before_v1.9/`.

---

## [v1.6.26] - 2026-11-10 (four remaining Minors)

- SSL section title: Coding and Synthesis (not Taxonomy). Opening sentence drops “crucial paradigm / over-smoothing”.
- PRISMA figure boxes label 750/140/103 as report arithmetic; identification $N=2{,}017$ as locked search log; footer note that a screening ledger is not deposited.
- Discussion Graph-KT points to Sec.~III provenance instead of repeating the topology paragraph.

---

## [v1.6.25] - 2026-11-10 (wording 1→2→4→3→5)

- Contribution 1, Table II, abstract, and conclusion now state a locked 37-PDF core and search-log $N=2{,}017$; 750/140/103 remain report arithmetic; the missing screening ledger is in Contribution 1, not only Threats.
- Internal `DEV-20261106-*` codes removed from the manuscript body (kept in `protocol_deviations.md` and this changelog).
- Sparse table caption and following paragraph name `tables/sparse_coldstart_audit.csv` as the full 37-row file.
- SSL presented as a coding table ($N_S=9$; two families $n=1$), not a saturated taxonomy.
- Provenance synthesis: EXTERNAL supports T2 interpretation; DYNAMIC is a representation mechanism; neither licenses T1. SKT is one paper / one display code; Junyi remains an expert map at the 8-way level.
- Rebuilt PDFs: anonymous 14 pages; author-identified 15 pages (cap 18). Cover letter page count aligned.

---

## [v1.6.24] - 2026-11-10 (sync `12_manuscript/` to TLT)

- Parent folder now points to the TLT package: `12_manuscript/README.md`.
- Copied current 14-page full/anonymous PDFs, `COVER_LETTER.tex`/`pdf` (date 10 Nov 2026), and `references.bib` to `12_manuscript/`.
- `HIGHLIGHTS.md` v1.1 (N=37, provenance 19/8/9); TKDE v1.0 kept as `HIGHLIGHTS_v1.0_TKDE.md`.
- `SUGGESTED_REVIEWERS.md` venue set to TLT.
- Historical `Graph_Based_SSL_KT_Sparse_Concept_Survey_2026.tex` and `MANUSCRIPT_EVIDENCE_ALIGNED_DRAFT.tex` marked superseded; do not submit.

---

## [v1.6.23] - 2026-11-06 (score sequence 1--5)

- Screening: identification $N=2{,}017$ tied to `03_search/search_log.csv`; 750/140/103 labelled as search-expansion report arithmetic without a deposited row ledger (DEV-20261106-01). Cover letter aligned.
- Provenance display collapse documented (DEV-20261106-02). KT036 recoded EXTERNAL→MODEL_DEFINED after PDF check; totals $19/8/9$ (DEV-20261106-03). SKT mixed construction noted; Capsule GNN stays MODEL_DEFINED.
- `supplementary_quality_scores.csv` rebuilt so raw = QA6-capped component sum (37 rows; HIGH 11 unchanged). Prior file kept as `_v1_as_deposited.csv`.
- Figures `fig_taxonomy_2d` and `fig_graph_construction_pipeline` updated to 19/8/9.
- Locked counts: `audit/LOCKED_COUNTS_v1.8.md`.

---

## [v1.6.22] - 2026-11-03 (contribution-score actions; PDFs not rebuilt)

- Group B of the agenda cut to one paragraph (no equations); `W` notation row removed.
- RQ1 narrowed to provenance/encoder/reporting condition; leakage field not reported (values reviewer-inferred, no locators).
- "mean 0.76" corrected to corpus mean; QA7 `NA` sensitivity added (31 HIGH / 6 MODERATE / 0 LIMITED); new `supplementary/supplementary_quality_scores_v2_QA7_sensitivity.csv`.
- Abstract states inclusion was not second-screened.
- Headline counts unchanged. Open blockers: `audit/SCORE_IMPROVEMENT_ACTIONS_2026-11-03.md` (C1-C5).

---

## [v1.6.21] - 2026-09-20 (IEEE Reference Guide / TLT refs)

- Aligned `references.bib` with IEEE Reference Guide (required by TLT Author Resources): braced model acronyms in titles; abbreviated conference names (`Proc.`/`Int.`/`Conf.`); `Inf. Process. Manag.`; KT069 `Art. no. 10`; Acknowledgment cites `Cursor_AI_2026`.
- Regenerated 14-page full + anonymous + title-named PDFs.
- Audit: `audit/REFERENCE_IEEE_STYLE_2026-09-20.md`.

---

## [v1.6.20] - 2026-09-16 (title-named PDF deliverables)

- Submission PDFs renamed to the article title:
  - full: `Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings - A Critical Survey.pdf`
  - anonymous: `… - A Critical Survey - Anonymous.pdf`
- Upload list updated; LaTeX build names (`manuscript_TLT_FORMATTED_v1.3.pdf`, `main_tlt_anonymous.pdf`) retained as compile outputs.

---

## [v1.6.19] - 2026-09-16 (polish sync)

- Abstract + Contribution 1: DyGKT REPRODUCED framed as one model / one dataset / one seed (aligned with §reliability / Contribution 4).
- Display name unified to R$^2$GCurL in manuscript tables and prose.
- Supplementary Table S-PRISMA-5: upload-facing `supplementary/Table_S-PRISMA-5.csv`; manuscript cites that filename.

---

## [v1.6.18] - 2026-09-15 (final technical fix gate)

- Kappa: invariant all-NO fields → κ NA; macro over defined fields only (NguyenKT 0.97; DaoMT 0.96).
- DyGKT ECE: CASE A REPRODUCED kept; manifest + bins CSV; single-run / not corpus calibration.
- QA tiers: add LIMITED; 0 papers in LIMITED.
- Calibration wording: unverified / calibration-unknown (not “uncalibrated corpus”).
- Fig. 2 footer; PRISMA-5 verification table; STSKT naming; AI disclosure; 5 Index Terms.
- Refs [6]/[45] verified KEEP. Gate: `audit/CURSOR_FINAL_SUBMISSION_GATE.md`.

---

## [v1.6.17] - 2026-09-15 (bibliography metadata sync)

- `references.bib`: KT079 pages `136--153`; KT029 ACM pages `78:1--78:24`; Xu_GbKT DOI `10.5281/zenodo.21443288`; Liu_pyKT pages `18542--18555`.
- Rebuilt `manuscript_TLT_FORMATTED_v1.3.pdf` and `main_tlt_anonymous.pdf` (14 pp); synced titled PDF copy.
- Adjudication: `audit/REFERENCE_ADJUDICATION_2026-09-15.md` (KT033 print TKDE kept).

---

## [v1.6.16] - 2026-09-15 (abstract alignment)

- Abstract: keep manuscript ECE $0/37$; name the DyGKT/ASSIST17 \texttt{REPRODUCED} overlay; frame three tutoring jobs vs prior TLT KT maps.

---

## [v1.6.15] - 2026-09-15 (Shen niche + Survey-scope framing)

- Intro / Table II / cover letter: explicit “why after Shen” (three tutoring jobs Shen does not code); dual-bar fit sharpened.
- Survey and Tutorial scope: classroom / tutor-log outcomes stated as out of article-type scope; LT deliverable = GO/NO-GO checklist.
- ECE row in comparison table mentions manuscript $0/37$ + one \texttt{REPRODUCED} overlay.
- Screening/full-text pair files still absent (no fabricated second-screener labels).

---

## [v1.6.14] - 2026-09-15 (Path A REPRODUCED ECE overlay)

- §VI calibration: manuscript-reported ECE remains **0/37**; added survey-computed DyGKT/ASSIST17 overlay (equal-width $M=10$: ECE **0.0361**, Brier **0.1770**, test AUC **0.8025**, $n=94156$, `REPRODUCED`).
- T3 / A2 / threats / Contribution 4 / cover letter: overlay does **not** flip corpus NO-GO or the $0/37$ reporting claim.
- Supplementary: Path A table + `supplementary_reproduced_ece_DyGKT.csv`; run log under `09_benchmark/path_a_ece/`.

---

## [v1.6.13] - 2026-09-14 (DaoMT independent full 20)

- DaoMT completed REST 10; merged FULL20 AS_SUBMITTED. Independent κ **157/160**, mean **0.97** (same 3 diffs as subset; gold = A).
- §II / threats / cover letter: independent 20-paper κ alongside locator-assisted NguyenKT 158/160 (not pooled).
- Record: `KAPPA_A_vs_DaoMT_FULL20_2026-09-14.md`.

---

## [v1.6.12] - 2026-09-14 (DaoMT independent subset κ)

- §II / threats / cover letter: separate 10-paper `DaoMT` κ (77/80; mean 0.95; no locator), not pooled with locator-assisted NguyenKT 158/160.
- Adjudication gold = A on KT047 family, KT070 provenance, KT068 encoder.
- Supplementary §7 updated. Frozen: `..._DaoMT_AS_SUBMITTED.csv`.

---

## [v1.6.11] - 2026-09-13 (GO/NO-GO tutoring checklist)

- §VII: three-decision GO/NO-GO (T1 new KC, T2 skill-map graph, T3 $P(r=1)$) as agenda inference from locked coding; Recs 1--5 mapped to those verdicts.
- Conclusion provenance $19/8$ → locked $18/9/9$.
- §II opening matches locator-assisted coding-sample $\kappa$ (screening/full-text package still not claimed).
- No new ECE, classroom, or independent-blind $\kappa$ numbers.

---

## [v1.6.10] - 2026-09-13 (pair table + PEBG inventory)

- Added `supplementary/inter_rater_coding.csv` (160 rows; A vs B as submitted). Supplementary §7 matches §II κ.
- Inventory PEBG encoder `GCN` → `NONE` (matches `graph_taxonomy.csv`).

---

## [v1.6.9] - 2026-09-13 (coding-sample κ in §II)

- §II / threats / cover letter report pre-adjudication $158/160$ and mean field-wise $\kappa=0.98$ (family $0.92$, provenance $0.93$).
- Source: A vs `..._v1.3_AS_SUBMITTED.csv`. B used a locator pack; text says this is not a fully independent blind $\kappa$.
- Record: `08_quality_reliability/KAPPA_A_vs_B_SUBMITTED_2026-09-13.md`.

---

## [v1.6.8] - 2026-09-13 (KT047 exclusive family = multiview)

- KT047 DC-SSL exclusive `ssl_family` GRAPH_CONTRASTIVE → **MULTIVIEW_CONTRASTIVE** (PDF §3.3 two DHGN views; same dual-view rule as KT011).
- Family counts: Multiview \(4\to5\), Graph contrast \(3\to2\). Still 4 locked tokens. \(N_S=9\) unchanged.
- `KT047_CODING_v1.0.md` not overwritten (listed GRAPH first). Record: `audit/SSL_FAMILY_LOCKED_ALIGNMENT.md`.

---

## [v1.6.7] - 2026-09-13 (PDF-strict: Coda provenance, HKT encoder)

- KT070 Coda `graph_provenance` MODEL_DEFINED_FIXED → **DYNAMIC_LEARNED** (learnable code-graph \(A_u\)).
- KT068 HKT `gnn_encoder` HETEROGENEOUS_GNN → **GNN_GENERIC** (attention on KHT/KAG; PDF never names a heterogeneous GNN).
- Provenance display \(19/9/8 \to 18/9/9\). Encoder display GCN/generic \(11\to12\), heterogeneous \(8\to7\).
- Evidence: `08_quality_reliability/ADJUDICATION_FIVE_CELLS_PDF_2026-09-13.md`. Counts: `audit/LOCKED_COUNTS_v1.6.md`.
- Not written into §II as \(\kappa\).

---

## [v1.6.6] - 2026-09-13 (KT076 venue matches deposited PDF)

- KT076 `venue_year` KBS 2025 → **ICIC 2025** on live taxonomy, sparse-audit, inventory, and coding-matrix CSVs.
- Matches title-page / bib: Di Zhang et al., ICIC 2025, Springer CCIS pp. 137–147, DOI `10.1007/978-981-96-9986-5_12`.
- Chen et al. KBS 2025 (`10.1016/j.knosys.2025.113400`) is a different article; v1.0 expansion coding is left in place. Record: `07_coding/expansion/KT076/KT076_IDENTITY_CORRECTION_v1.1.md`.
- `supplementary_prisma_exclusions.csv` `REC_0035` note now states that Chen KBS is not the deposited Zhang ICIC paper.

---

## [v1.6.5] - 2026-09-13 (shorter title)

- Official title shortened to *Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Critical Survey*.
- Dropped the tail “of Evaluation Gaps and Trustworthy Learning Technologies” (already in the abstract and keywords). Running header unchanged.

---

## [v1.6.4] - 2026-09-13 (PDF-strict recode of five mismatched cells)

Primary PDFs re-read; five locked-A cells did not match the executed protocol. CSVs updated; manuscript counts follow those CSVs. Record: `08_quality_reliability/ADJUDICATION_FIVE_DIFFS_PDF_2026-09-13.md` and `audit/LOCKED_COUNTS_v1.5.md`.

- KT026 PEBG: `item_cold_start` YES → NO (question-level sparsity, no unseen-item hold-out).
- KT031 KSG-AKT: `gnn_encoder` GCN → OTHER (Metapath2Vec + convolutional embedding; GCN is the GIKT baseline).
- KT044 SINKT: `gnn_encoder` GCN → GAT (three GAT layers).
- KT044 SINKT: `strict_kc_cold_start` YES → NO; `item_cold_start` stays YES (§5.5 is a 1/4-question hold-out).
- KT076 KGNN-KT: `item_cold_start` YES → NO (7:2:1 + difficulty bins; no new-item hold-out).

Locked counts now: strict KC YES $0/37$; item CS YES $1/37$ (SINKT); encoder display GCN/generic $11$, Other $6$, GAT $4$. This is not human–human $\kappa$.
- Agenda A1: $37/37$ do not isolate a zero-exposure KC split (the leftover $36/37$ line is removed). Journal text no longer says “PDF-strict recode.”
- §II QA7 overlay: generic split $34 \to 35$ so $35+1+1+0=37$ matches `H2_qa7_two_variables.csv`.

---

## [v1.6.3] - 2026-09-13 (score-lift steps 1–3)

- Cover letter: complementary niche vs Shen (five coded differences); honest statement that \(\kappa\) is not yet computed.
- Frozen 20-paper IRR sample + empty coder-B sheet: `08_quality_reliability/inter_rater_coding_sample_v1.0.csv`. Coder-A locked values in a separate file. Instructions: `CODER_B_INSTRUCTIONS.md`.
- §II ICR: points to that sample; still no \(\kappa\).
- Plan: `08_quality_reliability/TLT_SCORE_LIFT_STEPS.md`. Step 4 is human coder B.

---

## [v1.6.2] - 2026-09-13 (display PDF filename)

- Display PDF renamed to match the official title: `Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings - A Critical Survey of Evaluation Gaps and Trustworthy Learning Technologies.pdf`.
- Removed the old *Systematic Survey and Research Agenda* filename to avoid opening a stale copy.

---

## [v1.6.1] - 2026-09-13 (title + package sync)

- Official title now: *Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Critical Survey of Evaluation Gaps and Trustworthy Learning Technologies*.
- Cover letters and TLT PDF deliverables regenerated from `manuscript_TLT_FORMATTED_v1.3.tex`.
- Locked counts unchanged (\(N_S=9\), \(N_{G\cap S}=8\)).

---

## [v1.6.0] - 2026-09-13 (TLT major revision — critical survey)

- Title later applied in v1.6.1. Proposed sharper title was first recorded in `TLT_major_revision_report.md`.
- Abstract rewritten as a TLT critical-survey abstract (ITS/EDM problem, PRISMA-informed method, locked counts, deployment constraints). Index Terms expanded to 8, alphabetical.
- PRISMA wording: “PRISMA 2020-informed” / reporting structure. No “strict PRISMA 2020-compliant” claim. No invented \(\kappa\).
- New §II inter-coder subsection: protocol targets stated; reliability package not completed.
- Table II: added learning-technology-use row; complementary (not corrective) vs Shen / pyKT / Xu.
- Five TLT contributions; new §VII design recommendations; Table VI five-column decision table (6 rows).
- Agenda split: Group A corpus-derived first; Group B forward-looking with learning-technology rationale.
- Threats: six groups; supplementary mitigation sentence (artifacts exist).
- AI disclosure: Cursor only (actual tool). ChatGPT / Google Antigravity **not** added.
- Locked counts unchanged: \(N_S=9\), \(N_{G\cap S}=8\). Requested \(N_S=14\) rejected (H1 S-criterion).
- Deliverables: `main_tlt_full.tex`, `main_tlt_anonymous.tex`, `TLT_Supplementary_Evidence_Tables.md`.

---

## [v1.5.10] - 2026-09-13 (transparency D)

- Kappa package **not** completed: no pair-level `inter_rater_*.csv`, no 20-paper double-code sample, no human coder-B IDs.
- Do not use numbers from `08_quality_reliability/INTER_RATER_RELIABILITY_REPORT_v1.0.md` (no pair table; \(N=42\)).
- §IX.A: dropped the unsupported “20% second-coder” clause; protocol targets stated; no \(\kappa\) reported.
- Record: `audit/D_KAPPA_PACKAGE_2026-09-13.md`.

---

## [v1.5.9] - 2026-09-13 (format B)

- Tables I, V, and VI: no `\resizebox`. Footnotesize + column shrink; Table V protocol display labels map to locked tokens in the caption.
- Provenance and encoder charts combined as one `figure*` pair (height capped). Taxonomy width $0.78$. No “text page contains only floats” warning.
- PDF remains 13 pages (content from C, not a leftover float page). Cover letter 13-page line is still correct.

---

## [v1.5.8] - 2026-09-13 (dual-bar C)

- Abstract: tutoring-design constraints from $36/37$ missing zero-exposure KC splits and $0/37$ ECE (no new counts).
- §I.C: Shen is the broad TLT KT survey; this paper is the sparse-KC tutoring-condition reading. No “first” claim.
- Table VI: each row tagged with a TLT scope topic; unproven column unchanged.
- §VII.D: half-column ITS decision check (new KC / log graph / short history / $P(r=1)$).

---

## [v1.5.7] - 2026-09-13 (package A)

- Cover letter: 13 pages; IEEE TLT Author Portal (not ScholarOne); format compared to `New_IEEEtran_how-to.pdf`. `TLT-instructions-only.pdf` was not in the Selector packages on disk.
- Upload list: `audit/AUTHOR_PORTAL_UPLOAD_LIST_2026-09-13.md`. Compare record: `audit/FORMAT_COMPARE_HOWTO_2026-09-13.md`.
- No automatic upload.

---

## [v1.5.6] - 2026-09-13 (IEEE how-to residual)

- Index Terms reordered alphabetically: educational data mining; graph neural networks; intelligent tutoring systems; Knowledge tracing; self-supervised learning.
- Fig. PRISMA, provenance, and encoder: `[h]` → `[!t]`. Compiled PDF is 13 pages (was 12) because those figures now float to column tops; still under the 18-page Survey and Tutorial cap. No `h` float warning.
- Acknowledgment names the Cursor AI coding assistant and cites `Cursor_AI_2026` (IEEE AI-text citation). Author sign-off of the prior unnamed LLM sentence is in `audit/AUTHOR_SIGNOFF_2026-09-13.md`.

---

## [v1.5.5] - 2026-09-13 (author sign-off)

- Author sign-off: đồng ý SSL (\(N_S=9\)) and đồng ý AI Acknowledgment. Record: `audit/AUTHOR_SIGNOFF_2026-09-13.md`.
- ScholarOne file list: `audit/SCHOLARONE_UPLOAD_LIST_2026-09-13.md`. Do not upload `audit/` or the 14-row `supplementary_coding_matrix.csv`.
- Added `supplementary/supplementary_ssl_taxonomy_Ns9.csv`.

---

## [v1.5.4] - 2026-09-13 (residual review items)

- SSL families use four exclusive locked §14 tokens (not seven display aliases). PEBG prints `GRAPH_RECONSTRUCTION`. Map: `audit/SSL_FAMILY_LOCKED_ALIGNMENT.md`.
- H2 overlay: 32 generic / 1 HHSKT interaction-drop / 2 item CS / 1 strict KC. Claim tokens from codebook §16. Unnumbered summary in §II.D (Table III remains the graph taxonomy).
- Table II: no `\resizebox`.
- H6 gate updated to the RQ4 QA7 rationale (not “generic-sparsity YES”).
- Methods states the §22.1 NA option is permitted by the protocol and unused here.
- HIGH list wording: reporting-adequacy partition, not a contribution ranking.

---

## [v1.5.3] - 2026-09-13 (QA score naming)

- QA totals are named review-specific methodological evidence quality / evidence-quality score for the present review, not overall scientific quality.
- Methods: QA7 scores how informative the evaluation design is for RQ4.

---

## [v1.5.2] - 2026-09-13 (QA7 RQ4 lens)

- H2 KEEP_CURRENT: QA7 applies to 37/37 as RQ4 evidence adequacy, not as an author sparsity-claim test.
- Manuscript §II.D and §VI state that applicability follows the survey lens; `evaluation_support_regime` and `sparsity_claim` are separate (`tables/H2_qa7_two_variables.csv`).
- No `_LOCKED` edit; scores unchanged.

---

## [v1.5.1] - 2026-09-13 (review polish)

- §IV: five Graph-KT papers satisfy G-criterion but not S-criterion (no draft-internal “previously listed”).
- Xu et al. JEDM 2026: volume 18, number 2 (official issue page). No DOI added.
- Tables III–IV: no `\resizebox`; Table III split into two 18-row parts at `\footnotesize`. GKT provenance display is Model-defined (19/9/8).
- `graph_taxonomy.csv` / supplementary inventory: `KT004_Dense` is `DENSE_CONCEPT_GRAPH`, `directed=NO`; Transition stays `SEQUENTIAL_TRANSITION`.

---

## [v1.5.0] - 2026-09-13 (H1–H6 targeted TLT fix)

### H1
- \(N_S\) 14→9 and \(N_{G\cap S}\) 13→8 after S-criterion re-audit. SINKT, Coda, KGNN-KT, R²GCurL, STSKT stay Graph-KT only.

### H2
- QA7 remains applicable for 37/37 (`generic_data_sparsity=YES`). LIMITED tier kept at count 0.

### H3
- Table II adds Liu et al. TKDE 2025 and Xu et al. JEDM 2026. No “first survey” claim.

### H4
- Table III: one GKT row (multiple variants). PEBG encoder is none/PNN. GCN/generic 13; NONE 3.

### H5
- Treatment symbol \(W\) (not \(A\), which is adjacency); hyperbolic wording softened; two prior-survey bib entries.

### H6
- Five index terms. AI disclosure covers protocol-grounded audits and revision. Conclusion lists three non-GNN Graph-KT papers (PDKT-C, CMKT, PEBG). Gate: `audit/H6_FINAL_TLT_GATE.md`.

---

## [v1.4.12] - 2026-09-13 (cite ↔ PDF identity check)

### Checked
- All 44 in-text cite keys match a bib entry and the deposited PDF of that paper (title + authors).
- `KT076` is an image-only scan; title-page image matches KGNN-KT (Di Zhang et al., ICIC 2025).
- Log: `audit/CITE_PDF_IDENTITY_2026-09-13.md`.

---

## [v1.4.11] - 2026-09-13 (uncited PDFs dropped from the catalog)

### Changed
- Uncited deposits are no longer listed in `14_references/README.md` or `audit/PDF_BIB_INVENTORY_2026-09-13.csv`.
- Those PDFs stay in `14_references/`. They were never BibTeX entries.

---

## [v1.4.10] - 2026-09-13 (DGMN PDF identified and renamed)

### Changed
- The 11-page file stored as `Model Generalization - A Sharpness Aware Optimization Perspective.pdf` is the DGMN paper (Abdelrahman & Wang). Renamed to `Deep Graph Memory Networks for Forgetting-Robust Knowledge Tracing.pdf`.
- `KT033_DGMN_2023` now has a `file` field. Cited deposit is **44/44**.
- The 4-page SAM/ASAM report stays as `Model Generalization - A Sharpness Aware Optimization Perspective.pdf` and remains uncited.

---

## [v1.4.9] - 2026-09-13 (reference list synced to PDF filenames)

### Changed
- Each deposited cited work in `references.bib` now has `file = {14_references/<title>.pdf}`. IEEEtran does not print this field.
- `KT033_DGMN_2023` stays in the bibliography but has **no** `file` field (IEEE PDF still missing).
- Inventory: `audit/PDF_BIB_INVENTORY_2026-09-13.csv` and `14_references/README.md`.
- Audit CSVs: DKVMN is deposited; DGMN is `MISSING_CORRECT_PDF`; Piech author is Leonidas Guibas.
- Two extra PDFs remain uncited and were not added to the manuscript bibliography.

---

## [v1.4.8] - 2026-09-13 (bib synced to deposited PDFs)

### Changed to match title pages
- JKT authors: Yifu Tang, Taige Zhao, Yunliang Chen, Ziyu Guan.
- TSKT first author: Huali Yang (not Hua).
- Bi-CLKT: Qi Lei, Ajmal Mian.
- PDKT-C: Vincent W. Zheng.
- GKT title: singular *Graph Neural Network*.
- AKT: Andrew S. Lan.

### Not changed (file is not a usable title page)
- DGMN deposit is a different PDF (SAM/ASAM student report). Bib stays Abdelrahman & Wang.
- KGNN-KT deposit has no extractable text; bib stays Springer/Crossref.

---

## [v1.4.7] - 2026-09-13 (live Crossref author/title/DOI check)

### Fixed (publisher record)
- `KT026`: DOI `.../ijcai.2020/216` pointed at a different paper; official PEBG DOI is `.../219`.
- `KT035`: DOI `eswa.2023.119334` 404; official is `eswa.2022.119334`.
- `KT044`: title aligned to ACM *SINKT: ... Model with Large Language Model*.
- `KT053`: authors were Lixin Wang / Di Wu; official Springer list is Mengdan Wang et al.; pages 268--279.
- `KT063`: added Shengze Hu, Jing Geng, Qiang Zhu; volume 310.

### Checked
- 44/44 papers exist. 41 have resolving DOIs. Piech, Pandey, pyKT have proceedings URLs only.
- Full log: `audit/REFERENCE_FULL_CHECK_2026-09-13.md`.

---

## [v1.4.6] - 2026-09-13 (IEEE Reference Guide / TLT bib)

### Changed
- `IEEEtran.bst` 1.14 does not print `doi`; added `url = {https://doi.org/...}` so locators appear as `[Online]. Available:`.
- Journal titles abbreviated to IEEE style (`IEEE Trans. Learn. Technol.`, `Knowl.-Based Syst.`, etc.).
- `IEEEtranBSTCTL` + `\\bstctlcite`: list up to six authors, then first author *et al.* (IEEE Reference Guide).
- No-DOI official URLs: Piech (NeurIPS 2015 proceedings), Pandey (EDM 2019 proceedings).
- `KT077_R2GCurL_2026`: Crossref issue 6.
- Synced `12_manuscript/references.bib` to the TLT file.

---

## [v1.4.5] - 2026-09-13 (bibliography metadata)

### Changed
- `KT047_DCSSL_2023`: Crossref authors/title/volume (Tangjie Wu and Qiang Ling; ESWA 225:120212).
- `KT070_Coda_2025`: Crossref author list (Yuze Zhao, Hao Wang, Linan Yue, Fangzhou Yao, Zheng Zhang).
- `KT076_KGNNKT_2025`: Springer DOI `10.1007/978-981-96-9986-5_12`, pages 137--147.
- `Piech_DKT_2015`: Mehran Sahami (not Amit Sahai); NeurIPS volume 28.
- Audit rows updated in `supplementary/supplementary_doi_audit.csv` and `audit/REFERENCE_METADATA_AUDIT.csv`.

---

## [v1.4.4] - 2026-09-13 (Cách 1: contributions, tone, ITS paragraph)

### Changed
- Unified four contributions in the introduction and conclusion; conclusion uses readable labels (no codebook dump).
- Softened leftover rhetoric: abstract “degraded representation quality”, intro “severe bottleneck”, conclusion “pervasive methodological vulnerability”.
- After `tab:its_implications`, added an ITS operations paragraph from coded papers only (SINKT; PEBG/KT026 and KGNN-KT; PDKT-C and CMKT; ECE $0/37$). No classroom study and no AUC ranking.
- Conclusion states the survey standardizes evaluation for tutoring decisions, not a model league table.
- Locked counts and agenda pillars unchanged.

---

## [v1.4.3] - 2026-09-13 (copy-edit pass before upload)

### Changed
- Intro heading is now sparse-interaction motivation, not a measured “representation collapse” event.
- §5 leakage wording no longer implies a counted full-dataset construction rate; transductive “random guessing” is labeled structural, not measured.
- Section 8 title is “Research Agenda”; removed `LIT_SYNTHESIZED` / `AGENDA_INFERENCE` from TLT prose.
- Softened “dramatically improved” and “all 37 studies are evaluated on ASSISTments/…”.
- Comparison table: unbolded this-survey column; last row is QA6 author-artifact coding, not an open-science audit.
- SSL definition no longer treats masked auto-encoding as typical; PEBG stays bipartite reconstruction.
- Screening/coding story unified: primary screener + consensus + 20% QA check; protocol 25%/κ targets stated as not completed.
- “Meta-analysis” → count distributions. Complexity formulas removed (textbook, not coded). ECE stated once in §6.
- Graph/SSL tables use readable labels. DKVMN cited (`Zhang_DKVMN_2017`). Poincaré/Möbius removed from the notation table (kept only in open Pillar 2).
- Cover letters at `12_manuscript/COVER_LETTER.tex` and `12_manuscript/TLT/COVER_LETTER.tex` now address TLT, not TKDE.
- Added IEEE AI-text Acknowledgment. Format note: `audit/TLT_FORMAT_CHECK_v1.4.3.md` (`TLT-instructions-only.pdf` is not in the repo).

---

## [v1.4.2] - 2026-09-13 (claim hygiene, QA7, ITS table, captions)

### Changed
- Removed unreproduced SSL collapse, GKT/CL4KT cold-start degradation, HHSKT-as-inductive, and $P(r=1)>0.90$ as corpus facts.
- Comparison-table leakage cell is now “split/provenance coded; no locked leakage rate”.
- QA7 is applicable for all 37 papers (generic sparsity YES); denominator is 16, not NA/14.
- Agenda: pillars 3–4 from the corpus; 2/5/6 open directions; pillar 1 corpus-motivated only.
- Replaced five implication subsections with one ITS decision table (`tab:its_implications`).
- Captions cite the locked survey protocol instead of CSV filenames.

---

## [v1.4.1] - 2026-09-13 (figure redesign)

### Changed
- Redrew the four TLT figures as aligned three-column / two-row plates (no star mindmap, no drop shadows).
- Kept locked CSV counts: provenance 19/9/8, encoder 14/8/5/3/2/2/2, SSL $N_S=14$ and 12 families.
- Removed the old unbalanced percentages (GCN 40.5\%, hyperbolic 2.4\%, four-family SSL).

---

## [v1.4.0] - 2026-09-13 (Cách 1: lock counts to four CSVs)

### Changed
- Every corpus/taxonomy count in `manuscript_TLT_FORMATTED_v1.3.tex` and four figure PDFs now follows `tables/graph_taxonomy.csv`, `ssl_taxonomy.csv`, `sparse_coldstart_audit.csv`, and `corpus_counts.csv`.
- Graph provenance is the codebook triple only: `MODEL_DEFINED_FIXED` 19, `EXTERNAL_FIXED` 9, `DYNAMIC_LEARNED` 8 ($N_G=36$). Removed Expert/Log/Dynamic/LLM four-channel percentages.
- Encoder counts match the CSV, including `NONE` for PDKT-C and CMKT. Removed hyperbolic/GAE bars that are not in the CSV.
- SSL table lists all 14 rows (added KT044, KT070, KT076, KT077, KT079). Families are the 12 `ssl_family` codes; PEBG is bipartite pretraining, not masked concept prediction.
- QA items use codebook names (QA4 baseline, QA5 statistics, QA6 author artifacts). Tiers: 11 HIGH / 26 MODERATE after QA6 cap; extra IDs KT078 and KT080–KT083 excluded.
- Sparse caption: generic sparsity 37/37; strict KC cold-start 1/37 (SINKT); item cold-start 3/37 (KT026, KT044, KT076). Removed 48.4% leakage and 94.6%/5.4% splits that are not in the CSVs.
- Regenerated `fig_taxonomy_2d.pdf`, `fig_ssl_framework.pdf`, `fig_meta_analysis_charts.pdf`, `fig_graph_construction_pipeline.pdf`.
- Audit note: `audit/LOCKED_COUNTS_v1.4.md`.

---

## [v1.3.2] - 2026-09-13 (reference correction)

### Changed
- Withdrew fabricated `Wang_GraphKT_2024` (DOI `10.1109/TLT.2024.3456789` is not an IEEE record).
- Replaced it with Crossref-verified `Shen_KTSurvey_2024`: Shen, Liu, Huang, Zheng, Yin, Wang, and Chen, *A Survey of Knowledge Tracing: Models, Variants, and Applications*, IEEE TLT, vol. 17, pp. 1858--1879, 2024, doi: 10.1109/TLT.2024.3383325.
- Updated pyKT bib title/author spelling to the NeurIPS 2022 proceedings record (Shuyan Huang; full benchmark title).
- Deposited author/proceedings PDFs for Abdelrahman 2023, pyKT 2022, and Shen 2024 in `14_references/`.

---

## [v1.3.1] - 2026-09-13 (folder cleanup)

### Removed
- LaTeX build artifacts (`.aux`, `.log`, `.out`, `.bbl`, `.blg`)
- Temporary `extracted.txt`
- Superseded draft trees (`WORKING`, `TEMPLATE`, `STRUCTURE`, `FINAL_CANDIDATE`, and the duplicate `Graph_Based_and_Self_Supervised_*` copy)

### Kept
- Current source `manuscript_TLT_FORMATTED_v1.3.tex`
- Title-named PDF
- `IEEEtran.cls`, `references.bib`, figure sources/PDFs, `tables/`, `supplementary/`, `audit/`

---

## [v1.0.0] - 2026-09-12 (Task A15 Final Release)

### Added
- Created complete manuscript LaTeX candidate: `manuscript_TLT_FINAL_CANDIDATE.tex` and compiled PDF `manuscript_TLT_FINAL_CANDIDATE.pdf` (11 double-column pages).
- Created supplementary artifacts package in `supplementary/`:
  - `table_prisma_flow.csv`
  - `table_graph_kt_taxonomy.csv`
  - `table_ssl_kt_taxonomy.csv`
  - `table_quality_reliability.csv`
  - `table_supplementary_extended.csv`
  - `README.md`
- Created audit compliance artifacts in `audit/`:
  - `MANUSCRIPT_TLT_FINAL_COMPLIANCE.md`
  - `MANUSCRIPT_TLT_REMAINING_BLOCKERS.md`

### Changed
- Standardized section structure into 10 explicit IEEE TLT sections matching target journal requirements.
- Standardized mathematical formalism including explicit interaction-level cold-start sets $\mathcal{D}_{\text{train}}^{\text{cold}}$, temperature scaling $T > 0$, and backdoor adjustment causal graph.
- Repositioned core narrative to highlight implications for Intelligent Tutoring Systems (ITS), Educational Data Mining (EDM), and adaptive learning platforms.

### Removed
- Removed unverified hardcoded benchmark AUC/ACC comparison table (Task A9 decision `REMOVE`) to ensure 100% methodological traceability without data fabrication.

---

## [v0.1.0] - 2026-09-12 (Initial Migration)
- Migrated content from `04_manuscript/` into IEEE TLT structure (`12_manuscript/TLT/`).
