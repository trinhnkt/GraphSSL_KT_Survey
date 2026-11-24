# Applies the B4 equation edits to the three live manuscript files only.
from pathlib import Path

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT")
FILES = [
    ROOT / "main_tlt_anonymous.tex",
    ROOT / "main_tlt_full.tex",
    ROOT / "manuscript_TLT_FORMATTED_v1.3.tex",
]

REPLACEMENTS = [
    (
        r"\mathcal{D}_{\text{train}}^{\text{cold}} = \{(x_t, r_t) \in \mathcal{D}_{\text{train}} \mid \text{KC}(x_t) \in \mathcal{K} \setminus \mathcal{K}_{\mathrm{cold}}\}"
        "\n\\end{equation}\n"
        r"where $\text{KC}(x_t)$ maps exercise $x_t$ to its constituent KCs. Models must infer response accuracy over $\mathcal{K}_{\text{cold}}$ at test time using external structural graphs or semantic priors.",
        r"\mathcal{D}_{\text{train}}^{\text{cold}} = \{(x_t, r_t) \in \mathcal{D}_{\text{train}} \mid \text{KC}(x_t) \subseteq \mathcal{K} \setminus \mathcal{K}_{\mathrm{cold}}\}"
        "\n\\end{equation}\n"
        r"where $\text{KC}(x_t)$ is the set of knowledge components linked to exercise $x_t$, $(x_t, r_t)$ is one training interaction, and $\mathcal{D}_{\text{train}}$ is the training interaction set. The subset condition removes every interaction whose exercise contains at least one cold KC, including an exercise that also contains warm KCs. Any graph built from the interaction log, including a co-occurrence or transition graph, must be built from $\mathcal{D}_{\text{train}}^{\text{cold}}$. The fraction of training interactions removed by this filter is a required report of the benchmark. This paper does not compute that fraction. Models must infer response accuracy over $\mathcal{K}_{\text{cold}}$ at test time using external structural graphs or semantic priors.",
    ),
    (
        r"where $\tilde{\mathbf{A}} = \mathbf{A} + \mathbf{I}_{|\mathcal{K}|}$ adds self-loops and $\tilde{\mathbf{D}}$ is the corresponding degree matrix.",
        r"where $\mathbf{H}^{(l)}$ is the node-state matrix at layer $l$, $\mathbf{W}^{(l)}$ is the weight matrix of that layer, $\sigma$ is a pointwise nonlinearity, $\mathbf{A}$ is the adjacency matrix, $\mathbf{I}_{|\mathcal{K}|}$ is the identity of order $|\mathcal{K}|$, $\tilde{\mathbf{A}} = \mathbf{A} + \mathbf{I}_{|\mathcal{K}|}$ adds self-loops, and $\tilde{\mathbf{D}}$ is the corresponding degree matrix.",
    ),
    (
        r"where $\mathbf{z}_i^{(1)}, \mathbf{z}_i^{(2)}$ are normalized view embeddings, $\tau$ is temperature, and $B$ is batch size.",
        r"where $\mathbf{z}_i^{(1)}$ and $\mathbf{z}_i^{(2)}$ are the two normalized view embeddings of anchor $i$, $\mathrm{sim}$ is cosine similarity, $\tau$ is the temperature, $B$ is the batch size, and $j$ indexes the other embeddings in the denominator.",
    ),
    (
        r"where $B_m$ is the set of predictions in $((m-1)/M, m/M]$.",
        r"where $B_m$ is the set of predictions whose confidence falls in $((m-1)/M, m/M]$, $\mathrm{acc}(B_m)$ is the accuracy inside that bin, $\mathrm{conf}(B_m)$ is the mean predicted confidence inside that bin, $M$ is the number of bins, and $N$ in this display is the number of predictions, not the number of papers.",
    ),
    (
        "\\end{equation}\n\n\\subsection{Quality \\& Reliability Assessment Protocol}",
        "\\end{equation}\n"
        "In that tuple, the five slots are the record identifier, the field name, the assigned code, the location of the supporting passage, and the coding note.\n\n"
        "\\subsection{Quality \\& Reliability Assessment Protocol}",
    ),
    (
        "Only studies where Knowledge Tracing is the central prediction task AND that leverage explicit Graph-Based or Self-Supervised mechanisms are included in our primary synthesis corpus.",
        r"In that rule, KT means knowledge tracing is the central prediction task, GRAPH\_BASED means an explicit graph is a structural mechanism of the tracing model, and SELF\_SUPERVISED means an auxiliary pretext objective whose target is taken from the observed data. Only studies that meet the rule are included in the primary synthesis corpus.",
    ),
    (
        r"raw logits $z_i$ should be converted to calibrated probabilities $\hat{p}_i = \sigma(z_i/T)$, with temperature $T>0$ fitted on a held-out validation set by minimizing negative log-likelihood",
        r"raw logits $z_i$ should be converted to calibrated probabilities $\hat{p}_i = \sigma(z_i/T)$, where $\sigma$ is the logistic function and the temperature $T>0$ is fitted on a held-out validation set by minimizing negative log-likelihood",
    ),
]

for path in FILES:
    text = path.read_text(encoding="utf-8")
    for i, (old, new) in enumerate(REPLACEMENTS, start=1):
        count = text.count(old)
        if count != 1:
            raise SystemExit(f"{path.name}: replacement {i} found {count} times")
        text = text.replace(old, new, 1)
    if "W_Q" in text or "W_K" in text or "W_V" in text:
        raise SystemExit(f"{path.name}: weight matrices appeared after edit")
    if r"\text{KC}(x_t) \in" in text:
        raise SystemExit(f"{path.name}: membership condition remains")
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"updated {path.name}")
