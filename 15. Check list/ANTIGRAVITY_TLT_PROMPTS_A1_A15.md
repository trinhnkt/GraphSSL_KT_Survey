# ANTIGRAVITY — IEEE TLT PROMPTS A1 → A15

## Target manuscript

**Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda**

## Target journal

**IEEE Transactions on Learning Technologies (IEEE TLT)**  
Manuscript type: **Survey and Tutorial**

---

# GLOBAL RULES — APPLY TO ALL A1 → A15

Before every task, read:

1. `AGENTS.md`
2. `00_protocol/SOURCE_OF_TRUTH.md`
3. `00_protocol/SCOPE_v1.0_LOCKED.md`
4. `00_protocol/RQs_v1.0_LOCKED.md`
5. `00_protocol/SLR_PROTOCOL_v1.0_LOCKED.md`
6. current coding codebook
7. `CURRENT_STATUS.md`
8. `WAVE_A_REVIEW_v0.3.md`
9. current manuscript source/PDF

## Hard constraints

- Do **not** modify any `_LOCKED` file.
- Do **not** invent PRISMA counts, paper classifications, percentages, benchmark numbers, p-values, QA scores, hardware values, or references.
- If evidence is missing, use:
  - `NR`
  - `NA`
  - `UNCLEAR`
  - `TBD_VERIFY`
  - or remove the unsupported claim.
- Do not overwrite the current manuscript. Create versioned files.
- Every numerical claim must be traceable to a source CSV/log/workbook.
- Stop at the end of each task. Do not automatically start the next task.

---

# A1 — CREATE TLT WORKING COPY AND PROTECT EVIDENCE

## Prompt

```text
TASK A1 — Create a clean IEEE TLT working environment.

Read the project governance files first.

1. Create:
   12_manuscript/TLT/
   12_manuscript/TLT/figures/
   12_manuscript/TLT/tables/
   12_manuscript/TLT/supplementary/
   12_manuscript/TLT/audit/

2. Copy the current manuscript source into:
   manuscript_TLT_WORKING_v0.1
   without overwriting the original manuscript.

3. Create:
   MANUSCRIPT_TLT_FIX_DECISIONS.md
   MANUSCRIPT_TLT_CHANGELOG.md
   MANUSCRIPT_TLT_EVIDENCE_BLOCKERS.md

4. Record the current manuscript version, date, and source file.

5. Verify that all _LOCKED methodological files remain unchanged.

6. Do not edit scientific content yet.

OUTPUT:
- new TLT working directory;
- versioned manuscript copy;
- three audit Markdown files;
- list of files created.

STOP after A1.
```

### Acceptance gate
- Original manuscript untouched.
- `_LOCKED` files untouched.
- TLT working folder exists.

---

# A2 — MIGRATE TO OFFICIAL IEEE TLT TEMPLATE

## Prompt

```text
TASK A2 — Migrate the working manuscript to the official IEEE Transactions on Learning Technologies template.

1. Use the official IEEE TLT Word or LaTeX template.
2. Manuscript type: Survey and Tutorial.
3. Do not manually fake the journal header.
4. Remove any TKDE-specific header/text.
5. Preserve all current sections and references during migration.
6. Do not alter scientific claims yet.
7. Do not invent received/revised/accepted dates.
8. Keep corresponding-author information only in the proper IEEE template location.
9. Keep the manuscript within an eventual target of <=18 double-column pages, but do not shrink fonts or tables artificially.

Create:
- manuscript_TLT_TEMPLATE_v0.1.tex/.docx
- manuscript_TLT_TEMPLATE_v0.1.pdf

Update MANUSCRIPT_TLT_CHANGELOG.md.

STOP after template migration.
```

### Acceptance gate
- No TKDE header remains.
- Official TLT structure/template is used.
- No scientific claim changed in A2.

---

# A3 — REBUILD PRISMA AND CORPUS COUNTS

## Prompt

```text
TASK A3 — Audit and rebuild all systematic-review counts.

Do not trust any PRISMA number currently written in the manuscript.

1. Locate:
   search_log
   raw database exports
   deduplication log
   title/abstract screening
   full-text screening
   final corpus-tier files

2. Derive:
   N_IDENTIFIED
   N_DUPLICATES_REMOVED
   N_SCREENED
   N_TA_EXCLUDED
   N_FULLTEXT_ASSESSED
   N_FULLTEXT_EXCLUDED
   N_PRIMARY_CORE
   N_PRIMARY_ADJACENT_SPARSE
   N_PRIMARY_ADJACENT_METHOD

3. Check every arithmetic transition.

4. If the required source files do not exist:
   - do not reconstruct counts from the manuscript;
   - replace manuscript PRISMA numbers with TBD;
   - record the missing evidence in MANUSCRIPT_TLT_EVIDENCE_BLOCKERS.md.

5. Remove logic such as:
   "34 seed core + X PRISMA expansion"
   from final PRISMA accounting.
   Seed corpus is only a validation/recall resource.

6. Regenerate Figure 1 only from verified counts.

7. Search the entire manuscript for stale values such as 36, 37, 42 where they refer to corpus size and reconcile them.

Create:
- audit/PRISMA_AUDIT.md
- tables/corpus_counts.csv
- regenerated PRISMA figure if evidence permits.

STOP after A3.
```

### Acceptance gate
All PRISMA arithmetic reconciles, or unsupported values are explicitly `TBD`.

---

# A4 — REBUILD GRAPH-KT TAXONOMY FROM CODING DATA

## Prompt

```text
TASK A4 — Rebuild the Graph-KT taxonomy table from coding records, not prose memory.

1. Use current PAPER/MODEL/EXPERIMENT coding files.
2. Do not manually preserve old Table 3 values.
3. Separate paper count from model-entry count.
4. Generate the table fields:
   Paper
   Model entry
   Graph source
   Graph provenance
   Graph representation
   Directed
   Typed edges
   Graph/GNN encoder
   Temporal KT backbone
   Fusion
   Evidence status

MANDATORY CORRECTIONS:

KT004 / GKT:
- represent Dense, Transition, DKT Graph, PAM, MHA, VAE
  as separate model entries or a clearly labeled multi-variant row;
- use MODEL_DEFINED_FIXED where adjudicated;
- use SEQUENTIAL_TRANSITION where adjudicated.

KT014 / PDKT-C:
- graph_source = EXPERT_PREREQUISITE
- graph_provenance = EXTERNAL_FIXED
- graph_representation = KC_KC
- gnn_encoder = NONE
- temporal_backbone = RNN_LSTM_GRU
- fusion_type = REGULARIZATION_ONLY
- fusion_location = AUXILIARY_LOSS

KT039 / CL4KT:
- graph_source = NONE
- graph_provenance = NA
- graph_representation = NONE
- gnn_encoder = NONE
- temporal_backbone = SELF_ATTENTION_TRANSFORMER
- ssl_family = SEQUENCE_CONTRASTIVE

5. Do not state that all PRIMARY_CORE papers are Graph-KT.
6. Produce N_G, N_S, and N_G_AND_S separately.

Create:
- tables/graph_taxonomy.csv
- tables/graph_taxonomy_main.tex/.docx table
- audit/TAXONOMY_GRAPH_AUDIT.md

STOP after A4.
```

### Acceptance gate
KT004, KT014, KT039 exactly match adjudicated/pilot evidence.

---

# A5 — RESOLVE KT026 AND KT035 BEFORE FINAL TAXONOMY

## Prompt

```text
TASK A5 — Resolve the two major boundary papers KT026 and KT035.

PART 1 — KT026
1. Read the actual full paper and verify the PEBG/pretraining objective.
2. Determine whether it satisfies the frozen S-criterion.
3. Do not equate generic pretraining with SSL.
4. Verify whether the manuscript's current claims:
   masked concept prediction
   masked pretraining
   generic graph-autoencoder reconstruction
   are actually supported.
5. If unsupported, remove/rewrite them.

PART 2 — KT035 / HHSKT
1. Obtain/use lawful full-text evidence if available in the project.
2. Verify:
   graph source
   graph provenance
   node/edge types
   encoder
   temporal backbone
   fusion
   datasets
   split
   sparse/cold-start protocol
   whether strict zero-exposure KC evaluation truly exists.
3. If full text is still unavailable:
   keep FULLTEXT_REQUIRED/TBD_VERIFY;
   do not classify HHSKT as strict zero-exposure.

Create:
- audit/KT026_ADJUDICATION.md
- audit/KT035_FULLTEXT_AUDIT.md
- updated field-level evidence records

Do not change _LOCKED files.

STOP after A5.
```

### Acceptance gate
KT026 SSL status is explicit; KT035 zero-exposure status is evidence-based or remains TBD.

---

# A6 — REGENERATE SSL AND SPARSE/COLD-START TABLES + FIGURES

## Prompt

```text
TASK A6 — Rebuild the SSL and sparse/cold-start synthesis from coding data.

1. Regenerate SSL taxonomy from verified S-criterion papers.
2. For each paper/model record:
   ssl_family
   target level
   augmentation
   training mode
   educational_structure_preservation

3. Correct CL4KT:
   educational_structure_preservation = NO_EXPLICIT_CONSTRAINT
   unless new source evidence justifies otherwise.

4. Regenerate Figure 5 from actual SSL records.
5. Explicitly state its denominator:
   paper-level or model-entry-level.
6. State whether categories are mutually exclusive or multi-label.

7. Rebuild sparse/cold-start Table 6 using:
   LOW_FREQUENCY_KC
   LONG_TAIL_KC
   STRICT_KC_COLD_START
   LOW_DEGREE_GRAPH_NODE
   ITEM_COLD_START
   LEARNER_COLD_START
   SHORT_HISTORY
   GENERIC_DATA_SPARSITY
   SPARSE_ATTENTION_ARCHITECTURE

8. Do not publish 94.6% / 5.4% or any replacement percentage until the final corpus and KT035 status are verified.

9. Regenerate Figure 4/other percentages from source CSVs.
10. Record denominator and category-overlap rule in every caption.

Create:
- tables/ssl_taxonomy.csv
- tables/sparse_coldstart_audit.csv
- figures regenerated from scripts
- audit/SSL_SPARSE_AUDIT.md

STOP after A6.
```

---

# A7 — REGENERATE QUALITY, RELIABILITY, LEAKAGE, CALIBRATION

## Prompt

```text
TASK A7 — Rebuild Section 6 from quality/evidence coding.

1. Generate QA1–QA8 statistics from quality_assessment data only.
2. For each QA dimension report:
   applicable N
   NA count
   mean/median as appropriate
   denominator

3. Apply quality tiers exactly:
   HIGH >= 0.80
   MODERATE = 0.55–0.79
   LIMITED < 0.55

4. Remove the category MODERATE-HIGH.

5. QA7:
   use NA for papers that make no sparse/cold-start claim;
   do not penalize non-sparse studies.

6. QA6:
   distinguish:
   AUTHOR_CODE
   AUTHOR_SUPPLEMENT
   THIRD_PARTY_IMPLEMENTATION
   NO_ARTIFACT
   Third-party code does not raise author reproducibility score.

7. Leakage:
   distinguish:
   FULL_DATA_INFERRED
   PRECOMPUTED_UNCLEAR_SPLIT
   TRAIN_ONLY_INFERRED
   EXTERNAL_FIXED
   MODEL_DEFINED_FIXED
   JOINTLY_LEARNED_TRAINING

8. Do not turn UNCLEAR provenance into confirmed leakage.

9. Calibration:
   compute/report prevalence only after final coding.
   If incomplete, use cautious qualitative language.

10. Remove unsupported exact VRAM values.

Create:
- tables/quality_summary.csv
- tables/leakage_provenance_summary.csv
- tables/calibration_reporting_summary.csv
- audit/QUALITY_RELIABILITY_AUDIT.md

STOP after A7.
```

---

# A8 — REPOSITION THE PAPER FOR IEEE TLT

## Prompt

```text
TASK A8 — Reframe the manuscript specifically for IEEE Transactions on Learning Technologies.

1. Keep the technical Graph/SSL depth.
2. Strengthen relevance to:
   intelligent tutoring systems
   adaptive learning
   personalized learning
   learner-state estimation
   curriculum adaptation
   educational data mining
   trustworthy mastery prediction

3. Revise the Graph-KT definition to:
   explicit graph/graph-structured relations as a central mechanism,
   including but not limited to GNN message passing.

4. Remove unsupported "first systematic survey" claims.

5. Rebuild prior-survey positioning.
Include current major:
   broad KT surveys
   deep-KT/pyKT review/benchmark work
   dedicated Graph-KT survey(s)
   this survey

6. Compare surveys on:
   Graph coverage
   SSL coverage
   sparse/cold-start ontology
   graph provenance/leakage
   calibration
   reproducibility
   systematic-review protocol

7. End Sections 3–6 with a concise Learning-Technology Implication paragraph.

Create:
- audit/TLT_POSITIONING_AUDIT.md
- revised Introduction/Related Work text

STOP after A8.
```

---

# A9 — AUDIT THE CONTROLLED BENCHMARK BEFORE KEEPING IT

## Prompt

```text
TASK A9 — Decide whether the benchmark can remain in the TLT paper.

Search the project for raw benchmark evidence.

Required artifacts:
- dataset/version manifest
- preprocessing
- exact train/validation/test splits
- cold-KC lists
- model version/commit
- hyperparameters
- seeds
- logs
- predictions
- per-seed metrics
- ECE outputs
- statistical outputs
- hardware/environment

DECISION:

IF artifacts are incomplete:
1. remove Table 5 from the TLT working draft;
2. remove exact AUC/ECE/SD/p-value benchmark claims;
3. keep benchmark only as future/optional methodology if useful.

IF artifacts are complete:
1. verify every number independently from raw outputs;
2. continue to A10.

Do not reconstruct experiments from numbers already printed in the manuscript.

Create:
- audit/BENCHMARK_EVIDENCE_AUDIT.md
- explicit decision: KEEP / REMOVE / DEFER

STOP after A9.
```

---

# A10 — IF BENCHMARK IS KEPT, FIX DESIGN AND STATISTICS

## Prompt

```text
TASK A10 — Execute only if A9 decision = KEEP.

1. Resolve the learner split design.
Do not simultaneously describe it ambiguously as:
   80/20 holdout
   and
   5-fold CV.

If using 5-fold learner CV, document:
- outer fold structure;
- validation split inside training;
- early stopping;
- aggregation across folds/runs.

2. Audit cold-start fairness.

For every model create:
Model
Unseen-KC ID handling
Graph node available?
External graph?
Text semantics?
Pretrained semantics?
Train-only graph?
Other side information?

3. Ensure all models receive a documented information budget.

4. Recompute statistical tests.

5. Do not claim two-sided Wilcoxon p<0.01 from only five paired seed observations.

Choose:
- a valid larger independent repeated design;
- valid paired unit with justification;
- or remove inferential significance and report descriptive uncertainty.

6. Record the statistical unit explicitly:
seed / fold / learner / other.

7. Regenerate Table 5 only from raw output files.

Create:
- benchmark/BENCHMARK_PROTOCOL_LOCKED_FOR_RUN.md
- benchmark/information_budget.csv
- benchmark/statistical_analysis.md
- regenerated benchmark table

STOP after A10.
```

---

# A11 — FIX FORMULAS AND TECHNICAL DEFINITIONS

## Prompt

```text
TASK A11 — Correct the research-agenda equations and technical definitions.

1. Strict KC cold-start:
replace matrix-column zeroing with an interaction-level definition.

Use:
K_cold subset K
n_train(k)=0 for every k in K_cold

Define:
D_train^cold = interactions whose KCs are not in K_cold.

2. Temperature scaling:
state the standard procedure:
fit T on validation NLL/log-loss;
evaluate ECE/Brier afterward.

Do not state that standard temperature scaling directly minimizes ECE unless a specific method does so.

3. Causal equation:
describe the formula as backdoor adjustment under valid identification assumptions.
Do not present it as a universal do-calculus identity.

4. Check every equation symbol is defined immediately before/after use.
5. Ensure equations support the research agenda rather than create unsupported methodological claims.

Create:
- audit/EQUATION_AUDIT.md
- corrected equations in manuscript

STOP after A11.
```

---

# A12 — COMPLETE REFERENCE / DOI AUDIT

## Prompt

```text
TASK A12 — Verify all references before IEEE formatting.

For every reference:
1. verify author order;
2. title;
3. venue;
4. year;
5. volume/issue;
6. pages/article number;
7. DOI;
8. peer-reviewed vs preprint version.

Prefer official publisher/proceedings metadata.

Specially recheck:
- prior surveys;
- pyKT/deep-KT review;
- KGNN-KT;
- STG-SKT;
- R2GCurL;
- all 2025–2026 papers.

Do not silently replace conflicting metadata.
Record every conflict.

After verification:
- apply IEEE reference style;
- number references in first-citation order;
- remove uncited entries;
- ensure every in-text citation resolves.

Create:
- audit/REFERENCE_METADATA_AUDIT.csv
- audit/REFERENCE_CONFLICTS.md
- corrected IEEE reference list

STOP after A12.
```

---

# A13 — RESTRUCTURE THE MAIN PAPER FOR TLT

## Prompt

```text
TASK A13 — Restructure the evidence-aligned manuscript for IEEE TLT.

Use this order:

1. Introduction
   - learning-technology motivation
   - scope/definitions
   - prior-survey positioning
   - contributions

2. Systematic Review Methodology
   - protocol/RQs
   - search
   - screening
   - coding
   - quality/reliability
   - evidence synthesis

3. Graph-Based Knowledge Tracing
   - provenance
   - representations/encoders
   - temporal integration/fusion
   - learning-technology implications

4. Self-Supervised Knowledge Tracing
   - SSL objective taxonomy
   - augmentations
   - structure preservation
   - Graph+SSL intersection

5. Sparse-Concept and Cold-Start Evaluation
   - ontology
   - low-frequency vs zero-exposure
   - side information
   - evaluation gaps

6. Reliability, Reproducibility, and Calibration

7. Controlled Benchmark
   ONLY if A9/A10 approve KEEP

8. Discussion
   - Graph-KT contribution
   - SSL-KT contribution
   - sparse/unseen mechanisms
   - learning-technology implications
   - limitations

9. Research Agenda

10. Threats to Validity

11. Conclusion

Do not write the final Abstract or Conclusion yet.

Create manuscript_TLT_STRUCTURE_v0.x.

STOP after A13.
```

---

# A14 — REDESIGN TABLES, FIGURES, AND SUPPLEMENTARY

## Prompt

```text
TASK A14 — Optimize presentation for IEEE TLT without sacrificing readability.

Target:
<=18 double-column pages.

MAIN PAPER should keep:
1. prior-survey comparison;
2. Graph-KT taxonomy summary;
3. SSL taxonomy summary;
4. sparse/cold-start audit;
5. reliability/quality summary;
6. PRISMA;
7. key conceptual figures.

SUPPLEMENTARY should contain:
- full per-paper/model-entry inventory;
- full coding table;
- complete QA per paper;
- screening exclusion details;
- DOI audit;
- full benchmark details if retained.

Rules:
- do not reduce tables to unreadable font;
- do not manually edit quantitative figure percentages;
- every quantitative figure must have a source CSV/script;
- captions must state denominator and whether categories overlap.

Create:
- final main-paper table list
- supplementary table list
- regenerated figures
- audit/TABLE_FIGURE_SOURCE_MAP.md

STOP after A14.
```

---

# A15 — FINAL CONSISTENCY, ABSTRACT, CONCLUSION, TLT COMPLIANCE

## Prompt

```text
TASK A15 — Final evidence and IEEE TLT compliance pass.

Run only after A1–A14 are complete.

1. Search the manuscript for every number and verify its source.
2. Verify one consistent final corpus size everywhere.
3. Verify PRISMA arithmetic.
4. Verify Graph/SSL/sparse denominators.
5. Verify all Table/Figure captions.
6. Verify no unsupported:
   first
   state-of-the-art
   proves
   solves
   universally
   claims remain.

7. Rewrite the Abstract LAST:
- one paragraph;
- <=250 words;
- self-contained;
- no references;
- no equations;
- only frozen evidence;
- emphasize TLT relevance.

8. Use 3–5 Index Terms.

9. Rewrite Conclusion LAST:
- summarize verified findings;
- distinguish evidence from agenda;
- do not introduce new numbers;
- do not overclaim causal learning benefits.

10. Check:
- official TLT template;
- Survey/Tutorial manuscript type;
- <=18 double-column pages;
- readable figures/tables;
- IEEE citations/references;
- affiliations/corresponding author;
- no invented received/revised dates.

11. Create final compliance table:

Issue | Status | Evidence source | Final manuscript location | Remaining risk

12. Output:
- manuscript_TLT_FINAL_CANDIDATE source
- manuscript_TLT_FINAL_CANDIDATE.pdf
- MANUSCRIPT_TLT_FINAL_COMPLIANCE.md
- MANUSCRIPT_TLT_REMAINING_BLOCKERS.md

If any blocker remains, label the manuscript:
NOT READY FOR SUBMISSION.

Do not submit automatically.

STOP after A15.
```

---

# RECOMMENDED EXECUTION ORDER

Run exactly:

```text
A1
→ A2
→ A3
→ A4
→ A5
→ A6
→ A7
→ A8
→ A9
→ [A10 only if benchmark KEEP]
→ A11
→ A12
→ A13
→ A14
→ A15
```

## Important

Do not ask Antigravity to execute A1–A15 in one uncontrolled run.

Recommended:
- run one task;
- inspect output;
- approve/reject;
- then run the next.

The most important manual approval gates are:

```text
After A3  — PRISMA/corpus
After A5  — KT026 + KT035
After A7  — QA/reliability
After A9  — benchmark KEEP/REMOVE
After A12 — references
Before A15 — final scientific freeze
```
