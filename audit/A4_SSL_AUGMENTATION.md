# A4 — Page-checked augmentation wording for eight Graph+SSL papers

**Date:** 2026-11-22
**A4_EIGHT_AUGMENTATIONS_PAGE_CHECKED = YES**
**Family codes, \(N_S\), and \(N_{G \cap S}\) unchanged.**

CL4KT was already page-checked. This pass re-read the deposited PDFs of the other eight SSL papers and replaced the augmentation phrases in the SSL table. The older tokens in `supplementary/supplementary_ssl_taxonomy_Ns9.csv` were not rewritten.

| Paper | PDF page | What that page states | Prerequisite edge |
|---|---|---|---|
| KT011 Bi-CLKT | pp. 7, 10 | Two corrupted graph views; degree and PageRank variants | Not stated |
| KT026 PEBG | pp. 1, 3 | Product network recovers bipartite question–skill side information | Not stated |
| KT042 S2-HHN | p. 8 | Adaptive node-dropout probability; augmented view has its own hyperedge set (p. 9) | Not stated |
| KT043 3V-CLKT | pp. 4–5 | Meta-path, neighbor, and KT views; non-question nodes masked in meta-path sequences | Not stated |
| KT047 DC-SSL | pp. 4–5 | Meta-path channel and network-schema channel contrasted with InfoNCE | Not stated |
| KT050 GraphCA | pp. 6–7 | Replace question nodes with similar questions; reorder answers on the same question set | Not stated |
| KT066 HyperKT | pp. 8, 11 | Line graphs of state hypergraphs are the augment views; negatives by row and column shuffling | Not stated |
| KT068 HKT | pp. 5, 7 | Graph reconstruction and hierarchical contrast | Not stated |

Page numbers are PDF pages. The phrases “edge dropout,” “channel masking,” “hyperedge masking,” “three-view perturbation,” “dual-view masking,” and “hierarchical perturbation” were removed from the main-text augmentation column because those names are not the operators in the passages above. A background paragraph in Bi-CLKT (p. 6) lists eliminating edges as a general graph-contrastive example; the Bi-CLKT method sentence on p. 7 is the corrupted-view sentence used in the table.
