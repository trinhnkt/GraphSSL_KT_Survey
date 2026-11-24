"""Builds tables/A1_CORPUS_COVERAGE_AUDIT.csv. All G/S/KT judgements are AI_ASSISTED_READING (NOT a human screening decision).
present_in_raw_2017 / present_in_dedup_750 cannot be verified: raw exports and the 750-row ledger are not deposited in the repo.
"""
import csv, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import _a1_match as M

ROOT = M.ROOT
EV = os.path.join(ROOT, 'audit', '_a1_evidence')
NE = 'NEEDS_EVIDENCE (raw export not deposited)'
NE750 = 'NEEDS_EVIDENCE (no 750-row ledger deposited)'
NOREC = 'NO_RECORD_IN_DEPOSITED_LOGS (search/seed/screening/fulltext/venue files grep-checked 2026-11-13)'


def grab(fn, lineno_a, lineno_b):
    ls = open(os.path.join(EV, fn), encoding='utf-8', errors='ignore').read().split('\n')
    return ' '.join(ls[lineno_a - 1:lineno_b])


deckt_abs = grab('DECKT_fulltext_PMC12294018.txt', 20, 20)
dtr_abs = grab('DTransformer_fulltext_yin2023.txt', 57, 59)

SP_ABS = ("Knowledge tracing is a fundamental research issue in personalized education ... student interaction data tends to be sparse ... "
          "this paper proposes a novel self-paced learning data augmentation approach ... it leverages self-supervised contrastive learning to balance local and global information ... "
          "deep knowledge tracing framework based on self-paced contrastive learning ... Keywords: knowledge tracing self-paced learning contrastive learning")
COSKT_ABS = ("Knowledge tracing (KT) aims to trace students' evolving knowledge states ... collaborative self-supervised learning method for KT (CoSKT) ... retrieve similar students ... "
             "we introduce self-supervised learning by encouraging the consistency between the common knowledge state and individual knowledge state ...")
HCMKT_ABS = ("Knowledge tracing aims to track the evolution of knowledge state ... heterogeneous graph knowledge tracing method (HCMKT) with novel contrastive view and meta-path contexts ... "
             "meta-paths to construct coarse and fine-grained views ... construct contrastive view between the coarse and fine-grained views ... online knowledge distillation ...")
BIP_ABS = ("Knowledge tracking tasks ... bipartite graph representation ... exercises and knowledge concepts ... we propose a bipartite graph-based contrastive learning method with dual-view data augmentation ...")
HAN_ABS = ''  # abstract NOT retrieved (publisher abstract-only page not accessible in this environment); title-only simulation

C = []


def add(**k):
    C.append(k)


add(candidate_id='A1-C01', title='A Dual-Encoder Contrastive Learning Model for Knowledge Tracing (DECKT)', DOI='10.3390/e27070685', publication_year='2025',
    source_database='Entropy 27(7):685 (MDPI; PMC12294018; open access). Coverage in the 6 searched DBs: NEEDS_EXTERNAL_VERIFICATION',
    abs=deckt_abs, stage='NO_RECORD', original_decision='NONE', exclusion_code='NA',
    KT='YES', G='YES (question-concept bipartite graph; multi-layer GAT primary + EMA momentum encoder)', S='YES (InfoNCE between primary and momentum encoder embeddings; plus graph-structure-constraint loss)',
    gw='WOULD_PASS (PRIMARY_CORE; G and S) -- AI reading, not a screening decision',
    loc='Abstract; Sec.1 para 5-6 (GAT primary encoder, momentum encoder); Sec.3.3.1-3.3.2; contrastive objective (InfoNCE) ~Eq. after Sec.3.3.2; graph structure constraint loss (question-concept bipartite G=(V,E)); full text in audit/_a1_evidence/DECKT_fulltext_PMC12294018.txt',
    final='ELIGIBLE_BY_AI_READING -> NEEDS_HUMAN_DECISION', act='Human screener to confirm; if included add to corpus via A1 refreeze. Directly relevant to sparse-concept lens (low-frequency KCs) and to RQ3 (structure-preserving contrastive view, no destructive augmentation).',
    lvl='FULL_TEXT_OPEN_ACCESS')
add(candidate_id='A1-C02', title='Tracing Knowledge Instead of Patterns: Stable Knowledge Tracing with Diagnostic Transformer (DTransformer)', DOI='10.1145/3543507.3583255', publication_year='2023',
    source_database='The Web Conference (WWW) 2023 (ACM DL). Seed record KT040.',
    abs=dtr_abs, stage='SEED_LIST_ONLY (KT040; seed_classification_v1_0=BACKGROUND)', original_decision='BACKGROUND (seed note: "sequence/probabilistic KT baseline without a verified Graph-Based or Self-Supervised mechanism"; "inspect if needed")',
    exclusion_code='NOT_RECORDED (no EC code; seed tier BACKGROUND)',
    KT='YES', G='NO (no explicit graph; checked full text, no graph construction)', S='YES (sequence contrastive loss on augmented learner sequences: SCOPE s5 family "sequence contrastive learning")',
    gw='WOULD_PASS via S-criterion (PRIMARY_CORE) -- AI reading; the original BACKGROUND decision conflicts with SCOPE_v1.0_LOCKED s5 as written',
    loc='Abstract ("novel training algorithm based on contrastive learning"); Sec.3.3.1 "Contrastive loss of knowledge states" incl. sequence augmentation and Eq.(17); loss weight Eq.(22); Table 2 "w/o CL" ablation; Table 4. Text in audit/_a1_evidence/DTransformer_fulltext_yin2023.txt',
    final='OLD_DECISION_APPEARS_WRONG -> NEEDS_HUMAN_DECISION', act='Human re-screen. Do NOT change 37/9/8 until A1 refreeze. Note: seed note shows the BACKGROUND decision was made without full-text verification.',
    lvl='FULL_TEXT_AUTHOR_HOSTED')
add(candidate_id='A1-C03', title='Self-paced contrastive learning for knowledge tracing (alias SP-CLKT)', DOI='10.1016/j.neucom.2024.128366', publication_year='2024',
    source_database='Neurocomputing 609:128366 (Elsevier); SSRN preprint 4627338. Coverage in the 6 searched DBs: NEEDS_EXTERNAL_VERIFICATION',
    abs=SP_ABS, stage='NO_RECORD', original_decision='NONE', exclusion_code='NA', KT='YES', G='NO (no explicit graph reported in abstract; full text not read)',
    S='YES (self-supervised contrastive learning + self-paced augmentation; abstract-level)', gw='WOULD_PASS via S-criterion on abstract evidence -- full text not read',
    loc='SSRN abstract 4627338 (abstract, keywords); alias SP-CLKT used in Shukurlu 2025 arXiv:2504.15163 Table 1 (secondary source); Neurocomputing DOI metadata. Explicitly addresses sparse student interaction data (lens relevance).',
    final='ELIGIBLE_BY_AI_ABSTRACT -> NEEDS_HUMAN_DECISION', act='Obtain publisher full text; confirm S-criterion objective and sparse-data claim; confirm SP-CLKT alias.', lvl='ABSTRACT_ONLY')
add(candidate_id='A1-C04', title='Dynamic heterogeneous graph contrastive networks for knowledge tracing', DOI='10.1016/j.asoc.2024.112194', publication_year='2024',
    source_database='Applied Soft Computing 166:112194 (Elsevier; abstract-only access). Coverage in the 6 searched DBs: NEEDS_EXTERNAL_VERIFICATION',
    abs=HAN_ABS, stage='NO_RECORD', original_decision='NONE', exclusion_code='NA', KT='YES (title)', G='LIKELY (title: dynamic heterogeneous graph) -- NEEDS_EVIDENCE', S='LIKELY (title: contrastive networks) -- NEEDS_EVIDENCE',
    gw='NOT_ASSESSABLE (abstract not retrieved); title-level only', loc='Title + DOI metadata (Crossref/dblp HanTZDZS24); cited in Xu et al. Graph-KT survey reference list',
    final='NEEDS_EVIDENCE', act='Retrieve abstract/full text via institutional access; then human screen.', lvl='TITLE_ONLY')
add(candidate_id='A1-C05', title='Heterogeneous graph knowledge tracing with novel contrastive view and meta-path contexts (HCMKT)', DOI='10.1016/j.eswa.2025.128840', publication_year='2025 (online 2025-07-02; vol.295, 2026-01-01)',
    source_database='Expert Systems with Applications 295:128840 (Elsevier). Also venue-probe record VX05. Coverage in the 6 searched DBs: NEEDS_EXTERNAL_VERIFICATION',
    abs=HCMKT_ABS, stage='VENUE_EXTENSION_PROBE_LIST_ONLY (VX05, status TITLE_ABSTRACT_CANDIDATE_NOT_CODED); no screening record', original_decision='NONE', exclusion_code='NA', KT='YES',
    G='YES (heterogeneous information network from learning records, meta-path induced graphs)', S='YES (contrastive learning between coarse and fine-grained views + prototype CL; online knowledge distillation)',
    gw='WOULD_PASS (G and S) on abstract + intro evidence', loc='Abstract; Highlights; Introduction paragraph on contrastive view / graph augmentation (ScienceDirect open preview); abstract states sparse learning records',
    final='ELIGIBLE_BY_AI_ABSTRACT -> NEEDS_HUMAN_DECISION', act='Human screening; confirm from full text.', lvl='ABSTRACT_PLUS_INTRO_EXCERPT')
add(candidate_id='A1-C06', title='Contrastive Learning Based on Bipartite Graphs for Interpretable Knowledge Tracing', DOI='10.1007/978-981-96-0821-8_14', publication_year='2024 (online 2024-12-15)',
    source_database='ADMA 2024, LNAI 15389 (Springer). Coverage in the 6 searched DBs (SpringerLink searched): NEEDS_EXTERNAL_VERIFICATION',
    abs=BIP_ABS, stage='NO_RECORD', original_decision='NONE', exclusion_code='NA', KT='YES', G='YES (exercise-concept bipartite graph)', S='YES (bipartite-graph contrastive learning with dual-view data augmentation)',
    gw='WOULD_PASS (G and S) on abstract evidence', loc='Springer chapter page abstract (Chen, Mao, Zheng, Jiang); cites GCL with adaptive augmentation and CPC in its reference list',
    final='ELIGIBLE_BY_AI_ABSTRACT -> NEEDS_HUMAN_DECISION', act='Human screening; full text via institution.', lvl='ABSTRACT_ONLY')
add(candidate_id='A1-C07', title='CoSKT: A Collaborative Self-Supervised Learning Method for Knowledge Tracing', DOI='10.1109/TLT.2024.3386750', publication_year='2024',
    source_database='IEEE Transactions on Learning Technologies 17:1476-1488 (IEEE Xplore; IEEE Xplore was searched). Coverage: NEEDS_EXTERNAL_VERIFICATION',
    abs=COSKT_ABS, stage='NO_RECORD', original_decision='NONE', exclusion_code='NA', KT='YES', G='NO on abstract (similar-student retrieval by overlap rate; no explicit graph stated) -- verify in full text',
    S='YES (self-supervised consistency between common and individual knowledge states; SCOPE s5 "augmentation-free consistency learning")', gw='WOULD_PASS via S-criterion on abstract evidence; title contains "Self-Supervised"',
    loc='Abstract (IEEE Xplore/Crossref); Shukurlu 2025 Table 1 describes dual contrastive loss. Published in the same journal (IEEE TLT) as this survey is targeting.',
    final='ELIGIBLE_BY_AI_ABSTRACT -> NEEDS_HUMAN_DECISION', act='Human screening; confirm that no explicit graph is used (G=NO) and S objective from full text.', lvl='ABSTRACT_ONLY')
add(candidate_id='A1-C08', title='SP-CLKT (as named in the revision brief)', DOI='10.1016/j.neucom.2024.128366', publication_year='2024', source_database='= A1-C03',
    abs=SP_ABS, stage='NO_RECORD', original_decision='NONE', exclusion_code='NA', KT='YES', G='NO', S='YES', gw='SAME AS A1-C03 (alias; single paper)',
    loc='Alias per Shukurlu 2025 (arXiv:2504.15163) Table 1 row "SP-CLKT [6]" -> Dai et al. 2024 Neurocomputing 609:128366 (reference list). Not independently confirmed in publisher full text.',
    final='DUPLICATE_ALIAS_OF A1-C03', act='Merge with A1-C03 after confirming alias.', lvl='SECONDARY_SOURCE')

# venue-probe candidates (other than VX05 = A1-C05)
vx = list(csv.DictReader(open(os.path.join(ROOT, '03_search', 'venue_extension_candidates_v1.9.csv'), encoding='utf-8-sig')))
gs = {'VX01': ('YES (graph learned automatically)', 'NO'), 'VX02': ('YES (expert-defined graphs)', 'NO'), 'VX03': ('YES (graph-based reasonable KT)', 'NO'),
      'VX04': ('YES (bi-graph)', 'YES (self-supervised bi-graph co-contrastive pre-training)'), 'VX06': ('YES (graph contrast learning)', 'YES (graph contrast learning)'),
      'VX07': ('YES (concept graph)', 'YES (contrastive objective)'), 'VX08': ('LIKELY (directed interaction learning)', 'YES (self-supervised contrastive)'),
      'VX09': ('YES (multi-dimensional graph structures)', 'YES (self-supervised contrastive)'), 'VX10': ('YES (GCN)', 'YES (self-supervised learning)')}
n = 9
for r in vx:
    if r['candidate_id'] == 'VX05':
        continue
    g, s = gs[r['candidate_id']]
    add(candidate_id='A1-X%s' % r['candidate_id'][2:], title=r['title'], DOI=r['doi_or_url'].replace('https://doi.org/', ''), publication_year=r['year'],
        source_database='%s (venue-extension probe %s)' % (r['venue'], r['candidate_id']), abs='', stage='VENUE_EXTENSION_PROBE_LIST_ONLY (no screening record)',
        original_decision='NONE', exclusion_code='NA', KT='YES (title)', G=g + ' [title/snippet-level]', S=s + ' [title/snippet-level]',
        gw='NOT_ASSESSED (title-level only)', loc='03_search/venue_extension_candidates_v1.9.csv row %s' % r['candidate_id'], final='NEEDS_HUMAN_DECISION',
        act='Human screening (not requested in the 8-paper brief; listed because found in the earlier venue probe).', lvl='TITLE_OR_SNIPPET_ONLY')

fields = ['candidate_id', 'title', 'DOI', 'publication_year', 'source_database', 'present_in_raw_2017', 'present_in_dedup_750', 'stage_reached', 'original_decision', 'exclusion_code',
          'KT_central', 'G_criterion', 'S_criterion', 'primary_gateway_result', 'evidence_locator', 'final_decision', 'action_required',
          'evidence_level', 'simulated_Q_G_hits', 'simulated_Q_S_hits', 'simulated_retrievable_Scopus_Q_G_or_Q_S', 'simulation_note']
rows = []
for k in C:
    sim = M.simulate(k['title'], k.get('abs', ''))
    g, s = M.summarize(sim)
    rows.append(dict(candidate_id=k['candidate_id'], title=k['title'], DOI=k['DOI'], publication_year=k['publication_year'], source_database=k['source_database'],
                     present_in_raw_2017=NE, present_in_dedup_750=NE750,
                     stage_reached=k['stage'] if k['stage'] != 'NO_RECORD' else NOREC,
                     original_decision=k['original_decision'], exclusion_code=k['exclusion_code'], KT_central=k['KT'], G_criterion=k['G'], S_criterion=k['S'],
                     primary_gateway_result=k['gw'], evidence_locator=k['loc'], final_decision=k['final'], action_required=k['act'],
                     evidence_level=k['lvl'], simulated_Q_G_hits=';'.join(g), simulated_Q_S_hits=';'.join(s),
                     simulated_retrievable_Scopus_Q_G_or_Q_S=bool(sim['SRCH_009'] or sim['SRCH_010']),
                     simulation_note='SIMULATION of exact frozen query strings on title+abstract excerpt; NOT retrieval evidence'))
os.makedirs(os.path.join(ROOT, 'tables'), exist_ok=True)
with open(os.path.join(ROOT, 'tables', 'A1_CORPUS_COVERAGE_AUDIT.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader(); w.writerows(rows)
for r in rows:
    print(r['candidate_id'], '| G:', r['simulated_Q_G_hits'], '| S:', r['simulated_Q_S_hits'], '| scopus:', r['simulated_retrievable_Scopus_Q_G_or_Q_S'])
