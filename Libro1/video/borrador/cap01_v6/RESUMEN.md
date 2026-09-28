# Piloto v6 — Libro I, Capítulo 1 ("Una Herida en el Mundo")

**BORRADOR — pendiente de aprobación del autor.** Generado 2026-09-25 en dos rondas de corrección dirigida sobre v5, a partir de dos revisiones independientes de Codex (`cap01_v5/REVISION_CODEX_V5.md` y `cap01_v6/REVISION_CODEX_V6.md`). Nada de esto se ha commiteado.

## Ronda 1: los 6 bugs de contenido que Codex encontró en v5

Todos verificados uno a uno contra los datos resultantes tras regenerar S4/S5/S8 con notas de canon reforzadas:

1. **Lateralidad del ala de Miguel en S4**: estaba en la derecha; el canon dice izquierda. Corregido y confirmado en los 18 planos regenerados.
2. **Timing del silenciamiento de la herida en S8**: se silenciaba tarde. Ahora coincide exactamente con el plano donde Miguel fija la mirada en la espada por primera vez (P09).
3. **Bastón de Gabriel sin resolver en S5**: el gesto de la mano vacilante ahora usa la mano izquierda (ya libre); el bastón nunca se suelta.
4. **Lágrima de luz de Gabriel reiniciándose (S5)**: ahora aparece, se mantiene sin disolverse mientras Gabriel sigue presente, y se va con él.
5. **Contacto piel-empuñadura en S8**: hay un plano explícito (P18) donde Miguel se retira el guante antes de tocar la espada con la piel.
6. **Desaparición de la arboleda en S8**: el VFX de disolución arranca en el mismo plano del contacto (P20).

También se parchearon a mano las fronteras de luz S1→S2, S2→S3 y S6→S7 (sol duro vs. cielo cubierto; sombras de troncos vs. la regla "esta arboleda no proyecta sombra").

## Ronda 2: la revisión de Codex sobre esa v6 encontró una regresión real y varios pendientes

Codex NO aprobó la primera v6 y encontró, entre otras cosas, **un bug crítico que yo mismo introduje**: el comodín "conjunto completo" que añadí para resolver falsos positivos de vestuario podía ocultar que un objeto (en su prueba, una espada) apareciera en la mano de un personaje sin causa — exactamente el tipo de fallo que motivó todo este proyecto. Lo confirmó con una prueba de Node reproducible. Corregido de raíz: ahora el código rastrea explícitamente si cada objeto viene de una prenda o de la mano, y el comodín "conjunto completo" solo puede cubrir prenda-contra-prenda, nunca un objeto sostenido.

Además corrigió, con pruebas de Node contra las funciones reales:
- El filtro de rasgos anatómicos seguía sin separar por "/" en casos como "armadura/peto y rostro" (perdía el rastreo del peto).
- "guante izquierdo" seguía coincidiendo con "sabaton izquierdo" porque compartir la palabra "izquierdo" bastaba — ahora las palabras de lado no cuentan como coincidencia por sí solas.

Y encontró contenido pendiente que también se corrigió en esta ronda:
- **S5 P15→P16**: Miguel aparecía ya caminando/alejado justo después de solo pivotar en P15, adelantando la marcha que no debía empezar hasta P25. Corregido: permanece quieto en el mismo punto hasta P25.
- **S2 seguía con sol** en los campos internos de continuidad (`entorno.luz`, `frame_final_previsto`) y en sus 10 prompts de Flow, aunque el campo `luz` de nivel superior ya estaba corregido. Se regeneró la escena completa (luz + prompts) con la atmósfera de S1 aplicada de forma consistente en todas las representaciones.
- **S8**: la etiqueta de guion "Sonido ambiente:" (prohibida por el doc 14) se quitó de los 23 prompts; el zumbido grave de la herida (que el texto sitúa creciendo *antes* del contacto, no naciendo en ese instante) se resecuenció para empezar a crecer desde P15 en vez de aparecer de golpe en P20.
- **S7 P12**: una sombra bajo cejas/nariz contradecía la regla de "sin sombra propia" establecida en S6; corregida.
- **S6→S7 (enlace)**: el primer plano de S6 decía "sin elipsis" pese a que el propio párrafo 28 declara varios días de marcha; corregido el texto del enlace.

## Resultado

| Métrica | v4 | v5 (tras fix "cicatriz") | v6 |
|---|---|---|---|
| Escenas | 8 | 8 | 8 |
| Planos totales | 153 | 159 | **165** |
| Bloqueados | 50 (32,7%) | 9 (5,7%) | **8 (4,8%)** |
| Prompts de Flow listos | — | 150 | **158** |
| Bugs de contenido reales confirmados por Codex | sin auditar | 6 encontrados | **6 corregidos + 1 regresión propia corregida** |

El bloqueo subió ligeramente de la primera a la segunda v6 (6→8) porque el validador corregido detecta con más honestidad huecos de datos que antes quedaban enmascarados por sus propios bugs — es una mejora en la fiabilidad de la señal, no un empeoramiento del guion.

Duración total: 1277 s (~21,3 min) — sigue fuera del rango objetivo 8-15 min; mismo problema de calibración de segmentación ya documentado en versiones anteriores, no es un bug de continuidad.

## Los 8 planos que siguen bloqueados

Todos son el mismo patrón ya identificado por Codex: un personaje u objeto sale de un encuadre muy cerrado y el estado de entrada del plano siguiente no lo marca explícitamente como oculto (`vestuario_oculto`), así que el validador —correctamente, de forma conservadora— no puede confirmar que sigue ahí:

- **S1 P08/P09/P10/P12** (P13 es cascada de P12): el guante izquierdo y luego el derecho de Miguel no se repiten en una secuencia de primerísimos primeros planos sobre el peto.
- **S5 P19** (P20 es cascada): las hombreras de tela de Gabriel no se marcan como ocultas cuando él desaparece de cuadro por completo.
- **S7 P08**: el Pewter Sentinel sale de un plano cerrado sobre Miguel sin que su entrada tenga la misma etiqueta "conjunto completo" que sí lleva su salida.

Son ajustes de datos, no decisiones de canon ni errores narrativos — quedan señalados para revisión manual rápida en vez de forzar otro ciclo de regeneración con más reglas de detección, que es exactamente el tipo de parche que causó la regresión de esta misma ronda.

## Qué falta

- Decidir la calibración de duración/segmentación (21 min vs. objetivo 8-15 min).
- Ningún clip real se ha generado todavía en Flow. Codex recomienda explícitamente este como el siguiente paso útil: probar 2-3 prompts reales (en particular la retirada de guante y el contacto simultáneo con la disolución de S8) antes de seguir puliendo el JSON.
- Posible tercera revisión de Codex si tras probar clips reales aparecen discrepancias entre el plan y el resultado — no lanzada de oficio esta vez para no entrar en un ciclo de correcciones sin fin sobre el papel.

## Qué NO se ha hecho

- No se ha generado ningún vídeo real en Flow.
- No se ha commiteado ni hecho push de nada.
