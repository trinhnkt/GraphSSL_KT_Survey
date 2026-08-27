---
name: systematic-survey-coding
description: Codes Knowledge Tracing papers for the Graph-Based and Self-Supervised KT systematic survey using PAPER/MODEL/EXPERIMENT levels and field-level evidence.
---

# Systematic survey coding

## Use when

Use this skill when coding one included or pilot KT paper.

## Procedure

1. Read `00_protocol/coding_codebook_v0.3_PILOT.md` or the newest version.
2. Confirm paper identity and publication status.
3. Determine KT centrality.
4. Determine G-criterion and S-criterion independently.
5. Create PAPER record.
6. Split substantively different models into MODEL entries.
7. Split dataset/split/protocol combinations into EXPERIMENT entries.
8. Create field-level evidence records.
9. Record `NR/NA/UNCLEAR/TBD_VERIFY` explicitly.
10. Log any codebook gap without inventing a new category ad hoc.

## Critical distinctions

- relation-aware ≠ automatically graph-based;
- generic pretraining ≠ automatically SSL;
- sparse attention ≠ sparse KC;
- graph-based KT may have `gnn_encoder=NONE`;
- third-party code ≠ author artifact;
- repeated resampling ≠ random seeds.
