# Informe — Lote C de mini-subtramas L1: #1 (Camael/Jeremiel), #6 (Rafael y el soldado), #9 (Remiel)

**Fecha**: 2026-08-26
**Fuente de diseño**: `design_notes/2026-08-26_diseno_subtramas_L1.md`, propuestas 1, 6 y 9.
**Archivos tocados**: `Libro1/EN/11_Crossings.md`, `Libro1/ES/11_Crossings.md`, `Libro1/EN/12_A_Silence_in_Heaven.md`, `Libro1/ES/12_A_Silence_in_Heaven.md`, `Libro1/EN/45_The_Despairing_Front.md`, `Libro1/ES/45_The_Despairing_Front.md`, `Libro1/EN/46_The_Sundered_Sky.md`, `Libro1/ES/46_The_Sundered_Sky.md`, `Libro1/EN/51_The_Echo_of_the_Sword.md`, `Libro1/ES/51_The_Echo_of_the_Sword.md`, y su espejo `project/Chronicles_of_the_Sundering_Judgment/chapters/EN/B1C28_EN.md` (solo la línea de Remiel del cap. 51, único punto donde ese árbol paralelo se ve afectado).

Verificación de paridad: `git diff --stat` confirma el mismo número de líneas insertadas en cada par EN/ES (11: +4/+4, 12: +6/+6, 45: +18/+18, 46: +12/+12, 51: 1 línea modificada en ambos). Ninguna réplica de diálogo existente fue tocada; toda inserción se verificó contra el texto original antes de escribir con `Read`+`Edit`, nunca con reescritura de archivo completo. No se tocó la zona sagrada del cap. 51 (escena Belial/teniente, párrafo final del colgante) ni ningún otro archivo del repo (`29`, `33`, `40` aparecen modificados por otra sesión en paralelo — no se tocaron aquí).

---

## Subtrama #1 — Camael y Jeremiel

### Cap. 11 — beat ampliado (Jeremiel da algo concreto de sí)

Insertado inmediatamente después de la réplica existente de Camael ("Today's just the first time it got loud enough to notice." / "Hoy es solo la primera vez que se puso lo bastante fuerte como para notarlo.") y antes de "Jeremiel did not press further" / "Jeremiel no insistió más". Ninguna línea de diálogo previa fue alterada.

**EN:**

> Jeremiel let that settle before he answered with something Camael hadn't asked for. "First season I served under you, I fumbled a troop count — nothing that mattered by morning, but wrong all the same. You didn't correct it in front of the company. You called me to your tent that night and corrected it there, quietly, so nobody but the two of us ever knew I'd gotten it wrong." He kept his eyes on the column ahead rather than on Camael. "I've never forgotten you had the chance to use me as an example in front of everyone and didn't take it. That's most of why I don't push, when you go quiet like this. You've never once made me carry a mistake in front of men who'd remember it. Figured I owed you the same."
>
> It was not, strictly, an answer to anything Camael had asked. Camael understood that Jeremiel had offered it anyway, deliberately, the way he offered most things — sideways, timed to land exactly where it was needed rather than where it was expected. It was, Camael realized only now, close to the same instinct Jeremiel used to read an entire company's morale from the outside: not by asking soldiers how they felt, which few of them would ever answer honestly, but by noticing what they chose to protect without being told to — a letter kept dry through a storm nobody had ordered them to survive. Jeremiel had just done exactly that to him, in the middle of a silent column, and Camael let himself be read. He said nothing back. He didn't need to. Jeremiel had never once required it of him.

**ES:**

> Jeremiel dejó que eso se asentara antes de responder con algo que Camael no había preguntado. —La primera temporada que serví bajo tu mando, me equivoqué en un recuento de tropas... nada que importara para la mañana siguiente, pero equivocado de todos modos. No me corregiste delante de la compañía. Me llamaste a tu tienda esa noche y me corregiste ahí, en voz baja, de modo que nadie más que nosotros dos supo jamás que me había equivocado. —Mantuvo la vista en la columna que tenían delante en vez de en Camael—. Nunca olvidé que tuviste la oportunidad de usarme de escarmiento delante de todos y no la tomaste. Esa es la mayor parte de por qué no insisto, cuando te quedas callado así. Nunca una sola vez me hiciste cargar un error delante de hombres que lo recordarían. Supuse que te debía lo mismo.
>
> No era, en sentido estricto, una respuesta a nada que Camael hubiera preguntado. Camael comprendió que Jeremiel se lo había ofrecido de todos modos, deliberadamente, del modo en que ofrecía la mayoría de las cosas —de lado, calculado para aterrizar exactamente donde hacía falta en vez de donde se esperaba—. Era, comprendió Camael solo ahora, casi el mismo instinto que Jeremiel usaba para leer la moral de toda una compañía desde afuera: no preguntando a los soldados cómo se sentían, algo que pocos de ellos responderían jamás con honestidad, sino fijándose en lo que elegían proteger sin que nadie se lo ordenara —una carta mantenida seca a través de una tormenta que nadie les había ordenado sobrevivir—. Jeremiel acababa de hacerle exactamente eso, en medio de una columna silenciosa, y Camael se dejó leer. No respondió nada. No hacía falta. Jeremiel nunca se lo había exigido.

### Cap. 45 — escena nueva insertada ANTES del párrafo inicial actual

Planta la piedra de afilar como objeto compartido — un préstamo nunca devuelto, broma corriente entre ambos — que el lector reconoce sin declaración explícita cuando Camael sostiene "a whetstone in one hand" sobre la espada de Jeremiel en el cap. 51 ("This was the twelfth piece, and the one he had saved for last"). No se tocó ni una palabra del texto original del capítulo; la escena se colocó delante, seguida de un separador `---` nuevo.

**EN:**

> The night before the line formed, Camael found Jeremiel exactly where he expected to find him — seated on an overturned crate near the picket fires, Iustitia laid bare across his knees, a whetstone moving in slow, familiar strokes along its edge. It was the same stone Jeremiel had been carrying for longer than either of them could accurately place anymore — borrowed, by Jeremiel's own account, from Camael's own kit some three campaigns back, and never once returned despite Camael's regular, half-serious demands for it.
>
> "You're still carrying that," Camael said, more statement than question, settling onto the crate beside him.
>
> "You're still asking for it back." Jeremiel didn't look up from the blade. "One of these days I might actually give it to you. Ruin the whole arrangement."
>
> It was an old joke between them, worn as smooth as the stone itself — Camael pretending each time to want it returned, Jeremiel pretending each time to consider it, neither of them ever following through, because the asking had become its own kind of ritual, steadier than either of them would have admitted aloud. Camael held out his hand anyway, tonight, on impulse he didn't examine too closely.
>
> Jeremiel studied the offered hand a moment, then set the whetstone into it — not tossed, not handed off carelessly, but placed, the way a man sets down something he means to be careful with. "Keep it a night, then," he said. "You can give it back tomorrow, once this is over."
>
> "And if I decide to keep it instead?"
>
> "Then I'll know exactly where to find it." Jeremiel picked Iustitia back up, testing the edge against his thumb, satisfied. "You've never once kept anything of mine you didn't mean to give back eventually."
>
> Camael turned the stone once in his palm, feeling the worn hollow at its center where two men's hands had shaped it smoother than it had any right to be, and said nothing, because there was nothing in that particular silence that needed saying.

**ES:**

> La noche antes de que se formara la línea, Camael encontró a Jeremiel exactamente donde esperaba encontrarlo —sentado sobre una caja volcada cerca de las hogueras de guardia, Iustitia desnuda sobre las rodillas, una piedra de afilar moviéndose en pasadas lentas y conocidas por el filo—. Era la misma piedra que Jeremiel llevaba consigo desde hacía más tiempo del que ninguno de los dos podía ya ubicar con precisión —prestada, según la propia versión de Jeremiel, del equipo del propio Camael unas tres campañas atrás, y jamás devuelta pese a las exigencias regulares y medio serias de Camael por recuperarla.
>
> —Todavía la tienes —dijo Camael, más constatación que pregunta, sentándose en la caja junto a él.
>
> —Todavía la pides de vuelta. —Jeremiel no alzó la vista de la hoja—. Uno de estos días capaz que te la doy. Arruino todo el arreglo.
>
> Era una broma vieja entre ellos, gastada tan lisa como la propia piedra —Camael fingiendo cada vez querer que se la devolviera, Jeremiel fingiendo cada vez considerarlo, ninguno de los dos llevándolo nunca a término, porque el pedirla se había vuelto su propio tipo de ritual, más firme de lo que ninguno de los dos hubiera admitido en voz alta. Camael tendió la mano de todos modos, esa noche, por un impulso que no examinó demasiado de cerca.
>
> Jeremiel estudió la mano tendida un momento, y después puso la piedra de afilar en ella —no la arrojó, no se la pasó sin cuidado, sino que la colocó, del modo en que un hombre deja algo con lo que piensa tener cuidado—. —Guárdala una noche, entonces —dijo—. Me la devuelves mañana, cuando esto termine.
>
> —¿Y si decido quedármela?
>
> —Entonces sabré exactamente dónde encontrarla. —Jeremiel volvió a tomar Iustitia, probando el filo contra el pulgar, satisfecho—. Nunca te has quedado con nada mío que no pensaras devolver, tarde o temprano.
>
> Camael giró la piedra una vez en la palma, sintiendo el hueco gastado en su centro donde las manos de dos hombres la habían dejado más lisa de lo que tenía derecho a estar, y no dijo nada, porque no había nada en ese silencio en particular que necesitara decirse.

---

## Subtrama #6 — Rafael y el soldado que no quiere ser sanado

### Cap. 46 — beat insertado dentro del párrafo de la enfermería ya existente

Colocado justo después de "aware that rushing this kind of restoration risked losing whatever fragile progress each careful minute bought." / "consciente de que apresurar este tipo particular de restauración arriesgaba perder cualquier progreso frágil que cada minuto cuidadoso llegara a comprar." y antes de "He felt the losing shape of the battle" / "Sentía la forma de una batalla que se perdía". El cap. 46 se leyó en su estado ACTUAL (reescrito el mismo día por la llegada de Lucifer); la escena se colocó en el bloque de enfermería de Rafael, muy lejos del cierre reasignado a Lucifer (que empieza recién en la línea "A demon captain near the vanguard..."). El soldado queda anónimo — "one of ours" / "uno de los nuestros" — sin nombrar a Jeremiel.

**EN:**

> He moved to the next soldier before the thought could settle further, and found this one waiting for him already braced, not in relief but in something closer to refusal. The soldier's hand came up as Veritas's light reached for him, closing around the staff's shaft and pushing it firmly aside — not a flinch, not the reflex of a man in pain, but a deliberate, steady rejection Raphael had rarely met from anyone he'd come to heal.
>
> "Leave it," the soldier said, low enough that it barely carried past the two of them. His eyes were dry now, though the tracks of earlier tears still marked his face. "I don't want it gone yet."
>
> Raphael held the staff where it was, neither withdrawing it nor pressing forward. "It isn't punishment, what you're carrying. There's no virtue in keeping it."
>
> "I know that." The soldier's jaw tightened. "One of ours went down beside me tonight. If this goes quiet" — he nodded, barely, at his own chest — "he goes with it. I'm not ready to let go of both at once."
>
> It was not, Raphael understood, a refusal born of fear, and nothing in his long service had ever taught him to press past a soul that knew exactly what it was choosing and chose it anyway. He had healed grief before by simply outlasting a man's resistance to it, patient work that eventually won through even the most stubborn refusals. This felt different, and he trusted the difference enough not to test it.
>
> He withdrew Veritas without another word, no argument, no further offer of the light the soldier had just refused. He stayed a moment longer than the refusal strictly required, kneeling there in a silence that asked nothing further of either of them, and let the soldier keep what he had chosen to keep. Then he rose, and moved on to the next soldier waiting in the line, carrying the small, unresolved weight of a man he hadn't been permitted to help.

**ES:**

> Se movió hacia el siguiente soldado antes de que el pensamiento pudiera asentarse más, y encontró a este ya en guardia, no aliviado sino en algo más parecido al rechazo. La mano del soldado se alzó cuando la luz de Veritas se acercó a él, cerrándose alrededor del asta del báculo y apartándolo con firmeza —no un respingo, no el reflejo de un hombre con dolor, sino un rechazo deliberado y firme como Rafael rara vez había encontrado en nadie a quien hubiera venido a sanar.
>
> —Déjalo —dijo el soldado, bastante bajo como para que apenas llegara más allá de los dos. Tenía los ojos secos ya, aunque los surcos de lágrimas anteriores todavía le marcaban el rostro—. No quiero que se vaya todavía.
>
> Rafael mantuvo el báculo donde estaba, sin retirarlo ni presionar hacia adelante. —No es un castigo, lo que llevas encima. No hay virtud en conservarlo.
>
> —Lo sé. —La mandíbula del soldado se tensó—. Uno de los nuestros cayó a mi lado esta noche. Si esto se calla —asintió, apenas, hacia su propio pecho—, se va con él. No estoy listo para soltar los dos a la vez.
>
> No era, comprendió Rafael, un rechazo nacido del miedo, y nada en su largo servicio le había enseñado jamás a presionar más allá de un alma que sabía exactamente qué estaba eligiendo y lo elegía de todos modos. Había sanado el duelo antes simplemente sobreviviendo más que la resistencia de un hombre a él, un trabajo paciente que a la larga se abría paso incluso a través de las negativas más tercas. Esto se sintió distinto, y confió en la diferencia lo suficiente como para no ponerla a prueba.
>
> Retiró a Veritas sin una palabra más, sin discutir, sin ofrecer de nuevo la luz que el soldado acababa de rechazar. Se quedó un momento más de lo que el rechazo exigía en sentido estricto, arrodillado ahí en un silencio que no le pedía nada más a ninguno de los dos, y dejó que el soldado conservara lo que había elegido conservar. Después se levantó, y siguió hacia el siguiente soldado que esperaba en la fila, cargando el peso pequeño y sin resolver de un hombre al que no se le había permitido ayudar.

---

## Subtrama #9 — Remiel: las visiones que se niegan a coincidir

### Cap. 12 — ampliación del párrafo existente

Insertado después de "She had seen this kind of quiet before, in armies about to lose a war they didn't yet know they were losing." / "Ya había visto este tipo de silencio antes, en ejércitos a punto de perder una guerra que todavía no sabían que estaban perdiendo." y antes de "She found herself near Miguel's chambers again by midday" / "Se encontró de nuevo cerca de las cámaras de Miguel hacia el mediodía". No se revela ningún futuro concreto ni verificable — la frustración es puramente profesional (un instrumento que deja de rendir un solo resultado limpio).

**EN:**

> Then, for the length of a single breath, it did have something to tell her. The Spiral flared to life at her side without warning, and instead of the single clean thread she was trained to read, it threw up three at once, overlapping, each one insisting on itself with equal weight. She caught fragments of each before they collapsed back into stillness — enough to know they contradicted each other in ways that mattered, not enough to know which one, if any, deserved to be believed. The Spiral had never done that before. It had disagreed with itself on details, occasionally, the way any instrument reading a moving target might blur at the edges. It had never handed her three separate futures and refused to rank them.
>
> She stood very still until the light dimmed again, running through the same diagnostics she'd have run on any other captain's report that returned three incompatible readings from one instrument — recalibration, interference, a flaw in her own attention rather than the Spiral's. None of them held up. The Spiral had shown her exactly what it meant to show her; it simply meant three things at once, and expected her to carry all three without being told which one to trust.
>
> There was no one in the war room she could bring this to. A malfunctioning weapon, she could report. A captain doubting her own reading, she could manage alone and say nothing about. But a working instrument that had simply stopped agreeing with itself — that had no report format, no precedent in three centuries of service, and no colleague standing near enough tonight who wouldn't hear it as exactly the kind of uncertainty this room could not currently afford to add to its own. She let the Spiral go dark again and said nothing, filing the moment away the only place she had left to put it.

**ES:**

> Entonces, por la duración de una sola respiración, sí tuvo algo que decirle. El Espiral se encendió a su lado sin previo aviso, y en vez del hilo único y limpio que estaba entrenada para leer, le lanzó tres a la vez, superpuestos, cada uno insistiendo en sí mismo con el mismo peso. Alcanzó a captar fragmentos de cada uno antes de que volvieran a colapsar en quietud —lo suficiente para saber que se contradecían entre sí de maneras que importaban, no lo suficiente para saber cuál, si es que alguno, merecía creerse. El Espiral nunca había hecho eso antes. Había discrepado consigo mismo en detalles, ocasionalmente, del modo en que cualquier instrumento que lee un objetivo en movimiento puede desenfocarse en los bordes. Nunca le había entregado tres futuros distintos y se había negado a ordenarlos.
>
> Se quedó muy quieta hasta que la luz volvió a apagarse, repasando los mismos diagnósticos que habría aplicado al informe de cualquier otro capitán que le devolviera tres lecturas incompatibles del mismo instrumento —recalibración, interferencia, un fallo en su propia atención antes que en el Espiral—. Ninguno se sostenía. El Espiral le había mostrado exactamente lo que quería mostrarle; simplemente significaba tres cosas a la vez, y esperaba que ella cargara con las tres sin que se le dijera cuál confiar.
>
> No había nadie en la sala de guerra a quien pudiera llevarle esto. Un arma con fallas, podía reportarlo. Una capitana dudando de su propia lectura, podía manejarlo sola y no decir nada al respecto. Pero un instrumento en pleno funcionamiento que simplemente había dejado de estar de acuerdo consigo mismo —eso no tenía formato de informe, ningún precedente en tres siglos de servicio, y ningún colega lo bastante cerca esa noche que no fuera a oírlo como exactamente el tipo de incertidumbre que esta sala no podía permitirse sumar a la suya en este momento. Dejó que el Espiral volviera a apagarse y no dijo nada, archivando el momento en el único lugar que le quedaba para guardarlo.

### Cap. 51 — ampliación de la línea existente (eco del cap. 12)

Único cambio permitido en el cap. 51: la línea coral de Remiel. Zona sagrada (escena Belial/teniente, párrafo final del colgante) no tocada. Se editó también, idéntico, el espejo `project/Chronicles_of_the_Sundering_Judgment/chapters/EN/B1C28_EN.md` — la línea original ahí era byte-idéntica a `Libro1/EN/51`, verificado antes de editar.

**EN** (línea original + ampliación, ambas en `Libro1/EN/51` y `B1C28_EN.md`):

> Remiel watched her own shadow flicker against the wall, tracing futures that kept refusing to agree with each other — the same three futures the Spiral had thrown at her once before, still unresolved now that the fighting itself had ended. She had stopped expecting the disagreement to close. Whatever came after tonight, the shape of it hadn't decided on itself yet, and no reading she owned was going to force it to.

**ES:**

> Remiel observaba su propia sombra parpadear contra la pared, trazando futuros que seguían negándose a coincidir entre sí —los mismos tres futuros que el Espiral le había lanzado una vez antes, todavía sin resolverse ahora que el combate mismo había terminado. Había dejado de esperar que el desacuerdo se cerrara. Fuera lo que fuese lo que viniera después de esta noche, su forma todavía no se había decidido, y ninguna lectura que ella poseyera iba a obligarla a hacerlo.

No se revela ningún futuro concreto ni verificable — la ampliación deja claro (para el lector atento) que el don de Remiel no está fallando: es el futuro mismo, tras la caída de Miguel, el que sigue genuinamente indeciso.

---

## Verificación final

- `git diff --stat` sobre los 11 archivos tocados: inserciones EN/ES exactamente parejas en cada capítulo (11: +4/+4, 12: +6/+6, 45: +18/+18, 46: +12/+12, 51: 1 línea modificada en los tres archivos).
- Ninguna réplica de diálogo preexistente fue alterada; toda inserción se hizo con `Edit` puntual sobre el texto leído primero.
- No se tocaron `Libro1/EN|ES/29`, `33`, `40` (modificados por otra sesión en paralelo, fuera de este lote).
- No se tocó la zona sagrada del cap. 51 (escena Belial/teniente ni el párrafo final del colgante).
