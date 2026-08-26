# Pasada de variación de muletillas — Libro 2, capítulos 28–53 (EN + ES)

Relanzamiento de una pasada cuyo agente anterior murió a mitad de trabajo. Refina la voz de calibre B (`content/craft/12_calibre_b.md`), ya cerrada y aprobada — esta pasada no la reescribe ni la revierte, solo varía las palabras y fórmulas que se repiten con tanta frecuencia que el lector las oye.

**Criterio aplicado:**
1. La misma muletilla dos o más veces en el mismo párrafo, o en párrafos/bloques adyacentes (sin `---` de por medio) → variación obligatoria.
2. Reducción global moderada de las fórmulas más señaladas (EN: *something*, *found himself/found*, *moment*, *whatever*, *the shape of*, *in a way*, *the kind of*, *worth*, *rather than*, *never once*; ES: *del modo en que*, *todavía*, *jamás* — alternado con *nunca* —, *propio/propia*, *a lo largo de* temporal, *ninguno de los dos*, *por primera vez*, *de todos modos*, *valer/merecer la pena*, *una especie de*, *algo parecido a*, y el calco *algo más cercano a*), sin exterminarlas — quedan donde son la palabra correcta o hacen trabajo temático.
3. Técnicas por orden de preferencia: borrar, afirmación directa sin andamiaje (*found himself wondering* → *wondered*), sinónimo natural. Nunca tesauro ornamental.
4. Intocable: réplicas de diálogo (comillas EN / rayas ES / cursivas), tags "said"/"dijo", hechos, beats, canon, armas, la imagen ganada de cada escena. Específicamente en este tramo: la línea del ejecutor cap. 40 («the two signatures» / «las dos firmas»), la mención exacta de *Lamentum* en cap. 47, la luz-lenguaje de Selaphiel y la profecía de la antífona en cap. 49, y el mensaje en cursiva («someone will remember this» / «alguien recordará esto») del cap. 50.

## Qué se heredó ya hecho

El agente anterior murió más adelante de lo que la consigna original suponía. Diagnóstico real (vs. la hipótesis de arranque):

- **EN 28–43**: ya editado. El cap. 43 estaba solo parcialmente hecho (3 ediciones puntuales, reducción de apenas 33→30) — se completó en esta pasada antes de tocar nada más.
- **ES 28–42**: ya editado y **completo**, incluido el cap. 42 (la consigna original suponía que el espejo de ES 42 estaba a medias; la revisión mostró que en realidad se había terminado antes de la muerte del agente).
- **ES 43 en adelante**: sin tocar. **EN 44 en adelante**: sin tocar.

Se revisó la coherencia de lo heredado (28–42 en ambos idiomas): paridad de separadores `---` capítulo por capítulo, y una revisión dirigida de las líneas de diálogo tocadas por el predecesor confirmó que todas las ediciones cayeron en acotación narrativa entre rayas, nunca en la réplica hablada. No se encontraron capítulos a medias ni espejos rotos en el tramo heredado.

## Trabajo de esta pasada

Terminado el cap. 43 (EN+ES) y hechos desde cero, EN primero y ES espejo detrás: **44, 45, 46, 47, 48, 49, 50, 51, 52, 53** — 10 capítulos completos en ambos idiomas, más el cierre del 43.

Nota de registro: el cap. 51 (corte infernal, Vual/Agares/Nymos) es deliberadamente evasivo por caracterización — el capítulo empieza estableciendo que Agares comunica "as information offered sideways, never handed over directly". La mayoría de sus *something/shape/worth* viven dentro de diálogo protegido; se dejaron casi todos intactos a propósito, y el recorte real (42→40 EN) es menor que en el resto del tramo por esa razón, no por descuido.

## Verificación aplicada a los 26 capítulos completos (28–53)

- **Paridad de separadores `---` EN = ES**: confirmada capítulo por capítulo en los 26 capítulos, heredados y nuevos.
- **Diálogo byte-idéntico contra git HEAD (EN)**: verificado programáticamente extrayendo todo el texto entre comillas dobles de los 26 capítulos y comparando contra el commit previo a esta pasada — cero diferencias.
- **Cursivas byte-idénticas contra git HEAD (EN + ES)**: verificado programáticamente extrayendo todo el texto entre asteriscos — cero diferencias. Cubre la profecía de la antífona (cap. 49), la luz-lenguaje de Selaphiel (cap. 49), el mensaje "someone will remember this"/"alguien recordará esto" (cap. 50) y el documento falsificado de Agares (cap. 52).
- **Diálogo ES (rayas)**: verificado por inspección dirigida — todas las líneas de diff que empiezan con raya se revisaron una por una; en cada caso el texto cambiado cae en la acotación narrativa incrustada entre rayas (p. ej. "—dijo, su voz llevando..."), nunca en la réplica en sí.
- Líneas canon verificadas exactas contra HEAD: «the two signatures» / «las dos firmas» (cap. 40, sin tocar), *Lamentum* (cap. 47, mención preservada).
- Ningún hecho, beat, canon ni mención de arma fue alterado; todas las ediciones tocaron exclusivamente narración.

## Resultado cuantitativo (suma de los 26 capítulos, EN y ES por separado)

Extensión: EN 53.413 → 53.140 palabras (-0,51%); ES 57.987 → 57.626 palabras (-0,62%). Pasada de variación, no de recorte — el conteo de palabras se mueve poco mientras las repeticiones bajan con fuerza.

### EN

| Muletilla | Antes | Después | Δ |
|---|---|---|---|
| something | 207 | 168 | -19% |
| found himself/found | 136 | 73 | -46% |
| moment | 119 | 113 | -5% |
| whatever | 139 | 126 | -9% |
| the shape of | 24 | 11 | -54% |
| the kind of | 10 | 2 | -80% |
| worth | 50 | 46 | -8% |
| rather than | 77 | 72 | -6% |
| never once | 24 | 12 | -50% |
| **Total** | **786** | **623** | **-21%** |

### ES

| Muletilla | Antes | Después | Δ |
|---|---|---|---|
| del modo en que | 68 | 54 | -21% |
| todavía | 188 | 163 | -13% |
| jamás | 125 | 93 | -26% |
| propio/propia | 222 | 204 | -8% |
| a lo largo de | 73 | 67 | -8% |
| ninguno de los dos | 47 | 47 | 0% |
| por primera vez | 31 | 30 | -3% |
| de todos modos | 32 | 21 | -34% |
| valer/merecer la pena | 24 | 19 | -21% |
| una especie de | 3 | 2 | -33% |
| algo parecido a | 1 | 1 | 0% |
| algo más cercano a | 8 | 2 | -75% |
| **Total** | **822** | **703** | **-14%** |

La reducción es desigual a propósito. *found himself/found*, *never once*, *the shape of* y *the kind of* bajaron con fuerza: son las fórmulas que peor envejecen releídas y las que más aparecían dobladas en la misma frase o párrafo adyacente. *Moment*, *whatever*, *worth* y *rather than* casi no se tocaron porque, revisadas caso por caso, la mayoría vive dentro de diálogo protegido (especialmente en los capítulos de corte infernal, 46, 51 y 52) o hace trabajo de contraste real que no convenía forzar. En ES, *ninguno de los dos* y *algo parecido a* quedaron sin variación neta a propósito: en cada aparición eran única en su párrafo y sustituirlas habría forzado la prosa sin necesidad.

---

## Ejemplos representativos

**1. El calco explícitamente señalado por el encargo, "algo más cercano a" (cap. 43, ES, réplica intocable de por medio):**
- Antes: *"su voz había adoptado un registro por completo distinto, algo más cercano a un verso medio recordado que al habla ordinaria."*
- Después: *"su voz había adoptado un registro por completo distinto, más cercano a un verso medio recordado que al habla ordinaria."*
- Mismo calco cazado tres veces más en cap. 48 (*"algo más cercano a la simple curiosidad"* → *"una sensación más cercana a..."*; *"algo más cercano a una segunda oportunidad"* → eliminado del todo con la reestructura de la frase).

**2. "found himself/found" doblado en un mismo párrafo (cap. 44, EN, Arin y el intermediario):**
- Antes: *"a note in his voice Arin had never once heard from him... the kind of ordinary noise that told him the man was standing in his own kitchen..."*
- Después: *"a note in his voice Arin had never heard from him... ordinary noise that told him the man was standing in his own kitchen..."*
- ES espejo: *"una nota en su voz que Arin jamás le había oído... el tipo de ruido ordinario..."* → *"...nunca lo había imaginado... ruido ordinario..."* (variación jamás/nunca + "el tipo de" eliminado).

**3. "jamás" sobreusado dentro de un mismo capítulo — no solo dentro de un párrafo (cap. 46 y 47, ES):**
El cap. 47 tenía 14 apariciones de *jamás* y cero de *nunca* antes de esta pasada; el cap. 46, 11 y cero. Se alternó sistemáticamente sin tocar ninguna que estuviera dentro de réplica:
- Cap. 47, antes: *"Jamás se había sentido como esto... un casero que jamás hacía preguntas... Ninguna de esas versiones había sido jamás la totalidad de él."*
- Cap. 47, después: *"Jamás se había sentido como esto... un casero que nunca hacía preguntas... Ninguna de esas versiones había sido nunca la totalidad de él."*

**4. "the shape of" quitado donde no aportaba (cap. 48 y 53, EN):**
- Cap. 48: *"he found he could name the shape of it without flinching: not a sentence being served, but something closer to a second chance..."* → *"he could name it without flinching: not a sentence being served, but a second chance..."* (tres muletillas en una sola frase, resuelto de una vez).
- Cap. 53: *"He let himself feel the shape of what was coming the way he felt most things"* → *"He let himself feel what was coming the way he felt most things."*

**5. "never once" innecesario en narración (cap. 49 y 50, EN — se dejó intacto cada "never once" dentro de réplica):**
- Cap. 49: *"Selaphiel went still in a way her attendants had never once seen her go still..."* → *"Selaphiel went stiller than her attendants had ever seen her go..."* (resuelve a la vez "in a way" + "never once").
- Cap. 50: *"the tome that had never once, in all his long keeping of it, needed to be told what it was for"* → *"...had never, in all his long keeping of it, needed to be told..."*

**6. Réplicas y cursivas protegidas verificadas — ejemplo de acotación narrativa editable junto a réplica intocable (cap. 50, EN):**
- El mensaje *"someone will remember this."* / *"alguien recordará esto."* aparece dos veces (caps. 50, líneas 67 y 83) y quedó byte-idéntico en ambos idiomas en ambas apariciones — verificado por script, no solo por inspección.

---

## Nota sobre alcance

El tramo cubierto es Libro2, capítulos 28–53, EN y ES. No se tocaron los capítulos 01–27 de Libro2 (trabajo terminado de otros agentes) ni nada de Libro1 o Libro3. Los 26 capítulos del tramo quedan completos y verificados en ambos idiomas — no queda ningún espejo a medias.
