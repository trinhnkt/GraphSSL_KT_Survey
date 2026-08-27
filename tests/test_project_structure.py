from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

def test_locked_protocol_exists():
    assert (ROOT/"00_protocol/SCOPE_v1.0_LOCKED.md").exists()
    assert (ROOT/"00_protocol/RQs_v1.0_LOCKED.md").exists()
    assert (ROOT/"00_protocol/SLR_PROTOCOL_v1.0_LOCKED.md").exists()

def test_seed_count():
    with (ROOT/"01_seed_corpus/included_papers_seed_audited_v1.0.csv").open(
        encoding="utf-8-sig", newline=""
    ) as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 75

def test_pilot_count():
    with (ROOT/"02_pilot_coding/pilot_papers_15_v1.0.csv").open(
        encoding="utf-8-sig", newline=""
    ) as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 15
