# Auditoría de coherencia — Hilo 26: Eje diplomático Cielo-Infierno / Concordato de Ceniza

**Fecha**: 2026-08-22
**Auditor**: agente de coherencia (solo lectura, sin ediciones de prosa)
**Fuente de referencia**: `design_notes/2026-08-22_coherence_audit_thread_map.md` (Hilo 26, líneas 446-456)
**Alcance leído, en orden**:
- Libro1/EN: `39_The_Rift_That_Shouldnt_Exist.md`, `40_What_Not_Even_He_Can_Control.md`, `41_A_Truce_Neither_Will_Admit_To.md`, `42_What_Goes_Unspoken.md` (Hollowseam)
- Libro3/EN: `12_The_In-Between_War.md`, `24_A_Truce_of_Shadows_and_Light.md`, `25_The_Logic_of_the_Adversary.md`, `28_The_Concordat_of_Ash.md`, `29_The_Uneasy_Vanguard.md`, `34_The_Fleet_of_Dawn_and_Dusk.md`, `42_The_Sovereigns_Farewell.md`, `49_The_New_Pantheon.md`
- Verificación cruzada por `grep` en los 159 capítulos (Libro1/EN, Libro2/EN, Libro3/EN completos) para toda co-ocurrencia de "Camael"+"Vepar" y "Gabriel"+"Lucifer"/"Vepar"/"Hell"

**Conclusión general (spoiler del informe)**: sobre el estado actual de la prosa (no del outline), **no encontré ninguna de las dos contradicciones que el mapa de hilos marcaba como "ya detectadas."** La aritmética de encuentros Camael-Vepar es internamente consistente cuando se leen `L3/12` y `L3/29` juntos, y la afirmación de Gabriel sobre su "primer trato con el Infierno" no choca con Hollowseam ni con Turein porque el propio texto explica por qué Gabriel no podría saber de esos precedentes. Si un repaso anterior detectó una contradicción real aquí, probablemente vivía en el outline (`arco_argumental_completo.md`, ya marcado como superado) o ya fue corregida en la prosa aprobada. Ver el punto 3 para las reservas que sí dejo abiertas.

---

## 1. Conteo de encuentros Camael-Vepar

### Evidencia textual, capítulo por capítulo

**`Libro3/EN/12_The_In-Between_War.md`** (línea 29-31, POV Vepar): antes de que la brecha se abra entre las dos flotas, el segundo de Vepar pregunta:
> "You've fought this one before?" his second asked, nodding toward the gold ranks across the gap.
> "Twice," Vepar said. "He didn't win either time, and he didn't lose cleanly either."

Esto establece **dos enfrentamientos previos**, ninguno mostrado en página (ni en Libro1 ni en Libro2 — confirmado por grep, ver sección 1.2 abajo), ocurridos *antes* del capítulo 12. El encuentro del capítulo 12 en sí (la formación frente a frente, interrumpida por el vacío/Thamorak) sería entonces el **tercero**.

Esto se confirma en el propio capítulo 12 (línea 85, POV Vepar), ya durante la crisis del vacío:
> "He had fought this angel twice before, had studied his tactics closely enough to predict most of what the man was likely to do in any given engagement."

**`Libro3/EN/29_The_Uneasy_Vanguard.md`** (línea 9-11, POV Camael), en la primera reunión de coordinación logística Camael-Vepar tras el Concordato:
> "He heard Vepar's approach before he saw him, footsteps deliberate on the packed earth outside, unhurried in the same way Camael had come to recognize across three prior meetings on opposing sides of a battlefield gap. This would be their fourth. It would also, he understood, be the first where neither of them was trying to kill the other."
>
> "...with an enemy he'd twice already met across open ground and once watched share his own unshaped dread at something neither of their armies could touch."

Y en la misma escena, línea 21, POV Vepar:
> "He had fought this particular commander three times now, twice on even ground and once interrupted by a horror neither side had been prepared to name..."

### 1.1 Verificación de la aritmética

| # de encuentro | Fuente | Tipo |
|---|---|---|
| 1 | Off-page, mencionado en `L3/12` como "twice" (1 de 2) | Combate |
| 2 | Off-page, mencionado en `L3/12` como "twice" (2 de 2) | Combate |
| 3 | `L3/12_The_In-Between_War.md` (la formación frente a frente interrumpida por el vacío) | Interrumpido por el vacío, sin combate directo entre ambos |
| 4 | `L3/29_The_Uneasy_Vanguard.md` (la tienda de negociación tras el Concordato) | Primer encuentro no hostil, explícitamente numerado "cuarto" |

**Los tres pasajes citados (uno en `L3/12` desde Vepar, dos en `L3/29` desde Camael y desde Vepar respectivamente) coinciden exactamente**: 2 combates previos sin mostrar + el capítulo 12 (interrumpido por el vacío) = 3 encuentros previos, y `L3/29` se autodenomina, por partida doble (ambos POV), el cuarto. No hay discrepancia de conteo entre las dos escenas leídas.

### 1.2 Verificación cruzada en Libro1 y Libro2

Hice `grep` de "Vepar" en los 107 capítulos de Libro1/EN y Libro2/EN. Vepar aparece en 9 archivos (`L1/32`, `L1/34`, `L1/35`, `L1/36`, `L1/37`, `L1/45`, `L2/28`, `L2/29`, `L2/50`), todos relacionados con su rivalidad con Foras o su aparato de inteligencia (Selm). **Ninguno de esos 9 archivos menciona a Camael** (confirmado con `grep "Camael"` sobre cada uno — cero resultados). Es decir, los "dos encuentros previos" que Vepar cita en `L3/12` no están narrados en ningún capítulo de los tres libros; son puro trasfondo referido, nunca contradicho por una escena que los muestre de otra manera. No hay, por tanto, una tercera fuente en Libro1/Libro2 que desestabilice el conteo.

También verifiqué, por `grep` sobre los 52 capítulos de Libro3/EN, todos los archivos donde coinciden "Camael" y "Vepar": `12, 28, 29, 30, 34, 35, 37, 39, 40, 41, 49, 51`. De ellos, solo `12` y `29` narran un encuentro directo entre ambos (los demás son menciones de sus fuerzas en batalla conjunta, o menciones de uno por parte de terceros — p. ej. Naamah/Valefar hablando *de* Vepar). El único archivo intermedio que menciona a ambos nombres entre el 12 y el 29 es `L3/28_The_Concordat_of_Ash.md`, pero ahí Camael no aparece en persona: es Lucifer quien dice "Vepar and Camael will coordinate the details" (línea 21), una instrucción, no un encuentro. **No hay, por tanto, un encuentro no contado entre el 3º (cap. 12) y el 4º (cap. 29).**

### 1.3 Veredicto sobre este punto

**No encontré contradicción.** La cifra "cuarto encuentro" en `L3/29` es matemáticamente consistente con "twice" (cap. 12) + el propio capítulo 12 = 3 previos. Si el repaso anterior marcó esto como contradictorio, sospecho que comparaba la prosa contra el outline (`arco_argumental_completo.md`, ya invalidado explícitamente para el tramo B3C087 en adelante) en vez de comparar la prosa consigo misma, o bien la inconsistencia ya fue corregida en una revisión posterior a la que detectó el problema. Recomiendo retirar esta sub-alerta del hallazgo del Hilo 26, o como mínimo marcarla "verificada, sin contradicción en prosa actual" — salvo que el equipo tenga acceso a la nota original que documentaba el hallazgo previo, en cuyo caso valdría la pena cotejarla directamente contra estos pasajes.

---

## 2. "Primer trato con el Infierno" de Gabriel

### 2.1 La afirmación en `L3/24`

`Libro3/EN/24_A_Truce_of_Shadows_and_Light.md`, línea 5 (narración en POV Gabriel, antes de su primera reunión con Vepar):
> "He had negotiated treaties before, truces struck between factions that at least shared a common language of diplomacy. He had never once negotiated anything with Hell directly, and found the unfamiliarity of it settling into his chest with a weight he hadn't fully anticipated carrying."

Esta es una afirmación de narrador (no diálogo), aplicada específicamente a **negociar** con el Infierno — no a "tratar" con él en sentido amplio.

### 2.2 La afirmación relacionada en `L3/28`

`Libro3/EN/28_The_Concordat_of_Ash.md`, línea 35 (POV Gabriel, en su primer encuentro cara a cara con Lucifer mismo, no con Vepar):
> "He had heard a great deal, secondhand, about the particular contempt Lucifer brought to every dealing with Heaven, relayed through envoys and captured reports across an age of indirect war. Facing it directly for the first time, he found himself unable to immediately name what exactly had shifted between the reputation and the man actually standing in front of him."

Esta es una afirmación distinta y compatible: es la primera vez que Gabriel **se enfrenta personalmente a Lucifer**, no una repetición de la afirmación de `L3/24`. El texto distingue correctamente "primera negociación directa con el Infierno" (con Vepar, cap. 24) de "primer encuentro cara a cara con Lucifer" (cap. 28) — son dos primeras veces distintas y compatibles entre sí, no una contradicción.

### 2.3 Contraste con Hollowseam (`L1/39-42`)

Leí los cuatro capítulos completos. Son POV Thoria (Sentinel angélica) y Vem (Squad Leader demoníaco), atrapados junto con sus patrullas en una fisura inestable entre planos. Cooperan tácticamente para sobrevivir (Thoria cura a un soldado demoníaco con Alther; Thoria y Vem coordinan un ataque conjunto sin planearlo) pero **el capítulo cierra explícitamente negando que esto se convierta en un hecho reportado**:

`L1/42`, línea 49:
> "Neither patrol would speak of what had happened on that ground again, not in any report either commander eventually filed, Vem was fairly certain."

Y más explícitamente, líneas 21-27 (POV Thoria) y 29-33 (POV Vem): ambos deciden por separado, y sin coordinarse entre sí, **omitir de sus informes oficiales** la cooperación con el enemigo, precisamente para no tener que responder por ello ante su propia cadena de mando.

**Esto es la explicación textual, no una casualidad**: si ni Thoria ni Vem reportan nunca lo ocurrido en Hollowseam, entonces Gabriel (que no aparece en estos cuatro capítulos y no tiene ningún canal narrativo para enterarse de un incidente deliberadamente silenciado por ambos bandos) no tiene forma de saber que existió. Su afirmación en `L3/24` de que nunca ha negociado con el Infierno **no es refutada por Hollowseam** porque Hollowseam (a) no fue una negociación (fue cooperación de combate improvisada) y (b) nunca llegó a oídos de ningún mando, y mucho menos al suyo.

### 2.4 Contraste con Turein (`L1/31-34`)

No estaba en mi lista de lectura obligatoria pero lo repasé por contexto (vía el mapa de hilos, Hilo 04): Cassiel (angélico) y Selm (demoníaco) investigan por separado la resonancia de Turein, se cruzan, y "ninguno se mata, ambos se van con la mitad de una respuesta." Cassiel reporta a Iofiel, no a Gabriel directamente, y lo que reporta es una pista sobre el origen de Solmire, no un acuerdo con el Infierno. No hay negociación ni trato aquí tampoco — es reconocimiento paralelo, no diplomacia. No contradice la afirmación de Gabriel.

### 2.5 Verificación cruzada: ¿negoció Gabriel con el Infierno antes de `L3/24` en algún punto de Libro1 o Libro2?

Hice `grep` de toda coincidencia "Gabriel" + ("Lucifer" o "Vepar" o "Hell") en los 107 capítulos de Libro1/EN y Libro2/EN. Coincidencias en 9 archivos; revisé el contexto de cada una:
- `L1/54_The_Echo_of_the_Sword.md`: Gabriel propone vigilar en silencio "sin anunciar a Cielo ni a Infierno" — no es contacto con el Infierno, es lo contrario (ocultamiento mutuo).
- `L2/23_A_Thiefs_Legacy.md`, `L2/26_Report_from_the_Abyss.md`: Sariel, enviado por Gabriel, investiga *dentro* del Infierno como espía encubierto — no es Gabriel negociando, es Gabriel recibiendo inteligencia de un agente infiltrado.
- El resto de las coincidencias son menciones incidentales del nombre de Lucifer o de Hell en contexto no relacionado con Gabriel actuando directamente.

**No encontré ninguna escena en Libro1 o Libro2 donde Gabriel negocie personalmente con el Infierno.** La afirmación de `L3/24` se sostiene.

### 2.6 Veredicto sobre este punto

**No encontré contradicción.** El texto distingue correctamente:
- "Primera negociación directa de Gabriel con el Infierno" → cierto, con Vepar, `L3/24`.
- "Primer encuentro cara a cara de Gabriel con Lucifer" → cierto, `L3/28`, afirmación distinta y compatible.
- Hollowseam y Turein no son negociaciones y, en el caso de Hollowseam, el texto explica activamente por qué Gabriel no podría saber de su existencia.

---

## 3. Reservas y recomendaciones

1. **No pude cotejar contra la nota original del "repaso anterior"** que el mapa de hilos cita como fuente de la alerta — no la localicé en mi alcance de lectura. Si existe un documento específico (posiblemente uno de los `expansion_progress_*.md` o una entrada de proceso anterior) que detalla *exactamente* qué contradicción se detectó, vale la pena que alguien la revise directamente contra los pasajes citados arriba en las secciones 1.1 y 2.1-2.2: es posible que la contradicción detectada fuera entre prosa y **outline** (`arco_argumental_completo.md`), no entre prosa y prosa, en cuyo caso ya está cubierta por la advertencia general de que el outline no es canon.
2. **Fuera de mi alcance pero relevante**: no leí `L3/30_Whose_Idea_This_Was_Already.md` en detalle más allá del grep — ahí Naamah observa el arreglo Vepar-Camael desde fuera y dice que "nadie por encima de ninguno de los dos le ha preguntado qué aspecto tiene eso en la práctica." Esto es coherente con el resto (Camael y Vepar coordinando informalmente sin reportarlo con precisión hacia arriba), no contradictorio, pero lo señalo porque refuerza el mismo patrón temático (acuerdos Cielo-Infierno que quedan parcialmente fuera del registro oficial) que ya aparece en Hollowseam. Podría ser intencional como eco temático — no lo marco como hallazgo, solo como observación.
3. **Verifiqué `L3/51_The_Door_No_One_Sealed.md`** (fuera de mi lista, vía grep) porque menciona a Camael y Vepar: confirma que su arreglo sigue siendo informal y no auditado ("built on two commanders' stubborn competence, rather than on any court's careful design") hasta el cierre de la trilogía — consistente con todo lo anterior, sin contradicción.

## 4. Resumen ejecutivo

| Sub-hallazgo del mapa | Estado verificado |
|---|---|
| Aritmética Camael-Vepar ("cuarto encuentro") | **Sin contradicción.** 2 combates off-page + `L3/12` (interrumpido) = 3 previos; `L3/29` se autodenomina 4º, con cifras idénticas desde ambos POV (Camael y Vepar) |
| "Primer trato con el Infierno" de Gabriel | **Sin contradicción.** `L3/24` (primera negociación, con Vepar) y `L3/28` (primer encuentro cara a cara con Lucifer) son afirmaciones distintas y compatibles; Hollowseam y Turein no la contradicen porque no son negociaciones y, en el caso de Hollowseam, el propio texto explica por qué Gabriel nunca se enteraría |

No se encontraron contradicciones numéricas/cronológicas reales en el eje diplomático Cielo-Infierno dentro del alcance auditado. Recomiendo que el equipo de coherencia marque el Hilo 26 como **verificado sin hallazgos** en esta dimensión específica, sujeto a la reserva del punto 3.1 sobre la fuente del repaso anterior.
