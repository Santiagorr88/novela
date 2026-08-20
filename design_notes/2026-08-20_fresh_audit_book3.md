# Auditoría fresca — 5 capítulos nuevos de Libro III (2026-08-20)

**Alcance**: `B3C28pt5_EN.md`, `B3C28pt6_EN.md`, `B3C28pt7_EN.md`, `B3C44pt5_EN.md`, `B3C44pt6_EN.md`. Lectura completa e independiente de los 5 (más `B3C28_EN.md`, `B3C44_EN.md`, `content/lore/personajes.md`, `content/lore/expansion_guidelines.md`, `content/lore/arco_argumental_completo.md`, `content/lore/book3_part2_expanded_beats.md`, `content/lore/book3_part3_expanded_beats.md` y los 5 informes de revisión existentes en `chapters/EN/reports/`). Auditoría de solo lectura — ningún archivo del proyecto fue modificado.

**Nota de método**: cada capítulo ya pasó por un panel de 5 revisores antes de commitearse; esta pasada busca deliberadamente lo que ese proceso, capítulo a capítulo, no podía ver: contradicciones *entre* los 5 capítulos de hoy, y contra el resto del libro ya escrito.

---

## 1. Consistencia cruzada entre los 5 capítulos de hoy

### 1.1 Trío B3C28pt5/6/7 — cronología relativa

- **B3C28pt5** se ancla explícitamente "semanas" después de `B3C28` (la propia línea de cierre de `B3C28_EN.md`: *"...might yet prove worth whatever it kept costing both sides **in the weeks ahead**"*) y dentro de ese margen, "un mes" después (diálogo de Naamah a Vepar: *"you've spent a month holding a line..."*, `B3C28pt5_EN.md` línea 27). Coherente.
- **B3C28pt6** se ancla explícitamente 3 días después del cierre de B3C28pt5 (*"three days back from the Valley's edge"*, `B3C28pt6_EN.md` línea 3), que a su vez coincide con el propio cierre de pt5 (*"Lucifer's court received her three days ahead of Vepar's own courier"*, `B3C28pt5_EN.md` línea 59). Encaje exacto, sin salto ni duplicación.
- **B3C28pt7** **no tiene ningún ancla temporal explícita** relativa a B3C28, pt5 o pt6 — solo su propio marcador interno (*"Leraje's word reached her eleven days later"*, línea 53, relativo a sí mismo). No contradice a los otros dos, pero es el único de los tres sin fijar su posición en la ventana. **Hallazgo, cosmético**: dado que el encargo (`book3_part2_expanded_beats.md` línea 257) confirma que pt7 es "complementario" a pt6 y protege el acuerdo político que Naamah se atribuyó en pt5, sería más robusto anclarlo también con una frase temporal explícita (p. ej. "días después de haber asegurado la legión de Aamon") en vez de dejarlo flotando sin referencia a los otros dos capítulos de la misma ventana.

### 1.2 Trío B3C28pt5/6/7 — hechos asumidos por uno que otro establece

- No se encontró ninguna contradicción real de hecho (estado de la corte de Naamah, número de capitanes, qué sabe la corte de Lucifer) entre los tres. `personajes.md` líneas 1349-1411 confirma que la nota añadida hoy ("Ronove y Dantalion... desde B3C28.6 su lealtad operativa es a Naamah") documenta correctamente lo que pt6 dramatiza, y que pt5/pt7 nunca asumen ese reclutamiento como ya ocurrido (pt5 es anterior; pt7 no lo menciona ni lo necesita). Limpio.

### 1.3 Pareja B3C44pt5/pt6 — compatibilidad de detalles compartidos

- El dato compartido explícito — "Foras marchó una cuarta vez esta semana, y fracasó una cuarta vez" — es textualmente coincidente entre `B3C44pt5_EN.md` (línea 5, diálogo de Agares + línea 41, cifra corregida de Amy a "every one of them his") y `B3C44pt6_EN.md` (línea 5). Correcto, ya verificado también por el panel de revisión original.
- Jerarquía de mando verificada línea por línea contra `personajes.md`: Amy y Flauros bajo **Agares** (líneas 1763-1787), Valefar y Vine bajo **Vepar** (líneas 2090-2115). Correcto en ambos capítulos.
- **Hallazgo, menor** (ver sección 3.3 abajo): la premisa de fondo de `B3C44pt6` — una "shared line" activa, vigilada, con soldados de Camael y la flota de Vepar en tensión mutua — no está claramente reconciliada con el estado de "no hay ninguna frontera que valga la pena vigilar" que `B3C44_EN.md` (el capítulo ancla de la misma semana) atribuye explícitamente a Camael/Cielo.

---

## 2. Disciplina de POV (reglas B3C20 y B1C15)

Regla B3C20 (`expansion_guidelines.md` línea 153): ninguna generalización sobre el carácter/historia de un tercero puede narrarse como hecho — debe enmarcarse explícitamente como memoria/inferencia del propio POV ("she judged", "she thought", "he found himself wondering..."), incluso si es una generalización basada en conocimiento legítimo previo.
Regla B1C15 (línea 344): esa misma disciplina aplica también a certezas del propio ancla sobre el interior de OTRO personaje presente en su escena (no solo personajes claramente ajenos), y en particular a adverbios de certeza ("plainly", "clearly", "genuinely") pegados a estados internos ajenos.

Los 5 informes de revisión (`chapters/EN/reports/*.md`) ya corrigieron varias instancias de este patrón. Una relectura completa encontró instancias adicionales que sobrevivieron a esa revisión — todas del mismo tipo (generalización sobre el carácter/estado interno de un tercero, narrada como hecho en vez de como inferencia del POV):

| # | Archivo:línea | Cita | Problema |
|---|---|---|---|
| 1 | `B3C28pt5_EN.md:5` | *"In all the small services he'd done her, he had made a habit of never asking what she wanted a room to feel like before he arrived in it — the closest thing to loyalty he'd ever shown her."* | Afirma la lealtad histórica de Gusion como hecho narrado, no como juicio de Naamah. |
| 2 | `B3C28pt5_EN.md:13` | *"Gusion's smile was the smile of a man who enjoyed watching a gap in a contract before anyone else noticed it was there."* | Generalización de carácter sin marco de inferencia. |
| 3 | `B3C28pt6_EN.md:11` | *"Gusion took it from her, unhurried, the way a man behaves when he already half-suspects he'll enjoy the answer."* | Atribuye expectativa interna a Gusion como hecho. |
| 4 | `B3C28pt6_EN.md:15` | *"Gusion's smile was the smile of a man who had already half-guessed the answer before he'd been asked to find it."* | Mismo patrón que #3, repetido dos líneas después. |
| 5 | `B3C28pt7_EN.md:9` | *"Phenex arrived first, as he generally did, sweeping into her hall the way a man arrives at an entrance he's rehearsed."* | Generalización de hábito/carácter sin marco. |
| 6 | `B3C28pt7_EN.md:25` | *"Phenex's whole posture sharpened, the delight of a moment ago narrowing into something closer to real interest."* | Transición de estado interno de Phenex narrada como hecho. |
| 7 | `B3C28pt7_EN.md:35` | *"Leraje considered this, and let it go with the plain, unbothered shrug of someone who'd gotten more of an answer than she'd expected and had no further use for the rest."* | Afirma la expectativa previa de Leraje como hecho. |
| 8 | `B3C44pt5_EN.md:3` (línea de apertura) | *"Agares never simply told her what he wanted. He folded it inside a longer observation instead, and left her to do the unfolding herself."* | Generalización de carácter de Agares en la primerísima línea del capítulo, antes de cualquier anclaje de POV — narración omnisciente, no inferencia de Amy. |
| 9 | `B3C44pt5_EN.md:27` | *"Flauros found her patience harder to watch than the soldier found her questions."* | Afirma el estado interno de DOS terceros a la vez (Flauros y el soldado) en una comparación narrada como hecho — el caso más claro del lote. |
| 10 | `B3C44pt6_EN.md:19` | *"...the particular economy of a man who considered small talk a wasted key on a lock that didn't need one."* | Generalización sobre la filosofía de Valefar desde el bloque POV de Vine, sin marco de inferencia. Reutiliza además, sin que ningún revisor de esta sesión lo detectara, el mismo andamiaje "the [adj.] X of a [noun] who Y" que los informes de `B3C28.5/.6/.7` identificaron y eliminaron explícitamente como tic — reaparece aquí porque `B3C44.5/.6` pasaron por un panel de revisión distinto y en paralelo. |

**Severidad**: menor en los 10 casos — ninguno afirma un hecho de trama, cambia una decisión de personaje o revela algo prematuro; todos son el mismo tipo de deslizamiento de encuadre narrativo que el propio proceso del proyecto ya trata como "fix requerido" cuando lo detecta durante la revisión. Se listan agrupados porque el patrón es idéntico y probablemente se corrige con una sola pasada de "buscar generalizaciones de carácter de terceros sin 'she judged/she thought'" sobre los 5 archivos.

---

## 3. Continuidad con el resto de Libro III

### 3.1 Nombres, rangos, armas — verificado contra `personajes.md`

Todos correctos, sin excepción:
- Naamah — *Neriah* (velo), personalidad "enchanting, ambiguous, impossibly persuasive" (líneas 1337-1345): consistente en los 3 capítulos del trío.
- Gusion — *Veritas Inversa* (pluma), "calculating, manipulative" (1405-1411): consistente.
- Ronove — mazos gemelos, cuatro brazos, "animalistic, brutish, laughs while killing" (1353-1359): consistente en `B3C28pt6`.
- Dantalion — *Mnemosyn* (esfera), "cold, curious, intellectually twisted" (1373-1379): consistente.
- Phenex — *Degeneris* (pincel), "dramatic, eccentric, flamboyantly theatrical" (1385-1391): consistente en `B3C28pt7`.
- Leraje — *Mors* (arco), "sarcastic, taunting, lethally precise" (1395-1401): consistente.
- Agares — *Logomante* (no empuñada en escena, coherente al no ser un capítulo de combate), voz bífida en tonos contradictorios (1723-1730): consistente en `B3C44pt5`.
- Amy — *Laberynthus* (cubo), "philosophical, cruel, demolisher of convictions" (1781-1787): consistente.
- Flauros — *Aflame* (látigo), "furious, impatient" (1765-1771): consistente.
- Valefar — *Oblivion* (llave), "precise, meticulous, paranoid" (2100-2106): consistente en `B3C44pt6`.
- Vine — *Ferox* (flauta), "instinctive, savage, unpredictable" (2108-2114): consistente (y ya corregido en revisión previa por sonar demasiado parecido en cadencia a Valefar).
- Jerarquía: Ronove/Dantalion bajo Aamon→reclutados por Naamah (nota 2026-08-20 ya en `personajes.md` línea 1351); Phenex/Leraje/Gusion bajo Naamah (1383); Amy/Flauros bajo Agares (1763); Valefar/Vine bajo Vepar (2090). Los 5 capítulos respetan esta jerarquía sin excepción.

### 3.2 Regla Michael/Miguel

Ningún capítulo de los 5 menciona a Michael/Miguel/Mikel en ninguna forma (`grep` sin resultados en los 5 archivos). Regla no aplica, sin riesgo.

### 3.3 Regla Thamorak/Forgotten — reveal-pacing

- El trío `B3C28pt5/6/7` (ambientado antes de `B3C35`, el clímax de Thamorak) no menciona la entidad en ningún momento — limpio por ausencia total, sin riesgo de adelanto.
- La pareja `B3C44pt5/6` (ambientada después de `B3C35` y `B3C43`, con el asunto ya resuelto y de conocimiento público en el propio `B3C44_EN.md`) menciona "Thamorak's collapse" y "Thamorak's old chaos" (`B3C44pt6_EN.md` líneas 15, 55) en un registro coloquial/observacional (un domador de bestias describiendo el fenómeno desde fuera, no una explicación técnica) — no contradice el mecanismo ya fijado ("reintegrado como entropía natural" en `B3C35`) ni revela nada que un soldado de a pie no supiera ya en ese punto de la línea temporal. Sin riesgo.
- **Hallazgo, menor** (detalle que sí conviene señalar, ligado a §1.3): `B3C44pt6` construye toda su premisa sobre una "shared line" activa entre la flota de Vepar y "Camael's men" — vigilada, con hogueras de vigilia, soldados en tensión mutua, y Valefar auditando *"every point of contact along the shared line, every soldier on either side with access to more than his own orders"* (`B3C44pt6_EN.md` líneas 39, 49). Esto convive en la misma semana con `B3C44_EN.md`, donde Gabriel observa a Camael pidiendo repetidamente "a standing honor guard, a border patrol" y recibe la misma respuesta cada vez: *"there was, for now, genuinely nothing left standing at any border worth guarding"* (`B3C44_EN.md` línea 7). Las dos cosas son técnicamente reconciliables (Camael podría estar personalmente desvinculado de una guarnición residual que sigue en pie bajo un oficial subalterno, y de hecho el tema recurrente de los 5 capítulos de hoy es precisamente "nadie por encima de cierto rango se ha molestado en comprobar los detalles") — pero tal como está escrito, un lector atento puede leer una tensión real entre "no queda ninguna frontera que valga la pena vigilar" (voz de Cielo, capítulo ancla) y "una frontera compartida activa que un capitán audita por miedo a una traición" (voz de Hell, interludio del mismo día). Recomendado: una frase de enlace en cualquiera de los dos capítulos que aclare explícitamente que la guarnición de Camael en la línea compartida quedó desatendida por el propio Cielo mientras Camael personalmente ya no tiene mando de campo — encaja con el motivo ya establecido de negligencia burocrática que recorre el resto del lote de hoy, pero ahora mismo queda implícito, no escrito.

### 3.4 Citas del outline

- **Hallazgo, menor**: la nota de diseño de `B3C28pt6` en `content/lore/book3_part2_expanded_beats.md` línea 243 justifica la premisa del "vacío burocrático" de la legión huérfana de Aamon citando *"la 'Hell fracturada en tres cortes' que ya recorre el resto del arco (ver `arco_argumental_completo.md` líneas 1710-1711)"*. Verificado: las líneas 1710-1711 de `arco_argumental_completo.md` son la entrada **B3C115 "Three Courts, Not One"**, que pertenece íntegramente al bloque de entradas **B3C087-125** marcado explícitamente `SUPERADO, 2026-08-20` en la línea 1572 del mismo documento (*"la prosa ya escrita y aprobada no siguió"* esa versión del clímax/cierre; entradas B3C113-116 en particular describen una sucesión formal de Belial, una petición de Foras y una reunión de Balam que la prosa real de `B3C30-B3C45` no siguió). La cita, tal como está redactada en la nota de diseño, presenta una entrada superada como si fuera contexto de canon vigente para justificar `B3C28pt6`.
  - **Impacto real en la prosa**: ninguno. La premisa real de `B3C28pt6` (la legión de Aamon "scattered and leaderless" sin reasignar, `B1C13_EN.md`) está sólidamente anclada por sí sola, sin necesidad del concepto de "tres cortes" — el propio capítulo nunca menciona "tres cortes" en ningún momento del texto (verificado por lectura completa). El error está confinado a la nota de justificación del documento de planificación, no al capítulo publicado.
  - **Por qué igualmente vale la pena corregirlo**: `expansion_guidelines.md` (línea 38) declara ese tipo de documento como "fuente de verdad" para procesos automatizados futuros; dejar una cita a una entrada SUPERADA sin marcar, presentada como vigente, es exactamente el tipo de fuga que podría contaminar una sesión futura que confíe en la nota sin volver a verificar la fuente citada.

---

## 4. Resumen ejecutivo

**Total de hallazgos: 15.** Bloqueantes: **0**. Menores: **13**. Cosméticos: **1** (más un capítulo, `B3C28pt7`, confirmado limpio salvo sus 3 hallazgos de POV ya listados en la tabla).

Ningún capítulo queda completamente libre de hallazgos, pero **ninguno de los 15 es una contradicción de trama, de cronología dura, de ficha de personaje o de reveal-pacing** — los tres tipos de problema real que esta auditoría buscaba activamente. Los tres más importantes:

1. **Cita rota a entrada SUPERADA del outline** (§3.4): la nota de diseño de `B3C28pt6` en `book3_part2_expanded_beats.md:243` cita `arco_argumental_completo.md` líneas 1710-1711 (entrada B3C115) como si fuera contexto vigente, cuando esa entrada pertenece al bloque B3C087-125 explícitamente marcado `SUPERADO` desde la línea 1572 del mismo documento. No contamina la prosa publicada, pero sí una nota de "fuente de verdad" que sesiones futuras podrían confiar sin re-verificar.
2. **Tensión sin resolver entre "no hay frontera que vigilar" (B3C44, voz de Cielo) y la "shared line" activamente auditada de B3C44pt6** (§3.3): reconciliable en teoría (encaja con el motivo de negligencia burocrática del resto del lote) pero no reconciliada por escrito — vale una frase de enlace.
3. **Patrón de generalización de terceros sin marco de inferencia (reglas B3C20/B1C15), 10 instancias repartidas en los 5 capítulos** (§2): ninguna cambia un hecho de trama, pero es exactamente la clase de hallazgo que el propio pipeline de revisión del proyecto trata como corrección obligatoria cuando lo detecta — aquí sobrevivió porque `B3C44.5/.6` se revisaron en un panel paralelo distinto al del trío `B3C28`, y dos instancias del trío se colaron pese a que ese mismo panel ya había cazado y corregido el patrón en otras líneas del mismo capítulo.

No se encontró ninguna contradicción de cronología dura dentro del trío `B3C28pt5/6/7` ni dentro de la pareja `B3C44pt5/pt6`; los nombres, rangos y armas de los 12 personajes involucrados cuadran línea por línea con `personajes.md`; la regla Michael/Miguel no aplica (cero menciones); y no se detectó ninguna fuga prematura de lore sobre Thamorak/los Forgotten en ninguno de los 5 capítulos.
