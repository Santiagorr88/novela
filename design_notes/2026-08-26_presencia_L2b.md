# Presencia cinematográfica — Libro II, tramo b (cap. 28-53)

Fase 2 de la pasada de presencia. Fuente: `content/craft/13_presencia_cinematografica.md`, `content/lore/presencia_biblia.md`. Voz vigente: `content/craft/12_calibre_b.md`.

## Método

Lectura completa de los 26 capítulos (28-53) en EN y ES para localizar los puntos exactos que pide el encargo, más grep dirigido de Belial/lanza, Balam, Agares, Asmodeo, Dis y Sepulcro Doliente en todo el tramo para no dar por buena ninguna cita de la biblia sin verla en prosa. Inserciones hechas primero en EN, luego espejadas en ES en la misma posición y con la misma solución. Verificación final: recuento de párrafos/separadores `---` idéntico EN/ES en los 5 capítulos tocados, y `git diff --quiet` confirmando que los 21 capítulos restantes del tramo (28-31, 33-45, 47-48, 50, 53) quedaron byte-idénticos contra HEAD.

Nota: `Libro2/{EN,ES}/01_The_Professor_of_Lost_Things.md` aparecen modificados en el working tree pero **no fueron tocados por este agente** — cae fuera de mi tramo (cap. 28-53) y corresponde al trabajo paralelo del agente de L2a (cap. 1-27, presentación de Mikel/inconspicuidad). Se deja intacto.

## Inserciones realizadas

### 1. Selaphiel — cap. 32 (`32_What_the_Staff_Weighs`)
Ya existía una presentación fuerte (imaginada por Hadriel: luz tras el velo, ritmo que los capitanes leen como *sostenido*). Se reforzó el vector exacto del encargo — *"el rostro que nunca se muestra — la reverencia nace de lo oculto"* — añadiendo el hecho de que ningún capitán, ni siquiera Hadriel, ha visto jamás ese rostro, y que la reverencia de la sala coral nace precisamente de esa ausencia. Un solo párrafo, sin tocar diálogo.

### 2. Raziel — cap. 49 (`49_A_Verse_Withheld`)
Raziel ya tenía presencia extensa en diálogo (Ignotus, páginas chamuscadas, inscripciones inquietas) pero sin vector de peligro. Se insertó una frase en el beat entre réplicas (calibre B: la imagen vive en los beats) dándole el vector *"saber que quema al tocarlo"*: sus ojos llevan el mismo calor que el tomo, y estar cerca de él se siente como estar cerca de una llama que no ha decidido si necesita permiso para propagarse.

### 3. Agares — cap. 51 (`51_A_Truth_Told_First`)
Bajo el umbral (referencia puntual, no presentación completa, según indica el encargo). Ya tenía "voz bífida en dos tonos que no coinciden" — vector de la biblia parcialmente cumplido. Se añadió un toque mínimo al primer verbo de sonrisa: las comisuras de su sonrisa "nunca terminan el movimiento hacia algo que Vual llamaría cerrado" — fija el vector candidato de la biblia (*"la sonrisa que nunca cierra"*) sin escribirle una presentación completa.

### 4. Asmodeo — cap. 52 (`52_A_Familiar_Shape_in_Borrowed_Words`)
Su única aparición en el ES actual del libro es una mención de nombre en la reflexión de Lucifer (no tiene escena propia en este tramo). Se insertó el vector *"la forma que nunca se fija"* (1,60-2,10 m, siempre bello, siempre inquietante) como recuerdo de Lucifer — testigo POV — con el efecto pedido: desorientación, no miedo (sus propios comandantes no logran ponerse de acuerdo sobre lo que vieron tras una audiencia con él). Se dividió la frase original en tres para insertar la imagen sin tocar el hecho narrativo (sello ausente de Asmodeo, ya canon).

### 5. Dis — cap. 46 (`46_The_Unaccounted_Variable`)
Primera aparición nombrada del escenario en el libro (antes solo destino de correspondencia). Se añadió un párrafo de establecimiento, testigo Lucifer: corredores de basalto negro, paso uniforme de los ayudantes a cualquier hora, estandartes de los grandes comandantes —incluido Belial— en una sola fila sin jerarquía visible de tamaño. Es el estado "intacto y ordenado" que el encargo pide para que la disputa post-Belial de "The New Pantheon" (L3/49) duela por contraste. **Nota para el autor**: Dis resultó ser la sede de Lucifer (destino de los informes de Belial), no la fortaleza personal de Belial como sugería la hipótesis de la biblia — el orden establecido aquí es el de la corte de Lucifer, del que Belial es uno de los grandes comandantes con banner propio. Escenario nuevo con peso: pendiente de registrar en `prompt_universo.md` (Key Locations) al consolidar, según pide `13_presencia_cinematografica.md`.

### 6. Belial — peso de la lanza (inflexión, cap. 46)
La biblia marcaba `[verificar]` el capítulo exacto donde el peso de la lanza se instala como rasgo permanente. Cap. 46 ya contenía una escena completa y explícita (Lamentum sobre las rodillas cada noche desde la muerte de Aamon, el duelo del arma pulsando contra su esternón, "nunca había aprendido a leerlo"). Faltaba únicamente la pieza que pide el encargo — que el peso **no lo deja descansar** — así que se añadió una pincelada final: no ha logrado una noche de descanso sin perturbar desde que reclamó el arma, y ya no se pregunta si eso cambiará. Confirma cap. 46 como el punto de fijación del rasgo para L2.

### Balam
No aparece en ningún capítulo del tramo 28-53 (confirmado por grep en EN y ES) — sus dos apariciones (cap. 12-13) caen en el tramo anterior (L2a). Sin acción en este informe.

### Sepulcro Doliente
No reaparece en 28-53 (confirmado por grep) — fuera de alcance de este tramo.

## Tres mejores citas (EN / ES)

**1. Selaphiel (cap. 32)**
> EN: *"None of those captains, Hadriel included, had ever managed to describe that face to a newer soldier who asked afterward — not because the memory had faded, but because no one currently serving had actually seen it, and the chorus hall's whole reverence for her had grown, across the centuries, out of precisely that absence rather than despite it."*
> ES: *"Ninguno de esos capitanes, Hadriel incluida, había logrado jamás describirle ese rostro a un soldado más nuevo que preguntara después —no porque el recuerdo se hubiera desvanecido, sino porque nadie en servicio actualmente lo había visto en realidad, y la reverencia entera que la sala coral le profesaba había crecido, a lo largo de los siglos, precisamente de esa ausencia y no a pesar de ella—."*

**2. Dis (cap. 46)**
> EN: *"Dis kept its order the way it kept everything else that mattered to its sovereign: quietly, and without anyone needing reminding to maintain it. [...] The banners of Hell's greater commanders hung in a single ordered row above the audience hall below — Belial's storm-dark sigil no larger and no higher than any other lord's [...]"*
> ES: *"Dis conservaba su orden del mismo modo en que conservaba todo lo demás que le importaba a su soberano: en silencio, y sin que nadie necesitara que se lo recordaran para mantenerlo. [...] Los estandartes de los grandes comandantes del Infierno colgaban en una sola fila ordenada sobre la sala de audiencias de abajo —el sigilo tormentoso de Belial ni más grande ni más alto que el de ningún otro señor [...]"*

**3. Asmodeo (cap. 52)**
> EN: *"Asmodeus himself, on the rare occasions he troubled to hold court in person, never occupied quite the same height twice, beautiful in every shape he chose to wear and unsettling in exactly the same measure, so that his own commanders left an audience with him unable to agree afterward on what, precisely, they had seen."*
> ES: *"El propio Asmodeo, en las escasas ocasiones en que se molestaba en presentarse en persona ante la corte, jamás ocupaba dos veces la misma estatura, bello en cada una de las formas que elegía vestir e inquietante en exactamente la misma medida, de modo que sus propios comandantes salían de una audiencia con él incapaces de ponerse de acuerdo después sobre qué, exactamente, habían visto."*

## Archivos tocados

- `Libro2/EN/32_What_the_Staff_Weighs.md` / `Libro2/ES/32_What_the_Staff_Weighs.md`
- `Libro2/EN/46_The_Unaccounted_Variable.md` / `Libro2/ES/46_The_Unaccounted_Variable.md`
- `Libro2/EN/49_A_Verse_Withheld.md` / `Libro2/ES/49_A_Verse_Withheld.md`
- `Libro2/EN/51_A_Truth_Told_First.md` / `Libro2/ES/51_A_Truth_Told_First.md`
- `Libro2/EN/52_A_Familiar_Shape_in_Borrowed_Words.md` / `Libro2/ES/52_A_Familiar_Shape_in_Borrowed_Words.md`

Resto del tramo (28-31, 33-45, 47-48, 50, 53) verificado sin cambios (`git diff --quiet` contra HEAD).
