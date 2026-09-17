# SSL family alignment to locked codebook §14

**Date:** 2026-09-13  
**Not a codebook change.** Display aliases that are not in `coding_codebook_v1.0_LOCKED.md` §14 are retired from manuscript tables and `ssl_taxonomy.csv`.

## Exclusive `ssl_family` rule

Default: first locked §14 token in the paper’s existing coding record. If the first listed token is not locked, use the first locked token.

**2026-09-13 exception (mechanism alignment):** if the PDF treats two graph channels/layers as **views** of the same contrast (KT011 node/graph; KT047 DHGN channels), exclusive family is `MULTIVIEW_CONTRASTIVE` even when the coding record listed `GRAPH_CONTRASTIVE` first.

| paper_id | Retired display alias | Locked exclusive `ssl_family` | Secondary locked token (not a second count) | Coding source |
|---|---|---|---|---|
| KT011 | — | `MULTIVIEW_CONTRASTIVE` | `GRAPH_CONTRASTIVE` | `KT011_CODING_v0.4.md` |
| KT026 | `GRAPH_EMBEDDING_PRETRAINING` | `GRAPH_RECONSTRUCTION` | — | `KT026_CODING_v1.1.md` |
| KT039 | — | `SEQUENCE_CONTRASTIVE` | — | Wave-A / Table IV |
| KT042 | `HYPERGRAPH_CONTRASTIVE` | `MULTIVIEW_CONTRASTIVE` | `GRAPH_CONTRASTIVE` | `KT042_CODING_v0.4.md` |
| KT043 | — | `MULTIVIEW_CONTRASTIVE` | `GRAPH_CONTRASTIVE` | `KT043_CODING_v1.0.md` |
| KT047 | — | `MULTIVIEW_CONTRASTIVE` | `GRAPH_CONTRASTIVE` | Dual-channel = two views (PDF §3.3); exclusive token aligned with KT011 (2026-09-13). Coding v1.0 listed GRAPH first. |
| KT050 | — | `GRAPH_CONTRASTIVE` | `MULTIVIEW_CONTRASTIVE` | `KT050_CODING_v1.0.md` |
| KT066 | `CROSS_VIEW_CONTRASTIVE` | `MULTIVIEW_CONTRASTIVE` | `GRAPH_CONTRASTIVE` | `KT066_CODING_v0.4.md` |
| KT068 | `HIERARCHICAL_CONTRAST` | `GRAPH_CONTRASTIVE` | `GRAPH_RECONSTRUCTION` (H1 PDF caption) | `KT068_CODING_v1.0.md` used non-locked `HIERARCHICAL_CONTRASTIVE`; first locked token is `GRAPH_CONTRASTIVE` |

## Exclusive counts (\(N_S=9\))

| Locked `ssl_family` | n | papers |
|---|---:|---|
| `MULTIVIEW_CONTRASTIVE` | 5 | KT011, KT042, KT043, KT047, KT066 |
| `GRAPH_CONTRASTIVE` | 2 | KT050, KT068 |
| `GRAPH_RECONSTRUCTION` | 1 | KT026 |
| `SEQUENCE_CONTRASTIVE` | 1 | KT039 |

**4 locked families**, not 7 display aliases.

Mechanism phrases in Table IV (hypergraph views, line-graph, hierarchical levels) are readable notes, not codebook tokens.

## Reviewer sentence

Table IV reports exclusive `ssl_family` values from codebook §14. Hypergraph, cross-view, and hierarchical wording describe mechanism, not additional family codes.
