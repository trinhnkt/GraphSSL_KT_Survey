# Verification pass — 2026-11-17

No manuscript count was changed. N, N_G, N_S, 0/37, and 1/37 stay as printed. The bibliography was not edited.

## Five reference rows

| Item | What was opened | Result |
|---|---|---|
| Piech 2015 | NeurIPS abstract page and the deposited PDF (9 pages) | Title and the seven authors match the bibliography, including Jonathan Bassen. The abstract page does not print pages 505–513. Those page numbers were not found as the paper’s own pagination in the PDF text. Pages stay unverified. |
| SAKT 2019 | EDM 2019 proceedings index and the deposited PDF (6 pages) | The short-paper list includes Shalini Pandey and George Karypis, “A Self Attentive model for Knowledge Tracing” (no hyphen). The index does not print pages. Pages 384–389 appear only as a citation inside the deposited pyKT PDF. |
| pyKT 2022 | NeurIPS Datasets and Benchmarks abstract page and the deposited PDF (14 pages) | Title and the six authors match. PDF page 1 says the 36th NeurIPS (2022) Datasets and Benchmarks track. Pages 18542–18555 were not found in the PDF text. |
| DGMN | Crossref on 2026-11-17 and the deposited PDF | Crossref still returns early access only: issued 2022, pages 1–13, no volume. Title and both authors match. The deposited PDF is labeled “JOURNAL SUBMISSION” and has 11 pages. Volume 35, number 8, pages 7844–7855, year 2023 remains unverified. The bibliography was not replaced with the early-access pages. |
| Cursor | https://cursor.com on 2026-11-17 | The page loads and is the Cursor product page. The bibliography access date Sep. 13, 2026 was not changed. |

## Five removed DOIs, Crossref 2026-11-17

| ID | DOI | Result |
|---|---|---|
| KT078 | 10.1609/aaai.v39i1.30500 | HTTP 404 |
| KT080 | 10.1145/3690624.3709500 | HTTP 404 |
| KT081 | 10.24963/ijcai.2025/450 | Resolves to a different paper: “Discrete Budget Aggregation: Truthfulness and Proportionality,” IJCAI 2025, pp. 4040–4047 |
| KT082 | 10.1145/3627673.3679900 | Resolves to a different paper: “Does Knowledge Localization Hold True?,” CIKM 2024, pp. 4118–4122 |
| KT083 | 10.1016/j.neunet.2026.107500 | HTTP 404 |

These five stay out of the 37-paper corpus. The September 2026 findings are unchanged.

## Seven provenance records

PDF text was read. The displayed 19/8/9 counts were not changed. None of these sentences closes the display-versus-record difference.

| ID | PDF page | Sentence read | Record vs display |
|---|---|---|---|
| KT023 SGKT | pp. 2, 4 | A session graph captures transitions among neighboring exercises. | Record says jointly learned during training. The sentences do not say the adjacency is learned as a free parameter. |
| KT035 HHSKT | pp. 1, 5–6 | A heterogeneous graph is built with question, knowledge, and learner nodes. | The stored 8-way value is still UNCLEAR. This read is not a codebook adjudication. |
| KT050 GraphCA | p. 6 | Counterfactual subgraphs are constructed from the student–question–concept graph. | Does not say whether the base graph is jointly learned. |
| KT062 LGS-KT | p. 1 | A reweighted logical-skill evolution graph and a grammatical-skill interaction graph are constructed from code iterations. | Not described as an external expert map, and no train-only split is stated. |
| KT064 MG-Ensemble | pp. 5–6 | Similarity and dissimilarity interaction graphs are built from the interaction matrix. | A computed adjacency, not clearly a free learned adjacency. |
| KT065 CS-GKT | p. 7 | A directed concept graph uses co-occurrence counts. | The record says external fixed. This sentence describes a count-derived graph. |
| KT069 AEGOT-CDKT | pp. 3, 6 | Graph optimal transport aligns graphs, and exercise–exercise edges are weighted by co-occurrence. | Does not say the graph is learned dynamically, and does not state the split. |

## Eight SSL papers besides CL4KT

Text-layer counts only. Labels were not changed.

| ID | Present in the text layer | Not found as that string |
|---|---|---|
| KT011 Bi-CLKT | contrastive, subgraph, edge | drop, dropout |
| KT026 PEBG | bipartite, question-skill, relation, similar | reconstruct |
| KT042 S2-HHN | contrastive, hyperedge, drop | mask, masking |
| KT043 3V-CLKT | contrastive, three, view | — |
| KT047 DC-SSL | contrastive, dual-channel, channel, view | mask |
| KT050 GraphCA | InfoNCE, counterfactual, perturb | — |
| KT066 HyperKT | InfoNCE, hypergraph, “line graph” | “line-graph” as one hyphenated word |
| KT068 HKT | reconstruct, hierarchical, contrastive | — |

CL4KT was already page-checked in B3 and was not re-read here.

## Not done in this pass

ACM SRCH_001 and SRCH_002, and Web of Science SRCH_011 and SRCH_012, need a library login. B10, B2, the seven-candidate screen, and the second screener are human decisions. A2, A4, and C1–C3 stay waiting on a frozen corpus.
