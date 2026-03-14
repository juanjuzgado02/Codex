from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def resolve_path(value: str) -> Path:
    p = Path(value)
    return p if p.is_absolute() else project_root() / p
