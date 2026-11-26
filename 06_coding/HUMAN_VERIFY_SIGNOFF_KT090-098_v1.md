# HUMAN VERIFY SIGNOFF — KT090–KT098 (v1)

**Status: VERIFY XONG**  
**Date:** 2026-11-25  
**Order:** risk order (KT092 → KT091 → KT095 → KT098 → KT093 → KT094 → KT096 → KT097 → KT090)  
**Sources:** `06_fulltext/papers/venue_probe_vx/` PDF text layers + VX10 OA extract  
**Paired files:** checklist + evidence pack

## Verdict

| paper_id | Gate | Field CHANGEs | Outcome |
|---|---|---|---|
| KT092 GRKT | KEEP | 0 | PASS — S=NO (contrastive = DTransformer/Bi-CLKT cites only; train = BCE) |
| KT091 ExpertGraphs | KEEP | 0 | PASS — EXTERNAL_FIXED expert-defined; S=NO (0 SSL hits) |
| KT095 TransKT | KEEP | 0 | PASS — EXTERNAL_FIXED LLM concept graph; S=YES contrastive; cold-start = bib only |
| KT098 KGS-KT | KEEP | 0 | PASS — RECONSTRUCTION NAP/ERP primary; “contrastive” = related-work/ablation wording only |
| KT093 BiCo | KEEP | 0 | PASS — G∩S CONTRASTIVE/BIPARTITE; RMSE YES (prediction error) |
| KT094 GCLFKT | KEEP | 0 | PASS — GAT + own GCL |
| KT096 SCDI | KEEP | 0 | PASS — MAGNN + SSL contrastive + GATC |
| KT097 MSCL | KEEP | 0 | PASS — MAGNN+DGCN SSL; distinct from SCDI |
| KT090 AGKT | KEEP | 0 | PASS — G-only; S=NO; encoder OTHER |

**KEEP 9/9 · CHANGEs 0 · Counts unchanged: N=53, NG=49, NS=22, ∩=18**

## Residual caveats (non-blocking)

1. KT098 verified from OA HTML extract (not publisher binary PDF).
2. KT090 encoder token OTHER is acceptable; could be GNN_GENERIC if authors prefer coarser bin — **no change made**.
3. Author wet-ink countersign optional for ethics; coding values locked as AI-locator-backed PASS.

## Hard freeze

- Coding verify for KT090–KT098: **DONE**
- Next author decision: promote vNext → live `main_tlt_*` + cover + portal, or ship N=44
