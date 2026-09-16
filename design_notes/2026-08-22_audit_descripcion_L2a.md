# Auditoría de descripción e inmersión — Libro 2, capítulos 01–27 (EN)

Fecha: 2026-08-22 · Tramo: `Libro2/EN/01_*.md` a `27_*.md` (~57.900 palabras) · Área 5 (+6 parcial) del protocolo (`craft/10_auditoria_editorial.md`) · Criterios: `craft/07_descripcion.md`

**Regla fundamental aplicada**: cada hallazgo está clasificado como error real / debilidad / oportunidad / decisión estilística válida, con cita. No hay hallazgos 🔴 en este tramo: nada rompe lógica, continuidad ni comprensión. Los problemas de descripción son de acumulación y de paleta, no de arquitectura.

---

## 1. Diagnóstico general

La prosa del tramo es disciplinada: casi nunca hay bloque descriptivo que paralice una escena (la descripción viaja montada en el movimiento y la interioridad), los entornos clave tienen concreción real, y el contraste sensorial entre planos existe y se percibe. Las dos debilidades sistémicas son (a) **una paleta sensorial que se estrecha tras los primeros capítulos** — el olfato y el gusto casi desaparecen del libro después del cap. 02 — y (b) **un conjunto de muletillas de altísima frecuencia** ("the particular", "never once", "held breath", "unhurried", "the way a…") que, capítulo a capítulo funcionan, pero acumuladas en 27 capítulos producen el efecto exacto que `07_descripcion.md` prohíbe: apoyarse en la misma imagen en escenas consecutivas.

---

## 2. Lo que mejor funciona (pasajes especialmente buenos)

1. **Cap. 01, apertura** — "The lecture hall at Navarion smelled of old paper and radiator dust… grey light pressing flat against the high windows". Concreción terrestre inmediata, dos sentidos en la primera frase, y el aula descrita a través de conducta ("laptops open to windows that weren't his slides"). Y el cierre del motivo del pecho: "Not pain, exactly. A vacancy with edges" — abstracción ganada con imagen concreta.
2. **Cap. 07, la Grey City** — el mejor entorno terrestre del tramo. La ciudad no se describe: se demuestra. "He watched a woman drop her groceries on a corner and watched three people step around the spilled fruit without breaking stride". Un solo gesto observado sustituye párrafos de exposición sobre desesperanza ambiental.
3. **Cap. 12, el trabajo de Barbas** — inmersión táctil sostenida sin gore: "the particular shallow catch of her breath each time the needle found a memory", y la fe de la centinela "worn smooth the way a single stone goes smooth from the same hand closing around it". Además el terror trasladado al guardia joven ("his own skin feel too small for the body wearing it") — describir la tortura por su efecto acústico en el pasillo es una decisión de primer nivel.
4. **Cap. 15, las celdas** — carga emocional por detalle concreto, no por adjetivo: "his tie still knotted with the particular care of someone who had dressed for an ordinary morning and never made it home"; "a school bag still looped over one slack shoulder".
5. **Cap. 22, la visión de la forja** — el giro sensorial del libro: tras 21 capítulos de gravedad, "sparks that laughed as they scattered". El contraste con la lanza ("the dark, judging blade") se hace por temperatura emocional de la imagen y funciona.
6. **Cap. 27, la flor** — "Color bled back into its petals in a slow, unhurried bloom, as though it had simply been waiting… He kept playing… and let the flower have its moment without an audience". Milagro sin fanfarria; caracteriza a Milo mejor que cualquier descripción directa.

---

## 3. Hallazgos por prioridad

### 🟠-1. Ancla sensorial repetida: "held breath" (10 usos, con duplicaciones internas y una fórmula calcada)

La imagen del aliento contenido es el ancla de silencio/quietud del tramo entero. Grep: **10 apariciones**, incluidas **dos veces dentro del mismo capítulo en tres capítulos distintos**:

- Cap. 06 §3 ("reserved, the way a single held breath is reserved") y §25 ("let loose into the wind the way a held breath is finally let go") — apertura y clímax del mismo capítulo con el mismo símil.
- Cap. 15 §5 ("a held-breath quality to the air itself") y §7 ("thin as a held breath") — **párrafos consecutivos**.
- Cap. 19 §27 ("silent in a manner that went past ordinary quiet into something closer to held breath") y §37 ("holding its breath around him on purpose").
- Y la fórmula **verbatim** en dos capítulos: cap. 08 §59 y cap. 17 §75 usan idéntico "let himself feel, for the length of exactly one held breath, …" (una vez para Mikel, otra para Gabriel — al calcarse, deja de ser motivo y pasa a ser plantilla).

**Por qué importa**: es exactamente el caso que codifica la norma de la casa ("no apoyarse en la misma imagen…; al repetir, variar la imagen, no solo la palabra"). El lector de corrido percibe el molde. **Clasificación**: debilidad narrativa. **Solución sugerida**: conservar 2–3 usos donde la imagen es estructural (cap. 06 puede quedarse uno; cap. 19 uno) y sustituir el resto por anclas de quietud distintas (presión, temperatura, ausencia de eco…). Romper sí o sí los pares intra-capítulo de 15 y 19 y una de las dos fórmulas 08/17.

### 🟠-2. Carencia: el olfato y el gusto desaparecen del libro después del cap. 02

Conteo de léxico olfativo/gustativo en los capítulos terrestres: cap. 01: 2 · cap. 02: 7 · cap. 07: 1 · **cap. 08: 0 · cap. 19: 0 · cap. 22: 0 · cap. 24: 0 · cap. 27: 0** · cap. 25: 2. En los planos no terrestres es cero casi absoluto (aceptable como estilización en Cielo; ver §5).

El caso más costoso es el **cap. 19 (Turein)**: una travesía en barca pesquera entre niebla y una isla — y no hay sal, ni pescado, ni madera húmeda, ni el olor del musgo del claro. El capítulo se sostiene en tacto (niebla "strangely warm", corteza tibia) y en silencio, que están muy bien, pero una isla que "carries the same texture as those dreams" ganaría muchísimo con un solo olor imposible o desplazado. Lo mismo, en menor grado, el archivo del cap. 08 (un fondo de estantería no digitalizado en el que nada huele a papel viejo, cuando el aula del cap. 01 sí olía) y el gimnasio-refugio del cap. 25 (comida, cuerpos, lejía: nada).

**Por qué importa**: `07_descripcion.md` señala este exacto error ("centrar todas las descripciones en la vista… las sensaciones más profundas llegan por los otros sentidos"). El tramo no depende *solo* de la vista — el tacto y el sonido-ausencia trabajan bien — pero la nariz del lector se apaga en el cap. 02 y no vuelve a encenderse. **Clasificación**: debilidad. **Solución**: una pasada quirúrgica de 1 olor/sabor por capítulo terrestre en 08, 19, 22, 24, 25, 27. No hace falta más.

### 🟠-3. Muletillas de frecuencia industrial (área 6, adjetivos/adverbios y fórmulas)

Conteos en el tramo (27 capítulos):

| Fórmula | Usos | Nota |
|---|---|---|
| "exactly" | 113 | pico cap. 13/14 |
| "simply" | 100 | pico cap. 13 (×9) |
| "never once" | 72 | pico cap. 12 y 24 (×5 c/u) |
| "patient / patience / patiently" | 71 | pico cap. 12 (×10) |
| "the particular [sustantivo] of…" | 56 | pico cap. 12 y 27 (×5 c/u) |
| "unhurried" | 38 | pico cap. 27 (×6), 13 (×4) |
| símil "the way a/an …" | 37+ | cierra párrafo tras párrafo |
| "considerably" | 28 | pico cap. 13 (×5) |
| "something closer to" | 26 | — |
| "longer than … could count/measure/place" | 19 | — |
| "not X, exactly" | 10 | — |

Individualmente, casi todas son voz legítima de la casa (la prosa piensa en aproximaciones y correcciones: "not pain, exactly"; "something closer to"). El problema es de **acumulación**: en el cap. 13, "simply"×9 + "actually"×9 + "exactly"×7 + "considerably"×5 en 2.700 palabras significa un adverbio modal cada ~90 palabras; y "patient/unhurried" se ha convertido en el adjetivo comodín de *todos* los personajes competentes (Arin, Orifiel, Laila, Barbas, Orobas, Lucifer, Sariel, Milo), lo que aplana una distinción de caracterización que el libro necesita. **Clasificación**: debilidad por acumulación; ninguna instancia aislada es error. **Solución**: pasada de poda con cuota (p. ej. máx. 2 "never once" y 2 "the particular" por capítulo), y reservar "unhurried/patient" como firma de 2–3 personajes (Orobas, Barbas, Milo) quitándoselo al resto.

### 🟠-4. Adverbios -ly: picos en 13, 14, 23 (clasificación)

Tasa por 1.000 palabras (grep, excluidos no-adverbios): media del tramo ~18,5. **Picos: cap. 13 y 14 (24,7), cap. 23 (23,4), cap. 21 (22,7)**. Mínimos: cap. 17 (12,7), cap. 16 (14,3).

Clasificación del pico del cap. 13 (top: simply×9, actually×9, exactly×7, considerably×5, rarely×4, entirely×4, precisely×3): casi ninguno es adverbio de modo redundante con el verbo (el vicio clásico); son **adverbios modales/discursivos de cobertura** — la prosa matiza dos veces lo ya matizado. En diálogo de Orobas son *necesarios/útiles* (su evasividad es el personaje: "I realize how it sounds"). En narración de Malphas son mayormente *prescindibles*: "he preferred it, if he were honest with himself" ya contiene lo que "simply/actually" repiten. El cap. 14 (exactly×6, finally×5, entirely×4) es Mikel en tensión: la mitad sobrevive a la praxis de "si la frase vive sin él, sobraba"; la otra mitad no. **Solución**: poda dirigida solo en 13, 14, 21, 23 — el resto del tramo está dentro de rango razonable para esta voz.

### 🟡-5. El cielo de "moretón" aparece en dos planos distintos

Cap. 01 usa dos veces el cielo-hematoma para el campo de batalla del sueño (§7 "something closer to a bruise deciding whether to heal"; §39 "a sky bruised the exact color of a wound…") — repetición **deliberada y eficaz** (visión diurna y sueño son la misma herida). Pero el cap. 20 §3 da a Hell exactamente la misma ancla: "a sky the color of an old bruise". El moretón era la firma del trauma de la Sundered Sky; prestárselo al cielo cotidiano del Infierno diluye la firma y empaña el contraste entre planos. **Clasificación**: oportunidad de mejora. **Solución**: recolorear el cielo del cap. 20 (ceniza, herrumbre, bilis — cualquier cosa que no sea hematoma).

### 🟡-6. El ancla del esternón se presta a personajes que no son los gemelos

"Behind his sternum" (7 usos) es el motivo-firma de la herida compartida Mikel/Arin (caps. 01, 02, 07, 14×2, 15) y ahí funciona de maravilla — es el hilo físico que insinúa que son la misma alma partida. Pero el cap. 12 §33 se lo da a un guardia demonio anónimo ("a small cold weight settle behind his own sternum") y el cap. 26 §47 al residuo de Sariel ("a cold, foreign pressure lifting from somewhere behind his sternum"). **Por qué importa**: cuando el lector aprende que "esternón = los gemelos", cada uso ajeno gasta la señal. **Solución**: en 12 y 26 basta "chest" o reubicar la sensación.

### 🟡-7. Repeticiones intra-capítulo menores

- Cap. 05: "having worn it herself more times than she cared to count" (§37) y "having worn something close to it herself more times than she cared to count" (§51) — misma fórmula, mismo capítulo, mismo personaje focal.
- Cap. 19 §55 / cap. 22 §57: "the ethnography still tucked against his ribs" → "the notebook still tucked against his ribs" — capítulos consecutivos de Mikel con el mismo gesto-ancla. 🔵 fácil de variar.

### 🟡-8. Cielo descrito casi solo con luz (caps. 03–05)

Tres capítulos consecutivos de Cielo se anclan casi en exclusiva en luz/brillo: cap. 03 "the light had come back wrong… the way a body holds a scar"; cap. 04 armaduras que atrapan o no la luz; cap. 05 el brillo de Tenura. La luz-como-herida del cap. 03 es una imagen excelente y la firma del plano es legítima (ver §5), pero en 03 el único sentido activo durante todo el consejo es la vista. El cap. 04 lo corrige solo (cuerno de alarma, patio "frost-stiff") y el 17 añade frío y aire fino al observatorio. **Clasificación**: al borde entre decisión estilística y oportunidad — si se toca, solo el cap. 03 (un sonido del cámara: eco, roce de armadura, el silencio posterior a Rafael ya está bien usado).

### ⚪-9. Ciudades terrestres deliberadamente anónimas (registrar, no corregir)

La ciudad muerta del cap. 02 ("The Ghost of the Balkans") no tiene ni nombre, ni idioma, ni señal balcánica concreta; los bares de 02 y 07 son "the kind of bar this city still had" / "a bar with no name on the door"; Arin atraviesa "a string of cities he was already beginning to lose track of" (07, 21, 25). Leído contra el mandato del tramo (entornos terrestres no genéricos), esto podría parecer carencia — pero el texto lo motiva: la anonimia es el estado interior de Arin, y el cap. 02 compensa con concreción sensorial de primera ("concrete dust and old rain", "mildew and old grain dust instead of concrete"). **Clasificación**: decisión estilística válida en lo sensorial; queda como ⚪ **solo** la nota de que el título promete "Balcanes" y el capítulo no entrega ningún marcador local — un único detalle (una palabra de idioma, una marca de cigarrillos, un alfabeto en un cartel caído) pagaría el título sin romper la anonimia temática. A criterio del autor.

---

## 4. Checklist del área (07_descripcion.md)

- **¿Aperturas de capítulo >2 párrafos sin que pase nada?** Solo el cap. 06 (tres párrafos de montaña/figura antes de "Two threads, tonight, pulled at him differently"). Es la pieza contemplativa del libro y el estatismo *es* el tema (la quietud de Metatrón); funciona — decisión estilística válida. Ningún otro capítulo incumple: el tramo teje descripción en movimiento de forma ejemplar (p. ej. cap. 19 revela la isla al ritmo de la caminata).
- **¿Bloques que paralizan tensión?** No. El bloque más largo (Grey City, cap. 07 §33–35) está dramatizado con micro-acción observada.
- **¿Acumulación de adjetivos?** No hay racimos de 3+; el patrón de la casa es el par coordinado ("patient and unhurried", "small and mean", "low and total"), correcto en dosis, pero el par "patient/unhurried" está gastado por frecuencia (ver 🟠-3).
- **¿Símiles encadenados en una frase?** No se encontró ninguna violación de la regla dura (dos símiles encadenados en la misma oración). El riesgo real es otro: la **analogía como cierre de párrafo** ("the way a…", "the same way…") aparece 37+ veces y en capítulos densos cierra párrafos casi consecutivos — cadena a escala de página, no de frase. Vale la misma poda con cuota de 🟠-3.

## 5. Contraste sensorial entre planos (mandato del tramo)

**Veredicto: perceptible y consistente.** Firmas efectivas:

| Plano | Paleta dominante | Ejemplos ancla |
|---|---|---|
| Tierra | polvo, zumbido eléctrico, hormigón, frío húmedo, luz gris/fluorescente | radiator dust (01), concrete dust (02), fluorescent hum (07), frost del aliento (24) |
| Cielo | luz (y su "estar mal"), oro, piedra, aire fino y frío | luz-cicatriz (03), frost-stiff yard (04), observatorio frío (17, 26) |
| Infierno | humo, presión psíquica, piedra caliente, din | sheet of smoke (10), libros que "pulsed with a faint, sourceless heat" (20), el din del Tower (20/23) |
| Cumbre | frío que "borra", viento, hebras/tejido | "the cold did not so much bite as erase" (06) |

Fugas menores que empañan el contraste: el moretón compartido (🟡-5) y el hecho de que "cold" es el ancla táctil de los cuatro planos (19 usos repartidos; picos en 18/19). No exige corrección global — pero si se retocan 20 y 26, diferenciar el frío infernal (húmedo, graso) del celestial (fino, limpio) saldría casi gratis. El cap. 20 es, además, el capítulo donde el Infierno por fin tiene calle, burócrata y sobornos — su mejor concreción; los interiores de 09/10/12/13 son más abstractos, sostenidos por interioridad, y funcionan como decisión (el Infierno de este libro es burocracia y atención, no fuego).

## 6. Claridad espacial en los capítulos de Arin (07, 15, 18, 25)

- **07**: sin combate; la aproximación (semáforos, cruce, torre al centro) es nítida. ✔
- **15**: la mejor geografía del tramo — pisos, escaleras que no figuran en plano, filas de celdas, y la elección final planteada espacialmente ("Taking the corridor meant… Reaching the cells instead meant…"). El lector siempre sabe dónde está cada cosa. ✔
- **18**: adecuada. Posiciones legibles (liberados a la espalda contra la pared, capitán circulando, la mujer alzada). La "unmaking" sin mecanismo visible es decisión estilística válida y coherente con 16. Un solo roce 🔵: en §3 la llegada del capitán se siente "closing from behind" y en §7 entra de frente "stepping over their fallen bodies" — un ajuste de una palabra fija la brújula.
- **25**: la persecución invertida (el hueco en la valla no previsto, el atajo por el patio de carga, el muelle sin salida) es el mejor beat de acción del tramo en términos espaciales: cada giro es mapeable. ✔

## 7. Registro por capítulo de anclas dominantes (para vigilar repetición consecutiva)

01 polvo/tiza-luz gris + hueco en pecho · 02 polvo de hormigón/moho + hueco (eco deliberado de 01) · 03 luz-mal · 04 luz/escarcha/cuerno · 05 brillo de Tenura (3.ª luz consecutiva → §3 🟡-8) · 06 frío-viento/hebras + held breath×2 · 07 fluorescente/gris/café · 08 archivo-luz de ventana (sin olor) · 09 pulso de la lanza + held breath · 10 humo · 11 armadura marcada/jaula parpadeante · 12 aguja/respiración/piedra pulida · 13 arcilla/piedra · 14 pavimento frío/hoja luminosa + esternón×2 · 15 presión de wards/celdas + held breath×2 + esternón · 16 asfalto agrietado/inmovilidad · 17 frío-aire fino + fórmula held breath (=08) · 18 corredor/luz interna · 19 niebla cálida/plata/anvil tibio + held breath×2 (sin olor de mar) · 20 moretón-cielo (=01)/din/calor de libros · 21 mapa estelar/veladura · 22 chispas-risa/inscripción (anvil tibio, continuidad correcta con 19) · 23 estudio silencioso/tinta vieja · 24 anochecer de campus/aliento visible · 25 gimnasio-zumbido/óxido · 26 observatorio/residuo frío + esternón (🟡-6) · 27 hierba/luz dorada/acorde.

Repetición consecutiva problemática: **06→09 y 15→17→19** (held breath), **03→04→05** (luz sola), **19→22** (tucked against his ribs; el anvil tibio en cambio es continuidad correcta). El eco 01→02 (hueco/ausencia con forma) es deliberado y es de lo mejor del libro.

## 8. Prioridades de corrección (en orden)

1. 🟠-1 Podar "held breath" a 2–3 usos; deshacer los pares intra-capítulo (06, 15, 19) y una de las fórmulas gemelas 08/17.
2. 🟠-2 Un olor/sabor por capítulo en 08, 19, 22, 24, 25, 27 (empezando por la travesía a Turein).
3. 🟠-3/4 Pasada de poda con cuota sobre las muletillas, concentrada en 13, 14, 21, 23; reasignar "patient/unhurried" como firma exclusiva de Orobas/Barbas/Milo.
4. 🟡-5/6 Recolorear el cielo del cap. 20 y devolver el esternón a los gemelos (12, 26).
5. 🟡-7/8 Micro-variaciones (cap. 05, 19/22) y un sonido en el consejo del cap. 03.

**Notas fuera de área** (para las pasadas correspondientes, no evaluadas aquí): cap. 17 §69–71 tiene dos parlamentos consecutivos de Gabriel sin réplica de Sariel entre medio ("Neither have I…" / "Then go carefully…") — revisar en la pasada de diálogos.

**Valoración del área (orientativa)**: Descripciones 7,5/10 · Inmersión 8/10. Las tres cosas que más subirían la calidad del tramo: variar el ancla del aliento contenido, devolverle la nariz al libro, y racionar los adverbios modales de los picos.
