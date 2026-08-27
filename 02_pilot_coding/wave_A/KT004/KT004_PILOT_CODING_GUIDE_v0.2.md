# KT004_PILOT_CODING_GUIDE_v0.2

## Paper
**KT004 — Graph-Based Knowledge Tracing: Modeling Student Proficiency Using Graph Neural Network**

## Status
**Coder-A worked example for pilot coding. Not yet adjudicated.**

## Core decision
- `kt_central_task = Y`
- `G_criterion = Y`
- `S_criterion = N`
- `primary_gateway_pass = PASS`
- `corpus_status = PRIMARY_CORE`
- `role_in_survey = GRAPH_KT`

## Why six model rows?
Section 2.2 defines six substantively different graph-construction variants:
1. Dense Graph
2. Transition Graph
3. DKT Graph
4. Parametric Adjacency Matrix (PAM)
5. Multi-head Attention (MHA)
6. Variational Autoencoder (VAE)

Because the frozen codebook treats graph construction/provenance as a substantive model dimension, KT004 should be represented by six `model_entry_id` rows rather than one.

## Why twelve experiment rows?
Table 1 reports each of the six GKT variants on two datasets:
- ASSISTments 2009–2010 Skill Builder
- KDD Cup / Bridge to Algebra 2006–2007

Thus the worked example creates 6 × 2 = 12 proposed-model experiment rows.

## Important pilot findings
1. The Dense Graph exposes a missing `graph_provenance` value: a graph fixed by model design but not externally supplied and not data-inferred. Candidate: `MODEL_DEFINED_FIXED`.
2. The Transition Graph is based on ordered transitions, which is more precise than `CO_OCCURRENCE`. Candidate graph source: `SEQUENTIAL_TRANSITION`.
3. Field-level evidence provenance is needed; one `coding_basis` per model row is too coarse.
4. Filtering KCs answered fewer than 10 times is preprocessing, not evidence that the paper evaluates sparse KCs.

## Paper sections to read in order
1. Abstract + Introduction — confirm KT task and graph formulation.
2. Section 2.1 — architecture: Aggregate → Update → Predict.
3. Section 2.2 — six graph variants.
4. Section 3 + Table 1 — datasets, baselines, AUC results.
5. Appendix A + Table 2 — preprocessing and dataset statistics.
6. Appendix B — learner-based 8:1:1 split and hyperparameters.
7. Appendix C/D — graph analysis and interpretability only when coding claims/limitations.

## Workbook
See `KT004_pilot_coding_example_v0.2.xlsx`, especially:
- `Paper_Coding_KT004`
- `Model_Coding_KT004`
- `Experiment_Coding_KT004`
- `Field_Guide`
- `Codebook_Issues_KT004`
