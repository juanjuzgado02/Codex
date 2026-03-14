from __future__ import annotations

import typer

from src.bronze.macro_ingest import ingest_macro_bronze
from src.bronze.market_ingest import ingest_market_bronze
from src.core.config import load_project_config

app = typer.Typer(help="CLI for bronze ingestion pipelines")


@app.command("market")
def market() -> None:
    cfg = load_project_config()
    ingest_market_bronze(cfg)


@app.command("macro")
def macro() -> None:
    cfg = load_project_config()
    ingest_macro_bronze(cfg)


@app.command("all")
def run_all() -> None:
    cfg = load_project_config()
    ingest_market_bronze(cfg)
    ingest_macro_bronze(cfg)


if __name__ == "__main__":
    app()
