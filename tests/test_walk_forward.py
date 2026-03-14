from src.modeling.walk_forward import build_walk_forward_splits


def test_walk_forward_splits_are_temporal_and_non_random() -> None:
    splits = build_walk_forward_splits(n_samples=100, train_window=50, test_window=10, step=10)
    assert len(splits) == 5
    assert splits[0].train_start == 0
    assert splits[0].train_end == 50
    assert splits[0].test_start == 50
    assert splits[0].test_end == 60
