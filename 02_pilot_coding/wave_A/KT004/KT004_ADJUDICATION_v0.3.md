# KT004_ADJUDICATION_v0.3

## Status

**Adjudicated for pilot codebook development.**

This adjudication compares the existing Coder-A worked example with an **AI second-pass coding**. It is useful for codebook debugging, but it is **not formal independent human inter-rater reliability**.

## Consensus decisions

1. **Accept `MODEL_DEFINED_FIXED`** as a new `graph_provenance` value.
   - Rationale: GKT-Dense prescribes a fixed graph by model design; it is neither external knowledge nor inferred from data.

2. **Accept `SEQUENTIAL_TRANSITION`** as a new `graph_source` value.
   - Rationale: GKT-Transition uses ordered one-step transitions between concepts. This is more precise than generic co-occurrence.

3. **Accept a required field-level evidence table.**
   - Required schema:
     `evidence_id, entity_level, entity_id, field_name, coded_value, coding_basis, evidence_locator, evidence_note, source_url, coder_id, coder_type, coder_confidence, adjudication_status`

4. **Clarify `directed`.**
   - `directed` refers to graph-topology directionality.
   - Direction-specific message functions belong in `message_passing_direction`.

5. **Clarify `typed_edges`.**
   - `typed_edges=Y` only when multiple distinguishable edge/relation categories are modeled.
   - Incoming/outgoing processing alone does not create semantic edge types.

6. **QA6 consensus = 0 for KT004.**
   - No author-released reproducibility artifact is reported in the paper.
   - A third-party implementation does not earn author-artifact credit.

7. **Keep six model entries for KT004.**
   - Dense, Transition, DKT Graph, PAM, MHA, and VAE are substantively different graph-construction/provenance variants.

## Consensus topology details

- Dense: directed=N, typed_edges=N.
- Transition: directed=Y, typed_edges=N.
- DKT Graph: directed=Y, typed_edges=N.
- PAM: directed=Y, typed_edges=N.
- MHA: directed=Y, typed_edges=N.
- VAE: directed=Y, typed_edges=Y.

## Next action

Apply these decisions in `coding_codebook_v0.3_PILOT.md`, then code the remaining Wave-A papers:
KT039 → KT035 → KT014.
