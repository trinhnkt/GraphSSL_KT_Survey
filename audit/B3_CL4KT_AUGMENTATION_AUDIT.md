# B3 — CL4KT augmentation audit

**Date:** 2026-11-13. **Source:** `14_references/Contrastive Learning for Knowledge Tracing.pdf` (Lee et al., WWW 2022, DOI `10.1145/3485447.3512105`, 10 pages).
**Not done:** no locked file edited. N, N_G, N_S, and the 0/37 and 1/37 counts unchanged. The other eight SSL papers were not re-read. DyGKT was not removed. P0 was not cited.

## What the source says

| Claim | Locator | Reading |
|---|---|---|
| Two augmented copies of one history are a positive pair | Sec. 3.4.1 | Positive views, not negatives |
| Question mask | Sec. 3.5, Fig. 3(a) | Replace some questions by `[mask]`; responses unchanged. Called a noisy view of the same history |
| Interaction crop | Sec. 3.5, Fig. 3(b) | Contiguous subsequence of length \(\lfloor \gamma_{\mathrm{crop}} T \rfloor\) |
| Interaction permute | Sec. 3.5, Fig. 3(c) | Shuffle a contiguous subsequence |
| Question replace | Sec. 3.5, footnote 1, Fig. 3(d) | If the response is correct, replace the question by an easier one; otherwise by a harder one. Responses unchanged. Difficulty order is the training-set rate of correct answers |
| Hard negatives | Sec. 3.6 | Built separately by reversing responses, \(\tilde{r}_t = 1 - r_t\). The authors say that masking or replacing responses was not useful for positive pairs, because a changed response changes the meaning of the history |
| Prerequisite constraint | Sec. 3.5 | No concept graph. The difficulty chain is not stated as a constraint that keeps prerequisite edges. Footnote 1 says the method does not use a predefined skill–question relation |

## Sentence removed

The draft said that random item masking creates hard-negative views and used the token `NO_EXPLICIT_CONSTRAINT`. Section 3.5 describes masking as a positive view. Section 3.6 builds hard negatives by reversing responses. That sentence is removed from the three live manuscript files.

## Manuscript edits

Same text in `main_tlt_anonymous.tex`, `main_tlt_full.tex`, and `manuscript_TLT_FORMATTED_v1.3.tex`:

- The unattached augmentation list is replaced by Table `tab:cl4kt_aug` (four CL4KT rows, with section and figure locators).
- The structure-preservation subsection is rewritten in prose from Sec. 3.4.1, 3.5, and 3.6.
- The CL4KT row of the SSL table now lists mask, crop, permute, and replace. The old cell omitted question replace.

## Not re-verified

Edge dropping, node-attribute masking, random walks, and counterfactual rewiring are no longer stated as corpus facts. The augmentation labels of the other eight SSL papers remain the previously coded labels in the SSL table. Page locators for those eight are `NEEDS_EVIDENCE`.

B3_CL4KT_SENTENCE_CORRECTED = YES
