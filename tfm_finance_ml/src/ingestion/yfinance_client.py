from __future__ import annotations

import pandas as pd
import yfinance as yf

from src.ingestion.base import DataClient


class YFinanceClient(DataClient):
    """Client for downloading OHLCV+actions from yfinance."""

    def fetch(
        self,
        ticker: str,
        start_date: str,
        end_date: str | None = None,
        interval: str = "1d",
        auto_adjust: bool = False,
    ) -> pd.DataFrame:
        df = yf.download(
            tickers=ticker,
            start=start_date,
            end=end_date,
            interval=interval,
            auto_adjust=auto_adjust,
            progress=False,
            actions=True,
        )
        if df.empty:
            return df

        df = df.rename_axis("date").reset_index()
        out = pd.DataFrame(
            {
                "date": pd.to_datetime(df["Date"] if "Date" in df.columns else df["date"]),
                "open": df["Open"],
                "high": df["High"],
                "low": df["Low"],
                "close": df["Close"],
                "adjusted_close": df["Adj Close"] if "Adj Close" in df.columns else df["Close"],
                "volume": df["Volume"],
                "dividends": df["Dividends"] if "Dividends" in df.columns else 0.0,
                "stock_splits": df["Stock Splits"] if "Stock Splits" in df.columns else 0.0,
            }
        )
        return out
