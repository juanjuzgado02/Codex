# TFM Finance ML

Proyecto Python modular para un TFM de predicción probabilística en mercados financieros, con arquitectura Medallion (`bronze/silver/gold`), almacenamiento local en Parquet y validación temporal walk-forward.

## Estado actual

✅ **Fase 1 y Fase 2 implementadas**:
- Scaffolding profesional del repositorio.
- Configuración centralizada (`YAML` + `.env`).
- Sistema base de logging, paths y carga de configuración.
- Clientes de ingesta para `yfinance` y `FRED`.
- Pipelines bronze para `market` y `macro` con salida en Parquet particionada.
- CLI inicial para lanzar ingestas.
- Tests mínimos iniciales.

## Estructura

```text
tfm_finance_ml/
├── config/
├── data/
├── docs/
├── notebooks/
├── src/
└── tests/
```

## Instalación

```bash
cd tfm_finance_ml
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuración

1. Crear variables de entorno:
```bash
cp .env.example .env
```
2. Completar `FRED_API_KEY` en `.env`.
3. Ajustar parámetros en `config/settings.yaml` y `config/sources.yaml`.

## Ejecución (Fase 2)

### Ingesta de mercado (SPY)
```bash
python -m src.cli.ingest market
```

### Ingesta macro (FRED)
```bash
python -m src.cli.ingest macro
```

### Ingesta completa bronze
```bash
python -m src.cli.ingest all
```

## Salidas esperadas

- `data/bronze/market/source=yfinance/asset=SPY/part-*.parquet`
- `data/bronze/macro/source=fred/series_id=<SERIE>/part-*.parquet`

## Tests

```bash
pytest -q
```

## Próximas fases

- Fase 3: Silver (limpieza, normalización, quality checks).
- Fase 4: Gold (labels + features).
- Fase 7+: modelado, calibración, explainability y reporting.
