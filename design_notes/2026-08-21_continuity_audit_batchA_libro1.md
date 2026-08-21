# Auditoría de Continuidad y Lore — Libro I, primera mitad (Batch A)

**Alcance:** Solo lectura. No se editó ningún capítulo. Auditoría centrada exclusivamente en continuidad de personajes, objetos/armas, cronología, terminología, repetición estructural accidental y cabos sueltos — **no** en estilo, ritmo ni disciplina de POV (ya auditado en otra sesión).

**Ficha de referencia usada:** `content/lore/personajes.md` (rutas relativas a la raíz del repo `proyectos/novelas`).

**Archivos auditados, en el orden narrativo exacto indicado (no alfabético):**

1. `B1Cap01_EN.md`
2. `B1Cap02_EN.md`
3. `B1Cap03_EN.md`
4. `B1Cap04_EN.md`
5. `B1Cap05_EN.md`
6. `B1Cap06_EN.md`
7. `B1Cap07_EN.md`
8. `B1Cap08_EN.md`
9. `B1Cap09_EN.md`
10. `B1Cap10_EN.md`
11. `B1Cap11_EN.md`
12. `B1Cap12_EN.md`
13. `B1C11_EN.md`
14. `B1C12_EN.md`
15. `B1C13_EN.md`
16. `B1L01_EN.md`
17. `B1L02_EN.md`
18. `B1L03_EN.md`
19. `B1L04_EN.md`
20. `B1L05_EN.md`
21. `B1L06_EN.md`
22. `B1V01_EN.md`
23. `B1V02_EN.md`
24. `B1V03_EN.md`
25. `B1V04_EN.md`
26. `B1V05_EN.md`

(Todas las rutas completas: `project/Chronicles_of_the_Sundering_Judgment/chapters/EN/<archivo>`.)

---

## Resumen de hallazgos por tipo

| Tipo | Hallazgos |
|---|---|
| 1. Hechos de personajes contradictorios | 1 |
| 2. Continuidad de objetos/armas | 0 |
| 3. Cronología/secuencia | 0 |
| 4. Terminología inconsistente | 2 |
| 5. Repetición accidental | 2 |
| 6. Cabos sueltos evidentes | 3 |
| **Total** | **8** |

---

## Tipo 1 — Hechos de personajes contradictorios

### 1.1 Belial se muestra subordinado a Aamon, invirtiendo la jerarquía de `personajes.md`

**Archivo:** `B1C11_EN.md` ("A Feigned Loyalty" / "Commander Aamon"), líneas 13–27.

**Cita textual:**
> "'My lord,' Belial said, straightening only when Aamon gestured him up, 'I've found something worth your attention...'"
> [...] "Aamon listened with his arms crossed and his expression unreadable, in what Belial recognized as his usual manner with subordinates he had not yet decided to trust..."
> [...] "'You'll ride with the vanguard,' Aamon said [...] 'A commander who brings me a gift this good earns the right to watch it opened.' Belial inclined his head in gratitude he did not feel, accepting a position that suited his own purposes far better than Aamon could have any reason to suspect."

También línea 7: "Belial decided, with the same cold self-interest he had spent at the Tower of the Eternos, that Aamon's real cost was simply not a cost he intended to carry himself" — la escena entera lo trata implícitamente como "un comandante" entre otros que responden a Aamon.

**Con qué contradice:** `content/lore/personajes.md`, líneas ~2029–2040 y ~1323–1333. Belial tiene su propia entrada de máximo nivel ("🕳️ Belial — *Lord of Pride and Power*") con Comandantes propios subordinados ("Commanders under Belial: Foras, Vepar"), es decir, ocupa el mismo escalón que Leviathan o Asmodeus. Aamon, en cambio, aparece solo como "◉ Aamon — *Commander / Military Master*" bajo "Commanders under **Leviathan**" — un rango claramente inferior y de otra facción. Según la ficha, Belial nunca debería llamar a Aamon "mi señor" ni comportarse como su subordinado esperando ser "gestured up" para enderezarse.

**Posible explicación no contradictoria:** la escena puede ser una actuación deliberada de Belial (parte del engaño para tender la trampa) más que su rango real — el propio texto dice que Belial "accepting a position that suited his own purposes far better than Aamon could have any reason to suspect", lo que sugiere manipulación consciente. Pero el texto nunca marca explícitamente para el lector que se trata de una actuación de rango (a diferencia de, por ejemplo, aclarar "Belial dejó que Aamon lo creyera un simple comandante"); tal como está escrito, un lector que conozca la ficha de personajes lee una inversión real de jerarquía sin la salvedad correspondiente.

**Propuesta de resolución:** añadir una línea que deje explícito que la deferencia es puro teatro calculado (p. ej. algo como "un rango que Belial llevaba prestado esta noche, tan falso como el resto de su historia"), o confirmar en las notas de lore que "Commander of the Infernal Legions" es un título funcional que supera protocolariamente a los Lords en el terreno militar — y anotarlo en `personajes.md` para que quede resuelto de forma explícita en la ficha, no solo implícita en la prosa.

---

## Tipo 2 — Continuidad de objetos/armas

Sin hallazgos. Se verificó el estado y comportamiento de todas las armas relevantes de este lote — Solmire (`B1Cap01-02, 03-05, 08, 10-12`), Ruach y luego Lament (`B1Cap06, 09; B1C11, 13; B1L01-06`), Penumbra (`B1Cap07, 11-12; B1V03, 05`), Empath (`B1V01`), Deseum (`B1V04-05`) y Vox Aeternum (`B1Cap12`) — y en ningún caso cambian de dueño, aparecen reparadas tras un daño, o se describen con propiedades incompatibles entre capítulos de este lote. La transición Ruach→Lament como arma principal de Belial está explícitamente narrada y justificada (`B1L05-06`), no es un cambio silencioso.

## Tipo 3 — Cronología/secuencia

Sin hallazgos confirmados. Se revisó en detalle una aparente inconsistencia entre la mención de "a terrified survivor only weeks ago" en `B1Cap09_EN.md` (línea 33) y el reporte del superviviente narrado en `B1Cap06_EN.md` — a primera vista parecía implicar que ambas escenas ocurrían el mismo día (Belial "va directamente" de la corte a la Torre). Sin embargo, `B1Cap09_EN.md` línea 13 aclara que se trata de una **segunda** subida a la torre ("during his first ascent... by the time he passed back through it again"), lo que deja varias semanas de margen y resuelve la aparente contradicción. No se encontraron más casos de eventos referidos como "ya sucedidos" antes de tiempo, ni huecos de edad/duración inconsistentes, dentro de este lote.

---

## Tipo 4 — Terminología inconsistente

### 4.1 "Zadkiel" vs. "Zadquiel"

**Archivos:** `B1L02_EN.md`, líneas 33, 37, 39 ("Zadkiel"), frente a `content/lore/personajes.md`, línea 66 ("Zadquiel").

**Cita textual (`B1L02_EN.md`):**
> "It was **Zadkiel** who finally broke the deadlock [...] Decretum rested against the arm of his chair, unused, the way it always did in council rather than combat, and **Zadkiel** himself sat as still through the whole exchange as the hammer did, silver eyes moving between speakers..."

**Cita textual (`personajes.md`, línea 66):**
> "### ⚖️ **Zadquiel** — *Commander of Just Retribution* [...] **Weapon:** *Decretum* — A massive hammer that unleashes stored judgments with each strike."

El arma (Decretum), el rango (Commander of Just Retribution) y los ojos plateados coinciden exactamente, confirmando que es el mismo personaje — solo cambia la ortografía del nombre ("Zadkiel" sin la "u" en las 3 apariciones de `B1L02_EN.md`, frente a "Zadquiel" en la ficha).

**Propuesta de resolución:** unificar la grafía a "Zadquiel" en `B1L02_EN.md` (3 ocurrencias), o si "Zadkiel" es la forma correcta y `personajes.md` está desactualizado, corregir la ficha — pero elegir una sola forma y aplicarla en ambos lugares.

### 4.2 "Tower of the Eternals" vs. "Tower of the Eternos"

**Archivos:** `B1Cap06_EN.md`, línea 59, y `B1Cap09_EN.md` (referencias genéricas a "the tower"), frente a `B1C11_EN.md`, línea 7.

**Cita textual (`B1Cap06_EN.md`, línea 59):**
> "## The Tower of the Eternals
>
> The **Tower of the Eternals** stood alone in a forgotten corner of the realm, far from the capital's noise..."

**Cita textual (`B1C11_EN.md`, línea 7):**
> "Belial decided, with the same cold self-interest he had spent at the **Tower of the Eternos**, that Aamon's real cost was simply not a cost he intended to carry himself."

Es la misma torre (Belial acaba de visitarla en los capítulos inmediatamente anteriores para investigar el fragmento de Lament), pero el nombre cambia de "Eternals" a "Eternos" en `B1C11_EN.md`. Podría ser un residuo de traducción (Eternos = español) colado en el texto en inglés.

**Propuesta de resolución:** corregir "Tower of the Eternos" a "Tower of the Eternals" en `B1C11_EN.md`, línea 7.

---

## Tipo 5 — Repetición accidental

### 5.1 El patrón "lo archivó / ya habrá tiempo después" se repite casi palabra por palabra en al menos 8 pasajes de 7 capítulos distintos

Este bloque narrativo — un personaje nota algo inquietante, decide no decírselo a nadie, y se dice a sí mismo que "ya habrá tiempo" — aparece con una estructura y fraseo tan parecidos, en tantos personajes distintos (Miguel, Camael, Uriel, Sariel, Ophaniel, Corven, Andras), que da la sensación de haberse escrito capítulo a capítulo sin cotejar los anteriores, más que de ser un motivo estilístico deliberado.

**Citas textuales:**
- `B1Cap03_EN.md`, línea 49: "He filed it away rather than answer it, the way he had begun filing away several things since Serephis, and let the moment pass."
- `B1Cap03_EN.md`, línea 71: "he postponed examining the feeling. He told himself there would be time later to understand his new authority."
- `B1Cap04_EN.md`, línea 77: "Camael filed that away too, alongside Gabriel's silence and his own unease from the Overlook, in the growing collection of things he had decided not to voice yet. There would be a council for that eventually, he told himself..."
- `B1Cap05_EN.md`, línea 87: "He did not voice the thought to anyone. He told himself there would be time enough for that later, once the doubt had a clearer shape..."
- `B1Cap07_EN.md`, línea 71: "It was, he told himself, simply not relevant yet."
- `B1Cap08_EN.md`, línea 39: "she filed the belief away regardless, the way she had learned to file away most things that did not fit neatly into an entry."
- `B1Cap10_EN.md`, línea 9: "Corven filed the doubt away where doubts of this particular kind usually went before a mission — set carefully aside, never actually resolved"
- `B1C11_EN.md`, línea 39: "Andras said nothing. He filed the unease away instead, in the same quiet place he filed every other observation not yet worth the risk of voicing..."

**Propuesta de resolución:** no es un problema de lore en sí, pero al ser un patrón de *cierre de escena* repetido con tanta frecuencia y en personajes tan distintos, vale la pena variar la construcción en al menos la mitad de estos pasajes (distintas metáforas para "no decir nada todavía") para que no lea como una fórmula reciclada.

### 5.2 Las dos escenas de Miguel rezando ante el altar y solo oyendo el zumbido de la espada

**Archivos:** `B1Cap08_EN.md` (sección "The Silent Vigil", líneas 45–51) y `B1Cap12_EN.md` (sección "The Sword's Hum", líneas 41–45).

**Cita textual (`B1Cap08_EN.md`):**
> "Miguel knelt alone before the altar that night [...] He found, instead, only the hum. Solmire rested on the altar before him [...] its low, constant thrum filled the space more completely than silence ever had..."

**Cita textual (`B1Cap12_EN.md`):**
> "Miguel knelt before the small altar in his sealed chambers, Solmire laid flat across it, and tried [...] to form a prayer his own mind would let him finish. [...] Every time he tried to shape the first words of it, Solmire's hum rose beneath his thoughts instead [...] as if the sword had decided prayer itself was no longer necessary between them."

Ambas escenas usan la misma estructura casi idéntica (arrodillarse, intentar rezar, el zumbido de Solmire ocupa el lugar de la respuesta divina) y llegan a la misma conclusión emocional. A diferencia del hallazgo 5.1, aquí sí hay una posible lectura de escalada intencional (`B1Cap12_EN.md` dice explícitamente "as he had every night this week", reconociendo que es una repetición dentro de la propia historia). Se marca igualmente porque, colocadas a solo tres capítulos de distancia, el efecto es de redundancia más que de progresión — vale la pena que el autor confirme si la segunda escena aporta algo que la primera no aportó ya, o si conviene fusionarlas/recortar una.

---

## Tipo 6 — Cabos sueltos evidentes

### 6.1 El pergamino sellado que Gabriel nunca menciona ni usa

**Archivos:** `B1Cap01_EN.md`, línea 35; recordado en `B1Cap03_EN.md`, línea 59; y `B1Cap04_EN.md`, línea 69.

**Cita textual (`B1Cap01_EN.md`):**
> "Something else rode with his brother that Gabriel did not name. Miguel caught the edge of it as Gabriel shifted his weight — a folded parchment tucked close against his ribs, sealed in wax too dark and too formal for a simple message, the kind of seal that belonged to a Council order rather than a brother's private word. Gabriel made no move to produce it [...] Whatever it authorized, Gabriel had apparently decided, on his own, not to need it yet."

Se recuerda explícitamente dos veces más ("the sealed parchment still riding unmentioned against his ribs" en el capítulo 3; "the sealed parchment his brother had carried and never once mentioned" en el capítulo 4), estableciendo con fuerza que existe una orden formal del Consejo que Gabriel lleva encima y elige no invocar. Después de eso, el pergamino desaparece por completo del texto — ni siquiera se menciona en `B1Cap12_EN.md`, cuando Gabriel y Uriel forman en secreto un pacto (con Vox Aeternum) sobre qué hacer si Miguel se pierde del todo, que sería el momento narrativo más natural para recordarlo o finalmente usarlo.

**Propuesta de resolución:** o bien retomarlo explícitamente en el pacto de `B1Cap12_EN.md` (Gabriel podría mencionar que aún lo lleva, o decidir destruirlo/usarlo), o si su función es deliberadamente para más adelante en el libro, dejar una línea de anclaje aquí que señale que Gabriel sigue sin usarlo, para que no lea como un elemento olvidado dentro de este mismo tramo.

### 6.2 La amenaza de Malgorath se abandona sin seguimiento

**Archivo:** `B1Cap09_EN.md`, líneas 5–9.

**Cita textual:**
> "Commander — while you were occupied, Malgorath has been calling in favors across three courts. Building support." [...] "Let him." Belial did not slow his measured pace up the stairs [...] "Favors weigh nothing until someone tries to collect them, and by then I'll already be back."

Malgorath se presenta con detalle específico (tres cortes, acumulando apoyos) como una amenaza política concreta contra Belial, pero desaparece por completo del resto del lote — ninguna de las escenas posteriores en la corte de Belial (`B1L03_EN.md`, `B1L06_EN.md`) vuelve a nombrarlo. En su lugar, el hilo de "quién se aprovecha de la ausencia de Belial" se resuelve enteramente a través de Foras, un personaje distinto. Esto puede ser intencional (Belial descarta a Malgorath correctamente, y el peligro real resulta ser Foras), pero tal como está escrito, Malgorath queda introducido con una especificidad que sugiere que debía volver a aparecer y simplemente no vuelve a mencionarse en ningún momento posterior de este tramo.

**Propuesta de resolución:** si Malgorath es un simple señuelo narrativo (para que el lector, como Belial, subestime el peligro equivocado), conviene una línea breve en `B1L03_EN.md` o `B1L06_EN.md` que cierre explícitamente ese hilo (p. ej., un aparte de Nyx confirmando que Malgorath en efecto no llegó a nada). Si no es un señuelo, hace falta al menos una mención de seguimiento en este mismo tramo.

### 6.3 Tensión moral sin resolver: ¿el "plano neutral" purgado por Miguel era realmente inocente?

**Archivos:** `B1Cap08_EN.md`, línea 71; `B1Cap10_EN.md` (capítulo completo); `B1Cap11_EN.md`, línea 29; `B1V01_EN.md`, líneas 5–9 y 21–25; `B1V04_EN.md`, línea 15.

**Cita textual (`B1Cap08_EN.md`):**
> "'They're neutral, Miguel.' Gabriel's voice carried an edge Miguel had rarely heard from him before [...] 'They've committed no crime.'"

`B1Cap10_EN.md` desarrolla esa purga desde el punto de vista de Nyra, una civil no combatiente, y de un único "deep node" — una criatura antigua que protege a las familias sin nunca atacar ni levantar defensa alguna — que es aniquilada por Solmire sin que se muestre ningún combatiente demoníaco en toda la escena. El capítulo construye deliberadamente la purga como una injusticia contra población civil inocente.

**Cita textual (`B1V01_EN.md`, líneas 5–9):**
> "Krass had held this stretch of neutral plane for the better part of a decade [...] He simply held the line he had been given, day after quiet day [...] his bow resting unstrung across his back more often than not, Empath's arrows quiet in their quiver beside it."

**Cita textual (`B1V04_EN.md`, línea 15):**
> "A soul lost in Miguel's purge of the neutral plane, a demon named Krass by the account that reached him, had reincarnated somewhere in the mortal world..."

`B1V01_EN.md` revela que ese mismo "plano neutral" llevaba **una década** albergando una guarnición activa de demonios de Hell (el escuadrón de Krass, con soldados asignados, arcos y flechas) que efectivamente combate y muere ante el avance de Miguel. Esto no contradice frontalmente la escena de Cap10 (ambas pueden ser partes distintas de la misma batalla — Cap11 sí menciona genéricamente "shadow-beings scattered beyond the ridgelines"), pero crea una tensión de fondo que ningún personaje del lado de Heaven llega a plantearse dentro de este tramo: si de verdad había una guarnición demoníaca estacionada allí, la afirmación categórica de Gabriel ("They've committed no crime") queda técnicamente cuestionable, y ningún capítulo posterior de este lote lo señala o lo explica.

**Propuesta de resolución:** esto puede ser ironía dramática deliberada (el lector sabe algo que Heaven no sabe todavía), en cuyo caso no requiere corrección — pero conviene que el autor confirme la intención, porque tal como está, es fácil que un lector atento lo lea como una inconsistencia en vez de una ironía a propósito. Si es deliberado, bastaría con una línea en un libro/capítulo posterior donde Heaven descubra la guarnición de Krass y tenga que reconciliar su propia narrativa de "purga de inocentes".

---

## Nota metodológica

Se comparó cada personaje, arma y jerarquía mencionados contra `content/lore/personajes.md` en su totalidad (2348 líneas). Ereloth, Azael y Thaeriel quedan fuera del alcance de esta verificación porque su ficha completa vive en `prompt_universo.md`, no en `personajes.md`, y no se auditó ese archivo — por lo tanto, cualquier pregunta sobre el origen exacto de Solmire en relación con Ereloth (capítulos 1–2) queda deliberadamente fuera de este informe en vez de reportarse como una contradicción no verificable.
