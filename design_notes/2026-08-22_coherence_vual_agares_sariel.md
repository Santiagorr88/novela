# Auditoría de coherencia — Hilo 03 (Vual/Corin Vasse) + Hilo 14 (Agares) + Hilo 22 (Sariel cazador de reencarnaciones)

**Fecha**: 2026-08-22
**Alcance**: lectura en orden de `L1/07, 11, 12, 22, 23, 24, 25, 26`; `L2/17, 20, 23, 26, 36, 45, 47, 48, 53`; `L3/26, 50` (19 capítulos), más verificación cruzada por `grep` sobre los 159 capítulos y sobre `content/lore/*.md` para el hallazgo de Corin.
**Método**: lectura completa y secuencial de los 19 archivos designados; `grep -rl` de "Corin", "Vasse", "Vual", "Selke", "Undertow", "Nymos" sobre `Libro1/EN`, `Libro2/EN`, `Libro3/EN`; lectura adicional de `L3/47_The_Final_Verse.md` y `L3/49_The_New_Pantheon.md` para verificar si algo paga el hilo del Codex falsificado; consulta de `content/lore/book2_structure_proposal.md` y `book1_new_subplots_beats.md` para contexto de diseño sobre Corin.

---

## Hallazgo 1 — Corin Vasse: promesa narrativa rota, confirmada

**Archivos**: `Libro1/EN/23_A_Gift_With_No_Name.md`, `Libro1/EN/25_What_Desire_Promises.md`, `Libro1/EN/26_Two_Offers.md` (única aparición del personaje en toda la obra).

**Verificación**: `grep -rl "Corin\|Vasse" Libro1/EN Libro2/EN Libro3/EN` solo devuelve esos tres archivos de Libro I. Cero apariciones en los 105 capítulos de Libro II y Libro III.

**Pasaje clave** (`L1/26_Two_Offers.md`, cierre del hilo): Sariel deja ir a Corin con la frase *"This isn't forgiveness [...] It's borrowed time. Use it well."* — una sentencia explícitamente suspendida, no una resolución. El propio narrador insiste en que "nada de esto se sentía terminado" (`"none of it felt finished"`).

**Por qué es una incoherencia real**: no es solo que el hilo quede "abierto" en un sentido ambiguo — es una promesa de trama con estructura de Chéjov completa: un don sobrenatural sin explicar, dos facciones (Cielo e Infierno) que se lo disputan activamente, una amenaza personal formulada contra un tercero (Dez) que tampoco se vuelve a mencionar, y una "sentencia suspendida" que por definición narrativa implica una consecuencia futura. El propio material de diseño del proyecto confirma que esto no fue un cierre deliberado: `content/lore/book1_part2_master_order.md` línea 24 lo etiqueta explícitamente como *"hilo retomable en Libro II/III"*, y `content/lore/book2_structure_proposal.md` línea 61 lo deja como pregunta abierta sin responder: *"Si Corin Vasse (trama de Vual, Libro I) reaparece en este libro o queda cerrado como hilo de Libro I únicamente."* Esa pregunta de diseño nunca recibió una respuesta explícita en la prosa — el hilo simplemente se dejó caer por omisión, no por decisión narrativa. Vual mismo sigue activo en la obra (última aparición en `L2/47`), Sariel sigue activo (hasta `L3/26`), pero ninguno de los dos vuelve a mencionar a Corin ni una vez, ni siquiera de pasada, en los ~2 libros y 105 capítulos que siguen.

**Arreglo mínimo propuesto** (no aplicado): no requiere un capítulo nuevo. Bastaría con una línea de referencia en un capítulo ya existente de Sariel (p. ej. `L2/26_Report_from_the_Abyss.md`, donde ya reporta hallazgos acumulados a Gabriel, o `L3/26_The_Unlikely_Scouts.md`, donde ya está en modo "cazador de reencarnaciones" con Andras) que confirme el estado de Corin — vivo, sin incidentes, la sentencia suspendida nunca cobrada — para que el lector sepa que el hilo fue dejado abierto a propósito y no olvidado. Alternativamente, una nota de autor en `personajes.md` marcando a Corin como "hilo descartado conscientemente" bastaría para cerrar la brecha entre el material de diseño y la prosa final.

---

## Hallazgo 2 — El Codex Mortalis falsificado (Agares/Vual/Nymos): hilo huérfano, sin consecuencia narrativa

**Archivos**: `Libro2/EN/47_A_Truth_Told_First.md`, `Libro2/EN/48_A_Familiar_Shape_in_Borrowed_Words.md`.

**Verificación**: `grep -rl "Selke\|Undertow\|Nymos" Libro3/EN` no devuelve ningún resultado. Ninguno de los tres nombres —la corredora de rumores, el mercado subterráneo, o el capitán con rostro cambiante que ejecuta la segunda plantación— vuelve a aparecer en los 52 capítulos de Libro III. Se leyó también `L3/47_The_Final_Verse.md` (el verso final del Codex real, escrito por Azael/Iofiel) y `L3/49_The_New_Pantheon.md` (Agares vuelto a aparecer, en otro contexto) para confirmar que ninguno de los dos hace referencia retroactiva a la operación de desinformación.

**Pasaje clave** (`L2/47`, Agares dando la orden): *"I want this in the mortal world before Gabriel's people have finished agreeing on a font to print the real one in. Not shouted. Planted."* — y (`L2/48`, Lucifer leyendo el texto ya aprobado): se detiene en la frase *"three primordials, reunited"*, sintiendo una cadencia que "ought to have been able to place" y no logra ubicar, dejando el capítulo cerrado con una intriga explícita sin resolver: *"He set the pages face down on the table beside him, and did not turn them over again."*

**Por qué es una incoherencia real**: son dos promesas narrativas distintas, ambas cerradas en falso:
1. **La operación de desinformación en sí** — un plan con nombre, agentes, un mercado (el Undertow) y un mecanismo (doble fuente independiente) detallados durante dos capítulos completos nunca genera ninguna consecuencia visible: no hay reacción mortal, no hay descubrimiento por parte de Cielo, no hay fricción política cuando el verso real del Codex finalmente se revela en `L3/47`. El "verso final" real ni siquiera reconoce que una versión corrupta ya circulaba entre los mortales — algo que, dado que Iofiel (la Guardiana de la Sabiduría del propio Codex) sería la primera interesada en detectarlo, resulta un silencio narrativo llamativo.
2. **La "forma familiar" que Lucifer no logra ubicar** — el mapa de hilos de referencia ya anota esto como un eco deliberado del origen no revelado de Lucifer en Thamorak, pero esa lectura es enteramente inferencial: no hay ningún pasaje posterior (se revisaron `L3/05, 14, 25, 27, 28, 36, 42`, todos los capítulos con peso de Lucifer) que retome la frase, la cadencia, o la intriga que el propio texto instala explícitamente como un gancho ("*he found himself unable to set down as easily as the rest*"). Un gancho de este tipo, dejado así de explícito y nunca vuelto a tocar, lee como abandonado antes que como misterio deliberado.

**Arreglo mínimo propuesto** (no aplicado): en `L3/47_The_Final_Verse.md`, añadir un breve beat en que Iofiel note (aunque sea de pasada, en su proceso de catalogación) que una versión corrupta del Codex ya llevaba meses circulando entre los mortales antes de que llegara el verso real — esto pagaría el Hallazgo 2.1 con una sola frase y reforzaría además la ironía temática del capítulo (la diferencia entre una verdad "arreglada" y una verdad completa). Para 2.2, bastaría una línea en cualquier capítulo posterior de Lucifer (`L3/14` o `L3/28`, ambos ya con peso reflexivo) donde finalmente ubique la cadencia — o, si el autor prefiere dejarlo como misterio deliberado para una Saga II (coherente con el gancho ya sembrado en `L3/42`, "una guerra más interesante por venir"), convendría que quede documentado como decisión consciente en lugar de hilo simplemente perdido.

---

## Hallazgo 3 — Sariel: contradicción menor en el framing de "su primera desviación"

**Archivos**: `Libro1/EN/11_Crossings.md` y `Libro1/EN/24_The_Trail_That_Shouldnt_Be_There.md`.

**Pasaje 1** (`L1/11`, sobre el informe falso que presenta para justificar seguir vigilando a Arin Cross): *"It was the first false report he had filed in his entire long service, and he felt the weight of that violation clearly even as he committed it."*

**Pasaje 2** (`L1/24`, meses después según el propio texto — *"This was not the same uncertainty that had found him once before, months ago now, standing in a rooftop shadow..."* —, sobre su decisión de no ejecutar el protocolo al detectar la firma mixta de Corin): *"His own record named him unfailing [...] the simple, unbroken fact that once he decided a case, the decision stood, unrevisited, for good."* Y más abajo: *"It was also, Sariel understood clearly even as he made it, the first real deviation of his entire long service."*

**Por qué es una incoherencia real (aunque menor)**: leídos en el orden indicado por el propio mapa de hilos, ambos capítulos reclaman explícitamente el mismo superlativo — "la primera vez que su récord se rompe" — sobre dos actos distintos y ya separados por meses de historia interna. `L1/11` es inequívoco: presentar un informe falso a un superior es una violación consciente del protocolo, y el texto lo llama sin ambigüedad "la primera" de su carrera. Pero `L1/24` abre describiendo el historial de Sariel como todavía intachable ("no closed case ever needing to be reopened... the simple, unbroken fact that once he decided a case, the decision stood, unrevisited, for good") y cierra bautizando su nueva vacilación como "the first real deviation" — como si el informe falso de `L1/11` nunca hubiera ocurrido, o no contara. El adjetivo "real" sugiere que el autor era consciente de la tensión y trató de distinguir categorías (una mentira activa vs. una indecisión pasiva), pero esa distinción no se verbaliza en ningún momento para el lector — simplemente se reafirma el mismo superlativo dos veces sin reconocer el precedente. No rompe la trama, pero sí lee como un desliz de continuidad al leer los capítulos seguidos, típico de escribir dos beats de "primera grieta" sin cotejarlos entre sí.

**Arreglo mínimo propuesto** (no aplicado): una frase de enmienda en `L1/24`, en el mismo lugar donde ya reconoce el precedente del tejado ("*months ago now*"), que reconozca también el informe falso como el primer paso — algo como "the false report had been the first crack; this was the first time the crack reached all the way to a verdict" — convertiría la aparente contradicción en una progresión deliberada (mentira → indecisión → verdicto retenido), que de hecho es la lectura más generosa y probablemente la intención original del autor.

---

## Verificación adicional — arco de Sariel sin saltos de motivación mayores

Se leyó el arco completo de Sariel en el orden indicado (`L1/07, 11, 12, 24, 26` → `L2/17, 20, 23, 26, 36, 45, 53` → `L3/26`) buscando específicamente saltos de motivación, no solo el hallazgo puntual de arriba. Fuera de la contradicción menor del Hallazgo 3, el arco es internamente consistente: la escalada desde "hunter perfecto y sin dudas" (`L1/07`) hasta "cuestiona activamente su propio protocolo" (`L1/24`, `L1/26`) hasta "elegido por Gabriel para una misión no autorizada por el consejo" (`L2/17`, `L2/36`) hasta "trabaja codo a codo con un demonio en una misión conjunta, terminando en respeto mutuo a regañadientes" (`L3/26`) sigue una progresión emocional coherente, sin retrocesos ni saltos no explicados. La reconstrucción del robo de Lament (`L2/23`) y su entrega a Gabriel (`L2/26`) tampoco presentan fricción con el resto del hilo — el hallazgo del margen no firmado del Codex Mortalis ("*Whoever claims this without being its rightful owner will find no glory. They will find a debt*") en `L2/23` se archiva correctamente como detalle pendiente y no vuelve a mencionarse explícitamente en los capítulos leídos, pero no se detectó ninguna promesa formal atada a esa línea específica (a diferencia de Corin o del Codex falsificado) — se registra aquí solo como posible hilo menor a vigilar, no como hallazgo confirmado, ya que cae fuera del alcance de los capítulos asignados a esta auditoría.

---

## Resumen

| # | Hallazgo | Severidad | Estado |
|---|---|---|---|
| 1 | Corin Vasse nunca reaparece pese a "hilo retomable" documentado en el material de diseño | Real — promesa narrativa rota | Confirmado |
| 2 | Operación de desinformación de Agares/Vual (Codex falsificado) sin consecuencia ni cierre narrativo | Real — hilo huérfano | Confirmado |
| 3 | Sariel: dos capítulos reclaman ser "su primera desviación" sin reconocerse entre sí | Real pero menor — desliz de continuidad, no ruptura de trama | Confirmado |
| — | Arco general de Sariel (motivación, POV, progresión emocional) | Sin problema | Verificado limpio |
| — | Margen sin firmar del Codex Mortalis (`L2/23`) — posible hilo menor | Fuera de alcance | No confirmado, solo señalado |

No se encontraron personajes que mueran y reaparezcan sin explicación dentro del alcance de estos 19 capítulos.
