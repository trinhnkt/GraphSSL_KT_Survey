"""A1.5 / A1.6 helper (v2). Writes tables/A1_SEED_RECALL.csv and tables/A1_SNOWBALLING_LOG.csv.
SEED RECALL: SIMULATED application of the exact frozen queries to title + abstract region of the deposited PDF.
  NOT retrieval evidence (raw exports not deposited). actual retrieval = NEEDS_EVIDENCE.
SNOWBALLING: BACKWARD only (regex over reference sections). FORWARD = NEEDS_EXTERNAL_VERIFICATION.
"""
import csv, os, re, glob, sys, collections
import fitz
sys.path.insert(0, os.path.dirname(__file__))
import _a1_match as M

ROOT = M.ROOT
REF = os.path.join(ROOT, '14_references')
OUT = os.path.join(ROOT, 'tables')
EVID = os.path.join(ROOT, 'audit', '_a1_evidence')
os.makedirs(OUT, exist_ok=True)


def norm(s):
    return re.sub(r'[^a-z0-9 ]', ' ', s.lower()).split()


def jac(a, b):
    A, B = set(norm(a)), set(norm(b))
    return len(A & B) / max(1, len(A | B))


pdfs = glob.glob(os.path.join(REF, '*.pdf'))
seed = list(csv.DictReader(open(os.path.join(ROOT, '01_seed_corpus', 'included_papers_seed_audited_v1.0.csv'), encoding='utf-8-sig')))
core = [r for r in seed if r['seed_classification_v1_0'] == 'PRIMARY_CORE']
assert len(core) == 34


def abstract_region(path):
    d = fitz.open(path)
    t = re.sub(r'\s+', ' ', ' '.join(p.get_text() for p in d[:2]))
    d.close()
    m = re.search(r'\b(I\.\s+)?(INTRODUCTION|Introduction)\b', t[300:])
    end = 300 + m.start() if m else 3000
    return t[:min(end, 3500)]


rows = []
for r in core:
    best, bs = None, 0
    for p in pdfs:
        s = jac(r['title'], os.path.basename(p)[:-4])
        if s > bs:
            best, bs = p, s
    row = dict(seed_id=r['legacy_id'], title=r['title'], year=r['year'], venue=r['venue'],
               pdf_in_repo=os.path.basename(best) if bs >= 0.45 else '', pdf_match_score=round(bs, 2))
    if bs >= 0.45:
        sim = M.simulate(r['title'], abstract_region(best))
        g, s = M.summarize(sim)
        row.update(simulated_hits_Q_G=';'.join(g), simulated_hits_Q_S=';'.join(s),
                   simulated_retrievable_in_union_of_14_queries=bool(g or s),
                   simulated_retrievable_in_Scopus_Q_G_or_Q_S=bool(sim['SRCH_009'] or sim['SRCH_010']))
    else:
        row.update(simulated_hits_Q_G='', simulated_hits_Q_S='', simulated_retrievable_in_union_of_14_queries='NOT_SIMULATED_NO_PDF',
                   simulated_retrievable_in_Scopus_Q_G_or_Q_S='NOT_SIMULATED_NO_PDF')
    row['actual_retrieved_from_raw_2017'] = 'NEEDS_EVIDENCE (raw exports not deposited)'
    rows.append(row)
with open(os.path.join(OUT, 'A1_SEED_RECALL.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
u = [r for r in rows if r['simulated_retrievable_in_union_of_14_queries'] is True]
sc = [r for r in rows if r['simulated_retrievable_in_Scopus_Q_G_or_Q_S'] is True]
print('seed n=', len(rows), 'sim union', len(u), 'sim scopus', len(sc))
print('NOT in union:', [(r['seed_id'], r['title'][:50]) for r in rows if r['simulated_retrievable_in_union_of_14_queries'] is False])
print('NOT in scopus:', [(r['seed_id'], r['title'][:40]) for r in rows if r['simulated_retrievable_in_Scopus_Q_G_or_Q_S'] is False])
print('no pdf:', [r['seed_id'] for r in rows if r['pdf_in_repo'] == ''])

# ---------------- backward snowballing ----------------
corpus_titles = [r['title'] for r in seed] + [os.path.basename(x)[:-4] for x in pdfs]
sources = {
    'KT011 Bi-CLKT': 'Bi-CLKT',
    'KT039 CL4KT': 'Contrastive Learning for Knowledge Tracing',
    'KT042 S2-HHN': 'Self-Supervised Heterogeneous Hypergraph',
    'KT043 3V-CLKT': 'Three-View Contrastive',
    'KT047 Wu&Ling DC-SSL': 'Fusing Hybrid Attentive Network',
    'KT050 GraphCA': 'GraphCA',
    'KT066 HyperKT': 'Dual-Channel Adaptive Scale Hypergraph',
    'KT068 HKT': 'HKT - Hierarchical',
    'KT026 PEBG': 'Pre-training Question Embeddings',
    'Xu et al. Graph-KT survey': 'A Survey of Graph-Based Knowledge Tracing',
}
texts = {}
for label, key in sources.items():
    p = [x for x in pdfs if key.lower() in os.path.basename(x).lower()]
    if not p:
        print('NO PDF for', label); continue
    d = fitz.open(p[0]); texts[label] = '\n'.join(pg.get_text() for pg in d); d.close()
for label, fn in [('DECKT (if eligible)', 'DECKT_fulltext_PMC12294018.txt'), ('DTransformer (if eligible)', 'DTransformer_fulltext_yin2023.txt')]:
    fp = os.path.join(EVID, fn)
    if os.path.exists(fp):
        texts[label] = open(fp, encoding='utf-8', errors='ignore').read()

KEY = re.compile(r'(contrastive|self-supervised|self supervised|graph|hypergraph|heterogeneous|prerequisite|concept map|knowledge structure|knowledge graph)', re.I)
START = re.compile(r'^(\[\d{1,3}\]|\d{1,3}\.\s|[A-Z][A-Z\'\-]+(?: [A-Z\'\-]+)*, [A-Z]\.|[A-Z][a-z]+(?:-[A-Z][a-z]+)?,\s[A-Z]\.|[A-Z]\.\s?[A-Z][a-z]+)')
DOI = re.compile(r'10\.\d{4,9}/[^\s,;]+')
snow, seen = [], set()
for label, t in texts.items():
    idx = max(t.rfind('\nReferences'), t.rfind('REFERENCES'), t.rfind('## References'), t.rfind('REFERENCES'))
    ref = t[idx:] if idx > 0 and len(t) - idx > 1500 else t[int(len(t) * 0.7):]
    lines = ref.split('\n')
    entries, cur = [], ''
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        if START.match(s) and len(cur) > 40:
            entries.append(cur); cur = s
        else:
            cur = (cur[:-1] + s) if cur.endswith('-') else (cur + ' ' + s if cur else s)
    if cur:
        entries.append(cur)
    # DECKT/DTransformer text blobs may have entries in single line; also split on [n]
    ex = []
    for e in entries:
        ex.extend([x for x in re.split(r'(?=\[\d{1,3}\]\s)', e) if len(x) > 40])
    for e in ex:
        if re.search(r'received the|e1 e2 e3', e):
            continue
        if re.search(r'knowledge tracing|knowledge-tracing|\bKT\b', e, re.I) and KEY.search(e):
            key = ' '.join(norm(e)[:14])
            if (label, key) in seen:
                continue
            seen.add((label, key))
            dm = DOI.search(e)
            matched = max((jac(e[:220], ct) for ct in corpus_titles), default=0) >= 0.30
            snow.append(dict(source_paper=label, direction='BACKWARD', candidate=e[:300], DOI=dm.group(0).rstrip('.') if dm else '',
                             reason_found='reference string matches (knowledge tracing) AND (graph|contrastive|self-supervised|prerequisite|...) regex; no manual parse',
                             screened='NO', inclusion_decision='FUZZY_TITLE_MATCH_TO_SEED75_OR_14_REFERENCES_PDF (Jaccard>=0.30; approximate, verify)' if matched else 'NO_FUZZY_MATCH -> NEEDS_HUMAN_DECISION',
                             evidence='reference-list text of source file; eligibility not assessed'))
for label in texts:
    snow.append(dict(source_paper=label, direction='FORWARD', candidate='', DOI='',
                     reason_found='forward citation search not performed (no citation-index access in this environment)', screened='NO',
                     inclusion_decision='NEEDS_EXTERNAL_VERIFICATION', evidence='run cited-by in Scopus/WoS/Google Scholar and log here'))
with open(os.path.join(OUT, 'A1_SNOWBALLING_LOG.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=['source_paper', 'direction', 'candidate', 'DOI', 'reason_found', 'screened', 'inclusion_decision', 'evidence'])
    w.writeheader(); w.writerows(snow)
bw = [s for s in snow if s['direction'] == 'BACKWARD']
print('backward rows', len(bw), 'needs human', sum(1 for s in bw if s['inclusion_decision'].startswith('NO_FUZZY')))
print(collections.Counter(s['source_paper'] for s in bw))
