"""Build v1.9 provenance sub-bin table, 8-way appendix, and provenance x encoder cross-tab.
Read-only w.r.t. deposited artifacts; writes new v1.9 files under supplementary/.
Sub-bins are assigned by a documented deterministic rule; NOT re-read from PDFs.
"""
import csv, collections, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tax = list(csv.DictReader(open(os.path.join(BASE, 'tables', 'graph_taxonomy.csv'), encoding='utf-8')))
aud = {r['paper_id']: r for r in csv.DictReader(open(os.path.join(BASE, 'supplementary', 'graph_provenance_8way_audit_v1.9.csv'), encoding='utf-8'))}

# Manual resolutions of four papers whose coding records are not in the markdown format (xlsx / v0.4 md)
MANUAL = {
    'KT004': ('MIXED[Dense=MODEL_DEFINED_FIXED;Transition=PRECOMPUTED_UNCLEAR_SPLIT]', 'codebook CB09 table / KT004 adjudication v0.3'),
    'KT014': ('EXTERNAL_FIXED', 'WAVE_A_KT039_KT035_KT014_CODING_v0.3.xlsx'),
    'KT026': ('PRECOMPUTED_UNCLEAR_SPLIT', 'KT026_CODING_v0.4.md line 46 (IRR gold later adjudicated to MODEL_DEFINED_FIXED from PDF)'),
    'KT035': ('UNCLEAR', 'WAVE_A coding v0.3 (accessible abstract only); no later full-text 8-way value located'),
}
# Documented PDF-level adjudication / recode that supersedes the per-paper record
DOCUMENTED = {
    'KT026': 'IRR adjudication to locked gold (PDF p.3)',
    'KT031': 'IRR locked gold (PDF)', 'KT044': 'IRR locked gold (PDF p.4; ADJUDICATION_FIVE_DIFFS)',
    'KT047': 'IRR locked gold (PDF Sec.3.3)', 'KT068': 'IRR locked gold (PDF Sec.4.2-4.3)',
    'KT070': 'IRR locked gold (PDF Sec.3.1.1)', 'KT076': 'IRR locked gold (PDF p.7)',
    'KT016': 'DEV-20261106-03 PDF-strict recode', 'KT036': 'DEV-20261106-03 PDF-strict recode',
    'KT052': 'DEV-20261106-03 PDF-strict recode',
}
LOG_SOURCES = {'COOCCURRENCE_SIMILARITY', 'COOCCURRENCE_INFLUENCE', 'SESSION_GRAPH', 'SEQUENTIAL_TRANSITION', 'Q_MATRIX_COOCCURRENCE', 'DENSE_CONCEPT_GRAPH_AND_TRANSITION'}
DATA_DERIVED_8 = {'PRECOMPUTED_UNCLEAR_SPLIT', 'TRAIN_ONLY_INFERRED', 'FULL_DATA_INFERRED'}


def collapse(v):
    return v


# paper-level rows (KT004 collapsed)
papers = collections.OrderedDict()
for r in tax:
    pid = r['paper_id'].split('_')[0]
    if pid in papers:
        papers[pid]['sources'].add(r['graph_source'])
        continue
    papers[pid] = dict(pid=pid, model=r['model_entry'].split(' (')[0], disp=r['graph_provenance'], sources={r['graph_source']}, enc=r['gnn_encoder'])

ENC_GROUP = {'GCN': 'GCN/generic', 'GNN_GENERIC': 'GCN/generic', 'HETEROGENEOUS_GNN': 'Heterogeneous', 'GAT': 'GAT',
             'HYPERGRAPH_GNN': 'Hypergraph', 'DYNAMIC_GNN': 'Dynamic GNN', 'NONE': 'None (no GNN)'}
ENC_ORDER = ['GCN/generic', 'Heterogeneous', 'GAT', 'Hypergraph', 'Dynamic GNN', 'None (no GNN)', 'Other']
SUB = ['Q-matrix/expert-authored', 'Log-derived', 'Architecture-defined', 'External', 'Dynamic-learned']

out = []
for pid, p in papers.items():
    if p['disp'] == 'NA':
        continue
    a = aud[pid]
    rec = MANUAL[pid][0] if pid in MANUAL else a['coding_file_8way_graph_provenance']
    rec_src = MANUAL[pid][1] if pid in MANUAL else a['coding_file']
    src = sorted(p['sources'])
    if p['disp'] == 'MODEL_DEFINED_FIXED':
        has_log = any(s in LOG_SOURCES for s in src) or rec in DATA_DERIVED_8 or rec.startswith('MIXED')
        q_only = set(src) <= {'Q_MATRIX_DERIVED'}
        if q_only and not has_log or (q_only and rec == 'PRECOMPUTED_UNCLEAR_SPLIT' and pid in ('KT010', 'KT026', 'KT053')):
            sub = 'Q-matrix/expert-authored'
        elif has_log:
            sub = 'Log-derived'
        else:
            sub = 'Architecture-defined'
    elif p['disp'] == 'EXTERNAL_FIXED':
        sub = 'External'
    else:
        sub = 'Dynamic-learned'
    # does the 8-way record map to the displayed token?
    r8 = rec
    if r8.startswith('MIXED'):
        mapped = 'MODEL_DEFINED_FIXED'
    elif r8 in ('MODEL_DEFINED_FIXED', 'PRECOMPUTED_UNCLEAR_SPLIT', 'TRAIN_ONLY_INFERRED', 'FULL_DATA_INFERRED', 'MIXED_PROVENANCE'):
        mapped = 'MODEL_DEFINED_FIXED'
    elif r8 in ('EXTERNAL_FIXED',):
        mapped = 'EXTERNAL_FIXED'
    elif r8 in ('JOINTLY_LEARNED_TRAINING', 'PRETRAINED_TWO_STAGE'):
        mapped = 'DYNAMIC_LEARNED'
    else:
        mapped = 'UNMAPPED(' + r8 + ')'
    agrees = (mapped == p['disp'])
    if agrees:
        status = 'AGREES'
    elif pid in DOCUMENTED:
        status = 'DIFFERS_DOCUMENTED: ' + DOCUMENTED[pid]
    else:
        status = 'DIFFERS_UNDOCUMENTED'
    out.append(dict(paper_id=pid, model=p['model'], display_3token=p['disp'], record_8way=rec, record_source=rec_src,
                    graph_source=';'.join(src), subbin_v1_9=sub, display_vs_record=status, gnn_encoder=p['enc']))

path = os.path.join(BASE, 'supplementary', 'graph_provenance_subbins_8way_v1.9.csv')
with open(path, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
    w.writeheader(); w.writerows(out)

print('papers', len(out))
print('subbins', collections.Counter(o['subbin_v1_9'] for o in out))
print('status', collections.Counter(o['display_vs_record'].split(':')[0] for o in out))
print('8way (record, KT004 mixed)', collections.Counter(o['record_8way'].split('[')[0] for o in out))
print('UNDOCUMENTED:', [o['paper_id'] + ' ' + o['display_3token'] + ' vs ' + o['record_8way'] for o in out if o['display_vs_record'] == 'DIFFERS_UNDOCUMENTED'])
print('DOCUMENTED:', [o['paper_id'] for o in out if o['display_vs_record'].startswith('DIFFERS_DOC')])
for sb in ['Q-matrix/expert-authored', 'Log-derived', 'Architecture-defined']:
    print(sb, [o['paper_id'] for o in out if o['subbin_v1_9'] == sb])

# cross-tab
ct = collections.defaultdict(int)
for o in out:
    g = ENC_GROUP.get(o['gnn_encoder'], 'Other')
    ct[(g, o['subbin_v1_9'])] += 1
cpath = os.path.join(BASE, 'supplementary', 'graph_provenance_x_encoder_crosstab_v1.9.csv')
with open(cpath, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['encoder_group'] + SUB + ['row_total'])
    for e in ENC_ORDER:
        row = [ct[(e, s)] for s in SUB]
        w.writerow([e] + row + [sum(row)])
    tot = [sum(ct[(e, s)] for e in ENC_ORDER) for s in SUB]
    w.writerow(['col_total'] + tot + [sum(tot)])
print()
print('encoder'.ljust(16), *[s[:10].ljust(11) for s in SUB], 'tot')
for e in ENC_ORDER:
    row = [ct[(e, s)] for s in SUB]
    print(e.ljust(16), *[str(x).ljust(11) for x in row], sum(row))
print('col'.ljust(16), *[str(sum(ct[(e, s)] for e in ENC_ORDER)).ljust(11) for s in SUB])
print('empty cells', sum(1 for e in ENC_ORDER for s in SUB if ct[(e, s)] == 0), 'of', len(ENC_ORDER) * len(SUB))
