# Verificación B3C049-052 (hilo de Naamah) contra prosa real — 2026-08-20

**Alcance**: verificación de solo lectura sobre `main` (confirmado con `git branch --show-current`, sin cambio de rama). Continúa directamente la lección de la auditoría nocturna del 2026-08-19 (`design_notes/2026-08-19_overnight_summary.md`, `2026-08-19_contradictions_and_citations.md`): el outline no es automáticamente fiable, incluso en secciones no marcadas como "superadas", si nunca se cotejó contra la prosa ya escrita en el momento de diseñarlo.

**Motivo**: Naamah (Commander de pleno derecho, ficha en `content/lore/personajes.md` línea 1337) tiene cero apariciones en los 147 capítulos de prosa. El outline (`content/lore/arco_argumental_completo.md`, entradas **B3C049-052**, líneas 1405-1419) propone instalarla apropiándose del crédito político de una tregua de campo no autorizada entre Camael y Vepar. Estas cuatro entradas se diseñaron en una sesión previa de esta misma noche **sin cotejarlas contra la prosa de Vepar ya escrita y aprobada** en ese momento (`B3C11_EN.md`, `B3C28_EN.md`). Este informe hace esa verificación, tal como exige el encargo, antes de escribir una sola línea de prosa.

**Fuentes leídas completas antes de concluir**: `B3C11_EN.md` ("The In-Between War"), `B3C28_EN.md` ("The Uneasy Vanguard"), `B3C44_EN.md` ("The New Pantheon"), `B2C21pt5_EN.md` ("The Tide Remembers"); `content/lore/book3_part1_expanded_beats.md` y `book3_part2_expanded_beats.md` (documentación de producción de B3C10.5, B3C11, B3C27, B3C28, B3C29, B3C30); `content/lore/expansion_guidelines.md` (línea 167, log de aprobación de B3C28).

---

## Veredicto: NO son compatibles tal como están escritas. Contradicen aritmética de encuentros ya fijada en dos documentos independientes.

### Contradicción 1 — B3C049 exige un encuentro cara a cara que la prosa nunca muestra, y que rompería el conteo de encuentros ya fijado

`B3C049` ("What Neither Flag Commands") describe a Camael y Vepar "meeting alone in the dead space between their lines, close enough to kill each other." Pero `B3C11_EN.md` (línea 79, la escena que corresponde exactamente a este momento del outline — el vacío que se abre entre las dos flotas) describe explícitamente que se ven **"through their respective view-screens"** — nunca se encuentran físicamente. No hay conversación, no hay parley, no hay "una hora" compartida en tierra de nadie.

Más grave: `B3C28_EN.md` (línea 9) establece por escrito, en la propia prosa aprobada, la aritmética exacta de sus encuentros previos: *"This would be their fourth. It would also, he understood, be the first where neither of them was trying to kill the other."* Y `expansion_guidelines.md` línea 167 lo confirma de forma independiente en el registro de producción: *"su cuarto encuentro y primero hablado tras tres anteriores en el campo de batalla (B3C11)"*. Es decir: exactamente **tres** encuentros previos, ninguno hablado, ninguno pacífico, antes de la tienda de mando de B3C28. Un parley de una hora en tierra de nadie durante el tercero de esos encuentros (el del vacío) —tal como pide B3C049— convertiría ese tercer encuentro en uno "hablado" y añadiría un quinto encuentro total, contradiciendo directamente ambas fuentes.

### Contradicción 2 — B3C050 le da a la Lágrima de Fe de Camael un origen distinto e incompatible con el ya establecido

`B3C050` ("The Wall of Shields") monta un discurso de Camael sobre el muro de escudos como el origen de su "Tear-of-Faith beat" — su nota de función narrativa lo dice explícitamente: *"Installs Camael's Tear-of-Faith beat... Plants the trust Naamah later exploits."* Pero la auditoría de anoche (`2026-08-19_contradictions_and_citations.md`, Hallazgo E) ya documentó que la Lágrima de Fe usada en la forja del clímax tiene un origen fijado y distinto en la prosa: un guardapelo que Camael entrega a Michael la noche que "handed this locket over" (`B3C32_EN.md`, líneas 49-51; escena tejida a través de `B3C22`, `B3C29`, `B3C31pt5`, `B3C32`, `B3C33`). Un segundo origen —un discurso sobre un muro de escudos compartido con Vepar— no puede coexistir con el primero sin contradicción directa sobre el mismo objeto argumental.

Adicionalmente: la escena que B3C050 describe (`"the shield-wall that held today"`) no ocurrió — en `B3C11_EN.md` cada flota se retira a su propio lado por separado (Camael: "Hold position"; Vepar: "Fall back one full length... hold there"), sin ninguna formación combinada de escudos entre ambos bandos.

### Contradicción 3 — B3C051 exige un perímetro conjunto de tres días que ninguna prosa referencia, y que además contradice el tono de "confianza nueva y todavía incierta" del propio B3C28

`B3C051` ("A Line Held Together") describe tres días de perímetro conjunto no autorizado, con un demonio bajo el mando de Vepar rescatando a una ángel herida — un evento sustancial que debería preceder la reunión de la tienda de mando (B3C28). Pero la propia apertura de B3C28 (línea 6-11, POV Camael) encuadra la confianza hacia Vepar como algo que está a punto de extender por primera vez, con cautela real: *"waiting on an enemy commander he was about to ask his own soldiers to trust, at least provisionally"*; ninguna referencia a tres días ya compartidos de cooperación de campo demostrada. Es el mismo tipo de vacío narrativo que la auditoría de anoche identificó para el mecanismo de consejo/Gabriel: un evento entero que el outline exige y que la prosa simplemente no contiene ni puede sostener sin reescribir el tono ya aprobado de B3C28.

### B3C052 (Naamah) no es incompatible en sí misma — depende causalmente de 049-051

El mecanismo de B3C052 —Naamah interceptando la narrativa de un acuerdo de campo no autorizado ante la corte de Lucifer, antes de que el propio informe de Vepar llegue— es perfectamente compatible con el material ya escrito: encaja con la caracterización de Vepar en `B3C44_EN.md` (línea 23: *"occupied instead with the fleet and the particular loyalty he'd apparently built with certain angelic commanders during the peace talks"* — Asmodeus lo respeta precisamente por evitar la política de corte) y con su fiche (pragmático, indiferente al teatro de poder, ver `B2C21pt5_EN.md`). El problema no es la premisa de Naamah; es que su entrada está anclada, en el diseño actual, a tres beats previos (049-051) que sí contradicen la prosa. Retirado ese andamiaje, la esencia del personaje —manipuladora social, se apropia de crédito ajeno, opera con percepción en vez de fuerza— es plenamente utilizable.

**Nota de terminología**: el propio B3C049 se autodescribe como *"a deliberately smaller, commander-to-commander version of Duplicado.md's Concordato de Ceniza."* Ese nombre ya está tomado en la prosa real: `B3C27_EN.md` ("The Concordat of Ash") es el pacto institucional Gabriel-Lucifer, ya escrito y aprobado (`expansion_guidelines.md` línea 165). La nueva escena de Naamah no debe reutilizar ese nombre en el texto para el arreglo de campo Camael-Vepar, para no generar una confusión de "dos Concordatos de Ceniza" en la mente del lector.

---

## Decisión de diseño — introducción alternativa de Naamah, compatible con la prosa real

Se descarta el mecanismo literal de B3C049-051 (parley físico, discurso del muro de escudos como origen de la Lágrima, perímetro de tres días). Se conserva la esencia de B3C052 con un anclaje distinto:

- **Punto de inserción**: después de `B3C28` (el cuarto encuentro, primero hablado — la reunión en la tienda de mando que sí está escrita y aprobada) y antes de `B3C30` (el clímax de la Parte 2, donde la flota combinada ya opera bajo el arreglo táctico exacto negociado en B3C28, sin ninguna fricción política visible). `B3C29` es un capítulo Michael/Azael sin relación, así que no hay colisión.
- **Gancho temporal**: la propia línea de cierre de B3C28 lo autoriza — *"A war fought through trade rather than mere survival... might yet prove worth whatever it kept costing both sides in the weeks ahead."* Naamah se inserta en esas "semanas siguientes", cuando el arreglo informal de la tienda ya ha crecido en la práctica de campo (sin necesitar un perímetro de tres días específico y no mostrado — basta con que el arreglo siga funcionando, algo que B3C30 ya confirma que ocurrió).
- **Mecanismo conservado de B3C052**: la noticia del arreglo no autorizado llega a la corte de Lucifer filtrada por el propio relato de Naamah antes de que el informe de Vepar aterrice; ella se ofrece a "formalizar" políticamente lo que Vepar ya logró solo; Vepar, indiferente a la política de corte (rasgo ya fijado), se lo permite sin darse cuenta de lo que cede.
- **Sin conflicto con B3C44**: Asmodeus, en el capítulo final ya escrito, atribuye correctamente el logro a Vepar mismo, sin mencionar a Naamah — compatible, porque Asmodeus es un observador que ve a través del teatro político; Naamah gana la narrativa ante la corte de Lucifer, no ante Asmodeus.
- **Personaje secundario de anclaje**: Stolas (Captain bajo Vepar, ya con ficha y aparición previa en `B2C21pt5_EN.md`) como testigo con recelo no resuelto. Gusion (Captain bajo Naamah, *Mortal Politics*, "Fine print is my blade") como el agente/mecanismo que le hace llegar la noticia antes que el canal oficial — encaja literalmente con su ficha.

Este material se desarrolla como interludio nuevo `B3C28.5`, documentado en el Paso 2 de este mismo encargo.
