from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WalkForwardSplit:
    train_start: int
    train_end: int
    test_start: int
    test_end: int


def build_walk_forward_splits(
    n_samples: int,
    train_window: int,
    test_window: int,
    step: int,
) -> list[WalkForwardSplit]:
    splits: list[WalkForwardSplit] = []
    train_start = 0
    train_end = train_window

    while train_end + test_window <= n_samples:
        test_start = train_end
        test_end = test_start + test_window
        splits.append(
            WalkForwardSplit(
                train_start=train_start,
                train_end=train_end,
                test_start=test_start,
                test_end=test_end,
            )
        )
        train_end += step
    return splits
