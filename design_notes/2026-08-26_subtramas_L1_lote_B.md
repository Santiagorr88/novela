# Informe — Lote B de mini-subtramas L1: #3 (Iofiel), #7 (Foras/Vepar F2), #8 (Nocthel)

**Fecha**: 2026-08-26
**Fuente de diseño**: `design_notes/2026-08-26_diseno_subtramas_L1.md`, propuestas 3, 7 y 8.
**Encargo**: capítulos 29, 33, 34 y 40 de Libro1, ambos idiomas.

---

## 0. Hallazgo importante — subtrama #7 ya estaba completa, no se escribió nada nuevo para ella

Antes de escribir, releí los capítulos 33 y 34 tal como están hoy en prosa (ambos idiomas) para ubicar los puntos de inserción exactos que pedía el diseño. La propuesta #7 asumía un hueco real: cap. 33 terminando en el cierre de Malthus (F1) y saltando directo al cap. 34 (F3, la confrontación) sin mostrar el trabajo de espionaje de Stolas que la motiva.

Ese hueco **ya no existe en el archivo actual**. El capítulo 33, después del separador `---` que ya traía, contiene completo — orden de Vepar a Stolas en persona, excavación con *Umbra Manus*, hallazgo de Threll, comentario sarcástico de Stolas, informe de vuelta a Vepar — exactamente el contenido que la propuesta #7 quería insertar repartido entre el final del cap. 33 y el inicio del cap. 34. El diálogo coincide, casi palabra por palabra en su traducción, con el de F2 en `book1_new_subplots_beats.md`. Confirmé el origen: `design_notes/2026-08-23_mejoras_L1.md` ya documenta esta misma sección de Stolas como incorporada en una pasada anterior (23-08), y `2026-08-23_es_sync_L1c.md` describe la fusión de un archivo `__parte2.md` viejo dentro de `33_The_Price_of_Absence.md` que dejó F1 y F2 en un solo capítulo con un único `---`, en vez de repartidos entre el 33 y el 34 como proponía el diseño del 26-08.

El diseño del 26-08, pese a decir haber cotejado capítulo por capítulo, no detectó esto — probablemente porque leyó el cap. 33 solo hasta su primer párrafo o se guió por el resumen de otro documento sin abrir el archivo completo.

**Decisión tomada**: no dupliqué la escena. Añadir una segunda versión de la orden de Vepar y la excavación de Stolas al final del cap. 33 o al inicio del cap. 34 habría creado una repetición literal del mismo beat dos veces en capítulos consecutivos — el tipo de error que rompe lectura, no lo arregla. La subtrama #7 se considera **cerrada sin trabajo nuevo**; el cap. 34 ya abre correctamente presuponiendo el espionaje que el propio cap. 33 ya dramatiza.

Esto deja el lote reducido a **3 escenas nuevas** (no 5): las dos de #3 (Iofiel) y la única de #8 (Nocthel).

---

## 1. Verificación mecánica final

- `git diff` sobre los 6 archivos tocados (EN+ES de caps. 29, 33, 40): **cero líneas eliminadas**, solo inserciones — confirmado con `git diff | grep '^-'` vacío (descontando las cabeceras `---` del propio diff).
- Paridad de párrafos EN↔ES: cada archivo de capítulo usa una línea por párrafo. Recuento de líneas no vacías, antes/después, idéntico en los tres capítulos tocados (29: 28/28, 33: 35/35, 40: 29/29).
- Separadores `---`: mismos puntos en EN y ES en los tres capítulos.
- Ninguna réplica de diálogo existente fue tocada — todas las inserciones son narración pura o (en el caso de Nocthel) diálogo enteramente nuevo, no una edición de diálogo preexistente.
- Política de armas: *Lur* (trompeta de Nocthel) nombrada exactamente una vez en el capítulo 33 (su única presentación en el libro) — verificado por grep. *Umbra Manus* sin tocar (sigue en 1 mención en cap. 33, 0 en cap. 34, como ya estaba).
- H23 (Iofiel no debe saber ni sospechar que la redacción de la Necrópolis fue deliberada): ambas escenas de Iofiel se mantienen en duda profesional genérica ("¿cuántos informes de mi archivo dicen esto?"), nunca acusan ni insinúan mala fe de Kurel/Daith.
- H13 (nada de nombrar Thamorak ni conectar explícitamente el eco del cap. 40 con nada): el eco del cap. 40 es puramente sensorial/emocional — la palabra "ilegible" y la sensación de sostener una verdad a medias — sin nombrar nada ni cerrar ninguna conexión.

---

## 2. Subtrama #3 — Iofiel, el peso de lo que archiva sellado

### 2.1 Cap. 29 (*What Remains Unnamed* / *Lo Que Queda Sin Nombre*) — añadido al final del capítulo

Inserción tras un separador `---` nuevo, después del cierre existente de Daith. Cambio de POV a Iofiel, sola en sus cámaras esa misma noche.

**EN:**

> Iofiel remained in her chambers long after Daith and Kurel's footsteps had faded down the corridor, the hymn's fair copy still open on the table where she'd set it after filing the rest of the day's reports. She read the redacted stanza once more, the single editorial word standing in for whatever the corrupted line had actually carried. *Illegible.* She had accepted the word from Kurel and Daith without pressing further, the same way she accepted a hundred such words a year from a hundred other archivists — a judgment call made by people she trusted to make it honestly, in a discipline old enough that she had long since stopped expecting every fragment recovered whole.
>
> She drew Memnón across the page's edge, not invoking the staff's working, only resting it there the way she sometimes did when a thought needed company rather than magic. The gesture told her nothing the staff wasn't asked to tell. It steadied her anyway.
>
> She opened the drawer where the day's reports would join the rest of the archive's permanent record, and paused with the hymn's fair copy still in her hand. Somewhere in this room, in the shelves stretching beyond it, in the deeper vaults below the scriptorium she had never fully catalogued in all her centuries of trying, other reports carried that same word. She had never counted them. She found herself wanting to now, and immediately after, wondering what the number would actually tell her if she had it — whether a hundred honest gaps looked, from outside, indistinguishable from one dishonest one, and whether she would ever have cause to learn the difference.
>
> She filed the hymn where it belonged, beside every other report her archive held that admitted, in its own careful language, to not quite knowing what it had failed to preserve. She closed the drawer. The question outlived the gesture, the way it always did, and she let it, because she had no better place to put it than the same silence the stanza itself had been given.

**ES:**

> Iofiel permaneció en sus cámaras mucho después de que los pasos de Daith y Kurel se hubieran desvanecido por el corredor, la copia en limpio del himno todavía abierta sobre la mesa donde la había dejado tras archivar el resto de los informes del día. Leyó una vez más la estrofa redactada, la única palabra editorial sustituyendo lo que fuera que la línea corrompida hubiera llevado en realidad. *Ilegible.* Había aceptado la palabra de Kurel y Daith sin insistir más, del mismo modo en que aceptaba un centenar de palabras así al año de un centenar de otros archiveros —un juicio hecho por gente en quien confiaba para hacerlo con honestidad, en una disciplina lo bastante vieja como para que hubiera dejado hace mucho de esperar que cada fragmento se recuperara entero.
>
> Pasó Memnón por el borde de la página, sin invocar el trabajo del bastón, solo dejándolo descansar ahí de la forma en que a veces lo hacía cuando un pensamiento necesitaba compañía y no magia. El gesto no le dijo nada que no se le hubiera pedido al bastón que dijera. Aun así, la calmó.
>
> Abrió el cajón donde los informes del día se unirían al resto del registro permanente del archivo, y se detuvo con la copia en limpio del himno todavía en la mano. En algún lugar de esta sala, en los estantes que se extendían más allá de ella, en las bóvedas más profundas bajo el escritorio que nunca había logrado catalogar por completo en todos sus siglos de intentarlo, otros informes llevaban esa misma palabra. Nunca los había contado. Se descubrió queriendo hacerlo ahora, e inmediatamente después, preguntándose qué le diría en realidad el número si lo tuviera —si un centenar de vacíos honestos se veían, desde fuera, indistinguibles de uno deshonesto, y si alguna vez tendría motivo para aprender la diferencia.
>
> Archivó el himno donde correspondía, junto a cada otro informe que su archivo guardaba que admitía, en su propio lenguaje cuidadoso, no saber del todo qué había fallado en preservar. Cerró el cajón. La pregunta sobrevivió al gesto, como siempre hacía, y ella la dejó sobrevivir, porque no tenía mejor lugar donde ponerla que el mismo silencio que se le había concedido a la estrofa.

### 2.2 Cap. 40 (*Three Were Forged* / *Tres Fueron Forjadas*) — insertado mientras Iofiel trabaja sola con el Codex

Insertado entre el párrafo que especula que la resistencia del Codex podría ser autopreservación deliberada, y el párrafo del temblor de sus manos — antes de que Gabriel entre. Sin separador nuevo (misma escena continua, mismo POV).

**EN:**

> The thought carried her, unbidden, back to a hymn filed months ago and not revisited since — a single stanza two archivists had returned to her marked *illegible*, the word doing exactly as much work as they'd needed it to and no more. She had pressed them once, lightly, and let the answer stand when it came back unchanged. She did not, sitting here now with her own stubborn fragment refusing to yield its meaning cleanly, regret the choice. But she recognized the particular weight of it in a way she hadn't quite managed to, months ago, from the other side of someone else's redaction — the private arithmetic of deciding how much of a half-understood thing belonged in a permanent record, and how much was safer left to stand as a gap no one would think twice about. She set the memory aside without following it further, the way she had learned to set aside most things that offered comparison but no answer. The Codex in front of her had already asked her that same question twice this week. She doubted it would be satisfied with the same answer twice.

**ES:**

> El pensamiento la llevó, sin buscarlo, de vuelta a un himno archivado meses atrás y no revisitado desde entonces —una sola estrofa que dos archiveros le habían devuelto marcada *ilegible*, la palabra haciendo exactamente el trabajo que habían necesitado que hiciera y ni uno más—. Los había presionado una vez, ligeramente, y había dejado que la respuesta se sostuviera cuando volvió sin cambios. No se arrepentía de esa elección, sentada aquí ahora con su propio fragmento terco negándose a ceder su significado con limpieza. Pero reconocía el peso particular de aquello de una forma que no había logrado del todo, meses atrás, desde el otro lado de la redacción de otra persona —la aritmética privada de decidir cuánto de algo entendido a medias pertenecía a un registro permanente, y cuánto era más seguro dejar como un vacío en el que nadie volvería a pensar dos veces—. Apartó el recuerdo sin seguirlo más lejos, de la forma en que había aprendido a apartar la mayoría de las cosas que ofrecían comparación pero ninguna respuesta. El Códice frente a ella ya le había hecho esa misma pregunta dos veces esta semana. Dudaba que fuera a conformarse con la misma respuesta dos veces.

---

## 3. Subtrama #8 — Nocthel, un problema absurdo en la corte de Foras

### 3.1 Cap. 33 — insertado al INICIO del capítulo, antes de la línea original "Malthus felt the shift..."

Escena nueva completa, separada del texto original por un `---` nuevo (el texto original de Malthus queda intacto, sin tocar ni una palabra, inmediatamente después).

**EN:**

> Nocthel had assembled the recruits an hour before dawn, in the amphitheater carved into the black rock below Foras's own halls, because a summoning performed for an audience of one taught nothing and a summoning performed for an audience of forty might, if executed correctly, become the kind of story soldiers repeated for a century. He had rehearsed the invocation the way he rehearsed every invocation: aloud, alone, three times the night before, each pass adding another flourish his voice couldn't quite have justified un-rehearsed the first time.
>
> He raised Lur to his lips with both hands, holding the pause a beat longer than the ritual strictly required, and let the first note carry the length of the amphitheater before the second joined it. The recruits went quiet in the particular way recruits went quiet for something they didn't yet know whether to fear. Nocthel intended, by the third note, for them to have their answer.
>
> What answered instead was small.
>
> It arrived low along the amphitheater floor, more insect than entity, its many legs clicking against the black rock in a rhythm no invocation had specified, and made directly for Nocthel's boots with what could only be read, even by a demon disinclined to read anything as ordinary as an animal's intent, as hunger. Nocthel's second note died somewhere in his throat. He retreated a step, robes catching awkwardly on the horn's bell, and the recruits — forty of them, silent a moment ago out of dread — broke into laughter no rank in Hell's court had authority to suppress.
>
> He recovered enough composure to banish the thing before it reached his ankle, and salvaged what dignity remained by declaring, to no one who believed him, that the exercise had tested the recruits' discipline under an unexpected variable. Foras's court found the version without the declaration considerably funnier, and told it for most of a week.
>
> Malthus, crossing the amphitheater's upper walkway on his way to his own morning's business, caught the tail end of it with half an eye and did not break stride. He had larger currents to read than a Herald's wounded pride.

**ES:**

> Nocthel había reunido a los reclutas una hora antes del amanecer, en el anfiteatro excavado en la roca negra bajo los propios salones de Foras, porque una convocación realizada ante una audiencia de uno no enseñaba nada, y una convocación realizada ante una audiencia de cuarenta podía, si se ejecutaba correctamente, convertirse en el tipo de historia que los soldados repetirían durante un siglo. Había ensayado la invocación de la forma en que ensayaba cada invocación: en voz alta, a solas, tres veces la noche anterior, cada pasada añadiendo un adorno que su voz no habría podido justificar del todo sin ensayar la primera vez.
>
> Alzó Lur a sus labios con ambas manos, sosteniendo la pausa un latido más de lo que el ritual estrictamente exigía, y dejó que la primera nota recorriera la longitud del anfiteatro antes de que la segunda se le uniera. Los reclutas se quedaron en silencio de esa forma particular en que los reclutas se quedan en silencio ante algo que todavía no saben si temer. Nocthel pretendía, para la tercera nota, que tuvieran su respuesta.
>
> Lo que respondió, en cambio, era pequeño.
>
> Llegó bajo, a ras del suelo del anfiteatro, más insecto que entidad, sus muchas patas repiqueteando contra la roca negra en un ritmo que ninguna invocación había especificado, y avanzó directo hacia las botas de Nocthel con lo que solo podía leerse, incluso para un demonio poco inclinado a leer nada tan ordinario como la intención de un animal, como hambre. La segunda nota de Nocthel murió en algún punto de su garganta. Retrocedió un paso, la túnica enganchándose torpemente en la campana del cuerno, y los reclutas —cuarenta de ellos, silenciosos un momento antes por pavor— rompieron en una risa que ningún rango de la corte del Infierno tenía autoridad para sofocar.
>
> Recuperó suficiente compostura para desterrar a la criatura antes de que le alcanzara el tobillo, y salvó la dignidad que le quedaba declarando, ante nadie que le creyera, que el ejercicio había puesto a prueba la disciplina de los reclutas bajo una variable inesperada. La corte de Foras encontró considerablemente más graciosa la versión sin la declaración, y la contó durante casi una semana.
>
> Malthus, cruzando la pasarela superior del anfiteatro camino a los asuntos de su propia mañana, alcanzó a ver el final con medio ojo y no rompió el paso. Tenía corrientes más grandes que leer que el orgullo herido de un Heraldo.

---

## 4. Resumen de cargas

| # | Cap. | Palabras EN (aprox.) | Estado |
|---|---|---|---|
| 3 | 29 | ~290 | Escrito |
| 3 | 40 | ~200 | Escrito |
| 7 | 33/34 | 0 (ya existía) | Sin trabajo — hueco ya cerrado en pasada 2026-08-23 |
| 8 | 33 | ~290 | Escrito |

**Total nuevo**: ~780 palabras EN (+ espejo ES equivalente), en 3 capítulos (29, 33, 40), 0 capítulos nuevos, 0 renumeración, 0 líneas de diálogo o hecho preexistente alteradas.

El capítulo 33 queda efectivamente enmarcado solo por la inserción de Nocthel al inicio — la inserción de cierre que el diseño original preveía para #7 no se agregó porque el contenido que habría llevado ya está, literalmente, en el mismo capítulo.
