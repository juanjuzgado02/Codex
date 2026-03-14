class TFMFinanceMLError(Exception):
    """Base exception for project errors."""


class ConfigError(TFMFinanceMLError):
    """Raised when configuration is invalid or missing."""


class IngestionError(TFMFinanceMLError):
    """Raised when ingestion fails."""
