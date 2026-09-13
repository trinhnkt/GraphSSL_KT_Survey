# F9 – PRE‑A15 GATE AUDIT

**Status:** TODO – Aggregate PASS/FAIL of F1‑F8 and set readiness flag.

**Required actions**:
1. Read each `audit/F*_*.md` file and extract the line `**Status:** PASS` or `FAIL`.
2. If **all** are `PASS`, write `READY_FOR_FINAL_A15 = YES` to `status/ready_for_A15.md` and set this file's status to `PASS`.
3. Otherwise, write `READY_FOR_FINAL_A15 = NO` and list the failing tasks.

**Outputs**:
- `audit/F9_PRE_A15_GATE.md`
- `status/ready_for_A15.md`

**Notes**: After running the gate script, replace `TODO` with `PASS` or `FAIL` and add the appropriate links.
