# PDF recheck of five A-vs-B cells (2026-09-13)

Primary extracts: `08_quality_reliability/_adj_extract/KT011.txt`, `KT047.txt`, `KT026.txt`, `KT070.txt`, `KT068.txt`.  
IRR tokens only (B sheet). Codebook `MODEL_DEFINED_FIXED` = prescribed, **not** expert-supplied, **not** inferred from interactions, **not** jointly learned.

Does **not** change locked CSVs or §II unless the authors approve a recode.

| # | Paper | Field | A | B | PDF-strict | Keep live CSV? |
|---|---|---|---|---|---|---|
| 1 | KT011 | ssl_family | MULTIVIEW | GRAPH | **Both true**; exclusive rule → A | Yes (A) |
| 2 | KT047 | ssl_family | GRAPH | MULTIVIEW | **Both true**; PDF “two views” fits B; exclusive rule → A | Yes (A) |
| 3 | KT026 | provenance | MODEL_DEFINED | EXTERNAL | **Neither exact**; Q-tags + train difficulty | Yes (A collapse) |
| 4 | KT070 | provenance | MODEL_DEFINED | DYNAMIC | **B** | No — A conflicts with codebook |
| 5 | KT068 | encoder | HETEROGENEOUS_GNN | GNN_GENERIC | **B** (or OTHER) | Weak — PDF never says hetero GNN |

## 1. KT011 Bi-CLKT — family

Abstract: “node-level contrastive learning of subgraphs … and graph-level contrastive learning”; “two-layer comparative learning”; GCN at both levels.

- GRAPH: title *Bi-Graph Contrastive Learning*.
- MULTIVIEW: node-level vs graph-level (and two augmented views).

Survey exclusive token (`SSL_FAMILY_LOCKED_ALIGNMENT.md`): first locked token = MULTIVIEW. Not a PDF error.

## 2. KT047 DC-SSL — family

§3.3: “the two channels of DHGN are treated as **two views** … InfoNCE … contrast node representations from different views.”

B matches that sentence. A matches the exclusive-family table (GRAPH first, MULTIVIEW secondary). Token rule, not a missed pretext.

## 3. KT026 PEBG — provenance

- Bipartite \(G=(Q,S,R)\) from **skill–question relations** in the public logs (dataset tags, not an author concept map).
- Difficulty \(d_i\) = correct-rate **computed from the training dataset**.
- Implicit similarity from shared neighbors on that bipartite graph.

Codebook seed table: `PRECOMPUTED_UNCLEAR_SPLIT`.  
`MODEL_DEFINED_FIXED` requires “not inferred from interaction data” — difficulty **is** from train logs, so A is a collapse, not a perfect codebook match.  
`EXTERNAL_FIXED` fits PDKT-C/CMKT expert maps better than ASSISTments Q-tags.

Live IRR gold stays A so PEBG stays with other Q-matrix rows. Do not treat B as a PDF win.

## 4. KT070 Coda — provenance — **flip toward B**

§3.1.1: undirected code graph \(G_u=\{V_u,A_u\}\) with **learnable** \(A_u\); metric learning “automatically construct” the graph from the learner’s code sequence.  
Quote: “the structure of the code graph is learnable and **changes continuously with the update of W**.”

`MODEL_DEFINED_FIXED` forbids jointly learned topology. Expansion coding already had `JOINTLY_LEARNED_TRAINING`.  
IRR 4-way: **DYNAMIC_LEARNED** (B). Live `graph_taxonomy.csv` MODEL_DEFINED is the weaker cell.

## 5. KT068 HKT — encoder — **flip toward B**

Abstract: “construct different types of hierarchical graphs” (intra- vs cross-hierarchy).  
§4.2–4.3: **self-attention / multi-head attention** on KHT paths; neighbor attention inside a level.  
KHT = “expert prior knowledge”; KAG from learning sequences.

No sentence “heterogeneous GNN”, RGCN, HAN, or HGT.  
`HETEROGENEOUS_GNN` (A / taxonomy / v1.0 coding) is a label stretch.  
IRR: **GNN_GENERIC** (B) or `OTHER`. Not a typed hetero encoder.

## Action (applied 2026-09-13)

Live tables + manuscript follow PDF-strict: KT070 provenance → `DYNAMIC_LEARNED`; KT068 encoder → `GNN_GENERIC`. Counts: `audit/LOCKED_COUNTS_v1.6.md`. Family cells stayed A.
