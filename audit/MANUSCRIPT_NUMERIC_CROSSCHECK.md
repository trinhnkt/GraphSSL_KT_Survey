# MANUSCRIPT_NUMERIC_CROSSCHECK

Recomputed from PRIMARY_CORE_FINAL_v2.csv / SSL_TAXONOMY_FINAL.csv:

| number | meaning | source | current |
|---:|---|---|---|
| 53 | primary-core N | FINAL_v2 rows | 53 |
| 49 | NG | G=YES | 49 |
| 22 | NS | S=YES / SSL rows | 22 / 22 |
| 18 | NG∩S | G∧S / graph_present | 18 / 18 |
| 31/9/9 | provenance display | G rows | {'MODEL_DEFINED_FIXED': 31, 'EXTERNAL_FIXED': 9, 'DYNAMICALLY_LEARNED': 9} |
| 19/9/7/7/2/2/3 | encoder display | G rows mapped | {'GCN_generic': 19, 'HETERO': 9, 'OTHER': 7, 'GAT': 7, 'HYPER': 2, 'DYN': 2, 'NONE': 3} |
| 20/2 | SSL paradigm | SSL csv | {'contrastive': 20, 'reconstruction': 2} |
| view totals | SSL view_source | SSL csv | {'multi-view': 8, 'graph': 7, 'sequence': 3, 'hypergraph': 2, 'hierarchical': 1, 'bipartite': 1} |
| 0/53 | strict KC | FINAL_v2 | 0 |
| 1/53 | item CS | FINAL_v2 | 1 |
| 2/53 | learner CS | FINAL_v2 | 2 |
| 1/53 | interaction-drop | FINAL_v2 | 1 |
| 0/53 | ECE/Brier | FINAL_v2 | 0/0 |
| 15/53 | RMSE | FINAL_v2 | 15 |
| 2017 | Nrec | search log | historical |
| 750/140/103/37 | PRISMA arithmetic | report only | historical; not final N |

Union check NG+NS−∩=N: True
