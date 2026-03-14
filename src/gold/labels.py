from __future__ import annotations

import pandas as pd


def add_binary_targets(df: pd.DataFrame, price_col: str, horizons: list[int]) -> pd.DataFrame:
    out = df.copy()
    for h in horizons:
        future_ret = out[price_col].shift(-h) / out[price_col] - 1.0
        out[f"future_return_{h}d"] = future_ret
        out[f"target_up_{h}d"] = (future_ret > 0).astype("Int64")
    return out
