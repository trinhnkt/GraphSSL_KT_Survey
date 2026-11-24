import io, os, shutil

ROOT = r'D:\TRINH\GraphSSL_KT_Survey'
TLT = os.path.join(ROOT, '12_manuscript', 'TLT')


def edit(path, pairs):
    t = io.open(path, encoding='utf-8', newline='').read()
    crlf = '\r\n' in t
    t = t.replace('\r\n', '\n')
    for a, b in pairs:
        assert t.count(a) == 1, (path, a[:80], t.count(a))
        t = t.replace(a, b)
    io.open(path, 'w', encoding='utf-8', newline='').write(t.replace('\n', '\r\n') if crlf else t)


cover = [
    ("The compiled anonymous manuscript is 14 double-column pages; the author-identified version is 15 pages",
     "The compiled anonymous manuscript is 17 double-column pages; the author-identified version is 17 pages"),
    ("a three-job GO/NO-GO checklist", "a three-job go/not-enough-evidence checklist"),
    ("The 37 primary-core PDFs were identity-checked by the authors. Count-based findings are protocol-coded audit results.",
     "The 37 primary-core PDFs were identity-checked by the authors. Screening and primary coding were performed by an AI research assistant; human coding exists only for the 20-paper sample, so the coefficients measure agreement between human coders and an AI-generated, partly adjudicated reference. A post hoc venue probe (EDM, AIED, LAK, L@S, JEDM, IJAIED) found ten candidate Graph/SSL-KT papers outside the locked core; they are reported, not coded. Count-based findings are protocol-coded audit results."),
]
# cover letter already patched in a first run

high = [
    ("# Research Highlights (v1.2 — IEEE TLT)", "# Research Highlights (v1.3 — IEEE TLT)"),
    ("- **Sparse/cold-start audit:** Generic interaction sparsity is YES for all 37 papers. Strict zero-exposure KC cold-start is $0/37$. Item cold-start is YES for SINKT only ($1/37$). Learner cold-start is $0/37$.",
     "- **Sparse/cold-start audit:** Strict zero-exposure KC cold-start is $0/37$. Item cold-start is YES for SINKT only ($1/37$). Interaction-drop evaluation is YES for HHSKT only ($1/37$). Learner cold-start is $0/37$ (decision table in the paper)."),
    ("- **Calibration audit:** None of the 37 manuscripts report ECE",
     "- **ECE reporting audit (keyword scan of 36 PDFs: no Brier score, one calibration plot in CL4KT):** None of the 37 manuscripts report ECE"),
    ("- **Learning-technology deliverable:** A T1--T3 GO/NO-GO checklist",
     "- **AI role disclosed:** Screening and primary coding were produced by an AI research assistant; human coding covers a 20-paper sample only. A post hoc venue probe found ten candidate Graph/SSL-KT papers outside the locked core.\n- **Learning-technology deliverable:** A T1--T3 go/not-enough-evidence checklist"),
]
edit(os.path.join(ROOT, '12_manuscript', 'HIGHLIGHTS.md'), high)

entry = """## [v1.6.27] - 2026-11-11 (reviewer-response revisions 1-10)

- Sparse/cold-start: new `tables/sparse_coldstart_audit_v1.9.csv` (`sparse_interaction_drop_eval` YES for KT035 only; constant generic-sparsity column dropped; deposited v1 file unchanged). Generic sparsity removed from Contribution 3 and conclusion. One-sentence learner cold-start definition plus decision table.
- Contribution 4 renamed ECE reporting audit; keyword scan of 36 PDFs (ECE 0, Brier 0, one calibration plot in CL4KT; KGNN-KT has no text layer). Output: `supplementary/calibration_keyword_scan_v1.9.csv`.
- Provenance: sub-bins of the displayed model-defined code (Q-matrix 3 / log-derived 10 / architecture-defined 6), provenance x encoder cross-tab (35 cells, 15 empty, no outcome per cell), per-paper eight-value records in Appendix A. Disclosed that 24/36 records map to the display, 5 differ with PDF-level adjudication, 7 differ without (sensitivity 16/8/11 + 1 unclassified). Headline 19/8/9 unchanged.
- T1/T3 verdicts changed from NO-GO to "not enough evidence to GO"; T2 \"pedagogical object\" claim softened; worked SINKT example added.
- New subsections: Role of the AI Research Assistant, Venue-Extension Probe, Deviations from the Locked Protocol. Acknowledgment rewritten to match records (41/45 coding files name the AI assistant as coder; screening files list AI_ASSISTANT).
- DyGKT overlay: convenience choice and transductive setting stated.
- Venue probe logged in `03_search/search_log_venue_extension_v1.9.csv` and `03_search/venue_extension_candidates_v1.9.csv` (10 candidates, none coded; N=37 unchanged).
- Rebuilt PDFs: anonymous 17 pages; author-identified 17 pages (cap 18). Sources backed up in `12_manuscript/TLT/_backup_before_v1.9/`.

---

"""
edit(os.path.join(TLT, 'MANUSCRIPT_TLT_CHANGELOG.md'), [("## [v1.6.26] - 2026-11-10 (four remaining Minors)", entry + "## [v1.6.26] - 2026-11-10 (four remaining Minors)")])

nt = io.open(os.path.join(ROOT, 'NEXT_TASK.md'), encoding='utf-8', newline='').read()
nt = nt.replace("**Done (v1.6.26):**", "**Done (v1.6.27):** Reviewer-response revisions 1-10 (see `12_manuscript/TLT/MANUSCRIPT_TLT_CHANGELOG.md`). Open facts only the authors can confirm: who verified AI primary coding per paper; PDF-level re-check of seven provenance records (KT023, KT035, KT050, KT062, KT064, KT065, KT069); whether the ten venue-probe candidates were screened out.\n\n**Done (v1.6.26):**", 1)
io.open(os.path.join(ROOT, 'NEXT_TASK.md'), 'w', encoding='utf-8', newline='').write(nt)

dev = """## DEV-20261111-01
- Date: 2026-11-11
- Protocol version before: tables/sparse_coldstart_audit.csv (v1 as deposited); manuscript v1.6.26
- Protocol version after: tables/sparse_coldstart_audit_v1.9.csv; manuscript v1.6.27
- Change: (a) `sparse_interaction_drop_eval` corrected from constant YES (37 rows) to YES for KT035 only, matching the H2 overlay; generic-sparsity column dropped. (b) Per-paper 8-way provenance records compared with the 3-token display: 24/36 agree, 5 differ with PDF-level adjudication/recode (KT016, KT036, KT044, KT052, KT076), 7 differ with no PDF-level re-check (KT023, KT035, KT050, KT062, KT064, KT065, KT069). Display 19/8/9 retained; sensitivity 16/8/11 + 1 unclassified reported. (c) AI research assistant role in screening and primary coding disclosed (screening files: screener_id/reviewer_id = AI_ASSISTANT; 41/45 coding files: coder = AI_ASSISTED). (d) Post hoc venue-extension probe (EDM, AIED, LAK, L@S, JEDM, IJAIED) logged; 10 candidates not coded.
- Reason: Reviewer-response revisions; remove contradictions between deposited files and manuscript text; disclose rather than silently reconcile.
- Affected records: sparse/cold-start CSV; provenance reporting; Acknowledgment; search-completeness statement. Not changed: N=37, N_G, N_S, kappa values, 0/37 ECE.
- Screening repeated: no
- Coding repeated: no (sub-bins assigned by rule from coding records; not re-read from PDFs)
- Approved by: author request 2026-11-11 (reviewer-response revision list)

"""
edit(os.path.join(ROOT, '00_protocol', 'protocol_deviations.md'), [("## DEV-YYYYMMDD-XX", dev + "## DEV-YYYYMMDD-XX")])

# copy PDFs with title names
base = 'Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings - A Critical Survey'
for dst in (TLT, os.path.join(ROOT, '12_manuscript')):
    shutil.copyfile(os.path.join(TLT, 'main_tlt_anonymous.pdf'), os.path.join(dst, base + ' - Anonymous.pdf'))
    shutil.copyfile(os.path.join(TLT, 'main_tlt_full.pdf'), os.path.join(dst, base + '.pdf'))
shutil.copyfile(os.path.join(TLT, 'COVER_LETTER.tex'), os.path.join(ROOT, '12_manuscript', 'COVER_LETTER.tex'))
print('done')
