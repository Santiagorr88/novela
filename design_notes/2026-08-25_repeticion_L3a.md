# Pasada de variación de muletillas — Libro 3, capítulos 01–26 (EN + ES)

Aprobada por el autor. Refina, no renueva, la voz ya fijada en `content/craft/12_calibre_b.md` (Calibre B). Este tramo ya había pasado por la pasada de estilo previa (`2026-08-25_estilo_L3a.md` a `L3e.md`); esta pasada ataca un problema distinto y más mecánico: la repetición léxica y sintáctica medida a nivel de trilogía (`something`, `found himself/found`, `moment`, `the way he/a` + `in a way`, `worth`, `rather than`, `never once` en EN; `del modo en que`, `todavía`, `jamás`, `propio/propia`, `ninguno de los dos`, `de todos modos`, `valer/merecer la pena` en ES).

**Técnica, por orden de preferencia**: (1) borrar la muletilla cuando no aporta; (2) afirmación directa sin andamiaje ("found he could X" → "could X"); (3) sinónimo natural solo cuando fluye sin sonar a tesauro ("the way X" → "as X", "del modo en que" → "como"). Prioridad (a): misma muletilla dos o más veces en un párrafo o en párrafos adyacentes = corrección obligatoria. Prioridad (b): reducción global del libro.

**Intocable, verificado**: réplicas de diálogo (comillas en EN, rayas en ES, habla en cursiva), tags "said"/"dijo", y el canon del tramo — memoria de Mikel parcial hasta c07 (sin tocar), "Azael" solo desde c10, la revelación de Thamorak en c17 (línea de Azael «It has a name... Thamorak... But it is not an "it." It is a "we."» y «It is our child... And it has come home to devour its parents.» byte-idénticas), el duelo c19–20 («Te tolera» / "It endures you" byte-idéntica), el discurso de Lucifer en c25 («Lo que viene no es tiranía... Es el Vacío. Un "No" final, silencioso, universal... Y yo, que soy el "Sí" eterno del yo, no lo permitiré.» palabra por palabra), y todos los nombres de armas y beats de acción existentes. No se añadió ninguna metáfora nueva.

## Verificación

- **Paridad de líneas EN=ES y contra git HEAD**: recuento automatizado de líneas en los 26 capítulos — coincidencia exacta en los 26 (ninguna línea añadida ni eliminada; solo texto dentro de líneas existentes).
- **Diálogo intacto**: verificado por diff línea a línea contra git HEAD en los 26 capítulos. Todo cambio detectado cae fuera de comillas/rayas — en los casos donde la acotación narrativa comparte línea física con la réplica (p. ej. `"Take your time," the officer said... Lyra appreciated the patience but couldn't use it.`), la réplica entre comillas/rayas permanece byte-idéntica; solo la acotación circundante cambió.
- **Pasajes sagrados** (revelación de Azael c17, «Te tolera»/"It endures you" c19, discurso de Lucifer c25): confirmados palabra por palabra sin cambios mediante grep dirigido sobre el diff de cada capítulo.

## Conteos antes → después (tramo completo, cap. 01–26)

| Muletilla (EN) | Antes | Después | Δ |
|---|---|---|---|
| `found himself` | 32 | 2 | **-93,8%** |
| `found` (uso simple) | 171 | 91 | **-46,8%** |
| `the way` (simil "the way X...") | 117 | 88 | -24,8% |
| `del modo en que` — ver ES | | | |
| `never once` | 28 | 19 | -32,1% |
| `in a way` | 18 | 14 | -22,2% |
| `the shape of` | 27 | 24 | -11,1% |
| `the kind of` | 17 | 16 | -5,9% |
| `rather than` | 82 | 80 | -2,4% |
| `something` | 241 | 235 | -2,5% |
| `moment` | 150 | 148 | -1,3% |
| `whatever` | 134 | 134 | 0% |
| `worth` | 39 | 39 | 0% |

| Muletilla (ES) | Antes | Después | Δ |
|---|---|---|---|
| `descubrió` / `se descubrió` (calco de "found himself/found") | 93 | 21 | **-77,4%** |
| `del modo en que` (incl. "del mismo modo en que") | 102 | 72 | **-29,4%** |
| `propio/propia` | 237 | 232 | -2,1% |
| `todavía` | 164 | 160 | -2,4% |
| `ninguno de los dos` | 42 | 41 | -2,4% |
| `jamás` | 131 | 132 | +0,8% (sin tocar; ya alternaba con "nunca" en el original) |
| `a lo largo de` | 67 | 67 | 0% |
| `por primera vez` | 35 | 35 | 0% |
| `de todos modos` | 30 | 30 | 0% |
| `valer/merecer la pena` | 3 | 3 | 0% (frases recortadas alrededor, conteo intacto) |
| `una especie de` / `algo parecido a` | 0 / 1 | 0 / 1 | 0% |

**Palabras totales**: EN 54.754 → 54.554 (-0,37%); ES 59.969 → 59.730 (-0,40%). Reducción modesta y esperada: esta pasada reescribe construcciones (`found he couldn't` → `couldn't`), no poda párrafos — el objetivo es que la muletilla no se *oiga*, no bajar el conteo por sí mismo.

## Lectura del resultado

El hallazgo más claro del tramo: **`found himself` / `found` en EN y su calco `descubrió` / `se descubrió` en ES eran, con diferencia, la muletilla más audible del libro** — casi todos los capítulos de interioridad (02, 03, 05, 08, 12, 13, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26) repetían el patrón "personaje + found/descubrió + que + cláusula" varias veces por página, a menudo dos veces en el mismo párrafo. Es la construcción que este tramo recorta con más fuerza: -94% / -77%.

El segundo patrón, `the way X` / `del modo en que X`, resultó ser casi un tic de estructura de frase para las voces de Azael (c10, introducción del personaje: 16 instancias de "the way" en un solo capítulo) y de Thaeriel en Malignus/la Puerta del Infierno (c03, c09, c13: 12–13 instancias por capítulo). En esos tres capítulos se aplicó la poda más agresiva del tramo porque casi todos los párrafos —adyacentes entre sí— repetían la construcción; en el resto de capítulos, con densidad más baja, se dejaron las instancias únicas que servían de imagen fuerte (p. ej. "the way a man wades against a current", c03) y solo se varió o cortó la segunda repetición cuando aparecía en el mismo párrafo o en el inmediato siguiente.

`something`, `moment`, `whatever` y `worth` resultaron mucho más disciplinados de lo que sugería el inventario a nivel de trilogía: en este tramo específico casi todas sus apariciones son necesarias (climas de suspenso deliberado, p. ej. "something was still walking closer" cerrando el c03) o aparecen una sola vez por capítulo sin clúster — no se tocaron salvo en los pocos casos de repetición literal en el mismo párrafo (c01 párrafo con tres "something", c02 con dos "something" en la misma frase).

## Ejemplos

**1 — Cluster obligatorio, EN, c01 (tres "something" en un párrafo):**
> Antes: *"Mikel felt something cold settle behind his sternum. ...the judge through fire pulled at something in him that felt like Arin... The one who waited in silence pulled at something older and stranger..."*
> Después: *"Mikel felt something cold settle behind his sternum. ...the judge through fire felt like Arin... The one who waited in silence felt older and stranger still..."*
> (Se conserva el primer "something" — hace el trabajo real de la frase — y se eliminan los otros dos con afirmación directa.)

**2 — Tic de estructura, EN/ES, c10 (introducción de Azael, 16→9 "the way" en el capítulo):**
> Antes: *"...resting there the way it always rested during the long stretches... he let it gather, the way he let most things simply happen around him..."*
> Después: *"...resting there as it always did during the long stretches... he let it gather, as he let most things simply happen around him..."*
> Espejo ES: *"del modo en que siempre reposaba..."* → *"como siempre reposaba..."*; *"del modo en que dejaba que..."* → *"como dejaba que..."*

**3 — El patrón dominante del tramo, EN/ES, c08 (Barachiel, 7 "found" → 2):**
> Antes: *"Barachiel found himself unable to look away from it... he found, for one long and terrible second, that he could not recall the man's name."*
> Después: *"Barachiel couldn't look away from it... for one long and terrible second, could not recall the man's name."*
> Espejo ES: *"Barachiel se descubrió incapaz de apartar la vista..."* → *"Barachiel no podía apartar la vista..."*

**4 — Réplica sagrada verificada intacta, c19 (duelo Thaeriel/Belial):**
> Sin cambios: *"'It endures you,' Thaeriel said. 'That isn't the same thing.'"* / *"—Te tolera —dijo Thaeriel—. No es lo mismo."*
> Los únicos recortes de ese capítulo caen en narración adyacente ("found himself, for one humiliating instant, unable to remember" → "for one humiliating instant, could not remember"), nunca en la línea.

## Capítulos con más trabajo

c03, c08, c10, c13, c17 y c24 concentraron la mayor parte de los recortes: son los capítulos de narración pura o casi pura (sin apenas diálogo intercalado), donde la muletilla tenía más espacio para acumularse sin la variación natural que impone el diálogo. c11, c14, c25 recibieron el trato más ligero — ya llegaban disciplinados de la pasada de estilo previa, o la muletilla aparecía dispersa sin clústers que corregir de forma obligatoria.
