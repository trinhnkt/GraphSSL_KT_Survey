# CURSOR — FINAL TARGETED FIX FOR IEEE TLT MANUSCRIPT
## H1 → H6: inspect, decide, edit only when evidence supports the change

Target manuscript:
**Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda**

Latest reviewed manuscript:
`Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings - A Systematic Survey and Research Agenda.pdf`

Target journal:
**IEEE Transactions on Learning Technologies (IEEE TLT)**

# MASTER RULE — DO NOT BLINDLY APPLY CHANGES

Before editing anything:

1. Read the active manuscript source.
2. Read the locked protocol/codebook.
3. Read all current paper-level/model-level/evidence coding files.
4. Read the final PRISMA/corpus count tables.
5. Read the latest QA table.
6. Read the reference/BibTeX source.

For every issue below, Cursor must first classify it as:

- `CONFIRMED_FIX` — current manuscript is wrong and evidence supports the correction.
- `KEEP_CURRENT` — current manuscript is already correct.
- `NEEDS_EVIDENCE` — evidence is insufficient; do not invent.
- `MOVE_TO_SUPPLEMENT` — correct but too detailed for main paper.
- `WORDING_ONLY` — no data change; scientific wording needs tightening.

Create first:

`audit/CURSOR_FINAL_FIX_DECISIONS.md`

with columns:

| Issue | Current manuscript | Evidence checked | Decision | Exact change | File/section |

Do not edit `_LOCKED` files.

# H1 — RE-AUDIT THE 14 SSL PAPERS BEFORE FREEZING NS=14

```text
TASK H1 — Verify every paper currently counted as SSL-KT.

Current manuscript reports:
NS = 14
NG∩S = 13

Do not assume these counts are correct because Table IV has 14 rows.

For every current SSL paper, verify the frozen S-criterion:
A paper qualifies as SSL only if it has a self-generated/pretext/consistency target derived from observed data structure.

For each paper record:
- Paper ID
- Model
- S_criterion = Y/N
- Self-generated target
- Pretext/consistency objective
- Loss function
- Training mode
- Evidence locator
- Evidence note

Pay particular attention to:
- KT044 SINKT
- KT070 Coda
- KT076 KGNN-KT
- KT077 R²GCurL
- KT079 STG-SKT

Do not infer SSL from:
- "inductive"
- "pretraining"
- "curriculum learning"
- "reinforcement learning"
- "dynamic graph"
- "LLM"
alone.

If any paper fails S_criterion:
1. remove it from the SSL corpus;
2. recompute NS;
3. recompute NG∩S;
4. update Abstract, Contributions, Fig. 2, Fig. 5, Table IV, Discussion, Conclusion.

If all 14 pass:
keep NS=14 and explicitly document the objective/target/loss evidence.

Create:
- `tables/H1_ssl_criterion_audit.csv`
- `audit/H1_SSL_CRITERION_DECISION.md`

STOP after H1.
```

Acceptance check:
Cursor must be able to answer:
“What exact self-generated target and objective makes each of the 14 papers SSL?”

# H2 — FIX QA7 APPLICABILITY AND RESTORE COMPLETE QUALITY TIERS

```text
TASK H2 — Re-evaluate QA7 applicability.

Current manuscript states that QA7 applies to all 37 papers because all use generic sparse interaction data.

Check whether this matches the locked protocol.

Distinguish:
1. `evaluation_support_regime`
2. `sparsity_claim`

A paper may use a generic interaction split but have:
`sparsity_claim = NO_EXPLICIT_FOCUS`.

If the locked codebook defines QA7 as claim-dependent/applicability-dependent, QA7 should be NA for such papers.

For each paper determine:
- explicit sparse/cold-start claim? Y/N
- QA7 applicable? Y/N
- QA7 score or NA
- evidence locator

Then recompute:
- raw score
- applicable maximum
- normalized score
- quality tier

Use:
HIGH >= 0.80
MODERATE = 0.55–0.79
LIMITED < 0.55

Do not delete LIMITED even if count = 0.

Update:
- Section II.D
- Section VI
- quality counts/mean
- any figure/table using QA results
- Conclusion only if aggregate changes

Create:
- `tables/H2_quality_recomputed.csv`
- `audit/H2_QA7_APPLICABILITY.md`

STOP after H2.
```

Decision rule:
If the locked protocol explicitly says QA7 is applicable only when sparse/cold-start is claimed, use NA elsewhere.
If the locked protocol explicitly says generic sparsity makes QA7 applicable to all, keep current treatment and document why.

# H3 — REBUILD PRIOR-SURVEY POSITIONING FOR NOVELTY

```text
TASK H3 — Strengthen Table II and novelty positioning.

Current Table II does not yet sufficiently distinguish this survey from the strongest recent KT/Graph-KT surveys.

Verify and, where supported, add:
1. Abdelrahman et al. — broad KT survey.
2. Shen et al. — IEEE TLT 2024 KT survey.
3. Liu et al. — IEEE TKDE 2025 deep-KT review/tool/empirical study.
4. Xu et al. — 2026 dedicated Graph-KT survey.

For every prior survey compare:
- systematic review protocol
- Graph-KT coverage
- SSL-KT coverage
- sparse/cold-start ontology
- graph provenance/split control
- calibration audit
- reproducibility/artifact audit
- empirical benchmark/tool component

Do not claim "first survey" unless a documented prior-work search proves it.

Preferred novelty wording:

"This survey jointly synthesizes Graph-Based and Self-Supervised KT through a sparse-concept lens, with explicit attention to graph provenance, split control, strict cold-start construct validity, calibration, and reproducibility."

Update:
- Introduction Section I.C
- Table II
- contribution wording
- Discussion if needed

Create:
- `tables/H3_prior_survey_comparison.csv`
- `audit/H3_NOVELTY_POSITIONING.md`

STOP after H3.
```

# H4 — CORRECT TABLE III: KT004 AND KT026

```text
TASK H4 — Fix remaining technical taxonomy errors in Table III.

PART A — KT004 / GKT

Current manuscript row mixes:
"GKT (Dense)"
with:
"Sequential transition"

This is inconsistent because Dense and Transition are distinct graph variants.

Preferred main-paper representation:
Model = GKT
Graph source = MULTIPLE_GRAPH_VARIANTS
Provenance = MULTIPLE
Encoder = GNN_GENERIC
Temporal = RNN/GRU

Move Dense / Transition / DKT Graph / PAM / MHA / VAE details to Supplementary.

Do not write "GKT (Dense)" together with "Sequential transition".

PART B — KT026 / PEBG

Check the original PEBG paper and current codebook.

Do not label the encoder as GCN unless the paper explicitly uses a GCN.

Use a label consistent with the actual method, e.g.:
- `NONE / PNN PRETRAINING`
or
- a codebook-compatible product-based neural pretraining label.

Keep:
- graph/bipartite relation use
- two-stage pretraining
- actual reconstruction/relation objectives

Update:
- Table III
- graph-encoder count if KT026 changes category
- Fig. 4 if the encoder distribution changes
- Supplementary model-entry table

Create:
- `audit/H4_KT004_KT026_TABLEIII_FIX.md`

STOP after H4.
```

# H5 — COMPLETE REFERENCE AUDIT AND FIX EQUATION / NOTATION ISSUES

```text
TASK H5 — Final metadata and notation audit.

PART A — References

Verify every reference against official publisher/DOI metadata.

At minimum recheck:
- Shen et al. 2024 IEEE TLT survey
- STG-SKT 2026
- KGNN-KT 2025
- all 2025–2026 references
- all papers added to Table II

Correct:
- authors
- title
- venue
- year
- volume/issue
- pages/article number
- DOI

Do not trust prior manuscript metadata if official metadata disagrees.

PART B — Equation 8

Current rendering must not appear as:
`K/cold`

Use either:
KC(x_t) ∉ K_cold
or:
KC(x_t) ∈ K \ K_cold

Ensure the PDF renders correctly.

PART C — notation collision

The paper already uses `X_{1:T}` for interaction history.
Avoid reusing `X` as the causal treatment variable.

Rename the treatment variable, e.g.:
A = treatment/intervention/exposure

and update Eq. 11 plus surrounding text consistently.

PART D — hyperbolic wording

Replace:
"prevents exponential representation distortion"

with:
"may better accommodate hierarchical structure with lower representational distortion"

Create:
- `audit/H5_REFERENCE_NOTATION_AUDIT.md`
- updated bibliography

STOP after H5.
```

# H6 — FINAL TLT POLISH AND SUBMISSION GATE

```text
TASK H6 — Final scientific and TLT compliance pass.

Run only after H1–H5 are complete.

1. Recompute and verify:
   N_CORE
   N_G
   N_S
   N_G_AND_S
   strict KC cold-start count
   item cold-start count
   QA tier counts

2. Check denominator consistency across:
   Abstract
   Contributions
   Table II
   Table III
   Table IV
   Table V
   Figures 1–5
   Section VI
   Discussion
   Research Agenda
   Conclusion

3. Reduce Index Terms to 5 unless the current TLT template explicitly permits more.

Suggested:
- Knowledge Tracing
- Educational Data Mining
- Graph Neural Networks
- Self-Supervised Learning
- Intelligent Tutoring Systems

4. Check AI disclosure:
- If AI was used only for copy-editing/LaTeX formatting, state exactly that.
- If AI generated or materially revised scientific content, expand the disclosure so it accurately reflects actual use.
Do not understate the role of AI.

5. Final language rules:
- no "first" without evidence
- no "consistently improves" across unmatched studies
- no "prevents representation collapse"
- no chance/random-guess claim unless reproduced or directly supported
- no leakage percentage without coded evidence
- no cross-paper AUC league table

6. Produce final gate table:

| Check | Status | Source evidence | Manuscript location | Remaining risk |

7. Final status must be one of:
`READY_FOR_SUBMISSION`
or
`NOT_READY_FOR_SUBMISSION`

Create:
- `audit/H6_FINAL_TLT_GATE.md`
- final source
- final PDF

STOP.
Do not submit automatically.
```

# EXECUTION ORDER

Run exactly:

H1 → H2 → H3 → H4 → H5 → H6

Recommended human review:
- after H1: approve final SSL corpus
- after H2: approve QA rule
- after H3: approve novelty positioning
- after H5: approve bibliography
- after H6: decide submission
