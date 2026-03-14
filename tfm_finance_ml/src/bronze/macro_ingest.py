from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.core.config import ProjectConfig
from src.core.logger import setup_logger
from src.core.paths import resolve_path
from src.ingestion.fred_client import FredClient


def ingest_macro_bronze(config: ProjectConfig) -> list[Path]:
    settings = config.settings
    logger = setup_logger(resolve_path(settings.paths.logs))

    fred_cfg = config.sources.get("fred", {})
    series_list = fred_cfg.get("series", [])
    client = FredClient(base_url=fred_cfg.get("base_url"))

    outputs: list[Path] = []
    for series_id in series_list:
        df = client.fetch(series_id=series_id, start_date=settings.start_date, end_date=settings.end_date)
        if df.empty:
            logger.warning("No macro data returned for series=%s", series_id)
            continue

        df["source"] = "fred"
        df["ingestion_timestamp"] = pd.Timestamp.utcnow()

        out_dir = resolve_path(settings.paths.bronze) / "macro" / "source=fred" / f"series_id={series_id}"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "part-000.parquet"
        df.to_parquet(out_file, index=False)
        outputs.append(out_file)
        logger.info("Saved macro bronze series=%s rows=%s path=%s", series_id, len(df), out_file)

    return outputs
