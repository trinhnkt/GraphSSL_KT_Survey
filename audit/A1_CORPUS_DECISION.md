# A1 — Corpus coverage decision (Prompt 01)

**Date:** 2026-11-13. **Prepared by:** AI research assistant. All G / S / PRIMARY_CORE values below are AI readings, **not** screening decisions.
**Not done (by instruction):** no manuscript, figure, table, `*_LOCKED` file or count (N, N_G, N_S, N_G∩S) was changed.
**Supersedes:** `A1_CORPUS_DECISION_v0.1_superseded.md` (kept). Earlier 22-column table kept as `tables/A1_CORPUS_COVERAGE_AUDIT_EXTENDED_v0.1.csv`.

## 1. Source inventory (Step 1)

| Source | Found? | Where | Usable as evidence? |
|---|---|---|---|
| Raw search records N = 2,017 | **No (records absent)** | Only the log of 16 searches: `03_search/search_log.csv`. Counts sum to 2,017 (142+58+168+64+185+72+194+61+286+112+248+96+135+63+88+45). The 16 export files (`acm_qg_20260826.csv` …) are not in the repo; `03_search/reports/` has only `.gitkeep`. | Counts yes; records no |
| Deduplicated N = 750 | **No ledger** | `04_deduplication/deduplication_audit_v1.0.csv` has 34 duplicate groups (AI_ASSISTANT). The 1,267 removals are not listed. | No |
| Title/abstract screening log | **Partial** | `05_screening/title_abstract_screening_v1.0.csv` (43 rows, AI_ASSISTANT, placeholder row REC_0043–REC_0140) | No (cannot show the 610 exclusions) |
| Full-text screening log | **Partial** | `06_fulltext/fulltext_screening_v1.0.csv` (48 rows, AI_ASSISTANT, some DOIs wrong) | No (cannot show the 103 exclusions) |
| Exclusion log | **Partial** | `12_manuscript/TLT/supplementary/supplementary_prisma_exclusions.csv` (48 rows; only 2 EXCLUDE/BACKGROUND rows: REC_0047, REC_0048). Several DOIs look malformed (e.g. REC_0036 `10.1109/TKDE.2026.353000`, REC_0038 `10.1007/978-3-031-60000_15`) → flag for package B11. | No |
| Primary-core corpus (37) | Yes | `tables/corpus_counts.csv`, `12_manuscript/TLT/audit/LOCKED_COUNTS_v1.8.md` | Yes |
| Seed list of 34 | Yes | 34 `PRIMARY_CORE` rows in `01_seed_corpus/included_papers_seed_audited_v1.0.csv` (KT004 … KT070) | Yes |
| Queries Q-G, Q-S, Q-P, Q-R | Yes | `03_search/search_log.csv`: SRCH_001–014 (Q-G/Q-S), SRCH_015 (Q-P, 88 records), SRCH_016 (Q-R, 45 records) | Yes |

Grep of the whole repo (csv, md, tex, txt, json) for the 8 titles and both DOIs found **no occurrence** in any search, dedup, screening, full-text or exclusion file. Exceptions: DTransformer in the seed file (KT040) and HCMKT in my own venue-probe list (VX05).

## 2. Candidate status (Step 2) — table: `tables/A1_CORPUS_COVERAGE_AUDIT.csv`

| # | Paper | in raw 2,017 | in dedup 750 | Stage / decision / EC | KT central | G | S | PRIMARY_CORE (AI, provisional) |
|---|---|---|---|---|---|---|---|---|
| 1 | **DECKT** 10.3390/e27070685 (Entropy 2025) | NEEDS_EVIDENCE | NEEDS_EVIDENCE | no record anywhere / none / none | Y | Y | Y | Y |
| 2 | **DTransformer** 10.1145/3543507.3583255 (WWW'23) | NEEDS_EVIDENCE | NEEDS_EVIDENCE | **seed KT040, tier BACKGROUND**; no EC code recorded | Y | N | Y | Y (via S) |
| 3 | Self-paced contrastive learning for KT (Neurocomputing 609:128366, 2024) | NEEDS_EVIDENCE | NEEDS_EVIDENCE | no record | Y | N (abstract only) | Y | Y (via S, abstract only) |
| 4 | Dynamic heterogeneous graph contrastive networks for KT (ASOC 166:112194, 2024) | NEEDS_EVIDENCE | NEEDS_EVIDENCE | no record | Y (title) | NEEDS_EVIDENCE | NEEDS_EVIDENCE | NEEDS_EVIDENCE (abstract not retrieved) |
| 5 | HCMKT, 10.1016/j.eswa.2025.128840 (ESWA 295, 2025) | NEEDS_EVIDENCE | NEEDS_EVIDENCE | no screening record (only venue-probe VX05) | Y | Y | Y | Y |
| 6 | Contrastive learning on bipartite graphs for interpretable KT, 10.1007/978-981-96-0821-8_14 (ADMA 2024) | NEEDS_EVIDENCE | NEEDS_EVIDENCE | no record | Y | Y | Y | Y (abstract only) |
| 7 | **CoSKT** 10.1109/TLT.2024.3386750 (IEEE TLT 2024) | NEEDS_EVIDENCE | NEEDS_EVIDENCE | no record | Y | N (abstract only) | Y | Y (via S, abstract only) |
| 8 | SP-CLKT | = #3 (alias per Shukurlu 2025, arXiv:2504.15163, Table 1 → Dai et al., Neurocomputing 609:128366) | | | | | | same paper |

**Why "bị loại ở đâu / exclusion code" is not answered for 7 of 8.** No log records them. The answer is `NO_RECORD_IN_DEPOSITED_LOGS`, not "excluded". A human must check the raw exports or the 750-row ledger. DTransformer is the only one with a recorded decision: seed `BACKGROUND`, note "without a verified Graph-Based or Self-Supervised mechanism / inspect if needed". That decision was made without the full text. Its contrastive loss (§3.3.1, Eq. 17, ablation in Table 2) is the sequence-contrastive family of SCOPE_v1.0_LOCKED §5, the same family as CL4KT (KT039, already in the corpus).

**Evidence locators.** DECKT: abstract; Sec. 3.3.1 (GAT primary encoder), 3.3.2 (momentum encoder), InfoNCE objective, graph-structure-constraint loss (question–concept bipartite graph); text in `audit/_a1_evidence/DECKT_fulltext_PMC12294018.txt`. DTransformer: abstract, §3.3.1, Eq. 17 and 22, Table 2 "w/o CL"; text in `audit/_a1_evidence/DTransformer_fulltext_yin2023.txt`. Others: abstract/DOI pages (see CSV column `evidence_locator`).

## 3. Query-gap result (Step 4) — `audit/A1_QUERY_GAP_ANALYSIS.md`
For every candidate, the frozen queries should match on title/abstract (simulation). Checked keywords: contrastive, self-paced, dual/momentum encoder. The first appears in the frozen strings. The others are not in the frozen strings (not needed for these papers, a sensitivity risk for others). The gap is therefore **not a missing keyword**. It is a retrieval, deduplication or screening gap that the repo cannot resolve. Other findings: the term lists differ across databases (3 seed papers are reachable only through ACM/IEEE terms), and the arXiv queries are an OR-defect.

## 4. Seed recall (Step 5) — `tables/A1_SEED_RECALL.csv`, `tables/A1_SEED_RECALL_SUMMARY.csv`

```text
seed_recall = retrieved_seed / 34
actual:                              NEEDS_EVIDENCE (raw exports absent)
simulated, union of 14 queries:      34/34 = 1.000   (simulation only)
simulated, Scopus Q-G + Q-S only:    31/34 = 0.912   (KT014, KT016, KT037 unreachable)
```
Do not report the simulated value as recall. The seed list pre-dates the frozen queries.

## 5. Papers needing re-screening (human)
DECKT, DTransformer (KT040), Self-paced CL / SP-CLKT, HCMKT, bipartite-graph CL, CoSKT; Han 2024 after its abstract is obtained. Optional: the nine venue-probe papers (A1-X01, X02, X03, X04, X06–X10 in the extended table).

## 6. Papers / gaps needing supplementary search
- Run the harmonised strings in `A1_QUERY_GAP_ANALYSIS.md` §3 (`Q-G+`, `Q-S+`, `Q-S++`), same window and filters, plus re-run of the 14 original searches to test the deposited counts. Not run.
- The Xu et al. Graph-KT survey reference list contains many Graph-KT titles not in the 37 or the seed list (e.g. Hypergraph Transformer for KT, Attention-based hypergraph KT, AGKT, Meta-path structured graph pre-training for KT, Temporal enhanced inductive graph KT). Whether they meet SCOPE §4 is unassessed. Forward snowballing is not done (`tables/A1_SNOWBALLING_LOG.csv`, 12 sources `NEEDS_EXTERNAL_VERIFICATION`). Those example titles were not re-read in the 2026-11-13 pass over the deposited Xu PDF. That pass did search the seven A1 candidate strings and did not find them in the Xu file (section 8).

## 7. Is the corpus eligible to freeze?
**No.** Blockers: (1) raw exports and the 750-row ledger are missing; (2) six papers that look eligible under SCOPE §4–§5 have no screening record; (3) DTransformer's recorded exclusion conflicts with the locked S-criterion; (4) no supplementary search or forward snowballing has been run; (5) eligibility needs a human decision. Under the instruction, stop here; no other step was run.

## 8. Local library read (2026-11-13, `14_references`)

Every PDF in `14_references` was opened (48 files). Page-level identity is in `tables/A1_LOCAL_PDF_INVENTORY_2026-11-13.csv`. Full note: `audit/A1_LOCAL_PDF_READ.md`.

The folder holds the 37 primary-core PDFs, four baselines, and five prior surveys or benchmarks already cited by the manuscript. It does not hold a PDF of DECKT, DTransformer, self-paced contrastive KT, CoSKT, HCMKT, the bipartite-graph contrastive chapter, or Han et al. 2024. A full-text search of all 48 files found no occurrence of those titles except the citations named below. Having a PDF in this folder is not evidence that the paper was among the 2,017 search records.

Citations that are in the local files:

- DTransformer is cited by HKT (p. 10; the sentence says it incorporates contrastive learning), Coda (reference [47]), Multi-Granularity Ensemble (reference [36]), the Shen survey (reference [54]), and the Liu DLKT survey (reference [100]).
- Han et al., dynamic heterogeneous graph contrastive networks, is cited by the KT069 PDF (p. 24, reference [30]). The deposited Xu survey PDF does not contain that title, nor DECKT, CoSKT, HCMKT, or the self-paced and bipartite-graph candidate titles. The word "bipartite" in the Xu PDF is the general graph type.

Two files in the folder are not knowledge-tracing papers and are not in the README catalog: `Convolutional Neural Network for Trajectory Prediction.pdf` and `Model Generalization - A Sharpness Aware Optimization Perspective.pdf`. KGNN-KT remains an image-only scan.

This read does not screen any candidate in or out.

A1_CORPUS_FROZEN = NO

## 9. Later author decision (2026-11-18)

The evidence in sections 1–8 is unchanged. On 2026-11-18 the author froze the submitted corpus at the existing 37 papers and left the seven candidates out. Record: `audit/A1_CORPUS_FREEZE_2026-11-18.md`. Current flag: `A1_CORPUS_FROZEN = YES` for that submitted set only. The 2026-11-13 blockers are not closed.
