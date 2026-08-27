from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    "AGENTS.md",
    "START_HERE.md",
    "CURRENT_STATUS.md",
    "NEXT_TASK.md",
    "00_protocol/SCOPE_v1.0_LOCKED.md",
    "00_protocol/RQs_v1.0_LOCKED.md",
    "00_protocol/SLR_PROTOCOL_v1.0_LOCKED.md",
    "00_protocol/coding_codebook_v0.3_PILOT.md",
    "01_seed_corpus/included_papers_seed_audited_v1.0.csv",
    "02_pilot_coding/pilot_papers_15_v1.0.csv",
    "02_pilot_coding/WAVE_A_REVIEW_v0.3.md",
]

missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print("FAIL: missing required files")
    for p in missing:
        print(" -", p)
    sys.exit(1)

seed = ROOT / "01_seed_corpus/included_papers_seed_audited_v1.0.csv"
with seed.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
if len(rows) != 75:
    print(f"FAIL: expected 75 seed rows, found {len(rows)}")
    sys.exit(1)

pilot = ROOT / "02_pilot_coding/pilot_papers_15_v1.0.csv"
with pilot.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
if len(rows) != 15:
    print(f"FAIL: expected 15 pilot rows, found {len(rows)}")
    sys.exit(1)

locked = list((ROOT / "00_protocol").glob("*_LOCKED.md"))
if len(locked) < 3:
    print("FAIL: expected at least 3 locked protocol files")
    sys.exit(1)

print("PASS: project structure")
print("PASS: 75 seed records")
print("PASS: 15 pilot papers")
print("PASS: locked protocol artifacts present")
