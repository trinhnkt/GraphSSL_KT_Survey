# A1 — Query gap analysis (A1.4)

**Date:** 2026-11-13  **Package:** A1 (corpus coverage)  **Status:** analysis only. No frozen file edited, no search run, no manuscript edit.
**Evidence tables:** `tables/A1_CORPUS_COVERAGE_AUDIT.csv`, `tables/A1_SEED_RECALL.csv`
**Method note:** "hits" below come from a **simulation**. `audit/_a1_match.py` applies the exact frozen query strings in `03_search/search_log.csv` (rows SRCH_001–014) to a title + abstract excerpt. It is **not** retrieval evidence. Raw exports (`acm_qg_20260826.csv`, …) are not in the repo.

## 1. What the frozen queries look like

| DB | Q-G terms (after `"knowledge tracing" AND (…)`) | Q-S terms | Fields | Doc type |
|---|---:|---:|---|---|
| ACM DL | 15 (incl. prerequisite, concept map, skill graph, knowledge graph, concept graph, knowledge structure) | 8 (incl. masked prediction/interaction, reconstruction) | T/A/K | Journal/Conf |
| IEEE Xplore | 13 | 5 | T/A | Journal/Conf |
| ScienceDirect | 7 | 4 | T/A/K | **Journal only** |
| SpringerLink | 6 | 3 | T/A | Journal/Conf |
| Scopus | 8 | 4 | T/A/K | Journal/Conf |
| Web of Science | 7 | 3 | T/A/K | Journal/Conf |
| arXiv | 4 | 2 | T/A | Preprint |

All 14 core searches ran on 2026-08-26 with window 2015-01-01 to 2026-07-31 and English only (`search_log.csv`).

### Structural observations (facts from the log)
1. **The Q-G and Q-S term lists are not the same across databases.** The same conceptual query has 15 terms in ACM DL and 6 in SpringerLink. Three seed papers (KT014 Prerequisite-Driven DKT, KT016 Structure-Based KT, KT037 CMKT) are reachable in the simulation only through the ACM/IEEE term lists (`prerequisite`, `concept map`, `knowledge structure`). They are not reachable through Scopus, WoS, ScienceDirect or Springer terms (`A1_SEED_RECALL.csv`, column `simulated_retrievable_in_Scopus_Q_G_or_Q_S`). So retrievability depends on which database a paper happens to be indexed in.
2. **The arXiv queries as written are `ti:("knowledge tracing" …) OR abs:(…)`.** The first clause alone matches every arXiv paper with "knowledge tracing" in the title, regardless of graph/SSL terms. The arXiv count (135 / 63) therefore does not measure Graph/SSL retrieval. This is a query-construction defect to disclose. It is not a recall defect.
3. **ScienceDirect was limited to "Journal".** Conference-style items hosted there are excluded by design (disclose as filter).
4. Every query requires the exact phrase "knowledge tracing" or "student knowledge tracing". All 8 candidates contain it, so this is not a gap for them.

## 2. Candidate-by-candidate comparison with Q-G / Q-S (A1.4)

| ID | Paper | Contains KT phrase | Frozen terms found (title/abstract) | Would a frozen non-arXiv query match? | Missing-keyword gap? |
|---|---|---|---|---|---|
| A1-C01 | DECKT (Entropy 2025) | yes | graph, GAT, contrastive (Q-G and Q-S) | **yes**, all 6 non-arXiv DBs, both families (title+abstract) | **No** |
| A1-C02 | DTransformer (WWW 2023) | yes | "contrastive learning" in abstract (Q-S only; no graph) | **yes**, Q-S in all 6 non-arXiv DBs | **No** (and it was in the seed list as KT040) |
| A1-C03 / C08 | Self-paced CL for KT (Neurocomputing 2024; alias SP-CLKT) | yes | self-supervised, contrastive (Q-S) | yes (Q-S, all 6) | **No** |
| A1-C04 | Dynamic heterogeneous graph contrastive networks (ASOC 2024) | yes | heterogeneous, graph, contrastive (title only; abstract not retrieved) | yes by title alone | **No** |
| A1-C05 | HCMKT (ESWA 2025) | yes | heterogeneous, graph, contrastive | yes (both families) | **No** |
| A1-C06 | Contrastive learning on bipartite graphs, interpretable KT (ADMA 2024) | yes | graph(s), contrastive | yes (both families) | **No** |
| A1-C07 | CoSKT (IEEE TLT 2024) | yes | "Self-Supervised" in title (Q-S) | yes (Q-S, all 6) | **No** |

**Result.** For all 7 distinct candidates, the frozen strings should match in title/abstract. The gap is not missing keywords. It is one of: (a) the records were never retrieved by the database search (database coverage, export caps/pagination, UI behaviour); (b) they were retrieved but removed at deduplication or title/abstract screening; (c) they were removed at full-text screening. **The repository cannot distinguish (a)–(c).** None of the 7 appears in any deposited log. Only DTransformer appears, in the seed file, as `BACKGROUND`. HCMKT appears only in the venue-probe list (VX05).

### Keywords the frozen Q-S/Q-G strings do not contain (sensitivity risk, not an observed miss)
- SSL side: `momentum encoder`, `dual encoder`, `self-paced`, `consistency` / `consistency learning`, `auxiliary loss/task`, `representation learning`, `pre-training/pretraining`, `knowledge distillation`, `InfoNCE`, `mutual information`, `augmentation`. SCOPE §5 lists "augmentation-free consistency learning", "teacher–student/self-distillation" and "masked … prediction" as eligible families. A paper that uses such an objective without writing "contrastive", "self-supervised" or "masked modeling" would not be retrieved. DECKT, DTransformer, SP-CLKT and CoSKT all say "contrastive" or "self-supervised", so they are not examples of this risk.
- Graph side (Scopus, WoS, ScienceDirect, Springer, arXiv strings): `prerequisite`, `concept map`, `knowledge structure`, `knowledge graph`, `relation graph`, `network embedding`, `message passing`, `hierarchical`, `topological`. The seed result in §1 is a live example for the first three.

## 3. Proposed supplementary search (NOT executed; for a human to run and log)

**Label:** `SUPPLEMENTARY_SEARCH_UPDATE_v2.0`. It does **not** replace or rewrite `search_log.csv` (frozen history). It is a sensitivity search plus an audit of the original 16 searches.

**Purpose:** (i) harmonise the term lists across databases; (ii) test whether SSL-objective papers without the three frozen SSL words exist; (iii) re-run the 14 core searches to compare against the deposited counts. If the re-run counts differ strongly from 142/58/168/…, a retrieval or export problem is indicated.

**Template strings** (fill the database syntax; keep date window 2015-01-01 to 2026-07-31, English, same document-type filters as the original, **and also** a no-doc-type-filter variant for ScienceDirect):

```text
KT   = ("knowledge tracing" OR "student knowledge tracing" OR "deep knowledge tracing")

Q-G+ = KT AND (graph OR "graph neural network" OR GNN OR GCN OR GAT OR hypergraph OR heterogeneous
              OR "dynamic graph" OR "temporal graph" OR prerequisite OR "concept map" OR "skill graph"
              OR "knowledge graph" OR "concept graph" OR "knowledge structure")        # = ACM list, applied to ALL databases

Q-S+ = KT AND ("self-supervised" OR "self supervised" OR contrastive OR "masked modeling" OR "masked prediction"
              OR "masked interaction" OR reconstruction OR "pretext task")             # = ACM list, applied to ALL databases

Q-S++ (sensitivity) = KT AND ("momentum encoder" OR "dual encoder" OR "dual-encoder" OR "self-paced" OR consistency
              OR "auxiliary loss" OR "auxiliary task" OR "representation learning" OR pretraining OR "pre-training"
              OR "knowledge distillation" OR InfoNCE OR "mutual information")
```

| Field to record per search | Value |
|---|---|
| database / interface URL | `TO_BE_FILLED_BY_HUMAN` |
| exact query string as submitted | `TO_BE_FILLED_BY_HUMAN` |
| fields searched, filters | `TO_BE_FILLED_BY_HUMAN` |
| run date | `TO_BE_FILLED_BY_HUMAN` |
| records returned | `TO_BE_FILLED_BY_HUMAN` (**no value may be entered by Cursor**) |
| export file deposited (hash) | `TO_BE_FILLED_BY_HUMAN` |

**Handling of results:** new records go through dedup against the frozen 750 ledger (requires the ledger to be deposited first), then TA/FT screening by a human screener, then A3 reliability. Any inclusion is a documented deviation (`00_protocol/protocol_deviations.md`, to be added by the author only after the supplementary search is actually run). Not added now because nothing has been run.

## 4. Conclusion (A1.4)
- No evidence of a missing-keyword gap for the 8 named papers (7 distinct).
- Evidence of **inconsistent query construction across databases** and an **arXiv OR-defect**, both reportable in Supplementary Table S-Search (package B5).
- Whether the 7 papers were dropped at retrieval, TA or FT is **NEEDS_EVIDENCE** until the raw exports or the 750-row ledger are deposited.
