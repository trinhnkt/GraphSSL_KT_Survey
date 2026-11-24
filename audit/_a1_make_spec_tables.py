"""Prompt-01 conformant tables. Reads the extended v0.1 coverage table; writes the 14-column spec table for the 8 named candidates
and a seed-recall summary. Values are AI readings, not screening decisions."""
import csv, os, shutil
ROOT = r'D:\TRINH\GraphSSL_KT_Survey'
T = os.path.join(ROOT, 'tables')
ext = os.path.join(T, 'A1_CORPUS_COVERAGE_AUDIT_EXTENDED_v0.1.csv')
cur = os.path.join(T, 'A1_CORPUS_COVERAGE_AUDIT.csv')
if not os.path.exists(ext):
    shutil.copyfile(cur, ext)  # keep earlier 22-column version, never overwrite it
rows = list(csv.DictReader(open(ext, encoding='utf-8-sig')))

OVR = {  # candidate -> (KT, G, S, PRIMARY_CORE)
    'A1-C01': ('Y', 'Y', 'Y', 'PROVISIONAL_Y (AI reading of full text; needs human screen)'),
    'A1-C02': ('Y', 'N', 'Y', 'PROVISIONAL_Y via S (AI reading of full text; needs human screen)'),
    'A1-C03': ('Y', 'N (abstract only; full text not read)', 'Y', 'PROVISIONAL_Y via S (abstract only)'),
    'A1-C04': ('Y (title)', 'NEEDS_EVIDENCE', 'NEEDS_EVIDENCE', 'NEEDS_EVIDENCE (abstract not retrieved)'),
    'A1-C05': ('Y', 'Y', 'Y', 'PROVISIONAL_Y (AI reading of abstract + intro excerpt)'),
    'A1-C06': ('Y', 'Y', 'Y', 'PROVISIONAL_Y (AI reading of abstract)'),
    'A1-C07': ('Y', 'N (abstract only; verify no explicit graph)', 'Y', 'PROVISIONAL_Y via S (abstract only)'),
    'A1-C08': ('Y', 'N (abstract only)', 'Y', 'SAME PAPER AS A1-C03 (alias SP-CLKT)'),
}
ACTION = {
    'A1-C01': 'RE-SCREEN by human; supplementary-search coverage check; if included: sparse-concept + RQ3 relevant',
    'A1-C02': 'RE-SCREEN by human (seed KT040 BACKGROUND conflicts with SCOPE s5 sequence-contrastive family); protocol-deviation entry if reclassified',
    'A1-C03': 'RE-SCREEN by human after full text; confirm alias SP-CLKT',
    'A1-C04': 'GET abstract/full text, then RE-SCREEN',
    'A1-C05': 'RE-SCREEN by human; confirm from full text',
    'A1-C06': 'RE-SCREEN by human; obtain full text',
    'A1-C07': 'RE-SCREEN by human; confirm G=N and S objective from full text',
    'A1-C08': 'MERGE with A1-C03',
}
out = []
for r in rows:
    cid = r['candidate_id']
    if cid not in OVR:
        continue
    kt, g, s, pc = OVR[cid]
    out.append(dict(candidate_id=cid, title=r['title'], doi=r['DOI'],
                    present_raw='NEEDS_EVIDENCE (raw export not deposited; 16 export files named in search_log.csv are absent)',
                    present_dedup='NEEDS_EVIDENCE (no 750-row ledger; 04_deduplication/deduplication_audit_v1.0.csv has 34 AI-generated groups, no match)',
                    screening_stage=r['stage_reached'], original_decision=r['original_decision'], exclusion_code=r['exclusion_code'],
                    KT_central=kt, G_criterion=g, S_criterion=s, PRIMARY_CORE=pc,
                    evidence_locator=r['evidence_locator'], recommended_action=ACTION[cid]))
cols = ['candidate_id', 'title', 'doi', 'present_raw', 'present_dedup', 'screening_stage', 'original_decision', 'exclusion_code',
        'KT_central', 'G_criterion', 'S_criterion', 'PRIMARY_CORE', 'evidence_locator', 'recommended_action']
with open(cur, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(out)
print('spec rows', len(out))

seed = list(csv.DictReader(open(os.path.join(T, 'A1_SEED_RECALL.csv'), encoding='utf-8-sig')))
n = len(seed)
u = sum(1 for r in seed if r['simulated_retrievable_in_union_of_14_queries'] == 'True')
sc = sum(1 for r in seed if r['simulated_retrievable_in_Scopus_Q_G_or_Q_S'] == 'True')
summ = [
    ('seed_n', n, 'PRIMARY_CORE rows of 01_seed_corpus/included_papers_seed_audited_v1.0.csv'),
    ('retrieved_seed_actual', 'NEEDS_EVIDENCE', 'raw exports not deposited'),
    ('seed_recall_actual = retrieved_seed / 34', 'NEEDS_EVIDENCE', 'not computable'),
    ('simulated_retrieved_union_14_queries', u, 'simulation on title+abstract of deposited PDFs; not retrieval evidence'),
    ('simulated_seed_recall_union', round(u / n, 3), 'simulation only'),
    ('simulated_retrieved_Scopus_only', sc, 'KT014, KT016, KT037 not reachable with Scopus terms'),
    ('simulated_seed_recall_Scopus_only', round(sc / n, 3), 'simulation only'),
    ('ledger_asserted_duplicate_groups', 34, '04_deduplication/deduplication_audit_v1.0.csv; AI_ASSISTANT-authored; not accepted as retrieval evidence'),
]
with open(os.path.join(T, 'A1_SEED_RECALL_SUMMARY.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f); w.writerow(['metric', 'value', 'note']); w.writerows(summ)
for s_ in summ:
    print(s_)
