# Manuscript line/table audit — 2026-11-24

Source: `12_manuscript/TLT/main_tlt_anonymous.tex` vs `data/PRIMARY_CORE_EXPANDED_2026-11-24_QA7ALIGNED.csv`.
Script: `audit/_full_manuscript_line_audit_2026-11-24.py`.

## Locked CSV (PASS)

| Quantity | Value |
|---|---:|
| N | 44 |
| N_G / N_S / ∩ | 40 / 16 / 12 |
| Provenance | 24 / 7 / 9 |
| Encoder display | 14 / 7 / 6 / 6 / 2 / 2 / 3 |
| Strict KC / item / learner / drop | 0 / 1 / 2 / 1 |
| ECE / Brier / RMSE | 0 / 0 / 14 |
| QA HIGH / MODERATE / mean | 13 / 31 / 0.7472 |
| HIGH IDs | KT023,029,033,038,040,044,050,060,064,066,070,077,087 |

Abstract, contributions, cold-start table, QA table, conclusion: match locked counts.
PRISMA `37` strings are original-path arithmetic only (PASS).
Anonymous PDF after fix: **18 pages**.

## Critical findings (fixed in three live `.tex`)

1. **`tab:prov_encoder`** still printed as live $N=36$ with GAT=4 and GCN/generic=12, contradicting body $N_G=40$ encoder $14/7/6/6/2/2/3$. **Fix:** caption/body now label it as pre-expansion contingency only; locked marginals govern corpus claims.
2. **`tab:prov_appendix`** claimed $N_G=40$ / $24/7/9$ but printed 36 rows totaling $19/8/9$; KT062=EXT and KT069=DYN contradicted locked CSV; missing KT084/085/086/089. **Fix:** Disp locks + four expansion rows → printed $24/7/9$ on 40 IDs.
3. **`tab:graph_taxonomy_b`**: KT062 External / KT069 Dynamic contradicted adjudication; expansion Graph-KT rows absent. **Fix:** Model-defined + add DECKT/KT-Deeper/HCMKT/CLBG.
4. **SSL § opening**: “Five Graph-KT papers … do not meet S” read as exhaustive (true G¬S = 28). **Fix:** reword as 28 G¬S; five are the previously SSL-coded removals.
5. **`tab:ssl_taxonomy` caption** omitted “representative”. **Fix:** added.

## Still OK / residual (not blocking)

- SSL printed table = 9 of 16 rows (now captioned).
- Sparse printed table = representative subset (caption already says so).
- Mean printed as $0.75$ (locked $0.7472$) — intentional rounding.
- Bib key `HCMKT_2026` is acronym for the heterogeneous meta-path paper title.
- Optional: rebuild `manuscript_TLT_FORMATTED_v1.3.pdf` if that copy is still used for upload (portal pack prefers `main_tlt_*`).
