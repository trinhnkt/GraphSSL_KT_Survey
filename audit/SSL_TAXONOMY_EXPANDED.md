# SSL taxonomy after corpus expansion

Date: 2026-11-24

Coding table: `tables/SSL_EXPANDED_CODING.csv`

Crosstab: `tables/SSL_PARADIGM_BY_VIEW.csv`

Figure: `tables/SSL_TAXONOMY_EXPANDED.png`

The live manuscript was not edited. The section below is the rewritten Section IV for the expanded corpus.

The old four-family table put each SSL paper in one of multi-view contrastive, graph contrastive, sequence contrastive, or graph reconstruction. That table had nine papers. This pass re-read the SSL objective of those nine and of the seven papers added on 2026-11-23. Each paper now has one supervisory signal and one view object. A paper is not forced back into the four families.

`N_S` = 16

`N_G_AND_S` = 12

`N_S` is the number of expanded-corpus papers whose SSL objective is documented below. `N_G_AND_S` is the number of those papers whose SSL objective uses a graph. The other four SSL papers do not. The graph flag was not reopened for papers outside this SSL set. The check against the expanded corpus is 40 graph papers, of which 12 are also in this SSL set, and 16 SSL papers, of which 4 are not graph papers: 40 + 16 − 12 = 44.

## What the crosstab shows

Fifteen papers use a contrastive loss. One paper, PEBG (KT026), reconstructs the question-skill bipartite graph and does not define a contrastive pair. No paper uses a consistency loss that lacks negatives, a predictive pretext separate from the supervised next-response loss, or a view that had to be coded `MULTIVIEW` or `OTHER`.

The view object is where the old families break.

| View object | Contrastive | Generative reconstruction |
| --- | ---: | ---: |
| Sequence | 3 | 0 |
| Graph | 3 | 1 |
| Heterogeneous graph | 5 | 0 |
| Hypergraph | 2 | 0 |
| Momentum encoder | 1 | 0 |
| Collaborative student | 1 | 0 |

Empty cells for consistency, predictive, and other signals are omitted. The figure uses the same axes.

## Rewritten Section IV

### IV.1 What kinds of SSL supervisory signals are used?

The expanded SSL set uses two supervisory signals.

Contrastive alignment is the signal in 15 of 16 papers. The implemented losses are NT-Xent (Bi-CLKT), InfoNCE (S2-HHN, 3V-CLKT, DC-SSL, GraphCA, HyperKT, DECKT, CoSKT, CLBG), a mutual-information form of the same idea (KT-Deeper), or a contrastive loss written without the name InfoNCE (CL4KT, DTransformer, HKT, SP-CLKT, HCMKT). In each case the loss pulls a stated positive pair together and pushes other samples away.

Generative reconstruction is the signal in PEBG. A cross-entropy term reconstructs the observed question-skill edges, and a second term regresses question difficulty. There is no contrastive pair.

Two papers do not fit a single exclusive family even inside this coding. HKT trains a parent-child score on the knowledge hierarchy and a cross-graph contrast, and it also names graph reconstruction in the same embedding stage. The row is coded contrastive because the published objective scores positive parent-child pairs against negative nodes; the reconstruction term is recorded in the target field. CoSKT describes its goal as consistency between an individual state and a common state, and then defines that goal as InfoNCE with batch negatives. The row is coded contrastive. A consistency code would hide the negatives.

The supervised next-response loss is present throughout the set. It is the KT objective, not a second SSL family, so none of these papers is coded predictive.

### IV.2 What object is contrasted, reconstructed, or aligned?

The positive object depends on the view.

Sequence. CL4KT aligns two augmented views of the same learning history. DTransformer aligns knowledge states diagnosed from two augmented sequences of the same learner. SP-CLKT contrasts an answer-sequence sample with a positive sample `z+` and splits the negative term into local samples and overall samples. The equation does not give `z+` a further definition.

Graph. Bi-CLKT aligns two augmented views of an exercise graph and of a concept graph, both at node level and at graph level. CLBG aligns a node with the same node after edge augmentation of the exercise-concept graph and of the two same-type correlation graphs. HKT scores a parent node against its child in the knowledge hierarchy, and aligns embeddings across the hierarchy and the association graph. PEBG reconstructs question-skill edges rather than aligning two views.

Heterogeneous graph. 3V-CLKT aligns a question across a meta-path view, a neighbor-sampling view, and a KT view. DC-SSL aligns the meta-path channel and the network-schema channel of the same question. GraphCA aligns an observed student representation with a counterfactual representation on the student-question-concept graph. KT-Deeper aligns a local node embedding with the global summary of a temporal heterogeneous graph. HCMKT aligns the coarse-view and fine-grained-view embeddings of the same question, and adds a prototype term against cluster centers.

Hypergraph. S2-HHN aligns a node with its representation in an adaptively augmented hypergraph view. HyperKT aligns a global or local state-hypergraph encoding with the encoding of the corresponding line graph.

Momentum encoder. DECKT aligns the primary-encoder embedding and the momentum-encoder embedding of the same question node and of the same concept node. The graph is the intact question-concept bipartite graph. The two views are two encoders, not two corrupted graphs.

Collaborative student. CoSKT aligns a student's individual knowledge state with the common knowledge state of similar students.

### IV.3 Which augmentations are used?

Sequence operations are question masking, interaction cropping, interaction permutation, and difficulty-directed question replacement (CL4KT); response flipping, item dropping, and adjacent swapping (DTransformer); and skill replacement plus subsequence reordering (SP-CLKT). SP-CLKT also reports masking and clipping in a comparison table.

Graph operations are random edge deletion or addition, node deletion, and attribute masking (Bi-CLKT); random edge addition and deletion (CLBG); adaptive node dropout (S2-HHN); feature masking and edge masking (HCMKT); and replacement of questions by similar questions, with a destructive transformation used as the negative (GraphCA).

Several contrastive papers do not augment the input. DC-SSL contrasts two channels of one heterogeneous graph. DECKT contrasts two encoders of the intact graph. CoSKT contrasts two knowledge states and does not alter the sequence. HKT takes pairs from the hierarchy rather than from a stated perturbation. HyperKT builds negatives by row-wise and column-wise shuffling. KT-Deeper writes the negative graph as `tau` of the original features and adjacency and does not name `tau`.

### IV.4 Which methods explicitly preserve educational structure?

Four papers state an educational constraint in the SSL objective or in the augmentation rule.

- PEBG trains the embedding so that explicit question-skill relations are preserved.
- HKT uses parent-child pairs in the knowledge hierarchy as the positive pairs.
- DECKT adds a graph-structure constraint that pulls embeddings of connected question-concept pairs together, and it does not drop edges or mask features to make the contrastive views.
- SP-CLKT replaces a correctly answered question with an easier one and an incorrectly answered question with a harder one, and states that this keeps the student's mastery. Its reordering step is justified by the assumption that proficiency stays constant while the student is solving.

Five papers use a partial constraint: CL4KT directs one of four augmentations toward easier or harder questions; S2-HHN lowers the dropout probability of important nodes; 3V-CLKT masks non-question nodes after meta-path sampling; GraphCA replaces questions with similar questions; HyperKT builds hyperedges from skill similarity and response patterns while its negatives are shuffled copies.

Four papers use random or unconstrained perturbation and do not state a structure constraint: Bi-CLKT, DTransformer, HCMKT, and CLBG. DC-SSL and CoSKT have no augmentation. KT-Deeper does not say whether `tau` preserves educational structure, so that cell stays unclear.

The earlier statement that every coded SSL model explicitly enforces a structural constraint does not hold on this reading.

### IV.5 Which SSL approaches are sequence-only, and which are graph-based?

Twelve SSL papers use a graph in the SSL objective: Bi-CLKT, PEBG, S2-HHN, 3V-CLKT, DC-SSL, GraphCA, HyperKT, HKT, DECKT, KT-Deeper, HCMKT, and CLBG. These are the 12 papers in `N_G_AND_S`. They are not one graph family. Five contrast views of a heterogeneous graph, three contrast or reconstruct an ordinary or bipartite graph, two contrast a hypergraph, and one contrasts two encoders of an intact bipartite graph.

Four SSL papers do not use a graph. Three of them contrast augmented learning sequences: CL4KT, DTransformer, and SP-CLKT. CoSKT is the fourth. Its encoder is a sequence model, and its SSL pair is a student state against similar students' common state, so it is collaborative rather than a sequence augmentation and rather than a graph view.

## Why the four-family table is not extended

Appending the seven new papers to multi-view, graph, sequence, and reconstruction would hide the distinctions this reading supports. DECKT would be filed as graph contrastive even though it does not augment the graph. CoSKT would be filed as sequence contrastive even though the positive pair is another student's common state. HCMKT, DC-SSL, and 3V-CLKT would share one multi-view cell even though each contrasts named channels of a heterogeneous graph. HKT would have to drop either its contrastive pair or its reconstruction term. The crosstab keeps the signal and the object separate, which is the distinction the expanded set requires.
