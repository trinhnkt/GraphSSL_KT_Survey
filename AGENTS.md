# Agent instructions — GraphSSL_KT_Survey_2026

## Mission

Support the systematic survey:

**Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda**

Work as a research-engineering assistant. Preserve methodological traceability and do not optimize for producing a large number of coded rows.

## Source of truth

Always read:
- `00_protocol/SOURCE_OF_TRUTH.md`
- `CURRENT_STATUS.md`
- `NEXT_TASK.md`

Locked files:
- `00_protocol/SCOPE_v1.0_LOCKED.md`
- `00_protocol/RQs_v1.0_LOCKED.md`
- `00_protocol/SLR_PROTOCOL_v1.0_LOCKED.md`

Never edit locked files unless the user explicitly approves a protocol change and an entry is added to `00_protocol/protocol_deviations.md`.

Current codebook:
- `00_protocol/coding_codebook_v0.3_PILOT.md`
- status: PILOT, not frozen.

## Research rules

1. Do not fabricate paper metadata, methods, datasets, metrics, statistics, code availability, or results.
2. Prefer primary sources: publisher/proceedings full text, author-hosted accepted manuscript, official author repository.
3. If only an abstract is available, code only what that abstract supports and mark `coding_completeness`.
4. Do not treat author code as identical to manuscript-reported protocol unless verified.
5. Do not treat third-party code as an author reproducibility artifact.
6. `PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)`.
7. Sparse-concept settings are a cross-cutting lens, not an independent primary-corpus gateway.
8. Sparse attention is not sparse-KC evidence by itself.
9. Strict KC cold-start means zero training-interaction exposure; external graph/semantic information must be coded separately.
10. Graph-Based KT does not require a GNN if an explicit graph is a central structural mechanism.
11. Cross-paper AUC/ACC values are not a league table unless protocols are matched.
12. Keep `LIT_REPORTED`, `LIT_SYNTHESIZED`, `REPRODUCED`, and `AGENDA_INFERENCE` separate.

## Coding structure

Use three linked levels:
- PAPER
- MODEL
- EXPERIMENT

For nontrivial fields, maintain field-level evidence:
`entity_id + field_name + coded_value + coding_basis + evidence_locator + evidence_note + source`.

## File safety

Do not overwrite existing evidence artifacts.
Create versioned outputs.
Use `_DRAFT`, `_PILOT`, `_LOCKED`, or semantic version suffixes.
Before deleting or renaming a research artifact, ask for explicit approval.

## Current execution boundary

Do not mass-code the seed corpus yet.
First resolve Wave-A codebook candidates CB13–CB17, then continue the pilot.
