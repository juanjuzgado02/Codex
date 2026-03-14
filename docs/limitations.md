# Limitaciones iniciales

- `yfinance` puede presentar revisiones históricas o incidencias puntuales de disponibilidad.
- Algunas series FRED tienen distinta frecuencia y pueden contener valores faltantes (`.`).
- En esta fase no se integra todavía CBOE/OCC ni noticias en el core.
- Sin pipeline silver/gold todavía, no se aplican reglas completas anti-leakage más allá de la ingesta.
