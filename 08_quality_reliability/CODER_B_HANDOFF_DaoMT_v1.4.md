# Handoff — DaoMT subset (independent, 10 papers)

Give **DaoMT** only the files below. Do not give locator packs or NguyenKT sheets.

This does **not** relabel the locator-assisted `NguyenKT` rows.

## Give

| File |
|---|
| `08_quality_reliability/CODER_B_SUBSET_DaoMT_v1.4.md` |
| `08_quality_reliability/CODER_B_FILL_SHEET_DaoMT_v1.4.md` |
| `08_quality_reliability/inter_rater_coding_sample_BLIND_EMPTY_v1.4_DaoMT.csv` |
| PDFs for the 10 IDs in that sheet (`14_references/`) |
| `00_protocol/coding_codebook_v1.0_LOCKED.md` |
| `00_protocol/SCOPE_v1.0_LOCKED.md` §4–§6 |
| Optional: `08_quality_reliability/_kt076_pages/` |

## Do not give

- Locator packs, AI quote rules, Coder A, manuscript tables
- Any `BLIND_EMPTY_v1.3*.csv`
- `inter_rater_coding_sample_v1.0.csv` (`why_included` leaks A)
- `SUBSET_DaoMT_DESIGN_v1.4.md` (internal; names strata)

## After the CSV comes back

1. Freeze `inter_rater_coding_sample_BLIND_EMPTY_v1.4_DaoMT_AS_SUBMITTED.csv`.
2. Compare those 10 IDs to `inter_rater_coderA_locked_v1.0.csv`.
3. Run `python compute_kappa_daomt_subset.py` (writes a report only if all 80 cells are filled).
4. Do not pool with `NguyenKT` and call the pool independent-blind.
5. §II: keep locator-assisted 20-paper \(\kappa\) as is; add a separate sentence for the DaoMT subset if that pass is completed.
