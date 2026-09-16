# Auditoría editorial — Descripción e inmersión — Libro 1, capítulos 01–27 (EN)

Fecha: 2026-08-22 · Auditor: agente de descripción/inmersión · Tramo: `Libro1/EN/01_*.md` a `27_*.md` (27 capítulos, ~60.700 palabras, leídos completos y en orden).
Protocolo: `content/craft/10_auditoria_editorial.md` · Criterios: `content/craft/07_descripcion.md` + reglas de la casa de `prompt_universo.md`.

---

## 1. Diagnóstico general del tramo

El estilo cumple la premisa de la casa (**lírica contenida**): las imágenes son escasas, elegidas, y casi nunca decorativas. No hay purple prose, no hay bloques descriptivos que paralicen tensión, y **no encontré ninguna violación de la prohibición dura de símiles encadenados en una misma frase**. Las aperturas de capítulo entran en movimiento casi siempre en el primer párrafo — ninguna supera el umbral de ~2 párrafos sin que pase algo.

Los problemas del tramo no son de exceso sino de **repetición de fórmula y de carencia localizada**: (a) un vocabulario de interioridad idéntico compartido por todos los POV, (b) inflación de intensificadores abstractos (*exactly, simply, entirely, actually*) que crece capítulo a capítulo, y (c) dos capítulos (13 y sobre todo 24) donde el lector no puede imaginar el lugar donde ocurre la escena.

Contra el tópico del "escritor que solo ve": este libro **no** depende de la vista. El sentido dominante es el **oído** (hum de Solmire, chiming de las arboledas, la risa, el silencio como textura). Lo casi ausente es el **olfato** (sulfuro en 07, tierra quemada en 04, "old stone and older grief" en 15 — poco más en 27 capítulos) y el **gusto** (solo la sal del Sepulcro, 16). No es un error; es margen disponible.

---

## 2. Registro de ancla sensorial dominante por capítulo

| Cap | Ancla dominante | Nota |
|---|---|---|
| 01 | metal / luz sin sombras (+ calor, vidrio-arena) | tang metálico "after lightning" ≈ ozono |
| 02 | metal / luz sin sombras | continuación del mismo lugar — justificado; pero "shadowless light" 3× |
| 03 | luz fría (Solmire) vs. oro del Bastión | |
| 04 | luz + polvo pálido + silencio | firma del arma |
| 05 | luz + polvo blanco + silencio (+ barro, sangre) | repite el trío de 04 — ver hallazgo 6 |
| 06 | hueso, hierro negro, polvo, gritos residuales | buen cambio de paleta |
| 07 | lamplight, campana, música, sulfuro | refresco urbano; el mejor cambio del arco |
| 08 | luz + zumbido (hum) | |
| 09 | páginas orgánicas / farola, adoquines, perro | dos paletas distintas, ambas concretas |
| 10 | luz dura + chiming cristalino | mundo descrito por su sonido |
| 11 | silencio de marcha + táctil (la mano) | |
| 12 | luz fría del Bastión / calle mortal | |
| 13 | **(casi ninguna)** | ver hallazgo 8 |
| 14 | sonido (risa, campana) + sudor frío | |
| 15 | barro, fuego naranja vs. luz, gritos | |
| 16 | **sal (gusto) + chiming + frío** | punto alto del libro |
| 17 | (casi ninguna — sala de consejo) | tolerable en escena de deliberación |
| 18 | sal + chiming (Sepulcro) | eco justificado de 16 |
| 19 | visiones + mar (interludio pescador) | |
| 20 | frío, presión, gris, silencio total | punto alto |
| 21 | viento/olas (faro) + brasero en sala oscura | |
| 22 | chiming que muere | eco deliberado de 10 — funciona como rima |
| 23 | neón, TV, callos, cicatriz de llave inglesa | concreto, eficaz |
| 24 | **(ninguna)** | ver hallazgo 1 |
| 25 | garaje / lot al atardecer | fino pero suficiente |
| 26 | calle del garaje | suficiente |
| 27 | mármol de la Gran Mesa, grietas | |

Repeticiones de ancla en capítulos consecutivos: **03–04–05** (luz/polvo/silencio — motivo del arma, ver hallazgo 6) y **16→18→19→20** (sal/chiming — mismo plano en visitas sucesivas: propósito dramático claro, no lo señalo como falta). El eco 10→22 (arboledas que dejan de sonar) es rima estructural deliberada y es de lo mejor del tramo.

---

## 3. Adverbios en -ly: conteo y diagnóstico

Conteo bruto por capítulo (grep `\w+ly\b`, incluye falsos positivos tipo *only/family*; útil como tendencia relativa):

- Base del tramo: 27–50 por capítulo (~2.230 palabras/cap).
- **Picos**: cap. 24 (76), cap. 10 (70), cap. 25 (61), cap. 18 (59), cap. 23 (58), cap. 08 (56).
- Tendencia: la segunda mitad del tramo corre sistemáticamente más alta que la primera (caps. 01–05 promedian ~35; caps. 18–27, ~55).

Depurados los falsos positivos, el patrón real **no** es el adverbio ornamental clásico (-ly de modo pegado al verbo), sino la inflación de **intensificadores abstractos de certeza/totalidad**. Totales en los 27 capítulos:

| Palabra | Usos | Clasificación dominante |
|---|---|---|
| exactly | 109 | prescindible en ~2/3 de los usos |
| simply | 91 | prescindible en la mayoría |
| entirely | 73 | prescindible en la mayoría |
| actually | ~60 | prescindible/redundante |
| quietly | 25 | útil/prescindible según caso |
| carefully | 23 | útil/prescindible según caso |

Ejemplos de redundancia (el adverbio repite lo que la frase ya afirma):

- Cap. 10: "Miguel raised Solmire **the very instant** the threat-signal reached him […] **immediate and automatic**, faster than thought" — triple afirmación de inmediatez.
- Cap. 10: "a battle won this **cleanly** and this **completely**" — dos totalizadores para un dato ya dado por la escena.
- Cap. 24: "precise, **unhurried**, nothing wasted" y dos líneas después "as **clipped and functional** as every report" — la economía de Sariel se describe dos veces seguidas.
- Cap. 23: "an **entirely** ordinary night" / "an **entirely** unremarkable man" / "**entirely** on its own" — 6 usos de *entirely* en un capítulo cuyo tema ya es la ordinariez.

**Veredicto**: 🟠 debilidad real, no error — la prosa afirma certeza con adverbio en lugar de dejar que la frase la tenga. Una pasada de poda de *exactly/simply/entirely/actually* (la praxis obligada del apartado 07: si la frase sobrevive sin él, sobraba) bajaría el conteo un tercio sin tocar la voz. Priorizar caps. 10, 18, 23, 24, 25.

---

## 4. Hallazgos, por gravedad

### 🟠 H1 — Cap. 24: capítulo sin lugar + análisis circular
**Ubicación**: `24_The_Trail_That_Shouldnt_Be_There.md`, todo el capítulo (pico -ly: 76).
**Problema**: la única descripción del escenario en ~2.250 palabras es "The plane around him was already resettling into its ordinary rhythms" — un plano sin nombre, sin suelo, sin luz, sin temperatura. Sobre ese vacío, la firma anómala se re-analiza al menos seis veces con el mismo vocabulario (*unsettled, no category, patient, stable and unresolved* — párrs. de "The resonance carried…" a "He had no protocol built…").
**Por qué importa**: es el capítulo bisagra de Sariel (su primera desviación) y el lector lo atraviesa flotando en abstracción; la decisión pierde peso físico porque no ocurre *en* ningún sitio. Contrasta con el propio libro: la desviación paralela de Belial (caps. 16–20) está anclada en sal, frío y cristal, y por eso pesa.
**Solución sugerida** (sin cambiar esencia): dar al plano tres rasgos concretos (qué pisa Sariel, qué luz hay, qué queda del cadáver/kill site) y fundir dos de las seis vueltas analíticas. No hace falta reescribir: recortar y anclar.

### 🟠 H2 — Fórmula de interioridad compartida por todos los POV
**Ubicación**: transversal (los 27 capítulos).
**Problema**: todos los personajes piensan con las mismas tres muletillas: **"filed it/that away"** (8 usos, en POVs de Miguel, Camael, Ophaniel, Belial, Andras, Sariel, Corven y Raphael), **"told himself/herself"** (28 usos), **"did not examine"** (5 usos), más la etiqueta temporal **"in his/her long service"** (27 usos — casi uno por capítulo, en boca de ángeles, demonios y cazadores por igual).
**Citas**: cap. 5 "he **filed that fact away**, the way he had begun filing away so much else since Serephis" (Miguel); cap. 13 "Andras […] **filed the unease away** […] in the same quiet place he filed every other observation"; cap. 27 "He had let the question go unspoken since, **filed away** under things too inconvenient to raise twice" (Raphael); cap. 11 "Sariel **filed the sensation away** as background noise".
**Por qué importa**: la represión-de-lo-que-se-siente es EL gesto psicológico del libro (y es temáticamente correcto), pero al ejecutarse con idéntica fórmula verbal en ocho POVs distintos, las voces se funden en una sola y el gesto pierde significado — deja de caracterizar a Miguel que "archive" sus dudas si Andras, Ophaniel y Corven archivan con las mismas palabras.
**Solución sugerida**: conservar la fórmula como firma de 1–2 personajes (Miguel y Sariel son los candidatos obvios: el comandante y el burócrata de la caza) y variar el gesto en el resto (Belial ya tiene "crushed the doubt the way he crushed most doubts" en 09 — ese es el camino).

### 🟡 H3 — "unhurried": 35 usos en 17 capítulos
**Problema**: descriptor universal de compostura — se aplica a Lucifer (02, 06), Belial (13, 15, 18, 20), Foras (06, 21), Vual (25, 3×), Gabriel (08), Sariel (24, 26), Aamon, Camael, hasta un gesto de Corin. Picos: cap. 06 (4), caps. 13 y 25 (3).
**Por qué importa**: cuando la calma de Lucifer, la de Belial, la de Foras y la de Vual se nombran con la misma palabra, se pierde la jerarquía — la no-prisa de Lucifer debería ser de otra especie que la de un seductor de rango medio. Además el lector la registra como tic.
**Solución sugerida**: reservar *unhurried* para Lucifer (donde nació y donde es escalofriante) y diferenciar el resto por el cuerpo: Vual es paciencia de depredador, Foras es serenidad ensayada, Belial es control con costo — el texto ya lo sabe; solo la palabra los aplana.

### 🟡 H4 — Plantilla de símil "the way X does Y": 87 usos
**Problema**: no hay símiles encadenados (la prohibición dura se respeta), pero la misma sintaxis comparativa se repite hasta volverse previsible. Picos: cap. 22 (9), cap. 25 (9), cap. 11 (8), cap. 14 (7). Ejemplos: "the way a crowd gathers before it knows what it is gathering for" (03), "the way a person watches weather too large to argue with" (05), "the way a forger recognizes another forger's hand" (13 — este es excelente), "the way a man recognizes his own street" (22).
**Por qué importa**: muchas de estas comparaciones son buenas individualmente; en densidad de 5+ por capítulo, el mecanismo se hace visible y la mejor imagen del capítulo queda devaluada por sus vecinas — exactamente el caso "una imagen buena > tres adecuadas" de la regla de la casa.
**Solución sugerida**: en los cuatro capítulos pico, conservar la mejor de cada escena y podar o reformular (metáfora directa, o simple afirmación) las demás.

### 🟡 H5 — Caps. 03–04–05: tres demostraciones de Solmire con paleta y beats idénticos
**Problema**: tres capítulos consecutivos repiten la secuencia completa: onda de luz → enemigos deshechos en polvo pálido → armas bajadas sin orden → silencio → testigo inquieto (Tamiel/veteranos en 03; Camael/Dessa en 04; Joran/Mira/Raphael en 05). El ancla (luz fría + polvo + silencio) es la firma del arma — propósito dramático real — pero los *beats de reacción del testigo* también se repiten ("weapons lowered without any order to lower them" en 04 y su gemelo en 05; el suelo "too clean" en 04, 05 y de nuevo en 10).
**Por qué importa**: rendimiento decreciente — la tercera demostración impacta menos que la primera pese a ser objetivamente mayor. El cap. 10 rompe bien la serie (la erasure sin polvo siquiera, y el POV de Nyra), lo que confirma que la escalada funciona cuando cambia algo.
**Solución sugerida**: diferenciar la paleta de reacción en 05 (es la que más comparte con 04): Joran ya aporta la sangre de Nael y la lectura "scripture made real" — apoyarse en eso y podar los beats calcados (armas bajadas / suelo limpio), que ya están dichos en 04.

### 🟡 H6 — Cap. 02, agonía del árbol: un beat estirado
**Ubicación**: `02_The_Tree_Outside_Time.md`, párrafo "Behind him, the tree was dying…" y siguientes (~300 palabras).
**Problema**: la muerte del fresno acumula tres vueltas de lo mismo (polvo gris en los dedos → rama que cae y se parte → conteo de ramas → última hoja), y la frase "flat/flattened, shadowless light" aparece 3 veces en el capítulo (dos en este pasaje, una al final).
**Por qué importa**: es un momento de duelo ganado — pero la tercera repetición de la luz sin sombras y el doble beat de caída diluyen la imagen central (el conteo de ramas interrumpido, que es la mejor).
**Solución sugerida**: podar una de las dos menciones de "shadowless light" del pasaje y fundir rama+hoja en un solo beat; conservar intacto el conteo interrumpido.

### 🟡 H7 — Cap. 13: política sin cuerpo
**Ubicación**: `13_The_Devils_Gambit.md`, escenas del salón de Aamon y la marcha.
**Problema**: en todo el capítulo hay una sola imagen física del entorno (las columnas de obsidiana "arranged so that anyone standing before the throne had to look up") — el resto es maniobra pura. La marcha final tiene "banners low against the wind" y nada más.
**Por qué importa**: comparado con el cap. 06 (que construye corte, biblioteca y Torre con paleta propia), el 13 flota; el lector no puede situar la seducción de Aamon en un espacio, y la escena — larga — se sostiene solo por la tensión de la estafa. Es carencia, no error: la escena funciona, pero por debajo de su potencial.
**Solución sugerida**: 2–3 anclas físicas (el trono de Aamon, la luz del salón, algún sonido de la corte) repartidas en los párrafos de transición, no en los de maniobra.

### 🔵 H8 — Imagen reciclada dentro del cap. 01
"a compass needle with no patience for detours" (párr. del hallazgo de la calzada) y "like a compass needle holding north" (el guardián sin rostro) — la misma imagen dos veces en el mismo capítulo, aplicada a cosas distintas (la herida y el guardián), lo que además difumina a cuál pertenece. Dejar una.

### 🔵 H9 — Fórmulas temporales repetidas (pulido de línea)
"the better part of" (7 usos), la familia "in longer than he cared to measure / imagine / calculate" (16, 18, 20…), "for as long as he could remember". Ninguna daña por sí sola; juntas suman al efecto-fórmula de H2. Pasada de variación en revisión de línea.

### ⚪ H10 — Cap. 02, visión cósmica de la forja: densidad de imágenes alta pero legítima
El párrafo inicial acumula símiles en frases sucesivas ("like hot steel plunged into a bucket of dark", "a star-sized hammer […] an anvil made from a collapsed sun", "folded like cloth"). Cada frase lleva uno solo — no viola la prohibición — y el exceso controlado es el punto: la visión debe desbordar a Miguel. **Decisión estilística válida; no tocar.**

---

## 5. Lo que funciona especialmente bien (citar en futuras revisiones como vara)

1. **Cap. 16, llegada al Sepulcro** — "heavy on his tongue with the taste of salt and something colder than salt, something he did not yet have a word for" + el chiming "too close to weeping for Belial's taste". Gusto + oído + temperatura en un plano nuevo; la paleta sensorial más completa del libro, y toda al servicio del tema (el duelo como lugar).
2. **Cap. 20, cámara de la tumba** — "the air here carrying less salt and more of something Belial could only think of as pressure"; la lanza "so plain it took Belial a moment to accept that this was actually the thing he had bled for". Anti-clímax descriptivo deliberado: la sobriedad visual ES el significado del arma.
3. **Cap. 10, las arboledas** — "It sharpened, then scattered, then took on something that sounded […] uncomfortably close to a wail"; y al cierre, los groves junto al vacío "made no sound at all". Un mundo caracterizado enteramente por su sonido, y su herida narrada como silencio. La rima con el cap. 22 (Krass oye el chime morir "mid-tone") es de lo mejor estructuralmente.
4. **Cap. 9, el busker** — "guitar held together with what looked like actual tape", la farola con quejas en la oficina del distrito que se estabiliza, el perro que reconsidera. Lo numinoso construido con detalle municipal — máximo contraste de paleta con todo lo celestial/infernal, exactamente cuando el libro lo necesita.
5. **Cap. 4, el suelo limpio** — "ground so clean and so still it looked less like a battlefield than a room that had never been used", con el muro chamuscado al lado "as though two entirely different wars had been fought a few paces apart". La mejor formulación del horror de Solmire: por ausencia, no por gore.
6. **Cap. 1, el grove** — "a bright, even light that fell on nothing — no shadows anywhere, a flat and depthless world" y "Every soft crunch of fallen leaf beneath his boots felt like a shout inside a library". Inquietud sin adjetivos de inquietud.

---

## 6. Checklist del apartado 07 — resultado

- Aperturas de capítulo >2 párrafos sin que pase nada: **ninguna** ✅
- Acumulaciones de adverbios: **sí, intensificadores abstractos** (sección 3) — 🟠, picos en 10/18/23/24/25
- Escenas consecutivas con misma ancla sensorial: **03–04–05** (🟡, H5); 16–18–20 y 10↔22 justificadas ✅
- Tramos largos solo-vista: **no** — el oído domina; carencia real es *ausencia de todo sentido* en 13 y 24 (H1, H7)
- Cadenas de símiles en una frase: **ninguna** ✅ (plantilla "the way…" sobreusada — H4)
- Acumulación de adjetivos (2+ por sustantivo repetidos): **no sistemática** — los dobletes existen ("low, colorless glow"; "patient and enormous") pero espaciados y casi siempre con dos ejes distintos; no llega a hallazgo.

## 7. Nota orientativa del tramo (solo área Descripción/Inmersión)

**Descripción: 7,5/10 · Inmersión: 7/10.** El techo es alto (16, 20, 9, 10 son de nivel publicable tal cual); lo que baja la nota es transversal y barato de corregir: poda de intensificadores, des-uniformar la fórmula de interioridad, y anclar físicamente los caps. 13 y 24.

**Las tres cosas que más subirían la calidad del tramo**:
1. Reescritura ligera del cap. 24 (anclaje físico + fusión de vueltas analíticas) — H1.
2. Pasada global de poda: *exactly / simply / entirely / actually* + "the way…" en capítulos pico — sección 3 y H4.
3. Redistribuir la firma "filed away / told himself / long service" a 1–2 POVs — H2.

*Diagnóstico ≠ reescritura: nada de lo anterior se aplicó a la prosa. Cada intervención requiere aprobación del autor por hallazgo.*
