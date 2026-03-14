from src.core.config import load_project_config


def test_pipeline_smoke_config_and_paths() -> None:
    cfg = load_project_config()
    assert cfg.settings.paths.bronze.endswith("bronze")
