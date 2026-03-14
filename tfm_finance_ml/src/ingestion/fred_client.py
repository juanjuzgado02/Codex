from __future__ import annotations

import os

import pandas as pd
import requests

from src.core.exceptions import IngestionError
from src.ingestion.base import DataClient


class FredClient(DataClient):
    """Client for FRED time series observations."""

    def __init__(self, api_key: str | None = None, base_url: str | None = None, timeout: int = 30) -> None:
        self.api_key = api_key or os.getenv("FRED_API_KEY")
        self.base_url = base_url or "https://api.stlouisfed.org/fred/series/observations"
        self.timeout = timeout

    def fetch(self, series_id: str, start_date: str, end_date: str | None = None) -> pd.DataFrame:
        if not self.api_key:
            raise IngestionError("FRED_API_KEY is required to call FRED API")

        params = {
            "series_id": series_id,
            "api_key": self.api_key,
            "file_type": "json",
            "observation_start": start_date,
        }
        if end_date:
            params["observation_end"] = end_date

        response = requests.get(self.base_url, params=params, timeout=self.timeout)
        response.raise_for_status()
        payload = response.json()
        observations = payload.get("observations", [])

        df = pd.DataFrame(observations)
        if df.empty:
            return pd.DataFrame(columns=["date", "value", "series_id"])

        df = df[["date", "value"]].copy()
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["value"] = pd.to_numeric(df["value"].replace(".", pd.NA), errors="coerce")
        df["series_id"] = series_id
        return df.dropna(subset=["date"]).reset_index(drop=True)
