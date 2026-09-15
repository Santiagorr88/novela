# Investigación: vídeos cinematográficos largos (5–20 min) con Veo 3 para adaptar la novela

> Fecha: 2026-09-15
> Objetivo: determinar un workflow realista para convertir capítulos de *Chronicles of the Sundering Judgment* en vídeos cinematográficos de 5–20 minutos usando Veo 3/3.1, encadenando clips de 8 segundos sin que se noten los cortes (incluyendo planos de diálogo de ~1 minuto que deben leerse como una sola toma continua).
> Nota sobre las fuentes: `youtube.com` y `youtu.be` están bloqueados por el proxy de red de este entorno (egress bloqueado), así que no pude abrir directamente los 3 vídeos enlazados. Los identifiqué por su ID vía búsqueda y documento lo que encontré sobre cada uno abajo; el resto del informe se apoya en ~20 búsquedas adicionales sobre documentación oficial, blogs especializados, foros y tutoriales (fuentes citadas en cada sección).

---

## 0. Los 3 vídeos de referencia

| Link | Lo que pude identificar |
|---|---|
| `youtu.be/oodW_W15rLY` | No se pudo confirmar el título exacto (bloqueo de red + el ID no aparece indexado con contexto claro). Probablemente contenido general sobre Veo 3 (los resultados de búsqueda relacionados apuntan a vídeos oficiales tipo "Meet Veo 3"). **Recomendación**: si es importante, pásame el título o una captura y lo incorporo. |
| `youtube.com/shorts/AeGhWSYQkmc` | Tampoco se pudo confirmar con certeza. El contexto de búsqueda apunta a la ola de contenido sobre "Veo 3 Fast llega gratis a YouTube Shorts" (anuncio de sept. 2025). Podría ser un short mostrando esa función nativa, no necesariamente una técnica de edición avanzada. |
| `youtu.be/c772SYf6k-4` | **Sí identificado**: *"How to Finally Make Long Videos with VEO 3.1 (Create Consistent Videos of Any Length)"*, subido ~29 oct 2025. Trata sobre cómo generar vídeos largos consistentes con Veo 3.1, mencionando herramientas de terceros (p.ej. HitPaw) además del propio Flow. Confirma la premisa central de tu pregunta: sí existe un método fiable para encadenar clips sin que se note el corte, y gira en torno a la técnica de "última imagen → siguiente clip" + repetición de prompt que detallo abajo. |

Si me compartes capturas de pantalla o transcripciones de los otros dos, los integro en una revisión de este documento.

---

## 1. Fundamentos técnicos de Veo 3 / 3.1 (qué es posible hoy)

**Límite nativo real:** cada generación de Veo 3 produce **8 segundos** de vídeo (con audio síncrono: diálogo, ambiente, efectos). Ese límite no ha cambiado en Veo 3.1; lo que ha cambiado es la calidad de las herramientas para *encadenar* generaciones.

**Formas de superar el límite de 8s:**

1. **Flow Scene Builder** (`labs.google/flow`) — la vía recomendada por la mayoría de tutoriales 2026. Permite:
   - **Frames-to-Video**: tomar el último fotograma de un clip y usarlo como primer fotograma del siguiente, con audio y calidad completa de Veo 3 (a diferencia del botón "Extend" simple, que en muchos flujos solo usa Veo 2 Fast, sin audio y menor calidad).
   - **Extend nativo (Veo 3.1)**: ahora sí soporta continuación de audio; permite extender un clip hasta 20 veces, acumulando hasta ~148 segundos (2:28 min) de metraje continuo con sonido "pegado" en cada unión.
   - **Ingredients to Video**: hasta 3 imágenes de referencia (personaje / entorno / estilo-textura) que Veo 3.1 usa como anclas visuales para mantener identidad, vestuario y ambientación a través de múltiples generaciones.
   - **"Jump to" + Frames-to-Video (modo Fast)**: workaround reportado para lograr continuidad en modo "Fast" (más barato): generar clip → "Add to scene" → Scenebuilder → icono "+" → "Jump to" → quitar el botón "Jump to" → "Frames to Video" con el nuevo prompt. Discutido como un poco "loophole", puede cambiar.
   - **Sintaxis `@nombre`**: dentro de Flow puedes referenciar un "Ingredient" guardado escribiendo `@` + nombre en cualquier prompt posterior.
   - **Google Whisk** (generador de imágenes base combinando Sujeto+Escena+Estilo) fue **retirado como producto independiente en 2026** y sus funciones se integraron dentro de Flow/Ingredients. Sigue siendo útil como *concepto*: genera primero una imagen de referencia sólida de cada personaje antes de animar.

2. **Vía API (Gemini API / Vertex AI)** — para producción programática (útil si en el futuro automatizas la generación desde `src/`):
   - Precio de referencia: **~$0.75/segundo** con audio en Vertex AI (varía según proveedor: $0.20–$0.60/s según resolución y si lleva audio); un minuto de vídeo terminado puede rondar **$45** vía API directa. Proveedores de terceros (fal.ai, Replicate, etc.) ofrecen tarifas más bajas.
   - Límite de tasa habitual: ~10 requests/min.
   - Resoluciones: 720p/1080p estándar; 4K disponible en Vertex/Gemini API a precio premium.

3. **Plan por suscripción (Flow / Google AI Pro-Ultra)** — más económico para uso creativo manual:
   - Google AI Pro (~$20/mes): 1.000 créditos ≈ 100 vídeos "Lite", 50 "Fast" o 10 "Quality" (8s c/u).
   - Google AI Ultra (~$250/mes): 25.000 créditos ≈ 250 vídeos "Quality" de 8s ≈ **33 minutos** de metraje bruto Veo3 al mes antes de edición.
   - **Implicación práctica para un capítulo de 15–20 min**: con calidad completa necesitarás entre ~110 y ~150 clips de 8s (antes de descartar tomas fallidas). Con Ultra eso es ~1 mes de cuota completo para *un* capítulo si generas en máxima calidad; conviene mezclar "Fast" para planos secundarios/pruebas y "Quality" solo para los planos hero.

Fuentes: [Complete Guide to Extending Veo 3 Videos (Easton)](https://eastondev.com/blog/en/posts/ai/20251207-veo3-long-video-guide/), [How to Extend Veo 3 Videos Beyond 8 Seconds (veo3ai.io)](https://www.veo3ai.io/blog/veo-3-extend-video-beyond-8-seconds-2026), [Veo 3.1 Ingredients to Video — Google blog](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video/), [Veo 3.1 Video Continuation Guide (apiyi.com)](https://help.apiyi.com/en/veo-3-1-video-extend-guide-en.html), [Google Veo 3.1 Cost Guide (akool)](https://akool.com/blog-posts/google-veo-3-1-cost-guide), [5 tips for using Flow — Google blog](https://blog.google/technology/ai/flow-video-tips/), [Whisk AI Is Now Google Flow — migration guide](https://whiskaitemplate.com/blog/whisk-ai-google-flow-migration-guide-2026).

---

## 2. La técnica central: encadenar clips de 8s sin cortes visibles

Esto responde directamente a tu pregunta de "cómo pegar los 8 segundos para que no existan cortes". No hay una función mágica de "generar 5 minutos de una vez"; es una disciplina de **continuidad manual + ocultación de la unión**. Los pasos que se repiten en todas las fuentes:

### 2.1 En el momento de generar (evitar que el contenido cambie)

1. **"Character DNA"**: escribe una ficha fija (apariencia física, vestuario, iluminación, paleta de color, "vibe", voz) y **pégala entera en cada prompt nuevo**, no solo un resumen. La repetición de prompt es, según casi todas las fuentes, el factor #1 que determina si un vídeo largo se sostiene o "deriva" (drift): cambios de tono de piel, ropa, iluminación entre clips.
   - Regla práctica citada: cada prompt de extensión debe repetir **al menos el 80%** de la información del prompt original.
2. **Frames-to-Video encadenado**: guarda el último fotograma de cada clip como "asset" y úsalo como primer fotograma del siguiente (en vez de depender solo de "Extend"). Esto ancla literalmente el punto de partida visual.
3. **Ingredients (imágenes de referencia)**: sube 1–3 fotos limpias, bien iluminadas, del personaje/localización como "ingredientes" reutilizables; mejora mucho la consistencia frente a solo texto.
4. **Un plano = una acción**: evita "camina mientras habla y come" en un mismo prompt; una acción por segmento produce movimiento más limpio y left menos margen para que el modelo "rellene" con generación errática.
5. **Negative prompting básico**: Veo 3 no tiene un campo dedicado, pero añadir al final del prompt cosas como *"(no subtitles, no on-screen text, no watermark)"* reduce mucho el bug de subtítulos falsos/garabateados. Usa colon simple para diálogo (`Miguel dice: "..."`) en vez de comillas anidadas — es el fix más consistente reportado contra diálogo mal formado.
6. **Color/luz como números, no adjetivos**: en vez de "luz dramática", especifica temperatura de color, ratio de iluminación (key:fill), y "look" de film stock — ayuda a que el color no salte de clip a clip.

### 2.2 En el corte entre clips (ocultar la unión — "cut-hide technique")

Esto es la parte de **edición cinematográfica clásica** aplicada a IA, y es la respuesta más directa a "que no salgan cortes en una conversación de 1 minuto":

- **Nunca hagas el corte con la cámara y el sujeto quietos.** Dos clips de IA nunca encajan perfectamente al 100% (leve variación de iluminación/color, ~1% incluso en los mejores modelos de "extend"); esa variación es invisible si hay movimiento, pero salta a la vista si el plano está estático.
- **Corta sobre movimiento fuerte de cámara o del sujeto** (el ojo humano no puede escanear artefactos de fondo mientras algo se mueve rápido): esto es exactamente el mismo principio del **whip pan** clásico de cine — terminas un clip con un giro rápido de cámara en una dirección y empiezas el siguiente con un giro igual de rápido en la misma dirección; en el montaje el "blur" de ambos se funde y el corte desaparece.
- **Cobertura de objeto/personaje** ("object coverage"): un personaje camina hacia cámara y la tapa por completo (fundido a negro funcional); el siguiente clip empieza con la espalda del personaje alejándose. El corte queda literalmente oculto detrás del cuerpo.
- **Match on action**: cortar mientras una acción física está en marcha (una mano que empieza a cerrar una puerta en el clip A, termina de cerrarla en el clip B) — el cerebro rellena el gap.
- **Entrar/salir de zonas muy oscuras o muy luminosas**: un fundido "natural" dentro de la propia escena (pasar bajo una sombra, un relámpago, un portal de luz — muy aplicable a tu novela con arcángeles/luz divina).
- **Colocar la unión lejos del punto de atención**: si el espectador está mirando la cara del personaje que habla, el error de continuidad de fondo (cielo, hierba, textura) pasa desapercibido.

Con esta caja de herramientas, alguien documentado en las fuentes construyó una toma "continua" de 1:30 min a partir de múltiples clips de IA — los cortes existen, pero el espectador nunca los ve.

Fuentes: [Cut-Hide Technique (invideo)](https://invideo.io/faq/what-is-the-cut-hide-technique-in-ai-filmmaking-and-how/), [Match cut — Morphic](https://morphic.com/ai-glossary/match-cut), [Invisible Editing Techniques (plotwit)](https://plotwit.com/invisible-editing-techniques/), [How to Pull Off a Long Take with Hidden Cuts (4kshooters)](https://www.4kshooters.net/2022/09/10/how-to-pull-off-a-long-take-with-hidden-cuts/), [One-Take/Oner — Morphic glossary](https://morphic.com/ai-glossary/One-Take-Oner), [Master the Art of Consistent Characters in VEO 3 (Medium)](https://medium.com/@nahianbinrahman/master-the-art-of-consistent-characters-in-veo-3-for-long-form-videos-c0cb5fae18ac), [Unlock Continuity in Veo 3 "Fast" Mode (Medium)](https://therobbiedshow.medium.com/unlock-continuity-in-veo-3-fast-mode-with-this-loophole-37c4ad2afe7b).

---

## 3. El caso específico: una conversación de ~1 minuto sin cortes visibles

Esto es lo más difícil de lograr bien porque el diálogo hablado es lo que más rápido delata un corte (voz, labios, ritmo). Método recomendado combinando varias fuentes:

1. **Escribe el diálogo completo de la escena primero**, como guion, no como prompts sueltos. Divide en líneas que se puedan decir en ≤8 segundos cada una (evita que un personaje "hable demasiado rápido" porque metiste más texto del que cabe en el clip).
2. **Genera cada línea/beat como un clip de Veo 3 con audio nativo** (Veo 3 genera imagen + diálogo sincronizado en la misma pasada — no hace falta doblar después si el timing funciona).
3. **Técnica de audio recomendada para escenas largas**: pide que Veo 3 genere **solo el diálogo** (sin música de fondo ni SFX) y añade tú la banda sonora/ambiente en post. Esto evita el problema de que la música o el ambiente "salte" de volumen o tono entre clips — un problema mucho más perceptible al oído que un salto visual sutil.
4. **Oculta la unión de audio con J-cuts/L-cuts + crossfade**: deja que el audio del clip siguiente entre 1–2 segundos *antes* de que cambie la imagen (J-cut), o que el audio del clip anterior se sostenga 1–2 segundos *después* del corte de imagen (L-cut). Pasado ese margen (~3s) el espectador nota el desfase, así que hay que ser preciso.
5. **Una "cama" de ambiente continuo** (ambient bed: viento, eco de catedral, zumbido de energía angelical, lo que sea propio de la escena) que se solape sin cortes por debajo de todo el diálogo disimula radicalmente las uniones — es más fácil de lograr en post (DaVinci/Premiere/Audition) que pedirle a Veo 3 que lo mantenga consistente él solo.
6. **Refuerza lip-sync si hace falta reescritura de líneas**: si en post cambias una palabra del guion (p. ej. por continuidad de canon), usa una herramienta de lip-sync dedicada (Sync Labs, HeyGen, o el LipSync Studio de Higgsfield) en vez de re-generar todo el clip — es más barato y más controlable.
7. **Corta los cambios de plano en los turnos de conversación** (shot/reverse-shot clásico): cuando cambias de "Miguel habla" a "Gabriel responde" es un punto natural de corte que el espectador ya espera de cualquier diálogo de cine — no necesitas ocultarlo con trucos de whip-pan, solo necesitas que **ambos personajes mantengan su Character DNA** (ficha de apariencia) entre planos para que no "salten" de aspecto al alternar.

En la práctica: una conversación de 1 minuto entre dos personajes casi nunca necesita ser literalmente "un solo plano ininterrumpido" — el lenguaje cinematográfico normal (shot/reverse-shot, primeros planos, planos de reacción) ya rompe la escena en unidades de ≤8s de forma natural y **elegante**, y es mucho más fácil de lograr con IA que fingir una sola toma continua. Reserva la técnica de "toma continua oculta" (sección 2.2) para momentos de **impacto** (una revelación, una transformación, un descenso desde el cielo) donde el plano largo sin corte tiene valor dramático — como en tu capítulo de muestra, la desenvainada de Solmire o la visión cósmica de Miguel.

Fuentes: [J-Cuts and L-Cuts for Smooth Dialogue Edits (CapCut)](https://www.capcut.com/create/j-cuts-and-l-cuts-dialogue-edits), [J Cut and L Cut Explained 2026 (CutFast)](https://cutfa.st/en/blog/j-cut-l-cut-audio-transition-editing-cutfast-method-2026), [How to hide audio transitions (Videomaker)](https://www.videomaker.com/how-to/audio-how-to/audio-editing/how-to-hide-audio-transitions-for-a-cleaner-sounding-video/), [ElevenLabs use cases: video](https://elevenlabs.io/use-cases/videos), [ElevenLabs Lip Sync](https://elevenlabs.io/lip-sync), tutorial en español sobre personajes consistentes Veo 3 (comousarapps.com / juanmerodio.com — ver sección 5).

---

## 4. Prompting técnico: estructura JSON, cámara, diálogo

- **Cuándo usar JSON en vez de prosa libre**: cuando el prompt necesita controlar más de ~5 elementos cinematográficos distintos a la vez (tipo de plano, lente, movimiento de cámara, acción, audio). El JSON actúa como un "guion técnico" en bloques: `shot`, `subject`, `action`, `camera`, `lighting`, `audio`, `dialogue`, `negative`.
- **Orden importa**: Veo 3 pondera más las primeras palabras/campos; pon lo más crítico (tipo de plano, identidad del personaje) al principio.
- **Diálogo**: formatéalo como `Nombre dice: "línea"` (dos puntos, no solo comillas) — es el formato más fiable. Mantén cada línea dentro de lo que se puede pronunciar en 8s (Rule of thumb ≈ 18–20 palabras a ritmo conversacional normal).
- **Negativos**: al final del prompt, `(no subtitles, no on-screen text, no watermark, no extra limbs)`. No abuses de listas larguísimas de negativos: colisionan con la intención y generan resultados genéricos.
- **Un plantilla básica JSON reutilizable**:

```json
{
  "shot": "medium close-up, 35mm lens, slow push-in",
  "subject": "Miguel — [ficha DNA completa: armadura dorada agrietada, cabello blanco cenizo, ojos de llama azulada, alas radiantes]",
  "environment": "arboleda de metal pálido, luz uniforme sin sombras, aire de after-storm",
  "action": "Miguel alza la mano hacia la espada, dudando",
  "camera": "cámara estática, leve temblor orgánico, foco en la mano",
  "lighting": "luz fría cenital, sin sombras duras, tono azul-plata",
  "audio": "silencio tenso, zumbido grave apenas audible, sin música",
  "dialogue": "Miguel dice: \"¿Seguiré siendo yo mismo después?\"",
  "negative": "no subtitles, no on-screen text, no watermark"
}
```

Fuentes: [Ultimate prompting guide for Veo 3.1 — Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1), [Veo 3/3.1: pro JSON prompting step-by-step](https://developer.tenten.co/veo-331-pro-json-prompting-step-by-step), [GitHub: Veo-3-Prompting-Guide (snubroot)](https://github.com/snubroot/Veo-3-Prompting-Guide), [Veo 3 negative prompts (anakin.ai)](http://anakin.ai/blog/veo-3-negative-prompts-how-to-reduce-artifacts-and-unwanted-objects/), [How to prompt Veo 3 — Replicate blog](https://replicate.com/blog/using-and-prompting-veo-3).

---

## 5. Post-producción: color y montaje para que "no parezca IA cortada"

1. **Normaliza cada clip** (balance de blancos/exposición) contra un scope antes de nada — los clips de IA no salen en log/neutral, salen ya "cocinados" y con contraste variable.
2. **Aplica un LUT de emulación de película al 50–70% de intensidad** (nunca al 100%: satura highlights y ahoga sombras porque la imagen de IA ya viene contrastada).
3. **Añade grano + un toque de blur** para romper la nitidez "plástica" típica de vídeo generado.
4. **Iguala cada clip a un still de referencia** (una imagen del "grade" objetivo del capítulo) para que toda la escena, aunque venga de 10 generaciones distintas, se sienta de una sola paleta.
5. Herramientas: DaVinci Resolve (gratis, motor de color más potente) o Premiere; para el corte fino de audio, Audition/Resolve Fairlight.
6. Considera generar **sin música/SFX** desde Veo3 (ver §3) y construir el diseño de sonido completo en post — te da control total sobre continuidad y es más barato que regenerar clips por errores de audio.

Fuentes: [How to Get a Cinematic Film Look with Veo 3 (veo3ai.io)](https://www.veo3ai.io/blog/veo-3-cinematic-film-look-color-grading-2026), [Best Color Grading Workflow for AI-Generated Video (invideo)](https://invideo.io/faq/what-is-the-best-color-grading-workflow-for-ai-generated/), [AI Video Pipeline: Definition, Stages (trezalabs)](https://www.trezalabs.com/blog/how-to-build-an-ai-video-generation-pipeline).

---

## 6. Comparativa de herramientas (para narrativa larga con personajes recurrentes)

| Herramienta | Punto fuerte para este proyecto | Límite/coste |
|---|---|---|
| **Veo 3.1 + Flow (Google)** | Único con generación de **audio+diálogo nativo** en la misma pasada; Ingredients + Frames-to-Video para continuidad. Mejor opción "todo en uno" hoy. | 8s por generación nativa, hasta ~148s encadenando extensiones; drift de personaje si no repites el prompt completo. |
| **Runway Gen-4 / Aleph** | El sistema de "reference consistency" mantiene personaje/entorno estables en secuencias multi-plano largas con solo 1 imagen de referencia; Aleph permite editar un clip existente por texto sin regenerar todo. Útil para correcciones puntuales. | Sin audio nativo tan fuerte como Veo3 (según reportes); pensado más para edición que generación pura. |
| **Kling 3.0** | Herramienta de storyboard nativa por plano (cámara + ritmo), 4K, lip-sync nativo, buena consistencia de personaje/props en narrativa corta multi-shot. | Menos integrado con Google/Flow; ecosistema distinto. |
| **Luma Ray2/Ray3** | Mejor física de movimiento y extensiones de clip muy creíbles (5s→30s) para tomas de cámara calmadas (arquitectura, producto, planos contemplativos). | Menos indicado para diálogo intenso o acción rápida. |
| **LTX Studio** | Pipeline completo **guion → storyboard → shot list → clips → timeline**, perfiles de personaje persistentes reutilizables. Muy alineado con "meter un capítulo entero y que trocee en escenas". | Motor de vídeo propio (LTX-2), calidad/consistencia aún por detrás de Veo3 en algunos casos; plan gratuito limitado. |
| **Higgsfield** | Agrega 15+ modelos (incluido Veo 3.1) bajo un mismo panel; "Popcorn" para planear multi-shot con personajes/framing/ritmo antes de renderizar; "Soul ID" para lock de identidad entre modelos; LipSync Studio propio. *(Nota: este entorno de trabajo tiene un conector Higgsfield disponible — puede valer la pena probarlo directamente para producción real).* | Depende de qué modelo subyacente uses para coste/calidad final. |
| **ElevenLabs** | No genera vídeo, pero es el estándar para voice cloning consistente (una voz para cada personaje reutilizable en todos los capítulos) + lip-sync de alta calidad para arreglos puntuales. | Añade un paso extra al pipeline (voz separada del vídeo). |

Fuentes: [Kling AI vs Runway vs Luma (atlascloud)](https://www.atlascloud.ai/blog/guides/kling-ai-vs-runway-vs-luma), [Seedance 2.0 vs top AI video generators 2026 (ai.cc)](https://www.ai.cc/blogs/seedance-2-vs-top-ai-video-generators-2026/), [LTX Studio Review 2026 (dupple)](https://dupple.com/reviews/ltx-studio), [LTX Studio — script to video](https://ltx.io/studio/platform/script-to-video), [Higgsfield AI 2026 Features](https://geo.higgsfield.ai/higgsfield-ai-features-full-guide-2026), [How to Keep AI Persona Consistent — Higgsfield Popcorn](https://higgsfield.ai/blog/how-to-keep-ai-persona-consistent-higgsfield-popcorn).

---

## 7. Metodología para convertir un capítulo de la novela en vídeo

Tus capítulos (ver `B1C01_ES_v2.md`) rondan las 2.500–3.000 palabras (según el propio target del skill `beat-planner`: 15–20 min / 2.250–3.000 palabras), lo cual **encaja casi perfectamente** con tu objetivo de vídeos de 5–20 minutos: no hace falta condensar una novela entera, cada capítulo ya es del tamaño correcto para un "episodio".

### 7.1 Ratio de referencia
- Guion audiovisual estándar: **1 página ≈ 1 minuto de pantalla ≈ 130–150 palabras/minuto** (más lento si hay mucho diálogo reflexivo como en tu prosa; más rápido si es acción).
- Un capítulo de 2.800 palabras en prosa **no** se traduce 1:1 a minutos porque la prosa incluye pensamiento interno, descripción atmosférica y narrador — que hay que **externalizar** (convertir en imagen/acción/diálogo) o recortar. Con ese ajuste, 2.800 palabras de prosa producen razonablemente entre **8 y 15 minutos** de guion audiovisual utilizable, dependiendo de cuánta introspección se convierta en voz en off vs. se elimine.

### 7.2 Pasos concretos (aplicable capítulo a capítulo)

1. **Beat sheet visual**: parte del beat sheet narrativo que ya usa el proyecto (`beat-planner`, `*_expanded_beats.md`) y márcalo con una columna extra: *¿esto es diálogo, acción física, o pensamiento interno?* Todo lo que sea pensamiento interno necesita convertirse en: (a) voz en off, (b) un gesto/expresión visible, o (c) diálogo dicho en voz alta a otro personaje — igual que exige cualquier adaptación de novela a guion ("las novelas explican, los guiones muestran").
2. **Shot list por beat**: para cada beat, define: tipo de plano, personajes en cuadro, acción, línea de diálogo (si hay), duración estimada en múltiplos de 8s.
3. **Ficha visual por personaje/localización (= tus "Ingredients")**: usa las fichas que ya existen en `content/lore/personajes.md` (altura, apariencia, armadura, arma, personalidad) como base literal para el "Character DNA" del prompt — ya tienes el trabajo de diseño hecho, solo hay que traducirlo a lenguaje de prompt visual (ropa, color, textura, iluminación característica). Genera una imagen de referencia limpia una vez por personaje/localización recurrente y reutilízala como "Ingredient" en todos los capítulos donde aparezca — consistencia entre capítulos, no solo dentro de uno.
4. **Genera por escena, no por capítulo entero**: agrupa los beats en escenas (como ya hace tu prosa con los `---`), genera cada escena como una cadena de clips de 8s con su propio "Character DNA" pegado, y solo al final concatenas las escenas en el editor.
5. **Aplica la sección 2.2** (cut-hide) dentro de cada escena larga, y cortes normales de montaje (shot/reverse-shot) entre escenas.
6. **Pase de color + audio en post** (sección 5) sobre el corte final del capítulo completo para unificar look y sonido.
7. **QA de continuidad**: como el proyecto ya tiene una disciplina fuerte de auditoría de continuidad (ver `design_notes/*_continuity_audit_*`), aplica el mismo criterio al vídeo: una pasada de "revisión visual" comparando cada escena contra la ficha de personaje antes de dar por bueno el corte.

### 7.3 Ejemplo aplicado (usando el capítulo B1C01 real)

Tomando la escena Miguel–Gabriel de `B1C01_ES_v2.md`:
- **Escena 1** (exterior, Serephis): plano general de Miguel caminando por el desierto agrietado (1 clip, cámara estática con leve deriva) → primer plano de su mano sobre el pecho (1 clip) → llegada de Gabriel con luz (1 clip, corte oculto con destello de luz = "entrar en zona muy luminosa", sección 2.2).
- **Escena 2** (diálogo Miguel/Gabriel): shot/reverse-shot clásico, 4–6 clips de 8s alternando, con Character DNA de cada uno repetido en su propio prompt; audio pedido "solo diálogo" y ambiente (viento cálido, eco) añadido en post como cama continua.
- **Escena 3** (la arboleda + la espada Solmire): aquí sí vale la pena forzar una "toma continua" con Frames-to-Video encadenado y cortes ocultos por movimiento de cámara (push-in lento constante), porque es el clímax visual del capítulo.
- **Escena 4** (visión cósmica): ideal para un montaje con cortes visibles y rápidos (aquí el corte abrupto ayuda a la sensación de caos cósmico — no todo necesita ocultarse; a veces el corte visible es la herramienta narrativa correcta).
- **Escena 5** (Lucifer, cámara oscura): plano corto, contraste con la limpieza total del arco de Miguel.

Esto ilustra el principio clave: **decide primero si la escena narrativamente pide un "oner" (revelación/impacto) o un montaje clásico (diálogo/conversación) antes de elegir la técnica de corte** — no todas las escenas deben ocultarse, y forzarlo donde no aporta es esfuerzo desperdiciado.

Fuentes: [How to Adapt a Book into a Screenplay in 7 Steps (StudioBinder)](https://www.studiobinder.com/blog/how-to-adapt-a-book-into-a-screenplay/), [Adaptation 101 — From Novel to Screenplay](https://www.movieoutline.com/articles/adaptation-101-from-novel-to-screenplay.html), [Word Count to Movie Minutes](https://vweisfeld.com/?p=3944), [Ratio of pages to screen time — John August](https://johnaugust.com/2003/ratio-of-pages-to-screen-time), [How to Turn a Novel or Play Into an AI Film — ScreenWeaver](https://www.screenweaver.ai/blog/turn-novel-into-ai-film) *(nota: este dominio está bloqueado por el proxy de red del entorno; cito el título/resumen indexado por el buscador, no el contenido completo)*.

---

## 8. Estimación de coste/esfuerzo para un capítulo de 15–20 min

- Metraje bruto necesario (antes de descartes): ~110–150 clips de 8s en "Quality" (calidad completa Veo3).
- Con retoma de errores/descartes, cuenta con generar **1.5–2x** ese número de clips reales.
- **Coste vía Flow/Ultra**: ~1 mes completo de cuota Ultra ($250) por capítulo si todo va a calidad máxima; se abarata mucho generando planos secundarios/pruebas en "Fast" y reservando "Quality" para primeros planos y momentos clave.
- **Coste vía API directa**: a $0.75/s, 15–20 min = 900–1200s ≈ **$675–$900** por capítulo en bruto (antes de post). Proveedores de terceros más baratos pueden reducir esto sustancialmente.
- **Tiempo humano**: el cuello de botella real no es el dinero sino el tiempo de iteración manual (prompt → generar → revisar consistencia → repetir). Merece la pena planear un capítulo piloto corto (1 escena, 1–2 min) antes de comprometer el capítulo completo, para calibrar cuántos intentos por clip necesitas en la práctica.

---

## 9. Resumen ejecutivo / próximos pasos recomendados

1. **Pilotar con una sola escena** (la del diálogo Miguel/Gabriel, ~1 min) antes de intentar un capítulo entero: es la prueba de fuego perfecta para validar shot/reverse-shot + Character DNA + audio-solo-diálogo-más-ambiente-en-post.
2. **Convertir las fichas de `content/lore/personajes.md` en "Ingredients" visuales** reutilizables (una imagen de referencia limpia por personaje) — inversión única que paga en todos los capítulos futuros.
3. **Decidir el "look" de color del proyecto una vez** (LUT + reglas de iluminación por facción: Cielo=luz fría/dorada, Infierno=cálido/rojo-sombra, etc., coherente con las fichas ya escritas) y documentarlo como referencia para cada prompt.
4. **Reservar la técnica de "toma continua oculta" (whip pan, cobertura de objeto, match-on-action) para los momentos de clímax visual** de cada capítulo, no para diálogo cotidiano — ahí el shot/reverse-shot clásico es más simple, más barato y ya "no se nota el corte" porque el espectador lo espera.
5. Evaluar si conviene generar el diseño de sonido/ambiente por completo en post (DaVinci Fairlight/Audition) en vez de depender de que Veo3 lo mantenga consistente entre clips — parece ser el consejo más repetido y con mejor relación esfuerzo/resultado en las fuentes.
6. Si se decide automatizar parte del pipeline (guion → shot list → prompts) podría integrarse como un flujo adicional dentro de `src/`/`config/flows/`, en la línea de lo que ya hace el proyecto para generación de prosa — pero eso sería una fase posterior, no parte de esta investigación.
