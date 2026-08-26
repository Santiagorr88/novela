# Auditoría solo-informe — Canon de Solmire: portador vs. dueño de origen

**Fecha**: 2026-08-26
**Encargo**: corrección de canon del autor — *"La espada nunca fue de Miguel; su verdadero portador era Ereloth. Miguel lo que ocurre es que siente su presencia, o que Solmire lo está llamando."* Auditoría de solo lectura (no se tocó prosa).
**Método**: `grep` de `Solmire` en `Libro1/EN`, `Libro1/ES`, `Libro2/EN`, `Libro2/ES`, `Libro3/EN`, `Libro3/ES` (45 menciones EN, 45 ES, conteo idéntico), con contexto de 3-5 párrafos alrededor de cada una, más lectura completa de las escenas con peso dramático. Contrastado contra el trabajo previo ya existente en `design_notes/2026-08-22_coherence_ereloth.md`, `2026-08-22_coherence_tres_armas.md` y `2026-08-22_kg1_armas.md`, que ya habían mapeado la cadena de revelación Ereloth→Solmire capítulo por capítulo (ver sección 3).

**Cobertura**: Libro1 EN/ES caps. 01, 02, 03, 04, 05, 06, 08, 09, 10, 11, 12, 14, 21, 27, 30, 32, 35, 40, 41, 44, 47, 48, 49, 51 + `_index`. Libro2 EN/ES caps. 03, 09, 45. Libro3 EN/ES caps. 04, 06, 07, 14, 15, 16, 21, 22, 39, 40, 52. Estos son los únicos capítulos donde "Solmire" aparece nombrada en el texto aprobado — barrido exhaustivo, no muestreo.

---

## 1. Veredicto general

El canon nuevo **ya está mayormente sembrado en la prosa existente**. La gran mayoría de las 45 menciones de Solmire son compatibles sin tocar una palabra — de hecho varias escenas (L1/11, L1/32, L1/47-48, L3/06-07, L3/15-16) ya narran exactamente la tensión "¿es mía o me eligió?" que pide el encargo, con una calidad literaria notable. Solo **una** frase es un problema de voz narrativa/de tercero (no de Miguel) que afirma propiedad de origen como hecho establecido, y dos frases más son percepción subjetiva legítima de Miguel que puede quedarse tal cual — aunque una de ellas es la mejor candidata para un callback explícito en Libro III.

---

## 2. Tabla de conflictivas

| # | Cap. | Cita exacta (EN) | Cita exacta (ES) | Voz | Veredicto | Propuesta mínima |
|---|---|---|---|---|---|---|
| **C1** | L1/51 *The Echo of the Sword* | "None of us were meant to. **It answered to him and to no one else** — you saw what it did to lesser hands in the old records." (Iofiel) | "Ninguno de nosotros estaba destinado a hacerlo. **Le respondía a él y a nadie más**; ya vieron lo que les hizo a manos menores en los registros antiguos." | **Narrador-adyacente / tercero** (Iofiel, archivista del Codex, hablando en tono de hecho establecido, no de opinión) | **NECESITA RETOQUE.** Es la única línea de todo el barrido que afirma la exclusividad/permanencia del vínculo como dato objetivo desde la boca de un personaje distinto de Miguel, sin ninguna cobertura de "por elección". Encaja mal con "portador elegido, no dueño de origen": tal como está, suena a vínculo *de origen*, no a vínculo *de elección para esta era*. | Cambiar de lenguaje de permanencia/exclusividad a lenguaje de elección: **EN**: *"It answered to whoever it had chosen to carry it, and to no one else — you saw what it did to hands it hadn't chosen, in the old records."* **ES**: *"Le respondía a quien había elegido para llevarla, y a nadie más; ya vieron lo que les hizo a las manos que no había elegido, en los registros antiguos."* Conserva la función de la escena (nadie más puede cargarla con seguridad) pero desplaza el énfasis de "es suya por naturaleza" a "ella decide a quién elige" — coherente con Ereloth como forjador y Miguel como portador de esta era. Cambio de una frase, cero impacto en trama.|
| **C2** | L1/01 *A Wound in the World* | Párrafo 3 (antes del hallazgo): *"An ache with no name... a hollow in the center of his chest, where something had been taken from him."* Y en el hallazgo: *"He thought, with absolute and terrifying recognition: that is what was taken from me."* | *"Un hueco en el centro del pecho, donde algo le había sido arrebatado... ¿qué me fue arrebatado?"* / *"Pensó, con un reconocimiento absoluto y aterrador: eso es lo que me fue arrebatado."* | **Percepción subjetiva de Miguel**, marcada explícitamente ("he thought"/"pensó") | **PUEDE QUEDARSE COMO PERCEPCIÓN.** Es la escena fundacional del libro (página 1), pero está filtrada por completo por el punto de vista de Miguel — es su interpretación errónea de una sensación real (el tirón/llamada de la espada), no una afirmación del narrador omnisciente. De hecho, esta lectura errada ("me fue arrebatado" = robo) frente a la lectura correcta que el libro III construye ("me está llamando") es ironía dramática legítima y ya funciona en paralelo con el patrón que `2026-08-22_kg1_armas.md` documenta para el error de Iofiel en L1/43 (observación O5: error de época, protegido explícitamente para no destruir la ironía). **No se recomienda tocar el texto.** Si el autor quisiera un ancla más explícita, la opción más barata sería un único adjetivo cambiando "algo le había sido arrebatado" por algo que deje asomar la ambigüedad (p. ej. "algo lo llamaba, o le había sido arrebatado — no sabía distinguirlo"), pero no es necesario: el "hueco" y el "zumbido" ya son, en toda la trilogía, literalmente la sensación de la llamada de Solmire, y esta escena es la primera vez que Miguel la siente, simplemente sin saber todavía leerla bien. |
| **C3** | L1/41 *A Truth Offered* | *"I wasn't chosen," he said, louder now... "I wasn't chosen for anything. I was just the first fool who happened to be standing close enough to pick her up."* | *"—No fui elegido —dijo, más alto ahora... no fui elegido para nada. Fui simplemente el primer necio que resultó estar lo bastante cerca para recogerla."* | **Diálogo de Miguel**, en colapso emocional tras la revelación de la profecía | **PUEDE QUEDARSE COMO PERCEPCIÓN** — es exactamente el tipo de creencia subjetiva-en-crisis que el encargo autoriza a dejar intacta, y funciona dramáticamente (es el punto más bajo del arco de Miguel en L1). Nadie en la escena lo corrige; Gabriel oye "un llamado" donde Miguel oyó "pequeñez" — la propia prosa ya deja la puerta abierta a que Miguel esté equivocado, sin forzar una corrección prematura. **Pero es la mejor candidata de toda la trilogía para un callback correctivo explícito en Libro III** — ver sección 3, propuesta de revelación en L3/04. No tocar aquí; resolver hacia adelante. |

**Nota sobre lo que NO se encontró**: no hay ninguna frase de la forma "his sword" / "recuperar lo suyo" / "reclaim what was his" ligada a Solmire en el resto del corpus (sí existe, para otra arma, en L3/19: *"I'm not leaving without what belongs to me"* — pero es Thaeriel hablando de Lamentum, que **de hecho es** su arma de origen, así que ahí la frase es correcta y fuera del alcance de este encargo). Tampoco se encontró ninguna instancia de Miguel o de otro personaje afirmando en diálogo que Solmire fue forjada *para* él o *por* él.

**Observación menor fuera de alcance (propiedad, no origen)**: dos pasajes (L1/27 línea 17, L1/35 línea 45) usan la frase *"since the sword's forging"* / *"desde la forja de la espada"* como hito temporal en la vida de Miguel, lo cual —leído muy literalmente— sugeriría que la forja ocurrió cerca de cuando Miguel la encontró, en tensión con "forjada antes del Verbo Divino" (L1/41, L1/44). Es probablemente un uso coloquial de "forjar" en el sentido de "el momento en que se forjó el vínculo", no un error de canon de fondo, y no toca la cuestión de propiedad que pide este encargo — se deja registrado por si una futura pasada de continuidad quiere ajustarlo a "since he first drew it" / "desde que la desenvainó por primera vez".

---

## 3. Compatibles — ya encajan con el canon sin tocar nada

La lista es larga porque la prosa, leída en conjunto, **ya construye el arco "portador elegido, no dueño"** con bastante disciplina. Los ejemplos más fuertes, en orden narrativo:

- **L1/14** *(Dreams of Laughter)* — el sueño: *"Solmire had not come into being through any holy war. It had come into being for pleasure alone."* Primera grieta en la creencia de propiedad de Miguel; ya apunta a un origen ajeno a él.
- **L1/11** *(Crossings)* — la visión de la mano ajena en la empuñadura: *"it had a right to that hilt older and deeper than any right he could claim to it himself, a claim that made his own grip on the sword feel... distinctly borrowed."* Es, literalmente, la escena que dramatiza "el verdadero portador es otro" sin necesitar nombrarlo todavía.
- **L1/32 y L1/34** *(What Neither of Them Keeps)* — Cassiel/Iofiel: *"What I found predates Miguel's own claim to the blade."* Afirmación explícita y ya publicada de que el origen de Solmire es anterior a Miguel.
- **L1/35** *(The Irreverent Judgment)* — la masacre de rezagados: *"for the sword, and for whatever hand had first shaped it, this had never been war."* Liga la naturaleza indiferente del arma a su forjador original, no a Miguel.
- **L1/47–48** *(The Resonance / The Fall)* — el duelo con Belial: *"no longer entirely his to command"*; y el clímax — Belial: *"This power was never yours."* Miguel: *"Then tell me whose it is."* Esta es la pregunta central del encargo, ya formulada palabra por palabra en el texto, dejada deliberadamente sin responder como gancho de libro.
- **L1/49/51** — el rechazo violento de la espada a la mano de Belial: confirma en escena que el arma *elige* a quién acepta, mecanismo perfectamente compatible con "Solmire llama a su portador".
- **L2/22** *(The Riddle of the Laughing Smith)* — la visión del yunque y la inscripción: *"I am a verdict given not with anger, but with joy. I cannot be claimed by wrath, only by laughter."* Revelación parcial ya extensa (sin nombre) de la verdadera naturaleza/forjador de Solmire.
- **L3/01** *(The Divine Jester)* — la balada de Milo: *"One laughed the light into being, never asking, never warning."* Encaje mítico, coherente con Ereloth.
- **L3/04** *(The First Lesson Laughter)* — Ereloth en diálogo directo: *"Solmire wasn't forged to punish... It was forged to prune."* Ver sección 4 — casi-revelación explícita.
- **L3/06–07** *(The Storm of Sorrows / The Sword Remembers)* — la reclamación en Turein: *"He was not approaching an instrument of judgment to reclaim his authority. He was approaching something that had waited a very long time, and he wanted... to be worth the waiting."* Ejemplo modelo: rechaza explícitamente el marco "recuperar lo mío" a favor de "ser digno de la espera/elección".
- **L3/15–16** *(The Convergence / The Three Forgotten)* — todo el entrenamiento con Ereloth se narra como "seguir el tirón/corriente en la empuñadura", nunca como ejercer un derecho de propiedad; y explícitamente: *"He was not one of the three... his place in what came next was every bit as necessary as theirs, even if this particular moment... was not his to claim."* Ereloth es descrito como *"joy's own forger"* — el epíteto narrativo que lo liga a Solmire (arma del gozo) sin decirlo aún en lenguaje de manual.
- **L3/52** *(The Silent Guardians)* — cierre explícito: *"Ereloth had forged it from pure, defiant joy, long before any of them had needed it to cut anything at all."*

No se recomienda ningún cambio en esta lista.

---

## 4. El momento de revelación — ¿existe, y dónde debería estar?

**Sí existe**, pero repartido en "goteo" a lo largo de toda la trilogía en vez de concentrado en una sola escena — patrón que `2026-08-22_kg1_armas.md` ya documentó como la arquitectura general de revelación del Codex para las tres armas (sección 0 de ese informe). Para Solmire específicamente, la cadena es:

1. **L1/14** — sueño, sin nombre ("por placer, no por guerra santa").
2. **L2/22** — visión + inscripción, sin nombre ("un veredicto de alegría, no de ira").
3. **L3/01** — balada mítica, sin nombre explícito atado a Solmire.
4. **L3/04** — Ereloth, ya identificado como personaje, describe el propósito de la forja de Solmire en primera persona autorizada ("fue forjada para podar") **sin llegar a decir "yo la forjé"**.
5. **L3/16** — epíteto narrativo "joy's own forger" aplicado a Ereloth.
6. **L3/52** — afirmación llana y explícita en la interioridad de Miguel: *"Ereloth had forged it from pure, defiant joy."*

**El problema no es que falte la revelación — es que su formulación más clara e inequívoca (L3/52) llega en el último capítulo de los 52 de Libro III**, funcionando como cierre/confirmación en vez de como revelación con peso propio. Para un lector que termina Libro I con la frase de Iofiel sin corregir (C1 arriba), no hay ningún punto medio de la trilogía donde el texto le devuelva, con la misma claridad, "no, en realidad la espada te eligió a ti, no naciste con derecho a ella" — esa reconstrucción solo se completa retrospectivamente, capítulo 52 de 3.

**Corrección de los candidatos propuestos por el encargo**:
- **L2/22 (inscripción de la forja)**: ya es una revelación parcial (ver sección 3) — deliberadamente anónima, porque Mikel todavía no conoce el nombre "Ereloth" en ese punto de la historia (lo conoce recién en L3/01). No es el lugar correcto para nombrar al forjador sin romper la progresión de misterio ya construida.
- **L3/01 (balada de Ereloth)**: verificado — la balada nombra a los tres forjadores por función ("uno rió la luz"), no por nombre, y no menciona "Solmire" en absoluto en ese capítulo. Es tono mítico correcto, pero no es una revelación *atribuida* (Solmire ↔ Ereloth), solo *evocada*.
- **L3/17 (el plan del Sabio)**: verificado por grep — este capítulo **no menciona a Solmire en absoluto**; es la escena donde Azael revela Aetheris (su propia arma) a Miguel. No es un candidato válido para la revelación de Solmire; el encargo lo proponía por analogía estructural, pero pertenece a un arma distinta.

**Recomendación**: el capítulo idóneo para el beat de revelación explícita es **L3/04 (*The First Lesson Laughter*)**, no uno de los tres candidatos propuestos. Razones:
- Ereloth ya está en escena, ya hablando con autoridad sobre el propósito de la forja de Solmire — solo falta que reclame la autoría en primera persona.
- Es temprano en Libro III (cap. 4 de 52), con recorrido de sobra para que el resto de la trilogía se re-lea bajo esa luz.
- Permite resolver hacia adelante la línea C3 (L1/41, "no fui elegido... el primer necio") como ironía dramática deliberada con pago explícito, en vez de dejarla flotando hasta el epílogo del cap. 52.

**Propuesta de línea a insertar (no aplicada — tarea de solo lectura)**, inmediatamente después de la cita ya existente en L3/04 línea 43:

> — **EN**: *"I forged her myself, before your kind had a word for time. She didn't fall into careless hands, whatever you told yourself in the dark to survive carrying her. She called the hand that could still hear her, and you were the only one listening."*
> — **ES**: *"La forjé yo mismo, antes de que los tuyos tuvieran una palabra para el tiempo. No cayó en manos descuidadas, digas lo que te dijeras a ti mismo en la oscuridad para sobrevivir cargándola. Llamó a la mano que aún podía oírla, y tú fuiste el único que escuchaba."*

Esto (a) hace explícita y atribuible la revelación en escena en vez de solo en narración tardía; (b) cierra específicamente la herida de C3 sin tocar el capítulo 41 de Libro I; (c) no requiere ningún otro cambio en el resto de la trilogía, porque toda la prosa posterior (L3/06-07, 15-16, 52) ya es coherente con esta lectura.

---

## 5. Resumen ejecutivo

- **45/45 menciones de Solmire** revisadas en EN y ES (conteo idéntico).
- **1 línea realmente conflictiva** que necesita reformulación (C1, L1/51, Iofiel) — cambio de una frase, preserva la escena.
- **2 líneas de percepción subjetiva de Miguel** que pueden quedarse (C2 en L1/01, C3 en L1/41) — la segunda es la mejor candidata para un callback en L3/04.
- **La revelación ya existe en la prosa**, distribuida en 6 puntos crecientes de claridad (L1/14 → L2/22 → L3/01 → L3/04 → L3/16 → L3/52), pero su formulación más explícita llega recién en el capítulo final de la trilogía.
- **Recomendación de ubicación para reforzar la revelación**: L3/04, no los tres candidatos propuestos en el encargo (L2/22 y L3/01 ya son revelaciones parciales deliberadamente anónimas por diseño; L3/17 no menciona a Solmire en absoluto — es el capítulo de revelación de Aetheris, un arma distinta).
