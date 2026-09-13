# utils_audit.py – helper utilities for audit generation
"""Utility functions used by the audit scripts.

This module provides simple helpers to:
- load CSV files (pandas optional)
- compute counts for PRISMA, Graph‑KT, SSL, sparse‑cold‑start
- write audit markdown templates

The functions are intentionally lightweight; they can be called from the
individual task scripts (F2‑F9) to avoid duplication.
"""

import csv
from pathlib import Path
from typing import List, Dict, Any

def read_csv(path: str) -> List[Dict[str, Any]]:
    """Read a CSV file into a list of dict rows.
    """
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def write_csv(path: str, fieldnames: List[str], rows: List[Dict[str, Any]]):
    """Write rows to a CSV file.
    """
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def write_audit_md(path: str, title: str, status: str, details: str = ""):
    """Create a minimal audit markdown file.
    """
    content = f"# {title}\n\n**Status:** {status}\n\n{details}\n"
    Path(path).write_text(content, encoding='utf-8')
