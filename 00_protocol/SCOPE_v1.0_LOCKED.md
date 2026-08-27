# SCOPE_v1.0_LOCKED.md

## Scope Lock for the Systematic Survey

### Official title

**Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda**

Version: **v1.0 — FROZEN**  
Scope-lock date: **2026-08-09**

> **Scope status:** FROZEN.  
> Any substantive change after this version must be recorded in `protocol_deviations.md`, including the date, reason, affected records, and whether previous screening/coding must be repeated.

---

# 1. Purpose and positioning

This paper is an **evidence-driven systematic survey** of two methodological streams in Knowledge Tracing (KT):

1. **Graph-Based Knowledge Tracing (Graph-KT)**; and
2. **Self-Supervised Learning for Knowledge Tracing (SSL-KT)**,

examined through the cross-cutting lens of **sparse-concept settings**.

The paper is **not** intended to be:

- a general history of all KT models;
- a general survey of educational graph learning;
- a general survey of self-supervised learning;
- a survey of learning-path recommendation;
- a benchmark-only paper.

Its central question is:

> **How are graph structure and self-supervised learning used in Knowledge Tracing, what evidence exists that they improve learning-state estimation under sparse-concept conditions, and how trustworthy is that evidence?**

The review will produce:

- a systematic corpus;
- a unified taxonomy;
- a sparse-concept terminology framework;
- a reliability/reproducibility audit;
- an evidence synthesis;
- and a research agenda.

A controlled reproduced benchmark may be included as **supporting evidence**, but it is not the primary unit of the systematic review.

---

# 2. Central review lens

The survey follows the analytical chain:

> **Graph provenance → graph representation → KT architecture/fusion → self-supervised objective → sparse-concept generalization → reliability/reproducibility → research agenda**

The phrase **“in Sparse-Concept Settings”** is a **review lens**, not a requirement that every primary paper must itself contain a sparse-KC experiment.

Therefore:

- Graph-KT papers without explicit sparse evaluation may still enter the primary corpus.
- SSL-KT papers without explicit sparse evaluation may still enter the primary corpus.
- Their relevance to sparse concepts is then assessed through coding and synthesis.
- A paper that studies sparsity but uses neither Graph-KT nor SSL-KT is **not automatically a primary-core paper**.

This rule prevents the survey from drifting into a general sparse-KT review.

---

# 3. Primary-corpus eligibility rule

A publication can enter the **primary systematic corpus** only if it satisfies:

## 3.1 Mandatory KT criterion

The paper must study **Knowledge Tracing or sequential learner-state estimation** as a central task.

AND

## 3.2 At least one methodological criterion

The paper must satisfy at least one of:

- **G-criterion:** Graph-Based KT;
- **S-criterion:** Self-Supervised KT.

Thus the primary-corpus rule is:

```text
PRIMARY = KT AND (GRAPH_BASED OR SELF_SUPERVISED)
```

Sparse-concept evidence is coded as an analytical dimension, not as an independent gateway.

---

# 4. Operational definition of Graph-Based KT

A paper satisfies the **G-criterion** when an explicit graph, hypergraph, or typed relational structure is **constructed, supplied, learned, or consumed by the KT model or its training objective**.

An eligible structure should normally be representable as:

```text
G = (V, E)
```

or, for typed/multi-relational cases,

```text
G = (V, E, R)
```

or an equivalent hypergraph / dynamic-graph formulation.

## 4.1 Eligible graph sources and forms

Examples include:

- prerequisite/dependency graphs;
- curriculum/concept maps;
- Q-matrix-derived graphs;
- question–concept bipartite graphs;
- concept–concept graphs;
- item–item graphs;
- co-occurrence graphs;
- similarity graphs;
- heterogeneous graphs;
- hypergraphs;
- hierarchical graphs;
- multi-relational graphs;
- session graphs;
- dynamic/temporal graphs;
- jointly learned graphs;
- semantic-text-derived graphs;
- LLM-assisted graphs, **only when an explicit graph structure is actually constructed or used**.

## 4.2 Boundary rule: relation-aware does not automatically mean graph-based

A paper is **not automatically Graph-KT** merely because it uses:

- pairwise similarity;
- attention bias;
- side information;
- relation embeddings;
- correlation scores;
- knowledge-aware features.

To satisfy the G-criterion, the structural relation must be operationalized as an explicit graph/hypergraph/edge structure or an equivalent graph-learning mechanism used by the KT system.

Ambiguous cases are coded `SCREEN_FULL_TEXT` or `GRAPH_ADJACENT` until the full method is inspected.

---

# 5. Operational definition of Self-Supervised KT

A paper satisfies the **S-criterion** when it uses an auxiliary or pretraining objective whose target/supervision is derived from the observed data structure itself rather than requiring additional human-provided outcome labels beyond the KT observations.

Eligible families include:

- sequence contrastive learning;
- graph contrastive learning;
- multi-view contrastive learning;
- masked interaction prediction;
- masked concept/skill prediction;
- masked graph modeling;
- graph reconstruction;
- relation/edge prediction;
- generative reconstruction;
- teacher–student/self-distillation objectives;
- augmentation-free consistency learning;
- hybrid supervised + SSL objectives.

## 5.1 SSL boundary rules

The following do **not** automatically qualify as SSL:

- dropout;
- ordinary L1/L2 regularization;
- supervised multi-task learning using additional labeled targets;
- generic transfer learning;
- generic embedding initialization;
- generic pretraining without a clearly self-supervised objective;
- data augmentation alone without an SSL/pretext/consistency objective.

When the authors use the term “self-supervised” but the objective does not meet this operational definition, preserve the authors’ terminology in notes but code the method according to the review’s operational rule.

---

# 6. Sparse-concept settings: analytical definition

The survey treats **concept sparsity** as a family of data-support and generalization conditions involving knowledge components (KCs), skills, or concepts.

The review **does not impose one universal numerical frequency threshold on the literature**.

Each paper is coded using:

1. the paper’s original sparsity definition;
2. the numerical threshold/rule, if any;
3. the data partition used to compute that threshold;
4. the type of sparsity/generalization condition;
5. the support counts reported for evaluation.

## 6.1 Controlled sparse-concept vocabulary

Use:

- `LOW_FREQUENCY_KC`
- `LONG_TAIL_KC`
- `STRICT_KC_COLD_START`
- `LOW_DEGREE_GRAPH_NODE`
- `ITEM_COLD_START`
- `LEARNER_COLD_START`
- `SHORT_HISTORY`
- `GENERIC_DATA_SPARSITY`
- `SPARSE_ATTENTION_ARCHITECTURE`
- `MULTIPLE`
- `NO_EXPLICIT_FOCUS`
- `UNCLEAR`

## 6.2 Critical distinctions

### Low-frequency KC
The KC appears in the training data but has limited support.

### Strict KC cold-start
The KC has **zero training-interaction exposure** under the stated split.

External information may still be available, such as:

- prerequisite neighbors;
- curriculum metadata;
- text/semantic descriptions;
- pretrained semantic embeddings.

These sources must be coded separately because strict interaction cold-start is not the same as zero-information cold-start.

### Low-degree graph node
A graph-structural condition. It is related to, but not identical to, low interaction frequency.

### Item cold-start
A new item/exercise condition. It is not equivalent to unseen KC.

### Learner cold-start
A new learner or minimal-history condition. It is not equivalent to sparse KC.

### Sparse attention
An architectural/computational sparsity mechanism. It is **not** evidence of sparse-concept modeling unless the paper separately evaluates low-frequency or unseen KCs.

---

# 7. Sparse-only KT papers

A KT paper that directly studies concept sparsity/cold-start but satisfies neither the G-criterion nor the S-criterion is coded as:

```text
PRIMARY_ADJACENT_SPARSE
```

Such papers may be used to:

- define sparse/cold-start terminology;
- compare evaluation protocols;
- identify non-graph/non-SSL solutions;
- support the Research Agenda.

However, they are **not counted as primary Graph-KT/SSL-KT evidence** when synthesizing RQ1–RQ3.

This distinction should be preserved in corpus counts and tables.

---

# 8. Corpus tiers

Every included publication must receive exactly one main corpus tier.

## Tier A — `PRIMARY_CORE`

KT + Graph-Based and/or Self-Supervised criterion.

Examples:

- Graph-KT;
- SSL-KT;
- Graph + SSL KT;
- Graph/SSL KT with sparse/cold-start evaluation.

## Tier B — `PRIMARY_ADJACENT`

KT papers needed to interpret the primary scope but not themselves Graph/SSL core evidence.

Examples:

- sparse/cold-start KT without Graph/SSL;
- reliability/calibration KT papers;
- closely related inductive KT.

## Tier C — `BACKGROUND`

Used for foundations or positioning.

Examples:

- BKT;
- DKT;
- DKVMN;
- SAKT;
- AKT;
- simpleKT;
- general KT surveys;
- general GNN/GAT/Transformer/graph SSL methods;
- dataset papers;
- calibration/statistical methodology.

## Tier D — `EXCLUDE`

Fails the final scope criteria.

---

# 9. Background-only scope

The following may be retained as background but do not count as primary Graph/SSL evidence unless they independently satisfy the primary criteria:

- classical KT;
- sequence-only KT baselines;
- prior KT surveys;
- generic GNN/GAT/hypergraph foundations;
- generic contrastive/self-supervised learning foundations;
- calibration methods;
- statistical-test methodology;
- reproducibility/leakage methodology;
- dataset/toolkit papers;
- prerequisite-relation discovery without KT;
- educational recommendation without KT.

---

# 10. Learning Path Recommendation boundary

**Learning Path Recommendation (LPR)** is a downstream frontier and Research Agenda topic.

A paper is **not included in the primary corpus merely because it recommends learning paths**.

If an LPR paper independently satisfies the primary rule:

```text
KT AND (GRAPH_BASED OR SELF_SUPERVISED)
```

then it may enter the primary corpus based on its KT methodology. Its path-recommendation component is coded as a downstream application.

Otherwise it is coded:

```text
DOWNSTREAM_BACKGROUND
```

The survey will not make causal claims that better KT automatically implies better learning-path outcomes.

---

# 11. Out of scope

Exclude from the primary corpus when the paper is primarily:

- cognitive diagnosis without sequential KT;
- generic recommendation without KT;
- pure learning-path planning without central KT;
- generic educational graph mining without learner-state prediction;
- generic GNN/graph SSL without a KT application;
- generic LLM tutoring/chatbot research without KT state estimation;
- pure prerequisite discovery without KT;
- generic student-performance prediction not framed as KT/sequential learner-state modeling;
- “sparse attention” work with no concept-sparsity/generalization relevance to this survey’s primary methodological streams;
- editorials, tutorials, patents, posters, dissertations/theses, or short abstracts used as primary evidence;
- records with insufficient methodological detail to determine eligibility after reasonable full-text inspection.

Such items may still be cited as background where scientifically necessary.

---

# 12. Publication type and language

## Primary corpus

Prefer:

- peer-reviewed journal articles;
- peer-reviewed full conference papers;
- English-language full text;
- sufficient methodological detail for coding.

## Preprints

Preprints may be:

- tracked for update-search completeness;
- used to identify emerging directions;
- cited when no peer-reviewed version exists and the status is clearly labeled.

When a peer-reviewed version exists, that version takes precedence.

Preprints should not be mixed with peer-reviewed studies without an explicit publication-status field.

---

# 13. Time window

## Main systematic search

**2015-01-01 to 2026-07-31**

Rationale:

- 2015 marks the modern deep-KT transition;
- the period covers contemporary Graph-KT and SSL-KT development;
- the month-end cutoff provides a reproducible search boundary.

## Historical foundations

Pre-2015 papers may be retained as:

```text
FOUNDATIONAL_BACKGROUND
```

They do not enter the modern primary-corpus count unless the protocol is later formally amended.

## Final update search

Repeat all core database searches within **2–4 weeks before submission**.

If papers published after 2026-07-31 are added during the update search, the final manuscript must:

1. update the stated cutoff date;
2. rerun all relevant database searches to the same cutoff;
3. update PRISMA counts;
4. document the protocol amendment.

Do not add isolated later papers opportunistically while keeping the old cutoff.

---

# 14. Unit of analysis

The review uses two linked units.

## 14.1 Paper-level unit

One canonical bibliographic publication.

## 14.2 Model-entry unit

A paper may generate multiple model entries only when the models differ substantively in at least one of:

- graph source/construction;
- graph representation;
- graph encoder;
- KT temporal backbone;
- graph–sequence fusion;
- SSL objective;
- SSL training mode;
- sparse/cold-start protocol.

Do **not** create separate model entries for:

- random seeds;
- hidden dimensions;
- learning rates;
- ordinary ablations;
- repeated runs;
- dataset-specific checkpoints.

---

# 15. Evidence classes

Every substantive statement in the manuscript should be attributable to one of:

- `LIT_REPORTED` — directly reported in an original study;
- `LIT_SYNTHESIZED` — synthesized from multiple coded studies;
- `REPRODUCED` — generated by the survey authors under a controlled benchmark;
- `AGENDA_INFERENCE` — future direction inferred from systematic evidence gaps.

## Cross-paper metric rule

Original-paper AUC/ACC/NLL/ECE values must not be presented as a direct league table unless the underlying protocols are sufficiently matched.

Differences that may invalidate direct ranking include:

- dataset version;
- preprocessing;
- multi-skill handling;
- split protocol;
- graph construction;
- sequence truncation;
- tuning budget;
- metric implementation;
- test set.

---

# 16. Reliability dimensions within scope

Reliability is an analytical dimension, not an independent title-level corpus.

For each primary paper, code where applicable:

- train/validation/test split type;
- graph provenance;
- train-only graph construction;
- temporal leakage control;
- sparse-threshold provenance;
- support counts;
- number of seeds;
- confidence intervals;
- statistical tests;
- multiple-comparison correction;
- effect size;
- calibration metrics;
- code/configuration availability;
- hardware;
- training time;
- memory;
- scalability evidence.

A paper is not excluded solely because these items are missing; instead, missing items reduce confidence in the strength of evidence.

---

# 17. Controlled reproduced benchmark boundary

If the survey contains a reproduced benchmark, it must remain methodologically separate from the SLR corpus.

The benchmark may be used to test selected patterns such as:

- sequence-only vs graph-based KT;
- train-only vs leakage-prone graph construction;
- supervised vs self-supervised objectives;
- overall vs sparse-KC performance;
- discrimination vs calibration;
- performance vs computational cost.

The benchmark must **not** be used to redefine which literature papers are included.

---

# 18. Core contributions targeted by the survey

The survey targets five contributions.

## C1 — Unified taxonomy

A taxonomy connecting:

- graph provenance;
- graph representation;
- KT temporal backbone;
- graph–sequence fusion;
- SSL objective;
- sparse/generalization setting.

## C2 — Sparse-concept terminology framework

A formal separation among:

- rare/low-frequency KCs;
- strict unseen-KC conditions;
- low-degree graph nodes;
- item cold-start;
- learner cold-start;
- short histories;
- sparse-attention architectures.

## C3 — Reliability and reproducibility audit

An audit of:

- leakage control;
- split design;
- calibration;
- statistical rigor;
- reproducibility;
- computational reporting.

## C4 — Evidence synthesis

A synthesis of:

- when graph structure helps;
- when SSL helps;
- where evidence under sparse concepts is strong;
- where results are inconsistent or under-supported.

## C5 — Research agenda

Evidence-derived priorities including:

- leakage-controlled graph construction;
- prerequisite-aware SSL;
- inductive sparse-KC representation;
- noisy-graph uncertainty;
- calibrated sparse-KC prediction;
- dynamic/multi-relational graph learning;
- scalable KT;
- reproducible evaluation;
- downstream prerequisite-valid learning-path recommendation.

---

# 19. Explicit scope decisions — LOCKED

The following decisions are now frozen:

1. **The survey is not a general KT survey.**
2. **Primary corpus requires KT + (Graph-Based OR Self-Supervised).**
3. **Sparse-concept settings are a cross-cutting analytical lens, not an independent primary-corpus gateway.**
4. **Sparse-only KT may enter an adjacent corpus but not primary Graph/SSL evidence.**
5. **Relation-aware does not automatically mean Graph-Based KT.**
6. **Regularization/pretraining does not automatically mean Self-Supervised KT.**
7. **Sparse attention is not equivalent to sparse KCs.**
8. **Strict KC cold-start means zero training-interaction exposure; external structural/semantic information must be coded separately.**
9. **Learning Path Recommendation is downstream, not a primary survey axis.**
10. **Reliability and scalability are coded dimensions; missing reporting lowers evidence strength but does not automatically exclude a paper.**
11. **Primary modern search window is 2015-01-01 to 2026-07-31 unless formally amended.**
12. **Peer-reviewed full papers are the default primary evidence.**
13. **Paper-level and model-entry-level units remain separate.**
14. **Reported literature evidence and reproduced benchmark evidence remain separate.**
15. **Cross-paper performance values are not naïvely ranked under unmatched protocols.**

---

# 20. Scope-change procedure after v1.0

A substantive scope change is any change to:

- title;
- primary-corpus rule;
- Graph-Based KT definition;
- Self-Supervised KT definition;
- sparse-concept ontology;
- publication types;
- time window;
- LPR boundary;
- corpus tiers;
- evidence classes.

For every such change, add an entry to:

```text
protocol_deviations.md
```

with:

```text
date
scope_version_before
scope_version_after
change
reason
affected_records
screening_repeated (yes/no)
coding_repeated (yes/no)
author_approval
```

Minor wording clarifications that do not change eligibility may be recorded as editorial revisions without changing the scope version.

---

# 21. Next gate

With `SCOPE_v1.0_LOCKED.md` frozen, the next artifact to review and lock is:

```text
RQs.md → RQs_v1.0_LOCKED.md
```

The RQs must be checked against this scope. In particular:

- RQ1–RQ3 must use `PRIMARY_CORE` evidence;
- RQ4 may use both `PRIMARY_CORE` and `PRIMARY_ADJACENT` sparse evidence, clearly labeled;
- RQ5 audits the primary corpus;
- RQ6 must be derived from coded gaps rather than predetermined conclusions.
