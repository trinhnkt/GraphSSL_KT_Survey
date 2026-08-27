# RQs_v1.0_LOCKED.md

## Research Questions — Scope-Aligned Frozen Version

### Official survey title

**Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda**

Version: **v1.0 — FROZEN**  
RQ-lock date: **2026-08-09**  
Parent scope: **SCOPE_v1.0_LOCKED.md**

> **Status:** FROZEN.  
> Any substantive modification to RQ wording, evidence source, corpus tier, or expected output must be recorded in `protocol_deviations.md`.

---

# 1. Design principle

These are **systematic-review research questions**, not model-development research questions.

They are designed to answer:

1. what the literature does;
2. how Graph-Based KT and Self-Supervised KT are technically organized;
3. how sparse-concept conditions are defined and evaluated;
4. how trustworthy the empirical evidence is; and
5. which future research directions are supported by identified evidence gaps.

The RQs must remain consistent with the frozen primary-corpus rule:

```text
PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)
```

Sparse-concept settings are a **cross-cutting analytical lens** rather than an independent gateway into the primary corpus.

---

# 2. Final Research Questions

## RQ1 — Graph construction, provenance, and leakage control

### Final wording

**RQ1. How are graph structures for Knowledge Tracing constructed, represented, and validated, and what data-provenance and leakage risks arise from these construction choices?**

### Purpose

RQ1 establishes **where educational structure comes from** before comparing graph architectures.

It prevents fundamentally different graph sources from being treated as if they were equivalent.

### Subquestions

**RQ1.1** Which graph sources are used?

- expert-defined prerequisite relations;
- curriculum/concept maps;
- Q-matrix-derived relations;
- interaction co-occurrence;
- similarity relations;
- jointly learned relations;
- semantic/text-derived relations;
- LLM-assisted relations;
- hybrid/multi-source relations.

**RQ1.2** Which graph representations are used?

- homogeneous graphs;
- bipartite graphs;
- heterogeneous graphs;
- hypergraphs;
- hierarchical graphs;
- multi-relational graphs;
- directed acyclic graphs;
- session graphs;
- dynamic/temporal graphs.

**RQ1.3** How are graph semantics encoded?

- direction;
- edge type;
- edge weight;
- confidence;
- temporal validity;
- prerequisite reachability.

**RQ1.4** What is the provenance of data-derived graphs?

- external/fixed;
- train-only inferred;
- jointly learned from training data;
- inferred from full data;
- unclear.

**RQ1.5** How is graph quality evaluated?

- edge ablation;
- graph-noise perturbation;
- cycle/direction audit;
- structural validity;
- expert validation;
- downstream sensitivity.

**RQ1.6** What leakage risks are created when graph construction uses information outside the training partition?

### Evidence base

Primary evidence:

```text
PRIMARY_CORE papers satisfying the G-criterion
```

Background evidence may support definitions only.

### Main outputs

- **Fig. 1:** Graph-provenance and graph-representation taxonomy.
- **Table 1:** Graph construction, provenance, directionality, and validation.
- **Audit:** `EXTERNAL_FIXED / TRAIN_ONLY / JOINT_TRAIN / FULL_DATA / UNCLEAR`.
- **Research-agenda input:** leakage-controlled graph construction.

---

## RQ2 — Graph-Based KT architectures and graph–sequence fusion

### Final wording

**RQ2. How do Graph-Based Knowledge Tracing models integrate structural representations with temporal learner-state modeling, and what architectural patterns and trade-offs emerge across graph families?**

### Purpose

RQ2 analyzes **how graph information enters the KT prediction process** after RQ1 establishes where the graph comes from.

### Subquestions

**RQ2.1** Which graph encoders are used?

- GCN;
- GAT;
- relational GNN;
- heterogeneous GNN;
- hypergraph encoder;
- temporal/dynamic GNN;
- graph memory;
- graph-attention hybrids;
- other graph operators.

**RQ2.2** Which temporal KT backbones are combined with graph representations?

- RNN/LSTM/GRU;
- memory networks;
- self-attention/Transformer;
- temporal graph-native models;
- state-space models;
- semantic/LLM-assisted encoders.

**RQ2.3** How is graph information fused with learner-sequence information?

- input-level initialization;
- concatenation;
- addition;
- gating;
- attention;
- cross-attention;
- message passing inside the prediction loop;
- joint latent-state learning;
- auxiliary regularization;
- late fusion;
- teacher–student transfer.

**RQ2.4** What structural families dominate the literature?

- static concept graphs;
- question–concept graphs;
- heterogeneous graphs;
- hypergraphs;
- multi-relational graphs;
- dynamic/temporal graphs;
- hierarchical/DAG structures.

**RQ2.5** Which architectural benefits are supported by matched ablations rather than only comparisons between unrelated models?

**RQ2.6** What computational or modeling trade-offs are reported for more complex graph structures?

### Evidence base

```text
PRIMARY_CORE papers satisfying the G-criterion
```

### Main outputs

- **Fig. 2:** Graph-KT architecture taxonomy.
- **Table 2:** Graph encoder × temporal backbone × fusion mechanism.
- **Table 3:** Static vs heterogeneous vs hypergraph vs dynamic graph evidence.
- **Research-agenda input:** scalable and multi-relational Graph-KT.

---

## RQ3 — Self-supervised objectives and educational structure preservation

### Final wording

**RQ3. Which self-supervised learning objectives and augmentation strategies are used in Knowledge Tracing, how are they integrated with supervised KT, and to what extent do they preserve educationally meaningful structure?**

### Purpose

RQ3 separates **self-supervised learning mechanisms** from ordinary regularization or generic pretraining.

It also tests a central conceptual issue of the survey: augmentation that is valid statistically may not be valid pedagogically.

### Subquestions

**RQ3.1** Which SSL families are used?

- sequence contrastive learning;
- graph contrastive learning;
- multi-view contrastive learning;
- masked interaction prediction;
- masked concept/skill prediction;
- masked graph modeling;
- graph reconstruction;
- relation/edge prediction;
- generative pretext objectives;
- self-distillation/teacher–student objectives;
- hybrid objectives.

**RQ3.2** At what level is the self-supervised target defined?

- sequence;
- interaction;
- item;
- KC/concept;
- node;
- edge;
- subgraph;
- learner state;
- multiple levels.

**RQ3.3** Which augmentations are applied?

- masking;
- cropping;
- reordering;
- interaction replacement;
- node masking/dropping;
- edge dropping/adding/reweighting;
- subgraph sampling;
- relation perturbation;
- difficulty-aware masking;
- frequency-aware masking;
- semantic perturbation.

**RQ3.4** What invariances are assumed by these augmentations?

**RQ3.5** Are prerequisite direction, hierarchy, edge type, reachability, or other educational semantics explicitly preserved?

**RQ3.6** How is SSL combined with supervised KT?

- pretrain then fine-tune;
- joint training;
- alternating optimization;
- teacher–student transfer;
- other.

**RQ3.7** Are SSL benefits demonstrated with a matched supervised-only counterpart?

### Evidence base

Primary evidence:

```text
PRIMARY_CORE papers satisfying the S-criterion
```

Graph+SSL papers contribute to both RQ1/RQ2 and RQ3 where applicable.

### Main outputs

- **Fig. 3:** SSL objective and augmentation taxonomy.
- **Table 4:** SSL family × target level × augmentation × training mode.
- **Table 5:** Educational structure-preservation audit.
- **Research-agenda input:** prerequisite-aware and structure-preserving SSL.

---

## RQ4 — Sparse-concept definitions, protocols, and evidence

### Final wording

**RQ4. In Graph-Based and Self-Supervised Knowledge Tracing research, how are sparse-concept and related cold-start conditions defined and evaluated, and what evidence supports generalization to low-support or unseen knowledge components?**

### Purpose

RQ4 makes **sparse-concept settings the cross-cutting analytical lens** promised by the title.

It must not redefine the primary corpus as a general sparse-KT corpus.

### Subquestions

**RQ4.1** What does “sparse” mean in the literature?

- low-frequency KCs;
- long-tail KCs;
- low-degree graph nodes;
- generic data sparsity;
- short learner histories;
- sparse attention;
- other meanings.

**RQ4.2** How are rare/low-frequency KCs operationalized?

- fixed count threshold;
- quantile threshold;
- learner-count threshold;
- graph-degree threshold;
- other.

**RQ4.3** On which partition is the sparse threshold computed?

- train only;
- train+validation;
- full data;
- unclear.

**RQ4.4** How is strict KC cold-start constructed?

A strict KC cold-start claim requires evidence that the KC has **zero interaction exposure in training** under the stated split.

**RQ4.5** What non-interaction information remains available for unseen KCs?

- graph neighbors;
- curriculum metadata;
- semantic text;
- pretrained embeddings;
- LLM-derived semantics;
- none;
- unclear.

**RQ4.6** Are the following clearly separated?

- KC cold-start;
- item cold-start;
- learner cold-start;
- short-history prediction;
- low-degree graph nodes;
- sparse-attention architecture.

**RQ4.7** Are support counts reported for sparse strata?

- number of KCs;
- learners;
- items;
- positive/negative labels;
- test interactions.

**RQ4.8** Which Graph-KT or SSL-KT methods provide credible evidence of improvement for low-support or unseen KCs?

### Evidence base

Primary synthesis:

```text
PRIMARY_CORE
```

Contextual comparison may additionally use:

```text
PRIMARY_ADJACENT_SPARSE
```

Adjacent sparse-only papers must be labeled separately and must not be counted as Graph/SSL evidence.

### Main outputs

- **Fig. 4:** Sparse-concept and cold-start terminology map.
- **Table 6:** Sparse/cold-start definitions and split protocols.
- **Table 7:** Sparse evidence support-count and reliability audit.
- **Research-agenda input:** inductive KC representation and standardized sparse evaluation.

---

## RQ5 — Reliability, reproducibility, calibration, and computational evidence

### Final wording

**RQ5. How reliable and reproducible is the empirical evidence for Graph-Based and Self-Supervised Knowledge Tracing, particularly with respect to data splitting, leakage control, uncertainty, calibration, statistical testing, artifact availability, and computational reporting?**

### Purpose

RQ5 evaluates **the strength of the evidence**, not merely model accuracy.

Calibration and scalability are analytical dimensions within RQ5; they are not independent primary-corpus gateways.

### Subquestions

**RQ5.1** Which split protocols are used?

- random interaction;
- learner-based;
- temporal;
- item cold-start;
- KC cold-start;
- cross-domain;
- k-fold/other.

**RQ5.2** Are preprocessing, graph construction, sparse-stratum construction, and normalization protected from validation/test leakage?

**RQ5.3** How many random seeds/runs are reported?

**RQ5.4** Are uncertainty estimates reported?

- standard deviation;
- confidence intervals;
- bootstrap intervals;
- other.

**RQ5.5** Are statistical comparisons appropriate and transparent?

- paired/unpaired design;
- test type;
- multiple-comparison correction;
- effect size.

**RQ5.6** Are probabilistic-quality and calibration metrics reported?

- NLL/log loss;
- Brier score;
- ECE;
- reliability diagrams;
- calibration slope/intercept.

**RQ5.7** Are sparse-stratum metrics accompanied by enough support to judge their reliability?

**RQ5.8** Which reproducibility artifacts are available?

- code;
- processed data;
- configuration;
- seeds;
- environment;
- predictions;
- archived releases.

**RQ5.9** What computational evidence is reported?

- parameters;
- training time;
- time per epoch;
- inference latency;
- throughput;
- CPU RAM;
- GPU VRAM;
- graph-construction time;
- scale-up behavior;
- OOM/timeout;
- hardware.

**RQ5.10** How should evidence strength be qualified when high predictive performance is reported without adequate protocol transparency or uncertainty estimates?

### Evidence base

Primary audit:

```text
ALL PRIMARY_CORE papers
```

Selected `PRIMARY_ADJACENT` papers may be used to contextualize calibration/sparse-evaluation methodology but are not included in primary-core reliability rates unless explicitly reported separately.

### Main outputs

- **Fig. 5:** Reliability and reproducibility heatmap.
- **Table 8:** Evaluation protocol and leakage audit.
- **Table 9:** Calibration/statistical reporting audit.
- **Table 10:** Reproducibility/computational reporting.
- **Research-agenda input:** minimum reporting standards for Graph/SSL KT.

---

## RQ6 — Evidence-derived research agenda

### Final wording

**RQ6. What unresolved research gaps emerge from the systematic evidence on Graph-Based and Self-Supervised Knowledge Tracing in sparse-concept settings, and what methodological and evaluation priorities should guide future research?**

### Purpose

RQ6 is **derived from the results of RQ1–RQ5**.

It must not be written as a predetermined list of the authors’ future PhD tasks.

### Subquestions

**RQ6.1** Which important graph-construction assumptions remain insufficiently validated?

**RQ6.2** Which educational relations are poorly protected by current SSL augmentations?

**RQ6.3** What prevents robust inductive generalization to low-support or unseen KCs?

**RQ6.4** Which evaluation practices most limit confidence in current claims?

**RQ6.5** Where are calibration, uncertainty, and sparse-stratum reliability under-reported?

**RQ6.6** Which graph architectures or SSL objectives have weak scalability evidence?

**RQ6.7** What role can semantic/LLM-assisted representations play without introducing contamination, hallucinated structure, or evaluation leakage?

**RQ6.8** Which standardized artifacts, benchmarks, and reporting practices would most improve comparability?

**RQ6.9** How can reliable KT estimates support prerequisite-valid learning-path recommendation without equating predictive accuracy with causal learning gain?

### Evidence base

RQ6 may use:

```text
LIT_SYNTHESIZED
+ quality/reliability audit results
+ clearly labeled REPRODUCED evidence
```

Every agenda item must be linked to an identified evidence gap.

### Main outputs

- **Fig. 6:** Research-agenda roadmap.
- **Table 11:** Evidence gap → consequence → recommended research action.
- **Checklist:** Minimum reporting standard for future Graph/SSL KT studies.

---

# 3. RQ-to-corpus mapping — LOCKED

| RQ | Primary corpus used | Adjacent/background use |
|---|---|---|
| RQ1 | `PRIMARY_CORE` satisfying G-criterion | definitions only |
| RQ2 | `PRIMARY_CORE` satisfying G-criterion | architecture foundations only |
| RQ3 | `PRIMARY_CORE` satisfying S-criterion | SSL foundations only |
| RQ4 | `PRIMARY_CORE` | `PRIMARY_ADJACENT_SPARSE` for contextual comparison |
| RQ5 | all `PRIMARY_CORE` | adjacent methodology reported separately |
| RQ6 | synthesis of RQ1–RQ5 | background may contextualize agenda |

This mapping must not be changed silently during manuscript writing.

---

# 4. RQ-to-taxonomy mapping — LOCKED

| Taxonomy axis | Main RQ |
|---|---|
| A. Graph source and provenance | RQ1 |
| B. Graph representation | RQ1–RQ2 |
| C. Temporal KT backbone | RQ2 |
| D. Graph–sequence fusion | RQ2 |
| E. SSL objective and augmentation | RQ3 |
| F. Sparse/generalization and reliability | RQ4–RQ5 |
| Research agenda | RQ6 |

---

# 5. RQ-to-core-contribution mapping — LOCKED

| Contribution | Evidence source |
|---|---|
| C1 Unified Graph/SSL taxonomy | RQ1–RQ3 |
| C2 Sparse-concept terminology framework | RQ4 |
| C3 Reliability/reproducibility audit | RQ5 |
| C4 Evidence synthesis | RQ1–RQ5 |
| C5 Research agenda | RQ6 |

---

# 6. RQ-to-controlled-benchmark mapping

The controlled benchmark is **supporting evidence only**.

It may test a limited subset of literature patterns:

| Benchmark question | Related RQ |
|---|---|
| Train-only graph vs leakage-prone graph | RQ1, RQ5 |
| Sequence-only vs graph-based KT | RQ2 |
| Supervised vs SSL | RQ3 |
| Overall vs sparse-KC performance | RQ4 |
| AUC vs NLL/ECE/Brier | RQ5 |
| Performance vs compute cost | RQ5 |

The benchmark must not create new primary RQs.

---

# 7. Important wording decisions — LOCKED

## 7.1 No causal wording for literature-only comparisons

Avoid:

> “Graph provenance causes performance differences.”

Use:

> “Reported performance varies with graph provenance, but causal attribution requires matched experiments.”

## 7.2 No universal sparse threshold in the RQ

RQ4 intentionally asks **how the literature defines sparsity** rather than imposing one threshold before synthesis.

## 7.3 No assumption that SSL is beneficial

RQ3 asks which SSL objectives are used and what evidence supports them. It does not assume that SSL improves KT.

## 7.4 No assumption that Graph-KT is superior

RQ2 describes patterns and trade-offs. Superiority claims require matched evidence.

## 7.5 Scalability remains within RQ5

Because the final paper title does not claim a dedicated scalability survey, computational cost and scalability remain part of the reliability/evidence audit rather than a standalone RQ.

## 7.6 Learning-path recommendation remains within RQ6

LPR is a downstream research-agenda issue, not a separate main RQ.

---

# 8. Final six-RQ short form for the manuscript

For the Introduction / Review Methodology, the RQs may be presented in the following concise form.

### RQ1
**How are graph structures for KT constructed, represented, validated, and protected against data-provenance and leakage risks?**

### RQ2
**How do Graph-Based KT models integrate graph representations with temporal learner-state modeling, and what architectural patterns and trade-offs emerge?**

### RQ3
**Which self-supervised objectives and augmentation strategies are used in KT, and to what extent do they preserve educationally meaningful structure?**

### RQ4
**How are sparse-concept and related cold-start conditions defined and evaluated in Graph-Based and Self-Supervised KT, and what evidence supports generalization to low-support or unseen KCs?**

### RQ5
**How reliable and reproducible is the empirical evidence for Graph-Based and Self-Supervised KT with respect to splitting, leakage, uncertainty, calibration, statistics, artifacts, and computational reporting?**

### RQ6
**What evidence-supported research agenda follows from the unresolved methodological and evaluation gaps identified across RQ1–RQ5?**

These short forms are the preferred versions for the main manuscript.

---

# 9. RQ freeze criteria — PASSED

The RQ set is now frozen because:

- [x] every RQ is compatible with `SCOPE_v1.0_LOCKED.md`;
- [x] RQ1–RQ3 use primary Graph/SSL evidence rather than sparse-only literature;
- [x] RQ4 treats sparse-concept settings as a cross-cutting lens;
- [x] RQ4 separates KC, item, learner, low-degree, and sparse-attention conditions;
- [x] RQ5 audits reliability without making reliability a corpus gateway;
- [x] scalability is retained as an evidence dimension rather than a title-level promise;
- [x] LPR remains downstream in RQ6;
- [x] RQ6 is explicitly derived from RQ1–RQ5 evidence;
- [x] each RQ maps to planned tables/figures/coding fields;
- [x] controlled benchmark evidence is separated from systematic-review evidence.

---

# 10. Next gate

With both scope and RQs frozen, the next artifact to audit and lock is:

```text
SLR_PROTOCOL.md → SLR_PROTOCOL_v1.0_LOCKED.md
```

The protocol must now be checked against:

- `SCOPE_v1.0_LOCKED.md`;
- `RQs_v1.0_LOCKED.md`;
- search-query coverage;
- inclusion/exclusion logic;
- screening labels;
- deduplication rules;
- PRISMA accounting;
- pilot coding and inter-rater reliability;
- final update-search procedure.
