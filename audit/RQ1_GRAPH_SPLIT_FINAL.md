# RQ1 graph-split transparency

Date: 2026-11-24

Source table: `tables/RQ1_GRAPH_SPLIT_TRANSPARENCY.csv`

Corpus: the 44-row expanded file `data/PRIMARY_CORE_EXPANDED_2026-11-23.csv`. Forty of those papers are graph papers. The four sequence-only papers (KT039, KT040, KT087, KT088) have no graph-construction split and are not rows in the table.

Each code below was taken from the deposited PDF. An evaluation split, including an 80/20, 8:2, 7:3, or 8:1:1 sequence or student split, was not treated as a graph-construction statement. A sentence was coded `TRAIN_ONLY_EXPLICIT` only when the paper says the graph, or the log statistic that supplies the graph, was computed from the training data. A sentence was coded `FULL_DATA_EXPLICIT` only when the paper says the graph was computed on the full dataset, including the test portion or before the split. Absence of that sentence is `NOT_REPORTED`.

These integers are counts of papers. This audit does not report a leakage rate and does not convert the counts into a percentage.

## How graph provenance is distributed

Among the 40 graph papers, the regenerated provenance tally is:

| Provenance | Papers |
| --- | ---: |
| Model-defined fixed | 24 |
| External fixed | 7 |
| Dynamically learned | 8 |
| Unclear | 1 |

The unclear paper is KT085 (KT-Deeper). The sum is 40. `PROVENANCE_COUNTS_LOCKED` remains NO: 29 deposited graph papers kept their existing display and were not re-read for provenance in that pass. The printed 19 / 8 / 9 split belongs to the earlier 36-paper display and is not this tally.

Provenance and the construction split are different facts. Model-defined fixed includes a fixed graph whose edges come from the logs, such as a transition count, a session graph, or a co-correctness rate. That label does not say the counts were limited to the training split. External fixed is a supplied expert, curriculum, skill, or LLM map. Dynamically learned means the adjacency is updated as a free parameter during training. Neither label is a train-only or full-data statement about a precomputed log graph.

## Which log-derived graphs document train-only construction

Twenty-four of the 40 graph papers use a graph derived wholly or partly from interaction logs. The structures include transition counts, co-correctness and co-mastery rates, session graphs, directed transition graphs, student-question links, submission graphs, interaction-similarity graphs, response hyperedges, and temporal or collaboration edges.

Two of those 24 papers explicitly document train-only construction:

- KT043 (3V-CLKT), p.4. A weighted heterogeneous graph of students, questions, and skills is constructed according to the training data, and the question-skill weight is the difficulty calculated in the training data.
- KT070 (Coda), p.5. For each practiced question, accepted submissions are collected from the entire training data as the solution set used by the code-graph adaptor. The learnable learner adjacency on p.4 is a separate matrix.

No log-derived paper states that its graph was built on the full dataset, on the data before the split, or with the test interactions included.

`n_train_only_explicit` = 2

`n_full_data_explicit` = 0

`n_not_reported` = 22

## How many log-derived graphs fail to report the construction split

Twenty-two log-derived papers describe how the graph is built and do not say whether that construction used the training split only or the full data. They are KT004, KT011, KT012, KT023, KT029, KT033, KT035, KT038, KT050, KT056, KT060, KT062, KT064, KT065, KT066, KT067, KT068, KT069, KT077, KT079, KT085, and KT086.

Phrases that name the data without naming the split stay in this group. Examples are “all the answered” co-occurred exercises (KT011, KT012), “learning sequences of all students” (KT029), and a tripartite graph “constructed from the dataset” (KT060). Those phrases do not say that the test split was included or excluded.

Sixteen graph papers are `NOT_APPLICABLE`. Their stated edges are a question-skill or exercise-concept relation, an expert or supplied prerequisite or similarity map, a skill or template hyperedge, a capsule or meta-path structure, an association inventory whose method text does not tie the edges to answer counts, or an LLM-extracted graph. KT076 has an empty text layer (11 pages; both extractors return 0 characters), so its methods pages could not be searched; the row follows the file title and the recorded LLM-extracted graph source. These 16 papers are outside the three counts above.

## Why a missing split statement blocks a leakage-free claim

A log-derived edge is a statistic of interactions: who answered what, what followed what, which exercises were correct together, or which submissions were accepted. If that statistic is computed on the whole log, responses that belong to the test portion can enter the adjacency that the model later uses when it scores those same responses. The result is leakage through the graph, even when the prediction loss is trained only on the training sequences.

The papers that omit the split do not show that this happened. They also do not show that it was avoided. An evaluation split tells which sequences or students are held out for scoring. It does not rebuild the co-occurrence, transition, session, similarity, or student-question graph on the training portion alone. Unless the paper states that restriction, a reader cannot claim that the graph is leakage-free. The 22 `NOT_REPORTED` papers are papers for which that claim is not documented. They are not a measured leakage rate.

## Sentences that were not used as the paper's own split

- KT026 computes question difficulty from the training dataset. That sentence defines the difficulty vector. The graph is the binary question-skill adjacency, so the paper is `NOT_APPLICABLE`.
- KT033 criticizes earlier graphs as predefined on training-data ground truth. That sentence is about prior methods. DGMN's own latent graph remains `NOT_REPORTED`.
- KT036 counts node frequency along a meta-path in order to choose aggregation neighbors. That is a sampling step inside a heterogeneous attribute graph, not a log-count adjacency and not a split statement.
- KT044 says that GKT extracts a transition graph from training data. That sentence describes the GKT baseline. SINKT's own graph is the GPT-4 concept-question graph and is `NOT_APPLICABLE`.
- KT077 selects a subset of the training dataset inside the training scheduler. That sentence chooses which training rows update the model. It does not say the dynamic response graph excludes test interactions.
