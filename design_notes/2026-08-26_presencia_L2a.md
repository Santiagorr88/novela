# Presencia cinematográfica — Libro II, tramo a (cap. 01-27)

Fase 2 de la pasada de presencia. Fuente: `content/craft/13_presencia_cinematografica.md`, `content/lore/presencia_biblia.md`, `content/lore/personajes.md`, `content/lore/prompt_universo.md`. Voz vigente: `content/craft/12_calibre_b.md`.

## Método

Lectura completa de los capítulos designados (01, 02, 03, 04, 07, 10, 11, 17, 18, 23) en EN y ES antes de escribir, más grep dirigido de Navarion / Ciudad Gris / Torre de los Eternos / Sepulcro para verificar primera aparición y estado (confirmé por ejemplo que la Ciudad Gris de c07 termina colapsada — c25 la llama "ruinas de la Ciudad Gris" tras un "accidente industrial" oficial, así que la presentación de c07 se dejó tal cual, sin adelantar ese futuro). Inserciones hechas primero en EN, luego espejadas en ES en la misma posición, misma solución. Ningún diálogo tocado: toda inserción es narración añadida entre réplicas o en beats puros de interioridad/transición; verificado con `git diff` que ninguna línea con comillas o raya de diálogo cambió de contenido (solo aparecen en el diff de c18 porque la inserción queda *entre* dos réplicas de la misma línea larga — las réplicas en sí son byte-idénticas). Verificación final: recuento de párrafos en blanco y separadores `---` idéntico EN/ES en los 9 capítulos tocados (confirmado por conteo automatizado, ver tabla abajo).

Capítulos 32, 46, 49, 51, 52 aparecen modificados en el working tree pero corresponden al tramo paralelo b (28-53, agente distinto) — no tocados aquí.

## Inserciones realizadas

### 1. Mikel — cap. 01, doble inserción (inconspicuidad + inflexión del cuerpo)
El capítulo no mencionaba guantes ni describía a Mikel físicamente en absoluto. Se insertó el refresco de primera aparición del vector del craft — **inconspicuidad**: mediana edad, pelo cano prematuro, ropa modesta, guantes en toda estación, efecto (noventa alumnos lo miran sin registrar que lo miraron) — en el primer párrafo, sobre la presentación en el aula. Por separado, en la escena del despertar de la pesadilla (ya centrada en su mano derecha cerrándose sobre el vacío), se añadió la única pincelada de la inflexión física pedida por el encargo: la cicatriz bajo el guante da un pulso de calor sin causa. Un solo brushstroke en todo el tramo, tal como pide la instrucción ("1 pincelada, sin repetir la fórmula"); no se repitió en ningún otro capítulo de Mikel (08, 14, 19, 22, 24).

### 2. Navarion — cap. 01 (escenario, pico del libro)
El campus solo se nombraba como telón del aula. Se añadió, en la escena del patio (ya anclada a un lugar físico y con espacio para un hecho sin diálogo), un apunte de su antigüedad real — losas cóncavas por más siglos de los que la historia oficial admite, el silencio particular de tierra vieja — como testigo Mikel, sin adelantar el hecho del portal sellado (eso pertenece a Sariel/Arin más adelante en el libro, fuera del canon que me corresponde tocar). Ficha usada: `prompt_universo.md` §Key Locations.

### 3. Arin — cap. 02 (refresco de primera aparición, vector "nunca se relaja del todo")
El capítulo no describía a Arin físicamente. Se insertó en el primer párrafo: mercenario de finales de los 30, pelo negro corto, cicatriz en el cuello, armadura práctica incluso en una ciudad muerta sin nada contra qué pelear — hecho + efecto (la misma disposición que lleva a salas donde nada lo amenaza en meses; nunca ha terminado de creer que sea seguro comprobarlo). Vector distinto del de Thaeriel celestial (c18: fuego contenido) aunque comparten eje "contenido a la fuerza" según la biblia — aquí se leyó en clave humana de vigilancia crónica, no de fuego.

### 4. Gabriel / Uriel / Rafael — cap. 03 (refrescos de primera aparición)
Los tres ya tenían presencia por voz/actitud pero sin ancla física. Se insertaron tres pinceladas económicas, una por personaje, en sus respectivos beats de entrada:
- **Gabriel**: azul y plata sin armadura, pelo oscuro, ojos zafiro — vector *armonía que precede a la figura*: el murmullo de la sala se adelgaza media respiración antes de que hable.
- **Uriel**: el aire en su punto de la mesa sube de temperatura antes de que hable — vector *calor que se anuncia antes de verlo*, distinto del de Gabriel (auditivo/tono vs. térmico).
- **Rafael**: blanco y verde, ojos esmeralda con aire apenado en reposo — vector *calma que diagnostica*.

### 5. Orifiel — cap. 04 (refresco de primera aparición)
Ya tenía una presentación excelente del vector *el muro que no retrocede* (armadura esmeralda, escudo Muriel, disciplina de "wall"). Solo faltaba el ancla de estatura para redondear el refresco de primera aparición del libro; se añadió "un muro por derecho propio con poco más de dos metros" en la primera frase donde se planta contra el muro sur.

### 6. Lucifer — cap. 10 (refresco de primera aparición, belleza corrupta y voz)
El capítulo desarrollaba a fondo su psicología de control pero no lo anclaba físicamente ni una vez. Se insertó, al abrir la escena del salón privado: pelo blanco plateado, ojos rojo vino, piel pálida perfecta, alas negras — con el efecto pedido por el craft: la sala no reacciona a él, se reorganiza alrededor de su quietud, "como una corte que aprende a respirar al ritmo de un rey sin que se lo digan".

### 7. Camael — cap. 11 (refresco de primera aparición, estatura/fuerza legítima)
El capítulo ya presentaba muy bien su arco de desgaste (armadura marcada, once noches sin dormir) pero ese vector es distinto del que pide la biblia para Camael (estatura/fuerza, "es el martillo"). Se combinaron ambos sin contradicción: "hasta agotado hasta los huesos seguía llenando la puerta como los comandantes más jóvenes solo fingían llenarla" — torso desnudo grabado de runas, dos metros y algo, ojos como rayo atrapado.

### 8. Sariel — cap. 17 (refresco de primera aparición) + Torre de los Eternos (escenario)
Sariel ya estaba muy caracterizado por conducta (economía de movimiento, cataloga la sala) pero sin cifra ni arma. Se añadió: 1,90 m, la lanza Penumbra siempre a mano. Para la Torre de los Eternos (primera aparición nombrada en el libro, en la misma escena) se reforzó la imagen ya presente con un hecho concreto — aguja de basalto negro más vieja que el distrito construido a su alrededor — sin tocar el diálogo de Gabriel/Sariel donde se la nombra.

### 9. Thaeriel (forma celestial) — cap. 18
Primera forma celestial vista en el libro, tal como pide el encargo. La escena ya tenía la voz de Thaeriel hablando a través de Arin pero ningún indicio visual de la forma divina. Se insertó, entre las dos réplicas de la misma voz ("Thaeriel te juzga" / "Eres juzgado indigno"), un destello de menos de un segundo: fuego pálido bajo la piel, cadenas que se mueven como un voto, no como atadura — visible para el capitán, desaparecido antes de que termine de registrarlo. Ficha usada: `prompt_universo.md` §Thaeriel (forma divina).

### 10. Sepulcro Doliente — cap. 23 (escenario, referencia)
El Sepulcro solo se nombraba en los apuntes de Belial que Sariel lee (no hay visita en persona en este capítulo). Se añadió una glosa breve, encajada como conocimiento previo de Sariel — "una tumba que Sariel conocía solo de oídas: sellada por una paradoja, que tira con más fuerza cuanto más se le resiste, donde el suelo susurra en lenguas de ninguna era" — tomada de la ficha `prompt_universo.md` §Sepulcher of Sorrow, sin inventar nada nuevo. Nota de naming: la prosa usa "Weeping Sepulcher" / "Sepulcro Doliente" de forma consistente en L2 (no "Sepulcher of Sorrow" como en la ficha) — se respetó el término ya asentado en el libro, no se tocó.

### Ciudad Gris — cap. 07 (verificación sin cambios)
Ya cumple el encargo de forma ejemplar: presentación completa por efecto (torres brutalistas, gente que no reacciona a un accidente trivial, "la desesperación aquí no era un evento, era ambiental"), testigo POV correcto (Arin), y el giro craft de que la "grandeza inicial" está invertida a propósito (nunca hubo grandeza que mostrar, y eso es el punto). Confirmé por lectura de c25 que su destino posterior (colapso de la torre, "accidente industrial" oficial, refugiados) no contradice nada de c07. No se tocó: cualquier añadido habría sido relleno sobre una escena ya en presupuesto de imagen completo.

## Tres mejores citas (EN / ES)

**1. Lucifer (cap. 10)**
> EN: *"He was, even alone, a beauty gone wrong in some way no single feature could account for — silvery-white hair, eyes the wine-red of something spilled and left to dry, skin pale and flawless in the manner of a portrait rather than a face, black wings folded still behind a frame no throne in this hall required him to occupy. Nothing in the room moved to accommodate him. It simply reorganized itself around his stillness, the way a court learns, eventually, to breathe on a king's schedule without ever being told to."*
> ES: *"Era, incluso a solas, una belleza torcida en un punto que ningún rasgo aislado bastaba para explicar —pelo blanco plateado, ojos del rojo vino de algo derramado y dejado secar, piel pálida y perfecta a la manera de un retrato más que de un rostro, alas negras plegadas e inmóviles tras un cuerpo que ningún trono de este salón lo obligaba a ocupar—. Nada en la sala se movía para acomodarlo. Sencillamente se reorganizaba en torno a su quietud, del modo en que una corte aprende, con el tiempo, a respirar al ritmo de un rey sin que nadie se lo diga jamás."*

**2. Thaeriel, forma celestial (cap. 18)**
> EN: *"For less than a second, too fast for either of them to be sure it had happened at all, Arin's outline wasn't only Arin's — pale fire under the skin, wrapped in chains that moved the way a vow moves, not a restraint, and gone again before the captain's eyes could fully close around what they'd seen."*
> ES: *"Durante menos de un segundo, demasiado rápido para que ninguno de los dos pudiera estar seguro de que hubiera ocurrido en absoluto, el contorno de Arin no fue solo el de Arin —fuego pálido bajo la piel, envuelto en cadenas que se movían como se mueve un voto, no una atadura, y desaparecido de nuevo antes de que los ojos del capitán pudieran terminar de cerrarse en torno a lo que habían visto—."*

**3. Mikel (cap. 01, inconspicuidad + cicatriz)**
> EN: *"He was an unremarkable man to look at, and had built a small, unconscious craft out of staying that way — middle-aged, hair gone white a few decades early, dressed in the kind of modest wool a department stopped noticing after the first year, thin leather gloves worn in every season regardless of weather [...] Beneath the sheet, where the glove wasn't there to hide it, the old scar across his right palm gave one faint pulse of heat with no source he had ever managed to trace, and was gone again before he was fully certain he hadn't imagined it."*
> ES: *"Era un hombre en el que nadie se fijaba, y había construido, sin proponérselo del todo, un pequeño arte de seguir siéndolo —mediana edad, el pelo encanecido unas décadas antes de tiempo, vestido con la clase de lana modesta que un departamento dejaba de notar tras el primer año, guantes finos de cuero que llevaba en todas las estaciones sin importar el clima [...] Bajo la sábana, donde el guante no estaba para ocultarla, la vieja cicatriz de su palma derecha dio un único pulso tenue de calor sin origen que hubiera logrado rastrear nunca, y se apagó de nuevo antes de que pudiera estar del todo seguro de no haberlo imaginado."*

## Verificación de paridad (párrafos en blanco / separadores `---`, EN vs. ES)

| Capítulo | blank EN/ES | `---` EN/ES |
|---|---|---|
| 01 | 31/31 | 4/4 |
| 02 | 31/31 | 3/3 |
| 03 | 25/25 | 1/1 |
| 04 | 33/33 | 7/7 |
| 10 | 38/38 | 5/5 |
| 11 | 29/29 | 4/4 |
| 17 | 39/39 | 5/5 |
| 18 | 28/28 | 6/6 |
| 23 | 31/31 | 5/5 |

Diálogo verificado byte-idéntico contra HEAD en los 9 archivos EN + 9 ES (única línea con diff cerca de una réplica es c18, donde la inserción cae *entre* dos citas de la misma línea larga; ambas réplicas — "Thaeriel judges you" / "Thaeriel te juzga" y "You are judged unworthy" / "Eres juzgado indigno" — permanecen sin cambios).

## Archivos tocados

- `Libro2/EN/01_The_Professor_of_Lost_Things.md` / `Libro2/ES/01_The_Professor_of_Lost_Things.md`
- `Libro2/EN/02_The_Ghost_of_the_Balkans.md` / `Libro2/ES/02_The_Ghost_of_the_Balkans.md`
- `Libro2/EN/03_A_Throne_of_Fractured_Light.md` / `Libro2/ES/03_A_Throne_of_Fractured_Light.md`
- `Libro2/EN/04_The_First_Breach.md` / `Libro2/ES/04_The_First_Breach.md`
- `Libro2/EN/10_What_Even_He_Does_Not_Know.md` / `Libro2/ES/10_What_Even_He_Does_Not_Know.md`
- `Libro2/EN/11_A_Petition_of_Scars.md` / `Libro2/ES/11_A_Petition_of_Scars.md`
- `Libro2/EN/17_A_Mission_into_Memory.md` / `Libro2/ES/17_A_Mission_into_Memory.md`
- `Libro2/EN/18_Wrath_of_the_Just.md` / `Libro2/ES/18_Wrath_of_the_Just.md`
- `Libro2/EN/23_A_Thiefs_Legacy.md` / `Libro2/ES/23_A_Thiefs_Legacy.md`

Cap. 07 (Ciudad Gris) verificado sin cambios necesarios — ya cumple el encargo (ver nota arriba). Resto del tramo (05, 06, 08, 09, 12-16, 19-22, 24-27) no requería inserciones según el encargo (ningún personaje/escenario de la lista tiene su primera aparición ahí) y se dejó sin tocar.

## Flags para el autor

1. **Naming Sepulcro**: la prosa de L2 usa "Weeping Sepulcher" (EN) / "Sepulcro Doliente" (ES) de forma consistente en los tres capítulos donde aparece (09, 23, 26), mientras que la ficha de lore lo llama "Sepulcher of Sorrow". No es una contradicción de canon (ambos traducen la misma idea), pero si el autor quiere un nombre único en todo el libro, valdría la pena decidir cuál fijar antes de la pasada de consolidación.
2. Todo lo demás de mi tramo quedó sin discrepancias que reportar — ningún `[verificar en fase 2]` de la biblia caía dentro de mis capítulos asignados salvo los ya resueltos arriba (estado de Ciudad Gris, testigos POV de Navarion/Torre de los Eternos/Sepulcro).
