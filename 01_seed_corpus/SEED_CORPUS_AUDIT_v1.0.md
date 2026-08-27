# SEED_CORPUS_AUDIT_v1.0

## Survey
**Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda**

## Status
This is a **seed-corpus audit**, not the final systematic-review corpus.

## Classification after applying the frozen protocol

| Seed class | Count |
|---|---:|
| PRIMARY_CORE | 34 |
| PRIMARY_ADJACENT | 5 |
| BACKGROUND | 35 |
| EXCLUDE | 1 |
| **Total** | **75** |

Rows whose old preliminary label differs from the new four-class seed decision: **46**.

## Important corrections discovered during audit

- **KT026** was upgraded to `PRIMARY_CORE`: its full text explicitly formulates question–skill relations as a **bipartite graph** for KT.
- **KT019 (RKT)** remains `BACKGROUND`: relation-aware self-attention does not automatically satisfy the frozen Graph-Based KT criterion.
- **KT030 (DHKT)** remains `BACKGROUND`: hierarchy is modeled by an embedding hinge-loss relation rather than an explicit Graph-KT mechanism under the frozen scope.
- **KT041 (SparseKT)** remains `BACKGROUND`: “sparse” refers to k-sparse attention, not automatically sparse KCs.
- **KT044 (SINKT)** is `PRIMARY_CORE`: it constructs a heterogeneous concept–question graph and studies inductive/cold-start behavior.
- **KT051** is `PRIMARY_ADJACENT`: highly relevant to sparse KT/data augmentation, but not currently Graph-KT/SSL-KT under the locked definitions.
- **KT060 (STHKT)** is `PRIMARY_CORE`: it combines topological Hawkes processes with graph neural networks.
- **KT062 (LGS-KT)** is `PRIMARY_CORE`: available source evidence indicates a graph based on knowledge-concept similarity.
- **KT068 (HKT)** is `PRIMARY_CORE`: available source evidence indicates hierarchical/cross-graph modeling and contrastive learning.
- **KT055 (GKT-CD)** is provisionally `EXCLUDE` because cognitive diagnosis appears to be the central task; perform one full-text check before permanent removal.

## Rule that remains binding

`PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)`

Sparse-only or evaluation-only KT papers may be `PRIMARY_ADJACENT`; foundational/baseline/prior-survey/downstream papers are `BACKGROUND`.

## Next step

Do **not** freeze these 75 as the final corpus. Use them for:

1. pilot coding;
2. known-paper recall checks for Q-G/Q-S searches;
3. full-text boundary checks;
4. metadata/DOI audit.

The final systematic corpus must be generated from the locked SLR search, deduplication, and screening logs.
