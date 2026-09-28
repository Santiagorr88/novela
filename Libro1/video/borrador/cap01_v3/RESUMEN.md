# Piloto v3 — Libro I, Capítulo 1 ("Una Herida en el Mundo")

**BORRADOR — pendiente de aprobación del autor.** Generado 2026-09-20, tras el rediseño de ingeniería motivado por la regresión de v2 (ver `cap01_v2/REVISION_CODEX_V2.md`). Nada de esto se ha commiteado.

## Qué cambió respecto a v2

1. **Texto del capítulo pre-extraído por código** (35 párrafos, numerados `[P1]`…`[P35]`) e incrustado directamente en los prompts — ningún agente "va a leer el archivo" por su cuenta. Esto es lo que corrigió el bug de v2 donde la escena "Solmire" generaba contenido del flashback equivocado.
2. **Continuidad procesada en lotes de 4 planos**, encadenados, con validación de que los IDs devueltos coinciden con los pedidos y un reintento automático si faltan. Esto es lo que corrigió el 92% de bloqueo por pérdida de datos de v2.
3. **Categorías de bloqueo** (`ERROR_ENTREGA`, `CONTRADICCION_NARRATIVA`, `CONTRADICCION_CONTINUIDAD`, `REFERENCIA_PENDIENTE`) y **propagación de dependencias**: un plano de continuación bloqueado bloquea también al que depende de él, en vez de que el traductor lo salte en silencio.
4. **Notas de canon acotadas por escena**: la curación del ala de Miguel solo se narra en la escena del flashback; el resto de escenas solo reciben la nota corta "alas intactas, sin VFX de curación".
5. Incorporadas las 7 lecciones de tus pruebas reales en Flow (restricciones negativas en el prompt, evitar planos de frente a cámara, una sola referencia por defecto, etc.).

## Resultado

| Métrica | v1 | v2 | v3 |
|---|---|---|---|
| Planos totales | 122 | 131 | 123 |
| Bloqueados | — (esquema simplificado, sin bloqueo real) | 121 (92%) | **13 (10,6%)** |
| Bloqueados por pérdida de datos | — | 117 (96,7%) | **0** |
| Bloqueados por problema real detectado | — | 4 | **13** |
| Bug de contenido (escena equivocada) | no aplica | **sí, S6 = flashback** | **no** |

Duración total: 930 s (15,5 min), dentro del rango 8-15 min. 111 de 123 planos ya tienen su prompt de Flow listo para copiar y pegar.

## QA entre escenas (calculado aparte, con solo los planos de frontera, para evitar el error de v2 de "prompt demasiado largo")

- **4 de 5 fronteras coherentes.** La frontera S2→S3 es una discontinuidad física real pero correctamente señalizada como corte de flashback (no es un error). La regla de canon del ala de Miguel se verificó y se cumple: sana y sin marca de quemadura ya en el plano de transición y en el primer plano del presente.
- ✅ **1 incoherencia real — RESUELTA (2026-09-20)**: en la frontera S5→S6, la herida de Miguel aparecía "silenciada por completo" antes de que viera la espada. Corregido: el plano disparador real es `B1C01_S6_P07` (donde el texto dice "en el instante en que la vio... enmudeció"); los 6 planos anteriores de S6 ahora muestran la herida activa, sin silenciar. Esta corrección además **desbloqueó 2 planos** (P07 y P08, que estaban atascados exactamente por esta contradicción) — sus 2 prompts de Flow ya están generados. S6 queda con 0 planos bloqueados.

## Los 13 planos bloqueados restantes (por si quieres revisarlos antes de resolver nada)

- 9 `CONTRADICCION_CONTINUIDAD` — saltos reales detectados por el propio agente (ej. una pose que no se puede reconciliar con el plano anterior sin inventar datos).
- 3 `REFERENCIA_PENDIENTE` — bloqueados porque dependen de uno de los 9 anteriores.
- 1 `CONTRADICCION_NARRATIVA` — choque con el texto/canon.

Repartidos en S2 (4), S3 (4), S4 (4), S5 (1). Detalle en el campo `motivo_bloqueo` de cada plano, dentro de `B1C01_S*.json`.

## Qué falta

- Revisión independiente con Codex (QA doble, regla del proyecto) — no lanzada todavía, a la espera de que confirmes si quieres que la lance ahora.
- Resolver los 13 planos bloqueados restantes (la mayoría son ajustes menores de pose/estado, no decisiones de canon).

## Qué NO se ha hecho

- No se ha generado ningún vídeo real en Flow.
- No se ha commiteado ni hecho push de nada.
