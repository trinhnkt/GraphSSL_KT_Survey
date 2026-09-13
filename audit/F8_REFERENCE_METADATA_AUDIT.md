# F8 – REFERENCE & SCIENTIFIC CLAIM AUDIT

**Status:** TODO – Validate all references and remove unsupported claims.

**Required actions**:
- Verify each reference (author, year, venue, DOI) against Crossref/Publisher metadata.
- Produce `audit/F8_REFERENCE_METADATA_AUDIT.csv` with columns: `ref_id, author, year, venue, DOI, verification_status`.
- List any mismatches or missing DOIs in `audit/F8_REFERENCE_CONFLICTS.md`.
- Audit scientific claims in the manuscript (especially over‑claims listed in F8) and record decisions in `audit/F8_SCIENTIFIC_CLAIM_AUDIT.md`.

**Evidence sources**:
- `references.bib` (or the bibliography file used in LaTeX manuscript).

**Outputs**:
- `audit/F8_REFERENCE_METADATA_AUDIT.csv`
- `audit/F8_REFERENCE_CONFLICTS.md`
- `audit/F8_SCIENTIFIC_CLAIM_AUDIT.md`

**Notes**: After completing the audit, replace `TODO` with `PASS` and add links to the three output files.
