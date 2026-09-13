# F4 – SSL CORPUS & TABLE IV AUDIT

**Status:** TODO – Rebuild SSL corpus and Table IV.

**Required fields** (must be PASS):
- Table generated from rows where `S_criterion = Y`.
- Counts `N_S`, `N_G_AND_S`, and verified `N_CORE = N_G + N_S - N_G_AND_S`.
- KT026 adjudicated with correct fields.
- No unsupported labels retained.

**Evidence sources**:
- `coding_master.csv` (or the master coding sheet containing S_criterion).

**Outputs**:
- `tables/F4_ssl_papers.csv`
- `tables/F4_ssl_taxonomy.csv`
- Updated Table IV in manuscript.

**Notes**: After generation, replace `TODO` with `PASS` and add links to the CSV files.
