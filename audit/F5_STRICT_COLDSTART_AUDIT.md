# F5 – STRICT COLD‑START AUDIT

**Status:** TODO – Re‑audit KT035 and compute sparse counts.

**Required fields** (must be PASS):
- `STRICT_KC_COLD_START` set to `YES` only if evidence verified; otherwise `TBD_VERIFY`.
- All counts (`N_STRICT_KC_COLDSTART`, `N_LOW_FREQUENCY_KC`, `N_GENERIC_DATA_SPARSITY`, `N_ITEM_COLDSTART`, `N_LEARNER_COLDSTART`, plus other sparse ontology counts) must be recomputed and match the manuscript.

**Evidence sources**:
- Full‑text PDF of KT035 (path to be provided by the user).

**Outputs**:
- `tables/F5_sparse_coldstart_final.csv`

**Notes**: After audit, replace `TODO` with `PASS` and add a link to the CSV file.
