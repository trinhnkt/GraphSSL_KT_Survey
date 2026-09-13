# ANTIGRAVITY — IEEE TLT POST-CANARY FIX F1 → F9
## Apply to the active manuscript source confirmed by BUILD-CANARY-E2

Target manuscript:
**Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda**

Target journal:
**IEEE Transactions on Learning Technologies (IEEE TLT)**  
Manuscript type: **Survey and Tutorial**

Current evidence:
The latest PDF visibly contains `BUILD-CANARY-E2`, which proves that the source used for that build is active. However, the canary was not removed and the major scientific blockers remain unresolved.

---

# GLOBAL RULES

Before each task:
1. Read `AGENTS.md`.
2. Read `00_protocol/SOURCE_OF_TRUTH.md`.
3. Read all `_LOCKED` protocol files.
4. Read current codebook and pilot/adjudication files.
5. Read the exact active source that generated the PDF containing `BUILD-CANARY-E2`.
6. Read previous audit outputs from A/B/C/D/E runs.

Hard constraints:
- Never modify `_LOCKED` files.
- Never derive missing evidence from manuscript prose.
- Never keep a numerical claim only because it already exists in the PDF.
- Every quantitative claim must trace to a source table/log.
- Every taxonomy label must trace to field-level evidence.
- Stop after each task.
- Do not run F9 unless F1–F8 pass.

---

# F1 — REMOVE CANARY AND LOCK ACTIVE BUILD CHAIN

```text
TASK F1 — Finalize build-chain verification and remove BUILD-CANARY-E2.

1. Remove the literal string `BUILD-CANARY-E2` from the active manuscript source.
2. Clean the build directory.
3. Rebuild using the exact verified build command.
4. Open/render the resulting PDF.
5. Confirm:
   - `BUILD-CANARY-E2` no longer appears;
   - title/abstract are otherwise intact;
   - output PDF path is the path used for export.

6. Record:
   active source path
   build command
   final PDF path
   PDF timestamp
   checksum/hash

7. Create:
   `audit/F1_ACTIVE_BUILD_LOCK.md`

Required final fields:
ACTIVE_SOURCE_CONFIRMED = YES
CANARY_REMOVED = YES
CLEAN_BUILD_CONFIRMED = YES
EXPORTED_PDF_PATH_CONFIRMED = YES

STOP after F1.
```

PASS only if all four fields are YES.

---

# F2 — RESTORE THE LOCKED SEARCH PROTOCOL + PRISMA

```text
TASK F2 — Rebuild the search/PRISMA layer from the locked protocol and real logs.

IMPORTANT PROTOCOL RULE:
The frozen SLR protocol defines six CORE bibliographic databases:
- Scopus
- Web of Science Core Collection
- ACM Digital Library
- IEEE Xplore
- ScienceDirect
- SpringerLink

arXiv is a supplementary/preprint discovery source, not automatically a seventh core bibliographic database.

Current manuscript repeatedly says "seven electronic databases" and includes arXiv as database #7.
Do not keep this unless a documented protocol deviation explicitly changed the frozen protocol.

1. Inspect `SLR_PROTOCOL_v1.0_LOCKED.md`.
2. Inspect `protocol_deviations.md`.
3. If no approved deviation exists:
   revise manuscript wording to:
   "six core bibliographic databases, supplemented by arXiv/secondary discovery"
   or equivalent evidence-faithful wording.

4. Locate actual:
   - search log
   - raw exports
   - deduplication ledger
   - title/abstract screening ledger
   - full-text screening ledger
   - final corpus tier file

5. Recompute all PRISMA values from those files only.

6. Required counts:
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

7. Reconcile all arithmetic.
   If 140 - 98 = 42, explicitly account for the 42 retained records.
   Do not force 42 to equal 37.

8. Remove:
   "34 seed core + 3 PRISMA expansion"
   from final corpus accounting.
   Seed membership is validation metadata only.

9. Delete the old PRISMA figure.
10. Regenerate Figure 1 from the verified counts.
11. Rebuild PDF and visually inspect the rendered figure.

Create:
- `tables/F2_prisma_counts.csv`
- `audit/F2_PRISMA_AND_SEARCH_PROTOCOL.md`
- `figures/F2_prisma_final.*`

STOP after F2.
```

PASS only if:
- search-source wording matches locked protocol or documented deviation;
- prose == figure == caption == source table;
- all arithmetic reconciles.

---

# F3 — REBUILD GRAPH-KT TABLE III FROM G_CRITERION

```text
TASK F3 — Delete and regenerate Table III from final Graph-KT coding.

Current PDF states NG=31 but Table III contains more than 31 paper rows.

1. Select paper records where:
   G_criterion = Y

2. Compute:
   N_G_PAPERS
   N_G_MODEL_ENTRIES

3. Generate Table III from the filtered data, not from the legacy manuscript table.

MANDATORY CORRECTIONS:

KT004 / GKT
- main table:
  graph construction = MULTIPLE_GRAPH_VARIANTS
  graph provenance = MULTIPLE
- supplementary entries:
  Dense
  Transition
  DKT Graph
  PAM
  MHA
  VAE
- preserve adjudicated provenance/source fields.

KT014 / PDKT-C
- graph_source = EXPERT_PREREQUISITE
- graph_provenance = EXTERNAL_FIXED
- graph_representation = KC_KC
- gnn_encoder = NONE
- temporal_backbone = RNN_LSTM_GRU
- fusion_type = REGULARIZATION_ONLY
- fusion_location = AUXILIARY_LOSS
- remove "Relational Paths" from the GNN encoder column.

KT039 / CL4KT
- do not include in Graph-KT table under current pilot evidence;
- graph_source = NONE
- graph_provenance = NA
- graph_representation = NONE
- gnn_encoder = NONE.

4. Caption must distinguish:
   paper count vs model-entry count.

5. If the complete table is too large:
   keep a compact summary in main paper;
   move complete model-entry inventory to Supplementary.

Create:
- `tables/F3_graph_papers.csv`
- `tables/F3_graph_model_entries.csv`
- `audit/F3_GRAPH_TABLE_REBUILD.md`

STOP after F3.
```

PASS only if Table III is generated from `G_criterion` and all mandatory corrections are present.

---

# F4 — REBUILD SSL CORPUS, RESOLVE KT026, FIX TABLE IV

```text
TASK F4 — Rebuild SSL corpus and Table IV from S_criterion.

Current PDF states NS=14 but Table IV visibly contains only 9 rows.

1. Select:
   S_criterion = Y

2. Compute:
   N_S
   N_G_AND_S

3. Verify:
   N_CORE = N_G + N_S - N_G_AND_S

4. Re-adjudicate KT026 from the actual full paper.
Determine:
   - self-generated target?
   - pretext objective?
   - actual loss?
   - training mode?
   - graph role?
   - S_criterion?

5. Do not retain labels such as:
   MASKED_PRETRAINING
   masked concept prediction
   masked cross-entropy
unless the paper explicitly supports them.

6. Keep KT039:
   ssl_family = SEQUENCE_CONTRASTIVE
   educational_structure_preservation = NO_EXPLICIT_CONSTRAINT

7. Regenerate the SSL taxonomy table.

8. Main paper:
   may use a concise representative table.

9. Supplementary:
   must contain the complete verified SSL list if manuscript claims a complete classification.

Create:
- `tables/F4_ssl_papers.csv`
- `tables/F4_ssl_taxonomy.csv`
- `audit/F4_KT026_SSL_ADJUDICATION.md`

STOP after F4.
```

PASS only if the stated SSL denominator and listed papers agree exactly.

---

# F5 — VERIFY STRICT COLD-START AND REMOVE UNSUPPORTED 94.6/5.4

```text
TASK F5 — Rebuild sparse/cold-start evidence before any prevalence claim.

1. Re-audit KT035 / HHSKT full text.
2. Strict zero-exposure criterion:
   for every held-out KC k,
   n_train(k) = 0.

3. Record for KT035:
   dataset
   held-out KC definition
   training exposure
   test exposure
   side information
   graph information
   exact evidence locator

4. If not explicitly verified:
   set:
   STRICT_KC_COLD_START = TBD_VERIFY
   and do not count KT035 as strict cold-start.

5. Verify KT044/SINKT independently.

6. Recompute:
   N_STRICT_KC_COLDSTART
   N_LOW_FREQUENCY_KC
   N_GENERIC_DATA_SPARSITY
   N_ITEM_COLDSTART
   N_LEARNER_COLDSTART
   other sparse ontology counts

7. Do not force the literature into only two categories.
Retain the locked sparse ontology:
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

8. Remove/recompute all:
   94.6%
   5.4%
   35/37
   2/37
claims depending on final evidence.

9. Propagate the final evidence to:
   Abstract
   Contributions
   Section V
   Table V
   Discussion
   Conclusion

Create:
- `tables/F5_sparse_coldstart_final.csv`
- `audit/F5_STRICT_COLDSTART_AUDIT.md`

STOP after F5.
```

PASS only if all strict cold-start claims have direct source evidence.

---

# F6 — RESTORE QA RUBRIC + REMOVE UNSUPPORTED CODER CLAIMS

```text
TASK F6 — Restore the frozen QA rubric and correct Threats to Validity.

Restore exactly:

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
- QA6 uses author-supported artifacts only.
- third-party implementation does not increase QA6.

1. Recompute every paper:
   raw_score
   applicable_max
   normalized_quality
   quality_tier

2. Recompute aggregate QA statistics from the final table.
3. Remove stale percentages from old rubric/old corpus.
4. Restore LIMITED tier even if count=0.

5. Threats to Validity:
Current manuscript claims:
   "three independent screeners"
   and
   "secondary coder for a 20% random sample".

Verify these against actual human screening/coding logs.

6. If those human-human procedures are not documented:
   remove the claims.
   Do not count AI-assisted second-pass coding as formal independent human IRR.

7. If formal Cohen's kappa was not actually computed:
   do not imply it was.

Create:
- `tables/F6_quality_assessment.csv`
- `tables/F6_quality_summary.csv`
- `audit/F6_QA_AND_IRR_AUDIT.md`

STOP after F6.
```

PASS only if QA matches locked protocol and coder claims match real logs.

---

# F7 — REBUILD LEAKAGE ANALYSIS + FIGURES 2–5

```text
TASK F7 — Correct graph provenance/leakage logic and regenerate all taxonomy figures.

PART A — Leakage

1. Classify graph provenance as:
   EXTERNAL_FIXED
   MODEL_DEFINED_FIXED
   TRAIN_ONLY_INFERRED
   FULL_DATA_INFERRED
   PRECOMPUTED_UNCLEAR_SPLIT
   JOINTLY_LEARNED_TRAINING
   MIXED_PROVENANCE
   UNCLEAR

2. Do not equate:
   PRECOMPUTED_LOG
with:
   FULL_DATA_INFERRED.

3. Report separately:
   confirmed leakage risk
   potential leakage risk
   controlled provenance

4. Replace:
   "Avoid Precomputed Log Co-occurrence Graphs in Production"
with:
   "Construct log-derived graphs from training data only and report graph provenance explicitly."

PART B — Figures

5. Delete stale cached/generated Figures 2–5.

6. Figure 2:
   regenerate from final N_CORE, N_G, N_S, N_G_AND_S.

7. Figure 3:
   separate:
   - LLM semantic concept/question graph
   - programming/code structural graph
   Do not label SINKT as AST unless directly supported.

8. Figure 4:
   regenerate from final graph encoder counts.
   Do not retain old image percentages.

9. Figure 5:
   regenerate from final SSL counts after F4.
   Do not retain old image percentages.

10. For every figure record:
    source CSV
    generation script
    denominator
    analysis unit
    timestamp/version

11. Rebuild PDF and visually inspect actual rendered figures.

Create:
- `tables/F7_graph_provenance_summary.csv`
- `audit/F7_LEAKAGE_AND_FIGURE_AUDIT.md`
- regenerated Figure 2–5 files

STOP after F7.
```

PASS only if image == caption == prose == source CSV.

---

# F8 — REFERENCES + SCIENTIFIC OVERCLAIM CLEANUP

```text
TASK F8 — Validate references and remove unsupported scientific overclaims.

PART A — References

1. Verify current reference [6] against official DOI/publisher metadata.
If unverified:
   remove it.

2. Rebuild prior-survey comparison from verified sources only.

3. Include verified major prior works where relevant:
   - broad KT survey(s)
   - IEEE TLT 2024 KT survey
   - IEEE TKDE 2025 deep-KT review/tool/empirical study
   - dedicated Graph-KT survey(s), if officially verified

4. Audit all 2025–2026 references for:
   authors
   year
   venue
   pages/article number
   DOI

PART B — Claims

5. Replace/remove:
   "standard models collapse near random guessing"
unless direct matched evidence exists.

Preferred:
"Many transductive KT architectures lack an explicit inductive mechanism for unseen KC identifiers unless external structural or semantic features are available."

6. Do not call CL4KT a GCN/GNN model.

Use:
- DKT/CL4KT: unseen-ID / untrained-representation limitation
- log-derived GKT: unseen-node / graph-support limitation
- semantic inductive models: external side-information pathway

7. Replace:
"Graph-KT consistently improves"
with:
"Many Graph-KT studies report within-study improvements under their respective evaluation protocols."

8. Replace:
"SSL prevents representation collapse"
with:
"SSL regularizes representations and may improve robustness under low-support interaction settings."

9. Replace:
"hyperbolic metric prevents exponential distortion"
with:
"hyperbolic geometry may better accommodate hierarchical structure with reduced distortion."

10. Keep "0 out of N report ECE" only if final coding verifies every paper.

Create:
- `audit/F8_REFERENCE_METADATA_AUDIT.csv`
- `audit/F8_REFERENCE_CONFLICTS.md`
- `audit/F8_SCIENTIFIC_CLAIM_AUDIT.md`

STOP after F8.
```

PASS only if every cited survey/reference is verifiable and all empirical claims are evidence-supported.

---

# F9 — PRE-A15 GATE

```text
TASK F9 — Final evidence consistency gate before rewriting Abstract/Conclusion.

Do not rewrite final Abstract/Conclusion until the gate passes.

1. Report:
   F1 PASS/FAIL
   F2 PASS/FAIL
   F3 PASS/FAIL
   F4 PASS/FAIL
   F5 PASS/FAIL
   F6 PASS/FAIL
   F7 PASS/FAIL
   F8 PASS/FAIL

2. For every FAIL:
   unresolved blocker
   missing evidence
   exact file needed
   manuscript sections affected

3. Repository-wide consistency scan for:
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
   MODERATE-HIGH
   **HIGH**
   **MODERATE**

4. Verify every remaining occurrence is source-supported.

5. Verify the strict cold-start equation renders correctly:
   KC(x_t) ∉ K_cold
or
   KC(x_t) ∈ K \ K_cold

6. Check:
   PRISMA arithmetic
   corpus set identity
   Table III count
   Table IV count
   Table V denominator
   QA rubric
   reference list
   figure values
   cross-paper claims

7. Create:
   `audit/F9_PRE_A15_GATE.md`

If all F1–F8 PASS:
   READY_FOR_FINAL_A15 = YES
Else:
   READY_FOR_FINAL_A15 = NO

STOP.
Do not automatically run A15.
```

---

# EXECUTION ORDER

Run exactly:

F1 → F2 → F3 → F4 → F5 → F6 → F7 → F8 → F9

Human approval checkpoints:
- after F1
- after F2
- after F5
- after F6
- after F8
- after F9

Only after:
`READY_FOR_FINAL_A15 = YES`

should Antigravity rewrite the final Abstract, Conclusion, and produce the IEEE TLT submission candidate.
