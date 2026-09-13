# ANTIGRAVITY — EDITOR/REVIEWER FIX PROMPTS G1 → G10
## Target: IEEE Transactions on Learning Technologies (IEEE TLT)

Manuscript:
**Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda**

Latest reviewed PDF:
`Graph_Based_and_Self_Supervised_Knowledge_Tracing_in_Sparse_Concept_Settings(6).pdf`

Target article type:
**Survey and Tutorial**

---

# GLOBAL RULES

Before every task:

1. Read `AGENTS.md`
2. Read `00_protocol/SOURCE_OF_TRUTH.md`
3. Read all `_LOCKED` protocol files
4. Read the latest codebook
5. Read current coding/evidence tables
6. Read the latest active manuscript source
7. Read the latest PDF `(6)`
8. Read prior audit files

Hard constraints:

- Never modify `_LOCKED` files.
- Never invent PRISMA counts, taxonomy assignments, QA scores, ECE prevalence, cold-start counts, p-values, references, or benchmark values.
- Do not infer missing evidence from manuscript prose.
- Every numerical claim must be generated from a source CSV/log/workbook.
- Every taxonomy label must have field-level evidence.
- Every reference must be verifiable from official metadata.
- Stop after each task and report changed files.
- Do not rewrite the final Abstract and Conclusion until G1–G9 all pass.

---

# G1 — REMOVE BUILD CANARY + CLEAN BUILD

```text
TASK G1 — Remove BUILD-CANARY-E2 and lock the active build chain.

1. Remove literal text:
   BUILD-CANARY-E2

2. Clean all build/cache files.
3. Rebuild using the verified active source.
4. Confirm the canary is gone from the PDF.
5. Record:
   active source path
   build command
   output PDF path
   timestamp
   checksum/hash

Create:
audit/G1_BUILD_CLEAN.md

PASS only if:
CANARY_REMOVED = YES
ACTIVE_SOURCE_CONFIRMED = YES
CLEAN_BUILD_CONFIRMED = YES

STOP after G1.
```

---

# G2 — REBUILD PRISMA + FINAL CORPUS FROM REAL LOGS

```text
TASK G2 — Rebuild the PRISMA flow and final corpus accounting.

Current manuscript contains incompatible values:
- prose: 2,017 identified
- prose: 1,267 duplicates
- prose: 750 unique
- prose: 140 full text
- prose: 98 full-text excluded
- prose: 37 PRIMARY_CORE
- figure: 1,935 identified
- figure: 1,185 duplicates
- figure: 42 core
- prose: "34 seed core + 3 PRISMA expansion"

Do not repair these manually.

1. Locate actual:
   search logs
   database exports
   deduplication ledger
   title/abstract screening ledger
   full-text screening ledger
   final corpus-tier file

2. Compute:
   N_IDENTIFIED_CORE_DB
   N_IDENTIFIED_SUPPLEMENTARY
   N_IDENTIFIED_TOTAL
   N_DUPLICATES
   N_SCREENED
   N_TA_EXCLUDED
   N_FULLTEXT
   N_FT_EXCLUDED
   N_PRIMARY_CORE
   N_PRIMARY_ADJACENT_SPARSE
   N_PRIMARY_ADJACENT_METHOD
   N_OTHER_RETAINED

3. Use the locked protocol:
   six core bibliographic databases
   + arXiv/secondary discovery as supplementary
   unless `protocol_deviations.md` explicitly documents another decision.

4. Reconcile every arithmetic transition.

5. If:
   140 - 98 = 42
   classify all 42 retained records explicitly.
   Do not force 42 to equal 37.

6. Remove "seed core + expansion" from final PRISMA accounting.
   Seed status is metadata only.

7. Delete old Figure 1.
8. Regenerate Figure 1 from source data.
9. Update Methods, caption, Abstract, Conclusion only after counts are verified.

Create:
tables/G2_prisma_counts.csv
audit/G2_PRISMA_CORPUS_AUDIT.md
figures/G2_prisma_final.*

PASS only if:
prose == figure == caption == source CSV

STOP after G2.
```

---

# G3 — LOCK GRAPH / SSL CORPUS COUNTS

```text
TASK G3 — Recompute N_CORE, N_G, N_S, and N_G_AND_S from coding data.

1. Use paper-level coding:
   G_criterion
   S_criterion
   PRIMARY_CORE

2. Compute:
   N_CORE
   N_G
   N_S
   N_G_AND_S

3. Verify:
   N_CORE = N_G + N_S - N_G_AND_S

4. Do not retain:
   37
   31
   14
   8
unless regenerated from source coding.

5. Save one source-of-truth file:
   tables/G3_gateway_counts.csv

6. All manuscript references to:
   N_CORE
   N_G
   N_S
   N_G_AND_S
must be generated from this file.

Create:
audit/G3_GATEWAY_CORPUS_AUDIT.md

PASS only if all four counts are mathematically and evidentially consistent.

STOP after G3.
```

---

# G4 — REBUILD TABLE III + ADJUDICATE KT004 / KT014

```text
TASK G4 — Rebuild Graph-KT taxonomy from model-level coding.

1. Filter:
   G_criterion = Y

2. Compute:
   N_G_PAPERS
   N_G_MODEL_ENTRIES

3. Regenerate Table III from coding data.

Mandatory corrections:

KT004 / GKT
- main table:
  graph construction = MULTIPLE_GRAPH_VARIANTS
  graph provenance = MULTIPLE
- supplementary model entries:
  Dense
  Transition
  DKT Graph
  PAM
  MHA
  VAE
- preserve adjudicated provenance/source values.

KT014 / PDKT-C
- graph_source = EXPERT_PREREQUISITE
- graph_provenance = EXTERNAL_FIXED
- graph_representation = KC_KC
- gnn_encoder = NONE
- temporal_backbone = RNN_LSTM_GRU
- fusion_type = REGULARIZATION_ONLY
- fusion_location = AUXILIARY_LOSS
- remove "Relational Paths" from the GNN Encoder column.

KT039 / CL4KT
- do not include in Graph-KT table unless new evidence proves G_criterion=Y
- graph_source = NONE
- graph_provenance = NA
- graph_representation = NONE
- gnn_encoder = NONE

4. Caption must distinguish:
   paper count
   model-entry count

5. Move exhaustive model-entry inventory to Supplementary if needed.

Create:
tables/G4_graph_papers.csv
tables/G4_graph_model_entries.csv
audit/G4_GRAPH_TAXONOMY_AUDIT.md

PASS only if Table III is generated from `G_criterion`.

STOP after G4.
```

---

# G5 — REBUILD SSL TAXONOMY + ADJUDICATE KT026

```text
TASK G5 — Rebuild the SSL corpus and Table IV.

1. Filter:
   S_criterion = Y

2. Recompute:
   N_S
   N_G_AND_S

3. Re-adjudicate KT026 from the full paper.

For KT026 verify:
- actual pretraining objective
- self-generated target?
- loss function
- graph role
- two-stage vs joint training
- whether it satisfies the frozen S_criterion

4. Do not retain unsupported labels:
   MASKED_PRETRAINING
   masked concept prediction
   masked cross-entropy
unless explicitly supported by the paper.

5. Keep KT039 / CL4KT as:
   ssl_family = SEQUENCE_CONTRASTIVE
   educational_structure_preservation = NO_EXPLICIT_CONSTRAINT

6. Regenerate Table IV.

7. If main paper shows only representative rows:
   caption must say "Representative subset".
   Complete SSL list goes to Supplementary.

Create:
tables/G5_ssl_papers.csv
tables/G5_ssl_taxonomy.csv
audit/G5_KT026_SSL_ADJUDICATION.md

PASS only if stated NS matches source rows.

STOP after G5.
```

---

# G6 — REBUILD SPARSE / COLD-START EVIDENCE + VERIFY KT035

```text
TASK G6 — Rebuild sparse-concept/cold-start classification from the locked ontology.

Use:
LOW_FREQUENCY_KC
LONG_TAIL_KC
STRICT_KC_COLD_START
LOW_DEGREE_GRAPH_NODE
ITEM_COLD_START
LEARNER_COLD_START
SHORT_HISTORY
GENERIC_DATA_SPARSITY
SPARSE_ATTENTION_ARCHITECTURE
MULTIPLE
NO_EXPLICIT_FOCUS
UNCLEAR

Do not collapse the literature into only:
generic sparsity vs strict cold-start.

KT035 / HHSKT:
1. Read full text.
2. Strict zero-exposure requires:
   n_train(k) = 0
   for every held-out KC.

3. Record:
   held-out KC definition
   train exposure
   test exposure
   dataset
   side information
   graph information
   evidence locator

4. If not verified:
   STRICT_KC_COLD_START = TBD_VERIFY
   and do not count KT035 as strict cold-start.

5. Independently verify KT044 / SINKT.

6. Recompute all sparse/cold-start counts and percentages.

7. Remove/recompute:
   94.6%
   5.4%
   35/37
   2/37
unless source data support them.

8. Regenerate Table V.

Create:
tables/G6_sparse_coldstart.csv
audit/G6_SPARSE_COLDSTART_AUDIT.md

PASS only if every strict-cold-start paper has direct evidence.

STOP after G6.
```

---

# G7 — RESTORE LOCKED QA RUBRIC + IRR EVIDENCE

```text
TASK G7 — Restore the frozen QA rubric and remove unsupported coder claims.

Frozen rubric:

QA1 Task clarity
QA2 Dataset/preprocessing transparency
QA3 Split/graph provenance/leakage transparency
QA4 Baseline fairness/ablation adequacy
QA5 Statistical uncertainty/multi-run evidence
QA6 Reproducibility artifacts
QA7 Sparse/cold-start construct validity
QA8 Computational/scalability transparency

Quality tiers:
HIGH >= 0.80
MODERATE 0.55–0.79
LIMITED < 0.55

Rules:
- QA7 = NA when not applicable.
- QA6 counts author-supported artifacts only.
- third-party code does not increase QA6.

1. Delete the current manuscript QA definitions:
   QA4 Code Availability
   QA5 Metric Reporting
   QA6 Statistical Rigor
   etc.

2. Recompute every paper:
   raw_score
   applicable_max
   normalized_score
   tier

3. Recompute all aggregate QA values from source data.

4. Restore LIMITED tier even if count=0.

5. Threats to Validity:
verify actual human logs before claiming:
   "three independent screeners"
   "secondary coder for a 20% random sample"

6. AI-assisted second pass must NOT be presented as formal human-human IRR.

7. If Cohen's kappa was not actually computed:
   do not imply that it was.

Create:
tables/G7_quality_assessment.csv
tables/G7_quality_summary.csv
audit/G7_QA_IRR_AUDIT.md

PASS only if manuscript QA matches locked protocol exactly.

STOP after G7.
```

---

# G8 — FIX LEAKAGE CLAIMS + REGENERATE FIGURES 2–5

```text
TASK G8 — Correct graph provenance/leakage logic and regenerate figures.

PART A — Provenance

Classify:
EXTERNAL_FIXED
MODEL_DEFINED_FIXED
TRAIN_ONLY_INFERRED
FULL_DATA_INFERRED
PRECOMPUTED_UNCLEAR_SPLIT
JOINTLY_LEARNED_TRAINING
MIXED_PROVENANCE
UNCLEAR

Do not equate:
PRECOMPUTED_LOG
with:
FULL_DATA_INFERRED

Report separately:
- confirmed leakage risk
- potential leakage risk
- controlled provenance

Replace:
"Avoid Precomputed Log Co-occurrence Graphs in Production"

with:
"Construct log-derived graphs from training data only and report graph provenance explicitly."

PART B — Figures

Delete stale cached versions of Figures 2–5.

Figure 2:
- regenerate from G3 counts.

Figure 3:
- separate:
  LLM semantic concept/question graph
  programming/code structural graph
- do not label SINKT as AST unless source explicitly supports it.

Figure 4:
- regenerate from final graph encoder counts.

Figure 5:
- regenerate from final SSL counts.

For every figure record:
source CSV
generation script
denominator
analysis unit
version/date

Create:
tables/G8_graph_provenance.csv
audit/G8_LEAKAGE_FIGURE_AUDIT.md

PASS only if:
image == caption == prose == source CSV

STOP after G8.
```

---

# G9 — REFERENCES, PRIOR SURVEYS, CLAIMS, RESEARCH AGENDA

```text
TASK G9 — Audit references, prior-survey positioning, overclaims, and agenda evidence.

PART A — Prior surveys

1. Verify every survey/reference against official DOI/publisher metadata.

2. Audit current reference [6].
If unverifiable:
   remove it.

3. Rebuild Table II using verified prior works only, including where appropriate:
   - broad KT survey(s)
   - IEEE TLT 2024 KT survey
   - IEEE TKDE 2025 deep-KT review/tool/empirical study
   - dedicated Graph-KT survey(s), if officially verified

4. Remove unsupported "first" claims.

Preferred novelty framing:
"This survey jointly synthesizes Graph-Based and Self-Supervised KT through a sparse-concept lens, with explicit attention to graph provenance, leakage control, cold-start construct validity, calibration, and reproducibility."

PART B — Bibliography

5. Audit every 2025–2026 reference:
   title
   authors
   venue
   year
   volume/issue
   pages/article number
   DOI

6. Correct all verified metadata conflicts.

PART C — Scientific claims

Replace:
"standard models collapse near random guessing"
with:
"Many transductive KT architectures lack an explicit inductive mechanism for unseen KC identifiers unless external structural or semantic features are available."

Do not call CL4KT a GCN/GNN model.

Use:
- DKT/CL4KT: unseen-ID / untrained-representation limitation
- log-derived GKT: unseen-node / graph-support limitation
- semantic inductive models: side-information pathway

Replace:
"Graph-KT consistently improves"
with:
"Many Graph-KT studies report within-study improvements under their respective evaluation protocols."

Replace:
"SSL prevents representation collapse"
with:
"SSL regularizes representations and may improve robustness under low-support interaction settings."

Replace:
"hyperbolic metric prevents exponential distortion"
with:
"hyperbolic geometry may better accommodate hierarchical structure with reduced distortion."

Keep:
"0 out of N report ECE"
only if final coding verifies every paper.

PART D — Research agenda

7. Add one compact evidence-linking table:
Observed gap | Corpus evidence | Research implication | Agenda pillar

8. Do not call a pillar "evidence-derived" unless a corresponding observed corpus gap is documented.

Create:
audit/G9_REFERENCE_METADATA_AUDIT.csv
audit/G9_REFERENCE_CONFLICTS.md
tables/G9_prior_survey_comparison.csv
tables/G9_gap_to_agenda_map.csv
audit/G9_CLAIM_AGENDA_AUDIT.md

PASS only if references and claims are fully evidence-supported.

STOP after G9.
```

---

# G10 — FINAL PRE-SUBMISSION EDITOR GATE

```text
TASK G10 — Final editor/reviewer consistency gate before rewriting Abstract and Conclusion.

Do not rewrite final Abstract/Conclusion until this gate passes.

1. Report:
   G1 PASS/FAIL
   G2 PASS/FAIL
   G3 PASS/FAIL
   G4 PASS/FAIL
   G5 PASS/FAIL
   G6 PASS/FAIL
   G7 PASS/FAIL
   G8 PASS/FAIL
   G9 PASS/FAIL

2. For every FAIL:
   unresolved blocker
   missing evidence
   exact file needed
   manuscript sections affected

3. Search repository/manuscript for:
   BUILD-CANARY-E2
   seven electronic databases
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
   three independent screeners
   20% random sample
   consistently improves
   prevents representation collapse
   collapse near random
   **HIGH**
   **MODERATE**

4. Verify every remaining occurrence against source evidence.

5. Verify:
   PRISMA arithmetic
   corpus gateway identity
   Table III count
   Table IV count
   Table V denominator
   QA rubric
   IRR claims
   Figure 2–5 consistency
   prior survey table
   reference metadata
   research agenda evidence mapping

6. Verify the strict cold-start equation renders correctly:
   KC(x_t) ∉ K_cold
or:
   KC(x_t) ∈ K \ K_cold

7. Create:
   audit/G10_EDITOR_PRE_SUBMISSION_GATE.md

If G1–G9 all PASS:
   READY_FOR_FINAL_REWRITE = YES
else:
   READY_FOR_FINAL_REWRITE = NO

STOP.
Do not automatically rewrite Abstract/Conclusion.
```

---

# AFTER G10 PASSES — FINAL REWRITE ONLY

Run this only when:

`READY_FOR_FINAL_REWRITE = YES`

```text
FINAL TASK — Rewrite Abstract and Conclusion from frozen evidence.

ABSTRACT:
- one paragraph
- <=250 words
- self-contained
- no references
- no equations
- no unsupported claims
- use only frozen counts and verified findings
- emphasize TLT relevance:
  intelligent tutoring
  adaptive/personalized learning
  trustworthy learner-state estimation

CONCLUSION:
- summarize verified findings only
- no new numbers
- no unsupported empirical claims
- distinguish:
  literature evidence
  methodological synthesis
  future research agenda

Finally output:
- manuscript_TLT_EDITOR_READY.tex/.docx
- manuscript_TLT_EDITOR_READY.pdf
- audit/FINAL_EDITOR_COMPLIANCE.md

Final status must be one of:
READY_FOR_EXTERNAL_REVIEW
or
NOT_READY_FOR_EXTERNAL_REVIEW
```

---

# EXECUTION ORDER

Run exactly:

G1 → G2 → G3 → G4 → G5 → G6 → G7 → G8 → G9 → G10

Only after G10 PASS:
run FINAL TASK.

Do not merge steps.
Do not allow Antigravity to auto-run all tasks without stopping.
