import pandas as pd

from src.gold.labels import add_binary_targets


def test_add_binary_targets_creates_expected_columns() -> None:
    df = pd.DataFrame({"adjusted_close": [100, 101, 102, 98, 99]})
    out = add_binary_targets(df, price_col="adjusted_close", horizons=[1, 2])

    assert "future_return_1d" in out.columns
    assert "target_up_2d" in out.columns
    assert out["target_up_1d"].iloc[0] == 1
