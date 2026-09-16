# Diseño — slate de mini-subtramas para arcángeles y mandos de Libro I

**Fecha**: 2026-08-26
**Tipo**: diseño, solo-informe. **No se tocó prosa en ningún archivo.** No se crean capítulos nuevos ni se renumera nada — toda propuesta se inserta como escena(s) dentro de un archivo de capítulo ya existente (`Libro1/EN/NN_*.md` / `Libro1/ES/NN_*.md`), en un punto concreto de ese capítulo.
**Encargo**: el autor señala que arcángeles, señores infernales y mandos menores del Libro I no tienen introducción propia ni subtramas dentro de este libro, y pide mini-historias — algunas enlazadas a la trama principal, otras anécdotas autoconclusivas — para Gabriel, Uriel, Rafael, Camael, Zadkiel, Iofiel, Sariel, Foras, Vem/Thoria (si les falta algo) y 1-2 comandantes menores.

---

## 0. Lo que ya existe — verificación contra el material de generación (obligatoria antes de diseñar)

`content/lore/archive/fase_generacion/book1_new_subplots_candidates.md` y `book1_new_subplots_beats.md` (2026-08-08/09) ya diseñaron **5 subtramas completas** para Libro I, con capitanes/líderes de escuadra (no arcángeles): Vual/Sariel/Corin (reencarnación), Isla de Turein (Cassiel/Selm), Necrópolis (Kurel/Daith), Hollowseam (Vem/Thoria), Foras vs. Vepar (Malthus/Stolas). Cotejé cada una contra la prosa actual (`Libro1/EN/22-39`, confirmado idéntico en número/orden en `Libro1/ES`) capítulo por capítulo:

| Trama | Diseñada | Implementada | Estado |
|---|---|---|---|
| **Vual** (Sariel/Vual/Corin) | 5 caps. (V1-V5) | **Cap. 22-26, las 5** | ✅ completa |
| **Hollowseam** (Vem/Thoria) | 4 caps. (H1-H4) | **Cap. 36-39, las 4** | ✅ completa |
| **Turein** (Cassiel/Selm) | 4 caps. (T1-T4) | Cap. 30 (T1), 31 (T2), 32 (T4) | 🟡 falta T3 ("Los acertijos sin respuesta" — el capítulo de la mecánica del acertijo dramatizada) |
| **Necrópolis** (Kurel/Daith) | 3 caps. (N1-N3) | Cap. 28 (N1), 29 (N3) | 🟡 falta N2 ("La discrepancia" — la escalada física del choque metodológico; ch. 29 la resume en retrospectiva: *"the argument that had carried into a second full day without resolution"*, nunca dramatizada) |
| **Foras vs. Vepar** (Malthus/Stolas) | 3 caps. (F1-F3) | Cap. 33 (F1), 34 (F3) | 🟡 falta F2 ("Lo que la marea husmea" — la escena de espionaje de Stolas, con diálogo ya escrito en el propio doc de beats) |

**Conclusión operativa**: Sariel y Vem/Thoria **no necesitan trama nueva** — ya tienen arco completo y bien cerrado (confirmado también por `design_notes/2026-08-22_coherence_libroI_menores.md`, que verifica Hollowseam y Turein como internamente coherentes). Foras sí tiene un hueco real y barato de cerrar: el capítulo F2 ya está escrito en el doc de generación, solo nunca se insertó — es la propuesta #7 de este documento, no una trama nueva.

Lo que el encargo del autor señala con precisión: **ningún arcángel (Gabriel, Uriel, Rafael, Camael, Zadkiel) ni Iofiel tiene una mini-historia propia** — aparecen exclusivamente en capítulos de consejo/mando coral. Verificado por grep de nombre propio sobre `Libro1/EN/*.md`:

| Personaje | Capítulos donde aparece en L1 | Naturaleza de la aparición |
|---|---|---|
| Gabriel | 1,3,4,8,12,14,17,21,27,28,29,32,35,40,41,44,46,49,51 | Siempre coral (consejo, mando) |
| Uriel | 1,3,4,5,8,12,17,27,44,46,49,51 | Siempre coral |
| Rafael | 3,5,8,14,17,27,46,49,50,51 | Siempre coral/de fondo |
| Camael | 4,7,11,24,45,51 | Coral + **una escena real** con Jeremiel en cap. 11, pagada en cap. 45 y 51 |
| Zadkiel | 17,27,51 | Coral puro — 3 apariciones en todo el libro |
| Iofiel | 17,21,28,29,32,40,41,44,51 | Coral + trabajo de archivo (Necrópolis), sin POV propio |

Esto confirma el diagnóstico del autor con datos: hay material de personaje (fichas ricas, `content/lore/personajes.md`) que la prosa nunca activa en escena propia. Las propuestas 1-6, 8 y 9 de abajo llenan exactamente ese hueco, **insertando siempre dentro de capítulos donde el personaje ya aparece** — no se inventa ninguna aparición nueva de bando ni de mando.

### Nota sobre el clímax en reescritura (caps. 42-51)

Contrastado con `design_notes/2026-08-26_audit_duelo_lucifer.md`. Ninguna propuesta de este documento toca los capítulos 46-48 (el duelo Miguel/Lucifer en sí) ni el 49 (rechazo de Solmire). Las inserciones que sí caen en el tramo del clímax (caps. 44, 45, 46) se colocan exclusivamente en bloques que ese informe ya marca 🟢 **queda igual** bajo el rediseño (cap. 45 completo — no tiene POV de Belial ni Lucifer; la escena de infirmería de Rafael en cap. 46, que es anterior y ajena al cierre del capítulo que sí se reasigna). Es decir: estas propuestas son compatibles con el duelo tal como estaba *y* con el duelo reescrito, sin depender de qué decisión tome el autor sobre ese punto.

---

## 1. Slate de propuestas

### ⭐ 1. Camael y Jeremiel — el luto construido antes de la pérdida
**Personajes**: Camael, Jeremiel (Captain, *Morale & Tactics*, bajo Camael) · **Categoría**: enlazada

**Por qué**: el cap. 45 (*The Despairing Front*) ya mata a Jeremiel — es la primera víctima visible de la ola de desesperanza de Lamentum, y el cap. 51 ya dramatiza el duelo de Camael (afila la espada de Jeremiel, "the twelfth piece, and the one he had saved for last"). El vínculo tiene un solo asiento previo real en toda la obra: una escena de cuatro párrafos en el cap. 11 (*Crossings*). Es exactamente lo que pide el autor — el material existe, pero no está *construido*, así que el golpe del cap. 45 llega sin la carga que podría tener.

**Escenas concretas** (2, dentro de capítulos ya existentes):
1. **Cap. 11 (*Crossings*), ampliación de la escena ya existente** (línea ~15-19 del capítulo, inmediatamente después de "*It's been wrong for a while now... Today's just the first time it got loud enough to notice.*"): un beat adicional donde Jeremiel, en vez de solo callar, responde con algo concreto de sí mismo — una razón personal por la que sigue confiando en Camael pese al silencio, o un detalle de su método (cómo lee la moral de la tropa) que Camael no conocía. Convierte la "confianza táctica" ya escrita en algo más personal, sin tocar ni una línea del diálogo existente. ~250-300 palabras.
2. **Cap. 45 (*The Despairing Front*), beat nuevo insertado ANTES del párrafo inicial actual** (antes de "Camael held the center of the line..."): una escena breve, la noche anterior o los minutos previos a que la línea se forme — Jeremiel le devuelve o le muestra a Camael algo pequeño y concreto (una costumbre compartida, un objeto, una promesa a medio bromear) que el lector reconocerá después, cuando Camael afile esa misma espada en el cap. 51. No cambia ni una palabra del texto actual del capítulo — se coloca delante. ~300-350 palabras.

**Riesgos de canon**: ninguno — Jeremiel ya muere en este capítulo en la prosa actual; esto no cambia el hecho, solo lo antecede. No interfiere con el rediseño del duelo (cap. 45 está marcado 🟢 intacto en la auditoría del clímax).

**Carga estimada**: ~550-650 palabras totales.

---

### ⭐ 2. Zadkiel — la grieta que mide sin saber qué está midiendo
**Personajes**: Zadkiel, Iofiel (testigo) · **Categoría**: enlazada

**Por qué**: en el cap. 51, Zadkiel entra con un manuscrito quemado bajo el brazo y dice, sin preámbulo: *"The cycle isn't broken... But it's bent further than I've ever measured it. I don't know what it costs to bend it back."* Es la línea de mayor peso temático que Zadkiel pronuncia en toda la trilogía (confirmado por `design_notes/2026-08-22_coherence_zadkiel.md`: la promesa queda huérfana en L2/L3, un problema de libros posteriores que este documento no puede resolver, pero sí puede *cargarla* mejor en origen). Hoy esa línea llega de la nada — Zadkiel solo tiene 3 apariciones en todo el libro, todas corales. Dar a Zadkiel una pauta de medición ya en marcha antes del cap. 51 hace que esa línea aterrice como el final de un arco, no como una ocurrencia.

**Escenas concretas** (2):
1. **Cap. 17 (*What the Council Won't Decide*), beat nuevo insertado justo después de que Zadkiel rompe el punto muerto** (después de "*Bring me a location, and I will bring you soldiers... I will not spend them on a translation, however careful the translator.*"): mientras el resto del consejo se dispersa, Zadkiel se queda un momento más de lo esperado con Iofiel, y le pide, aparte, un dato administrativo concreto y aparentemente menor — cuántas almas han "vuelto" (reencarnado) en el último ciclo de reportes, comparado con el ciclo anterior. Iofiel se lo da sin entender por qué lo pregunta. Cierre en la incomodidad de Zadkiel archivando el número sin comentario. ~200-250 palabras.
2. **Cap. 27 (*A Fissure in the Light*), beat nuevo insertado tras el anuncio de que Belial tiene Lamentum**: Zadkiel, en un margen de la misma reunión, cruza una mirada breve con Iofiel — la cifra del cap. 17 y esta noticia no encajan del modo en que él esperaba que no encajaran. Una frase suya, seca y sin explicar del todo, sobre que el margen de error que él mismo se permite medir "se ha reducido más rápido este año que en los últimos cien". Nadie más en la sala lo registra como relevante. ~250-300 palabras.

**Riesgos de canon**: **alto cuidado, bajo riesgo real si se respeta la restricción**. H13 del grafo de conocimiento fija que "Thamorak" es nombre exclusivo del Libro III y que "Belial, la tropa y los mortales nunca lo conocen" — Zadkiel no debe, bajo ninguna circunstancia, acercarse a nombrar una causa. La propuesta se mantiene deliberadamente en el registro puramente estadístico/institucional (cifras de reencarnación, márgenes de error) sin ninguna hipótesis de causa — el mismo registro que ya usa el cap. 51 real ("I don't know what it costs"). No contradice H27 (la medición de Zadkiel del ciclo doblado, ya canónica desde el cap. 51) — la refuerza dándole una curva de datos previa en vez de una declaración aislada.

**Carga estimada**: ~450-550 palabras totales.

---

### 3. Iofiel — el peso de lo que archiva sellado
**Personajes**: Iofiel · **Categoría**: enlazada

**Por qué**: Iofiel es la Capitana de Zadkiel y la que recibe tanto el himno redactado de la Necrópolis (cap. 29, ya en prosa) como, más adelante, la profecía de las tres armas (cap. 40-41). Hoy no tiene ni una sola línea de interioridad propia sobre lo que archiva — solo actúa como receptora. Esta propuesta le da una hebra propia de "guardiana que empieza a notar el peso de lo que calla", en paralelo (sin cruzarse en página) con la de Zadkiel arriba — ambas comparten la misma capitana como testigo, reforzando el mando Zadkiel→Iofiel sin que ninguna escena lo declare explícitamente.

**Escenas concretas** (2):
1. **Cap. 29 (*What Remains Unnamed*), beat añadido al final del capítulo**, después de que Kurel y Daith entregan la versión con la estrofa marcada "illegible": Iofiel, a solas, archivando el informe, se permite un momento de duda profesional — no sobre si Kurel mintió (no lo sabe, y esta escena no se lo revela: H23 del grafo exige que solo Kurel y Daith sepan que fue deliberado), sino sobre cuántos informes de su archivo llevan la misma palabra, "illegible", y si alguna vez alguien vuelve a abrirlos. Cierre sin resolución. ~250-300 palabras.
2. **Cap. 40 (*Three Were Forged*), beat insertado mientras Iofiel trabaja con los fragmentos del Codex** (ella ya es la POV de apertura de este capítulo): un breve recuerdo lateral, no verbalizado a nadie, de la estrofa de la Necrópolis — la misma sensación de sostener una verdad a medias entre las manos. No se nombra Thamorak ni se conecta explícitamente; es textura de personaje, un eco, no una revelación. ~200-250 palabras.

**Riesgos de canon**: bajo. Cuidado explícito de no romper H23 (Iofiel no debe aprender ni sospechar que la redacción fue deliberada) ni H13 (sin nombrar nada). Es compatible con, y de hecho mejora, el material que la auditoría de coherencia (`2026-08-22_coherence_libroI_menores.md`) ya señala como una promesa que en L3 queda huérfana — esta propuesta no la cierra (eso es trabajo de L3, fuera de alcance), pero le da más asiento en origen, lo cual solo ayuda a quien eventualmente decida pagarla.

**Carga estimada**: ~450-550 palabras totales.

---

### ⭐ 4. Gabriel — el sello que nunca rompe
**Personajes**: Gabriel · **Categoría**: enlazada

**Por qué**: en los caps. 1 y 12, Gabriel porta un pergamino sellado del Consejo — una autorización para actuar contra Miguel — que no vuelve a mencionarse en ningún capítulo posterior de todo Libro I (confirmado por `design_notes/2026-08-22_coherence_gabriel.md`, que lo marca como "detalle de caracterización... que simplemente queda sin retomar", no un error). Es el prop de Chéjov más claro de toda la ficha de Gabriel sin usar. Pagarlo *dentro* de Libro I —sin abrir el sello, solo mostrando la tentación y la elección de no usarlo— le da a Gabriel una escena de decisión propia, en el momento de mayor tensión posible: justo cuando el Infierno se hace con Lamentum y él, de facto, es la autoridad más alta presente.

**Escena concreta** (1):
1. **Cap. 27 (*A Fissure in la Luz*), beat insertado dentro de la reunión del Consejo**, en el tramo donde Gabriel procesa la noticia de que Belial tiene Lamentum (el capítulo ya es su POV — cita real: *"Gabriel had called the Council within hours of the scout's return..."*): en un momento de silencio de la sala, Gabriel toca, sin sacarlo, el pergamino sellado que lleva desde el cap. 1 — la autorización que le permitiría tomar el mando militar por encima de Miguel si lo invocara ahora, con Miguel ilocalizable y la amenaza real. Lo considera. No lo rompe. La escena no explica por qué (el contenido del pergamino sigue sin revelarse — no se inventa lore nuevo), solo muestra el peso de cargar una autoridad que se niega a usar incluso cuando tendría la excusa perfecta. ~300-350 palabras.

**Riesgos de canon**: mínimo. No se abre el sello ni se revela contenido — se preserva exactamente el misterio que la auditoría de coherencia ya documentó como intacto. No contradice nada de L2/L3 (el pergamino no vuelve a mencionarse en ningún libro posterior tampoco, así que no hay continuidad que romper).

**Carga estimada**: ~300-350 palabras.

---

### ⭐ 5. Uriel y Camael — la apuesta que nadie cobra
**Personajes**: Uriel, Camael · **Categoría**: anécdota

**Por qué**: pedido explícito del autor ("una apuesta entre Uriel y Camael"). El cap. 4 (*The First Swing*) ya tiene el material perfecto para construirla encima sin inventar nada: Camael aposta con un soldado joven que Miguel "fumbles" la espada nueva, pierde la apuesta, y el capítulo ya nota explícitamente la dinámica Uriel/Camael en el consejo que sigue (Camael observando la "ausencia total de fricción" en el sí inmediato de Uriel al plan de ataque). Extender la apuesta a Uriel mismo — y dejarla, a propósito, sin cobrar — es una anécdota autocontenida que además ilumina (sin explicarla) la lectura que Camael ya hace de Uriel en la escena siguiente del mismo capítulo.

**Escena concreta** (1):
1. **Cap. 4, beat insertado entre el regreso de Camael del Overlook y la entrada a la sala de guerra** (el propio texto ya marca esa transición: *"the war room felt different with Solmire present..."*): Uriel intercepta a Camael en el pasillo, ya ha oído del wager perdido, y propone el suyo propio — más grande, más seguro de sí mismo, típico de su temperamento impulsivo ("brave, forthright" según su ficha) — sobre cuánto durará la ofensiva a Zaphor'el. Camael, todavía escaldado por perder el primero, lo acepta con menos entusiasmo. Ninguno de los dos vuelve a mencionarlo — la anécdota se cierra sola, sin resolución, exactamente en el registro de "cosas que Camael archiva y no dice en voz alta" que el propio capítulo ya establece como su patrón. ~300-350 palabras.

**Riesgos de canon**: ninguno — no introduce hechos, arma nueva, ni cambia el resultado de Zaphor'el (que la prosa posterior no vuelve a detallar en cifras). Coherente con la ficha de ambos (Camael: "impaciente con el lenguaje cuidadoso"; Uriel: "impulsivo, valiente, directo").

**Carga estimada**: ~300-350 palabras.

---

### ⭐ 6. Rafael y el soldado que no quiere ser sanado
**Personajes**: Rafael, un soldado sin nombre de las filas de Camael (el Unbroken) · **Categoría**: anécdota (con eco enlazado a la propuesta #1)

**Por qué**: pedido explícito del autor. El cap. 46 (*The Sundered Sky*) ya tiene la escena perfecta ya escrita para insertarlo dentro: Rafael trabajando sin pausa en una enfermería improvisada, tratando precisamente a los soldados golpeados por la misma ola de desesperanza que mató a Jeremiel un capítulo antes (cap. 45). Insertar aquí a un soldado concreto que se resiste activamente a ser sanado —porque soltar el dolor se siente como soltar al amigo que acaba de perder— es una anécdota autoconclusiva que, de regalo, resuena con la propuesta #1 sin necesitar que ninguna escena lo declare.

**Escena concreta** (1):
1. **Cap. 46, beat insertado dentro del párrafo ya existente de la enfermería** (justo después de "*It was slow work... he gave it the same patient attention regardless*"): Rafael llega a un soldado que aparta a Veritas con la mano, no por miedo ni por daño físico, sino porque no está listo para que el vacío deje de doler — nombra, de pasada, a alguien que perdió esa misma noche (sin necesidad de nombrar a Jeremiel explícitamente: puede ser "uno de los suyos", dejando la conexión abierta al lector sin forzarla). Rafael, fiel a su ficha ("cree que toda alma puede redimirse — pero nunca a ciegas"), no insiste. Se queda un momento, en silencio, y pasa al siguiente. ~300-350 palabras.

**Riesgos de canon**: ninguno. No cambia el resultado de la batalla ni introduce personajes con nombre que deban rastrearse en libros posteriores (el soldado es intencionalmente anónimo, evitando cualquier "cabo suelto" nuevo del tipo que las auditorías de coherencia ya han señalado en otros interludios). Cae dentro del bloque del cap. 46 marcado 🟢 en la auditoría del duelo (la escena de la enfermería es anterior y ajena al cierre reasignado a Lucifer).

**Carga estimada**: ~300-350 palabras.

---

### 7. Foras / Vepar — completar F2 ("Lo que la marea husmea")
**Personajes**: Vepar, Stolas, Malthus (mención) · **Categoría**: enlazada (cierra un hueco real de una trama ya aprobada)

**Por qué**: no es una trama nueva — es la pieza que falta de la trama Foras-vs-Vepar ya diseñada y aprobada en `book1_new_subplots_beats.md` (Trama 5), con diálogo ya escrito, nunca insertada en prosa. Hoy el cap. 33 (F1, Malthus) salta directo al cap. 34 (F3, la confrontación) sin que el lector vea a Stolas hacer el trabajo de espionaje que motiva esa confrontación — el propio cap. 34 ya lo asume ("Malthus found Stolas exactly where his own informants had placed him") sin haberlo mostrado.

**Escenas concretas** (2, usando el material ya aprobado del doc de generación):
1. **Cap. 33 (*The Price of Absence*), beat añadido al final del capítulo** (después del cierre actual, "la resolución de Malthus de actuar antes de que Stolas avance más"): la escena F2 beat 2 ya escrita — Vepar da la orden a Stolas en persona (*"Foras está débil, y la debilidad es solo otro fluido esperando encontrar su nivel... Ve y averigua exactamente cuánto ha bajado la marea."*). ~300-350 palabras.
2. **Cap. 34 (*A War Nobody Declares*), beat insertado ANTES del párrafo inicial actual** (antes de "Malthus found Stolas exactly where..."): Stolas usando *Umbra Manus* para desenterrar el secreto concreto sobre las posesiones de Foras (F2 beats 3-6 del doc de generación), cerrando con su reporte de vuelta a Vepar — que es, literalmente, lo que el capítulo actual ya presupone que acaba de pasar. ~350-400 palabras.

**Riesgos de canon**: ninguno — es material ya validado por el propio proceso de generación del libro, solo pendiente de inserción.

**Carga estimada**: ~650-750 palabras totales.

---

### 8. La corte de Foras — un problema absurdo (anécdota)
**Personajes**: un demonio menor de la corte de Foras (candidato: **Nocthel**, *Squad Leader / Herald of Summoning* bajo Raum→Foras — "trata cada batalla como ceremonia", voz haughty/teatral) · **Categoría**: anécdota

**Por qué**: pedido explícito del autor. Da textura cómica y de mundo a la corte de Foras sin tocar la política seria de Malthus/Stolas — funciona mejor como contraste de tono justo antes de esa seriedad.

**Escena concreta** (1):
1. **Cap. 33, beat insertado al INICIO del capítulo, antes de la línea actual "Malthus felt the shift in Hell's court..."**: Nocthel intenta convocar una entidad menor con una ceremonia de trompeta excesivamente elaborada frente a una audiencia de reclutas — y la entidad que responde no es en absoluto la que esperaba, resultando en un incidente menor y vergonzoso que la corte comenta entre risas contenidas durante días. Malthus, de fondo, lo nota con medio ojo mientras camina hacia su propia escena — el contraste (política mortal vs. absurdo burocrático) es el chiste. ~250-300 palabras.

**Riesgos de canon**: ninguno — personaje ya fichado, sin arco previo que romper, no introduce hechos de trama.

**Carga estimada**: ~250-300 palabras.

---

### 9. Remiel — las visiones que se niegan a coincidir (comandante menor)
**Personajes**: Remiel (Captain, *Prophetic Recon*, bajo Camael) · **Categoría**: enlazada, ligera

**Por qué**: Remiel ya es, sin que ningún diseño lo haya planeado, el personaje con más apariciones "fantasma" del libro — tres escenas (cap. 4, 12, 51), todas de una sola frase, todas mostrándola observar sin actuar ("tracing futures that keep refusing to agree with each other"). Es la candidata más barata de todo este slate: no hace falta insertar nada nuevo estructuralmente, solo profundizar dos de sus tres apariciones ya existentes para que se lean como arco, no como decoración repetida.

**Escenas concretas** (2, ampliación de material ya existente):
1. **Cap. 12 (*A Silence in Heaven*), ampliación del párrafo ya existente** (la propia escena ya es su POV — "*Remiel stood near the edge of the war room... The Spiral of Prophecy stayed dim and quiet at her side*"): un beat adicional inmediatamente después, donde el Espiral por una vez SÍ le muestra algo — pero tres futuros distintos y contradictorios a la vez, ninguno más claro que otro, y ella no tiene con quién compartir una visión que ni ella misma puede leer con certeza. Frustración profesional concreta, no misticismo vago. ~250-300 palabras.
2. **Cap. 51, ampliación de la línea ya existente** ("*Remiel watched her own shadow flicker against the wall, tracing futures that keep refusing to agree with each other*"): una frase o dos más, cerrando el eco directo con el cap. 12 — los mismos futuros contradictorios que vio entonces, todavía sin resolverse ahora que la batalla ya pasó, dejando claro para el lector atento que su don no le está fallando: el futuro mismo, tras la caída de Miguel, sigue genuinamente indeciso. ~150 palabras.

**Riesgos de canon**: ninguno — no revela ningún futuro concreto (evita cualquier profecía verificable que control de canon en L2/L3 tendría que honrar o contradecir); se mantiene deliberadamente en la ambigüedad que ya define su ficha ("cryptic, wise, speaks in layered truths").

**Carga estimada**: ~400-450 palabras totales.

---

## 2. Notas sobre Sariel y Vem/Thoria (por qué no llevan propuesta nueva)

- **Sariel**: arco completo de 5 capítulos ya implementado (Trama Vual, cap. 22-26) — el más desarrollado de todo Libro I fuera de la trama principal. Darle más aquí sería sobrecargar a un personaje que ya tiene el mini-arco mejor pagado del libro.
- **Vem/Thoria**: arco completo de 4 capítulos ya implementado (Hollowseam, cap. 36-39), confirmado internamente coherente por auditoría previa. Mismo razonamiento — no falta nada real.

Si el autor de todos modos quiere una gota más para cualquiera de los dos, la opción más barata y de menor riesgo sería una sola línea de callback en cap. 51 (donde ya hay una escena coral de posguerra) reconociendo de pasada que ninguno de los dos ha vuelto a mencionar en público lo que pasó en la fisura — no requiere escena nueva, solo una frase.

---

## 3. Resumen y recomendación

| # | Subtrama | Categoría | Caps. afectados | Escenas | Palabras aprox. | Recomendada |
|---|---|---|---|---|---|---|
| 1 | Camael/Jeremiel | Enlazada | 11, 45 | 2 | 550-650 | ⭐ |
| 2 | Zadkiel — deriva doctrinal | Enlazada | 17, 27 | 2 | 450-550 | ⭐ |
| 3 | Iofiel — el peso del archivo | Enlazada | 29, 40 | 2 | 450-550 | |
| 4 | Gabriel — el sello que no rompe | Enlazada | 27 | 1 | 300-350 | ⭐ |
| 5 | Uriel/Camael — la apuesta | Anécdota | 4 | 1 | 300-350 | ⭐ |
| 6 | Rafael — el soldado que no sana | Anécdota | 46 | 1 | 300-350 | ⭐ |
| 7 | Foras/Vepar — completar F2 | Enlazada (ya aprobada) | 33, 34 | 2 | 650-750 | |
| 8 | Corte de Foras — anécdota absurda | Anécdota | 33 | 1 | 250-300 | |
| 9 | Remiel — visiones que no coinciden | Enlazada, ligera | 12, 51 | 2 | 400-450 | |

**Total si se hacen las 9**: ~3.650-4.250 palabras nuevas repartidas en 10 capítulos (4, 11, 12, 17, 27, 29, 33, 34, 40, 45, 46, 51 — 12 capítulos, ninguno tocado más de dos veces), cero capítulos nuevos, cero renumeración.

**Las 5 recomendadas para empezar corto** (marcadas ⭐ arriba: Camael/Jeremiel, Zadkiel, Gabriel, Uriel/Camael, Rafael) cubren los cinco casos de mayor prioridad — los cuatro arcángeles/mandos con cero mini-historia propia hoy (Camael, Zadkiel, Gabriel, Rafael) más una anécdota pura (Uriel) — con el menor riesgo de canon de todo el slate (ninguna de las 5 toca hechos del grafo de conocimiento, ninguna introduce personajes nuevos con nombre, y las tres que caen en el tramo del clímax en reescritura están en bloques ya confirmados 🟢 intactos). Juntas suman ~1.900-2.250 palabras — un día razonable de escritura, con el mayor impacto emocional del lote (el hilo Camael/Jeremiel es, con diferencia, el que más responde a la queja original del autor).

Las 4 restantes (Iofiel, Foras F2, corte de Foras, Remiel) quedan listas para una segunda pasada — la #7 (Foras F2) es la más barata de todas si se prioriza por esfuerzo, porque el diálogo ya está escrito y aprobado desde 2026-08-09.
