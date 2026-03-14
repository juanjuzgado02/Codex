# Arquitectura

## Patrón general

Se adopta una arquitectura **Medallion**:
- **Bronze**: datos crudos de fuentes externas, con metadatos de ingesta.
- **Silver**: datos limpios, tipados y alineados temporalmente.
- **Gold**: dataset analítico/ML con etiquetas y features.

## Componentes principales

- `src/core`: configuración, paths, logging, utilidades y excepciones.
- `src/ingestion`: conectores desacoplados por fuente.
- `src/bronze`: pipelines de ingesta y persistencia en Parquet.
- `src/cli`: comandos para ejecutar etapas del pipeline.

## Reproducibilidad

- Configuración centralizada en YAML.
- Secrets/API keys en `.env`.
- Parámetros y rutas desacoplados del código.
- Escritura determinista de rutas por `source/asset/series`.
