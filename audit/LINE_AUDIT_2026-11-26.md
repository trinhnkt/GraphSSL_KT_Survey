# Line audit — live N=53 manuscript

Date: 2026-11-26

## Corpus vs text
- CSV: N=53, NG=49, NS=22, cap=18, prov={'MODEL_DEFINED_FIXED': 31, 'EXTERNAL_FIXED': 9, 'DYNAMICALLY_LEARNED': 9}
- Text markers: N=53×10, NG=49×13, NS=22×17

## Appendix coverage
- appendix IDs=49
- missing=[]
- extra=[]

## Forbidden leftovers
- none

## Figures text layer
- fig_taxonomy_2d.pdf: stale=none; saw=['N = 53', 'NG = 49', 'NS = 22', '31/9/9']
- fig_ssl_framework.pdf: stale=none; saw=['NS = 22']
- fig_meta_analysis_charts.pdf: stale=none; saw=['NG = 49']
- fig_prisma_flow.pdf: stale=none; saw=['N = 53']
- fig_graph_construction_pipeline.pdf: stale=none; saw=['NG = 49']

## Anon/full body sync
- abstract→bibliographystyle equal: True

## Line-level language flags
- flag count=0

## Internal consistency spot checks
- OK provenance % in TeX as `63.3\%` / `18.4\%` (false FAIL was unescaped `%` in checker)
- OK 13/39/1, overlay 49+1+1+2, appendix 49/49, venue/gateway N=53 narrative
- OK principal human-human; cover AI sentence; cover N_G=49

## Defects found and fixed this pass
- **Graph-only count:** “Twenty-eight Graph-KT papers do not meet S” was leftover from $N_G=40$, $∩=12$. Correct is **Thirty-one** ($49-18=31$). Fixed + rebuilt.
- **Typo:** “deposited titled title/abstract rows” → “deposited title/abstract rows”.
- **RQ2 wording:** “utilized” → “used”.

## LaTeX undefined (from last log)
- log hits=0 after rebuild; PDFs still **16 pages**
