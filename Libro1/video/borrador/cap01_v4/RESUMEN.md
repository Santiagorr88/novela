# Piloto v4 — Libro I, Capítulo 1 ("Una Herida en el Mundo")

**BORRADOR — pendiente de aprobación del autor.** Generado 2026-09-22, tras la ronda de rediseño que atacó el patrón "objeto sin resolver → reaparece sin justificación" y el bug del reintento. Nada de esto se ha commiteado.

## Confirmado: los fixes de esta ronda funcionan

- **0 planos bloqueados por pérdida de datos** (`ERROR_ENTREGA`), igual que v3 — el bug del reintento no volvió a manifestarse.
- El patrón "bastón/guante que reaparece sin acción" **no se reprodujo** en las escenas donde se detectó originalmente (verificado plano a plano: el bastón de Gabriel se mantiene en su mano hasta que sale de escena con él, sin huecos).

## Nuevo hallazgo: un falso positivo distinto, mismo origen

El validador automático que añadí esta ronda (detecta objetos que "reaparecen" sin justificación) confunde **prendas que se pueden quitar** con **rasgos anatómicos permanentes** que a veces el agente clasifica como "vestuario" por error: los ojos y los zarcillos de peltre fundidos en los hombros del Pewter Sentinel (parte de su diseño, siempre presentes), y la grieta del peto de Miguel descrita con distinta granularidad entre plano y plano. Esto concentra casi todo el bloqueo de esta pasada en la escena del Centinela (12/14 planos) y en el arranque de Miguel (8/15).

## Datos de esta pasada

- **La segmentación salió distinta esta vez**: 8 escenas en vez de 6 (no determinista — el modelo dividió más fino, separando el flashback en dos escenas y creando una escena aparte para el Centinela). Esto disparó la duración a **1290 s (21,5 min)** — por encima del rango 8-15 min que buscamos. No es un problema de continuidad, es un problema de la escala de la segmentación esta vez.
- 153 planos totales, 50 bloqueados (32,7%): 35 `REFERENCIA_PENDIENTE` (cascada desde los falsos positivos), 10 `CONTRADICCION_CONTINUIDAD`, 5 `CONTRADICCION_NARRATIVA`.
- QA de fronteras (7, por las 8 escenas): 2 plenamente verificables y coherentes; 5 parcialmente verificables (dependen de planos bloqueados en el lado de salida) sin incoherencia detectada dentro de lo disponible. Se encontró **una incoherencia real nueva**: los sabatones de Miguel pasan de "agrietados" al cierre de la escena 1 a "sin daño" al abrir la escena 2, sin ninguna elipsis que lo explique.
- La regla de canon del ala/herida de Miguel se cumple en las 7 fronteras.

## Qué falta

- Decidir si se afina el validador (excluir rasgos anatómicos permanentes de la comprobación de "vestuario") antes de otra pasada, o si se revisa a mano esta vez.
- La incoherencia de los sabatones (S1→S2) queda sin resolver.
- Revisión independiente con Codex — no lanzada todavía.
- La segmentación en 8 escenas / 21,5 min necesita decidirse: ¿se acepta como episodio más largo, o se ajusta el pipeline para converger siempre a la duración objetivo?
