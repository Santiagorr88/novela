# Auditoría fresca — B1C27.5 (Anael) y B2C36.8 (Vual/Agares/Nymos) (2026-08-21)

**Alcance**: `B1C27pt5_EN.md` ("Sparks for the Numb", Anael, Libro I) y `B2C36pt8_EN.md` ("A Truth Told First", Vual/Agares/Nymos, Libro II). Lectura completa e independiente de ambos, más `B1C27_EN.md`, `B1C28_EN.md` (vecinos directos de B1C27.5), `B2C36pt6_EN.md` y `B2C36pt7_EN.md` (vecinos directos de B2C36.8), `content/lore/personajes.md` (fichas de Anael, Ezihel, Barachiel, Vual, Agares, Nymos, Asmodeus), `content/lore/expansion_guidelines.md` (reglas B3C20/B1C15, ahora reubicadas), `content/lore/book1_part3_expanded_beats.md` y `content/lore/book2_part3_expanded_beats.md` (planes de beats de ambos capítulos), `content/lore/arco_argumental_completo.md` (entradas B2C147-151 y el bloque `SUPERADO` línea 1572), `content/lore/expansion_progress_libro2.md` (sesión que documenta la restricción de orden cronológico entre B2C36.5/.6/.7/.8), y los dos informes de revisión ya existentes (`chapters/EN/reports/B1C27.5_review.md`, `chapters/EN/reports/B2C36.8_review.md`). Auditoría de solo lectura — no se editó ningún archivo de prosa; solo se produjo este informe.

**Nota de método**: igual que en `2026-08-20_fresh_audit_book2.md` y `_book3.md`, cada capítulo ya pasó por un panel de 5 revisores (4 Claude + Codex) antes de commitearse. Esta pasada busca deliberadamente lo que ese proceso, capítulo a capítulo, no ve: instancias de POV que sobreviven a la revisión, contradicciones con capítulos vecinos, y citas rotas de outline.

---

## 1. B1C27.5 — "Sparks for the Numb" (Anael)

**Ficha verificada contra `personajes.md`**: Anael, Captain / Emotion & Inspiration, arma *Lyre of Light* (línea 122-128) — consistente, entrada única, sin fichas duplicadas contradictorias. Barachiel, Captain / Angelic Communications, arma "Living scrolls" (línea 132-138) — consistente; el capítulo lo usa como mensajero de rosters administrativos, no en combate, coherente con su arma sin necesidad de invocarla literalmente. Ezihel, Squad Leader / Spirit Reanimator bajo Anael (Captain), arma *Lumen* (línea 182-187) — consistente, y la escena respeta correctamente la jerarquía (Ezihel solo se permite dudar en privado ante su propia capitana, nunca frente a los heridos). El propio plan de beats (`book1_part3_expanded_beats.md` línea 78) ya documenta y resuelve una contradicción de cadena de mando en el propio `personajes.md` (Anael listada una vez bajo "Camael" y dos veces bajo "Zadquiel" como Commander) — verificado que el capítulo nunca nombra a ningún Commander en prosa, así que esa contradicción de documentación no tiene impacto textual.

**Continuidad verificada**: encaja exactamente en el hueco temporal entre `B1C27_EN.md` (la noche de la retirada) y `B1C28_EN.md` (que abre "weeks had passed" en el mismo Temple of Shattered Light, intacto y no tocado). La escena dramatiza línea por línea lo que `B1C28` resume en una sola frase ("Anael moved among the soul-wounded... leaving small sparks of feeling in hands too numb to ask for them") y reutiliza a Barachiel, ya presente en esa misma escena coral de B1C28 ("murmured old prayers toward scattered squads"). Sin contradicción de fecha, lugar ni personaje. `B1C28_EN.md` confirmado intacto (no aparece en el historial de commits de hoy).

### Hallazgos de POV (regla B3C20 / B1C15)

- **[Menor]** Línea 13: *"his usual eloquence dulled by three weeks of very little sleep"* — afirma como hecho de narrador el rasgo habitual de Barachiel ("usual eloquence") y una cifra concreta de su historia reciente ("three weeks"), sin marco de inferencia de Anael. Propuesta: *"though this morning she heard his usual eloquence dulled, worn thin by weeks of too little sleep."*

- **[Menor]** Línea 13: *"he still moved through the gallery like a man accustomed to being listened to"* — generalización de carácter/historia de Barachiel narrada como hecho vía símil, no como lectura de Anael. Mismo patrón que el ya señalado en la auditoría del 2026-08-20 (Book II) para Orifiel/Zaphiel. Propuesta: *"he still moved through the gallery the way she'd always read him — like a man accustomed to being listened to."*

- **[Menor]** Línea 15: *"He held the scroll out, not quite meeting her eyes, the way a man offers something he suspects is unkind to give."* — atribuye una sospecha interna concreta a Barachiel como hecho narrado. Propuesta: *"the way a man offers something she read as suspecting was unkind to give."*

- **[Menor]** Línea 29: *"the same steadiness everyone in her squad had come to expect of her"* — generalización sobre la reputación establecida de Ezihel dentro de su escuadrón, narrada como hecho, no como conocimiento específico de Anael. Nota: esta es exactamente la línea que el informe de revisión (`B1C27.5_review.md`, hallazgo bloqueante #1) corrigió por otra razón (fuga del término de producción "fiche") — el fix aplicado resolvió la fuga léxica pero no tocó la generalización de fondo, que sobrevive en la nueva redacción. Mismo patrón de "brecha entre lo corregido y lo que queda" ya documentado en `2026-08-20_fresh_audit_book2.md` §1 (caso B2C03.6). Propuesta: *"the steadiness Anael had come to read as Ezihel's own, held in place by something costing her more than usual today."*

- **[Cosmético]** Línea 5: *"the rhythm of a body that had forgotten it was allowed to relax"* — atribuye un estado cognitivo ("had forgotten") al soldado catatónico sin nombre, como hecho narrado. Es un recurso lírico deliberado (el mismo verbo "forgotten" se reutiliza en la línea 45 como eco intencionado), pero técnicamente afirma interioridad de un tercero. Propuesta: *"the rhythm of a body that seemed, to her ear, to have forgotten it was allowed to relax."*

- **[Cosmético]** Línea 45: *"a hand that had forgotten, until that instant, that it still belonged to him"* — mismo patrón que la línea 5, en el beat central de la "chispa". Severidad cosmética porque es el clímax deliberado del capítulo y el resto del párrafo ya está correctamente enmarcado ("she did not reach for the meaning of it either, certain that..."). Propuesta: *"a hand that seemed, for that one instant, to remember it still belonged to him."*

- **[Cosmético]** Línea 51: *"stripped of whatever kindness his voice had tried to wrap around it"* (sobre Barachiel) — atribuye un esfuerzo intencional a Barachiel como hecho. Propuesta: *"stripped of whatever kindness she'd heard him trying to wrap around it."*

- **[Cosmético]** Línea 59: *"the first sound all evening that hadn't been carefully held in place"* (sobre Ezihel) — generalización de certeza sobre el autocontrol deliberado de Ezihel durante toda la tarde, no marcada como percepción de Anael. Propuesta: *"the first sound all evening Anael hadn't heard her holding carefully in place."*

**Resto del capítulo**: limpio, y con buenos ejemplos del patrón correcto ya presentes — *"the tone she imagined he once used"* (línea 19, hedge explícito), *"Anael could see costing her more than usual today"* (línea 29, hedge explícito en la misma frase que contiene el hallazgo de arriba), *"Anael recognized without needing to ask"* (línea 55), *"Anael thought she might argue it"* (línea 37) — confirman que el capítulo sabe aplicar la regla correctamente cuando lo hace, lo que hace más notable que sobrevivieran las 7 instancias de arriba.

---

## 2. B2C36.8 — "A Truth Told First" (Vual / Agares / Nymos)

**Ficha verificada contra `personajes.md`**: Agares, Commander / Language Manipulation, bajo Asmodeus (confirmado línea 1699-1711, "Asmodeus... and all his forces" como cabecera de sección que engloba a Balam y Agares como Commanders) — consistente con la propia prosa de `B2C36pt6_EN.md` ("Agares answered to Asmodeus in every matter of ordinary chain and rank"). Vual, Captain / Seducer of Reincarnated Souls, bajo Agares, arma *Deseum* (línea 1773-1779, no invocada en este capítulo — correcto, no es un capítulo de combate). Nymos, Squad Leader / Prince of Masks bajo Vual → Agares, arma *Volarien* — "Mask reflecting the beholder's hidden desire" (línea 1949-1954); el uso en prosa ("Volarien does the rest. It always does") es fiel al mecanismo fichado (confirma lo que el objetivo ya cree, no transformación genérica). Ley de Percepción Mortal respetada: Selke nunca percibe a Vual ni a Nymos como algo distinto de hombres ordinarios.

**Continuidad cronológica verificada contra `B2C36pt6_EN.md`**: `expansion_progress_libro2.md` (línea 31-35) documenta una restricción dura de diseño — la redacción y primera difusión del falso Codex (B2C36.8, outline `B2C149`) tienen que ser previas a la aprobación de Lucifer (B2C36.6, outline `B2C150`). Verificado que el texto respeta esa restricción sin contradicción: en `B2C36pt8`, el pergamino que Vual lleva es explícitamente un *borrador tosco, sin pulir* ("rougher than anything Agares would ever let leave Dis with his own name attached to it... the polish, if the thing ever needed polish, was Agares's business to add later"), distinto de las "polished pages" que Lucifer aprueba en `B2C36pt6` sin cambiar una sílaba. `B2C36pt6` a su vez afirma que esas páginas pulidas aún no habían "left Dis for the mortal underground" en el momento de esa escena — compatible con que una versión previa y más tosca del mismo rumor ya circulara informalmente por el Undertow (mercado mortal, un canal distinto y deliberadamente no oficial, tal como Agares lo pide explícitamente en diálogo: *"I don't care whose mouth it starts in, so long as it isn't recognizably mine"*). El propio outline (`arco_argumental_completo.md` líneas 1133-1138, entradas B2C149/B2C150) confirma esta misma estructura de dos pistas paralelas. Sin contradicción real.

**Continuidad verificada contra `B2C36pt7_EN.md`**: sin solapamiento de personajes, escenas ni afirmaciones — `B2C36pt7` (Raziel/Eshriel/Jahiel/Zaphiel) ocurre en un hilo completamente distinto (Cielo rastreando un fragmento del Codex en la Ashgrave) sin ningún punto de contacto textual con `B2C36pt8` (Agares/Vual fabricando y difundiendo una versión falsa en el mundo mortal). Ambos capítulos comparten solo el tema general de "el Codex se está filtrando", sin que ninguno mencione hechos del otro. Limpio.

**Hallazgo, cosmético** (continuidad/estructura, no POV): a diferencia de `B2C36pt7` (que se ancla explícitamente "three nights past" respecto a `B2C36pt5`), `B2C36pt8` no contiene ningún marcador temporal en prosa que lo sitúe respecto a sus vecinos — su posición cronológica real (entre .5 y .6) vive solo en `expansion_progress_libro2.md`, no en el texto. Mismo patrón exacto ya señalado como hallazgo cosmético en `2026-08-20_fresh_audit_book3.md` §1.1 para `B3C28pt7`. Dado que el propio proyecto ya advirtió (`expansion_progress_libro2.md` línea 35) que el sufijo numérico `.8` no refleja el orden cronológico real, una frase de anclaje explícita evitaría que un lector que siga el orden de archivos (`.5 → .6 → .7 → .8`) infiera el orden equivocado. Propuesta: una cláusula de apertura del tipo *"days before the pages he'd eventually seal with his own hand would ever reach Lucifer's desk"*.

### Hallazgos de POV (regla B3C20 / B1C15)

Patrón dominante y repetido: la construcción **"the particular/frank/loose [cualidad] of a [sustantivo] who/that [generalización de carácter]"**, aplicada a un tercero (Agares o Nymos) sin verbo de inferencia de Vual — la misma familia de tic ya identificada como recurrente entre sesiones en `2026-08-20_fresh_audit_book3.md` (hallazgo #10, construcción "the [adj.] X of a [noun] who Y"). Aparece aquí seis veces, casi siempre sobre los mismos dos personajes:

| # | Línea | Cita | Tercero afectado |
|---|---|---|---|
| 1 | 9 | *"Agares's smile widened, unhurried, the particular pleasure of a man watching his own reasoning arrive exactly where he had steered it."* | Agares |
| 2 | 13 | *"Agares studied him with the frank, appraising patience of a man selecting a tool for a job he had already solved in his own head."* | Agares |
| 3 | 17 | *"What was written inside was rougher than anything Agares would ever let leave Dis with his own name attached to it"* | Agares |
| 4 | 19 | *"...the loose, unbothered confidence of someone who had never once needed to work for an invitation."* | Nymos |
| 5 | 47 | *"...dropping into the chair with the satisfied economy of a man reporting a job that had required less effort than promised."* | Nymos |
| 6 | 51 | *"Nymos's smile came back easily, whatever had briefly interrupted it filed away wherever he kept things he preferred not examined."* | Nymos |
| 7 | 63 | *"...found his commander receiving the account the way he received most successes — with a stillness that carried more satisfaction in it than any open pleasure could have managed."* | Agares |
| 8 | 69 | *"Agares's smile settled into something almost restful, the particular ease of a man who had built a mechanism and watched it run exactly to specification."* | Agares |

**Severidad**: [Menor] en las 8 instancias — ninguna cambia un hecho de trama ni contradice la ficha de personaje (de hecho, todas describen correctamente el carácter ya fichado de Agares/Nymos); todas comparten el mismo defecto de encuadre: hecho de narrador en vez de lectura explícita de Vual. Nótese el contraste con la línea 19 (justo antes del hallazgo #4 en la misma tabla), donde el propio informe de revisión ya corrigió un cabalgamiento de POV casi idéntico en la misma entrada de Nymos (*"an expression that struck him as arrived at rather than simply worn"*) — la corrección se aplicó a esa frase concreta pero no generalizó el patrón al resto del capítulo, donde reaparece sin tocar seis veces más. Propuesta de reescritura de una cláusula, aplicable al patrón entero (ejemplo sobre #1): *"Agares's smile widened, unhurried — Vual read in it the particular pleasure of a man watching his own reasoning arrive exactly where he'd steered it."*

- **[Menor, el más notable de los dos capítulos]** Línea 59: *"Somewhere above the reach of anything he could see from this cellar, a committee was weighing caution against candor, drafting language careful enough to survive its own scrutiny."* — a diferencia de los 8 hallazgos de arriba (generalización de carácter de un tercero presente en escena), este es un cabalgamiento de POV genuino: narra como hecho una escena en Cielo que el propio texto admite, en la misma frase, estar "beyond the reach of anything he could see" — es decir, se afirma como sabido algo que el narrador acaba de declarar inaccesible para el ancla de POV (Vual). La frase anterior (*"He thought... of the councils in Heaven that had not yet finished agreeing..."*) sí está correctamente enmarcada como el pensamiento de Vual; esta segunda frase, en cambio, rompe ese marco y narra directamente. Propuesta: *"He imagined it easily enough: a committee, somewhere above the reach of anything he could see from this cellar, weighing caution against candor, drafting language careful enough to survive its own scrutiny."*

- **[Cosmético]** Línea 57: *"Neither buyer knew they were purchasing the same seed, grown to fit two different appetites."* — afirmación omnisciente sobre el estado mental de dos compradores de fondo sin nombre. Severidad baja por tratarse de personajes de fondo no presentes en escena con Vual, mismo criterio de severidad usado en `2026-08-20_fresh_audit_book2.md` para el caso análogo de "mensajeros sin nombre" en B2C21.6.

**Resto del capítulo**: los pasajes que sí enmarcan correctamente la inferencia de Vual son mayoría y de buena calidad — *"Vual read that choice the way he read most things Agares did"* (línea 3, hedge explícito desde la primera frase), *"he read something in the too-composed set of the man's features — an expression that struck him as..."* (línea 19, la corrección ya aplicada por el panel), *"something like genuine interest"* (línea 21, hedge suave aceptable), *"Whatever passed behind his shifting face in that half-second, he offered nothing further to explain it... chose not to ask"* (línea 47, buen ejemplo de ambigüedad preservada sin asertar contenido interno) — de nuevo, el capítulo demuestra saber aplicar la regla, lo que hace más notable la persistencia del tic en las líneas de arriba.

---

## 3. Citas rotas

Ninguno de los dos capítulos cita en su propia prosa un número de entrada del outline ni un `subplot_id` — igual que en la auditoría anterior, esas referencias viven solo en los documentos de planificación.

- **B1C27.5**: `book1_part3_expanded_beats.md` línea 78 afirma explícitamente que `arco_argumental_completo.md` no tiene ninguna entrada específica para Anael. Verificado con `grep -n "Anael" content/lore/arco_argumental_completo.md`: cero resultados — la afirmación es correcta, no es una cita rota (es la ausencia documentada correctamente).
- **B2C36.8**: `expansion_progress_libro2.md` y `book2_part3_expanded_beats.md` citan `arco_argumental_completo.md`, entradas **B2C148-150** (líneas 1129-1141) y el `subplot_id` **`B2-agares-01`**. Verificado: las tres entradas existen exactamente donde se citan, con el contenido descrito (B2C149 se titula literalmente "A Truth Told First", el mismo título que el capítulo). Verificado también que están **fuera** del bloque `SUPERADO` (que empieza en la línea 1572 y cubre B3C087-125, un rango de Libro III sin relación) — cita correcta, sin riesgo de apoyarse en contenido descartado.

---

## 4. Regla Miguel/Michael

`grep -ni "michael\|miguel"` sobre ambos archivos: cero resultados en los dos. Regla no aplica, sin riesgo.

## 5. Reveal-pacing (Thamorak / los Forgotten)

`grep -ni "thamorak\|ereloth\|thaeriel\|azael\|forgotten"` sobre ambos archivos: las únicas coincidencias son el verbo común "forgotten" en `B1C27pt5` (líneas 5 y 45, ya analizadas arriba como parte de los hallazgos de POV, sin relación con la entidad Forgotten) — cero menciones de las entidades propiamente dichas en ningún capítulo. Verificado además que `B2C36.8` no toca en ningún momento la inquietud privada de Lucifer sobre "three primordials, reunited" que `B2C36pt6` ya establece y que el propio outline (`arco_argumental_completo.md` línea 1139) marca explícitamente como no revelable hasta `B3C059`/`B3C061` — `B2C36.8` se mantiene enteramente dentro de la mecánica de Agares/Vual/Nymos/Selke difundiendo el rumor, sin acercarse a esa interioridad de Lucifer. Limpio en ambos capítulos.

---

## 6. Resumen ejecutivo

| Capítulo | Hallazgos POV | Bloqueantes | Menores | Cosméticos | Continuidad/nombres/armas | Citas outline | Reveal-pacing |
|---|---|---|---|---|---|---|---|
| B1C27.5 (Anael) | 7 | 0 | 4 | 3 | Limpio | Limpio (ausencia documentada correcta) | Limpio |
| B2C36.8 (Vual/Agares/Nymos) | 10 | 0 | 9 | 1 | Limpio (más 1 hallazgo cosmético de anclaje temporal en prosa) | Limpio (B2C148-150, `B2-agares-01`, fuera de SUPERADO) | Limpio |
| **Total** | **17** | **0** | **13** | **4** | | | |

**Total de hallazgos: 18** (17 de POV + 1 de continuidad/anclaje temporal en B2C36.8). **Bloqueantes: 0.**

Ningún capítulo queda completamente limpio, pero **ningún hallazgo es bloqueante**: no hay contradicciones de continuidad con los capítulos vecinos (`B1C27_EN.md`/`B1C28_EN.md` para el primero, `B2C36pt6_EN.md`/`B2C36pt7_EN.md` para el segundo, ambos verificados intactos y compatibles), ni errores de nombre/rango/arma/comandante contra `personajes.md`, ni citas rotas de outline, ni fugas de reveal-pacing sobre Miguel/Michael o Thamorak/los Forgotten.

**Los hallazgos más importantes**:

1. **B2C36.8 concentra el tic de estilo/POV más denso de los dos capítulos**: la construcción "the particular/frank/loose [cualidad] of a [sustantivo] who/that [generalización]" aparece 8 veces sin marco de inferencia de Vual, repartida casi igualmente entre Agares y Nymos (tabla en §2). Es la misma familia de tic ya documentada como recurrente *entre sesiones* en `2026-08-20_fresh_audit_book3.md` (hallazgo #10) — vale la pena una pasada de búsqueda específica de este patrón en el resto de escenas de Agares/Vual ya escritas, no solo en este capítulo.
2. **B2C36.8, línea 59**: el único cabalgamiento de POV genuino (no solo generalización de carácter) de los dos capítulos — narra como hecho una escena en Cielo que la propia frase anterior admite estar fuera del alcance de lo que Vual puede ver. Es el hallazgo individual más claro de los 18.
3. **B1C27.5, línea 29**: mismo patrón ya visto en la auditoría del 2026-08-20 — el informe de revisión corrigió esta línea por una razón (fuga del término "fiche") pero dejó intacta una generalización de fondo sobre la reputación de Ezihel que el proceso de revisión no estaba buscando. Confirma que el patrón de "el fix resuelve el síntoma señalado, no el problema de encuadre subyacente" no es un caso aislado de la sesión anterior.
4. **B2C36.8 es, de los dos, el que depende más de documentación externa a la prosa para su continuidad**: tanto la restricción de orden cronológico frente a `B2C36pt6` (§2) como su posición relativa a `B2C36pt5`/`.7` (hallazgo cosmético de anclaje temporal) viven únicamente en `expansion_progress_libro2.md`, no en el texto — reconciliable con lectura cuidadosa del propio outline y de los informes de revisión, pero no auto-evidente para un lector que solo tenga la prosa delante.
