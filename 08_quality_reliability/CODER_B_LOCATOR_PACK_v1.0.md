# Coder B locator pack v1.0

AI passage retrieval only. **No codes.** You still fill `inter_rater_coding_sample_BLIND_v1.0.csv`.

Page numbers are **PDF page** (1 = first page of the file), not always the printed footer. Quotes are truncated extracts. If a quote is not enough, open the PDF at that page.

`ECE` search used the strings `ECE`, `Expected Calibration Error`, `Brier`, `calibration`. A reliability plot without the word ECE is still your decision.

KT076 is an image-only scan (0 extractable characters). Quotes below are from page renders in `08_quality_reliability/_kt076_pages/`.

---

## KT004 GKT
`Graph-based Knowledge Tracing - Modeling Student Proficiency Using Graph Neural Network.pdf`

- **Graph / encoder (p.2):** “Inspired by the recent successes of the graph neural network (GNN), we herein propose a GNN-based knowledge tracing method… Casting the knowledge structure as a graph…”
- **Graph source (p.2–3):** “As the knowledge graph structure is not explicitly provided in most cases, we propose various implementations of the graph structure.” / “It is possible for human experts to heuristically and manually annotate… however… we empirically validate…”
- **SSL search:** VAE/NRI text on p.4–5 is about *learning edge types in GKT*, not a named KT pretext table. No `InfoNCE` / `self-supervised` hit as the paper’s own objective.
- **Cold-start / ECE:** no extract hits.

## KT011 Bi-CLKT
`Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf`

- **SSL (p.1–3):** “Inspired by recent advances in self-supervised learning, we propose a Bi-Graph Contrastive Learning based Knowledge Tracing (Bi-CLKT)…” / “two-layer comparative learning scheme”
- **Encoder (p.6–7):** “GCN-based encoder… node-level fφ and graph-level gθ” / GCN formula with adjacency `A`.
- **Graph source (p.5):** exercise influence subgraph from co-correctness / co-occurrence; edge if `Qij e` larger than threshold `τ`.
- **Cold-start / ECE:** no extract hits.

## KT014 PDKT-C
`Prerequisite-Driven Deep Knowledge Tracing.pdf`

- **Graph source (p.1–3):** “incorporate the knowledge structure information, especially the prerequisite relations…” / “model prerequisite concept pairs as ordering pairs” / “this property can be utilized as constraints” / Q-matrix and prerequisite matrix `E` “manually labeled by experts” vs automatic.
- **SSL search:** no extract hits.
- **GNN search:** no `GNN`/`GCN` hit in this paper’s method (constraints + deep KT). Check whether you treat that as `NONE`.
- **Cold-start / ECE:** no extract hits.

## KT026 PEBG
`Improving Knowledge Tracing via Pre-training Question Embeddings.pdf`

- **Pretrain / relations (p.1–3):** “pre-training embeddings for each question on abundant side information” / PEBG “learn a low-dimensional embedding for each question” / “four loss functions… explicit skill-question relations, implicit question similarity and skill similarity, and question difficulty” / “product-based neural networks to recover the side information”
- **Graph (p.2):** question–skill “bipartite graph G = (Q, S, R)”
- **Cold-start search:** “new question” in the standard KT goal (p.2). Check Experiments for a held-out *item* or *KC* protocol; extract did not find `cold-start` / `zero-shot`.
- **ECE:** no extract hit.

## KT031 KSG-AKT
`Knowledge Structure Enhanced Graph Representation Learning Model for Attentive Knowledge Tracing.pdf`

- **Graph source (p.1, 3–4, 7):** skills “linked as a graph (…prerequisite relations)” / Q-matrix “provided by education experts” / “our method learns the KS from learner response data and integrates it with the Q-matrix”
- **Encoder (p.8–9):** Metapath2Vec + “convolutional” question representation; related-work GCN discussion.
- **SSL search:** mentions PEBG pretraining as *related work*; this paper’s own training is embedding + AKT-style attention (confirm Method).
- **Cold-start (p.18):** “predict the learners’ performance on new questions” as an RQ wording. Check whether that is a zero-exposure *KC* hold-out.
- **ECE:** no extract hit.

## KT035 HHSKT
`HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf`

- **Encoder (p.1–2):** “heterogeneous GNN-based model” / “Higher-order relationships between items and skills are extracted by heterogeneous GNN”
- **Graph (p.1):** “constructing a heterogeneous graph-based graph information augmentation component”
- **SSL search:** PEBG listed as related work; no own contrastive/pretext section in extract.
- **Sparsity (p.1):** “sparsity of the interaction records”. Open **Experiments** and search `drop` / subsample — extract did not isolate a zero-exposure KC sentence.
- **ECE:** no extract hit.

## KT037 CMKT
`CMKT - Concept Map Driven Knowledge Tracing.pdf`

- **Graph source (p.1–3):** “utilizes educational concept map for learner modeling” / “pairwise educational relations… formulated as the ordering pairs and are used as mathematical constraints” / “topology information… network embedding” / input includes “a concept map G”
- **SSL search:** no extract hits.
- **GNN search:** method uses constraints + embedding of the map; related-work GNN only in bibliography. Confirm `gnn_encoder`.
- **Sparseness (p.1):** “learner data sparseness” as motivation. No cold-start / ECE extract hits.

## KT038 DyGKT
`DyGKT - Dynamic Graph Learning for Knowledge Tracing.pdf`

- **Graph / encoder (p.1–3):** “Dynamic Graph-based Knowledge Tracing” / “continuous-time dynamic question-answering graph” / “students and questions are represented as nodes”
- **Cold-start (p.2):** “robust on unseen questions” / “ID-embedding-based representation does not provide information for questions not contained in the training data”
- **SSL / ECE:** no extract hits.

## KT039 CL4KT
`Contrastive Learning for Knowledge Tracing.pdf`

- **SSL (p.2–3):** “contrastive learning framework for knowledge tracing” / CL4KT “pulling similar learning histories together and pushing dissimilar learning histories apart”
- **Encoder (p.4):** two **Transformer** encoders (question + interaction), not a GNN block in the extract.
- **Graph (p.6):** optional “chain-type directed acyclic graph based on the question difficulty” for an augmentation (`Repl`). Decide whether that is a central KT graph or sequence-only.
- **Calibration (p.9):** Figure 7 “Calibration binned by predictions on assist09” / “Perfectly calibrated”. No `ECE` string in extract.
- **Split (p.7):** 5-fold “split based on the students”.

## KT042 S2-HHN
`Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf`

- **SSL (p.1–3):** keywords “Contrastive learning / Self-supervised learning” / “we introduce self-supervised learning (SSL)” / “generate multi-views of graphs… contrastive learning”
- **Encoder (p.1):** heterogeneous GNN + hypergraph network.
- **Cold-start (p.2):** “KT usually encounters the cold-start or long-tail problem, i.e., most questions are only interacted by a few students”
- **ECE search:** hits are “calibrated Q-matrix” *related work* (CQKT), not ECE.

## KT043 3V-CLKT / TCL4KT
`Weighted Heterogeneous Graph-Based Three-View Contrastive Learning...pdf`

- **SSL (p.1–3):** “Three-view Contrastive Learning framework for Knowledge Tracing (TCL4KT)” / “Self-supervised learning technology uses pretext tasks”
- **Graph / encoder (p.2–3):** weighted heterogeneous graph; GCN discussed for bipartite graphs; their model uses three view encoders.
- **Cold-start / ECE:** no extract hits.

## KT044 SINKT
`SINKT - A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model.pdf`

- **Graph source (p.1–2):** “SINKT first employs LLMs to generate a concept-question heterogeneous graph”
- **Encoder (p.4–5):** “three different Graph Attention Networks (GAT)” (C-C, C-Q, Q-C) + PLM text encoder + GRU student state.
- **Cold-start / inductive (p.1–2):** “new questions and concepts consistently arrive” / “when a new concept c4 and a new question q5 are added… transductive KT models lack interaction data” / “predictions for newly ingested questions, i.e., realize inductive knowledge tracing”
- **SSL search:** CL4KT cited as related work; SINKT’s own extra signal in extract is LLM graph + inductive setup. Confirm whether a pretext/contrastive loss is defined for SINKT itself.
- **ECE:** no extract hit.

## KT047 DC-SSL / DHGN
`Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph...pdf`

- **SSL (p.1–3):** keywords Contrastive / Self-supervised / “we introduce self-supervised learning into DHGN” / “two channels of DHGN to conduct contrastive learning”
- **Graph / encoder (p.1–4):** heterogeneous GNN; “pre-defined heterogeneous graph between questions”
- **Cold-start (p.3):** MetaHIN cold-start is *recommendation related work*. KT goal uses “new question” (p.4).
- **ECE search:** “calibrated Q-matrix” related work only.

## KT050 GraphCA
`GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf`

- **SSL (p.1–4):** “exploit the counterfactual outcomes in a contrastive learning framework” / “Contrastive learning is a type of self-supervised learning method”
- **Graph / encoder (p.1–3):** heterogeneous graph (students, questions, concepts) + GNN; index terms include graph neural network.
- **Cold-start / ECE:** no extract hits in this pass — still open Experiments.

## KT066 HyperKT
`Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning...pdf`

- **SSL / encoder (p.1):** “cross-view contrastive learning (HyperKT)” / “dual-channel hypergraph encoders” / “simplified hypergraph convolution network and a collaborative hypergraph convolution network” / “To enhance the supervisory signal in the state hypergraphs, we introduce the [contrastive…]”
- **Cold-start / ECE:** check Experiments; not in dedicated extract hits.

## KT068 HKT
`HKT - Hierarchical Structure-Based Knowledge Tracing.pdf`

- **SSL keyword (p.1):** keywords include “Graph contrastive learning”
- **Graph (p.1):** “construct different types of hierarchical graphs” / “intra-hierarchy dependencies and cross-hierarchy relations”
- **Open Method** for whether contrastive is a training loss (not only a keyword) and where the hierarchy comes from (expert curriculum vs learned).
- **Cold-start / ECE:** no extract hits.

## KT070 Coda
`Denoising Programming Knowledge Tracing with a Code Graph-based Tuning Adaptor.pdf`

- **Graph / encoder (p.1–5):** “cluster-aware GCN to the code graph” / “construct an undirected code graph Gu = {Vu, Au}” / adjacency from similarity ranking.
- **SSL search:** CodeBERT is a pretrained encoder; related-work “graph contrastive learning” is not Coda’s stated KT pretext in extract. Method is **denoising / adaptor**.
- **Split (p.7):** 70/10/20 sequence split.
- **Cold-start / ECE:** no extract hits.

## KT076 KGNN-KT (scan)
`KGNN-KT - Enhancing Knowledge Tracing in Programming Education Through LLM-Extracted Knowledge Graphs.pdf`  
Renders: `08_quality_reliability/_kt076_pages/p01.png` … `p11.png`

- **p.1 Abstract:** constructs a knowledge graph by extracting programming concepts from problem descriptions and solutions using LLMs; then processes that graph with student interaction history; reports AUC (not ECE).
- **p.4 §3.1–3.2:** knowledge graph processed via **RGCN**; “The knowledge graph G=(V,E) is constructed through a hybrid approach combining LLM-based parsing and rule-based validation… we employ GPT-4…”
- **p.6–7 §3.5 / §4:** training loss is binary cross-entropy + L2; metrics AUC-ROC and F1; 7:2:1 split; ablation *removes the knowledge graph* (component ablation), not described as a zero-exposure KC hold-out in the rendered experiment pages.
- **SSL:** no contrastive / pretext section on the rendered method pages.
- **ECE:** no ECE string on rendered pages 1, 4, 6–8.

## KT077 R²GCurL
`R2GCurL - Reinforced Robust Knowledge Tracing via Dynamic Graph Curriculum Learning.pdf`

- **Graph (p.1, 8):** “construct dynamic graphs from student responses” / “Exercise–Concept Bipartite Graph Construction… we build a graph at every step”
- **Other mechanisms (p.1–2):** curriculum learning + reinforcement learning scheduler — not described as contrastive SSL in the abstract extract.
- **SSL search:** `pre-training` / `contrastive` hits are **bibliography**, not the method title.
- **Cold-start / ECE:** “new concept region” appears in a noise-vs-topic-switch analysis (p.27), not clearly a hold-out protocol. No ECE hit.

## KT079 STG-SKT / STSKT
`Spatio-Temporal Fusion in Graph Neural Network for Streaming Knowledge Tracing.pdf`

- **Graph (p.1–4):** “dynamic heterogeneous graph” / question co-occurrence, collaboration, temporal proximity edges / streaming GNN
- **SSL search:** “Sequential contrastive learning…” is a **citation** (Wen et al.), not this paper’s method in extract.
- **Cold-start / ECE:** no extract hits.

---

## How to use (15–20 min/paper)

1. Read the 4–6 quotes above.
2. Open the PDF only if a field is still unclear.
3. Write tokens in the **blind** CSV. Put the PDF page in `coderB_locator`.
4. Do not copy a token from this pack — there are none.

When all 20 rows are filled, return only `inter_rater_coding_sample_BLIND_v1.0.csv`.

---

## Experiment locators (pass 2)

Added after a second PDF pass. Still **no codes**.

**KT004 (p.3–4).** Two ways to get a graph: “simple statistics… such as the transition probability of concept answering” vs “learn the graph structure itself.” Statistics-based types: “Dense graph” (uniform `1/(|V|−1)`) and “Transition graph” (`ni,j` counts). NRI/VAE is an implementation option for latent edges, not a named KT contrastive pretext.

**KT014 (p.3–5).** Sequence model is **GRU**, not a GNN. Objective: log-likelihood plus prerequisite inequalities turned into “soft regularization” (PDKT-C).

**KT026 (p.3–4, 5–6).** Reconstruction-style losses: `L1` recovers bipartite `rij` by cross-entropy; `L2`/`L3` implicit similarities; joint `min λ(L1+L2+L3)+(1−λ)L4`. Ablations RER/RIS remove those terms. Evaluation is AUC; “question-level prediction” / sparsity of question interactions — no `cold-start` string. Standard KT wording “new question” is the next-item goal, not automatically a hold-out.

**KT031 (p.4–9).** Own encoder named **Metapath2Vec** + convolutional question representation. GCN appears as *related* (GIKT). KS “learned from learner response data” and combined with expert Q-matrix.

**KT035 (p.6, 8).** “raw data use masks to prevent the relationships to be predicted from being captured in advance.” Split: **5-fold**, 60/20/20 train/val/test — this is a CV split, not by itself a zero-exposure KC protocol. Related-work “cold start” is about KTM, not HHSKT’s own table.

**KT037 (p.1).** Concept map → ordering-pair constraints + “network embedding” of topology + **RNN** for KT. No GNN named in the abstract/method extract.

**KT044 (p.2, 6–7 §5.5).** Figure 1: new concept `c4` and new question `q5` “do not appear in any learning history.” RQ2: “when a new question is added.” **Inductive protocol:** “we remove 1/4 of the question from the training set and evaluate… on these questions.” Ablation: some variants “do not support predicted responses to unseen questions.” Encoder ablation names **GAT**. Decide separately: item hold-out vs strict **KC** zero-exposure (does the 1/4-question removal also withhold every KC?).

**KT050 (p.1–3).** “heterogeneous graph convolutional network”; counterfactual transforms then “contrastive learning between the observational and the counterfactual user representations.”

**KT066 (p.1).** “cross-view contrastive learning mechanism, which performs among state hypergraph views and their transformed line graph views”; hypergraph convolution encoders.

**KT068 (p.2, 5, 7).** “Knowledge Hierarchy Tree (KHT) based on expert prior knowledge”; “cross-graph, hierarchical contrastive learning”; §4.4 hierarchy-oriented contrastive strategy; related-work names InfoNCE; embeddings also use “graph reconstruction” (p.5, p.9). Pick **one** exclusive family if you code S=Y.
