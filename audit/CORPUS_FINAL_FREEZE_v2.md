# CORPUS_FINAL_FREEZE_v2

**Date:** 2026-11-25

```
CORPUS_FINAL_FREEZE = YES_VERIFIED_AI_LOCATOR
```

Gateway PDF gap closed for VX01–VX10. Freeze is **provisional** because new-row coding and QA are AI-primary and still marked human-verification REQUIRED.

Source base: `data\PRIMARY_CORE_EXPANDED_2026-11-24.csv` (N=44).
Output: `06_coding\PRIMARY_CORE_FINAL_v2.csv`.

## Regenerated counts (from FINAL_v2 rows)

- N = **53**
- NG = **49**
- NS = **22**
- NG∩S = **18**
- Check NG+NS−∩ = 53 (== N: YES)

### Provenance display (G rows)

- model-defined fixed = 31
- external fixed = 9
- dynamically learned = 9
- unclear = 0

### Sparse / calibration

- strict KC cold-start YES = 0/53
- item cold-start YES = 1/53
- learner cold-start YES = 2/53
- interaction-drop YES = 1/53
- ECE YES = 0/53
- Brier YES = 0/53
- RMSE YES = 15/53

## Additions

- KT090 VX01 AGKT
- KT091 VX02 Expert-defined graphs L@S
- KT092 VX03 GRKT
- KT093 VX04 BiCo
- KT094 VX06 GCLFKT
- KT095 VX07 TransKT
- KT096 VX08 SCDI
- KT097 VX09 MSCL
- KT098 VX10 KGS-KT

## Removals

- none

## Unresolved / caveats

- KT090–KT098 locator-backed verify COMPLETE 2026-11-25 (`06_coding/HUMAN_VERIFY_SIGNOFF_KT090-098_v1.md`); 9/9 KEEP, 0 CHANGEs. Author wet-ink countersign optional.
- VX10 coded from OA HTML extract (binary publisher PDF download previously blocked).
- Live TLT manuscript still quotes N=44 until rewrite phases update tex.

## Manuscript status (2026-11-25 evening)

- Revised versioned MS exists: `12_manuscript/TLT/Graph_SSL_KT_TLT_REVISED_vNext_{anonymous,full}.{tex,pdf}` (16 pp; N=53).
- Live TLT ship files (`main_tlt_*`, cover, portal pack) still quote N=44 until author promotion.

## Verify completion (2026-11-25)

- Status: **VERIFY XONG**
- Freeze token: `YES_VERIFIED_AI_LOCATOR`
- Signoff: `06_coding/HUMAN_VERIFY_SIGNOFF_KT090-098_v1.md`
