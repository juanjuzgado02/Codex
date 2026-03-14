import pandas as pd

from src.ingestion.fred_client import FredClient


class DummyResponse:
    def raise_for_status(self):
        return None

    def json(self):
        return {
            "observations": [
                {"date": "2020-01-01", "value": "1.23"},
                {"date": "2020-01-02", "value": "."},
            ]
        }


def test_fred_client_fetch(monkeypatch):
    monkeypatch.setenv("FRED_API_KEY", "dummy")

    def fake_get(*args, **kwargs):
        return DummyResponse()

    monkeypatch.setattr("src.ingestion.fred_client.requests.get", fake_get)

    client = FredClient()
    df = client.fetch("DGS10", "2020-01-01")

    assert list(df.columns) == ["date", "value", "series_id"]
    assert df["series_id"].iloc[0] == "DGS10"
    assert pd.isna(df["value"].iloc[1])
