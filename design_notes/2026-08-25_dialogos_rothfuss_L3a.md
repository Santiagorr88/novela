# Pasada de diálogos — modo Rothfuss — Libro III, capítulos 01–13 (EN + ES)

**Fecha**: 2026-08-25 · **Tramo**: `Libro3/EN/01_*.md`–`13_*.md` y sus espejos `Libro3/ES/01_*.md`–`13_*.md` (13 capítulos × 2 idiomas, 26 archivos leídos íntegros). **Encargo**: cazar la atribución mecánica de diálogo ("X said" / "—dijo X—" en cadena, "X's voice", "La voz de X") y sustituirla por beat de acción, ping-pong sin atribuir (ancla cada 4–6 réplicas) o etiqueta superviviente llana/con información nueva, según el modelo Patrick Rothfuss aprobado por el autor. **Límites duros respetados**: ninguna réplica tocada en su contenido; ningún hecho, POV ni separador (`---`) alterado; solo atribución/beats. Las tres continuidades marcadas como protegidas del tramo (los intercambios de Turein "I've stood on it" en c04/c06, la réplica de Halaliel en c08, la réplica variada del ayudante de Camael en c12) se verificaron con las palabras intactas.

**Método**: EN primero, ES espejo inmediato de cada edición, capítulo por capítulo. Verificación por capítulo: estructura EN↔ES párrafo a párrafo + prueba "¿sé quién habla?" releyendo la escena sin las etiquetas retiradas.

---

## Diagnóstico previo

El encargo advertía que Libro III es el tramo más mecánico del corpus (248 etiquetas "X said" frente a 117 de Libro I) y que este tramo tendría "trabajo real, no solo verificación". La lectura íntegra de los 13 capítulos en ambos idiomas contradijo esa expectativa: **el tramo 01–13 ya está en un estado casi ejemplar del modelo Rothfuss**, con la única excepción real localizada en el capítulo 7. Esto es coherente con el propio encargo, que ya señalaba c01 y c04 como "ping-pong ideal" — lo que no se había anticipado es que caps. 05, 06, 08, 09, 11 y 12 comparten el mismo nivel de pulido, probablemente por tratarse en su mayoría de escenas de dos voces con registros ya muy distintivos (Ereloth/Mikel, Lucifer/Belial, Kushiel/Thariel/Sachael) donde el autor ya escribió con beats y pronombres desde el primer borrador.

| Cap. | Diálogo | Veredicto |
|---|---|---|
| 01 | Ereloth/Mikel (taberna) | Ya limpio — 8 tags repartidos sin cadena, ninguno consecutivo sin beat de por medio |
| 02 | Lyra (informe) | Ya limpio — 3 líneas totales, tags espaciados |
| 03 | Sin diálogo | N/A |
| 04 | Ereloth/Mikel (lección) | Ya limpio — el "ping-pong ideal" señalado por el encargo; beats ya hacen la mayor parte del trabajo |
| 05 | Lucifer/demonio, Lucifer/Belial | Ya limpio — interrogatorio casi sin nombre propio; consejo con anclas cada 2 turnos, sin cadena |
| 06 | Ereloth/Mikel (tormenta) | Ya limpio — **protegido**: "I've stood on it" (Mikel) intacto |
| **07** | Ereloth/Mikel (playa) | **Editado** — único hallazgo real del tramo |
| 08 | Barachiel/Halaliel | Ya limpio — **protegido**: réplica de Halaliel intacta, ya sin tag propio |
| 09 | Thaeriel/Vorlag | Ya limpio — anclas cada 2 turnos, técnica de revelación diferida ("a third voice said" → "Sachael") |
| 10 | Sin diálogo | N/A |
| 11 | Kushiel/soldado, Kushiel/Thariel/Kemuel/Sachael | Ya limpio — coral de cuatro voces con claridad ya priorizada, tags mid-quote y beats extensos |
| 12 | Camael/Vepar (batalla) | Ya limpio — **protegido**: réplica del ayudante de Camael intacta, ya sin tag |
| 13 | Sin diálogo | N/A |

**Hallazgo principal**: de 13 capítulos, 3 no tienen diálogo (03, 10, 13) y de los 10 restantes solo uno (07) tenía un defecto real de atribución mecánica. Se comprobó explícitamente que no hay ninguna instancia de "That was X" ni "La voz de X" como *patrón de atribución* (las apariciones de "Ereloth's voice", "Halaliel's voice", "Thariel's voice", "Sachael's voice" localizadas por grep son todas usos descriptivos legítimos — "su voz llegó desde algún lugar cercano", "su voz se mantuvo plana" — no sustitutos de etiqueta). Tampoco se encontró ningún sinónimo ornamental de "said/dijo" (hissed, growled, intoned, snapped, etc.) en todo el tramo.

---

## Capítulo 7 — The Sword Remembers / La espada recuerda

Único hallazgo del tramo: doble etiqueta redundante en la primera línea de Ereloth tras la reforja de Solmire — el momento de mayor peso emocional del capítulo, lo que hacía la redundancia más visible, no menos.

**EN**, antes:
> `"There he is," Ereloth said. He said it the way a man says something he's been waiting a long while to be able to say honestly. "Welcome back, brother."`

**EN**, después:
> `"There he is." Ereloth said it the way a man says something he's been waiting a long while to be able to say honestly. "Welcome back, brother."`

Se eliminó la primera etiqueta ("Ereloth said") por ser enteramente redundante con la segunda oración, que ya cumple la función de etiqueta + beat con información real (el tono, la espera). La réplica en sí no se tocó una sola palabra.

**ES**, antes:
> `—Ahí está —dijo Ereloth. Lo dijo del modo en que un hombre dice algo que lleva mucho tiempo esperando poder decir con honestidad—. Bienvenido de vuelta, hermano.`

**ES**, después:
> `—Ahí está. —Lo dijo del modo en que un hombre dice algo que lleva mucho tiempo esperando poder decir con honestidad—. Bienvenido de vuelta, hermano.`

Se retiró "dijo Ereloth" y se dejó "Lo dijo..." solo, apoyándose en el pro-drop español (la conjugación de "dijo" ya identifica sujeto sin necesidad de nombrarlo, y Ereloth es el único hablante posible en la escena). Estructura de rayas verificada como válida (inciso narrativo de una oración completa, abierto y cerrado con raya, entre dos fragmentos de la misma réplica). Resto del capítulo verificado sin más hallazgos: el resto de la escena playa ya usa beats puros ("Ereloth shrugged, the gesture easy...", "Ereloth looked out at the water, considering...") sin ninguna etiqueta añadida.

## Capítulos sin cambios (01–06, 08–13)

Verificados íntegros en ambos idiomas y dejados sin tocar por ya cumplir el modelo:

- **01** (Ereloth/Mikel, taberna): 8 tags en ~13 réplicas, ninguno en cadena — cada uno separado por al menos un párrafo de beat o narración. Ereloth ya es identificable por voz sola (apodos, humor torcido) en la mayoría de sus líneas.
- **02** (Lyra, informe de campo): diálogo mínimo (3 líneas), tags espaciados por páginas de narración entre ellos.
- **04** (Ereloth/Mikel, lección): el "ping-pong ideal" del encargo. Comprobado turno a turno: cada etiqueta con beat combinado o con información real (tono, ritmo); ninguna cadena de 3+ tags consecutivos en todo el capítulo.
- **05** (Lucifer/demonio → Lucifer/Belial): el interrogatorio inicial resuelve casi todo por alternancia sin nombre ("he said" una sola vez para Lucifer, "it said" una vez para el demonio); el consejo con Belial usa anclas de apertura de turno cada 2 réplicas, exactamente el patrón recomendado por la regla 2.
- **06** (Ereloth/Mikel, tormenta de Turein): **protegido** — "I've stood on it" (Mikel) verificado intacto, tag ya mínimo ("Mikel said, and it came out almost as an objection" — con información real, no se tocó). El resto del capítulo usa el entorno (viento, distancia) para atribuir sin nombrar ("Ereloth's voice reached him from somewhere close by").
- **08** (Barachiel/Halaliel, torre vigía): **protegido** — la réplica de Halaliel ("It's not registering on any of the standard instruments...") ya no lleva tag propio; el único tag de la escena abre el parlamento completo y no se repite.
- **09** (Thaeriel/Vorlag, Malignus): anclas cada 2 turnos; uso de revelación diferida para Sachael-equivalente ("a third voice said" seguido de identificación por acción) ya presente y funcional.
- **10** y **13**: sin diálogo, capítulos enteramente narrativos (Azael en la cima, Thaeriel en las Llanuras de Nihil).
- **11** (Kushiel/soldado, luego Kushiel/Thariel/Kemuel/Sachael): coral de cuatro voces resuelto con exactamente la prioridad que pide el encargo ("corales con claridad absoluta") — tags mid-quote, revelación diferida para la entrada de Sachael, beats extensos que sustituyen tag en más de la mitad de las réplicas.
- **12** (Camael/Vepar, la brecha del Entremedio): **protegido** — la réplica del ayudante de Camael ("I don't — sir, nothing will read it...") ya carece de tag alguno, atribuida solo por alternancia tras la pregunta de Camael. Escena coral de batalla (dos comandantes + dos ayudantes) con densidad de tag alta pero justificada: cada bando necesita anclaje propio para no confundir "his aide"/"his second" entre los dos ejércitos — se verificó que ninguna secuencia de tags es mecánicamente repetitiva (varían entre "asked/answered/added/agreed/reported/ordered", todos con función real, ninguno ornamental).

---

## Resumen cuantitativo

| Capítulo | Ediciones EN | Ediciones ES | Tipo de intervención |
|---|---|---|---|
| 07 | 1 | 1 | Fusión de doble etiqueta redundante ("said... He said it...") en tag+beat único |
| 01–06, 08–13 | 0 | 0 | Verificados, ya conformes al modelo |

**Total**: 1 edición en EN, 1 edición espejo en ES (2 ediciones en 2 archivos), sobre 26 archivos leídos íntegros.

## Protegidos verificados intactos

Las tres continuidades marcadas como no tocables en el encargo se comprobaron sin alteración de una sola palabra: "I've stood on it" (Mikel, c06, con eco temático en c04 sobre la misma isla), la réplica de Halaliel en c08, y la réplica variada del ayudante de Camael en c12. Ningún hecho, orden causal, POV o separador (`---`) se modificó en ningún capítulo del tramo.

## Nota de método

El volumen de ediciones (1 de 26 archivos) es real, no un artefacto de lectura superficial: se leyeron los 13 capítulos completos en ambos idiomas, se verificó cada instancia de "voice"/"voz" para descartar el patrón de atribución que el encargo pedía cazar explícitamente, se hizo grep dirigido de sinónimos ornamentales (ninguno encontrado) y de dobles etiquetas ("X said. He/She said" — solo el caso del c07), y se contrastó la densidad EN↔ES capítulo por capítulo para descartar asimetrías de traducción (las diferencias de conteo bruto entre idiomas, mayores en ES por variantes de grep como "convino"/"informó"/"añadió" no cubiertas en el patrón inglés, resultaron ser artefactos del método de conteo, no atribución real añadida en la traducción — confirmado leyendo íntegros los capítulos con mayor diferencia aparente: 02, 05, 11, 12). La conclusión honesta es que este tramo específico (01–13) ya había recibido, en su redacción original o en una pasada previa no registrada bajo este nombre, un tratamiento de diálogo muy cercano al modelo Rothfuss — a diferencia de lo que el encargo anticipaba para "el libro más mecánico del corpus", esa densidad mecánica no aparece concentrada en este primer tercio. Queda como hipótesis razonable para quien continúe el tramo 14–52 que la densidad real esté más adelante.
