from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from src.core.exceptions import ConfigError
from src.core.paths import project_root, resolve_path


class FlagsConfig(BaseModel):
    enable_options: bool = False
    enable_news: bool = False
    enable_cboe_connector: bool = False


class PathsConfig(BaseModel):
    data_root: str
    bronze: str
    silver: str
    gold: str
    marts: str
    artifacts: str
    logs: str


class SettingsConfig(BaseModel):
    project_name: str = "tfm_finance_ml"
    asset: str = "SPY"
    timezone: str = "America/New_York"
    frequency: str = "daily"
    currency: str = "USD"
    start_date: date | str = "2004-01-01"
    end_date: date | str | None = None
    horizons: list[int] = Field(default_factory=lambda: [21, 63, 126])
    label_price_field: str = "adjusted_close"
    random_seed: int = 42
    flags: FlagsConfig
    paths: PathsConfig


class ProjectConfig(BaseModel):
    settings: SettingsConfig
    sources: dict[str, Any]
    features: dict[str, Any]
    models: dict[str, Any]
    horizons: dict[str, Any]


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ConfigError(f"Missing YAML configuration file: {path}")
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def load_project_config(config_dir: str | Path = "config") -> ProjectConfig:
    load_dotenv(project_root() / ".env")

    config_path = resolve_path(str(config_dir))
    settings = SettingsConfig(**_load_yaml(config_path / "settings.yaml"))

    return ProjectConfig(
        settings=settings,
        sources=_load_yaml(config_path / "sources.yaml"),
        features=_load_yaml(config_path / "features.yaml"),
        models=_load_yaml(config_path / "models.yaml"),
        horizons=_load_yaml(config_path / "horizons.yaml"),
    )
