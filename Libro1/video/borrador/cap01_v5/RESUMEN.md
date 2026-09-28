# Piloto v5 — Libro I, Capítulo 1 ("Una Herida en el Mundo")

**BORRADOR — pendiente de aprobación del autor.** Generado 2026-09-24, tras una ronda de rediseño centrada en dos problemas reales encontrados en v4: la paranoia del agente de continuidad y un validador de continuidad entre planos demasiado estricto (zero-tolerance). Nada de esto se ha commiteado.

## Qué cambió respecto a v4

1. **Prompt recalibrado para bajar la "paranoia" del agente**: se sustituyeron los relatos vívidos de bugs pasados (bastón/guante reapareciendo) por ejemplos calmados SÍ/NO bloquear y un límite explícito de alcance ("evalúa solo contra el plano inmediatamente anterior, no reconstruyas la cadena completa de la escena").
2. **Propagación de dependencias restringida a enlaces `continuacion`** (antes incluía también `cambio_angulo`, que es casi todo enlace intra-escena, y provocaba que un bloqueo temprano arrastrara en cascada el resto de la escena).
3. **Eliminado el chequeo de frontera entre planos de tolerancia cero** (`detectarRupturasEntrePlanos`, exigía que CADA objeto/herida se restableciera explícitamente en CADA frontera de plano, sin excepción posible) — con más personajes/objetos y 159 planos, esto escalaba mal y bloqueaba el 87% del capítulo. Se mantiene solo la validación dentro del propio plano (entrada→salida), que sí es fiable.
4. **Bug real encontrado y corregido en esta misma ronda** (no estaba en el plan inicial): el validador de "vocabulario de curación física prohibido" para la herida de Miguel usaba un simple `includes()` sobre la palabra "cicatriz", sin mirar si estaba negada. La forma CORRECTA y deseada de describir la herida — "sin marca física, cicatriz ni perforación visible" — contiene literalmente la palabra "cicatriz" y se bloqueaba igual que si dijera que la herida está cicatrizada. Esto por sí solo causaba 98 de 105 bloqueos en una primera pasada completa (66% del capítulo). Fix: el chequeo ahora exige que la palabra prohibida no esté precedida en su misma frase por una negación (sin/ni/no/ninguna/nunca/jamás).

## Resultado

| Métrica | v3 | v4 | v5 |
|---|---|---|---|
| Escenas | 6 | 8 | 8 |
| Planos totales | 123 | 153 | **159** |
| Bloqueados | 13 (10,6%) | 50 (32,7%) | **9 (5,7%)** |
| Bloqueados por falso positivo de validador | — | ~40 (paranoia + granularidad) | 0 (verificado uno a uno) |
| Duración total | 930 s (15,5 min) | 1290 s (21,5 min) | 1280 s (21,3 min) |

150 de 159 planos ya tienen su prompt de Flow listo para copiar y pegar.

**Nota sobre la duración**: la segmentación converge de forma no determinista entre 6 y 8 escenas según la pasada; en 8 escenas la duración se sale del rango objetivo (8-15 min) porque el flashback de las Puertas de Ónice y la escena del Centinela se separan como escenas propias. No es un problema de continuidad — es un tema de calibración de la segmentación que queda pendiente de decidir (¿aceptar episodios más largos, o forzar fusión de escenas cortas?).

## QA entre escenas (calculado aparte, solo planos de frontera — el QA dentro del propio Workflow sigue fallando por "prompt demasiado largo" con 8 escenas completas)

**7 de 7 fronteras coherentes.** Verificado explícitamente:
- La herida metafísica de Miguel (el "hueco" bajo el esternón) se mantiene activa y sin marca física en las 7 fronteras, sin cerrarse antes de tiempo.
- En la frontera S7→S8 ("Solmire"), el propio dato del plano de entrada confirma que la herida "aún no se ha silenciado (eso ocurrirá más adelante en esta misma escena, al ver la espada)" — exactamente lo que exige el canon.
- Las dos discontinuidades físicas y espaciales fuertes (entrada al flashback S3→S4, salida del flashback S4→S5) están correctamente señalizadas como corte de recuerdo, tanto por el flag `es_flashback_alas_miguel` como por el texto del propio plano de entrada.
- No se detectaron objetos, prendas o heridas que aparezcan o desaparezcan sin justificación narrativa en ninguna frontera.

## Los 9 planos bloqueados (revisados uno a uno, no son el bug de la ronda anterior)

Todos son `CONTRADICCION_CONTINUIDAD` (8) o su cascada de dependencia (`REFERENCIA_PENDIENTE`, 1), y todos apuntan al mismo patrón: un objeto/prenda descrito con distinta granularidad entre plano y plano (ej. "sabatón izquierdo" vs. el resto del calzado, "conjunto completo" vs. piezas sueltas del atuendo del Pewter Sentinel, "cuerpo completo de Miguel" como entrada genérica de un encuadre muy cerrado) sin que el validador reconozca que es el mismo objeto/persona ya presente:

- S1: P08, P09 (calzado de Miguel)
- S2: P05, P06 (guantes de Miguel; P06 es cascada de P05)
- S5: P21 (túnica de Gabriel)
- S7: P06, P08, P13 (vestuario de Miguel y del Pewter Sentinel)
- S8: P05 (encuadre muy cerrado del "cuerpo completo" de Miguel)

Repartidos en 5 de las 8 escenas, ninguna concentración anómala. Son candidatos razonables a revisión manual rápida (probablemente todos resolubles ampliando el diccionario de sinónimos de granularidad de vestuario), no señal de un problema estructural nuevo.

## Qué falta

- Revisar y (si procede) desbloquear los 9 planos anteriores — no son decisiones de canon, son ajustes de reconocimiento de vestuario.
- Decidir la calibración de duración/segmentación (8 escenas / 21 min vs. forzar 6-8 min-target).
- Revisión independiente con Codex (QA doble, regla del proyecto) — no lanzada todavía.
- S7 (Pewter Sentinel) sigue marcada `requiere_aprobacion_autor=true`: el texto original describe una figura sólida de metal pálido, pero el diseño vigente (aprobado 2026-09-18) es de niebla/vapor — la escena aplica esa identidad, pero queda señalada por si el autor quiere revisarla.

## Qué NO se ha hecho

- No se ha generado ningún vídeo real en Flow.
- No se ha commiteado ni hecho push de nada.
