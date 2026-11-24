# PDF recheck of three remaining A-vs-B cells (2026-09-13)

After Coda/HKT recode. Extracts: `_adj_extract/KT011.txt`, `KT047.txt`, `KT026.txt`.  
IRR 4-way provenance; exclusive `ssl_family` = first locked §14 token in the coding record (`SSL_FAMILY_LOCKED_ALIGNMENT.md`).

| # | Paper | Field | A | B | PDF | Live gold |
|---|---|---|---|---|---|---|
| 1 | KT011 | ssl_family | MULTIVIEW | GRAPH | Both true | **Keep A** |
| 2 | KT047 | ssl_family | GRAPH | MULTIVIEW | Both true; PDF says “two views” | **Keep A** (rule). Optional flip if mechanism-aligned with KT011. |
| 3 | KT026 | provenance | MODEL_DEFINED | EXTERNAL | Q-tags + train difficulty; **not** expert map | **Keep A** |

No CSV change in this pass.

## 1. KT011 Bi-CLKT — family

PDF §4: “two-layer” node-level (E2E) + graph-level (C2C) contrast; “two graph views” by augmentation; GCN encoders. Title: *Bi-Graph Contrastive Learning*.

`KT011_CODING_v0.4.md`: `MULTIVIEW_CONTRASTIVE, GRAPH_CONTRASTIVE` (MULTIVIEW first).

B = secondary token. Not a missed pretext.

## 2. KT047 DC-SSL — family

PDF §3.3: “the two channels of DHGN are treated as **two views** … InfoNCE … contrast node representations from different views.” Contrast is on a heterogeneous graph (RGCN / meta-path).

`KT047_CODING_v1.0.md`: `GRAPH_CONTRASTIVE, MULTIVIEW_CONTRASTIVE` (GRAPH first).

Same exclusive-rule as KT011 → A.  
If exclusive family were assigned by **mechanism** (dual views → MULTIVIEW), this cell would match B and KT011; family counts would become MULTIVIEW 5 / GRAPH 2. That is a rule choice, not a PDF miss.

## 3. KT026 PEBG — provenance

PDF: bipartite \(G=(Q,S,R)\) from **observed question–skill links**; difficulty from the **training** set. Related-work contrast: PDKT-C “manually labels prerequisite relations … not suitable for large-scale data.”

v0.4 coding: `PRECOMPUTED_UNCLEAR_SPLIT` (not in the IRR 4-way set).  
`EXTERNAL_FIXED` is the PDKT-C/CMKT expert-map code. PEBG rejects that construction.  
`MODEL_DEFINED_FIXED` is the live collapse for Q-matrix incidence (same as GIKT/JKT rows). B is the weaker 4-way token.

## Action

**KT047 recoded 2026-09-13** to exclusive `MULTIVIEW_CONTRASTIVE` (author decision: match KT011 dual-view rule). Family counts: Multiview 5, Graph contrast 2. KT011 and KT026 unchanged.
