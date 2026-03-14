from src.core.config import load_project_config


def test_load_project_config() -> None:
    cfg = load_project_config()
    assert cfg.settings.asset == "SPY"
    assert 21 in cfg.settings.horizons
    assert "fred" in cfg.sources
