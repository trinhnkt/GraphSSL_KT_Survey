# H4 — Table III KT004 and KT026

## KT004 GKT

Was: model “GKT (Dense)” and graph source “Sequential transition” in one row.

Now: model **GKT**; graph source **Multiple graph variants**; provenance **Model-defined** (counted in `MODEL_DEFINED_FIXED`, \(n=19\)); encoder **Generic GNN**; temporal **RNN**.

Supplementary model-entry rows (`graph_taxonomy.csv`):
- `KT004_Dense`: `graph_source=DENSE_CONCEPT_GRAPH`, `directed=NO` (architecture-complete KC graph; Wave-A adjudication).
- `KT004_Trans`: `graph_source=SEQUENTIAL_TRANSITION`, `directed=YES`.

Unique paper count remains 1.

## KT026 PEBG

Was: encoder **GCN**.

PDF/codebook: product-based neural pretraining on a question–skill bipartite graph; `gnn_encoder=NONE`.

Now: encoder **none / PNN pretrain**; fusion **embedding init**. Graph/bipartite use and two-stage training kept.

Encoder totals after the change (\(N_G=36\)): GCN/generic **13** (GCN 12 + GNN_GENERIC 1); NONE **3** (PDKT-C, CMKT, PEBG).
