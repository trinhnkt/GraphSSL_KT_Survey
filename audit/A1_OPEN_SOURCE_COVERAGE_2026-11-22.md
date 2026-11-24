# A1 open-source coverage and snowball — 2026-11-22

**Corpus status:** still frozen at 37. No paper was added. \(N\), \(N_G\), \(N_S\), \(N_{G \cap S}\), 0/37, and 1/37 were not changed. The three live manuscript files were not edited.

**What this is:** a dated Crossref and OpenAlex check. It is not the search of 2026-08-26, and it does not show whether any record was among the 2,017 logged hits. `present_in_original_2017` stays `NEEDS_EVIDENCE`. No row below is a screening decision.

**Sources queried:** Crossref works API for the seven candidate DOIs; OpenAlex works API for backward references and forward citations of the nine included SSL papers and the Xu survey. Queried 2026-11-22. Forward lists were not truncated: the largest cited-by count in this set is 291 (Bi-CLKT), and the page cap was 500. OpenAlex citing-filter with a cursor parameter returned HTTP 401; pagination by page number returned the lists used here.

## Seven candidates

Crossref dates, all inside 2015-01-01 to 2026-07-31. Decision on every row: `NOT_ADDED_NEEDS_HUMAN_SCREEN`.

| ID | Paper | Crossref date | Container | In window | Recovered by this snowball |
| --- | --- | --- | --- | --- | --- |
| A1-C01 | DECKT, 10.3390/e27070685 | 2025-06-26 | Entropy | YES | YES. Forward links from KT011, KT026, KT039, KT042, KT043, KT050 |
| A1-C02 | DTransformer, 10.1145/3543507.3583255 | 2023-04-30 | WWW 2023 | YES | Not tested by the title filter. The title has no graph, contrastive, self-supervised, pretext, hypergraph, or bipartite token, so this pass would drop it even if a source cited it |
| A1-C03 | SP-CLKT, 10.1016/j.neucom.2024.128366 | 2024-12 | Neurocomputing | YES | NO in the OpenAlex reference and citation lists of the nine SSL papers and Xu |
| A1-C04 | Han et al. 2024, 10.1016/j.asoc.2024.112194 | 2024-11 | Applied Soft Computing | YES | YES. Forward from KT026; backward from Xu |
| A1-C05 | HCMKT, 10.1016/j.eswa.2025.128840 | 2026-01 | Expert Systems with Applications | YES | YES. Forward from KT011, KT039, KT043, KT047. OpenAlex prints 2025-07-02 for the same DOI; both dates are inside the window |
| A1-C06 | Bipartite chapter, 10.1007/978-981-96-0821-8_14 | 2024-12-15 | LNCS | YES | NO in those same OpenAlex lists |
| A1-C07 | CoSKT, 10.1109/TLT.2024.3386750 | 2024 | IEEE TLT | YES | YES. Forward from KT026. Crossref gives the year only |

GraphCA (KT050, 10.1109/JAS.2023.123678) resolved on OpenAlex to “GraphCA: Learning from Graph Counterfactual Augmentation for Knowledge Tracing.” The DOI was not replaced.

## Snowball

Seeds: KT011 Bi-CLKT, KT026 PEBG, KT039 CL4KT, KT042 S2-HHN, KT043 3V-CLKT, KT047 DC-SSL, KT050 GraphCA, KT066 HyperKT, KT068 HKT, and the Xu survey (OpenAlex W7169714148, Zenodo DOI 10.5281/zenodo.21443287, publication date 2026-07-19, 74 references, 0 citations). A kept row has “knowledge tracing” in the title and one of: graph, contrastive, self-supervised, pretext, ssl, hypergraph, bipartite.

- Detail log: `tables/A1_SNOWBALL_OPENALEX_2026-11-22.csv` (263 kept links).
- One row per DOI: `tables/A1_SNOWBALL_NEW_IN_WINDOW_2026-11-22.csv`.
- Candidate dates: `tables/A1_COVERAGE_OPEN_2026-11-22.csv`.
- Raw work records: `audit/_a1_2026-11-22/`.

Unique in-window records whose DOI is not in `12_manuscript/TLT/references.bib`: **90**.

- 1 is the Xu survey itself. It is already cited. OpenAlex exposes the Zenodo DOI, which is not the bibliography key.
- 4 are named candidates: DECKT, CoSKT, Han et al. 2024, HCMKT.
- 31 other titles contain contrastive, self-supervised, or pretext.
- 54 other titles are graph-and-knowledge-tracing hits without those words.

None of the 90 was screened. A close title overlap with the bibliography is not an identity except the Xu survey. Preprints, a Research Square record, and one non-publisher DOI string are inside the 90 and are not publisher versions.

## What this does not close

- Membership of any candidate in the original 2,017 records.
- An x/34 recall sentence.
- ACM SRCH_001, ACM SRCH_002, WoS SRCH_011, and WoS SRCH_012.
- A fate code for the seven candidates or for the extra title hits.
- A1. The gate stays NO.

Adding an in-window paper, including DECKT, would reopen the freeze and require the counts to be rebuilt. That decision is still the author’s.
