import csv
from collections import Counter
from pathlib import Path

qa = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\supplementary\supplementary_quality_scores.csv")
cols = [
    "QA1_task_clarity",
    "QA2_data_transparency",
    "QA3_split_control",
    "QA4_baseline_adequacy",
    "QA5_statistical_rigor",
    "QA6_author_artifacts_capped",
    "QA7_sparse_construct",
    "QA8_computational_reporting",
]
rows = list(csv.DictReader(qa.open(encoding="utf-8")))
print("n_rows", len(rows))
tiers = Counter(r["quality_tier"] for r in rows)
print("tiers", dict(tiers))
norms = [float(r["normalized_score"]) for r in rows]
print("mean", round(sum(norms) / len(norms), 4))
for c in cols:
    ctr = Counter(r[c] for r in rows)
    print(c, dict(sorted(ctr.items())))
    s = sum(int(r[c]) for r in rows)
    raw_ok = all(int(r["raw_score"]) == sum(int(r[k]) for k in cols) for r in rows)
print("raw_matches_sum", raw_ok)

old = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\tables\sparse_coldstart_audit.csv")
old_rows = list(csv.DictReader(old.open(encoding="utf-8")))
print("old_n", len(old_rows))
print("generic", Counter(r["generic_data_sparsity"] for r in old_rows))
print("old_drop", Counter(r["sparse_interaction_drop_eval"] for r in old_rows))

new = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\tables\sparse_coldstart_audit_v1.9.csv")
new_rows = list(csv.DictReader(new.open(encoding="utf-8")))
print("v19_n", len(new_rows))
print("v19_cols", new_rows[0].keys())
print("v19_drop", Counter(r["sparse_interaction_drop_eval"] for r in new_rows))
print("v19_item", Counter(r["item_cold_start"] for r in new_rows))
print("v19_kc", Counter(r["strict_kc_cold_start"] for r in new_rows))
print("v19_learn", Counter(r["learner_cold_start"] for r in new_rows))
