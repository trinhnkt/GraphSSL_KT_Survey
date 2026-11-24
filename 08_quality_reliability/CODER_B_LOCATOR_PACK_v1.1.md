# Coder B locator pack v1.1

Mỗi paper: **4–6 câu trích** + **số trang PDF** (trang 1 = trang đầu file). Không mã `Y/N`.

Bốn mục: **SSL** · **Graph** · **Cold-start** · **ECE**.  
`[no hit]` = không thấy chuỗi tìm kiếm trong PDF (hoặc chỉ bài *khác* ở phần related/references).

KT076: PDF scan; trang = `08_quality_reliability/_kt076_pages/pNN.png`.

B điền 8 ô vào `inter_rater_coding_sample_BLIND_EMPTY_v1.3.csv`. Handoff: `CODER_B_HANDOFF_v1.3.md`. Không mở `BLIND_EMPTY_v1.2.csv` / `BLIND_v1.0.csv` (bản AI).

---

## KT004 GKT
File: `Graph-based Knowledge Tracing - Modeling Student Proficiency Using Graph Neural Network.pdf`

1. **SSL (p.4):** “Neural relational inference (NRI) leverages a variational autoencoder (VAE) to learn the latent graph structure in an unsupervised manner.” (cách dựng cạnh GKT, không phải InfoNCE/pretext KT.)
2. **Graph (p.2):** “Inspired by the recent successes of the graph neural network (GNN), we herein propose a GNN-based knowledge tracing method… Casting the knowledge structure as a graph…”
3. **Graph (p.4):** “Dense graph is a simple densely connected graph… Transition graph is a transition probability matrix, where Ai,j is ni,j / Σk ni,k…”
4. **Cold-start:** `[no hit]` (`cold-start`, `zero-shot`, `unseen concept`).
5. **ECE:** `[no hit]` (`ECE`, `Expected Calibration Error`, `Brier`).

## KT011 Bi-CLKT
File: `Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf`

1. **SSL (p.1):** “Inspired by recent advances in self-supervised learning, we propose a Bi-Graph Contrastive Learning based Knowledge Tracing (Bi-CLKT)…”
2. **SSL (p.3):** “Through contrastive self-supervised learning, we solve a number of problems encountered by traditional GNN-based knowledge-tracing models…”
3. **Graph (p.6):** “GCN-based encoder. GCN-based encoders node-level fφ and graph-level gθ for augmented graphs…”
4. **Graph (p.5):** “Edge Ee(Vje, Vie) only exists when Qije is larger than a certain threshold τ” (co-correctness / co-occurrence).
5. **Cold-start:** `[no hit]`.
6. **ECE:** `[no hit]`.

## KT014 PDKT-C
File: `Prerequisite-Driven Deep Knowledge Tracing.pdf`

1. **SSL:** `[no hit]` (`self-supervised`, `contrastive`, `InfoNCE`, `pretext`).
2. **Graph (p.1):** “We advocate for and propose to incorporate the knowledge structure information, especially the prerequisite relations between pedagogical concepts…”
3. **Graph (p.3):** “A prerequisite matrix E… Identifying the prerequisite… manually labeled by experts.”
4. **Graph (p.3–5):** “We model each exercise sequence si with a Gated Recurrent Unit (GRU)…” / prerequisites as “soft regularization” (không GNN trong extract).
5. **Cold-start:** `[no hit]`.
6. **ECE:** `[no hit]`.

## KT026 PEBG
File: `Improving Knowledge Tracing via Pre-training Question Embeddings.pdf`

1. **SSL (p.3):** “PEBG pre-trains question embeddings using four loss functions… explicit skill-question relations, implicit question similarity and skill similarity, and question difficulty.”
2. **SSL (p.3):** “the local proximity is enforced to be close to skill-question relations in the bipartite graph via a cross-entropy loss function: L1(Q,S)=…”
3. **Graph (p.2):** “the question-skill relations can be naturally represented as a bipartite graph G = (Q, S, R)…”
4. **Cold-start (p.2):** “predict the probability that the student will correctly answer a new question, i.e., P(ct=1|qt,X).” (mục tiêu next-item; `[no hit]` cho `cold-start` / `zero-shot`.)
5. **ECE:** `[no hit]`.

## KT031 KSG-AKT
File: `Knowledge Structure Enhanced Graph Representation Learning Model for Attentive Knowledge Tracing.pdf`

1. **SSL (p.6):** PEBG “pretrained the question and skill embedding…” — *related work*, không phải loss của KSG-AKT trong extract.
2. **Graph (p.3):** “The question–skill mapping information is typically encoded as a Q-matrix of prior knowledge provided by education experts…”
3. **Graph (p.7):** “our method learns the KS from learner response data and integrates it with the Q-matrix… Leveraging the Metapath2Vec method…”
4. **Graph (p.20):** “GIKT … using a GCN” is the **baseline** row. Same page: “To embed the nodes … using Metapath2Vec…” Table: “Our model / Metapath2Vec / Convolutional dense embedding.”
5. **Cold-start (p.18):** “how well does KSGKT predict the learners’ performance on new questions?” (câu RQ; chưa thấy hold-out KC zero-exposure.)
6. **ECE:** `[no hit]`.

## KT035 HHSKT
File: `HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf`

1. **SSL:** `[no hit]` cho pretext của HHSKT (PEBG chỉ ở bảng related).
2. **Graph (p.2):** “This work proposes HHSKT, a heterogeneous GNN-based model… Higher-order relationships between items and skills are extracted by heterogeneous GNN…”
3. **Graph (p.6):** “The raw data use masks to prevent the relationships to be predicted from being captured in advance.”
4. **Cold-start (p.8):** “5-fold cross-validation… 20% within each fold was used for testing, 20% for validation, and 60% for training.” (CV learner-fold, không phải zero-exposure KC trong extract.)
5. **ECE:** `[no hit]`.

## KT037 CMKT
File: `CMKT - Concept Map Driven Knowledge Tracing.pdf`

1. **SSL:** `[no hit]`.
2. **Graph (p.1):** “a novel concept map driven knowledge tracing (CMKT) model, which utilizes educational concept map for learner modeling.”
3. **Graph (p.1):** “The pairwise educational relations in the concept map are formulated as the ordering pairs and are used as mathematical constraints… topology information… network embedding… CMKT adopts the recurrent neural network…”
4. **Cold-start (p.1):** “addresses the issue of learner data sparseness…” (động cơ; `[no hit]` `cold-start` / `zero-shot`.)
5. **ECE:** `[no hit]`.

## KT038 DyGKT
File: `DyGKT - Dynamic Graph Learning for Knowledge Tracing.pdf`

1. **SSL:** `[no hit]`.
2. **Graph (p.1):** “we propose a Dynamic Graph-based Knowledge Tracing model, namely DyGKT… a continuous-time dynamic question-answering graph…”
3. **Graph (p.2):** “students and questions are represented as nodes, while the [answering behaviors are edges]…”
4. **Cold-start (p.2):** “the prediction should be multi-step and robust on unseen questions… the ID-embedding-based representation does not provide information for questions not contained in the training data.”
5. **ECE:** `[no hit]`.

## KT039 CL4KT
File: `Contrastive Learning for Knowledge Tracing.pdf`

1. **SSL (p.3):** “we propose a contrastive learning (CL) framework for KT, named CL4KT… pulling similar learning histories together and pushing dissimilar learning histories apart…”
2. **Graph (p.4):** “To encode a series of questions and interactions, we employ two Transformer encoders… a question encoder and an interaction encoder.” (không GNN trong extract.)
3. **Graph (p.6):** “we posit that the knowledge structure is a chain-type directed acyclic graph based on the question difficulty” (augmentation `Repl`).
4. **Cold-start (p.7):** “We perform 5-fold cross-validation… folds are split based on the students.”
5. **ECE (p.9):** Figure 7: “Calibration binned by predictions on assist09” / “Perfectly calibrated.” `[no hit]` chuỗi `ECE`.

## KT042 S2-HHN
File: `Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf`

1. **SSL (p.2–3):** “we introduce self-supervised learning (SSL) into our model… we generate multi-views of graphs in different manners to conduct contrastive learning.”
2. **Graph (p.1):** keywords: “Heterogeneous graph neural network; Hypergraph network; Contrastive learning; Self-supervised learning.”
3. **Cold-start (p.2):** “KT usually encounters the cold-start or long-tail problem, i.e., most questions are only interacted by a few students.”
4. **ECE (p.2):** “calibrated Q-matrix (CQKT)” — *bài related*, không phải ECE của S2-HHN.
5. **ECE (this paper):** `[no hit]` `Expected Calibration Error`.

## KT043 3V-CLKT
File: `Weighted Heterogeneous Graph-Based Three-View Contrastive Learning for Knowledge Tracing in Personalized e-Learning Systems.pdf`

1. **SSL (p.1):** “we propose… weighted heterogeneous graph-based Three-view Contrastive Learning framework for Knowledge Tracing (TCL4KT).”
2. **SSL (p.2):** “Self-supervised learning technology uses pretext tasks to extract supervision information from large-scale unsupervised data…”
3. **Graph (p.2):** “we expand the heterogeneous graph to a weighted heterogeneous graph, and employ the contrastive learning method…”
4. **Cold-start:** `[no hit]`.
5. **ECE:** `[no hit]`.

## KT044 SINKT
File: `SINKT - A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model.pdf`

1. **SSL (p.2):** CL4KT cited as related (“positive and negative sample pairs… contrastive learning”). `[no hit]` pretext/contrastive *của SINKT*.
2. **Graph (p.2):** “SINKT first employs LLMs to generate a concept-question heterogeneous graph…”
3. **Graph (p.4):** “We apply three different Graph Attention Networks (GAT) to aggregate neighborhood information…”
4. **Cold-start (p.2):** “when a new concept c4 and a new question q5 are added… transductive KT models lack interaction data to learn their representations.”
5. **Cold-start (p.7 §5.5):** “we remove 1/4 of the question from the training set and evaluate the model’s prediction accuracy on these questions…”
6. **ECE:** `[no hit]`.

## KT047 DC-SSL
File: `Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing.pdf`

1. **SSL (p.2):** “we introduce self-supervised learning into DHGN… we utilize the question representations learned by the two channels of DHGN to conduct contrastive learning…”
2. **Graph (p.1):** keywords: “Heterogeneous graph neural network; Contrastive learning; Self-supervised learning.”
3. **Graph (p.4):** “Given a student’s interactive sequence… and the pre-defined heterogeneous graph between questions G…”
4. **Cold-start (p.3):** MetaHIN “cold-start problem of recommendation systems” — *related*. KT goal: “predict… a new question” (p.4).
5. **ECE:** `[no hit]` (chỉ “calibrated Q-matrix” related).

## KT050 GraphCA
File: `GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf`

1. **SSL (p.1):** “exploit the counterfactual outcomes in a contrastive learning framework.” Index terms: “Contrastive learning…”
2. **SSL (p.3):** “we further conduct contrastive learning between the observational and the counterfactual user representations.”
3. **Graph (p.1):** “leverage a heterogeneous graph convolutional network to conduct representation learning.”
4. **Cold-start (p.15):** “heterogeneous graph neural model for cold-start recommendation” — *reference khác*. `[no hit]` protocol cold-start KT.
5. **ECE:** `[no hit]`.

## KT066 HyperKT
File: `Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing.pdf`

1. **SSL (p.1–2):** “we introduce the cross-view contrastive learning mechanism, which performs among state hypergraph views and their transformed line graph views.”
2. **Graph (p.1):** “dual-channel hypergraph encoders… a simplified hypergraph convolution network and a collaborative hypergraph convolution network.”
3. **Cold-start (p.7):** “the new question embedding concatenates…” (công thức next-item; `[no hit]` `cold-start` / `zero-shot`.)
4. **ECE:** `[no hit]`.
5. **SSL extra (p.3):** mục “C. Contrastive Learning” — self-supervised representation (bối cảnh phương pháp).

## KT068 HKT
File: `HKT - Hierarchical Structure-Based Knowledge Tracing.pdf`

1. **SSL (p.2):** “These embeddings are further refined through the application of a cross-graph, hierarchical contrastive learning strategy.”
2. **SSL (p.7):** “4.4. Hierarchical contrastive learning We propose a hierarchy-oriented knowledge contrastive learning strategy…”
3. **Graph (p.2):** “we introduce a Knowledge Hierarchy Tree (KHT) based on expert prior knowledge…”
4. **Graph (p.5):** “embedding training through graph reconstruction and cross-graph hierarchical contrastive learning.”
5. **Cold-start:** `[no hit]`.
6. **ECE:** `[no hit]`.

## KT070 Coda
File: `Denoising Programming Knowledge Tracing with a Code Graph-based Tuning Adaptor.pdf`

1. **SSL (p.7):** “We utilize a pre-trained Code-Bert to encode input codes…” (encoder pretrained; `[no hit]` pretext KT kiểu InfoNCE trong method.)
2. **Graph (p.1):** “We then apply a cluster-aware GCN to the code graph…”
3. **Graph (p.4):** “construct an undirected code graph Gu={Vu,Au} where Au is the learnable adjacency matrix…”
4. **Cold-start:** `[no hit]`. Split (p.7): “70%, 10% and 20% programming sequences… train / valid / test.”
5. **ECE:** `[no hit]`.

## KT076 KGNN-KT
File: `KGNN-KT - Enhancing Knowledge Tracing in Programming Education Through LLM-Extracted Knowledge Graphs.pdf`  
Ảnh: `_kt076_pages/p01.png` … `p11.png`

1. **SSL (p.6–7):** loss “binary cross-entropy… and L2 regularization.” `[no hit]` contrastive / pretext trên trang method đã render.
2. **Graph (p.1):** “first constructs a comprehensive knowledge graph by extracting programming concepts from problem descriptions and solutions using LLMs…”
3. **Graph (p.4):** “The knowledge graph is processed via RGCN…” / “constructed through a hybrid approach combining LLM-based parsing… we employ GPT-4…”
4. **Cold-start (p.7):** “split 7:2:1 for training/validation/testing”; ablation “Removing the knowledge graph…” (component ablation, không mô tả zero-exposure KC trên trang đã đọc).
5. **ECE (p.7–8):** metric “AUC-ROC and F1-score.” `[no hit]` ECE.

## KT077 R²GCurL
File: `R2GCurL - Reinforced Robust Knowledge Tracing via Dynamic Graph Curriculum Learning.pdf`

1. **SSL:** `[no hit]` trong method; `contrastive` / `pre-training` ở **tài liệu tham khảo**.
2. **Graph (p.1):** “we recast KT as a graph classification problem and construct dynamic graphs from student responses…”
3. **Graph (p.8):** “Exercise–Concept Bipartite Graph Construction… we build a graph at every step 1≤t≤T.”
4. **Cold-start (p.27):** “A topic switch typically produces a coherent transition into a new concept region…” (phân tích nhiễu vs đổi topic, không phải bảng hold-out.)
5. **ECE:** `[no hit]`.

## KT079 STG-SKT
File: `Spatio-Temporal Fusion in Graph Neural Network for Streaming Knowledge Tracing.pdf`

1. **SSL (p.15):** “Sequential contrastive learning for progressive knowledge tracing” — *citation*, không phải method STSKT trong extract.
2. **Graph (p.2):** “We propose a dynamic heterogeneous graph construction method…”
3. **Graph (p.4):** “dynamic heterogeneous graph Gt=(Vt,Et)… question co-occurrence edge… collaboration association edge… temporal proximity edges.”
4. **Cold-start:** `[no hit]`.
5. **ECE:** `[no hit]`.

---

20 paper × (SSL / Graph / Cold-start / ECE). Câu `[no hit]` cũng là locator: mở PDF, Ctrl+F các từ trên, rồi ghi token.
