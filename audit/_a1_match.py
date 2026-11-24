"""Shared helper: SIMULATED application of the exact frozen queries (03_search/search_log.csv, Q-G / Q-S rows)
to a title + abstract-region text. This is NOT retrieval evidence (raw exports are not deposited)."""
import csv, re, os

ROOT = r'D:\TRINH\GraphSSL_KT_Survey'
CASE_SENSITIVE = {'GNN', 'GCN', 'GAT'}


def load_queries():
    qs = []
    for r in csv.DictReader(open(os.path.join(ROOT, '03_search', 'search_log.csv'), encoding='utf-8-sig')):
        if r['query_family'] not in ('Q-G', 'Q-S'):
            continue
        q = r['exact_query']
        arxiv = r['database'] == 'arXiv'
        tail = q.split(' AND ', 1)[1] if ' AND ' in q else q
        if arxiv:
            tail = q.split('AND (', 1)[1]
        tail = tail.replace('(', ' ').replace(')', ' ')
        terms = [t.strip().strip('"') for t in re.split(r'\sOR\s', tail.strip()) if t.strip()]
        qs.append(dict(id=r['search_id'], db=r['database'], fam=r['query_family'], terms=terms, arxiv=arxiv))
    return qs


QUERIES = load_queries()


def term_hit(txt, t):
    pat = r'\b' + re.escape(t) + r'\b' if ' ' not in t and t.isalpha() else re.escape(t)
    if t in CASE_SENSITIVE:
        return re.search(r'\b' + t + r'\b', txt) is not None
    return re.search(pat, txt, re.I) is not None


def simulate(title, abstract_region):
    """return dict {search_id: bool}"""
    full = title + ' ' + abstract_region
    kt_full = re.search(r'knowledge tracing', full, re.I) is not None
    kt_title = re.search(r'knowledge tracing', title, re.I) is not None
    out = {}
    for q in QUERIES:
        has = any(term_hit(full, t) for t in q['terms'])
        if q['arxiv']:
            out[q['id']] = kt_title or (kt_full and has)  # arXiv query as written: ti:(KT) OR abs:(KT AND (...))
        else:
            out[q['id']] = kt_full and has
    return out


def summarize(sim):
    g = [k for k, v in sim.items() if v and [q for q in QUERIES if q['id'] == k][0]['fam'] == 'Q-G']
    s = [k for k, v in sim.items() if v and [q for q in QUERIES if q['id'] == k][0]['fam'] == 'Q-S']
    return g, s


if __name__ == '__main__':
    for q in QUERIES:
        print(q['id'], q['db'], q['fam'], q['terms'])
