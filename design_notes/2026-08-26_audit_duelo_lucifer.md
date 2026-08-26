# Auditoría — Cambio de duelo final de Libro I: Miguel vs. Lucifer (no Belial)

**Fecha**: 2026-08-26
**Tipo**: Auditoría de mapeo, solo-informe. **No se tocó prosa** en ningún archivo.
**Decisión de trama auditada** (del autor): Belial busca y consigue Lamentum (caps. 6-20, intactos) → se la entrega a Lucifer (beat nuevo) → Lucifer baja al campo y mata a Miguel en el duelo → Belial extiende la mano hacia Solmire sobre el cuerpo caído y es rechazado (queda igual) → Lucifer le devuelve la lanza a Belial → desde ahí L2 y L3 quedan como están.
**Método**: lectura completa de `Libro1/EN/44` a `51` (con verificación puntual de paridad en `Libro1/ES/44-51`), lectura completa de `Libro1/EN/40-43` (el tramo inmediatamente anterior al clímax) y de los cuatro capítulos de todo Libro I que mencionan a Lucifer (`02, 06, 09, 21`), grep dirigido sobre L1/L2/L3 para referencias retrospectivas al duelo, lectura de `Libro2/EN/10` (el capítulo ancla de la ignorancia de Lucifer sobre Lamentum), lectura de fragmentos de `Libro3/EN/14, 19, 20, 36, 45` y de `content/lore/grafo_conocimiento.md`, `content/lore/personajes.md`, `content/lore/prompt_universo.md`, y de dos auditorías de coherencia previas (`2026-08-22_coherence_lucifer.md`, `2026-08-22_coherence_belial_lament.md`).

**Nota crítica de numeración** (aplicable a toda referencia futura a este informe): los archivos de lore antiguos (`grafo_conocimiento.md`, `prompt_universo.md`, las auditorías de coherencia del 22/08) citan capítulos de Libro I con la numeración **de origen** (`B1C##`, `B1L##`, `L1/##`), no la numeración actual de archivo. Verificado contra `Libro1/EN/_manifest.json`, campo `source`:

| Cita antigua | Archivo actual | Título |
|---|---|---|
| `B1C18` / `L1/43`(ish) | `40_Three_Were_Forged.md` | Three Were Forged |
| `B1C19` / `L1/44`(ish) | `41_A_Truth_Offered.md` | A Truth Offered |
| `B1C20` | `42_The_Master_of_Lament.md` | The Master of Lamentum |
| `B1C21` | `43_The_Summit.md` | The Summit |
| `B1C22` | `44_The_Eve_of_Ruin.md` | The Eve of Ruin |
| `B1C23` | `45_The_Despairing_Front.md` | The Despairing Front |
| `B1C24` | `46_The_Sundered_Sky.md` | The Sundered Sky |
| `B1C25` / `L1/25-26` en prompt_universo | `47_The_Resonance.md` | The Resonance |
| `B1C26` | `48_The_Fall.md` | The Fall |
| `B1C27` | `49_The_Sound_of_Retreat.md` | The Sound of Retreat |
| `B1C27pt5` | `50_Sparks_for_the_Numb.md` | Sparks for the Numb (insertada post-hoc, ver nota abajo) |
| `B1C28` / `L1/54` | `51_The_Echo_of_the_Sword.md` | The Echo of the Sword |

Chapters 22-39 actuales corresponden a hilos secundarios con prefijos propios (`B1V01-05`, `B1N01-03`, `B1T01-04`, `B1F01-03`, `B1H01-04` — este último, **H**, es el arco de Hollowseam) intercalados entre los capítulos "troncales" `B1C15` (ahora 27) y `B1C17` (ahora 35) y `B1C18` (ahora 40). **Dato relevante para la propuesta del punto 3**: el manuscrito ya tiene precedente de insertar un capítulo nuevo sin renumerar el resto usando sufijo `ptN` — así se insertó `B1C27pt5` (hoy cap. 50, "Sparks for the Numb") entre `B1C27` y `B1C28`. Es el mismo patrón que recomiendo para el beat de entrega.

---

## 1. Beat map del clímax (caps. 44-51), veredicto por beat

Leyenda: 🟢 **QUEDA IGUAL** — 🔵 **REASIGNAR** (mover la atribución de Belial a Lucifer sin tocar sustancia) — 🟡 **REESCRIBIR** (contenido nuevo o ajuste sustancial) — 🟠 **AJUSTE MENOR** (una frase o un pronombre)

### Cap. 44 — The Eve of Ruin
- Uriel en la sala de guerra, colapso de una docena de frentes: 🟢 igual. No depende de quién porte la lanza.
- Gabriel busca a Miguel: **"He has the spear. He is breaking them."** 🟠 ajuste menor — el pronombre "He" hoy es ambiguo/genérico sobre Belial. Bajo el diseño nuevo esta línea es candidata a reforzarse como revelación ("Lucifer has taken the field himself"), lo cual de hecho **sube** la tensión de la escena (que Lucifer en persona baje al frente es un dato mucho más alarmante que "Belial avanza"). Decisión de tono, no de trama.
- Miguel recupera a Solmire: 🟢 igual, no depende del duelo final.

### Cap. 45 — The Despairing Front (Camael/Jeremiel)
- 🟢 **Queda igual en su totalidad.** No hay POV de Belial ni de Lucifer. La única atribución es posicional: *"The pulse arrived from the direction of Belial's advancing vanguard"* — esto describe de dónde viene el frente que avanza, no quién empuña personalmente el arma. Es compatible con que Lucifer viaje con el mismo cuerpo de ejército que comanda Belial.

### Cap. 46 — The Sundered Sky
- Uriel/Ignis Lux, Raphael/infirmería, Gabriel en la mesa de mando: 🟢 igual.
- El soldado demonio que ve el "comet of judgment" (Miguel) y el soldado angélico que no lo saluda: 🟢 igual — es sobre Miguel, no sobre su oponente.
- **El cierre del capítulo (líneas finales, POV Belial)**: *"Belial felt Miguel's approach before he saw any physical sign of it... He halted his own advance, Lamentum steady in his grip, and sent a pulse of open challenge... This ... had narrowed ... to something older than either army and far more personal — a reckoning between two kings..."* → 🔵🟡 **REASIGNAR + construir la llegada.** Este bloque completo debe pasar a Lucifer. Nótese que la frase *"a reckoning between two kings"* hoy es una licencia retórica (Belial no es rey; Lucifer sí lo es — es el "Absolute Sovereign of the Pit" en `personajes.md`). Bajo el diseño nuevo la frase deja de ser metáfora y pasa a ser literalmente exacta — mejora de coherencia, no downgrade. Este es el punto donde debe quedar establecido en página que **Lucifer, no Belial, ha bajado personalmente al campo** con la lanza — necesita una o dos frases nuevas de entrada (su llegada, por qué él y no Belial lidera este tramo) si no se resuelve ya en el beat de entrega propuesto en la sección 3.

### Cap. 47 — The Resonance
- Los interludios mortales (Arin Cross, Milo Ray) y el despertar de Azael (segunda grieta): 🟢 igual — no dependen de la identidad del duelista.
- **El duelo mismo (choque inicial, la onda, el "veredicto"/"verdad" de cada arma, la interioridad de "Belial")**: 🔵 **REASIGNAR**, con una observación de oficio importante — la interioridad atribuida hoy a "Belial" en este capítulo (*"had studied Miguel across this entire war, had watched him from a distance long before either of them ever crossed blades directly"*; *"había ganado duelos antes por paciencia más que por fuerza"*) encaja **mejor** con la ficha de Lucifer (`personajes.md`: *"Never strikes head-on; corrupts, divides and deceives"*; L2/10: gobierna "por atención", observando todo desde lejos) que con la de Belial (`personajes.md`: *"Disciplined, wrathful... Tactical overlord—coordinates brutal charges"*, un comandante de fuerza bruta, no un observador paciente). La reasignación no es solo correcta en trama: es un mejor calce de personaje que el actual.

### Cap. 48 — The Fall
- **El duelo físico completo, el intercambio de réplicas, el golpe final**: 🔵 **REASIGNAR en bloque**, es el capítulo de mayor carga a mover.
  - *"This power was never yours."* / *"Then tell me whose it is."* → funciona en boca de Lucifer sin reescritura de fondo, y de hecho mejora: es exactamente el tipo de ataque psicológico-verbal (no físico) que define a Lucifer en su ficha canónica, mientras que en Belial es una desviación puntual de su estilo de combate habitual (fuerza directa, ver ficha). **Recomendación de craft**: preservar el mecanismo (derrota por duda existencial, no por poder bruto) — es más coherente con Lucifer que con Belial, y además es exactamente lo que ya documenta `prompt_universo.md` línea 547 sobre el sistema de tiers de poder (ver sección 4).
  - La interioridad de "Belial" tras el golpe (agotamiento físico, "había ganado más de lo que le había costado", la sonrisa contenida): 🔵 reasignar a Lucifer.
- **Nota de tier de poder** (sección 4 abajo): este capítulo es, en el diseño actual, la escena que `prompt_universo.md` cita como el único ejemplo canónico de que un Lord (Belial) pueda dañar a un Apex (Miguel) — "solo explotando el costo psicológico de Solmire, no por poder bruto". Ese respaldo doctrinal deja de aplicar tal cual si el duelista es Lucifer (Apex vs. Apex, mismo nivel) — hay que decidir si se conserva la mecánica "gana por palabras, no por fuerza" (recomendado, ver arriba) o si se reescribe como enfrentamiento de poder puro entre iguales. Documentado como pregunta abierta en sección 5.

### Cap. 49 — The Sound of Retreat
- Gabriel/sala de guerra, la pantalla que muere, Uriel pidiendo venganza, Gabriel niega, el toque de retirada, las puertas del Cielo cerrándose: 🟢 **igual en su totalidad.** Ninguna de estas líneas depende de la identidad del vencedor, solo del hecho de la derrota de Miguel.
- **Belial se acerca a la espada caída** (*"Belial approached the fallen sword slowly, too exhausted by the duel's own cost..."*) hasta el rechazo de Solmire (la mano quemada, el grito psíquico, "poisoned rather than triumphant"): esto es H21 del grafo de conocimiento (*"Solmire quemó a Belial al rechazarlo"*) y **debe seguir siendo Belial** — el autor ya lo especifica así en el diseño ("Belial extiende la mano... y es rechazado"). 🟠 **Ajuste menor únicamente**: la frase *"too exhausted by the duel's own cost"* atribuye el agotamiento de Belial al duelo que él mismo peleó; bajo el diseño nuevo Belial no peleó el duelo, así que esa causa debe cambiar (p. ej. agotamiento por el día entero de campaña, o eco físico de lo que acaba de recibir de vuelta la lanza — ver propuesta del beat de devolución en sección 3, que resuelve esto limpiamente si se coloca en la costura 48/49).
- El resto del capítulo (sección con el jinete/soldado en retirada) 🟢 igual.

### Cap. 50 — Sparks for the Numb
- 🟢 **Queda igual en su totalidad.** Es un interludio de Anael/Ezihel/Barachiel sin ninguna mención de Belial ni Lucifer.

### Cap. 51 — The Echo of the Sword
- El consejo de guerra (Gabriel, Uriel, Raphael, Iofiel, Zadkiel, Cassiel, Camael, Elom): 🟢 igual — todo gira en torno a la ausencia de Miguel y de Solmire, no del vencedor.
- **La escena de Belial en su guarida** (*"Belial sat with Lamentum across his knees and a burn across his palm that would not fade"*): si la devolución ocurre en la costura 48/49 (propuesta sección 3), esta escena **ya encuentra a Belial con la lanza de vuelta, sin necesitar ningún cambio estructural**. Solo dos ajustes de matiz:
  - *"He had won. He told himself that in the particular tone one uses on a fact that no longer feels like enough."* 🟡 **reescribir** — Belial no ganó el duelo, lo ganó Lucifer y le regaló el resultado. Esta línea es en realidad una oportunidad: profundiza exactamente la inseguridad que se paga en `Libro3/EN/19` ("mi poder respondía al de Lucifer"). Recomendado convertirla en algo como "había ganado — Lucifer se lo había entregado como quien entrega ganado" o similar, sembrando ya en L1 la semilla de la confesión de L3/19.
  - El resto de la escena (el teniente, "The Host awaits orders", "Rebuild the lines... Let them believe I'm resting", la reflexión sobre el soldado que se sacrificó por Miguel, "find out who forged this spear"): 🟢 **queda igual**, es coherente tanto si Belial ganó el duelo como si se lo entregaron — de hecho el diseño actual (Belial reconstruyendo su autoridad ante un ejército que empieza a "contar espadas") funciona *mejor* narrativamente si su victoria es prestada y él lo sabe, porque añade urgencia genuina a por qué necesita que "crean que estoy descansando" en vez de mostrar la verdad.
- Los interludios mortales (Arin Cross, Milo Ray, Azael abriendo los ojos) y el cierre con Gabriel rezando y la escena de playa (el "hombre de la hamaca"): 🟢 igual — no dependen del vencedor del duelo.

**Resumen cuantitativo**: de los 8 capítulos, **2 quedan intactos al 100%** (45, 50), **4 tienen reasignación de bloques Belial→Lucifer** (46 cierre, 47 duelo, 48 duelo completo, 49 una frase), **1 necesita una frase nueva/aclaratoria** (44), y **1 necesita un ajuste de matiz interno más una posible frase nueva** (51). El corazón físico del trabajo de reescritura es casi enteramente el **cap. 48** (y la segunda mitad del 47): son los únicos dos capítulos donde Belial es protagonista activo del combate y de la interioridad ganadora.

---

## 2. Referencias retrospectivas — lista completa

Búsqueda exhaustiva por grep de patrones ("defeat", "killed Miguel", "duel", "phantom weight", "power answered to", "Belial.*Miguel", equivalentes en español) sobre L1, L2 y L3 completos.

### Dentro de Libro I (antes del clímax)
- **Ningún capítulo entre 22 y 43 menciona a Lucifer** (verificado por grep). Los únicos 4 capítulos de todo Libro I que lo mencionan son `02, 06, 09, 21` — los cuatro anteriores a la reclamación de la lanza, ninguno anticipa el duelo. Esto significa que **no hay ninguna anticipación textual existente del enfrentamiento Miguel-Lucifer que haya que ajustar** — es terreno limpio, pero también significa que el beat de entrega (sección 3) es el único lugar donde el lector recibirá la primera señal de que Lucifer va a intervenir personalmente.
- `Libro1/EN/06` y `09`: Lucifer le advierte a Belial sobre "old songs" respecto de armas como esta, sin dar respuesta directa. Esto **no requiere cambio** — de hecho es el mejor material de siembra ya existente para justificar por qué Lucifer, más adelante, querría la lanza para sí (ya estableció curiosidad e inquietud por su naturaleza).

### Libro II
- `Libro2/EN/03_A_Throne_of_Fractured_Light.md`: *"Solmire, lost somewhere... Miguel, lost in a different and more permanent sense years ago now, his soul long since turned and settled somewhere in the reincarnation cycle."* Uriel: *"Belial's hunters are not sitting idle... a Hell that already knows exactly what it's holding."* → 🟢 no necesita cambio; no atribuye la muerte de Miguel a Belial, solo habla de la cacería de Solmire por parte de las fuerzas de Belial (que sigue siendo dueño de la lanza tras la devolución).
- `Libro2/EN/04_The_First_Breach.md`: *"a garrison so quiet that its own soldiers had taken to calling the posting... since before Miguel's own fall"* → 🟢 referencia temporal neutra, sin atribuir vencedor.
- `Libro2/EN/26_Report_from_the_Abyss.md`: Gabriel: *"Miguel's soul is not the only anomaly this council needs to find. Whatever forged those weapons predates us."* → 🟢 no atribuye el duelo a Belial.
- `Libro2/EN/10_What_Even_He_Does_Not_Know.md` (capítulo ancla de H2): Lucifer observa a Belial cargando la lanza semanas después de Libro I, investiga su origen sin éxito. **Compatible con el diseño nuevo siempre que la devolución ya haya ocurrido para este punto** (lo cual la propuesta de la sección 3 garantiza). Ver análisis de riesgo completo en sección 4 (H2).

### Libro III
- `Libro3/EN/14_Reading_the_Scars.md`: revela un duelo **antiguo y distinto**, prehistórico, entre Michael y Lucifer en el "Scar of Ruin" / "el mundo's oldest fracture" — un choque que, junto a la resonancia accidental de las tres armas primordiales, originó Thamorak. **No es el mismo evento que el clímax de L1** (ocurre eones antes, con Solmire y Lamentum ya como entidades activas junto al báculo de Azael). Cita: *"Michael and Lucifer had fought here, their unresolved extremes lending the wound its exact shape."* → 🟢 no requiere cambio, pero es un dato de lore importante: **ya existe precedente canónico de un duelo Miguel-Lucifer** en la historia profunda de la obra, lo cual refuerza — no contradice — la coherencia temática de que ambos se enfrenten de nuevo en el clímax de L1. Ver más en sección 4.
- `Libro3/EN/36_The_Fallens_Debt.md`: Michael recuerda *"a duel fought at the world's oldest fracture, judgment against defiance, neither side ever quite finishing what they'd started there"* y se pregunta si la deuda que Lucifer le ofrece pagar viene de ahí. → 🟢 mismo duelo antiguo de L3/14, no el de L1. No requiere cambio.
- `Libro3/EN/19_The_Duel_of_Truth_and_Pride.md` (duelo Belial vs. Thaeriel): la confesión clave —
  > *"A fear he'd never let himself examine directly, that his own power answered to Lucifer's the way a reflection answers to the thing it reflects — convincing enough to command armies, never proven substantial on its own terms."*
  → 🟡 **esta línea se vuelve mucho más rica bajo el diseño nuevo** y no requiere reescritura, solo ganancia de resonancia: si Lucifer literalmente le quitó el momento de gloria decisiva del duelo con Miguel (le "prestó" la victoria y se la devolvió), la sospecha de Belial de que su poder es solo un reflejo del de Lucifer deja de ser una metáfora abstracta y pasa a tener un antecedente concreto en la propia trama. Recomiendo señalar esto al autor como una razón más para hacer el cambio, no como algo que auditar como problema.
  - En el mismo capítulo, Thaeriel le revela a Belial el verdadero origen y propósito de Lamentum (H2: Belial aprende que la forjó Thaeriel). Esto **no cambia** — sigue siendo Belial quien lo aprende, en el mismo duelo, sin relación con si Lucifer la portó brevemente en L1.
- `Libro3/EN/20_The_Spark_of_Defiance.md`: Thaeriel toma la lanza de las manos de Belial al final del duelo — *"The spear stopped resisting him the instant that hand made contact, as though it had been waiting this entire duel for permission to finally let go."* → 🟢 no requiere cambio; es coherente con que la lanza haya tenido, para entonces, tres portadores distintos (Belial, brevemente Lucifer, Belial de nuevo, y ahora Thaeriel) — de hecho una lanza que ya ha "soltado" a un portador antes (implícitamente al ser devuelta por Lucifer) hace más creíble que vuelva a soltar en esta escena.
- **No se encontró ningún pasaje en L2 o L3** donde Belial presuma explícitamente, en diálogo, de haber matado a Miguel personalmente, ni ningún pasaje que dependa textualmente de que fue su mano y no la de Lucifer la que dio el golpe final. Esto reduce considerablemente el riesgo de la reasignación: **no hay una "bomba de coherencia" retroactiva escondida en L2/L3** — el material retrospectivo es, en general, agnóstico sobre la identidad exacta del vencedor, salvo la instancia puntual de L3/19 (que, como se explicó, mejora con el cambio en vez de romperse).

---

## 3. Propuesta de los dos beats nuevos

### Beat A — Entrega (Belial le da la lanza a Lucifer)

**Ubicación propuesta**: costura entre el cap. **42** (`The_Master_of_Lament.md`) y el cap. **43** (`The_Summit.md`), o como capítulo nuevo insertado ahí (siguiendo el precedente `ptN` ya usado en el manuscrito para el cap. 50 actual — ver nota de numeración arriba).

**Por qué ahí y no antes**:
- El cap. 42 es exactamente donde Belial **termina de dominar** la lanza (aprende a dirigir el dolor hacia afuera en vez de contenerlo) y cierra con la declaración a sus legiones: *"We will not break their shields... We will break their hearts."* Es el pico narrativo natural para que Belial tenga algo que **mostrarle** a su rey — no antes, porque antes la lanza todavía lo derrotaba a él mismo en los entrenamientos (cap. 42, primera mitad) y no sería un "regalo" creíble, sino una prueba de fracaso.
- El cap. 43 es un capítulo puramente cósmico/atmosférico centrado en Azael (sin ningún POV de Belial ni Lucifer) — no compite temáticamente con una escena de corte, y ya tiene precedente en el manuscrito de capítulos que intercalan material de fuentes distintas (ver cap. 28, 30 y 33 en la tabla de la sección de numeración, que fusionan dos archivos de origen cada uno).
- Ningún capítulo entre 22 y 43 menciona a Lucifer (sección 2), así que colocar la entrega justo antes del cierre de este tramo (en vez de, por ejemplo, en el cap. 34 "A War Nobody Declares", que es de un hilo secundario ajeno a Belial) mantiene la tensión de su ausencia hasta el último momento posible, maximizando el efecto sorpresa/escalada cuando reaparece para tomar personalmente el campo en el cap. 46-47.

**Motivación en carácter para Lucifer** (material de apoyo ya existente, no inventado): `Libro2/EN/10` establece explícitamente que Lucifer observa a Belial acumular poder e influencia a través de la lanza con una inquietud calculada — *"a vassal accumulating a currency that ran through none of Lucifer's own ledgers... had a way, in his long experience, of eventually buying something a king would have preferred to keep unsold."* Aunque ese capítulo es posterior (L2), el patrón de personalidad es completamente coherente para retroproyectar el mismo instinto a L1: un Lucifer que, viendo a su vasallo más ambicioso a punto de convertirse en el matador del Campeón del Cielo — el golpe más grande de toda la guerra — decide reclamar personalmente ese momento antes de que ocurra, tanto por control político (no dejar que Belial acumule ese prestigio) como por curiosidad genuina hacia el arma que ni su archivo de conocimiento (L2/10) pudo identificar. Esto también deja sembrada, ya en L1, la razón por la que en L3/19 Belial confiesa que su poder "siempre respondió al de Lucifer" — aquí sería la primera vez que se lo demuestran en carne propia.

### Beat B — Devolución (Lucifer le devuelve la lanza a Belial)

**Ubicación propuesta**: costura entre el cap. **48** (`The_Fall.md`, el golpe final) y el cap. **49** (`The_Sound_of_Retreat.md`), **antes** de que Belial se acerque al cuerpo de Miguel a buscar a Solmire.

**Por qué ahí exactamente**: es la ubicación que exige la menor cantidad de reescritura de todo el clímax. El cap. 49 ya abre con Belial acercándose a la espada caída — si la devolución ocurre en el instante inmediatamente anterior (Lucifer, agotado por el duelo, le pone la lanza en las manos a Belial con un gesto breve — "ve a reclamar lo que queda" o silencio y un asentimiento, cualquiera de los dos tonos que el autor prefiera entre "recompensa" o "el llanto lo inquieta") entonces:
- Todo el resto del cap. 49 (el rechazo de Solmire, la mano quemada, el grito psíquico, "poisoned rather than triumphant") **no necesita ningún cambio de fondo** — solo la frase de causa del agotamiento de Belial (sección 1, cap. 49).
- El cap. 51 encuentra a Belial ya con la lanza en su regazo **sin ningún salto narrativo que explicar** — la escena tal como está escrita hoy (*"Belial sat with Lamentum across his knees"*) queda intacta.
- Es coherente con el propio patrón de Lucifer (L2/10: gobierna por atención, casi nunca interviene directamente, y cuando lo hace es breve, quirúrgico y calculado) — un Lucifer que aparece, mata, y se retira dejando el trofeo/la carga a su vasallo en la misma escena, sin quedarse a gestionar el campo, es exactamente el tipo de intervención mínima y controlada que su ficha de personaje predice.

**Sobre el motivo** ("recompensa" vs. "el llanto lo inquieta"): ambas lecturas son compatibles con el material existente y no son mutuamente excluyentes — el cap. 51 actual ya tiene la semilla perfecta para la segunda opción: *"beneath the spear's endless appetite... something almost like grief. Not his. The spear's."* Esa línea, si se conserva (movida a la mano de Lucifer durante el duelo, o repetida cuando la lanza vuelve a Belial), sugiere que Lucifer —quien por ficha de personaje jamás muestra vulnerabilidad ("did not let his composure break... it was simply how he existed")— preferiría no cargar con un arma que le hace sentir el duelo de otro. Esto da pie a una devolución motivada por incomodidad genuina disfrazada de generosidad, más rica que una simple recompensa política.

---

## 4. Implicaciones de canon

### H2 (`grafo_conocimiento.md`) — "Lucifer nunca sabe el origen de Lamentum"
**Riesgo real, no trivial.** No es solo la línea de H2: hay una auditoría de coherencia previa completa (`design_notes/2026-08-22_coherence_lucifer.md`) que verificó explícitamente, capítulo por capítulo, que esta ignorancia se sostiene sin fisuras a lo largo de **al menos 11 capítulos posteriores**: `Libro2/EN/10, 48, 50`, `Libro3/EN/05, 14, 25, 27, 28, 36, 42`. Cualquiera de estos que muestre a Lucifer reaccionando con reconocimiento, alivio o certeza ante datos sobre Lamentum quedaría en tensión si el nuevo beat le da contacto físico y prolongado con el arma durante un duelo a muerte.

**Matiz necesario, y por qué sí sobrevive**: el precedente ya existe en el propio libro — Belial cargó y entrenó con Lamentum durante semanas enteras (cap. 21-42) sin aprender jamás quién la forjó ni por qué, incluso recibiendo una visión directa en el cap. 42 (*"a weeping archangel, vast and sorrowful"*) que no supo interpretar hasta que Thaeriel se lo dijo de frente en `L3/19`. El arma comunica **sensación** (dolor, duelo), no **información** (nombres, historia). Mientras la prosa nueva del duelo Miguel-Lucifer se mantenga en ese mismo registro — Lucifer siente el peso, el duelo, quizás una visión fragmentaria similar a la de Belial, pero **no** una revelación de autoría o procedencia — H2 sobrevive intacto. **Recomendación explícita para quien escriba la escena**: prohibir cualquier línea donde Lucifer "reconozca" o "identifique" algo sobre la lanza durante el duelo; cualquier fragmento de visión debe quedar tan opaco para él como lo estuvo para Belial en el cap. 42.

### H17 — Asesinato de Aamon
Sin relación directa con este cambio. Aamon murió antes del clímax (cap. 13, sacrificado por Belial para abrir el Sepulcro), y el secreto de su asesinato lo retiene el Cielo (Sariel), no Lucifer ni Belial en el contexto del duelo. **No requiere ningún ajuste.**

### La profecía ("Three were forged...")
`Libro1/EN/40-41` establece que Solmire juzga y Lamentum sufre, con un tercer arma (creación) sin identificar en ese momento. El clímax (caps. 47-48) hace explícito que cada golpe de las armas es un "veredicto"/"verdad" sobre la naturaleza del portador contrario. Bajo el diseño nuevo, es Lucifer — no Belial — quien porta el "veredicto de sufrimiento" de Lamentum contra Miguel. Esto es **compatible sin fricción**: la profecía nunca ató el arma a un portador específico, solo a una función (juzgar / sufrir / crear), así que cualquier portador de Lamentum activa la misma dinámica. No requiere actualización de lore.

### Sistema de tiers de poder (`prompt_universo.md`, líneas 546-548)
**Hallazgo de alto impacto.** El propio documento de reglas del universo clasifica explícitamente:
> *"1. Apex: Lucifer (Hell) ≈ Miguel while he held Solmire... 2. Archangels/Lords: Gabriel, Raphael, Uriel (Heaven) ≈ Belial... This tier can meaningfully hurt an Apex-tier figure only in exceptional, earned circumstances (see B1C25-26 [=caps. 47-48 actuales]: Belial only overcomes Miguel by exploiting Solmire's psychological cost, not by raw power)."*

Es decir: **el propio sistema de poder de la obra ya reconoce que un Lord (Belial) venciendo a un Apex (Miguel) es la excepción que requiere justificación especial** — la actual solución narrativa (explotar la duda existencial de Miguel, no el poder bruto) es precisamente ese parche. Bajo el diseño nuevo, Lucifer es Apex, del mismo tier que Miguel — el duelo deja de necesitar ese parche de "circunstancia excepcional" para ser creíble en términos de sistema de poder. **Esta línea de `prompt_universo.md` necesita actualizarse** en dos frentes: (1) la cita de capítulo (aclarar que ahora describe a Lucifer, no a Belial) y (2) posiblemente el encuadre — recomiendo, como ya se dijo en la sección 1, conservar el mecanismo "gana por palabras, no por fuerza bruta" incluso siendo ambos Apex, porque es más fiel a la ficha de Lucifer, pero esa es una decisión del autor a confirmar, no algo que este informe resuelva unilateralmente.

### Ficha de personaje de Lucifer (`content/lore/personajes.md`, líneas 1296-1306)
**Segundo hallazgo de alto impacto, y el que más tensión genera con el diseño propuesto.** La ficha canónica actual dice, literalmente:
> *"Weapon: None fixed — gestures, words and occult sigils make the very world obey."*
> *"Combat Style: Never strikes head-on; corrupts, divides and deceives, often posing as an ally until the truth comes too late."*

El diseño nuevo requiere que Lucifer **empuñe Lamentum y mate a Miguel en combate directo, cuerpo a cuerpo** — lo opuesto literal de "never strikes head-on" y "no fixed weapon". Esto no es necesariamente un error a corregir por reescritura de prosa (fuera de alcance de esta auditoría), pero **sí es una ficha de lore que debe actualizarse o matizarse** una vez que el autor confirme el cambio, con dos caminos posibles:
1. Tratar el duelo de L1 como la **única excepción documentada** en toda la obra al patrón de combate de Lucifer — lo cual, narrativamente, puede jugarse a favor: que Lucifer rompa su propio patrón de no ensuciarse las manos es, en sí mismo, la señal de cuánto le importa este movimiento (control sobre Belial, curiosidad por el arma, o ambos). Si se elige este camino, la ficha de personajes.md debería ganar una línea aclaratoria (ej. "*Excepción documentada: empuña Lamentum brevemente contra Miguel en el clímax de Libro I — ruptura deliberada de su propio patrón, no un cambio de estilo permanente*"), no una reescritura de fondo.
2. Alternativamente, la ficha podría interpretarse ya como compatible si se lee "empuñar Lamentum" como una extensión de "gestures... make the world obey" — un arma prestada usada como instrumento de un solo golpe decisivo, no como adopción de un estilo de combate regular. Más forzado, pero evita tocar la ficha.

Cualquiera de los dos caminos requiere **decisión del autor**, no una edición unilateral de lore en esta pasada.

### Confirmación positiva — el checkpoint canónico `B1C28` sobrevive intacto
Dato tranquilizador: `prompt_universo.md` línea 28 fija el estado final obligatorio de Libro I como *"Heaven's retreat; Solmire lost; Belial with Lamentum; Miguel reincarnated"* — el checkpoint del que dependen decenas de capítulos posteriores de L2 y L3. **El diseño propuesto no lo toca**: al final de la secuencia (entrega → duelo → devolución), Belial sigue siendo quien porta Lamentum, Solmire sigue perdida, Miguel sigue reencarnando. El cambio es enteramente interno al tramo 42-49 y no se propaga a ningún checkpoint estructural del resto de la trilogía.

### `personajes_muertes_reencarnaciones.md`
Revisado — no contiene ninguna entrada sobre la muerte de Miguel específicamente (rastrea personajes secundarios). **No requiere actualización.**

---

## 5. Preguntas abiertas para el autor (no resueltas por este informe, solo señalizadas)

1. **¿El mecanismo de victoria se conserva?** — Recomendado (sección 1 y 4): que Lucifer venza por la misma vía psicológica ("This power was never yours") en vez de por fuerza bruta pura, porque calza mejor con su ficha y evita reabrir el parche de tier de poder como una excepción nueva que justificar.
2. **Tono de la devolución**: ¿recompensa política o incomodidad genuina por el llanto de la lanza (o ambas)? Sección 3 propone que ambas son compatibles con el material existente.
3. **¿Cuánto se muestra en página de la llegada de Lucifer al campo?** — El cap. 46 hoy salta directamente al desafío sin mostrar el trayecto. Decidir si el beat de entrega (cap. 42/43) ya deja suficientemente establecido que Lucifer viaja con el ejército, o si hace falta una frase adicional en el cap. 44-46 marcando su presencia antes del duelo.
4. **Ficha de Lucifer en `personajes.md`**: ¿excepción documentada o reformulación del "Combat Style"? (sección 4).
5. **`prompt_universo.md` línea 547**: actualizar la cita de capítulo y decidir si el encuadre "gana por explotar el costo psicológico, no por poder bruto" se mantiene para Lucifer o se reescribe como choque de iguales.

---

## Archivos consultados (referencia)

- `Libro1/EN/{02,06,09,21,40,41,42,43,44,45,46,47,48,49,50,51}.md` (lectura completa)
- `Libro1/ES/{44,45,46,47,48,49,50,51}.md` (verificación de paridad puntual, conteo de palabras + cotejo de líneas clave)
- `Libro2/EN/{03,04,10,26}.md` (lectura completa/parcial)
- `Libro3/EN/{14,19,20,36,45}.md` (fragmentos vía grep + contexto)
- `content/lore/grafo_conocimiento.md`, `content/lore/personajes.md`, `content/lore/prompt_universo.md`, `content/lore/personajes_muertes_reencarnaciones.md`
- `design_notes/2026-08-22_coherence_lucifer.md`, `design_notes/2026-08-22_coherence_belial_lament.md`
- `Libro1/EN/_manifest.json` (mapeo de numeración de origen)
