# Venue-probe window under the 23 November 2026 eligibility date

**Date:** 2026-11-23. **Rule:** DEV-20261123-01. A paper published on or before 23 November 2026 is eligible to be read. The logged search remains 2015-01-01 to 2026-07-31, and \(N_{\mathrm{rec}}=2{,}017\).

These ten rows are not full-text decisions and are not coding rows. Abstracts come from OpenAlex or Crossref. VX05 was already read in full as HCMKT. The other nine stay `NEEDS_FULL_TEXT`. Itemized \(N\) stays 37.

Dates are Crossref `issued` unless noted. The Crossref record-created date is not the publication date. November export hits are own-title or own-DOI matches in the 14–16 November 2026 files. A short string that hits a different paper is marked as not an own record.

| ID | Paper | Publication date used | In the 23 Nov 2026 window | November own record | Abstract-level gateway |
|---|---|---|---|---|---|
| VX01 | AGKT, EDM 2022 poster | OpenAlex 2022-07-18. Zenodo DOI 10.5281/zenodo.6853056 returned Crossref 404, so that DOI is not confirmed. | Yes | Scopus Q-G, title | Graph-based KT. The abstract does not state whether an edge structure is built. S not stated. |
| VX02 | Expert-defined graphs, L@S 2024, 10.1145/3657604.3664683 | 2024-07-09 | Yes | Scopus Q-G, title phrase | Expert-defined graph used by the model. S not stated. |
| VX03 | GRKT, KDD 2024, 10.1145/3637528.3671853 | 2024-08-24 | Yes | arXiv Q-G and Q-S, own title; Scopus Q-G and Q-S, title phrase. The IEEE Q-G hit on `grkt` is a different paper. | Concept graph with a GNN. S not stated in the abstract excerpt. |
| VX04 | BiCo, TKDD, 10.1145/3638055 | 2024-02-12 | Yes | Scopus Q-G and Q-S, title phrase | Bi-graph and self-supervised contrastive pre-training for KT. |
| VX05 | HCMKT, 10.1016/j.eswa.2025.128840 | OpenAlex online 2025-07-02; Crossref issue 2026-01 | Yes. Already full text. | ScienceDirect both families; Scopus Q-G, Q-S, Q-P | G and S, decided from the PDF on 2026-11-22. |
| VX06 | GCLFKT, ICEIT 2025, 10.1109/iceit64364.2025.10976145 | 2025-03-14 | Yes | IEEE both families; Scopus Q-G and Q-S, DOI | GAT question embeddings and graph contrast learning. |
| VX07 | TransKT, IJCAI 2025, 10.24963/ijcai.2025/823 | Crossref 2025-09; OpenAlex 2025-09-01 | Yes | arXiv Q-G and Q-S, own title; Scopus Q-G and Q-S, DOI | Cross-course concept graph and a contrastive objective. |
| VX08 | SCDI, IEEE Access, 10.1109/access.2025.3542870 | Crossref issued year 2025; record created 2025-02-17. OpenAlex 2025-01-01 is not used as the day. | Yes | IEEE both families; Scopus Q-G and Q-S, DOI | Heterogeneous graph, graph contrastive learning, and a directed interaction graph. |
| VX09 | MSCL, Neurocomputing 692:133837, 10.1016/j.neucom.2026.133837 | Crossref print 2026-09. No published-online date. | Yes under the 23 Nov rule. It was after the 31 July 2026 logged cutoff. | ScienceDirect both families; Scopus Q-G and Q-S, DOI | No abstract in the Crossref or OpenAlex record retrieved on 2026-11-23. |
| VX10 | KGS-KT, 10.4018/ijicte.385130 | 2025-07-14. Authors Yanhong Shen and Yi Chen. Pages 1–22. | Yes | Scopus Q-G and Q-S, title phrase | Knowledge graph, GCN, and two self-supervised tasks (node attribute and edge relation). |

Evidence file: `audit/_a1_evidence/venue_probe_2026-11-23.json`. Hit lines: `audit/_a1_evidence/venue_probe_checks_2026-11-23.json`.

None of VX01–VX04 or VX06–VX10 is entered in the itemized tables. The next step is the full text of those nine, still without changing \(N\).
