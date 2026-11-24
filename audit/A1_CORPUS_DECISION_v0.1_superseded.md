# A1 — Corpus decision (A1.1–A1.7)

**Date:** 2026-11-13  **Prepared by:** AI research assistant (Cursor). Not a human screening decision.
**Scope:** audit only. No manuscript, locked, search-log or corpus file was changed. No count was changed.

## 0. Final status

```text
A1_CORPUS_FROZEN = NO
```

**Why NO (all four are blocking):**
1. The raw exports (2,017 records) and a 750-row deduplicated ledger are not deposited. "Present in raw / dedup" cannot be verified for any candidate.
2. At least 6 distinct papers that look eligible under SCOPE §4–§5 are in no deposited search, screening or full-text log (HCMKT appears only in the venue-probe list VX05; DECKT, Self-paced CL / SP-CLKT, CoSKT, HCMKT, bipartite-graph CL, and, from the title alone, Han et al. dynamic heterogeneous graph CL). A seventh, DTransformer, is in the seed list as `BACKGROUND` (KT040), and that decision conflicts with SCOPE §5 as written.
3. The supplementary search has not been run (no database access; strings proposed in `A1_QUERY_GAP_ANALYSIS.md`).
4. Eligibility decisions need a human screener. Cursor's reading is not an independent second screen (see A3).

Per the protocol: **STOP. Package A3 is not started.**

## 1. A1.1–A1.3 Coverage of the named candidates

Full row-level table: `tables/A1_CORPUS_COVERAGE_AUDIT.csv` (7 distinct papers, one alias row, plus 9 venue-probe papers, 17 rows).

| ID | Paper | Year | In raw 2,017 | In dedup 750 | Only record found in repo | G | S | AI reading of gateway | Evidence level |
|---|---|---|---|---|---|---|---|---|---|
| A1-C01 | DECKT, Entropy 27(7):685, DOI 10.3390/e27070685 | 2025 | NEEDS_EVIDENCE | NEEDS_EVIDENCE | none | YES | YES | would pass (G∩S) | full text (open access) |
| A1-C02 | DTransformer, WWW'23, DOI 10.1145/3543507.3583255 | 2023 | NEEDS_EVIDENCE | NEEDS_EVIDENCE | seed KT040, `BACKGROUND` | NO | YES | would pass (S) | full text |
| A1-C03 (=C08) | Self-paced CL for KT / SP-CLKT, Neurocomputing 609:128366 | 2024 | NEEDS_EVIDENCE | NEEDS_EVIDENCE | none | NO (abstract) | YES | would pass (S) | abstract only |
| A1-C04 | Dynamic heterogeneous graph contrastive networks for KT, ASOC 166:112194 | 2024 | NEEDS_EVIDENCE | NEEDS_EVIDENCE | none | likely | likely | **not assessable** | title only |
| A1-C05 | HCMKT, ESWA 295:128840 | 2025 | NEEDS_EVIDENCE | NEEDS_EVIDENCE | venue-probe list VX05 only | YES | YES | would pass (G∩S) | abstract + intro excerpt |
| A1-C06 | Contrastive learning on bipartite graphs for interpretable KT, ADMA'24 (LNAI 15389) | 2024 | NEEDS_EVIDENCE | NEEDS_EVIDENCE | none | YES | YES | would pass (G∩S) | abstract only |
| A1-C07 | CoSKT, IEEE TLT 17:1476–1488 | 2024 | NEEDS_EVIDENCE | NEEDS_EVIDENCE | none | NO (abstract) | YES | would pass (S) | abstract only |

**Ruling basis.** SCOPE_v1.0_LOCKED §5 lists as eligible SSL families: sequence contrastive learning, graph contrastive learning, multi-view contrastive learning, augmentation-free consistency learning. DTransformer's contrastive loss on augmented learner sequences (§3.3.1, Eq. 17) is the same family as CL4KT (KT039), which is in the corpus with S=Y. DECKT's InfoNCE between primary and momentum encoders is augmentation-free contrastive learning, and its graph-structure-constraint loss ties to the question–concept graph. CoSKT's consistency between common and individual knowledge states falls under "augmentation-free consistency learning".

**What the old seed record says about KT040.** The note reads "sequence/probabilistic KT baseline *without a verified* Graph-Based or Self-Supervised mechanism" and "inspect if needed". The BACKGROUND decision was therefore not made from the full text. This is a stage-of-error finding (A1.3), not a case where the paper was excluded with an EC code. No exclusion code is recorded (`NOT_RECORDED`).

**Where each was dropped (stage_reached).** Unknown for 6 of 7 (no record). The prompt asked never to write a bare "NOT INCLUDED". The entry is `NO_RECORD_IN_DEPOSITED_LOGS`, with the grep scope stated in the CSV. To make it verifiable, a human must check the raw exports or the 750-row ledger.

**Integrity limits of the existing screening files (relevant to A1.3).** `05_screening/title_abstract_screening_v1.0.csv` has 43 rows, including a placeholder row (`REC_0043`–`REC_0140`). `06_fulltext/fulltext_screening_v1.0.csv` has 48 rows, some with wrong DOIs. Both are AI-assistant-generated seed-stage records. Neither is a 610-row / 103-row ledger. They cannot show why a paper was excluded. The PRISMA counts 2,017 → 750 → 610 → 140 → 103 → 37 are arithmetic with no row ledger.

## 2. A1.4 Query gap
See `audit/A1_QUERY_GAP_ANALYSIS.md`. Short form: no missing-keyword gap for the named papers. The frozen strings are inconsistent across databases and the arXiv query is an OR-defect. A supplementary search is proposed but **not run**.

## 3. A1.5 Snowballing
`tables/A1_SNOWBALLING_LOG.csv`.
- **Backward (done, partial, regex-based):** 75 reference strings from 12 sources (the 9 SSL-KT corpus papers: KT011, KT039, KT042, KT043, KT047, KT050, KT066, KT068, plus KT026 PEBG; the Xu et al. Graph-KT survey; DECKT; DTransformer). Filter: contains "knowledge tracing" and a graph/contrastive/SSL/prerequisite keyword. 47 have no fuzzy title match in the seed list or the 14_references PDFs.
- The fuzzy match is only approximate. Some strings are false negatives, e.g. GIKT, CL4KT, GraphCA, which differ in title format. Treat the "no match" rows as *to be checked*, not as "missing".
- **Largest signal:** the Xu et al. Graph-KT survey reference list contains many Graph-KT works that are not in the 37 or in the seed list. Examples from its list: Hypergraph Transformer for KT, Attention-based hypergraph KT, HGKT (hypergraph; and the hierarchical-exercise-graph HGKT), AGKT, Heterogeneous graph based KT (Luo 2022), Temporal enhanced inductive graph KT, Meta-path structured graph pre-training for KT (Zhu 2024), MGKT, Qiu & Wang 2025 multigraph, Han 2024 dynamic heterogeneous graph contrastive. Whether these meet SCOPE §4 is not assessed. It does suggest the Graph-KT stream (N_G = 36) may be under-covered. This is a risk to the RQ1/RQ2 claims, not a finding.
- **Forward (not done):** all 12 sources are `NEEDS_EXTERNAL_VERIFICATION`. Cited-by search needs Scopus/WoS/Google Scholar access.
- The regex parse is not exhaustive (for example DECKT's list yielded 1 row). A manual pass is still needed.

## 4. A1.6 Seed recall
`tables/A1_SEED_RECALL.csv`. The legacy seed list is the 34 `PRIMARY_CORE` rows of `01_seed_corpus/included_papers_seed_audited_v1.0.csv` (KT004 … KT070). The corpus of 37 = these 34 + KT076, KT077, KT079.

```text
seed_recall (actual) = retrieved_seed_records / 34   -> NOT COMPUTABLE (raw exports absent)   [NEEDS_EVIDENCE]
simulated recall, union of 14 frozen core queries   = 34 / 34   (simulation, title+abstract of deposited PDFs)
simulated recall, Scopus Q-G ∪ Q-S only             = 31 / 34   (KT014, KT016, KT037 not reachable)
```

The simulated 34/34 is not a measured recall. It only says no seed paper is *outside* the term space of the union of the queries. Seed recall is also not independent. The seed list was assembled before the frozen queries were run, from the authors' prior knowledge. Do not report 34/34 in the manuscript as recall.

## 5. A1.7 Corpus refreeze — NOT DONE
No count regenerated. **Illustrative sensitivity only, not for the manuscript:** if every one of the 7 distinct candidates were accepted, N_S could rise from 9 to at most 16 (S: 7 of 7 candidates satisfy S on abstract/full-text reading, C04 not yet assessable). N_G could rise by up to 4, with C04 pending (C01, C05, C06 YES). N_{G∩S} up to 12. Inclusion of any would also change the provenance, QA, sparse/cold-start and calibration tables (including DECKT, which addresses low-frequency KCs). The headline "9 SSL papers" would no longer hold. This is a bound, not a count.

## 6. Human decisions required (before A3)
1. Deposit (or confirm absence of) the raw exports `*_20260826.csv` and the 750-row dedup ledger. Without them, 'present in raw / dedup' stays NEEDS_EVIDENCE.
2. Human screen of A1-C01…C07 (and, if wanted, the 9 venue-probe papers) against SCOPE §4–§5. Supply an exclusion code if any is rejected.
3. Decide whether to run `SUPPLEMENTARY_SEARCH_UPDATE_v2.0` and who runs it. Log it only after it is run.
4. Decide how to handle KT040 (seed `BACKGROUND` vs SCOPE §5 sequence contrastive). This requires a protocol-deviation entry if the corpus changes, because SCOPE/SLR protocol are `*_LOCKED`. Cursor did not edit them.
5. Decide whether to keep the corpus at 37 with an explicit "coverage limitation" disclosure, or reopen the corpus (A1.7 NO → this decision is the author's).

## 7. Files created by A1
- `audit/REVISION_MASTER_STATUS.md`, `audit/A1_QUERY_GAP_ANALYSIS.md`, `audit/A1_CORPUS_DECISION.md`
- `tables/A1_CORPUS_COVERAGE_AUDIT.csv`, `tables/A1_SEED_RECALL.csv`, `tables/A1_SNOWBALLING_LOG.csv`
- Helper scripts: `audit/_a1_match.py`, `audit/_a1_compute_seed_and_snowball.py`, `audit/_a1_build_coverage_table.py`
- Evidence copies (open-access / author-hosted, text extracts): `audit/_a1_evidence/DECKT_fulltext_PMC12294018.txt`, `DTransformer_fulltext_yin2023.txt`, `Shukurlu_LossAugmentedKT_arXiv2504.15163.txt`

```text
A1_CORPUS_FROZEN = NO
```
