#!/usr/bin/env python3
"""Equal-width ECE + Brier from dumped DyGKT test probabilities (REPRODUCED)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def expected_calibration_error(
    y_true: np.ndarray, y_prob: np.ndarray, n_bins: int = 10
) -> tuple[float, list[dict]]:
    """Equal-width ECE over ((m-1)/M, m/M], matching the manuscript definition."""
    y_true = np.asarray(y_true, dtype=np.float64).ravel()
    y_prob = np.asarray(y_prob, dtype=np.float64).ravel()
    if y_true.shape != y_prob.shape:
        raise ValueError(f"shape mismatch: y_true {y_true.shape} vs y_prob {y_prob.shape}")
    if not (0.0 <= y_prob.min() and y_prob.max() <= 1.0 + 1e-8):
        raise ValueError("y_prob must be in [0, 1]")

    n = len(y_true)
    if n == 0:
        raise ValueError("empty arrays")

    bin_edges = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0
    rows: list[dict] = []
    for m in range(n_bins):
        lo, hi = bin_edges[m], bin_edges[m + 1]
        if m == 0:
            mask = (y_prob >= lo) & (y_prob <= hi)
        else:
            mask = (y_prob > lo) & (y_prob <= hi)
        count = int(mask.sum())
        if count == 0:
            rows.append(
                {
                    "bin": m + 1,
                    "lo": float(lo),
                    "hi": float(hi),
                    "n": 0,
                    "acc": None,
                    "conf": None,
                    "abs_gap": None,
                }
            )
            continue
        acc = float(y_true[mask].mean())
        conf = float(y_prob[mask].mean())
        gap = abs(acc - conf)
        ece += (count / n) * gap
        rows.append(
            {
                "bin": m + 1,
                "lo": float(lo),
                "hi": float(hi),
                "n": count,
                "acc": acc,
                "conf": conf,
                "abs_gap": gap,
            }
        )
    return float(ece), rows


def brier_score(y_true: np.ndarray, y_prob: np.ndarray) -> float:
    y_true = np.asarray(y_true, dtype=np.float64).ravel()
    y_prob = np.asarray(y_prob, dtype=np.float64).ravel()
    return float(np.mean((y_prob - y_true) ** 2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--probs-file",
        type=Path,
        default=Path(__file__).resolve().parent / "results" / "dygkt_assist17_test_probs.npz",
        help="NPZ with y_true, y_prob arrays",
    )
    parser.add_argument("--n-bins", type=int, default=10)
    parser.add_argument(
        "--out-json",
        type=Path,
        default=Path(__file__).resolve().parent / "results" / "dygkt_assist17_ece.json",
    )
    args = parser.parse_args()

    data = np.load(args.probs_file, allow_pickle=True)
    y_true = data["y_true"]
    y_prob = data["y_prob"]
    ece, bins = expected_calibration_error(y_true, y_prob, n_bins=args.n_bins)
    brier = brier_score(y_true, y_prob)

    payload = {
        "evidence_source_type": "REPRODUCED",
        "paper_id": "KT038",
        "model": "DyGKT",
        "dataset": "assist17",
        "split": str(data["split"]) if "split" in data.files else "test",
        "n": int(len(y_true)),
        "n_bins": args.n_bins,
        "ece_equal_width": ece,
        "brier": brier,
        "positive_rate": float(np.mean(y_true)),
        "mean_confidence": float(np.mean(y_prob)),
        "bins": bins,
        "probs_file": str(args.probs_file.resolve()),
        "note": (
            "Survey-computed ECE on author DyGKT code. "
            "Does not change the locked corpus claim that 0/37 manuscripts report ECE."
        ),
    }

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps({k: payload[k] for k in ("ece_equal_width", "brier", "n", "n_bins")}, indent=2))
    print(f"wrote {args.out_json}")


if __name__ == "__main__":
    main()
