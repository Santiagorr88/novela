# Auditoría de coherencia — Hilo 18: Iofiel y el Codex Mortalis

**Fecha**: 2026-08-22
**Alcance**: los 13 capítulos listados para el Hilo 18 en `2026-08-22_coherence_audit_thread_map.md`, leídos en el orden indicado —
Libro1/EN: `17_What_the_Council_Wont_Decide`, `21_What_Winning_Costs`, `28_What_the_Choir_Wont_Sing`, `29_The_Discrepancy`, `30_What_Remains_Unnamed`, `34_What_Neither_of_Them_Keeps`, `43_Three_Were_Forged`, `44_A_Truth_Offered`, `54_The_Echo_of_the_Sword`;
Libro2/EN: `26_Report_from_the_Abyss`, `46_A_Verse_Withheld`, `49_No_One_Trained_to_Hear_It`;
Libro3/EN: `47_The_Final_Verse`.
Más `content/lore/prompt_universo.md` (sección "FRAGMENTS FROM THE CODEX MORTALIS") como material de comparación.
**Método**: lectura completa y en orden de los 13 archivos de prosa, más `grep` dirigido sobre `Libro2/EN` y `Libro3/EN` para confirmar ausencia/presencia de callbacks explícitos. Sin ediciones — auditoría de solo lectura.

---

## 1. La promesa de `Libro1/EN/30` — HALLAZGO REAL

**Punto de partida**: `L1/30_What_Remains_Unnamed.md` cierra con Kurel y Daith archivando la estrofa final de un himno dañado del Coro Silencioso como "illegible" en la copia formal para Gabriel, dejando en su propio registro de trabajo una línea tachada sin traducción defendible. El texto dice explícitamente: *"It would remain there, Daith supposed, until further evidence made a defensible reading possible — not lost, not destroyed, only unresolved. Someday, perhaps, someone might possess enough evidence and understanding to finish what the two of them had chosen, deliberately, to leave undone."* Esa estrofa contiene, según el propio hilo del mapa (Hilo 05), la primera mención corrupta y sin nombre de Thamorak.

**Verificación realizada**: rastreé toda mención posterior a Kurel, Daith, "illegible", "redact*" o "Necropolis" en los 159 capítulos de Libro2/EN y Libro3/EN (`grep` completo). Resultado: **cero coincidencias** salvo un uso incidental no relacionado de la palabra "illegible" en `Libro2/EN/49` (describe daño por fuego en una ruina distinta, sin relación con Kurel/Daith). Ningún personaje —ni Iofiel, ni Kurel, ni Daith— vuelve a mencionar esa estrofa concreta en ningún capítulo posterior.

**`Libro3/EN/47_The_Final_Verse.md` es un objeto textual distinto**, no la misma promesa pagada:
- Es **una página distinta** del Codex: "a page near the volume's end, one that had remained stubbornly blank" — no la estrofa tachada del himno de la Necrópolis, que sigue archivada como una entrada separada en los registros profundos del archivo (línea 41 de `L1/30`: *"The struck-through working transcription went into the archive's deepest records that evening... filed alongside thousands of other fragments"*).
- Es **de autoría distinta**: la tinta que llena la página en blanco lleva la firma de Azael ("the same essence she'd read described in the Choir's oldest records as belonging to one of the three Forgotten. Azael"), no una traducción reconstruida del himno original de Kurel/Daith.
- Es **de contenido distinto**: el verso de `L3/47` trata la reconciliación de los tres Forgotten y el rol de Michael como catalizador — no menciona a Thamorak, ni la palabra corrupta que resistía la pronunciación, ni nada que remita explícitamente a la Necrópolis.

**Por qué es una incoherencia real**: `L1/30` construye, con bastante peso narrativo (dos capítulos enteros de disputa entre Kurel y Daith, un pequeño "funeral" ceremonial por la línea tachada, y una promesa explícita de cierre futuro), una expectativa concreta y nombrable en el lector: *esa estrofa específica* será leída por alguien, algún día. `L3/47` sí paga la expectativa general y más abstracta de "el Codex Mortalis se completa al final de la trilogía", pero no paga la promesa concreta que `L1/30` planteó. Un lector que recuerde a Kurel y Daith llega al final de la trilogía sin que se le confirme nunca qué decía esa palabra que se resistía a ser pronunciada, ni que alguien haya vuelto a abrir ese cajón del archivo. La promesa queda huérfana.

**Arreglo mínimo propuesto** (no aplicado): insertar un párrafo breve (2-4 frases) en `Libro3/EN/47_The_Final_Verse.md`, en la reflexión de Iofiel tras leer el verso de Azael, donde ella recuerde explícitamente la estrofa redactada de la Necrópolis y conecte ambos hechos — por ejemplo, que la nueva revelación le permite entender por fin qué palabra se resistía a ser pronunciada en aquel himno, o que decide, ahora sí, reabrir el registro de Kurel y Daith para intentar una nueva lectura. Alternativamente, si el hueco es intencional (dejar ese hilo abierto a propósito, como ya ocurre con Corin Vasse o Nyx), bastaría con una frase que lo reconozca como tal en vez de dejarlo sin mención — pero tal como está hoy, no hay señal en el texto de que se trate de una omisión deliberada.

---

## 2. Comparación contra los 6 fragmentos de `prompt_universo.md`

Comparé el verso final de `L3/47` (leído por Iofiel: *"Three forgers who were one... Ereloth, who forged creation and joy... Thaeriel, who judged suffering into its proper, necessary shape... Azael, who held the balance..."*) contra los 6 fragmentos de la sección "FRAGMENTS FROM THE CODEX MORTALIS":

- **Fragmento I** ("Three were forged before the chain... If they do not sing together again — by choice, this time — the silence after will not be peace") es, en esencia, la misma profecía que `L1/43` traduce como *"Three were forged before time; one to judge, one to suffer, and one to create"* y que `L3/47` resuelve. La condición del Fragmento I — que la reconciliación debía ser **elegida**, no accidental — se cumple explícitamente en `L3/47`: el verso describe la fractura original como "an accident born of love turned careless" y el desenlace como "a transformation, not an ending" que Azael elige. **Consistente, sin contradicción.**
- **Fragmento II** (Solmire como arma de borrado, no de herida) y **Fragmento IV** (la maldición de Lament sobre quien la roba sin merecerla) no se tocan en los capítulos de este hilo; no hay nada en `L3/47` que los contradiga.
- **Fragmento III** (Thamorak ligado a la vulnerabilidad de Ereloth) tampoco se menciona en `L3/47` — es coherente con que el hilo de Thamorak se resuelve en otros capítulos (`L3/40`, fuera de este hilo), no aquí.
- **Fragmento V** ("One will die who has already died. Another will forget what they were. And the third—will choose to become the wound") es notablemente la misma profecía, en otra traducción, que Selaphiel descubre oculta en el himno del alba en `L2/46`: *"The third will choose the wound... One who has died already will die again... One will forget the shape it wore..."* Ambas versiones son coherentes entre sí como dos traducciones distintas de un mismo verso — algo explícitamente permitido por el propio canon, que establece que "the Codex rearranges itself when it's spoken aloud" (dicho por Jophiel en `L2/46` y corroborado por Iofiel: *"no liturgist invented this cadence independently"*). El desenlace real —Thaeriel conserva la memoria intacta (`L3/46`, confirmado en el mapa de hilos), Azael se transforma en vez de desaparecer— se lee como la variante "buena" que el Fragmento I anticipaba si el trío elegía actuar por voluntad propia en vez de por accidente. **No hay contradicción; es consistencia temática deliberada.**
- **Fragmento VI** (sección ilegible, "the mirror dreams backwards... remakes the Judge") no aparece en ningún capítulo de este hilo. No contradicho, simplemente no abordado — coherente con la nota del propio documento de que el Codex "puede contener más de 777 versos" y con el gancho ya señalado hacia una posible Saga II (advertencia de Lucifer en `L3/42`, fuera de este hilo).

**Conclusión de esta sección**: no se detectó contradicción de tono ni de contenido entre el verso final de `L3/47` y los fragmentos ya establecidos en `prompt_universo.md`. La correspondencia con el Fragmento I es, de hecho, un caso de pago de promesa bien resuelto.

**Nota adyacente, no un hallazgo de esta auditoría**: en `L2/46`, Raziel le dice a Gabriel que existe "a verse deeper in that text" que se niega a entregar todavía ("You'll have it when I judge you ready to survive knowing it"), y en `L2/49` investiga en secreto una segunda cláusula de una inscripción distinta (las ruinas de Ashgrave) que tampoco comparte con nadie. Ninguna de las dos cosas se revela dentro de los capítulos de este hilo. No es necesariamente un error — pertenece más al arco de Raziel/Selaphiel (Hilo 15) que al de Iofiel — pero señalo que existe un tercer hilo de "verso del Codex retenido" además del de la Necrópolis, y que si el equipo que audita el Hilo 15 no lo tiene ya localizado, vale la pena que lo revise para confirmar si se paga en capítulos fuera de esta lista.

---

## 3. Cronología de cuánto sabe Iofiel y cuándo

Rastreé cada punto donde Iofiel actúa sobre información del Codex Mortalis para confirmar que nunca sabe algo antes de que la prosa muestre cómo lo obtuvo:

- `L1/17`: encuentra el fragmento sobre la lanza (Lament) por trabajo directo de archivo — origen mostrado en página.
- `L1/28-30`: encarga la traducción del himno de la Necrópolis a Kurel/Daith; recibe el informe redactado como "illegible" y lo acepta sin presionar — consistente con no saber más de lo que el informe dice.
- `L1/34`: recibe de Cassiel la resonancia de Turein (el origen oficial de Solmire no cuadra) — la archiva como pregunta abierta, sin nombre ni cara. Consistente.
- `L1/43-44`: traduce ella misma, en página, la línea "one to judge, one to suffer, and one to create"; conecta explícitamente esa línea con el informe de Cassiel (Turein) y con Lament — la conexión se muestra en el propio razonamiento del capítulo, no se da por sentada. Sobre el tercer arma dice explícitamente "The text was too damaged. I do not know" — no reclama saber más de lo que tiene.
- `L2/26`: recibe de Sariel la confirmación de que las armas son reliquias anteriores a la guerra, robadas por Belial; el informe no nombra forjadores. Iofiel teoriza en voz alta sobre patrones (el ciclo, las señales de Navarion/Grey City) sin saltar a conclusiones no respaldadas por lo que acaba de escuchar.
- `L2/46`: reconoce de inmediato la estructura y cadencia del Codex en el verso que trae Selaphiel — afirmación respaldada por su experiencia ya establecida como traductora principal del Codex; no requiere conocimiento previo no mostrado.
- `L3/47`: reconoce la "firma" de la tinta como perteneciente a Azael, uno de los tres Forgotten, basándose en haber "estudiado fragmentos de su escritura antigua" a lo largo de su carrera. Este es el único punto donde vale la pena una nota de precaución (ver más abajo), pero no constituye un salto narrativo duro dentro de los capítulos leídos.

**Nota menor, no un hallazgo de incoherencia dura**: en `L3/47`, Iofiel reconoce la firma estilística de Azael citando "fragments too old and too faded for most keepers to properly identify anymore" que ya había estudiado antes. Los capítulos de este hilo nunca muestran a Iofiel enterándose explícitamente de la identidad de Azael como uno de los tres Forgotten (esa revelación ocurre en capítulos fuera de su hilo — `L3/16-17`, parte del Hilo 11). La frase se sostiene igual sin contradicción, porque lo que dice haber estudiado antes es la firma de "uno de los tres Forgotten" en abstracto (un patrón ya insinuado desde `L1/43`), no la identidad de Azael en concreto — y es razonable asumir que, como Wisdom Keeper del Coro, fue informada extraoficialmente tras el clímax del Libro III (`L3/38-40`) aunque esa escena de puesta al día no se muestre en página. Es un salto leve, cubierto por inferencia razonable más que por evidencia directa. Si se quisiera blindar del todo, bastaría una frase en `L3/47` ("news of the Summit's true identity, relayed to her secondhand weeks ago...") — pero no lo considero una incoherencia real que requiera corrección obligatoria.

---

## 4. Veredicto

**Un hallazgo real**: la promesa explícita de `Libro1/EN/30_What_Remains_Unnamed.md` (alguien completará algún día la lectura de la estrofa redactada del himno de la Necrópolis) **no se paga** en `Libro3/EN/47_The_Final_Verse.md`. Este último es un objeto textual distinto — otra página del Codex, de otra autoría, sobre otro contenido — que cierra una expectativa distinta y más general (el Codex se completa al final de la trilogía) sin tocar la promesa concreta y nombrada que `L1/30` planteó. Ningún capítulo posterior de Libro2 o Libro3 vuelve a mencionar a Kurel, Daith, ni esa estrofa específica. Arreglo mínimo propuesto: un párrafo breve de callback en `L3/47`, o una frase que reconozca el hilo como deliberadamente abierto.

**Sin hallazgos** en la comparación contra los 6 fragmentos de `prompt_universo.md` (consistencia de tono y contenido confirmada, incluyendo una correspondencia bien resuelta con el Fragmento I) ni en la cronología del conocimiento de Iofiel (un único punto de inferencia razonable pero no evidenciado en página, no considerado una incoherencia real).

**Nota adyacente para otro hilo**: el "verso más profundo" que Raziel retiene deliberadamente (`L2/46`, `L2/49`) nunca se revela dentro de los capítulos de este hilo — posible hilo abierto a verificar en la auditoría del Hilo 15 (Selaphiel/Raziel), no incluido aquí como hallazgo propio porque cae fuera del arco asignado a Iofiel.
