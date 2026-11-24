# B4 — equation check

**Date:** 2026-11-13. **Scope:** the three live manuscript files only. Backups, locked files, and corpus counts were not edited.

## Formula (6), cold-start filter

The displayed filter now uses \(\subseteq\):

\[\mathcal{D}_{\text{train}}^{\text{cold}} = \{(x_t, r_t) \in \mathcal{D}_{\text{train}} \mid \mathrm{KC}(x_t) \subseteq \mathcal{K} \setminus \mathcal{K}_{\mathrm{cold}}\}\]

The sentence after the display states three consequences:

- An exercise that mixes warm and cold KCs is removed in full.
- A log-derived graph, including co-occurrence and transition, must be built from this filtered training set.
- The removed-interaction fraction is a required benchmark report. No fraction is computed in this paper.

The \(0/37\) and \(1/37\) counts are unchanged. *pyKT-ColdStart* remains a specification with no executed run.

## Formula (7), LLM–GNN dimensions

`W_Q`, `W_K`, and `W_V` are **NOT_IN_CURRENT_DRAFT**. Group B is one paragraph and has no fusion equation. The dimension correction was not rewritten into the paper.

## Other displays

Six numbered displays remain. Symbols that the following sentence did not name are now named there. No display was added. \(N\) inside the ECE display is defined as the prediction count. Renaming it to \(n\) is C2 and was not done.

| Display | Following sentence |
|---|---|
| Gateway rule | KT, GRAPH_BASED, and SELF_SUPERVISED are defined |
| Evidence tuple | Five slots are defined in words |
| GCN update | \(\mathbf{H}^{(l)}\), \(\mathbf{W}^{(l)}\), \(\sigma\), \(\mathbf{A}\), \(\mathbf{I}\), \(\tilde{\mathbf{A}}\), \(\tilde{\mathbf{D}}\) |
| InfoNCE | Views, cosine similarity, temperature, batch size, index \(j\) |
| ECE | Bin set, accuracy, confidence, \(M\), and \(N\) as the prediction count |
| Cold-start filter | Set-valued \(\mathrm{KC}(x_t)\), interaction, and training set |

The inline temperature map in agenda item A2 now says that \(\sigma\) is the logistic function. Equations (8), (9), and the causal display named in the review are not in the current draft.

B4_EQUATION_CHECK_COMPLETE = YES
