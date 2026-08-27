# SLR_PROTOCOL_v1.0_LOCKED.md

## Systematic Literature Review Protocol — Frozen Version

### Official survey title

**Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda**

Protocol version: **v1.0 — FROZEN**  
Protocol-lock date: **2026-08-09**  
Parent scope: **SCOPE_v1.0_LOCKED.md**  
Parent RQs: **RQs_v1.0_LOCKED.md**

> **Status:** FROZEN BEFORE THE NEW SYSTEMATIC SEARCH.  
> Any substantive change after this version must be recorded in `protocol_deviations.md`, including the date, reason, affected records, and whether prior screening/coding must be repeated.

---

# 1. Review objective

The review will systematically identify, screen, code, and synthesize research on:

1. **Graph-Based Knowledge Tracing (Graph-KT)**;
2. **Self-Supervised Knowledge Tracing (SSL-KT)**;
3. sparse-concept and related cold-start conditions as a cross-cutting analytical lens;
4. reliability, reproducibility, calibration, statistical rigor, and computational reporting;
5. evidence-supported future research priorities.

The primary systematic-corpus rule is fixed as:

```text
PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)
```

Sparse-only KT papers may enter an adjacent corpus for terminology and evaluation context, but they do not become primary Graph/SSL evidence merely because they study sparsity.

The review will keep:

```text
LIT_REPORTED
LIT_SYNTHESIZED
REPRODUCED
AGENDA_INFERENCE
```

as separate evidence classes.

---

# 2. Review questions

The protocol operationalizes six frozen RQs.

- **RQ1:** graph construction, provenance, representation, validation, and leakage risk;
- **RQ2:** Graph-KT architecture and graph–sequence fusion;
- **RQ3:** SSL objectives, augmentation, training mode, and educational structure preservation;
- **RQ4:** sparse-concept/cold-start definitions, protocols, and evidence;
- **RQ5:** reliability, reproducibility, calibration, statistics, artifacts, and computational reporting;
- **RQ6:** evidence-derived research agenda.

The full wording and subquestions are defined in `RQs_v1.0_LOCKED.md`.

---

# 3. Review period

## 3.1 Main modern-KT search

```text
2015-01-01 through 2026-07-31
```

This cutoff is fixed for the first complete search.

## 3.2 Historical foundations

Pre-2015 publications may be retained as:

```text
FOUNDATIONAL_BACKGROUND
```

They do not enter the modern primary-corpus count.

## 3.3 Final update search

All core database searches must be rerun **within 2–4 weeks before submission**.

If the review team decides to extend the cutoff beyond 2026-07-31, the extension must be systematic:

1. update the cutoff;
2. rerun all core searches to the same new cutoff;
3. re-run deduplication/screening for newly retrieved records;
4. update PRISMA counts;
5. record the amendment in `protocol_deviations.md`.

Do not add isolated later papers opportunistically while retaining the old cutoff.

---

# 4. Information sources

## 4.1 Core bibliographic databases

Search each source independently:

1. **Scopus**
2. **Web of Science Core Collection**
3. **ACM Digital Library**
4. **IEEE Xplore**
5. **ScienceDirect**
6. **SpringerLink**

The purpose of using multiple databases is to reduce publisher/database coverage bias.

## 4.2 Secondary discovery and metadata validation

May be used for citation chasing or verification:

- DBLP;
- Crossref;
- Google Scholar;
- official publisher/proceedings pages.

Secondary sources do **not** replace the core searches.

## 4.3 Preprints

arXiv/OpenReview/other preprints may be tracked for:

- emerging-work monitoring;
- discovery of a peer-reviewed version;
- background when no peer-reviewed version exists.

When a peer-reviewed version exists, it is the preferred record.

Publication status must be explicitly coded.

---

# 5. Search architecture

The search strategy has **core retrieval queries** and **supplementary lens queries**.

Core queries identify the primary Graph/SSL corpus. Supplementary queries improve recall for sparse-concept and reliability evidence but do not override the primary-corpus eligibility rule.

Every executed query must be saved **verbatim** in `search_log.csv`.

---

# 6. Core search queries

## Q-G — Graph-Based KT

```text
("knowledge tracing" OR "student knowledge tracing")
AND
(
  graph OR "graph neural network" OR GNN OR GCN OR GAT
  OR hypergraph OR heterogeneous
  OR "dynamic graph" OR "temporal graph"
  OR prerequisite OR "prerequisite graph"
  OR "concept map" OR "skill graph"
  OR "knowledge graph" OR "concept graph"
  OR "knowledge structure"
  OR "multi-relational" OR "multi relational"
)
```

Purpose:

- primary retrieval for RQ1–RQ2;
- discovery of Graph+SSL papers;
- discovery of graph-based sparse/cold-start papers.

---

## Q-S — Self-Supervised KT

```text
("knowledge tracing" OR "student knowledge tracing")
AND
(
  "self-supervised" OR "self supervised"
  OR contrastive
  OR "masked modeling" OR "masked prediction"
  OR "masked interaction" OR "masked concept"
  OR reconstruction
  OR "pretext task"
  OR "self-distillation" OR "self distillation"
  OR "teacher student" OR "teacher-student"
  OR "consistency learning"
)
```

Purpose:

- primary retrieval for RQ3;
- discovery of Graph+SSL papers;
- discovery of SSL methods evaluated under sparsity/cold-start.

---

# 7. Supplementary lens queries

## Q-P — Sparse / cold-start KT lens

```text
("knowledge tracing" OR "student knowledge tracing")
AND
(
  sparse OR sparsity
  OR "low frequency" OR "low-frequency"
  OR "long tail" OR long-tail
  OR few-shot OR "few shot"
  OR "cold start" OR cold-start
  OR unseen OR inductive
)
AND
(
  concept OR skill OR "knowledge component"
  OR item OR exercise OR learner
)
```

Purpose:

- identify sparse/cold-start Graph/SSL papers missed by Q-G/Q-S;
- identify `PRIMARY_ADJACENT_SPARSE` papers;
- map terminology for RQ4.

A Q-P hit enters `PRIMARY_CORE` only if it also satisfies the G-criterion or S-criterion.

---

## Q-R — Reliability/evaluation lens

```text
("knowledge tracing" OR "student knowledge tracing")
AND
(
  calibration OR reproducibility OR leakage
  OR "temporal split" OR "learner split"
  OR "cold start" OR cold-start
  OR "confidence interval"
  OR bootstrap
  OR "statistical significance"
  OR "multiple comparison"
  OR "effect size"
  OR scalability
  OR "training time" OR memory
)
```

Purpose:

- identify KT evaluation/reliability papers;
- support RQ5 methodology and adjacent evidence;
- discover primary Graph/SSL papers with reliability-focused titles/abstracts.

A Q-R hit does not become `PRIMARY_CORE` unless it satisfies the frozen primary-corpus rule.

---

# 8. Database-specific query adaptation

Each database may require syntax changes for:

- title/abstract/keyword field identifiers;
- phrase quotation;
- wildcard operators;
- date filters;
- document-type filters.

Rules:

1. preserve the conceptual meaning of Q-G, Q-S, Q-P, and Q-R;
2. do not silently add/remove substantive search concepts;
3. record the **exact adapted query**;
4. record search date and filters;
5. record returned count before manual screening;
6. save/export the raw result file.

Required `search_log.csv` fields:

```text
search_id
database
query_family
search_date
cutoff_start
cutoff_end
exact_query
fields_searched
language_filter
document_type_filter
records_returned
export_filename
notes
```

---

# 9. Identification and export

For every database/query execution, export when available:

- title;
- authors;
- publication year;
- venue/source title;
- abstract;
- DOI;
- URL/database record;
- author keywords;
- index keywords;
- document type;
- publication status;
- database source;
- citation metadata.

Every imported row must receive:

```text
record_id
source_database
search_id
```

The original export must remain unchanged in the archive.

---

# 10. Deduplication

Deduplication occurs **after combining all search exports**.

## 10.1 Matching hierarchy

1. normalized DOI exact match;
2. normalized title exact/near-exact match;
3. title + first author + year;
4. manual resolution.

## 10.2 Normalization

For duplicate matching only:

- lowercase title;
- normalize whitespace;
- remove non-semantic punctuation;
- normalize DOI prefix/URL form.

Do not overwrite the original source metadata.

## 10.3 Conference/journal extensions

Do not automatically merge conference and journal versions.

Code one of:

- `DUPLICATE_SAME_WORK`;
- `EXTENDED_VERSION`;
- `RELATED_NOT_DUPLICATE`;
- `UNCLEAR`.

When the journal version is a substantive extension, both may remain if each contributes distinct evidence. The relationship must be noted.

## 10.4 Deduplication audit

Maintain:

```text
duplicate_group_id
kept_record_id
removed_record_id
matching_rule
resolution
reviewer
notes
```

---

# 11. Screening workflow

Screening has two stages.

## Stage 1 — Title/abstract screening

Allowed decisions:

- `INCLUDE_FULLTEXT`
- `BACKGROUND`
- `EXCLUDE_TITLE_ABSTRACT`
- `UNCERTAIN`

Any `UNCERTAIN` record moves to full text rather than being excluded on doubt alone.

## Stage 2 — Full-text screening

Allowed final decisions:

- `PRIMARY_CORE`
- `PRIMARY_ADJACENT_SPARSE`
- `PRIMARY_ADJACENT_METHOD`
- `BACKGROUND`
- `EXCLUDE_FULLTEXT`

Each full-text exclusion must have **one primary exclusion reason**.

Secondary notes may be retained, but PRISMA exclusion counts use the primary reason only.

---

# 12. Inclusion criteria

## 12.1 Mandatory criteria for `PRIMARY_CORE`

A paper must satisfy all:

- **IC1:** English-language full text.
- **IC2:** Peer-reviewed journal article or peer-reviewed full conference paper.
- **IC3:** Knowledge Tracing or sequential learner-state estimation is a central task.
- **IC4:** Sufficient methodological detail exists for the relevant RQ coding.
- **IC5:** Full text is accessible to the review team.

AND at least one:

- **IC6-G:** satisfies the frozen operational definition of Graph-Based KT;
- **IC6-S:** satisfies the frozen operational definition of Self-Supervised KT.

Therefore:

```text
PRIMARY_CORE = IC1–IC5 AND (IC6-G OR IC6-S)
```

## 12.2 Adjacent sparse inclusion

A paper may be retained as:

```text
PRIMARY_ADJACENT_SPARSE
```

when:

- KT is central;
- sparse/cold-start concept evidence is central or methodologically important;
- but neither G-criterion nor S-criterion is satisfied.

These papers support RQ4 context, not primary Graph/SSL claims.

## 12.3 Adjacent method inclusion

A paper may be retained as:

```text
PRIMARY_ADJACENT_METHOD
```

when it is directly useful for:

- KT calibration;
- leakage methodology;
- reproducibility;
- sparse-stratum evaluation;
- statistical evaluation;

but it is not a Graph/SSL primary paper.

Its evidence must be reported separately from `PRIMARY_CORE`.

---

# 13. Exclusion criteria

Use one primary reason from the following controlled list.

- **EC1_NO_KT:** no Knowledge Tracing/sequential learner-state task.
- **EC2_CD_ONLY:** cognitive diagnosis only, without sequential KT.
- **EC3_RECOMMENDATION_ONLY:** recommendation/path planning only, without central KT.
- **EC4_GENERIC_GRAPH_SSL:** generic graph/SSL method without KT application.
- **EC5_LLM_TUTOR_ONLY:** LLM tutoring/dialogue without KT state estimation.
- **EC6_SPARSE_ATTENTION_ONLY:** sparse refers only to architectural/computational sparsity and the paper neither satisfies the G/S criterion nor contributes relevant adjacent sparse evidence.
- **EC7_WRONG_PUBLICATION_TYPE:** abstract, poster, editorial, thesis/dissertation, patent, tutorial, or insufficient non-full publication.
- **EC8_DUPLICATE_SUPERSEDED:** duplicate/superseded version not selected.
- **EC9_INSUFFICIENT_METHOD:** insufficient methodological detail after reasonable full-text inspection.
- **EC10_NON_ENGLISH:** non-English full text.
- **EC11_PERFORMANCE_PREDICTION_NOT_KT:** generic student-performance prediction without KT/sequential learner-state framing.
- **EC12_OUTSIDE_DATE_WINDOW:** outside modern review window and not retained as foundation.
- **EC13_OTHER:** use only with an explicit written justification.

Do not use `EC13_OTHER` when a more specific code applies.

---

# 14. Operational boundary decisions used during screening

The following scope rules are binding.

## 14.1 Relation-aware ≠ automatically Graph-Based

Pairwise relation scores, side features, attention bias, or embeddings do not satisfy the G-criterion unless an explicit graph/hypergraph/edge structure or equivalent graph-learning mechanism is used.

## 14.2 Pretraining/regularization ≠ automatically SSL

Ordinary regularization, transfer learning, embedding initialization, or supervised auxiliary tasks do not satisfy the S-criterion unless a self-generated/pretext/consistency objective is present.

## 14.3 Sparse attention ≠ sparse concept

Architectural sparse attention is coded separately from sparse KC/cold-start.

## 14.4 Strict KC cold-start

A strict KC cold-start claim requires zero training-interaction exposure for the held-out KC under the stated split.

External graph/semantic information must be coded separately.

## 14.5 Learning Path Recommendation

LPR is downstream. It enters the primary corpus only when the same paper independently satisfies:

```text
KT AND (GRAPH_BASED OR SELF_SUPERVISED)
```

---

# 15. Snowballing

Snowballing begins after a provisional `PRIMARY_CORE` set is established.

## 15.1 Backward snowballing

Inspect references of all `PRIMARY_CORE` papers for potentially eligible works.

## 15.2 Forward snowballing

Use citation indexes/Google Scholar/publisher citation tools for:

- seminal Graph-KT papers;
- seminal SSL-KT papers;
- core sparse/cold-start Graph/SSL papers.

## 15.3 Prior-survey reference mining

Inspect reference lists of major prior KT/Graph-KT/SSL-KT surveys.

## 15.4 Snowballing rule

Every discovered record enters the same screening pipeline.

Do not directly add a snowballed paper to the final corpus.

Code source as:

- `BACKWARD`;
- `FORWARD`;
- `PRIOR_SURVEY_REFERENCE`.

---

# 16. Seed corpus use

The existing 75-paper corpus is a **legacy seed set**, not the result of the new systematic search.

Use it for:

- search-term calibration;
- pilot coding;
- known-paper recall checks;
- metadata conflict detection.

Do not:

- use 75 as a PRISMA inclusion count;
- assume all 75 satisfy the new scope;
- skip independent database retrieval because a paper already exists in the seed set.

Each seed paper must be linked to the new search/screening record where retrieved.

---

# 17. Unit of analysis

Maintain two linked units.

## 17.1 Paper unit

```text
paper_id
```

One canonical publication.

## 17.2 Model-entry unit

```text
model_entry_id
```

Create a separate model entry only when the paper contains substantively different:

- graph construction;
- graph representation;
- graph encoder;
- temporal KT backbone;
- graph–sequence fusion;
- SSL objective/training mode;
- sparse/cold-start protocol.

Do not create a model entry for:

- seeds;
- hyperparameters;
- ordinary ablations;
- dataset-specific checkpoints;
- repeated runs.

---

# 18. Data extraction

Data extraction follows `coding_codebook.md`, which must be frozen as v1.0 after pilot coding.

Minimum extraction domains:

1. bibliographic metadata;
2. corpus role/status;
3. graph source and provenance;
4. graph representation;
5. graph encoder;
6. temporal KT backbone;
7. graph–sequence fusion;
8. SSL family/objective/training mode;
9. augmentation and educational structure preservation;
10. sparse/cold-start construct;
11. datasets/preprocessing;
12. split and leakage controls;
13. predictive metrics;
14. calibration metrics;
15. statistical evidence;
16. reproducibility artifacts;
17. computational/scalability reporting;
18. limitations;
19. claim/evidence strength;
20. research-agenda tags.

Missing-value vocabulary:

```text
NR       = not reported
NA       = not applicable
UNCLEAR  = relevant information exists but cannot be coded confidently
TBD_VERIFY = metadata/coding requires source verification
```

Do not infer an unreported methodological choice from model family/name alone.

---

# 19. Pilot coding

Before full coding, select **12–15 papers purposively** to span the intended taxonomy.

Pilot set should include examples of:

- foundational sequence KT;
- prerequisite Graph-KT;
- co-occurrence/similarity or learned Graph-KT;
- heterogeneous Graph-KT;
- hypergraph KT;
- dynamic/temporal graph KT;
- sequence contrastive KT;
- graph contrastive KT;
- graph+SSL KT;
- sparse/cold-start KT;
- inductive/semantic/LLM-assisted KT;
- one ambiguous boundary case.

Two coders independently code all pilot papers.

After discussion:

1. revise definitions;
2. document unresolved edge cases;
3. update controlled vocabulary if necessary;
4. recode affected pilot papers;
5. freeze `coding_codebook_v1.0_LOCKED.md`.

The full-corpus coding must not begin before this gate is passed.

---

# 20. Screening reliability

## 20.1 Title/abstract stage

A **25% random sample** of deduplicated records will be independently screened by a second coder.

Additionally, all records initially labeled `UNCERTAIN` by the first coder must receive second review.

Report:

- sample size;
- raw agreement;
- Cohen’s kappa;
- disagreement categories;
- consensus procedure.

If agreement is unacceptably low for meaningful use of the protocol, clarify the screening rules and re-screen affected records.

## 20.2 Full-text stage

All full-text records assigned either:

- `EXCLUDE_FULLTEXT`, or
- `UNCERTAIN` before final decision,

must receive a second reviewer check.

At least **25% of all full-text eligibility decisions** must be independently double-screened overall.

This ensures exclusion decisions are not based on one reviewer alone while remaining feasible for a specialized technical survey.

---

# 21. Coding reliability

After codebook freeze, independently double-code:

```text
max(20 papers, 25% of PRIMARY_CORE)
```

subject to the obvious cap that the double-coded sample cannot exceed the corpus.

The sample should be stratified across:

- Graph-KT;
- SSL-KT;
- Graph+SSL;
- sparse/cold-start evidence;
- static/dynamic/hypergraph families.

Report:

- raw agreement;
- Cohen’s kappa for categorical dimensions where appropriate;
- macro-average or distribution across dimensions;
- disagreement-resolution process.

Do not copy inter-rater statistics from the previous survey automatically; the new scope and codebook require a new reliability estimate.

---

# 22. Quality and evidence-reliability assessment

Quality does **not** automatically determine inclusion.

Score applicable criteria 0/1/2:

- **QA1:** problem/task clarity;
- **QA2:** dataset/preprocessing transparency;
- **QA3:** split/graph provenance/leakage transparency;
- **QA4:** baseline fairness and ablation adequacy;
- **QA5:** statistical uncertainty/multi-run evidence;
- **QA6:** reproducibility artifacts;
- **QA7:** sparse/cold-start construct validity;
- **QA8:** computational/scalability transparency.

## 22.1 Applicable-item normalization

Because QA7 may be `NA` for papers making no sparse/cold-start claim, do not automatically penalize those papers.

Report:

```text
raw_score
applicable_max
normalized_quality = raw_score / applicable_max
```

Suggested interpretation:

```text
HIGH      >= 0.80
MODERATE  0.55–0.79
LIMITED   < 0.55
```

For continuity, raw 0–16 totals may also be reported when all eight criteria are applicable.

## 22.2 Evidence strength

Quality score is not identical to claim truth.

A study may be categorized as:

- `STRONG`;
- `MODERATE`;
- `LIMITED`;
- `UNVERIFIED`;

for a specific claim based on protocol match, uncertainty, support, and transparency.

---

# 23. Evidence-synthesis rules

## 23.1 No naïve cross-paper ranking

Do not directly rank original-paper AUC/ACC/NLL values across unmatched protocols.

Potential incompatibilities include:

- dataset version;
- preprocessing;
- multi-skill handling;
- sequence truncation;
- split protocol;
- graph construction;
- tuning budget;
- metric implementation;
- test set.

## 23.2 Evidence labels

Every quantitative or evaluative table should identify whether a value is:

```text
LIT_REPORTED
REPRODUCED
```

Narrative synthesis may additionally use:

```text
LIT_SYNTHESIZED
AGENDA_INFERENCE
```

## 23.3 Sparse evidence

A sparse/cold-start claim should record, where available:

- exact sparsity definition;
- threshold/rule;
- partition used to define sparsity;
- number of KCs;
- number of learners/items;
- positive/negative labels;
- test interactions;
- uncertainty;
- calibration;
- reliability caveat.

## 23.4 Null and counter-pattern evidence

Do not suppress:

- no-gain results;
- cases where graph models underperform sequence baselines;
- cases where SSL gains are dataset-dependent;
- cases where AUC improves while calibration worsens;
- sparse strata with insufficient support.

These are part of the evidence synthesis.

---

# 24. Calibration and reliability coding

Calibration is not required for inclusion, but it is a key RQ5 field.

Record:

- NLL/log loss;
- Brier score;
- ECE;
- adaptive ECE;
- reliability diagrams;
- calibration slope/intercept;
- post-hoc calibration method.

If a paper reports only AUC/ACC, code calibration as `NR`, not as evidence of good or poor calibration.

---

# 25. Computational/scalability coding

Computational cost is not required for inclusion.

Record only reported/measured evidence:

- parameter count;
- training time;
- time/epoch;
- inference latency;
- throughput;
- CPU RAM;
- GPU VRAM;
- graph-construction time;
- hardware;
- complexity analysis;
- scale-up experiments;
- OOM/timeout.

Do not infer scalability from model size or architecture alone.

---

# 26. Controlled reproduced benchmark

A reproduced benchmark is **outside SLR eligibility** and is used only as supporting evidence.

Possible benchmark questions:

- train-only vs leakage-prone graph;
- sequence-only vs graph-based model;
- supervised-only vs SSL;
- overall vs sparse-KC performance;
- discrimination vs calibration;
- performance vs computational cost.

Rules:

1. same data/split/preprocessing where comparisons are made;
2. test data not used for model selection;
3. sparse strata defined from training information only;
4. outputs labeled `REPRODUCED`;
5. original-paper claims and reproduced results remain separate;
6. benchmark results do not determine literature inclusion.

---

# 27. PRISMA-style accounting

Maintain exact counts for:

- records identified from each database;
- records identified via snowballing;
- duplicates removed;
- records screened at title/abstract;
- title/abstract exclusions;
- full texts sought;
- full texts unavailable;
- full texts assessed;
- full-text exclusions by primary reason;
- final `PRIMARY_CORE`;
- `PRIMARY_ADJACENT_SPARSE`;
- `PRIMARY_ADJACENT_METHOD`;
- background/foundational records.

**Do not create final PRISMA counts before the logs exist.**

The legacy 75-paper corpus is not a PRISMA count for this review.

All displayed PRISMA numbers must reconcile with the screening CSV files.

---

# 28. Required artifacts

Recommended project structure:

```text
protocol/
  SCOPE_v1.0_LOCKED.md
  RQs_v1.0_LOCKED.md
  SLR_PROTOCOL_v1.0_LOCKED.md
  coding_codebook.md
  protocol_deviations.md

slr/
  search_log.csv
  records_raw.csv
  records_deduplicated.csv
  deduplication_log.csv
  screening_title_abstract.csv
  screening_fulltext.csv
  included_papers_seed.csv
  final_primary_core.csv
  primary_adjacent_sparse.csv
  primary_adjacent_method.csv
  background_corpus.csv
  model_entries.csv
  quality_assessment.csv
  inter_rater_screening.csv
  inter_rater_fulltext.csv
  inter_rater_coding.csv
  metadata_conflicts.csv
```

Optional but recommended:

```text
slr/exports/
slr/fulltexts_manifest.csv
slr/doi_audit.csv
```

---

# 29. Metadata verification

Before final manuscript synthesis, verify for every cited primary paper:

- title;
- authors;
- year;
- venue;
- DOI;
- publication type;
- peer-reviewed version;
- conference/journal extension relationship.

Use official publisher/proceedings records where possible.

Conflicts must be stored in:

```text
metadata_conflicts.csv
```

Do not silently replace uncertain metadata.

---

# 30. Protocol deviations

After v1.0 freeze, changes to any of the following require a logged deviation:

- title or scope;
- RQ wording/evidence mapping;
- date window;
- database set;
- core/supplementary search architecture;
- inclusion/exclusion criteria;
- screening decision labels;
- Graph-Based KT operational definition;
- Self-Supervised KT operational definition;
- sparse-concept ontology;
- quality criteria;
- inter-rater sampling plan;
- evidence-class rules.

Deviation record:

```text
date
protocol_version_before
protocol_version_after
change
reason
affected_records
screening_repeated
coding_repeated
author_approval
```

---

# 31. Stop rules

Do not proceed to full coding if:

- scope and RQs are not frozen;
- database queries have not been logged exactly;
- raw exports are missing;
- deduplication has not been audited;
- pilot coding has unresolved recurrent boundary disputes;
- codebook v1.0 is not frozen.

Do not proceed to manuscript evidence synthesis if:

- corpus is not frozen;
- PRISMA counts do not reconcile;
- primary-paper metadata conflicts are unresolved or explicitly documented;
- quality assessment is incomplete;
- inter-rater results are missing;
- Graph/SSL/sparse-cold-start fields required for the relevant RQs remain systematically uncoded.

---

# 32. Completion criteria for the SLR phase

The SLR phase is complete when all are true:

- [ ] all six core database searches have been executed;
- [ ] Q-G and Q-S have been executed in every core database;
- [ ] supplementary Q-P/Q-R coverage has been completed or any database-specific limitation documented;
- [ ] search logs and raw exports are archived;
- [ ] deduplication is complete and auditable;
- [ ] title/abstract screening is complete;
- [ ] full-text screening is complete;
- [ ] final corpus tiers are frozen;
- [ ] `coding_codebook_v1.0_LOCKED.md` is frozen;
- [ ] all `PRIMARY_CORE` papers are fully coded;
- [ ] adjacent corpora are coded to the fields needed for their intended RQs;
- [ ] quality/evidence-reliability assessment is complete;
- [ ] inter-rater screening and coding results are reported;
- [ ] metadata/DOI conflicts are resolved or explicitly flagged;
- [ ] PRISMA counts reconcile exactly with screening logs;
- [ ] the final update search is completed before submission;
- [ ] RQ1–RQ5 have sufficient coded evidence for synthesis;
- [ ] RQ6 agenda items can be traced to explicit evidence gaps.

---

# 33. Changes from v0.1 before freeze

The following corrections were made before locking v1.0.

## Correction 1 — Primary-corpus rule

Removed the previous rule that allowed sparse-only papers to enter the same primary corpus via an independent `IC6-P`.

Locked rule:

```text
PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)
```

Sparse-only KT is now `PRIMARY_ADJACENT_SPARSE`.

## Correction 2 — Search architecture

Separated:

- core Graph-KT query `Q-G`;
- core SSL-KT query `Q-S`;

from supplementary:

- sparse/cold-start query `Q-P`;
- reliability query `Q-R`.

This makes search logic match the frozen title and scope.

## Correction 3 — Screening labels

Added:

```text
PRIMARY_ADJACENT_SPARSE
PRIMARY_ADJACENT_METHOD
```

so contextual evidence is not mixed with primary Graph/SSL evidence.

## Correction 4 — Inter-rater plan

Replaced the vague “20–30%” plan with a locked minimum:

- 25% random title/abstract double-screen;
- all uncertain title/abstract records receive second review;
- at least 25% of full-text decisions double-screened;
- all full-text exclusions/uncertain decisions receive second review;
- coding double-check of `max(20 papers, 25% of PRIMARY_CORE)` subject to corpus size.

## Correction 5 — Quality-score normalization

Added applicable-item normalization so papers without sparse/cold-start claims are not automatically penalized on QA7.

## Correction 6 — PRISMA accounting

Separated final counts for:

- primary core;
- adjacent sparse;
- adjacent method;
- background/foundational.

## Correction 7 — Cutoff-update rule

Added the requirement that extending the publication cutoff must trigger a systematic update across all databases rather than opportunistic insertion of later papers.

---

# 34. Protocol lock decision

**SLR_PROTOCOL_v1.0 is approved for execution.**

Next methodological gate:

```text
included_papers_seed.csv
```

should now be audited against the frozen scope and RQs, but it remains a **seed corpus only**.

The next operational task after seed-corpus audit is:

```text
coding_codebook.md
```

pilot testing and freeze as `coding_codebook_v1.0_LOCKED.md`.
