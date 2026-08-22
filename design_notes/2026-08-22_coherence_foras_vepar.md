# Auditoría de coherencia — Hilo Foras vs. Vepar (Hilos 07 y 12)

**Fecha**: 2026-08-22
**Alcance**: rivalidad Foras/Vepar y sus capitanes a través de los 3 libros.
**Método**: lectura completa y en orden de los 20 capítulos asignados (Libro1/EN: 18, 21, 32, 35, 36, 37, 45; Libro2/EN: 28, 29, 50; Libro3/EN: 12, 24, 29, 30, 34, 35, 41, 49, 50, 51), más Libro2/EN/16 (muerte de Malthus, fuera de la lista pero necesaria como referencia de verdad) y un grep de "Malthus" sobre los 52 capítulos de Libro3/EN para verificar ausencia/presencia de referencias póstumas. Fuente de verdad: `2026-08-22_coherence_audit_thread_map.md`, secciones 2 (Hilos 07/12) y 3 (registro de vida/muerte).

---

## Hallazgo 1 (real) — El patrón "Foras fracasa una cuarta vez" cuenta dos historias distintas según el capítulo

**Archivos**: `Libro3/EN/49_The_New_Pantheon.md` vs. `Libro3/EN/50_What_the_Cube_Found.md` y `Libro3/EN/51_The_Door_No_One_Sealed.md`

**Pasaje — L3/49 (POV Asmodeus)**:
> "Asmodeus had watched three separate claimants make that march already, each announcing his particular flavor of cruelty to the assembled court as though the announcement alone settled the matter, and had watched all three retreat, in turn... **Foras** preached his usual sermons about the purity of dominance to soldiers whose eyes... had stopped following him... Vepar, characteristically, had simply declined to compete at all..."
> más adelante: "He thought, watching **the fortress's latest claimant** storm out empty-handed **for a fourth time**, of the small, dwindling faction..."

**Pasaje — L3/50 (diálogo Agares/Amy)**:
> "'**Foras** marched on the fortress **a fourth time** this week,' he said... 'And a fourth time, his soldiers watched him do it rather than following him into it.'"
> Amy, más tarde, al soldado: "I've watched **four separate marches** on that fortress fail this week alone — **every one of them his**."
> El soldado, aportando cronología interna: "Kaeth... died believing it, second march on the fortress, the one before this week's."

**Pasaje — L3/51 (POV Valefar / Vepar)**:
> "**Foras had marched** on Belial's empty fortress a fourth time that week and failed a fourth time, his own soldiers watching him do it rather than following him in."
> "Word had reached him already, secondhand, of **Foras's** fourth failed march on the empty fortress that same week..."

**Por qué es una incoherencia real**: L3/50 y L3/51 son completamente inequívocos y mutuamente consistentes — dos POV distintos (Agares/Amy y Valefar/Vepar) confirman, con las mismas palabras, que fue **Foras personalmente** quien marchó **cuatro veces**, **todas dentro de la misma semana**, y que sus propios cuatro fracasos son el objeto del "cuarta vez". El testimonio del soldado (Kaeth murió en la "segunda marcha... la de antes de esta semana") corrobora que las cuatro marchas pertenecen a una sola racha, de un solo comandante, en un solo tramo de tiempo corto.

L3/49, sin embargo, monta la escena de un modo que un lector natural interpreta de otra forma: "Asmodeus había visto **tres pretendientes distintos** hacer esa marcha ya... y vio **retirarse a los tres**" — tres individuos, no Foras (a quien el texto introduce en la frase siguiente, por separado, como un caso aparte: "Foras preached his usual sermons..."). Solo después, la frase "the fortress's latest claimant storm out... for a fourth time" retoma el conteo — pero como viene inmediatamente después de establecer que ya hubo *tres pretendientes distintos* (no Foras) fracasando, la lectura más natural en ese punto es que el "cuarto pretendiente" es una **cuarta persona distinta** (posiblemente el propio Foras, pero contado como el cuarto nombre en una lista de señores distintos, no como su cuarto intento personal). Esto choca con L3/50-51, donde no hay "tres pretendientes distintos" en absoluto: los cuatro fracasos pertenecen todos a Foras, en la misma semana, sin mención de ningún otro señor intentándolo.

En otras palabras: L3/49 monta un Infierno en plena disputa dinástica con **varios señores distintos** disputándose el trono vacío (cuadro político amplio, "meses" de duración, según abre el capítulo: "in the handful of months since the man's... dissolution"), mientras que L3/50-51 reducen ese mismo "cuarto fracaso" a la **obstinación personal de un solo comandante** repitiendo la misma marcha cuatro veces **en una sola semana**. Ambas versiones usan literalmente el número "cuarta vez", lo cual sugiere que se pretendía el mismo evento — pero el mecanismo narrativo (quién marcha, cuántos individuos, en qué escala de tiempo) es incompatible entre capítulos.

**Arreglo mínimo propuesto** (no aplicado): en L3/49, sustituir la ambigüedad de "the fortress's latest claimant" por una referencia explícita a Foras ("Foras himself, storming out empty-handed for a fourth time that week alone"), y aclarar que los "tres pretendientes distintos" fracasaron en los meses *anteriores* a que Foras iniciara su propia racha de marchas repetidas — de modo que el lector entienda que los tres señores y las cuatro marchas de Foras son dos fenómenos separados y consecutivos, no el mismo conteo. Alternativamente, ajustar L3/50-51 para reconocer que Foras fue precedido por otros pretendientes, sin necesidad de que sus cuatro marchas ocurrieran "todas esta semana". Cualquiera de las dos vías basta — el problema es de una o dos frases, no estructural.

---

## Hallazgo 2 (verificado, sin incoherencia) — Muerte de Malthus

**Archivos revisados**: `Libro2/EN/16_A_Category_No_One_Has.md` (evento), `Libro2/EN/28_The_Tide_Remembers.md`, `Libro2/EN/29_The_Grief_They_Mistook_for_Softness.md`, y grep de "Malthus" sobre los 52 capítulos de `Libro3/EN/`.

- L2/16 (POV Camael): Malthus ataca a un mortal (Milo Ray/Ereloth, aunque el capítulo no lo nombra) creyéndolo relacionado con Miguel, y es desintegrado sin dejar rastro — "there was simply less of him than there had been, and then nothing."
- L2/28 abre explícitamente: **"The same night the crossroads claimed Malthus..."** — coincide exactamente con el evento y la noche de L2/16.
- L2/29 abre con **"the dead soldier's arm"** de un superviviente y "word of Malthus reached his workshop" — Malthus es tratado como muerto, sin ambigüedad, por Marbas y Raum.
- Grep sobre los 52 capítulos de `Libro3/EN/`: **cero coincidencias** de "Malthus". No hay ninguna referencia póstuma en Libro III dentro ni fuera de mi lista — ni consistente ni inconsistente, simplemente ausente.

**Conclusión**: no hay incoherencia. Las referencias en mi lista (L2/28, L2/29) son plenamente consistentes entre sí y con el evento de L2/16. Nadie lo trata como vivo. Confirma lo ya anotado en el mapa de hilos (Hallazgo previo #2): el único problema real con Malthus es de *memoria del proyecto* (el encargo asumía Libro I), no de la prosa.

---

## Hallazgo 3 (observación, no incoherencia) — Salto de escala en la rivalidad directa Foras–Vepar entre Libro II y Libro III

**Archivos**: comparar `Libro1/EN/35-37`, `Libro2/EN/28-29, 50` con `Libro3/EN/12, 24, 29, 30, 34, 35, 41, 49-51`.

En Libro I y Libro II, Foras y Vepar mantienen una rivalidad **directa y activa**: Malthus detecta el sondeo de Stolas, hay un duelo real entre capitanes, insultos calculados ("imaginative captain"), captains de Foras poniéndolo a prueba, y en L2/50 Vepar pregunta abiertamente por "el arreglo entre comandantes" delante de Belial — la disputa es "common knowledge across his court".

En Libro III, dentro de mi lista, **Vepar y Foras no vuelven a interactuar ni a mencionarse mutuamente en ningún capítulo antes de L3/49**. Los capítulos 12, 24, 29, 30, 34, 35 y 41 giran enteramente en torno a la alianza Vepar–Camael contra Thamorak; Foras está completamente ausente de esas siete unidades. Cuando reaparece la rivalidad en L3/49-51, se presenta ya resuelta de forma pasiva: Vepar "simplemente declinó competir", sin sentir "ninguna satisfacción particular" al ver fracasar a Foras.

Esto **no es una incoherencia** — se explica narrativamente por la amenaza existencial de Thamorak (que vuelve irrelevante la vieja disputa cortesana) y por la disolución de Belial (que cambia por completo el cálculo político: ya no se trata de competir por su favor, sino por un trono vacante que a Vepar no le interesa). Pero es un salto grande y completamente elidido: nunca se dramatiza el momento en que Vepar deja de ver a Foras como rival activo. Lo dejo anotado como observación menor, no como hallazgo de coherencia, por si el autor quiere una frase puente en algún capítulo intermedio del Libro III (fuera de mi lista) que muestre ese cambio de prioridad en curso, en vez de solo constatarlo ya consumado en L3/49.

---

## Hallazgo 4 — Personajes muertos que reaparecen

No se encontró ningún caso dentro de los capítulos leídos. Malthus (L2/16) no reaparece. Kaeth, mencionado por primera y única vez en L3/50 como soldado muerto "en la segunda marcha", no vuelve a aparecer y no hay contradicción asociada.

---

## Resumen

- **1 hallazgo real**: la aritmética de "cuarta vez" del cierre de Foras (L3/49 vs. L3/50-51) monta dos versiones incompatibles del mismo conteo — varios pretendientes distintos vs. un solo Foras marchando cuatro veces en una semana. Arreglo mínimo: una o dos frases en L3/49 para atar el "cuarto pretendiente" explícitamente a Foras y separar temporalmente a los "tres pretendientes distintos".
- **Muerte de Malthus**: verificada, consistente en toda mi lista y sin referencias póstumas en Libro III.
- **Cronología de la escalada**: sin saltos de motivación que constituyan incoherencia; hay una elipsis grande pero narrativamente justificada entre la rivalidad activa de Libros I-II y su resolución pasiva en Libro III, anotada como observación, no como defecto.
- **Reapariciones sin explicar**: ninguna encontrada en el hilo asignado.
