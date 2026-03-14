# Diccionario de datos (Fase 2)

## Bronze market

Campos:
- `date` (datetime64[ns])
- `open` (float)
- `high` (float)
- `low` (float)
- `close` (float)
- `adjusted_close` (float)
- `volume` (float)
- `dividends` (float)
- `stock_splits` (float)
- `ticker` (str)
- `source` (str)
- `ingestion_timestamp` (datetime64[ns, UTC])

## Bronze macro

Campos:
- `date` (datetime64[ns])
- `value` (float, nullable)
- `series_id` (str)
- `source` (str)
- `ingestion_timestamp` (datetime64[ns, UTC])
