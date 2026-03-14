import pandas as pd

from src.gold.labels import add_binary_targets


def test_feature_shape_preserves_rows() -> None:
    df = pd.DataFrame({"adjusted_close": [100, 101, 102, 103, 104]})
    out = add_binary_targets(df, price_col="adjusted_close", horizons=[1])
    assert len(out) == len(df)
