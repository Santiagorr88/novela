# Pasada de variación de muletillas — Libro 1, capítulos 01–26 (EN + ES)

Aprobada por el autor. Refina la voz de calibre B (`content/craft/12_calibre_b.md`), ya cerrada y aceptada — esta pasada no la reescribe ni la revierte, solo varía las palabras y fórmulas que se repiten con tanta frecuencia que el lector las oye.

**Criterio aplicado:**
1. La misma muletilla dos o más veces en el mismo párrafo, o en párrafos adyacentes → variación obligatoria.
2. Reducción global moderada de las fórmulas más señaladas (EN: *something*, *found himself*, *moment*, *whatever*, *the shape of*, *in a way*, *the kind of*, *worth*, *rather than*, *never once / had never*; ES: *modo en que*, *todavía*, *jamás*, *propio/propia*, *a lo largo de*, *ninguno de los dos*, *por primera vez*, *de todos modos*, *valer/merecer la pena*, *una especie de*, *algo parecido a*), sin exterminarlas — quedan donde son la palabra correcta.
3. Técnicas por orden de preferencia: borrar, afirmar directo, sinónimo natural. Nunca tesauro ornamental.
4. Intocable: réplicas de diálogo (comillas EN / rayas ES / cursivas), tags "said"/"dijo", hechos, beats, canon, armas, la imagen ganada de cada escena.

**Un matiz importante detectado en la revisión:** varias repeticiones que a primera vista parecían muletillas eran en realidad paralelismo retórico deliberado (p. ej. "worth keeping, not yet worth acting on"; "caution rather than failure, patience rather than evidence"; los tres "whatever" seguidos en el cierre del cap. 26). Esas se dejaron intactas — el criterio 1 aplica a repetición perezosa, no a anáfora construida a propósito.

## Verificación aplicada a los 26 capítulos

- **Paridad de párrafos EN = ES** confirmada en los 26 capítulos (`grep -c '^$'` idéntico en ambos idiomas, capítulo por capítulo).
- **Diálogo byte-idéntico contra git HEAD**: verificado programáticamente contra el commit previo a esta pasada. Las únicas coincidencias que el script marcó como "distintas" (caps. 08, 13, 23) resultaron ser falsos positivos del heurístico de línea — en los tres casos el texto editado era la acotación narrativa incrustada entre rayas (p. ej. "—dijo Aamon, ya decidiendo cada detalle..."), nunca la réplica hablada en sí. Confirmado por inspección manual línea a línea.
- Ningún hecho, beat, canon ni mención de arma fue alterado; todas las ediciones tocaron exclusivamente narración.

## Resultado cuantitativo (suma de los 26 capítulos, EN y ES por separado)

Extensión: EN 51.710 → 51.664 palabras (-0,09%); ES 56.152 → 56.072 palabras (-0,14%). Esta pasada no es de recorte — es de variación, por eso el conteo de palabras apenas se mueve mientras las repeticiones bajan.

### EN

| Muletilla | Antes | Después | Δ |
|---|---|---|---|
| something | 200 | 166 | -17% |
| moment(s) | 122 | 99 | -19% |
| whatever | 84 | 81 | -4% |
| rather than | 68 | 63 | -7% |
| never once / had never | 57 | 49 | -14% |
| worth | 44 | 42 | -5% |
| the kind of | 33 | 31 | -6% |
| the shape of | 14 | 10 | -29% |
| in a way | 16 | 14 | -13% |
| found himself/found | 15 | 12 | -20% |

### ES

| Muletilla | Antes | Después | Δ |
|---|---|---|---|
| propio/propia | 164 | 163 | -1% |
| todavía | 125 | 123 | -2% |
| jamás | 100 | 97 | -3% |
| modo en que | 72 | 68 | -6% |
| a lo largo de | 42 | 41 | -2% |
| de todos modos | 36 | 35 | -3% |
| ninguno de los dos | 36 | 36 | 0% |
| por primera vez | 24 | 24 | 0% |
| algo parecido a | 3 | 3 | 0% |
| valer/merecer la pena | 1 | 1 | 0% |

La reducción es desigual a propósito: *something* y *the shape of* — las peores del inventario, con la fórmula "something closer to X" citada como ejemplo del problema — bajaron con fuerza porque aparecían dobladas dentro de una misma frase con frecuencia (ver ejemplos). *Whatever*, *ninguno de los dos* y *por primera vez* casi no se tocaron porque, revisadas caso por caso, casi nunca estaban dobladas ni eran sustituibles sin forzar la prosa — *no hacía falta exterminarlas*, y forzar un número parejo habría ido contra el mandato explícito del encargo.

---

## Ejemplos representativos

**1. Doble en la misma frase, capítulo modelo (cap. 1, intocable en su mayoría — solo se tocó lo estrictamente doblado):**
- Antes (EN): *"...as though something in him recognized something in it. He did not like the shape of that thought."*
  Después: *"...as though he recognized something of himself in it. He did not like the thought."*
- Antes (ES): *"...como si algo en él reconociera algo en ella. No le gustó la forma de ese pensamiento."*
  Después: *"...como si reconociera algo de sí mismo en ella. No le gustó el pensamiento."*

**2. Triple en un mismo párrafo (cap. 4, "moment" x3):**
- Antes: *"One moment the air had been full of the ordinary chaos of a skirmish... The next moment, nothing... gusting hard enough to sting a moment before, had gone still..."*
  Después: *"One moment the air had been full of the ordinary chaos... Then, nothing... gusting hard enough to sting a breath before, had gone still..."*
- ES espejo: *"Un momento el aire había estado lleno..."* → *"Entonces, nada"* / *"escocer un aliento antes"*.

**3. La fórmula explícitamente señalada por el encargo ("something closer to"), capítulos 4, 7, 14, 17, 22:**
- Cap. 4 (EN): *"Something closer to standing at the edge of a very tall place..."* → *"More like standing at the edge of a very tall place..."*
- Cap. 22 (EN): *"dread shifted into something closer to resolve"* → *"dread shifted into resolve"*
- Cap. 22 (ES espejo): *"el pavor desplazado hacia algo más cercano a la resolución"* → *"el pavor desplazado hacia la resolución"*

**4. Tres "modo en que" en tres párrafos consecutivos (cap. 8, ES):**
- Antes: *"...del modo en que sus instructores le habían inculcado..."* / *"...del modo en que siempre parecían propagarse..."* (conservado, el del medio) / *"...del modo en que la conmovía cualquier pieza..."*
  Después: *"...tal como sus instructores le habían inculcado..."* / (sin cambio) / *"...como la conmovía cualquier pieza..."*

**5. "Had never" repetido en párrafos adyacentes (cap. 24, EN — voz analítica de Sariel):**
- Antes: *"He had never resolved that unease... his orders that day had never required him to examine it. The rooftop unease had never asked him..."* (triple)
  Después: se dejó el primer y tercer "had never" (marco retórico deliberado del contraste final) y se reescribió el del medio: *"his orders that day gave him no cause to examine it."*

---

## Nota sobre alcance

El tramo cubierto es Libro1, capítulos 01–26, EN y ES. No se tocaron los capítulos 27 en adelante (fuera de este encargo). La verificación de diálogo detectó diferencias en capítulos 29, 31–33, 35, 41, 47, 49–50 — todos fuera de este tramo y no modificados por esta pasada; probablemente residuo de pasadas anteriores de otro agente, no de este trabajo.
