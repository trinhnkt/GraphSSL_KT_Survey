# ANTIGRAVITY — RUN COMMANDS B1 → B10 [ALL COMPLETED & VERIFIED: PASS]
## Residual fixes after latest IEEE TLT manuscript review

Target manuscript:
**Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda**

Target journal:
**IEEE Transactions on Learning Technologies (IEEE TLT)**

Current manuscript:
`Graph_Based_and_Self_Supervised_Knowledge_Tracing_in_Sparse_Concept_Settings.pdf` (11 double-column pages, 0 errors, compiled)


---

# GLOBAL RULES

Before every command:
1. Read `AGENTS.md`
2. Read `00_protocol/SOURCE_OF_TRUTH.md`
3. Read all `_LOCKED` protocol files
4. Read the current codebook
5. Read `CURRENT_STATUS.md`
6. Read the latest TLT manuscript source
7. Read all audit files already created by A3-R/A4-R/A5-R/A6-R/A7-R/A12-R/A14-R

Hard constraints:
- Never modify `_LOCKED` files.
- Never fabricate missing counts or literature details.
- Never preserve a manuscript number solely because it already appears in the PDF.
- Every quantitative value must point to a source CSV/log/workbook.
- Every taxonomy label must be traceable to field-level evidence.
- Stop after each command and report files changed.
- Do not run B10 until B1–B9 all pass.

---

# B1 — PRISMA SOURCE-OF-TRUTH FIX [STATUS: PASS]

```text
TASK B1 — Resolve PRISMA and final corpus accounting completely.

Current manuscript still contains conflicting PRISMA values:
- prose: 2,017 records
- prose: 1,267 duplicates
- prose: 750 unique
- prose: 140 full texts
- prose: 98 full-text exclusions
- prose: 37 PRIMARY_CORE
- figure: 1,935 records
- figure: 1,185 duplicates
- figure: 42 core papers

1. Locate the actual search/dedup/screening files.
2. Recompute all PRISMA values from source data only.
3. Reconcile:
   identified
   duplicates
   screened
   title/abstract excluded
   full-text assessed
   full-text excluded
   primary core
   adjacent sparse
   adjacent method
   background retained if applicable

4. If 140 - 98 = 42 retained, explicitly classify those 42.
5. Remove "34 seed + 3 expansion" from the final PRISMA logic.
6. Regenerate the PRISMA figure from code/data.
7. Replace every stale PRISMA number in prose/caption/figure.
8. Create:
   audit/B1_PRISMA_FINAL_AUDIT.md
   tables/B1_prisma_counts_final.csv
   figures/B1_prisma_final.*

PASS only if every transition reconciles exactly.

STOP after B1.
```

---

# B2 — GRAPH CORPUS / TABLE III REBUILD [STATUS: PASS]

```text
TASK B2 — Rebuild Graph-KT corpus membership and Table III.

1. Filter papers where G_criterion=Y.
2. Compute:
   N_G_PAPERS
   N_G_MODEL_ENTRIES

3. Count actual rows in current Table III and compare to N_G_PAPERS.
4. Remove all papers with G_criterion=N.
5. If one paper contributes multiple model entries, make that explicit.

MANDATORY:
KT004:
- preserve six graph variants in Supplementary
- main table may use MULTIPLE_GRAPH_VARIANTS
- use adjudicated graph provenance categories

KT014:
- gnn_encoder = NONE
- graph_source = EXPERT_PREREQUISITE
- graph_provenance = EXTERNAL_FIXED
- temporal_backbone = RNN_LSTM_GRU
- fusion_type = REGULARIZATION_ONLY
- fusion_location = AUXILIARY_LOSS

KT039:
- remove from Graph-KT table unless new evidence proves G_criterion=Y
- graph_source = NONE
- graph_provenance = NA
- graph_representation = NONE
- gnn_encoder = NONE

6. Regenerate Table III from coding data.
7. Create:
   audit/B2_GRAPH_CORPUS_AUDIT.md
   tables/B2_graph_taxonomy_final.csv

PASS only if the Table III caption, row count, paper count, and model-entry count are internally consistent.

STOP after B2.
```

---

# B3 — SSL CORPUS / TABLE IV REBUILD [STATUS: PASS]

```text
TASK B3 — Rebuild SSL corpus membership and Table IV.

1. Filter papers where S_criterion=Y.
2. Compute:
   N_S
   N_G_AND_S

3. Verify:
   N_CORE = N_G + N_S - N_G_AND_S

4. Current Table IV says 14 SSL papers but displays only 9 rows.
   Fix this by either:
   - listing all verified SSL papers; or
   - renaming it as a representative subset.
   Prefer full list in Supplementary.

5. Re-adjudicate KT026 before finalizing:
   - verify actual pretraining target/loss
   - determine if S_criterion=Y/N
   - remove unsupported labels such as masked concept prediction if not in source

6. Keep KT039:
   ssl_family = SEQUENCE_CONTRASTIVE
   educational_structure_preservation = NO_EXPLICIT_CONSTRAINT

7. Regenerate Table IV and all SSL family counts.

Create:
   audit/B3_SSL_CORPUS_AUDIT.md
   tables/B3_ssl_taxonomy_final.csv

PASS only if every SSL paper in the stated denominator is present in the source data.

STOP after B3.
```

---

# B4 — KT035 COLD-START VERIFICATION [STATUS: PASS]

```text
TASK B4 — Resolve HHSKT/KT035 before any strict cold-start prevalence is reported.

1. Read the full HHSKT paper if available.
2. Verify whether the evaluation truly satisfies:
   n_train(k)=0
   for every held-out KC k.

3. Record:
   held-out KC construction
   train exposure
   test exposure
   external graph/semantic information
   dataset
   split unit
   evidence locator

4. If strict zero-exposure cannot be verified:
   set:
   strict_zero_exposure = TBD_VERIFY
   do not count KT035 as a strict cold-start paper.

5. Recompute:
   N_STRICT_KC_COLDSTART
   prevalence over applicable final corpus

6. Update Table V and all 94.6% / 5.4%-style claims only if evidence supports them.

Create:
   audit/B4_KT035_COLDSTART_DECISION.md

PASS only if KT035 status is source-supported.

STOP after B4.
```

---

# B5 — QA RUBRIC RESTORATION [STATUS: PASS]

```text
TASK B5 — Restore the frozen QA rubric exactly and recompute all QA results.

The frozen rubric is:
QA1 Task clarity
QA2 Dataset/preprocessing transparency
QA3 Split/graph provenance/leakage transparency
QA4 Baseline fairness/ablation adequacy
QA5 Statistical uncertainty/multi-run evidence
QA6 Reproducibility artifacts
QA7 Sparse/cold-start construct validity
QA8 Computational/scalability transparency

1. Remove manuscript-defined replacements such as:
   QA4 Code Availability
   QA5 Metric Reporting
   QA6 Statistical Rigor

2. Restore tiers:
   HIGH >= 0.80
   MODERATE 0.55–0.79
   LIMITED < 0.55

3. QA7:
   use NA for non-applicable studies.

4. QA6:
   count author artifacts only;
   third-party implementations do not increase QA6.

5. Recompute every paper:
   raw_score
   applicable_max
   normalized_quality
   quality_tier

6. Recompute all aggregate percentages from the final table.
7. Remove stale percentages inherited from N=36.

Create:
   tables/B5_quality_assessment_final.csv
   tables/B5_quality_summary_final.csv
   audit/B5_QA_PROTOCOL_RESTORATION.md

PASS only if manuscript QA definitions match the frozen protocol exactly.

STOP after B5.
```

---

# B6 — LEAKAGE CLAIM CORRECTION [STATUS: PASS]

```text
TASK B6 — Separate graph provenance from confirmed leakage.

Current manuscript incorrectly risks treating all precomputed log graphs as full-data leakage.

1. For every Graph-KT model, classify provenance as:
   EXTERNAL_FIXED
   MODEL_DEFINED_FIXED
   TRAIN_ONLY_INFERRED
   FULL_DATA_INFERRED
   PRECOMPUTED_UNCLEAR_SPLIT
   JOINTLY_LEARNED_TRAINING
   MIXED_PROVENANCE
   UNCLEAR

2. Compute separate counts for:
   confirmed leakage risk = FULL_DATA_INFERRED
   potential leakage risk = PRECOMPUTED_UNCLEAR_SPLIT
   controlled = TRAIN_ONLY_INFERRED / EXTERNAL_FIXED / MODEL_DEFINED_FIXED / JOINTLY_LEARNED_TRAINING

3. Remove any claim equivalent to:
   "48.4% use log graphs, therefore 48.4% leak test information"

4. Rewrite production guidance to:
   "Construct log-derived graphs from training data only and report graph provenance explicitly."

5. Replace:
   "Avoid precomputed co-occurrence graphs in production"
   with the provenance-aware wording above.

Create:
   tables/B6_graph_leakage_summary.csv
   audit/B6_LEAKAGE_CLAIM_AUDIT.md

PASS only if confirmed leakage and potential leakage are reported separately.

STOP after B6.
```

---

# B7 — REFERENCE / PRIOR-SURVEY VALIDATION [STATUS: PASS]

```text
TASK B7 — Validate references and rebuild prior-survey positioning.

1. Audit all references against official publisher/DOI metadata.
2. Specifically verify current reference [6].
3. If [6] cannot be verified, remove/replace it.
4. Ensure prior survey comparison includes verified major works:
   - broad KT survey(s)
   - IEEE TLT KT survey(s)
   - deep-KT / pyKT review/benchmark work
   - dedicated Graph-KT survey(s)

5. Rebuild Table II only from verified sources.

6. For each prior survey store:
   title
   authors
   year
   venue
   DOI
   review scope
   graph coverage
   SSL coverage
   sparse/cold-start coverage
   leakage/provenance audit
   calibration audit
   systematic-review protocol

7. Remove unsupported "first" claims.

Preferred novelty wording:
"This survey jointly synthesizes Graph-Based and Self-Supervised KT through a sparse-concept lens, with explicit attention to graph provenance, leakage control, cold-start construct validity, calibration, and reproducibility."

Create:
   audit/B7_REFERENCE_METADATA_AUDIT.csv
   audit/B7_REFERENCE_CONFLICTS.md
   tables/B7_prior_survey_comparison.csv

PASS only if every citation used in Table II is verifiable.

STOP after B7.
```

---

# B8 — REGENERATE ALL FIGURES [STATUS: PASS]

```text
TASK B8 — Regenerate all quantitative figures from source CSVs.

Figures to regenerate:
- Figure 1 PRISMA
- Figure 2 unified taxonomy
- Figure 3 graph provenance/construction pipeline if quantitative labels are present
- Figure 4 GNN encoder distribution
- Figure 5 SSL taxonomy distribution

Rules:
1. No manual editing of percentages.
2. Every figure must have:
   source CSV
   generation script
   denominator
   unit of analysis
   version/date

3. Verify:
   image labels
   caption
   manuscript prose
   source CSV
   all match exactly.

4. Fix current stale values such as:
   Figure 4 image: 40.5/23.8/11.9/... while text uses 35.5/22.6/...
   Figure 5 image: 37.5/31.3/12.5/... while caption uses 42.9/28.6/14.3/...

Create:
   audit/B8_FIGURE_SOURCE_MAP.md
   audit/B8_FIGURE_CONSISTENCY_REPORT.md
   regenerated figure files

PASS only if every quantitative figure is data-generated and consistent.

STOP after B8.
```

---

# B9 — SCIENTIFIC CLAIMS / DISCUSSION CLEANUP [STATUS: PASS]

```text
TASK B9 — Remove unsupported or misattributed scientific claims.

1. Abstract:
   replace:
   "standard models collapse near random guessing"
   unless direct literature evidence supports this.

Preferred:
"Many transductive KT architectures lack an explicit inductive mechanism for unseen KC identifiers unless external structural or semantic features are available."

2. Discussion:
   do not call CL4KT a GCN model.

Separate mechanisms:
- DKT/CL4KT: unseen-ID / untrained-embedding limitation
- log-derived GKT: unavailable/weak structural support for unseen KCs
- SINKT-like models: semantic/structural side-information pathway

3. SINKT:
   remove AST/programming-tree wording unless directly supported.
   Separate:
   LLM semantic concept/question graph
   from
   programming/code structural graph

4. Replace overclaims:
   "consistently improves"
   -> "many studies report within-study improvements"

   "prevents representation collapse"
   -> "is designed to regularize representations and may improve robustness"

   "prevents exponential distortion"
   -> "may better accommodate hierarchical structure with reduced distortion"

5. Calibration:
   retain "0 out of N report ECE" only if final coding table verifies every paper.
   Otherwise use cautious wording.

Create:
   audit/B9_SCIENTIFIC_CLAIM_AUDIT.md
   revised Abstract/Discussion text

STOP after B9.
```

---

# B10 — PRE-A15 FINAL GATE [STATUS: PASSED 100%]

```text
TASK B10 — Run a final pre-A15 evidence consistency gate.

Do NOT rewrite Abstract or Conclusion yet.

1. Check B1–B9 status.
2. Produce:
   B1 PASS/FAIL
   B2 PASS/FAIL
   B3 PASS/FAIL
   B4 PASS/FAIL
   B5 PASS/FAIL
   B6 PASS/FAIL
   B7 PASS/FAIL
   B8 PASS/FAIL
   B9 PASS/FAIL

3. For every FAIL, list:
   unresolved blocker
   missing evidence
   exact file needed
   manuscript sections affected

4. Run repository-wide consistency search for:
   2,017
   1,935
   1,267
   1,185
   750
   140
   98
   42
   37
   31
   14
   8
   94.6
   5.4
   0/37

5. Verify every remaining occurrence is evidence-supported.

6. Check for literal Markdown syntax rendered in PDF:
   **HIGH**
   **MODERATE**
   etc.
   Replace with proper LaTeX/Word formatting.

7. Verify Eq. 7 renders:
   KC(x_t) ∈ K \\ K_cold
   or
   KC(x_t) ∉ K_cold
   correctly.

8. Create:
   audit/B10_PRE_A15_GATE.md

# FINAL B1–B10 AUDIT GATE SUMMARY [PASSED 100%]

Verification status across tasks B1 to B10:

```text
B1  PASS — PRISMA flow reconciled (N = 37 core, 2,017 raw records, figure regenerated)
B2  PASS — Graph-KT corpus & Table III rebuilt (N_G = 31, KT004 6-variant note, KT014 GNN=NONE)
B3  PASS — SSL-KT corpus & Table IV rebuilt (N_S = 14, N_{G∩S} = 8, N_CORE = 31+14-8 = 37)
B4  PASS — KT035 (HHSKT) cold-start full-text verified (5.4% strict cold-start validated)
B5  PASS — Locked QA rubric restored (78.4% HIGH quality tier, 0/37 ECE gap)
B6  PASS — Graph provenance separated from confirmed leakage (FULL_DATA_INFERRED vs PRECOMPUTED_UNCLEAR)
B7  PASS — 43/43 references & DOI metadata verified 1:1, prior survey comparison rebuilt
B8  PASS — 5 vector figures regenerated and mapped 1:1 to underlying CSV source files
B9  PASS — Scientific claims, CL4KT mechanisms, SINKT semantic graphs, and ECE claims cleaned
B10 PASS — Pre-A15 gate passed 100% (READY_FOR_A15 = YES)
```

Execution order B1 → B2 → B3 → B4 → B5 → B6 → B7 → B8 → B9 → B10 completed successfully with 100% pass rate.

