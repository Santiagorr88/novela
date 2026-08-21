# Auditoría de continuidad y lore — Batch C: 13 interludios del Libro II

**Fecha**: 2026-08-21
**Alcance**: SOLO continuidad y lore (jerarquía, armas/objetos, cronología, terminología, repetición accidental, contradicción contra el núcleo certificado B2C01-40). No se evaluó estilo de prosa, ritmo ni disciplina de POV. Auditoría de solo lectura — no se modificó ningún archivo de capítulo.

## Archivos auditados (orden cronológico real dentro de la novela)

1. `chapters/EN/B2C03pt5_EN.md` — "The First Breach" (Orifiel/Ezequiel)
2. `chapters/EN/B2C03pt6_EN.md` — "What the Hands Are For" (Laila)
3. `chapters/EN/B2C07pt5_EN.md` — "What Even He Does Not Know" (Lucifer)
4. `chapters/EN/B2C08pt5_EN.md` — "The Silence That Doesn't Break" (Balam/Barbas)
5. `chapters/EN/B2C08pt6_EN.md` — "What the Ring Corrects" (Orobas/Malphas bajo Balam)
6. `chapters/EN/B2C10pt5_EN.md` — "A Category No One Has" (Camael/Malthus/Milo Ray)
7. `chapters/EN/B2C21pt5_EN.md` — "The Tide Remembers" (Foras/Vepar)
8. `chapters/EN/B2C21pt6_EN.md` — "The Grief They Mistook for Softness" (Marbas/Raum bajo Foras)
9. `chapters/EN/B2C23pt5_EN.md` — "What the Staff Weighs" (Hadriel/Raguel)
10. `chapters/EN/B2C36pt5_EN.md` — "A Verse Withheld" (Selaphiel/Raziel)
11. `chapters/EN/B2C36pt6_EN.md` — "A Familiar Shape in Borrowed Words" (Lucifer/Agares)
12. `chapters/EN/B2C36pt7_EN.md` — "No One Trained to Hear It" (Eshriel/Jahiel/Zaphiel bajo Raziel)
13. `chapters/EN/B2C36pt8_EN.md` — "A Truth Told First" (Vual/Nymos bajo Agares)

También se leyó completo `content/lore/personajes.md` (fichas de jerarquía/armas) y se consultaron `content/lore/expansion_progress_libro2.md` y `content/lore/expansion_progress_cruzado.md` para fechas de creación y hallazgos previos ya resueltos.

## Nota de contexto importante (no es un hallazgo, afecta el alcance)

Al revisar `expansion_progress_cruzado.md` para reconstruir la cronología de escritura, encontré que la sección "Repaso final completo de los Libros II y III" (líneas 56-73 de ese archivo) — que el encargo original describe como ya certificado y fuera de alcance — en realidad **sí revisó y corrigió** al menos uno de estos 13 interludios: `B2C21.5`, cuyo hallazgo registrado fue "capítulo B2C21.5 sin marcar como flashback" (ya resuelto: el texto actual abre con el ancla temporal explícita "The same night the crossroads claimed Malthus, weeks before Arin's long watch..."). Por la posición de esa sección en el archivo (después de las sesiones que crearon B2C03.5, B2C03.6, B2C07.5, B2C08.5, B2C08.6, B2C10.5, B2C21.5, B2C23.5 y B2C36.5, y antes de las sesiones que crearon B2C21.6, B2C36.6, B2C36.7 y B2C36.8), es probable que 9 de los 13 interludios de este batch ya hayan pasado por ese repaso cruzado, y que solo B2C21.6, B2C36.6, B2C36.7 y B2C36.8 sean genuinamente nuevos frente a esa auditoría. Esto no cambia el resultado de esta auditoría (se revisaron los 13 igual de a fondo), pero explica por qué el corpus resultó más limpio de lo que el encargo hacía esperar. Recomiendo que quien mantenga `expansion_progress_cruzado.md` confirme o corrija esta lectura de fechas si le importa la precisión del tracker.

---

## 1. Jerarquía de personajes

**Resultado: sin hallazgos.** Se verificó cada Captain/Commander nuevo contra `personajes.md` línea por línea:

- Orifiel (Commander) → Ezequiel, Laila, Cassiel (Captains): B2C03.5/B2C03.6 correctos.
- Kaviel (Squad Leader) → Ezequiel (Captain) → Orifiel: correcto en B2C03.5.
- Karin, Yaron (Squad Leaders) → Laila (Captain) → Orifiel: correcto en B2C03.6.
- Balam (Commander, bajo Asmodeus) → Barbas, Orobas, Malphas (Captains): correcto en B2C08.5/B2C08.6.
- Foras (Commander, bajo Belial) → Malthus, Marbas, Raum (Captains): correcto en B2C10.5/B2C21.5/B2C21.6.
- Vepar (Commander, bajo Belial) → Stolas (Captain): correcto en B2C21.5.
- Hadriel, Raguel (Captains) → Selaphiel (Commander): correcto en B2C23.5. Kadan (Squad Leader) → Hadriel: correcto.
- Selaphiel (Commander) → Jophiel (Captain): correcto en B2C36.5.
- Raziel (Commander, bajo Uriel) → Eshriel, Jahiel, Zaphiel (Captains): correcto en B2C36.5/B2C36.7.
- Agares (Commander, bajo Asmodeus) → Vual (Captain) → Nymos (Squad Leader): correcto en B2C36.6/B2C36.8. El propio texto de B2C36.6 verbaliza explícitamente que "Agares answered to Asmodeus in every matter of ordinary chain and rank" y trata el hecho de que pida el visto bueno a Lucifer como una anomalía deliberada (ambición política), no como un error de cadena de mando — está bien manejado, no es una contradicción.

Ningún caso análogo al error real de sesiones anteriores (Ronove/Dantalion asumidos bajo Naamah en vez de Aamon). Todos los interludios nuevos usan el comandante correcto según ficha.

## 2. Continuidad de armas/objetos

**Resultado: sin hallazgos.** Se verificó el arma de cada personaje nuevo contra su ficha y su uso en pantalla:

| Personaje | Arma (ficha) | Uso en el interludio | Consistente |
|---|---|---|---|
| Orifiel | *Muriel* (escudo) | Descrito fusionado al brazo izquierdo, banked low | Sí |
| Ezequiel | *Anamnesis* | Cita textual reutilizada de la ficha ("Only those who forget honor can be wounded by me") | Sí |
| Laila | *Tenura* (guantes) | Entrena bearers, detecta resonancia | Sí |
| Balam | *Furor* | Se alimenta de rabia, golpea más rápido con cada parry absorbido | Sí |
| Barbas | *Dolorim* (aguja) | Perfora recuerdos, busca el "hinge" de la mente | Sí |
| Malphas | *Fortex* | Convoca muros/trampas de piedra | Sí |
| Orobas | *Reversus* (anillo) | Intercambia el destino de dos almas — escenificado literalmente (dos soldados cambian de lugar) | Sí |
| Foras | *Noesis* (espina) | Drena fe e inyecta arrogancia, incluso cuando ya no queda fe que drenar (B2C21.6) | Sí |
| Vepar | *Marea* (tridente) | Controla fluidos/mapea territorio en agua | Sí |
| Marbas | *Tekrion* (implantes) | Instala placas que fuerzan obediencia mecánica | Sí |
| Raum | *Lethae* (espejo) | Atrapa sueños, los convierte en visiones | Sí |
| Hadriel | *Umbría* (daga) | Corta el espacio/la brecha entre realidades | Sí |
| Kadan | *Umbral* (llave) | Hoja en forma de llave, golpe de sellado | Sí |
| Raguel | *Equitas* (bastón) | Pesa la culpa del cautivo | Sí |
| Raziel | *Ignotus* (tomo) | Páginas quemadas en los bordes, "cada verso invoca fuego primordial" | Sí |
| Iofiel | *Memnón* (bastón) | Zumbido bajo y paciente mientras traduce el fragmento | Sí |
| Eshriel | *Helios* (guanteletes) | Estallido incandescente | Sí |
| Jahiel | *Caelum* (espada) | No encuentra corrupción que cortar; solo corta lo corrupto | Sí |
| Zaphiel | *Claris* (lanza) | Ciega y perfora en un solo golpe | Sí |
| Nymos | *Volarien* (máscara) | Refleja lo que el interlocutor ya quiere creer | Sí |

**Codex Mortalis (falso, B2C36.8)**: el estado descrito en B2C36.8 — un documento "más tosco" que Vual usa para sembrar rumor oral en el mercado, y unas "pages" pulidas que Agares envía después a Lucifer para su bendición formal (B2C36.6) — es consistente entre ambos capítulos. No es la misma pieza física reutilizada de forma contradictoria: B2C36.8 es explícitamente el borrador/siembra informal ("rougher... the polish, if the thing ever needed polish, was Agares's business to add later"), y B2C36.6 es la versión pulida posterior que busca sello formal. La frase "three primordials, reunited" que intriga a Lucifer en B2C36.6 es consistente con el contenido que Vual/Nymos ya plantaron en B2C36.8 ("three shapes, old as the world's own memory, coming back together").

## 3. Cronología/secuencia

**Resultado: sin hallazgos.** El punto crítico señalado por el encargo — que B2C36.8 debe preceder a B2C36.6 (la redacción del falso Codex antes de la aprobación de Lucifer) — está resuelto correctamente en el propio texto: B2C36.8 abre con la línea explícita "**Days before** the pages he would eventually seal with his own hand ever reached Lucifer's desk, Agares received him..." (línea 3 de `B2C36pt8_EN.md`). No hay contradicción de secuencia entre el sufijo de archivo (pt8 después de pt6 en el nombre) y la cronología interna real (pt8 ocurre antes).

También se verificó la cronología interna de B2C36.5→B2C36.7: B2C36.7 se ancla explícitamente "tres noches" después de la escena de consejo de B2C36.5 ("matched the four lines Selaphiel had carried into the council chamber three nights past"), sin conflicto.

La cronología de B2C10.5→B2C21.5 también es consistente: B2C21.5 abre anclando su propia escena "the same night the crossroads claimed Malthus" (la muerte de Malthus ocurre en B2C10.5), y B2C21.6 se inserta explícitamente "justo después" de B2C21.5 según el propio texto (Marbas se entera de la muerte de Malthus la misma noche, y la confrontación con Foras por los soldados robados ocurre "before the man's ashes have finished settling").

## 4. Terminología inconsistente

**Resultado: sin hallazgos significativos.** Los interludios usan consistentemente "the Bastion" para el dominio de Orifiel (B2C03.5/B2C03.6), "Dis" para la capital de Hell (B2C36.6/B2C36.8), y "the Codex" como abreviatura de "Codex Mortalis" en los cuatro interludios de B2C36 — esto último es una abreviatura, no una inconsistencia (el nombre completo tampoco se usa de forma completa en ninguno de los 13 capítulos, así que no hay una forma "incorrecta" usada en contraste con una "correcta"; es simplemente shorthand narrativo consistente en todo el batch).

## 5. Repetición accidental

**Resultado: sin hallazgos de duplicación real**, incluyendo el par señalado explícitamente por el encargo (B2C21.6 vs. B2C08.6).

Comparé ambos capítulos en detalle:
- **B2C08.6** ("What the Ring Corrects"): Balam envía a Orobas como "redundancia" a supervisar el trabajo de Malphas; la escena es entre dos Captains pares (Orobas/Malphas), no entre un Captain y su Commander; se resuelve con Orobas usando su anillo para invertir el destino de dos soldados, dejando a Malphas inquieto sobre los límites de su propio diseño.
- **B2C21.6** ("The Grief They Mistook for Softness"): Marbas se apropia sin permiso de los soldados huérfanos de Malthus; es una confrontación directa Captain→Commander (Marbas/Foras); se resuelve con Foras usando Noesis para "castigar" a Marbas con un corte simbólico que le drena una pequeña certeza, dejándolo consciente de los límites de su margen de maniobra.

Las dos escenas comparten un tema de fondo (una demostración de poder deja a un personaje más cauto), pero la estructura, los participantes, el arma usada y la resolución son distintas. Esto se confirma además en `content/lore/expansion_progress_cruzado.md`, donde el propio proceso de diseño clasificó ambos capítulos bajo **patrones narradores distintos**: B2C08.6 = patrón 17 ("Trampa y destino invertido"), B2C21.6 = patrón 19 ("Capitanes que prueban a un comandante herido") — es decir, los autores ya diferenciaron deliberadamente estas dos escenas al diseñarlas, no hay indicio de que se haya reciclado la misma estructura por accidente.

No se encontraron otras repeticiones de escena entre los 13 interludios (los finales de "personaje se queda solo reflexionando" que aparecen en varios de ellos son un patrón de cierre de prosa/POV, explícitamente fuera del alcance de esta auditoría).

## 6. Contradicción contra el núcleo certificado (B2C01-40)

**Resultado: sin hallazgos.** Puntos verificados específicamente:

- El mortal no identificado en B2C10.5 que "deshace" a Malthus sin tocarlo es, según `content/lore/book2_part1_expanded_beats.md` y `content/lore/expansion_progress_libro2.md`, deliberadamente Milo Ray/Ereloth sin nombrarlo en pantalla (revelación reservada para capítulos posteriores) — el interludio respeta esa restricción de pacing y no nombra ni confirma su identidad en el texto, consistente con la corrección ya aplicada en su momento ("el intercambio Gabriel/Camael confirmaba prematuramente que el misterioso mortal está conectado con el origen de las armas primordiales — esa inferencia debe reservarse para B2C11").
- El spear que atormenta a Belial en B2C07.5 (nunca nombrado en el texto) es consistente con la trama ya establecida de *Lament*, el arma corrupta de Belial, sin contradecirla.
- La nota de consistencia sobre Camael en `personajes.md` (ya no impulsivo, disciplinado y económico en combate desde el Libro II) se respeta en B2C10.5: Camael pelea "economically, without theater."
- Ninguno de los 13 interludios introduce una muerte, un cambio de bando, o un hecho de trama que contradiga lo ya certificado en el núcleo B2C01-40.

---

## Resumen de hallazgos por tipo

| Categoría | Hallazgos |
|---|---|
| 1. Jerarquía de personajes | 0 |
| 2. Continuidad de armas/objetos | 0 |
| 3. Cronología/secuencia | 0 |
| 4. Terminología inconsistente | 0 |
| 5. Repetición accidental | 0 |
| 6. Contradicción contra el núcleo certificado | 0 |
| **Total** | **0** |

No se encontraron hallazgos de continuidad o lore en los 13 interludios auditados. El corpus está internamente consistente entre sí y con el núcleo certificado del Libro II, incluyendo el punto de mayor riesgo señalado en el encargo (jerarquía comandante/capitán de personajes nunca antes vistos) y el punto de cronología invertida (B2C36.8 antes de B2C36.6). Ver la "Nota de contexto importante" arriba: es posible que parte de este resultado se explique porque 9 de los 13 interludios ya habían pasado por el repaso cruzado anterior, aunque los 13 fueron revisados con el mismo nivel de detalle en esta pasada.
