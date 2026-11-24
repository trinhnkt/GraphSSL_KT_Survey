# -*- coding: utf-8 -*-
"""Write the expanded SSL coding table, crosstab, and taxonomy figure."""
import csv
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
CSV_PATH = ROOT / "tables" / "SSL_EXPANDED_CODING.csv"
CROSS_PATH = ROOT / "tables" / "SSL_PARADIGM_BY_VIEW.csv"
FIG_PATH = ROOT / "tables" / "SSL_TAXONOMY_EXPANDED.png"

# graph_used follows the SSL objective, which matches G_criterion for these 16 papers.
# G flags are carried from the expanded corpus and were not reopened here.
G = {
    "KT011": "Y", "KT026": "Y", "KT039": "N", "KT040": "N", "KT042": "Y",
    "KT043": "Y", "KT047": "Y", "KT050": "Y", "KT066": "Y", "KT068": "Y",
    "KT084": "Y", "KT085": "Y", "KT086": "Y", "KT087": "N", "KT088": "N",
    "KT089": "Y",
}

rows = [
    ["KT011", "Bi-CLKT", "CONTRASTIVE", "GRAPH",
     "NT-Xent on exercise-to-exercise and concept-to-concept graphs, at node level and graph level",
     "Two augmented views of the same graph (graph level), or the same node across those two views (node level)",
     "Other graphs at graph level, and other nodes at node level",
     "Random edge deletion or addition, node deletion, and attribute masking",
     "NO_EXPLICIT_CONSTRAINT", G["KT011"],
     "p.6 and p.8"],
    ["KT026", "PEBG", "GENERATIVE_RECONSTRUCTION", "GRAPH",
     "Cross-entropy reconstruction of explicit question-skill edges, with a separate difficulty regression",
     "Not a contrastive pair. The target is the observed question-skill relation",
     "Not a contrastive pair. Non-edges enter the cross-entropy as the negative class of the relation",
     "No view augmentation. The pretext is reconstruction of the bipartite question-skill graph",
     "YES_EXPLICIT", G["KT026"],
     "p.3, explicit question-skill loss L1; p.4, joint optimization"],
    ["KT039", "CL4KT", "CONTRASTIVE", "SEQUENCE",
     "Contrastive loss on encoded question histories and interaction histories",
     "Two augmented views of the same learning history, s+1 and s+2",
     "Other histories in the batch, plus hard negatives made by changing responses",
     "Question mask, interaction crop, interaction permutation, and question replacement by an easier or harder question",
     "PARTIAL", G["KT039"],
     "p.5, Sec. 3.4-3.5; p.6, Sec. 3.6"],
    ["KT040", "DTransformer", "CONTRASTIVE", "SEQUENCE",
     "Contrastive loss on knowledge states diagnosed from augmented learning histories",
     "Knowledge states from two augmented sequences of the same learner",
     "Knowledge states of other learners in the batch",
     "Flip response, drop item, and swap adjacent question-response pairs",
     "NO_EXPLICIT_CONSTRAINT", G["KT040"],
     "Sec. 3.3.1, Eq. (17)"],
    ["KT042", "S2-HHN", "CONTRASTIVE", "HYPERGRAPH",
     "InfoNCE between a node and its representation in an adaptively augmented hypergraph view",
     "Views of the same node",
     "Views of different nodes, with a further negative set of nodes that share a hyperedge",
     "Adaptive node dropout, with dropout probability adjusted by node importance",
     "PARTIAL", G["KT042"],
     "p.1 and p.3; p.8-p.9, InfoNCE"],
    ["KT043", "3V-CLKT", "CONTRASTIVE", "HETEROGENEOUS_GRAPH",
     "InfoNCE between the meta-path view and the neighbor-sampling view, and between the meta-path view and the KT view, of the same question",
     "The positive set P_i of the target question node in another view",
     "The remaining nodes N_i in that view",
     "Three relation views of one heterogeneous graph; non-question nodes are masked after meta-path sampling",
     "PARTIAL", G["KT043"],
     "p.4 and p.5, Eq. (11)"],
    ["KT047", "DC-SSL", "CONTRASTIVE", "HETEROGENEOUS_GRAPH",
     "InfoNCE between the meta-path channel and the network-schema channel of the same question node",
     "The two channel views of the same node",
     "Channel views of different nodes",
     "No input augmentation. The two views are the meta-path channel and the network-schema channel",
     "NO_AUGMENTATION", G["KT047"],
     "p.5, InfoNCE on the two channels"],
    ["KT050", "GraphCA", "CONTRASTIVE", "HETEROGENEOUS_GRAPH",
     "InfoNCE, written with binary cross-entropy, between an observed student representation and a counterfactual student representation on the student-question-concept graph",
     "The student representation after the first counterfactual transformation",
     "A destructed transformation of the same student representation",
     "Counterfactual replacement of questions by similar questions, plus a destructive transformation used as the negative",
     "PARTIAL", G["KT050"],
     "p.5, Sec. III; p.9, Eq. (20)"],
    ["KT066", "HyperKT", "CONTRASTIVE", "HYPERGRAPH",
     "InfoNCE between a state-hypergraph encoding and the encoding of its line graph, computed separately for global and local states",
     "A global or local state encoding and the corresponding line-graph encoding",
     "The same pair after row-wise and column-wise shuffling of the hypergraph",
     "No separate random view augmentation. Negatives are shuffled copies. Hyperedges are distilled from skill similarity and response patterns",
     "PARTIAL", G["KT066"],
     "p.7-p.8, Eqs. (20)-(21)"],
    ["KT068", "HKT", "CONTRASTIVE", "GRAPH",
     "Parent-child score on the knowledge hierarchy, together with cross-graph hierarchical contrast between the hierarchy and the association graph. The paper also names graph reconstruction as part of the same embedding stage",
     "A parent-child pair in the knowledge hierarchy",
     "Other nodes sampled as the negative set",
     "No stated node, edge, or sequence perturbation. The pairs come from the hierarchy and from the cross-graph alignment",
     "YES_EXPLICIT", G["KT068"],
     "p.5, figure caption; p.7, Eqs. (15)-(16)"],
    ["KT084", "DECKT", "CONTRASTIVE", "MOMENTUM_ENCODER",
     "InfoNCE between primary-encoder and momentum-encoder embeddings, plus a graph-structure constraint on connected question-concept pairs",
     "The same question node, or the same concept node, encoded by the primary encoder and by the momentum encoder",
     "Different nodes in the batch",
     "No explicit augmentation. Views come from the intact bipartite graph through a momentum encoder",
     "YES_EXPLICIT", G["KT084"],
     "Sec. 3.2 and Sec. 3.5; InfoNCE and graph-structure constraint"],
    ["KT085", "KT-Deeper", "CONTRASTIVE", "HETEROGENEOUS_GRAPH",
     "Mutual-information loss between a local node representation and the global summary of a temporal heterogeneous graph",
     "A node embedding and the global summary of the same graph",
     "A corrupted graph instance produced by an operator tau",
     "The negative graph is tau of the original features and adjacency. The paper does not name the corruption",
     "UNCLEAR", G["KT085"],
     "p.2; Sec. 4.2, Eq. (4)"],
    ["KT086", "HCMKT", "CONTRASTIVE", "HETEROGENEOUS_GRAPH",
     "Contrastive loss between coarse-view and fine-grained-view embeddings of the same question, plus a prototype contrastive loss",
     "The coarse-view embedding of a question and its fine-grained-view embedding; for the prototype term, the question and its cluster-center prototype",
     "Other question nodes, reweighted by clustering; prototype vectors outside the node's cluster",
     "Feature masking and edge masking on the fine-grained view",
     "NO_EXPLICIT_CONSTRAINT", G["KT086"],
     "Sec. 4.1, feature and edge masking; Sec. 4.4, Eqs. (15)-(16)"],
    ["KT087", "CoSKT", "CONTRASTIVE", "COLLABORATIVE_STUDENT",
     "InfoNCE that the paper describes as encouraging consistency between a student's individual knowledge state and the common state of similar students",
     "The individual knowledge state of student u at step t and the common knowledge state of that student's similar students",
     "The other individual and common states in the mini-batch",
     "No input augmentation",
     "NO_AUGMENTATION", G["KT087"],
     "Sec. III-D, Eqs. (12)-(13). The paper names Lssf as InfoNCE"],
    ["KT088", "SP-CLKT", "CONTRASTIVE", "SEQUENCE",
     "Contrastive loss on student answer sequences, with the denominator split into local-sample and overall-sample terms",
     "z+ , called the positive sample of answer-sequence sample f. The equation does not give z+ a further definition",
     "Local-sample terms and overall-sample terms in the denominator, with weight mu on the local term",
     "Skill replacement by difficulty order, and reordering inside a subsequence. A comparison table also reports masking and clipping",
     "YES_EXPLICIT", G["KT088"],
     "Sec. 3.3, skill replacement; Sec. 3.4, Eq. (7); Sec. 4, reordering"],
    ["KT089", "CLBG", "CONTRASTIVE", "GRAPH",
     "InfoNCE-style loss between a node and the same node after bipartite-graph augmentation, summed over the exercise-concept graph and the two same-type correlation graphs",
     "The same node in the original graph and in the augmented graph of the same view",
     "Different nodes",
     "Random edge addition and edge deletion with probability p",
     "NO_EXPLICIT_CONSTRAINT", G["KT089"],
     "Sec. 3.4, graph augmentation; Sec. 3.5, contrastive objective"],
]

header = [
    "paper_id", "model", "ssl_paradigm", "view_source",
    "pretext_or_consistency_target", "positive_pair_definition",
    "negative_pair_definition", "augmentation",
    "augmentation_structure_constraint", "graph_used_YN", "evidence_locator",
]
paradigms = ["CONTRASTIVE", "GENERATIVE_RECONSTRUCTION", "CONSISTENCY", "PREDICTIVE", "OTHER"]
views = ["SEQUENCE", "GRAPH", "HETEROGENEOUS_GRAPH", "HYPERGRAPH",
         "MOMENTUM_ENCODER", "COLLABORATIVE_STUDENT", "MULTIVIEW", "OTHER"]
assert len(rows) == 16
assert len({r[0] for r in rows}) == 16
for r in rows:
    assert r[2] in paradigms, r[0]
    assert r[3] in views, r[0]
    assert r[9] in ("Y", "N")

with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)

# crosstab of counts
count = {(v, p): 0 for v in views for p in paradigms}
ids = {(v, p): [] for v in views for p in paradigms}
for r in rows:
    count[(r[3], r[2])] += 1
    ids[(r[3], r[2])].append(r[1])

with CROSS_PATH.open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["view_source"] + paradigms)
    for v in views:
        w.writerow([v] + [count[(v, p)] for p in paradigms])

n_s = len(rows)
n_g_and_s = sum(1 for r in rows if r[9] == "Y")
print("N_S", n_s)
print("N_G_AND_S", n_g_and_s)
print("paradigm", Counter(r[2] for r in rows))
print("view", Counter(r[3] for r in rows))
print("structure", Counter(r[8] for r in rows))
print("graph N", [r[0] for r in rows if r[9] == "N"])

# figure: paradigm x view_source, empty rows and columns omitted from the drawing
used_p = [p for p in paradigms if any(count[(v, p)] for v in views)]
used_v = [v for v in views if any(count[(v, p)] for p in paradigms)]
mat = [[count[(v, p)] for p in used_p] for v in used_v]
fig, ax = plt.subplots(figsize=(7.4, 7.2))
im = ax.imshow(mat, cmap="Blues", vmin=0, vmax=max(max(row) for row in mat))
ax.set_xticks(range(len(used_p)))
ax.set_xticklabels([p.replace("_", "\n") for p in used_p], fontsize=9)
ax.set_yticks(range(len(used_v)))
ax.set_yticklabels([v.replace("_", " ") for v in used_v], fontsize=9)
for i, v in enumerate(used_v):
    for j, p in enumerate(used_p):
        n = count[(v, p)]
        if n:
            label = str(n) + "\n" + "\n".join(ids[(v, p)])
            ax.text(j, i, label, ha="center", va="center", fontsize=6.5,
                    color="white" if n >= 3 else "black")
ax.set_xlabel("SSL supervisory signal")
ax.set_ylabel("Object that supplies the SSL view")
ax.set_title("SSL-KT taxonomy after corpus expansion (16 papers)")
fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="Papers")
fig.tight_layout()
fig.savefig(FIG_PATH, dpi=160)
print("figure", FIG_PATH, FIG_PATH.stat().st_size)
