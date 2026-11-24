# CURSOR final-fix decisions (H1–H6)

| Issue | Current manuscript (before this pass) | Evidence checked | Decision | Exact change | File/section |
|---|---|---|---|---|---|
| H1 \(N_S=14\) | Table IV had 14 SSL rows | Locked SCOPE §5; PDFs; coding records | **CONFIRMED_FIX** | \(N_S=9\), \(N_{G\cap S}=8\), 7 families. Drop KT044/070/076/077/079 from SSL only | Abstract, I.C, Figs. 2/5, Table IV, §IV, Discussion, Conclusion |
| H2 QA7 on all 37 | QA7 applicable, max=16 | Protocol *may* NA no-claim papers; this survey uses the RQ4 evidence lens | **KEEP_CURRENT** | QA7 = review evidence adequacy, not author sparsity-claim. Keep `evaluation_support_regime` ≠ `sparsity_claim`. Scores unchanged | §II.D; §VI; `audit/H2_QA7_APPLICABILITY.md` |
| H3 novelty | Table II omitted Liu TKDE 2025 and Xu JEDM 2026 | Publisher/JEDM records | **CONFIRMED_FIX** | Add those surveys; no “first survey” claim; use joint-synthesis wording | §I.C, Table II, `references.bib` |
| H4 KT004 | “GKT (Dense)” + “Sequential transition” | Codebook: Dense and Transition are distinct | **CONFIRMED_FIX** | One GKT row: multiple graph variants | Table III |
| H4 KT026 | Encoder labeled GCN | PEBG PDF + codebook `gnn_encoder=NONE` | **CONFIRMED_FIX** | none / PNN pretrain; GCN/generic 13; NONE 3 | Table III, Fig. 4, encoder prose |
| H5 refs | Missing Liu 2025 / Xu 2026 | IEEE DOI `10.1109/TKDE.2025.3552759`; JEDM URL | **CONFIRMED_FIX** | Two bib entries | `references.bib` |
| H5 Eq. cold-start | Risk of `K/cold` | Source used `\notin \mathcal{K}_{\text{cold}}` | **CONFIRMED_FIX** | Use `\in \mathcal{K} \setminus \mathcal{K}_{\mathrm{cold}}` | Agenda Eq. 8 |
| H5 treatment \(X\) | \(X\) also used for history; \(A\) is adjacency | Notation table uses \(\mathcal{X}_{1:T}\) and \(\mathbf{A}\) | **CONFIRMED_FIX** | Treatment renamed \(W\) (not \(A\)) | Eq. causal + notation table |
| H5 hyperbolic wording | “prevents exponential representation distortion” | Agenda is open inference | **WORDING_ONLY** | Softer hierarchical-structure sentence | Agenda pillar |
| H6 keywords | 7 terms | H6 asks for 5 unless template requires more | **WORDING_ONLY** | Five IEEE keywords | Title block |
| H6 AI disclosure | Copy-edit / LaTeX only | This pass revised SSL counts and taxonomy | **CONFIRMED_FIX** | Disclose audits + revision; authors remain responsible | Acknowledgment |

Do not edit `_LOCKED` protocol files.
