# A3 — Screening reliability

**Date:** 2026-11-18
**A3_KAPPA_COMPUTED = NO**
**A3_PAIR_FILES_PRESENT = NO**
**Manuscript sections II-E and IX were not edited.**

The sentence in the manuscript remains true: the title/abstract and full-text pair files named in the protocol are not present. No screening κ was calculated. No second-screener label was created.

## What the locked protocol requires

`00_protocol/SLR_PROTOCOL_v1.0_LOCKED.md`, sections 20.1, 20.2, and 28. Read only. Not edited.

- Title/abstract: a second coder independently screens a 25% random sample of the deduplicated records, plus every record the first coder marked `UNCERTAIN`.
- Full text: a second reviewer checks every `EXCLUDE_FULLTEXT` and every full-text `UNCERTAIN`, and at least 25% of all full-text eligibility decisions are double-screened.
- Pair files named by the protocol: `inter_rater_screening.csv` and `inter_rater_fulltext.csv`.
- Report sample size, raw agreement, Cohen’s κ, disagreement categories, and the consensus procedure.

The reviewer note of 13/11/2026 (page 6) asks for a different draw: 25% of the 610 title/abstract exclusions (about 153 records, fixed seed) plus all 103 full-text exclusions, done by a person who is not an author. That draw also needs the row lists. Those lists are not in the repository, so neither sample was drawn.

## What is actually deposited

Counted 2026-11-18 from the CSV files.

| File | Rows | Screener | What it is not |
|---|---|---|---|
| `05_screening/title_abstract_screening_v1.0.csv` | 43 | `AI_ASSISTANT` on all 43 | Not the 750-row ledger. Not the 610 exclusions. Decisions: `INCLUDE_FULLTEXT` 42, `EXCLUDE_TITLE_ABSTRACT` 1. |
| `06_fulltext/fulltext_screening_v1.0.csv` | 48 | `AI_ASSISTANT` on all 48 | Not the 103 full-text exclusions. Tiers: `PRIMARY_CORE` 42, `PRIMARY_ADJACENT_SPARSE` 3, `PRIMARY_ADJACENT_METHOD` 1, `EXCLUDE_FULLTEXT` 1, `BACKGROUND` 1. |
| `04_deduplication/deduplication_audit_v1.0.csv` | 34 duplicate groups | — | Not the 1,267 duplicate removals. |
| `12_manuscript/TLT/supplementary/supplementary_prisma_exclusions.csv` | 48 | `AI_ASSISTANT` on all 48 | Same shape as the full-text file. Not 98 row-level EC1–EC7 exclusions. |

No file named `inter_rater_screening.csv` or `inter_rater_fulltext.csv` exists. The stage counts 2,017 → 750 → 140 → 37 stay report arithmetic, as the manuscript already says.

## Why κ is not reported

Cohen’s κ needs two independent labels on the same records. This repository has one screener label, `AI_ASSISTANT`, and it does not have the 610 or 103 records the reviewer named. Filling a second column from the first column, or sampling 153 exclusions from a file that contains one exclusion, would invent the reliability result. That was not done.

The coding κ values already in the manuscript (0.97 and 0.96 on the 20-paper sample) are coding agreement. They are not a screening κ. They were not recomputed and not pooled.

## What a real A3 still needs

1. The deposited row list of the deduplicated records, or of the 610 title/abstract exclusions and the 103 full-text exclusions. It is not in this repository.
2. A second screener who is not an author of the paper. That person screens without seeing the first decision. This assistant does not take that role.
3. After those labels exist, κ can be computed for each stage, disagreements adjudicated, and the pair files saved under the protocol names. Only then can sections II-E and IX report a screening κ.

## Stop

`A3_KAPPA_COMPUTED = NO`
