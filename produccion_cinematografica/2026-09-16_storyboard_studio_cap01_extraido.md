# Storyboard Studio — export del capítulo 1 (extraído y analizado)

> Fecha del export original: 2026-09-15. Analizado: 2026-09-16.
> Archivo fuente (sin las imágenes embebidas, que pesaban ~14 MB y ya existen como PNG en `character_library`/`video_production`): `storyboard_studio_exports/cap01_storyboard_studio_2026-09-15_sin_imagenes.json`.

Esto es, casi con toda seguridad, el contenido real de `design_notes/2026-09-16_flow_storyboard_studio_cap01.md` que los README de `character_library` llevaban días señalando como "autoridad de generación" y que nunca llegó a pushearse — solo que en vez de markdown, es el export nativo JSON del proyecto de Storyboard Studio. Aporta 3 cosas que no teníamos con esta precisión: **un guion ya adaptado a formato de guion cinematográfico real**, **descripciones de personajes/localizaciones/props mucho más detalladas y ya usadas en producción**, y **3 planos de la primera escena ya completamente resueltos** (cámara, movimiento, audio).

## 1. Qué contiene el proyecto

- `globalStyle: "3D-Animation"` — confirma una vez más el estilo oficial.
- **19 assets**: 4 personajes (Miguel, Gabriel, Lucifer, Pewter Sentinel), 9 localizaciones (Serephis en varias sub-zonas: Black Glass Flats, Ash Dunes, Obsidian Waste, la Carretera Enterrada, la Arboleda, el Claro del Fresno, Onyx Gates, la Fortaleza Ardiendo del flashback), 6 props (Solmire, Vox Aeternum, la Orden del Concilio, Sabatons, el bloque de pavimento).
- **13 "frames" (planos)**, pero **solo 3 están completamente desarrollados** (cámara + movimiento + audio) — los de la Escena 01 "Ext. Serephis - Day". El resto (Escenas 02-04: Black Glass Flats, Ash Dunes, Buried Road) están creados como placeholders vacíos — la sesión se quedó a medias justo ahí.
- `fullMarkdown` (2.711 caracteres) es el **guion ya convertido a formato de guion de cine real** (`### EXT. SEREPHIS - DAY`, líneas de acción, etc.) — cubre desde la apertura hasta el descubrimiento de la carretera enterrada, y termina en `##### FADE TO BLACK:` justo antes de que llegue Gabriel. **No incluye el diálogo con Gabriel, la arboleda, el Centinela ni el fresno** — la adaptación se paró ahí.

## 2. Los 3 planos ya resueltos (Escena 01 — apertura)

Coinciden de forma notable con lo que yo había propuesto para "Escena 1 — La marcha" en el plan del capítulo, pero con más precisión de cámara/audio. Los adopto como la versión oficial de esos 3 planos:

**Plano 1 — "The Scorched Kingdom"**
> Visual: plano general extremo del desierto de Serephis bajo un cielo gris-morado nublado; paisaje de vidrio negro roto y ceniza gris hacia un horizonte distorsionado por el calor.
> Movimiento: la cámara hace un paneo lento por el horizonte, enfatizando la escala vasta y desolada.
> Audio: viento bajo y lastimero silbando entre los fragmentos de vidrio; zumbido de distorsión por calor.

**Plano 2 — "The Golden Speck"**
> Visual: desde un ángulo alto, una pequeña mancha dorada se mueve despacio por el páramo obsidiana de Black Glass Flats — el color brillante contrasta con el paisaje monocromático oscuro.
> Movimiento: zoom-in lento, la figura dorada distante se va enfocando con claridad.
> Audio: metal crujiendo suavemente contra vidrio y ceniza, pasos con eco solitario y rítmico.

**Plano 3 — "Journey Through Ash"**
> Visual: la cámara capta a la figura dorada a media distancia atravesando las Dunas de Ceniza; ondas de calor difuminan los bordes del vidrio roto en primer plano.
> Movimiento: travelling horizontal siguiendo a la figura, manteniendo su paso solitario y constante.
> Audio: el crujido de los sabatones sobre la ceniza gris se vuelve el sonido principal, mezclado con el roce del viento moviendo polvo fino.

## 3. Hallazgo estructural importante — cómo manejan las variantes de daño

A diferencia de lo que hicimos a mano (generar una imagen de personaje aparte "Miguel con armadura agrietada"), Storyboard Studio usa otro patrón:

- El **asset "Miguel"** se mantiene siempre en su forma **pristina/base** (alas "symmetrical and pristine", sin mencionar grietas).
- El daño específico de la escena (armadura agrietada, alas con ceniza y "old burn wear") se describe **directamente en el texto de la escena/guion**, no como una variante de personaje separada: *"wearing heavy golden celestial plate armor, intricately etched but battered, dusty, and visibly cracked from the old Onyx Gates campaign... wings... lightly stained with fine grey ash and showing subtle old burn wear."*

**Esto no invalida lo que ya generamos a mano** (la variante de armadura agrietada + ala quemada que aprobamos) — sigue siendo perfectamente válida y ya está pagada/generada. Pero si seguimos usando Storyboard Studio para el resto del capítulo, el patrón a seguir de aquí en adelante es: **mantener el asset del personaje limpio, y describir el desgaste de cada escena en el prompt del plano**, en vez de generar una variante de personaje nueva cada vez. Dos formas de trabajar igual de válidas — lo importante es no mezclarlas sin darse cuenta dentro del mismo capítulo.

## 4. Descripciones oficiales de personajes (más detalladas que `character_library`)

Las fichas de `character_library/*/README.md` siguen siendo el resumen humano correcto, pero **estas son las descripciones exactas que ya se usaron para generar producción real** — más precisas y con más matices de lo que había en los README. Merece la pena actualizar los README con esto en algún momento (no urgente, no bloquea nada ahora mismo).

- **Miguel**: 2,25 m, complexión atlética-potente de hombros anchos, rostro severo de pómulos altos/mandíbula cuadrada, pelo blanco ceniza corto y voluminoso agitado por el viento, ojos cian eléctrico brillante **contenido dentro del iris/pupila, nunca derramándose sobre la piel**, piel clara "luminosa y noble, no pálida de cadáver". Armadura dorada pulida, elegante más que voluminosa, hombreras con motivo de pluma, estrella de ocho puntas cian-blanca en el pecho, azul medianoche bajo la armadura, sin correa de bandolera ni arnés asimétrico.
- **Gabriel**: 1,95 m, **explícitamente masculino, nunca femenino/andrógino** (esto resuelve la ambigüedad que señalaba el README viejo sobre "v1 rudo vs versión final"), mandíbula fuerte, pelo negro largo liso partido al centro cayendo por debajo de los hombros, ojos zafiro sin brillo sobrenatural. Túnica azul real y plata, sin armadura pesada, silueta de hombros anchos y línea vertical estructurada. **Nota explícita del asset**: "Gabriel does not inherently carry any weapon or staff. Vox Aeternum is a separate prop and must only appear when explicitly assigned to the scene."
- **Lucifer**: ~2,10 m (más alto que los 2,20 m de `personajes.md`, diferencia menor, no bloqueante), complexión "war-capable", nunca frágil ni de estética vampírica gótica — el asset insiste varias veces en esto: *"He must not feel fragile, delicate, or vampiric"*, *"No horns, no tail, no monstrous demon traits, no gothic vampire styling"*. Pelo plateado largo ondulado, ojos rojo vino con brillo interior contenido en el iris, piel pálida "como marfil frío o mármol a la luz de la luna, todavía viva y luminosa, no muerta". Ropa: túnicas de batalla negras en capas, silueta regia-militarista, sin cuernos ni cola ni ornamento dorado — "fallen archangel sovereign and war-capable rival to Miguel".
- **Pewter Sentinel**: coincide con lo que ya teníamos en `character_library/otros/Pewter Sentinel/README.md`, sin cambios sustanciales — confirmación, no corrección.

## 5. Localizaciones y props (nuevo — no estaban documentados hasta ahora)

- **Serephis — Dead Desert**: vidrio negro fracturado, dunas de ceniza pálida, calor que sube de la tierra (no del cielo), cielo morado-gris enfermizo, sin vegetación/agua/vida.
- **The Buried Road**: piedra de pavimento tallada, suficientemente ancha para 10 personas en fila, mayormente cubierta de ceniza — "arqueológico, solemne, monumental".
- **The Grove**: rejilla perfecta de árboles idénticos de metal peltre mate, hojas de lámina metálica plana, musgo verde apagado en el suelo, sin viento, "inquietantemente silenciosa, simétrica, glacial".
- **The Ash Tree Clearing**: el fresno en el centro, corteza negra agrietada tipo lava volcánica enfriada, raíces en un charco circular de luz plateada estática (**"no es un anillo mágico, portal, círculo rúnico ni barrera de energía"** — nota explícita a tener en cuenta al promptear), Solmire como única fuente de luz real.
- **The Burning Fortress (Flashback)**: fortaleza de piedra negra colapsando, humo de azufre y fuego infernal, columnas negras agrietándose, "chiaroscuro expresionista violento" — esta descripción es la que hay que usar para el plano 10 del flashback de Onyx Gates en vez de la que yo había improvisado.
- **Solmire (versión Libro I — blanca/glacial)**: sin guarda ni empuñadura de espada convencional — todo es una forma continua de luz blanco-glacial condensada, filos azul-hielo tenues, luz "estable, fría y pura, como luz de luna congelada hecha materia". **Nada de chispas, llamas, partículas ni pulsos de luz.**
- **Vox Aeternum**: bastón esbelto de metal plata-blanco con matices azules, cabeza del bastón como "instrumento de resonancia divina", brillo controlado azul-plata, nunca caótico.
- **Council Order**: pergamino ceremonial de material marfil pálido, sellado con cera negra densa y un sigilo oficial austero — sin decoración dorada brillante ni lazo.

## 6. Cómo continuar (lo que me preguntaste)

1. **Retoma el proyecto en Storyboard Studio** (si te deja reabrir/continuar este mismo proyecto) y completa los planos vacíos de las Escenas 02-04 (Black Glass Flats, Ash Dunes, Buried Road) — ya tiene la estructura de escena creada, solo faltan los campos de visual/movimiento/audio de cada plano, igual que están rellenos en la Escena 01.
2. Cuando llegues al `FADE TO BLACK` (justo antes de Gabriel), **continúa el guion manualmente** dentro de la misma herramienta si te deja añadir escenas nuevas, pegando el resto del capítulo — o si no te deja, seguimos con el storyboard manual que ya tenemos (`2026-09-16_escena_piloto_dialogo.md`), que cubre exactamente esa parte (el diálogo) con el mismo nivel de detalle.
3. Usa las descripciones de la sección 4-5 de este documento como texto base para los prompts de plano de ahora en adelante, en vez de las que yo había reconstruido a partir de las imágenes — son más precisas y ya están validadas en producción real.
4. Decide **un solo patrón para el daño de Miguel** en el capítulo: o seguimos con la variante de personaje pre-generada (armadura agrietada + ala quemada, ya aprobada), o cambiamos a describir el daño por plano como hace Storyboard Studio — mejor no mezclar los dos sin querer entre escenas distintas del mismo capítulo.

Fuente completa (JSON limpio de imágenes, con todos los campos): `storyboard_studio_exports/cap01_storyboard_studio_2026-09-15_sin_imagenes.json`.

---

## 7. Los 10 planos vacíos, ya completados (2026-09-16)

Ya están escritos también dentro del JSON (`storyboard_studio_exports/...json`, campos `title`/`visualDescription`/`motionDescription`/`audioDescription` de cada `frame`), por si Storyboard Studio permite reimportar. Aquí en texto para copiar y pegar directamente en la interfaz si no admite reimportar el JSON.

### Escena 02 — Ext. Serephis - Black Glass Flats - Day

**Plano 1 — "The Weight of the Armor"**
- Visual: *Medium-wide shot of Miguel marching across the Black Glass Flats, full figure visible — his golden celestial plate armor visibly battered and cracked from the Onyx Gates campaign, two enormous pearl-white wings trailing behind him, feathers lightly stained with fine grey ash. The fused black glass ground stretches flat and reflective around him.*
- Movimiento: *Steady lateral tracking shot at knee height, keeping pace with Miguel's stride as the glass terrain slides past.*
- Audio: *Each step produces a sharp, brittle crack as the black glass splinters beneath his sabatons; a low, dry wind hisses across the flat expanse.*

**Plano 2 — "Splintering Ground"**
- Visual: *Low, close shot on Miguel's sabatons striking the black glass — the surface fracturing into a spiderweb of cracks with each footfall, fine ash puffing up around his boots.*
- Movimiento: *Static camera with a slight handheld tremor, holding tight on the ground-level impact.*
- Audio: *A dry, rhythmic crunch with each step, echoing faintly across the empty flats; a distant heat-distortion hum underneath.*

**Plano 3 — "Twelve Days"**
- Visual: *Close-up on Miguel's face and shoulders, ash-white hair windswept, a faint cyan glow contained within his eyes, his expression carrying the exhaustion of twelve days of travel. His wings are partially visible behind him, feathers dulled with grey ash and old burn wear.*
- Movimiento: *Slow, almost imperceptible push-in on his face.*
- Audio: *Wind fades to near silence; his breathing is audible, slow and effortful.*

### Escena 03 — Ext. Serephis - Ash Dunes - Later

**Plano 1 — "The Failing Armor"**
- Visual: *Close tracking shot following Miguel from the side as he walks through the Ash Dunes, his ash-white hair stirring faintly in the dry wind, eyes glowing faintly cyan.*
- Movimiento: *Camera tracks alongside at shoulder height, matching his pace precisely.*
- Audio: *Fine dust hissing against armor plating; the dry rasp of wind moving sand.*

**Plano 2 — "Cracks Spiderweb"**
- Visual: *Close-up on Miguel's breastplate — deep cracks spiderwebbing visibly across the gold plate, the metal flexing slightly with each labored stride.*
- Movimiento: *Static camera, subtle handheld breathing motion.*
- Audio: *A low metallic groan with each step; his breath grows shallow and grit-coated.*

**Plano 3 — "The Hollow"**
- Visual: *Close-up as Miguel's gauntleted hand rises instinctively to the center of his sternum, pressing against an unseen wound; his gaze fixed on the distant horizon, haunted by an unnamed question.*
- Movimiento: *Camera holds still, then drifts almost imperceptibly closer to his hand.*
- Audio: *Wind drops to near-total silence; a faint, cold resonant hum underscores the moment.*

### Escena 04 — Ext. Serephis - The Buried Road - Continuous

**Plano 1 — "Something Solid"**
- Visual: *Wide-medium shot of Miguel trudging up the face of a steep ash dune, boots sinking into grey powder — until his stride catches, his foot striking something solid beneath the surface.*
- Movimiento: *Camera tracks low alongside his climbing stride, then holds as he stops abruptly.*
- Audio: *The soft crunch of ash underfoot shifts suddenly to a dull, solid thud; the wind quiets as if the moment itself holds its breath.*

**Plano 2 — "Worked Stone"**
- Visual: *Close-up on Miguel's gauntleted fingers brushing ash away, revealing the perfectly square edge of a worked paving block beneath the soot; a second and third block emerge as he clears more space.*
- Movimiento: *Slow, deliberate push-in on his hands and the stone.*
- Audio: *Fine ash sifting away with each brush of his fingers; distant wind, otherwise near-silent.*

**Plano 3 — "The Buried Road"**
- Visual: *Wide reveal shot as a broad, ancient road emerges from the waste — paving stones running in a straight, defiant line toward the same horizon Miguel has been following, most of it still buried beneath the dunes on either side.*
- Movimiento: *Slow pull-back and crane up, revealing the scale and direction of the road against the desolate landscape.*
- Audio: *Wind picks up faintly, carrying a low, almost reverent tone; Miguel's breathing steadies.*

**Plano 4 — "The Trembling Stops"**
- Visual: *Close-up on Miguel's face as he looks down at the worked stone, then back toward his own chest, toward the hollow; for the first time in twelve days, his hand stops trembling.*
- Movimiento: *Static, intimate close-up, minimal movement.*
- Audio: *Near silence, the wind fully faded; the faint cold resonant hum returns subtly, then settles.*

## 8. Diagnóstico del problema de generación de vídeo

Tu lectura de lo que pasó es correcta: **Storyboard Studio no está pensado para darte el vídeo final directamente desde ahí** — su trabajo es producir las **imágenes fijas de cada plano** (el panel del storyboard), con el personaje, encuadre e iluminación ya resueltos. Si le pides que anime esos paneles con su propio botón interno, probablemente use un modelo de vista previa rápido/barato pensado para "ver el ritmo", no para calidad final — de ahí que el resultado saliera mal.

**El flujo correcto es el mismo que ya validamos con la escena del diálogo**:
1. Genera/aprueba el panel de imagen fija de cada plano en Storyboard Studio (con los prompts de la sección 7).
2. Saca esa imagen del storyboard y **úsala en el flujo normal de Escenas** — exactamente como hicimos con la imagen de Gabriel: `Vídeo → Fotogramas` (subiendo el panel como fotograma) o `Vídeo → Ingredientes` (si el personaje ya está creado como Character), con `Omni 1.1 Flash` como modelo por defecto.
3. Ahí sí escribes el prompt de movimiento/audio completo (ya los tienes en la sección 7, en los campos Movimiento/Audio) y generas el clip final.

Es decir: Storyboard Studio resuelve el **"qué genero de personajes y planos"**, pero el vídeo final sigue saliendo del mismo sitio de siempre (Escenas, con el modelo que ya sabemos que funciona). No es un atajo que salte ese paso — es una forma más rápida de planificar antes de llegar a él.
