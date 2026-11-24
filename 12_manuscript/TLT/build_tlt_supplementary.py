"""Build TLT_Supplementary_Evidence_Tables.md from locked CSVs. No new counts."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "TLT_Supplementary_Evidence_Tables.md"

def _rows(p):
    return list(csv.DictReader(Path(p).open(encoding="utf-8-sig")))

graph_rows = _rows(ROOT / "tables" / "graph_taxonomy.csv")
ssl_rows = _rows(ROOT / "tables" / "ssl_taxonomy.csv")
sparse_rows = _rows(ROOT / "tables" / "sparse_coldstart_audit.csv")
search_rows = _rows(Path(r"D:\TRINH\GraphSSL_KT_Survey\03_search\search_log.csv"))
qa_rows = _rows(ROOT / "supplementary" / "supplementary_quality_scores.csv")
h1_rows = _rows(ROOT / "tables" / "H1_ssl_criterion_audit.csv")

ssl_ids = {r["paper_id"] for r in ssl_rows}
sparse_by = {r["paper_id"]: r for r in sparse_rows}
ssl_by = {r["paper_id"]: r for r in ssl_rows}

# Unique graph papers: prefix before _Dense/_Trans
unique_graph = {}
for r in graph_rows:
    pid = r["paper_id"].split("_")[0] if r["paper_id"].startswith("KT004_") else r["paper_id"]
    if pid == "KT039":
        continue
    unique_graph.setdefault(pid, r)

cite = {
    "KT004": "KT004_GKT_2019", "KT010": "KT010_GIKT_2021", "KT011": "KT011_BiCLKT_2022",
    "KT012": "KT012_JKT_2021", "KT014": "KT014_PDKTC_2018", "KT016": "KT016_SKT_2020",
    "KT023": "KT023_SGKT_2022", "KT026": "KT026_PretrainQ_2020", "KT029": "KT029_DGEKT_2024",
    "KT031": "KT031_KSGAKT_2022", "KT033": "KT033_DGMN_2023", "KT035": "KT035_HHSKT_2023",
    "KT036": "KT036_TSKT_2024", "KT037": "KT037_CMKT_2022", "KT038": "KT038_DyGKT_2024",
    "KT039": "KT039_CL4KT_2022", "KT042": "KT042_S2HHN_2023", "KT043": "KT043_3VCLKT_2024",
    "KT044": "KT044_SINKT_2024", "KT047": "KT047_DCSSL_2023", "KT050": "KT050_GraphCA_2023",
    "KT052": "KT052_CapsuleGNN_2022", "KT053": "KT053_GASKT_2021", "KT056": "KT056_LSTGraph_2025",
    "KT060": "KT060_STHKT_2025", "KT062": "KT062_LGSKT_2025", "KT063": "KT063_MAHKT_2025",
    "KT064": "KT064_MGEnsemble_2025", "KT065": "KT065_CSGKT_2025", "KT066": "KT066_HyperKT_2025",
    "KT067": "KT067_SKMGKT_2025", "KT068": "KT068_HKT_2025", "KT069": "KT069_AEGOTCDKT_2025",
    "KT070": "KT070_Coda_2025", "KT076": "KT076_KGNNKT_2025", "KT077": "KT077_R2GCurL_2026",
    "KT079": "KT079_STGSKT_2026",
}

all_ids = sorted(set(unique_graph) | {"KT039"} | set(sparse_by), key=lambda x: int(x[2:]))

lines = []
A = lines.append
A("# TLT Supplementary Evidence Tables")
A("")
A("Date: 2026-09-13. Sources are locked CSVs and `00_protocol/SLR_PROTOCOL_v1.0_LOCKED.md`.")
A("No new screening, coding, QA, or reliability numbers are invented here.")
A("")
A("**Locked identity (do not use N_S=14):** $N=37$, $N_G=36$, $N_S=9$, $N_{G\\cap S}=8$ ($36+9-8=37$).")
A("Historical 14-row SSL lists are superseded by `audit/H1_SSL_CRITERION_DECISION.md`.")
A("")
A("## 1. Search strings by query family")
A("")
A("Copied from locked protocol §6–7 (`SLR_PROTOCOL_v1.0_LOCKED.md`). Database runs may use adapted syntax; exact adapted strings are in §2.")
A("")
A("### Q-G Graph-KT")
A("")
A("```")
A('("knowledge tracing" OR "student knowledge tracing") AND (graph OR "graph neural network" OR GNN OR GCN OR GAT OR hypergraph OR heterogeneous OR "dynamic graph" OR "temporal graph" OR prerequisite OR "prerequisite graph" OR "concept map" OR "skill graph" OR "knowledge graph" OR "concept graph" OR "knowledge structure" OR "multi-relational" OR "multi relational")')
A("```")
A("")
A("### Q-S Self-Supervised KT")
A("")
A("```")
A('("knowledge tracing" OR "student knowledge tracing") AND ("self-supervised" OR "self supervised" OR contrastive OR "masked modeling" OR "masked prediction" OR "masked interaction" OR "masked concept" OR reconstruction OR "pretext task" OR "self-distillation" OR "self distillation" OR "teacher student" OR "teacher-student" OR "consistency learning")')
A("```")
A("")
A("### Q-P Sparse-Concept Lens")
A("")
A("```")
A('("knowledge tracing" OR "student knowledge tracing") AND (sparse OR sparsity OR "low frequency" OR "low-frequency" OR "long tail" OR long-tail OR few-shot OR "few shot" OR "cold start" OR cold-start OR unseen OR inductive) AND (concept OR skill OR "knowledge component" OR item OR exercise OR learner)')
A("```")
A("")
A("### Q-R Reliability Lens")
A("")
A("```")
A('("knowledge tracing" OR "student knowledge tracing") AND (calibration OR reproducibility OR leakage OR "temporal split" OR "learner split" OR "cold start" OR cold-start OR "confidence interval" OR bootstrap OR "statistical significance" OR "multiple comparison" OR "effect size" OR scalability OR "training time" OR memory)')
A("```")
A("")
A("## 2. Database execution table")
A("")
A("Per-query rows: `03_search/search_log.csv` (search date 2026-08-26).")
A("Locked identification totals (`tables/corpus_counts.csv`): Scopus 531, WoS 344, ScienceDirect 257, SpringerLink 255, IEEE Xplore 232, ACM DL 200, arXiv 198; sum $N_{\\mathrm{IDENTIFIED}}=2{,}017$.")
A("")
A("| search_id | database | family | date | records_returned | notes |")
A("|---|---|---|---|---:|---|")
for r in search_rows:
    A(f"| {r['search_id']} | {r['database']} | {r['query_family']} | {r['search_date']} | {r['records_returned']} | {r['notes']} |")
A("")
A("Exact adapted queries are in `03_search/search_log.csv` column `exact_query`.")
A("")
A("## 3. Inclusion / exclusion")
A("")
A("- Gateway: `PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)` (`SCOPE_v1.0_LOCKED.md` §5; protocol §12.1).")
A("- EC1_NO_KT; EC2_CD_ONLY; EC3_RECOMMENDATION_ONLY; EC4_GENERIC_GRAPH_SSL; EC5_LLM_TUTOR_ONLY; EC6_SPARSE_ATTENTION_ONLY; EC7_WRONG_PUBLICATION_TYPE (`SLR_PROTOCOL_v1.0_LOCKED.md` §13).")
A("- Also defined: EC10_NON_ENGLISH; EC11_PERFORMANCE_PREDICTION_NOT_KT; EC12_OUTSIDE_DATE_WINDOW; EC13_OTHER.")
A("- PRISMA arithmetic: $2{,}017-1{,}267=750$; $750-610=140$; $140-103=37$.")
A("")
A("## 4. Full 37-paper corpus")
A("")
A("Graph fields: `tables/graph_taxonomy.csv` (KT004 is one paper; Dense/Trans are model entries).")
A("SSL: `tables/ssl_taxonomy.csv` ($N_S=9$). Sparse: `tables/sparse_coldstart_audit.csv`.")
A("ECE reporting is a corpus-level audit ($0/37$); there is no per-paper ECE locator file beyond that locked claim.")
A("")
A("| paper_id | cite key | year | venue | Graph | SSL | provenance | encoder | sparse/cold-start | ECE reported |")
A("|---|---|---|---|---|---|---|---|---|---|")
for pid in all_ids:
    g = unique_graph.get(pid)
    if pid == "KT039":
        graph_yn = "NO"
        prov = "NA"
        enc = "NONE"
        venue = "WWW 2022"
        year = "2022"
    else:
        graph_yn = "YES"
        prov = g["graph_provenance"] if g else "Data required from locked coding sheets."
        enc = g["gnn_encoder"] if g else ""
        venue = g["venue_year"] if g else ""
        year = venue.split()[-1] if venue else ""
    ssl_yn = "YES" if pid in ssl_ids else "NO"
    sp = sparse_by.get(pid, {})
    cat = sp.get("sparse_protocol_category", "")
    A(f"| {pid} | {cite.get(pid,'')} | {year} | {venue} | {graph_yn} | {ssl_yn} | {prov} | {enc} | {cat} | NO |")
A("")
A(f"Row count in this table: {len(all_ids)} (must be 37).")
A("")
A("## 5. Field-level evidence for locked claims")
A("")
n_strict = sum(1 for r in sparse_rows if r.get("strict_kc_cold_start") == "YES")
n_item = sum(1 for r in sparse_rows if r.get("item_cold_start") == "YES")
A(f"### Strict KC cold-start YES = {n_strict}/37; item cold-start YES = {n_item}/37")
A("")
A("| paper_id | strict_kc_cold_start | item_cold_start | learner_cold_start | source |")
A("|---|---|---|---|---|")
for r in sparse_rows:
    if r["strict_kc_cold_start"] == "YES" or r["item_cold_start"] == "YES":
        A(f"| {r['paper_id']} | {r['strict_kc_cold_start']} | {r['item_cold_start']} | {r['learner_cold_start']} | tables/sparse_coldstart_audit.csv |")
A("")
A("All other primary-core rows are NO / NO / NO for those three fields (see the same CSV).")
A("")
A("### ECE reporting = 0/37")
A("")
A("Locked statement in `audit/LOCKED_COUNTS_v1.5.md`. No manuscript in the 37-paper set is coded as reporting ECE.")
A("That **manuscript-reporting** claim is unchanged.")
A("")
A("### Survey-computed REPRODUCED ECE overlay (Path A; not a corpus count)")
A("")
A("Source: `09_benchmark/path_a_ece/results/dygkt_assist17_ece.json` and `RUN_LOG_DyGKT_assist17.md`.")
A("Author code: DyGKT (`KT038`); dataset ASSIST17; seed 0; equal-width $M=10$ on the transductive test split.")
A("")
A("| paper_id | model | dataset | split | n | ECE (M=10) | Brier | test AUC (author metric) | evidence_source_type |")
A("|---|---|---|---|---:|---:|---:|---:|---|")
A("| KT038 | DyGKT | assist17 | test | 94156 | 0.0361 | 0.1770 | 0.8025 | REPRODUCED |")
A("")
A("Do **not** rewrite the $0/37$ manuscript-reported ECE cell to YES. Do **not** pool this overlay into a cross-paper ECE ranking.")
A("")
A("### H1 S-criterion (why N_S=9, not 14)")
A("")
A("| paper_id | S_criterion | note |")
A("|---|---|---|")
for r in h1_rows:
    A(f"| {r['paper_id']} | {r['S_criterion']} | {r['evidence_note'][:160].replace('|','/')} |")
A("")
A("## 6. QA1–QA8 scores")
A("")
A("Source file: `supplementary/supplementary_quality_scores.csv`.")
A("Manuscript tiers use `audit/LOCKED_COUNTS_v1.5.md`: drop KT078 and KT080–KT083; cap QA6 at 2; HIGH 11 / MODERATE 26 / mean 0.76.")
A("HIGH IDs (locked): KT029, KT033, KT035, KT038, KT044, KT050, KT060, KT064, KT066, KT070, KT077.")
A("Some `raw_score` cells in the CSV do not equal the arithmetic sum of QA1–QA8; **do not invent a corrected score**. Use the locked HIGH list for manuscript claims.")
A("")
A("| paper_id | QA1 | QA2 | QA3 | QA4 | QA5 | QA6 | QA7 | QA8 | raw_score (file) | norm (file) | tier (file) |")
A("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|")
keep = {f"KT{i:03d}" for i in range(1, 80)}
keep |= {"KT004","KT010","KT011","KT012","KT014","KT016","KT023","KT026","KT029","KT031","KT033","KT035","KT036","KT037","KT038","KT039","KT042","KT043","KT044","KT047","KT050","KT052","KT053","KT056","KT060","KT062","KT063","KT064","KT065","KT066","KT067","KT068","KT069","KT070","KT076","KT077","KT079"}
for r in qa_rows:
    if r["paper_id"] not in keep:
        continue
    A(
        f"| {r['paper_id']} | {r['QA1_task_clarity']} | {r['QA2_data_transparency']} | {r['QA3_split_control']} | {r['QA4_baseline_adequacy']} | {r['QA5_statistical_rigor']} | {r['QA6_author_artifacts']} | {r['QA7_sparse_construct']} | {r['QA8_computational_reporting']} | {r['raw_score']} | {r['normalized_score']} | {r['quality_tier']} |"
    )
A("")
A("Excluded from the 37-paper QA claim (present in the raw file only): KT078, KT080, KT081, KT082, KT083.")
A("")
A("## 7. Coder reliability / adjudication")
A("")
A("Coding-sample pair table: `supplementary/inter_rater_coding.csv` (20 papers × 8 fields; locator-assisted NguyenKT).")
A("B as submitted: `08_quality_reliability/inter_rater_coding_sample_BLIND_EMPTY_v1.3_AS_SUBMITTED.csv` (`coderB_id=NguyenKT`).")
A("Kappa record: `08_quality_reliability/KAPPA_A_vs_B_SUBMITTED_2026-09-13.md`.")
A("Coder B used a quote locator pack; this is **not** a fully independent blind pass.")
A("")
A("Independent 20-paper pass: `08_quality_reliability/inter_rater_coding_sample_BLIND_EMPTY_v1.4_DaoMT_FULL20_AS_SUBMITTED.csv` (`coderB_id=DaoMT`, no locator).")
A("Kappa record: `08_quality_reliability/KAPPA_A_vs_DaoMT_FULL20_2026-09-14.md` (157/160; mean 0.97). Not pooled with NguyenKT.")
A("Adjudication (same three cells as the 10-paper subset): `08_quality_reliability/ADJUDICATION_DaoMT_THREE_DIFFS_2026-09-14.md`.")
A("Do **not** use `08_quality_reliability/INTER_RATER_RELIABILITY_REPORT_v1.0.md` (no pair table; $N=42$).")
A("")
A("Still absent (protocol §20–21): `inter_rater_screening.csv`, `inter_rater_fulltext.csv`.")
A("")
A("| Item | Status |")
A("|---|---|")
A("| Double-coded primary-core papers | 20/37 coding sample |")
A("| Pre-adjudication (NguyenKT, locator) | 158/160; mean kappa 0.98 |")
A("| Pre-adjudication (DaoMT, independent) | 157/160; mean kappa 0.97 |")
A("| Adjudicated cells | KT011/KT047 family → MULTIVIEW; KT026 provenance → MODEL_DEFINED; KT070 provenance → DYNAMIC; KT068 encoder → GNN_GENERIC |")
A("| Screening / full-text pair files | Not present |")
A("")

OUT.write_text("\n".join(lines), encoding="utf-8")
print("Wrote", OUT, "corpus_rows", len(all_ids))
