# Protocol deviations

Recorded 2026-11-06. Locked protocol files were not edited.

Use one section per deviation:

## DEV-20261106-01
- Date: 2026-11-06
- Protocol version before: SLR_PROTOCOL_v1.0_LOCKED
- Protocol version after: unchanged
- Change: Title/abstract and full-text second-screener pair files, the 750-row screening ledger, named database export files, and a 98-row EC1--EC7 exclusion ledger are not deposited. Identification $N=2{,}017$ is the sum of `03_search/search_log.csv`. Stage counts 1,267 / 750 / 140 / 103 remain those of the PRISMA search-expansion report. The coded primary core is the 37 papers with deposited PDFs.
- Reason: Repository audit found no record-level screening ledger matching the reported PRISMA flow; labels will not be fabricated.
- Affected records: PRISMA flow reporting; not the 37-paper coding tables.
- Screening repeated: no
- Coding repeated: no
- Approved by: author execution of score-improvement sequence 1--5 (2026-11-06)

## DEV-20261106-02
- Date: 2026-11-06
- Protocol version before: coding_codebook_v1.0_LOCKED (8-way `graph_provenance`)
- Protocol version after: unchanged codebook; manuscript display uses 3 tokens
- Change: Manuscript provenance counts use the IRR three-token collapse (`MODEL_DEFINED_FIXED` / `EXTERNAL_FIXED` / `DYNAMIC_LEARNED`). Display `MODEL_DEFINED_FIXED` includes architecture-defined, Q-matrix, and log-derived *fixed* graphs that are not expert maps and not jointly learned. It does **not** mean the graph was not inferred from interaction data. Codebook tokens `TRAIN_ONLY_INFERRED`, `FULL_DATA_INFERRED`, `PRECOMPUTED_UNCLEAR_SPLIT`, and `MIXED_PROVENANCE` are not counted separately in the manuscript.
- Reason: Match the 20-paper IRR workpack tokens; keep one exclusive code per paper.
- Affected records: $N_G=36$ provenance display counts.
- Screening repeated: no
- Coding repeated: no (display rule documented; KT036 recoded separately in DEV-20261106-03)
- Approved by: author execution of score-improvement sequence 1--5 (2026-11-06)

## DEV-20261106-03
- Date: 2026-11-06
- Protocol version before: graph_taxonomy.csv v1.6 (`KT036` `EXTERNAL_FIXED`)
- Protocol version after: graph_taxonomy.csv v1.8 (`KT036` `MODEL_DEFINED_FIXED`)
- Change: TSKT (KT036) recoded from `EXTERNAL_FIXED` / `TEXT_SEMANTICS` to `MODEL_DEFINED_FIXED` / `HETEROGENEOUS_SCHEMA` after PDF check: BERT encodes item text as node features; knowledge-space edges join exercises that share KCs (Sec.~4.2--4.3.1). Not an expert or LLM-extracted skill graph. Display provenance becomes 19 / 8 / 9. SKT (KT016) remains `MODEL_DEFINED_FIXED` under the three-token rule; PDF is mixed (Junyi expert map; ASSISTments correct-transition graph). Capsule GNN (KT052) remains `MODEL_DEFINED_FIXED` (PDF: no expert pre-definition); the 2026-08-26 coding file `EXTERNAL_FIXED` is superseded.
- Reason: Lock display codes to deposited PDFs.
- Affected records: KT036; provenance totals $N_G=36$.
- Screening repeated: no
- Coding repeated: KT036 provenance only
- Approved by: author execution of score-improvement sequence 1--5 (2026-11-06)


## DEV-20261111-01
- Date: 2026-11-11
- Protocol version before: tables/sparse_coldstart_audit.csv (v1 as deposited); manuscript v1.6.26
- Protocol version after: tables/sparse_coldstart_audit_v1.9.csv; manuscript v1.6.27
- Change: (a) `sparse_interaction_drop_eval` corrected from constant YES (37 rows) to YES for KT035 only, matching the H2 overlay; generic-sparsity column dropped. (b) Per-paper 8-way provenance records compared with the 3-token display: 24/36 agree, 5 differ with PDF-level adjudication/recode (KT016, KT036, KT044, KT052, KT076), 7 differ with no PDF-level re-check (KT023, KT035, KT050, KT062, KT064, KT065, KT069). Display 19/8/9 retained; sensitivity 16/8/11 + 1 unclassified reported. (c) AI research assistant role in screening and primary coding disclosed (screening files: screener_id/reviewer_id = AI_ASSISTANT; 41/45 coding files: coder = AI_ASSISTED). (d) Post hoc venue-extension probe (EDM, AIED, LAK, L@S, JEDM, IJAIED) logged; 10 candidates not coded.
- Reason: Reviewer-response revisions; remove contradictions between deposited files and manuscript text; disclose rather than silently reconcile.
- Affected records: sparse/cold-start CSV; provenance reporting; Acknowledgment; search-completeness statement. Not changed: N=37, N_G, N_S, kappa values, 0/37 ECE.
- Screening repeated: no
- Coding repeated: no (sub-bins assigned by rule from coding records; not re-read from PDFs)
- Approved by: author request 2026-11-11 (reviewer-response revision list)

## DEV-20261123-01
- Date: 2026-11-23
- Protocol version before: SCOPE_v1.0_LOCKED §13 (main search window 2015-01-01 to 2026-07-31)
- Protocol version after: locked scope text unchanged; this deviation governs the revision
- Change: Papers read for this revision are eligible when published on or before 23 November 2026. The logged identification search stays 2015-01-01 to 2026-07-31 and $N_{\mathrm{rec}}=2{,}017$. A database rerun through 23 November 2026 is not complete: saved files stop on 14 and 16 November 2026, and ACM Digital Library and Web of Science have no saved file. Itemized counts stay at 37 until full-text rows exist. A print or issue date after 31 July 2026 and on or before 23 November 2026 is inside this revision window. The Crossref record-created date is not used as the publication date.
- Reason: Author decision on 2026-11-23 that papers are updated to the present date.
- Affected records: eligibility of papers found after the July cutoff, including venue-probe VX09 (Crossref print date September 2026). Not changed: N, N_G, N_S, PRISMA arithmetic, locked scope file.
- Screening repeated: no
- Coding repeated: no
- Approved by: author, 2026-11-23

## DEV-20261124-01
- Date: 2026-11-24
- Protocol version before: codebook QA7 (sparse/cold-start construct validity) as applied in the deposited-plus-expansion score file
- Protocol version after: locked scope/codebook text unchanged; two QA7 cells realigned to the locked cold-start decision table
- Change: Set QA7 = 0 for KT035 (HHSKT; all four cold-start constructs NO) and QA7 = 2 for KT023 (SGKT; learner cold-start YES). Recompute HIGH membership for those two papers only. Corpus HIGH/MODERATE counts and mean normalized score remain 13 / 31 / 0.7472.
- Reason: Remove carry-forward inconsistency between QA7 and the locked sparse/cold-start fields before TLT submission.
- Affected records: KT035, KT023 in `data/PRIMARY_CORE_EXPANDED_2026-11-24.csv`; manuscript QA HIGH identifier list; threats wording. Evidence note: `audit/QA7_COLDSTART_ALIGNMENT_2026-11-24.md`.
- Screening repeated: no
- Coding repeated: QA7 only for two papers (aligned to existing cold-start codes; PDFs not re-scored on QA1–QA6/QA8)
- Approved by: author request 2026-11-24 (pre-submission residual fix)

## DEV-YYYYMMDD-XX
- Date:
- Protocol version before:
- Protocol version after:
- Change:
- Reason:
- Affected records:
- Screening repeated: yes/no
- Coding repeated: yes/no
- Approved by:
