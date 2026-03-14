from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.core.config import ProjectConfig
from src.core.logger import setup_logger
from src.core.paths import resolve_path
from src.ingestion.yfinance_client import YFinanceClient


def ingest_market_bronze(config: ProjectConfig) -> Path:
    settings = config.settings
    logger = setup_logger(resolve_path(settings.paths.logs))
    source_cfg = config.sources.get("yfinance", {})

    ticker = settings.asset
    client = YFinanceClient()
    df = client.fetch(
        ticker=ticker,
        start_date=settings.start_date,
        end_date=settings.end_date,
        interval=source_cfg.get("interval", "1d"),
        auto_adjust=source_cfg.get("auto_adjust", False),
    )

    if df.empty:
        logger.warning("No market data returned for %s", ticker)
        return resolve_path(settings.paths.bronze) / "market"

    df["ticker"] = ticker
    df["source"] = "yfinance"
    df["ingestion_timestamp"] = pd.Timestamp.utcnow()

    out_dir = resolve_path(settings.paths.bronze) / "market" / "source=yfinance" / f"asset={ticker}"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "part-000.parquet"
    df.to_parquet(out_file, index=False)

    logger.info("Saved market bronze rows=%s path=%s", len(df), out_file)
    return out_file
