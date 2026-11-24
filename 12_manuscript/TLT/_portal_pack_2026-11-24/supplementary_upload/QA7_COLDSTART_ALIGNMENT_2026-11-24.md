# QA7 alignment to locked cold-start fields

Date: 2026-11-24.

Rule: QA7 = 2 iff at least one of interaction_drop / item_cold_start / learner_cold_start / strict_KC_cold_start is YES under the locked decision table; else 0 for these rows (no QA7=1 used here).

| paper_id | cold-start YES | QA7 before | QA7 after | raw before | raw after | tier before | tier after |
|---|---|---:|---:|---:|---:|---|---|
| KT035 HHSKT | none | 2 | 0 | 13 | 11 | HIGH | MODERATE |
| KT023 SGKT | learner | 0 | 2 | 12 | 14 | MODERATE | HIGH |

Corpus after sync: HIGH 13, MODERATE 31, LIMITED 0, mean 0.7472.
QA7 item distribution remains 0→40, 1→0, 2→4.
HIGH IDs: KT023, KT029, KT033, KT038, KT040, KT044, KT050, KT060, KT064, KT066, KT070, KT077, KT087.

Machine files: `PRIMARY_CORE_EXPANDED_2026-11-24.csv` (updated), aligned copy `PRIMARY_CORE_EXPANDED_2026-11-24_QA7ALIGNED.csv`, pre-align snapshot `PRIMARY_CORE_EXPANDED_2026-11-24_PRE_QA7ALIGN.csv`.
Prior carry-forward note in `COUNTS_EXPANDED_FINAL.md` is superseded for these two cells.
