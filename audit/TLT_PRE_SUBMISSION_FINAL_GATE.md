# TLT pre-submission final gate

**Date:** 2026-11-25

```
TLT_PRE_SUBMISSION_STATUS = NOT_READY
```

## Checklist

### CORPUS
- [x] all 10 known candidates listed and reviewed at AI level
- [ ] all 10 resolved without UNCERTAIN-for-missing-PDF
- [ ] final primary core frozen (`PRIMARY_CORE_FINAL_v2.csv`)
- [ ] N/NG/NS/NG∩S regenerated from final table
- [x] no manual count forcing in this revision pass

### SEARCH
- [x] final update status documented (`FINAL_SEARCH_UPDATE_COMPLETED = NO`)
- [x] no fabricated search counts
- [x] PRISMA not newly invented

### SCREENING
- [x] true paired title/abstract file used (`05_screening/inter_rater_screening.csv`)
- [x] true paired full-text file used (`05_screening/inter_rater_fulltext.csv`)
- [x] REC_0047 adjudication documented in project CSV
- [x] screening raw agreement reported (`tables/SCREENING_RELIABILITY_FINAL.csv`)
- [x] screening κ only where defined (FT κ = NA at n=1)

### CODING RELIABILITY
- [x] direct NguyenKT vs DaoMT analysis completed
- [x] invariant fields → κ NA when pe=1
- [ ] human–human reliability emphasized in **live manuscript** (pending rewrite)
- [ ] AI–human reliability moved to Supplementary in live package (pending)

### RELATED WORK
- [x] Zanellati et al. 2024 metadata verified
- [ ] added to Related Work / Table II in live tex
- [x] novelty claim policy: no “first survey”

### GRAPH / SSL / SPARSITY / CALIBRATION / QA
- [ ] regenerate after freeze only

### AI DISCLOSURE
- [x] draft roles transparent (`audit/AI_DISCLOSURE_FINAL.md`)
- [ ] live Acknowledgment updated after author approval

### REFERENCES / TITLE / METHODS / ABSTRACT / TABLES
- [ ] pending freeze / author decisions

### MANUSCRIPT PACKAGE
- [ ] versioned `Graph_SSL_KT_TLT_REVISED_vNext` created
- [x] current live PDFs ≤ 18 pages (16 pp)
- [x] no automatic submission

## Blockers

1. **BLOCKER_1:** VX02, VX04, VX06, VX08, VX09 UNCERTAIN (no full PDF).  
2. **BLOCKER_2:** Human verification of AI PRIMARY_CORE for VX01, VX03, VX07, VX10 before membership change.  
3. **BLOCKER_3:** Final six-DB search update not executed.  
4. **BLOCKER_4:** Live manuscript not yet rewritten to prioritize NguyenKT↔DaoMT κ / Zanellati / SSL full-NS taxonomy.  
5. **BLOCKER_5:** Author decision on title Option B pending.
