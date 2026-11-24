# Research Highlights (v1.3 — IEEE TLT)

**Survey Title:** Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Critical Survey  
**Target Venue:** IEEE Transactions on Learning Technologies (TLT), Survey and Tutorial  
**Locked counts:** `12_manuscript/TLT/audit/LOCKED_COUNTS_v1.8.md`  
**Historical TKDE draft:** `HIGHLIGHTS_v1.0_TKDE.md` (N=42; superseded)

---

## Key Highlights

- **Locked 37-PDF corpus:** Six core bibliographic databases plus arXiv preprint monitoring yield $N_{\mathrm{rec}}=2{,}017$ identified records and a 37-paper primary core (2018--2026; $N_G=36$, $N_S=9$, $N_{G\cap S}=8$). Identification counts come from the locked search log; stage counts 750/140/103 are search-expansion report arithmetic without a deposited row-level screening ledger.
- **Three-token graph coding:** Graph-KT is classified by display provenance **19 / 8 / 9** (model-defined / external / dynamically learned) and encoder family, including three papers with an explicit graph and no GNN (PDKT-C, CMKT, PEBG). SSL-KT is a locked coding table of four pretext families ($N_S=9$; two families have one paper each), not a saturated taxonomy.
- **Sparse/cold-start audit:** Strict zero-exposure KC cold-start is $0/37$. Item cold-start is YES for SINKT only ($1/37$). Interaction-drop evaluation is YES for HHSKT only ($1/37$). Learner cold-start is $0/37$ (decision table in the paper).
- **ECE reporting audit (keyword scan of 36 PDFs: no Brier score, one calibration plot in CL4KT; RMSE in 12 PDFs as overall prediction error):** None of the 37 manuscripts report ECE ($0/37$).
- **Gateway check, 23 November 2026:** Seven further in-window papers meet the same inclusion gateway and are not rows in the itemized tables. DECKT, KT-Deeper, HCMKT, and CLBG are graph and self-supervised. CoSKT, DTransformer, and SP-CLKT are sequence self-supervised only. None of the seven reports ECE or a zero-exposure KC split.
- **AI role disclosed:** Screening and primary coding were produced by an AI research assistant; human coding covers a 20-paper sample only. A post hoc venue probe found ten candidate Graph/SSL-KT papers outside the locked core.
- **Learning-technology deliverable:** A T1--T3 go/not-enough-evidence checklist for new-KC onboarding, treating a log-derived graph as a skill map, and acting on raw $P(r=1)$, plus five reporting rules. Corpus-derived agenda items precede open technical directions.
