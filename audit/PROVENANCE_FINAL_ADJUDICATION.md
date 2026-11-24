# Provenance adjudication after the seven PDF re-reads

Date: 2026-11-24. Updated same day: KT085 display locked.

Source table: `tables/PROVENANCE_SEVEN_PDF_RECHECK.csv`, plus KT085 Sec. 4.1 re-read in `audit/_a1_evidence/Han2024_fulltext_2026-11-22.txt`.
Each final label uses the manuscript display rule: a fixed graph that is not an expert, curriculum, skill, or supplied LLM map is model-defined fixed; a graph supplied from such an external source is external fixed; a graph whose adjacency is updated as a free parameter during training is dynamically learned.

## Seven papers

| Paper | Display before | PDF final | Changed |
|---|---|---|---|
| KT023 SGKT | MODEL_DEFINED_FIXED | MODEL_DEFINED_FIXED | N |
| KT035 HHSKT | MODEL_DEFINED_FIXED | MODEL_DEFINED_FIXED | N |
| KT050 GraphCA | MODEL_DEFINED_FIXED | MODEL_DEFINED_FIXED | N |
| KT062 LGS-KT | EXTERNAL_FIXED | MODEL_DEFINED_FIXED | Y |
| KT064 MG-Ensemble | MODEL_DEFINED_FIXED | MODEL_DEFINED_FIXED | N |
| KT065 CS-GKT | MODEL_DEFINED_FIXED | MODEL_DEFINED_FIXED | Y against the eight-value record, N against the display |
| KT069 AEGOT-CDKT | DYNAMIC_LEARNED | MODEL_DEFINED_FIXED | Y |

## KT085 (KT-Deeper)

Earlier pass left KT085 as UNCLEAR because the construction-split sentence (train-only vs full data) is missing. That gap belongs to RQ1 `graph_split_statement = NOT_REPORTED`, not to the three-token provenance display.

Sec. 4.1 formulates dynamic graph generation as an MDP and uses reinforcement learning to iteratively update edges of the temporal heterogeneous graph sequence (add or leave edges; actions over node pairs). The adjacency is therefore updated during training as part of the model, so the display token is **DYNAMICALLY_LEARNED**.

## Counts on the expanded corpus

The other deposited graph papers keep the display already in `graph_provenance_8way_audit_v1.9.csv`, except where the seven-PDF table overrides them. Expansion graph papers: KT084, KT086, KT089 = MODEL_DEFINED_FIXED; KT085 = DYNAMICALLY_LEARNED.

Among 40 graph papers:

| Display | Count |
|---|---|
| MODEL_DEFINED_FIXED | 24 |
| EXTERNAL_FIXED | 7 |
| DYNAMICALLY_LEARNED | 9 |
| UNCLEAR | 0 |
| Sum | 40 |

Machine-readable lock file: `data/PRIMARY_CORE_EXPANDED_2026-11-24.csv`.

**PROVENANCE_COUNTS_LOCKED = YES**

Unresolved provenance display count = 0. RQ1 construction-split gaps remain separate and are not reopened here.
