# PILOT_CODING_PLAN_v1.0

## Status
**Approved pilot design — codebook is NOT yet frozen.**

## Pilot size
**15 papers**

## Selection logic
The pilot is purposive rather than random. It is designed to stress-test every difficult boundary in the locked scope and protocol.

### Composition
- Graph-KT core: 7 papers
- SSL / Graph+SSL core: 4 papers
- Sparse/inductive core or adjacent: 2 papers
- Boundary/background/exclusion cases: 2 papers

Note: some papers belong to more than one methodological family; the composition is based on their primary pilot role.

## Selected papers

| # | ID | Seed class | Primary pilot role | Why selected |
|---:|---|---|---|---|
| 1 | KT004 | PRIMARY_CORE | Graph source | Seminal explicit Graph-KT; tests basic graph-source, representation, GNN, and fusion fields. |
| 2 | KT010 | PRIMARY_CORE | Graph representation | Tests question–concept interaction graph and graph–sequence integration. |
| 3 | KT014 | PRIMARY_CORE | Prerequisite direction | Tests prerequisite semantics, directionality, and graph-provenance/leakage coding. |
| 4 | KT026 | PRIMARY_CORE | Graph gateway | Boundary case: graph-derived pretraining/question embeddings; tests Graph-KT vs generic pretraining distinction. |
| 5 | KT035 | PRIMARY_CORE | Heterogeneous nodes/edges | Tests heterogeneous multi-node graph coding and typed relations. |
| 6 | KT037 | PRIMARY_CORE | Concept map | Tests externally supplied concept-map/curriculum structure and fixed-graph provenance. |
| 7 | KT038 | PRIMARY_CORE | Dynamic graph | Tests dynamic/temporal graph coding and metadata-conflict workflow. |
| 8 | KT039 | PRIMARY_CORE | Sequence contrastive SSL | Pure sequence-level contrastive KT; tests SSL coding when graph_source = NONE. |
| 9 | KT011 | PRIMARY_CORE | Graph contrastive SSL | Graph + contrastive learning; tests hybrid Graph/SSL coding and augmentation fields. |
| 10 | KT042 | PRIMARY_CORE | Hypergraph | Heterogeneous hypergraph + self-supervision; stress-tests graph representation + SSL objective interaction. |
| 11 | KT066 | PRIMARY_CORE | Hypergraph | Modern hypergraph + cross-view contrastive learning; tests multi-view SSL and computational reporting. |
| 12 | KT044 | PRIMARY_CORE | Strict KC cold-start | Inductive/cold-start + semantic/LLM-assisted structure; stress-tests sparse ontology and external-information coding. |
| 13 | KT049 | PRIMARY_ADJACENT | Adjacent sparse/cold-start | PRIMARY_ADJACENT sparse/cold-start case; tests RQ4 contextual evidence without forcing Graph/SSL gateway. |
| 14 | KT041 | BACKGROUND | Sparse-attention ambiguity | Critical boundary case: k-sparse attention is not sparse-concept evidence. |
| 15 | KT055 | EXCLUDE | Task eligibility | Critical exclusion boundary: cognitive diagnosis enhanced by Graph-KT; tests KT-central-task eligibility. |


## Coding order

### Wave A — easy anchors
Code first:
- KT004
- KT039
- KT035
- KT014

Purpose: calibrate the obvious Graph-KT, SSL-KT, heterogeneous, and prerequisite cases.

### Wave B — Graph+SSL complexity
Then:
- KT011
- KT042
- KT066
- KT010
- KT037

Purpose: test hybrid Graph/SSL and provenance/fusion fields.

### Wave C — difficult modern cases
Then:
- KT038
- KT044
- KT026

Purpose: test dynamic graph, semantic/LLM-assisted inductive KT, and pretraining-vs-SSL boundaries.

### Wave D — boundary adjudication
Finally:
- KT049
- KT041
- KT055

Purpose: test adjacent sparse evidence, sparse-attention ambiguity, and cognitive-diagnosis exclusion.

## Two-coder procedure

1. Coder A and Coder B independently code all 15 papers.
2. Do not discuss individual values before both coders finish a paper.
3. Every nontrivial code must include `evidence_locator` and a short `evidence_note`.
4. Compare values field-by-field.
5. Enter disagreements in `pilot_disagreement_log.csv`.
6. Adjudicate only after the independent pass is complete.
7. If the same ambiguity appears in 3 or more papers, revise the codebook rather than resolving it ad hoc.
8. Recode all affected pilot papers after a substantive rule change.

## Pilot success criteria

The pilot passes when:
- primary-core/adjacent/background/exclude boundaries are consistently applied;
- Graph-KT vs relation-aware ambiguity is resolved;
- SSL vs generic pretraining ambiguity is resolved;
- paper/model/experiment levels work without duplication;
- graph provenance/leakage can be coded;
- strict KC cold-start and external unseen-KC information can be separated;
- sparse attention is not misclassified as sparse-concept evidence;
- LLM semantic support is not automatically coded as the temporal backbone;
- no recurring unresolved category remains;
- inter-rater agreement is acceptable for the key categorical dimensions.

## Important

These 15 papers are selected **for codebook validation**, not because they are the “best 15” papers in the field and not because they are guaranteed to remain in the final PRISMA corpus.
