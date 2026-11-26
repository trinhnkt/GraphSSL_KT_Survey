# No-DOI bibliography check — 2026-11-24

Source: `12_manuscript/TLT/references.bib` (55 bibliographic entries).
Entries without a `doi=` field: **6**.

## `Piech_DKT_2015` (inproceedings)

- Title: Deep Knowledge Tracing
- Year: 2015
- Venue: Adv. Neural Inf. Process. Syst. (NeurIPS)
- URL in bib: https://proceedings.neurips.cc/paper/2015/hash/bac9162b47c56fc8a4d2a519803d51b3-Abstract.html
- Note: (none)
- URL resolve: **OK** (200)
- Candidate identifier: `10.48550/arXiv.1506.05908`
- doi.org resolve: **OK** (200)
- Type: **arXiv preprint DOI** (not the archival conference/journal DOI).

## `Pandey_SAKT_2019` (inproceedings)

- Title: A Self-Attentive Model for Knowledge Tracing
- Year: 2019
- Venue: Proc. 12th Int. Conf. Educ. Data Mining (EDM)
- URL in bib: https://educationaldatamining.org/edm2019/proceedings/
- Note: (none)
- URL resolve: **OK** (200)
- Candidate identifier: `10.48550/arXiv.1907.06837`
- doi.org resolve: **OK** (200)
- Type: **arXiv preprint DOI** (not the archival conference/journal DOI).

## `Liu_pyKT_2022` (inproceedings)

- Title: {pyKT}: A {Python} Library to Benchmark Deep Learning based Knowledge Tracing Models
- Year: 2022
- Venue: Adv. Neural Inf. Process. Syst. (NeurIPS) Datasets Benchmarks Track
- URL in bib: https://proceedings.neurips.cc/paper_files/paper/2022/hash/75ca2b23d9794f02a92449af65a57556-Abstract-Datasets_and_Benchmarks.html
- Note: (none)
- URL resolve: **OK** (200)
- Candidate identifier: `10.52202/068431-1347`
- doi.org resolve: **OK** (200)
- Crossref title: PyKT: A Python Library to Benchmark Deep Learning Based Knowledge Tracing Models
- Crossref container: Advances in Neural Information Processing Systems 35

## `Shukurlu_LossKT_2025` (misc)

- Title: Survey of Loss Augmented Knowledge Tracing
- Year: 2025
- Venue: arXiv:2504.15163
- URL in bib: https://arxiv.org/abs/2504.15163
- Note: (none)
- URL resolve: **OK** (200)
- Candidate identifier: `10.48550/arXiv.2504.15163`
- doi.org resolve: **OK** (200)
- Type: **arXiv preprint DOI** (not the archival conference/journal DOI).

## `Xu_GbKT_2026` (article)

- Title: A Survey of Graph-Based Knowledge Tracing from Structural and Propagation Perspectives: Models, Applications, and Future Directions
- Year: 2026
- Venue: J. Educ. Data Min.
- URL in bib: https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1089
- Note: No Crossref DOI registered; publisher landing page used
- URL resolve: **OK** (200)
- Candidate identifier: `10.5281/zenodo.21443288`
- doi.org resolve: **OK** (200)
- Type: **Zenodo/repository DOI** (not a Crossref journal DOI). Prior adjudication preferred publisher landing page.

## `Cursor_AI_2026` (misc)

- Title: {Cursor} {AI} Coding Assistant
- Year: 2026
- Venue: [Online]. Available: https://cursor.com
- URL in bib: (none)
- Note: Accessed: Sep. 13, 2026
- Candidate DOI: none proposed beyond current URL.

## Verdict

| Key | Has archival/publisher DOI? | Action |
|---|---|---|
| `Liu_pyKT_2022` | **YES** — NeurIPS proceedings DOI `10.52202/068431-1347` | **Add doi+url** to bib |
| `Piech_DKT_2015` | No NeurIPS paper DOI; only arXiv `10.48550/arXiv.1506.05908` | Keep proceedings URL; optional arXiv note (do not replace venue with preprint) |
| `Pandey_SAKT_2019` | No EDM paper DOI; only arXiv `10.48550/arXiv.1907.06837` | Keep EDM proceedings URL; optional arXiv note |
| `Xu_GbKT_2026` | No Crossref journal DOI; Zenodo repo DOI exists | Keep JEDM landing URL (current); Zenodo optional secondary |
| `Shukurlu_LossKT_2025` | arXiv DOI expected | Confirm eprint/DOI in `@misc` |
| `Cursor_AI_2026` | N/A (software/tool) | Keep `@misc` online citation |