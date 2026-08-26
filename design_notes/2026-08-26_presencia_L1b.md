# Presencia cinematográfica — Fase 2, Libro I, capítulos 27–51 (2026-08-26)

Tramo ejecutado: **Libro1, capítulos 27 a 51, EN + ES**. Fuente: `content/lore/presencia_biblia.md` (única), voz `content/craft/12_calibre_b.md`, encargo `content/craft/13_presencia_cinematografica.md`.

Lectura completa (no solo grep) de los 25 capítulos en ambos idiomas antes de tocar nada. Verificación final: paridad de líneas EN/ES en cada archivo tocado (confirmado con `wc -l`), y `git diff` revisado inserción por inserción — cada cambio es una sola oración insertada, nada más se movió.

---

## 1. Inserciones realizadas

| # | Capítulo | Personaje/lugar | Vector (biblia) | Qué se insertó |
|---|---|---|---|---|
| 1 | L1/30 (×2 puntos) | **Cassiel** — presentación | Percepción rastreadora | Rasgo físico discreto ("unremarkable build, a stillness he wore the way other scouts wore armor") + efecto en Ophaniel, que alza la vista antes de que él hable, reflejo de quien sabe que él no busca a nadie con las manos vacías |
| 2 | L1/32 | **Orifiel** — presentación (mención sin escena propia) | El muro que no retrocede | Aposición breve sobre el nombre ya existente en el texto ("bajo el mando de Orifiel"): escudo fundido al brazo, su línea nunca cedía terreno. No se inventó escena ni diálogo — solo una imagen anclada al nombre ya mencionado |
| 3 | L1/36 | El plano sin nombre — anclaje físico | (sin vector de personaje; escenario) | Reforzado el anclaje visual ya existente (luz, inestabilidad, sabor metálico) con un detalle concreto de superficie: color ceniza mojada, ausencia de sombra pese a la luz cambiante |
| 4 | L1/50 | **Templo de la Luz Quebrada** — presentación con grandeza previa | (escenario, testigo Anael) | Nuevo pasaje explicando el nombre por su arquitectura (bóveda de cristal fracturado que rompe la luz en láminas prismáticas por diseño, no por guerra) — grandeza intencional que precede y contrasta con la ruina bélica ya escrita en L1/51 |
| 5 | L1/51 | **Azael** — despertar | Quietud cósmica | Una frase: el viento que raspaba la cumbre sin pausa simplemente muere en el instante en que despierta — el entorno físico se silencia con su sola presencia, distinto de la quietud de archivo de Iofiel. Replicado byte-idéntico en `project/Chronicles_of_the_Sundering_Judgment/chapters/EN/B1C28_EN.md` |

Total: 6 inserciones puntuales (una oración o aposición cada una), en 5 capítulos, EN+ES espejadas, más la réplica obligatoria en B1C28_EN.md. Ninguna toca diálogo, hecho, beat o canon. Ninguna introduce metáfora decorativa: todas son hecho concreto + efecto, dentro del presupuesto de una imagen por escena.

**Por qué no hay más**: la biblia solo marca presentaciones pendientes de mi tramo para Cassiel (c30), Orifiel (c32) y Azael (c51). El resto del reparto recurrente en 27–51 (Miguel, Belial, Gabriel, Uriel, Rafael, Camael, Iofiel, Zadkiel) ya tuvo su primera aparición antes de mi tramo — insertar una segunda presentación habría violado la regla de "primera aparición por libro, no repetición". No se tocaron sus arcos de inflexión salvo para verificarlos (ver §3).

---

## 2. Los tres nombres candidatos para el plano sin nombre (L1/36–39)

No se acuñó ningún topónimo en el texto — el autor decide el nombre. Se ancló el lugar solo con descripción física (luz que pulsa sin fuente, superficie color ceniza mojada sin sombra, sabor metálico, frío que no es temperatura, inestabilidad del propio concepto de "suelo firme") y el testigo POV Thoria, cuya reacción es catalogación procedimental — formación, recuento de soldados, órdenes tácticas — nunca asombro.

1. **Hollowseam / Costura Hueca** — formaliza el código de trama interno (`B1H0N`) que ya existe en `book1_part2_master_order.md`. Es literalmente lo que el texto ya describe ("some unstable seam between the two [planes]"). Camino de menor fricción: no exige inventar nada, solo nombrar lo que la prosa ya insinúa.
2. **The Greyfold / El Pliegue Gris** — nace del detalle que acabo de anclar (superficie color ceniza mojada) y del verbo que abre el desastre en c36 ("the ground... folded inward"). Sugiere el lugar como un pliegue entre planos, no un sitio fijo — coherente con que se cierra solo al final de c39 sin dejar rastro.
3. **The Undecided Ground / El Suelo Indeciso** — tomado casi textualmente de la propia prosa ("as though the very concept of solid footing hadn't been fully decided here yet" / "unsettlingly undecided about what it was"). Es el más "diegético": sonaría como el apodo que unos soldados supervivientes le pondrían después, no como un nombre de mapa oficial.

Mi recomendación, si el autor pide una, sería la 1 (Hollowseam) por ser la de menor fricción canónica — pero las tres son coherentes con el lore y quedan a su elección.

---

## 3. Verificaciones (sin inserción, solo lectura)

- **Caída de Miguel / mano quemada de Belial**: la biblia (Fase 1, basada en grep) las ubica en L1/51. Lectura completa muestra que en realidad ocurren en **c48** ("The Fall": Miguel cae ante Belial) y **c49** ("The Sound of Retreat": Belial extiende la mano hacia Solmire caída y se quema). El c51 solo las **recuerda** ("a burn across his palm that would not fade" / "He had reached for Solmire too, over Miguel's fallen body..."). No se tocó ninguna de las tres escenas — ni la original en c48–49 ni el recuerdo en c51 (zona sagrada) — pero señalo la discrepancia de capítulo para que quede en el registro del proyecto.
- **Isla de Turein (c30, c32)**: ambas visitas son de Cassiel, no de Mikel/Miguel. No hay mención de que Miguel/Mikel haya pisado la isla en ningún capítulo del tramo 27–51 — no se profundizó la violación **V-TUREIN** (que es sobre la cronología de la visita de Mikel en L2/L3). Confirmado también en c40, donde Iofiel recuerda el informe de Cassiel sobre Turein sin mencionar a Miguel en la isla.
- **Estado del Bastión / "Ciudad Celestial" en c51**: confirmado por lectura directa — en L1 el lugar se llama **"the Bastion"**, nunca "Ciudad Celestial" (ese nombre aparece más tarde, en L3, según la biblia). El daño que el craft 13 cita explícitamente ("la bóveda herida y los estandartes a media asta del L1/51") está confirmado tal cual en el texto: *"the vault healed in strange, uneven cycles... Banners hung at half their old height"*. Punto **[verificar en fase 2]** de la biblia queda resuelto: sí es el Bastión, sí coincide con la cita del craft, y la grandeza previa (necesaria para que la ruina duela) queda ahora anclada en c50 con la inserción del Templo (§1, ítem 4).
- **Contradicciones de tramo**: lectura completa de c27–49 no encontró ningún pasaje que contradiga los estados físicos de Miguel o Belial que llegan a c51 ya escritos.

---

## 4. Tres mejores inserciones (citas EN/ES)

**Cassiel (L1/30)** — vector "percepción rastreadora":

> EN: *"He found Ophaniel filing her own routine report an hour later — she glanced up before he'd said a word, the reflex of anyone who'd worked alongside him long enough to know he rarely sought someone out empty-handed — and mentioned the anomaly in passing rather than as anything requiring escalation."*
>
> ES: *"Encontró a Ophaniel presentando su propio informe rutinario una hora después —ella alzó la vista antes de que él dijera una palabra, el reflejo de quien ha trabajado a su lado el tiempo suficiente para saber que rara vez busca a alguien con las manos vacías— y mencionó la anomalía de pasada más que como algo que requiriera escalarse."*

**Templo de la Luz Quebrada (L1/50)** — grandeza previa al colapso de L1/51:

> EN: *"The Temple of Shattered Light took its name honestly — a vault of fractured crystal overhead built to throw its light in broken, prismatic sheets rather than one clean shaft, a beauty the builders had chosen on purpose long before the war ever asked the name to mean something else."*
>
> ES: *"El Templo de la Luz Quebrada llevaba el nombre con honestidad —una bóveda de cristal fracturado sobre sus cabezas, construida para arrojar su luz en láminas rotas y prismáticas en vez de un único haz limpio, una belleza que los constructores habían elegido a propósito mucho antes de que la guerra le pidiera al nombre significar otra cosa—."*

**Azael (L1/51)** — quietud cósmica:

> EN: *"He did not speak. There was no one there to speak to. The wind that had scoured this summit without pause for longer than anyone below could measure simply died — the silence around him deeper, suddenly, than even five thousand years of stillness had made it."*
>
> ES: *"No habló. No había nadie ahí a quien hablarle. El viento que había raspado esta cumbre sin pausa durante más tiempo del que nadie abajo pudiera medir simplemente murió —el silencio a su alrededor, de pronto, más profundo de lo que incluso cinco mil años de quietud habían logrado hacerlo—."*

---

## 5. Archivos tocados

- `Libro1/EN/30_The_Island_That_Appears_on_No_Map.md`, `Libro1/ES/30_The_Island_That_Appears_on_No_Map.md`
- `Libro1/EN/32_What_Neither_of_Them_Keeps.md`, `Libro1/ES/32_What_Neither_of_Them_Keeps.md`
- `Libro1/EN/36_The_Rift_That_Shouldnt_Exist.md`, `Libro1/ES/36_The_Rift_That_Shouldnt_Exist.md`
- `Libro1/EN/50_Sparks_for_the_Numb.md`, `Libro1/ES/50_Sparks_for_the_Numb.md`
- `Libro1/EN/51_The_Echo_of_the_Sword.md`, `Libro1/ES/51_The_Echo_of_the_Sword.md`
- `project/Chronicles_of_the_Sundering_Judgment/chapters/EN/B1C28_EN.md` (réplica obligatoria del cambio en c51)

Capítulos 27–29, 31, 33–35, 37–49 del tramo: leídos completos, sin cambios (ni presentaciones pendientes de la biblia ni escenarios nuevos que anclar en ellos).
