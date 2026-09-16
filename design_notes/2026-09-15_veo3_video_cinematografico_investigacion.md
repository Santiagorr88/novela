# Investigación: vídeos cinematográficos largos (5–20 min) con Veo 3 para adaptar la novela

> Fecha: 2026-09-15
> Objetivo: determinar un workflow realista para convertir capítulos de *Chronicles of the Sundering Judgment* en vídeos cinematográficos de 5–20 minutos usando Veo 3/3.1, encadenando clips de 8 segundos sin que se noten los cortes (incluyendo planos de diálogo de ~1 minuto que deben leerse como una sola toma continua).
> Nota sobre las fuentes: `youtube.com` y `youtu.be` están bloqueados por el proxy de red de este entorno (egress bloqueado), así que no pude abrir directamente los 3 vídeos enlazados. Los identifiqué por su ID vía búsqueda y documento lo que encontré sobre cada uno abajo; el resto del informe se apoya en ~25 búsquedas adicionales sobre documentación oficial, blogs especializados, foros y tutoriales (fuentes citadas en cada sección).

> **Actualización — pivote de formato (misma fecha):** tras revisar esta primera pasada, se confirmó que el objetivo es un **vídeo narrado** (voz en off que cuenta el capítulo, estilo audiolibro/documental cinematográfico), no una dramatización con personajes hablando en diálogo directo y lip-sync. Esto **simplifica bastante** el problema técnico central de las secciones 2–3: sin lip-sync que mantener, la pista de audio maestra es la narración (continua, generada aparte y nunca cortada) y el vídeo de Veo3 pasa a ser "ilustración visual" (B-roll cinematográfico) que se corta libremente al ritmo de las frases narradas. Ver la **sección 9 (nueva)** para el pipeline específico de este formato — es la sección más relevante para el trabajo inmediato; las secciones 1–8 siguen siendo útiles como fondo técnico y como opción avanzada (dramatizar algún diálogo puntual dentro del vídeo narrado).

---

## 0. Los 3 vídeos de referencia

| Link | Lo que pude identificar |
|---|---|
| `youtu.be/oodW_W15rLY` | No se pudo confirmar el título exacto (bloqueo de red + el ID no aparece indexado con contexto claro). Probablemente contenido general sobre Veo 3 (los resultados de búsqueda relacionados apuntan a vídeos oficiales tipo "Meet Veo 3"). **Recomendación**: si es importante, pásame el título o una captura y lo incorporo. |
| `youtube.com/shorts/AeGhWSYQkmc` | Tampoco se pudo confirmar con certeza. El contexto de búsqueda apunta a la ola de contenido sobre "Veo 3 Fast llega gratis a YouTube Shorts" (anuncio de sept. 2025). Podría ser un short mostrando esa función nativa, no necesariamente una técnica de edición avanzada. |
| `youtu.be/c772SYf6k-4` | **Sí identificado**: *"How to Finally Make Long Videos with VEO 3.1 (Create Consistent Videos of Any Length)"*, subido ~29 oct 2025. Trata sobre cómo generar vídeos largos consistentes con Veo 3.1, mencionando herramientas de terceros (p.ej. HitPaw) además del propio Flow. Confirma la premisa central de tu pregunta: sí existe un método fiable para encadenar clips sin que se note el corte, y gira en torno a la técnica de "última imagen → siguiente clip" + repetición de prompt que detallo abajo. |
| `youtu.be/6iBc4aoiwf4` | **Sí identificado**: *"Veo 3 AI Movie: 'Road Less Traveled' (Continuous Dialogue Shot for One Minute)"*. Demuestra en la práctica la técnica de Frames-to-Video (sección 2.1) para producir un **plano de diálogo continuo de 1 minuto** con audio y lip-sync sincronizados encadenando generaciones de Veo 3 desde imágenes de referencia — es la prueba en vídeo de que la técnica que recomendamos en este documento funciona en un caso real de diálogo largo, no solo B-roll. |
| `youtu.be/i_KlptBTdck` | **Sí identificado** (por título/descripción que compartiste): *"How to Create Long AI Animation Videos with Consistent Characters \| VEO 3.1 + Google Flow"*, 18:35 min, subido 10 nov 2025, con hashtags `#africanfolktales #googleaistudio #googleflow`. Este es exactamente el género que necesitamos como referencia: canales que adaptan **cuentos/folclore narrados** (guion → narración en off → animación con personajes consistentes) a vídeos largos con VEO 3.1 + Flow — es prácticamente el mismo objetivo que tu novela, aplicado a folclore africano en vez de a *Chronicles of the Sundering Judgment*. Busqué el flujo típico de este tipo de canales (ver §9.5, nueva) y confirma y refina el pipeline narrado de la sección 9. |

Si me compartes capturas de pantalla o transcripciones de los otros dos, los integro en una revisión de este documento.

### 0.1 Catálogo adicional de vídeos de referencia (aportados por el usuario, 16 sept.)

El usuario compartió esta lista de títulos/canales para orientar la investigación. No pude abrir ninguno directamente (bloqueo de red), pero los localicé e investigué su contenido por título:

| Vídeo | Canal | Qué aporta |
|---|---|---|
| *How to Create Long AI Animation Videos with Consistent Characters \| VEO 3.1 + Google Flow* | King Charles Tv (183K) | El mismo vídeo de folclore africano ya documentado en §0 (`i_KlptBTdck`) y §9.5. |
| *How to Finally Make Long Videos with VEO 3.1 (Create Consistent Videos of Any Length)* | AI PIPELINE (73K) | El mismo vídeo ya documentado (`c772SYf6k-4`), técnica Frames-to-Video + repetición de prompt (§2). |
| *Tutorial Google Veo 3.1 en Flow: la IA para hacer videos que REVOLUCIONA TODO* | Alan Daitch (32K) | Tutorial general en español de Flow (oct. 2025); confirma las funciones ya cubiertas (audio más rico, control narrativo, Img-to-Video mejorado) sin técnica adicional relevante. |
| *GOOGLE VEO 3: GUÍA DEFINITIVA Desde Cero para Videos VIRALES y Prompts* | Arca Artificial by Lordwind Enrique (289K) | Creador venezolano especializado en IA visual (colabora con Magnific/Freepik, Higgsfield, Kling Elite Creator). Aporta una **variante de estructura de prompt en 8 campos**: *sujeto, acción, entorno, estilo visual, perspectiva de cámara, iluminación, sonido, diálogo* — prácticamente idéntica a la de §10, confirmando el consenso entre creadores independientemente del idioma. |
| *DESDE CERO GOOGLE FLOW 2026 Tutorial Gratis — Parte 1* | AyA Academy IA (19K) | Tutorial en español para principiantes; confirma el dato práctico de que **cualquier cuenta de Google recibe 50 puntos gratis al día en Flow** (no acumulables) para probar sin suscripción — útil para pilotar antes de pagar Pro/Ultra (ver §1 y §8). |
| *This Is How To Use Google Veo 3 Like A PRO: JSON Prompt* | Sebastien Jefferies (309K) | Refuerza el enfoque JSON ya documentado en §4/§10; sin hallazgos adicionales verificables más allá de lo ya cubierto. |
| *How to Use Veo 3 to Build Short Films — Prompting Like a Pro* | EchoLab AI (83K) | Aporta la técnica del **"prompt sandwich"** y confirma de forma independiente la técnica de imagen-primero-luego-animar (§9.5) — ver detalle abajo. |
| *Easily Create Long Videos with Consistent Characters using VEO 3* | King Charles Tv | Ya documentado en la búsqueda en español de la sección 5 (técnica de personaje en croma/green-screen). |

**Técnica nueva — "prompt sandwich" (EchoLab AI) para cortometrajes con Veo3:**
1. **Capa 1 — ingrediente principal**: el sujeto/personaje (igual que el "Subject" de las plantillas anteriores).
2. **Capa 2 — acción central**: qué está pasando, una sola acción por clip.
3. **Capa 3 — detalles técnicos**: ángulo de cámara, iluminación, movimiento.
4. **Capa 4 — estilo**: mood, paleta de colores, género/tono.

Además, confirma dos reglas prácticas que conviene subrayar para tu proyecto: **no metas una historia entera en un solo clip** (un clip = una acción, ya lo decíamos en §2.1, pero aquí se enfatiza como la causa #1 de resultados "caóticos"), y usa **imagen-a-vídeo (primer fotograma)** como método por defecto en vez de texto-a-vídeo puro — coincide de forma independiente con el refinamiento de §9.5. Lista de negativos recurrente en cortometrajes: `blur, shaky camera, distorted hands`.

Fuentes: [Arca Artificial — VEO 3 Guía desde 0](https://arcaartificial.com/veo-3-guia-desde-0-videos-virales/), [Google Flow gratis: 50 puntos diarios (iageducacion.org)](https://iageducacion.org/google-flow-gratis-50-puntos-diarios/), [How to Use Veo 3 to Build Short Films — EchoLab AI (YouTube)](https://www.youtube.com/watch?v=0ZZnRSWIleg), [How to Write Veo 3 Prompts: Complete Tutorial (veotutorials.substack.com)](https://veotutorials.substack.com/p/how-to-write-veo-3-prompts-complete).

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

## 9. Formato narrado (voz en off): pipeline específico

Esta es la sección que aplica directamente a "convertir los capítulos en un vídeo cinematográfico **narrado**". Cambia el orden de producción respecto a un vídeo con diálogo dramatizado: **la narración se genera primero y por completo, entera y sin cortes**; el vídeo se construye después *alrededor* de ese audio, no al revés.

### 9.1 Por qué el formato narrado es más fácil que el dramatizado

- **No hay lip-sync que mantener.** El problema más difícil de las secciones 2–3 (que un corte entre clips de 8s no rompa la ilusión de una boca hablando de forma continua) desaparece casi por completo: los personajes en pantalla no tienen por qué estar hablando a cámara, así que un corte de plano cada 5–8 segundos es completamente normal y esperado — es exactamente el lenguaje visual de un documental, un tráiler de libro o un vídeo tipo "historia narrada" (el género que domina en YouTube/TikTok con historias de Reddit, mitología, terror, etc.).
- **Veo 3 genera silencioso por defecto** si no le pides audio explícitamente — es decir, ya está pensado para funcionar como B-roll puro bajo una voz en off separada, sin que tengas que "silenciar" nada después.
- **La consistencia de personaje/color sigue importando** (secciones 1–2, Character DNA + Ingredients), pero ya no depende de que el diálogo hablado encaje frase a frase con los labios — solo de que el personaje "se vea igual" en cada plano que ilustra la narración.

### 9.2 Pipeline de producción (orden correcto)

1. **Adaptar el texto del capítulo a guion de narración.** No es el texto literal de la novela palabra por palabra: hay que
   - mantener la voz del narrador en tercera persona tal cual (tu prosa ya está escrita para eso),
   - decidir qué hacer con el diálogo entrecomillado: lo más simple para un narrado puro es que el propio narrador lo lea integrado ("—No puedo —dijo Miguel, con la mirada ya encendida—" se lee todo con la misma voz, solo con una leve inflexión dramática al llegar a la cita), sin necesidad de voces de personaje separadas,
   - recortar redundancias/descripciones muy extensas si el ritmo se vuelve lento para vídeo (el narrado tolera menos "relleno atmosférico" seguido que la prosa escrita, porque en audio no hay forma de "leer en diagonal").
2. **Generar el audio de narración completo, de una sola vez, con una única voz** (ElevenLabs, modelo **Multilingual v2 / Studio** para calidad de audiolibro en español). Usar **una sola voz fija para todo el proyecto** — es mucho más fácil de mantener consistente que las voces de personaje, porque solo hay una.
   - Crear un **diccionario de pronunciación** con los nombres propios del universo (Ereloth, Azael, Thaeriel, Solmire, Serephis, etc.) para que la IA no los pronuncie distinto entre capítulos.
   - Generar en trozos de párrafo/escena (no todo el capítulo en una sola llamada) para poder revisar y regenerar solo el trozo que falle, pero **conservando siempre la misma configuración de voz/velocidad/estabilidad** para que al unir los trozos no se note el cambio.
3. **Trocear el audio final en segmentos naturales** (por frase u oración) y anotar la duración exacta de cada uno — esto es tu "shot list temporal": cada segmento de narración es un hueco que hay que rellenar con un plano.
4. **Generar los clips de Veo3 como B-roll silencioso** (o con audio ambiente muy discreto, sin diálogo hablado) que ilustren cada segmento:
   - Duración de cada clip generado en Veo3: 5–8s (dentro de su rango nativo, sin necesitar extender la mayoría de las veces).
   - Si un segmento narrado dura más de 8s, aquí sí aplican las técnicas de la sección 2 (Frames-to-Video encadenado, Character DNA repetido) para producir un plano más largo; si dura menos, simplemente se recorta el clip o se deja un plano estático/lento que sobra en post.
   - Para pasajes puramente descriptivos/atmosféricos (paisajes, arquitectura celestial/infernal, objetos), usar planos con movimiento de cámara lento y constante (push-in, pan lento) — es el punto fuerte de Veo3/Luma para B-roll y el más barato de generar bien a la primera.
5. **Montaje**: la narración va en la pista maestra, **continua, sin cortes ni crossfades** (es la columna vertebral del vídeo). Los clips visuales se colocan encima, cortando aproximadamente en los límites de frase/oración marcados en el paso 3 — igual que se edita cualquier documental o vídeo de "storytime". No hace falta ocultar estos cortes con whip pans ni cobertura de objeto (sección 2.2): un corte de plano bajo narración continua ya es invisible por convención de género.
6. **Música y ambiente** en una capa aparte, por debajo de la narración, con crossfades suaves entre escenas (aquí sí aplican J-cuts/L-cuts y "ambient bed" de la sección 3, pero ahora sirven para separar *escenas* del capítulo, no líneas de diálogo).
7. **Color grading final** sobre todo el corte (sección 5) para unificar el look de todos los clips generados en distintas sesiones.

### 9.3 Cuándo sí merece la pena "dramatizar" (mezcla híbrida, opcional)

El formato 100% narrado es el más rápido y barato de producir en serie (bueno si el objetivo es sacar muchos capítulos con consistencia). Si en algún momento se quiere subir el nivel cinematográfico, se puede **hibridar**: mantener la narración en off para los tramos descriptivos/introspectivos, y cambiar puntualmente a una escena dramatizada con diálogo hablado y lip-sync (aplicando entonces sí toda la sección 2–3 de este documento) en los 1–2 momentos de mayor tensión del capítulo — por ejemplo, en B1C01, dramatizar la breve confrontación Miguel/Gabriel con sus propias voces, y dejar todo lo demás (la marcha por Serephis, la arboleda, la visión cósmica, la escena de Lucifer) en narración pura sobre B-roll. Es una decisión de presupuesto/tiempo, no técnica: ambas cosas son compatibles en el mismo vídeo.

### 9.4 Ejemplo aplicado (B1C01, primer párrafo)

- **Narración** (una sola toma de audio, sin cortes): *"La marcha a través de Serephis era un ejercicio de deshilachamiento. No del cuerpo, aunque el calor fundía la arena en láminas de vidrio negro bajo sus sabatones... Su mano, enfundada en el guantelete, subió a su pecho por instinto..."* (≈35s de audio a 145–155 palabras/min).
- **Plano 1** (0–8s): plano general, Miguel caminando por el desierto agrietado, cámara estática con leve deriva, luz de "cielo color moretón". *Sin diálogo, sin audio hablado.*
- **Plano 2** (8–16s): plano medio, calor deformando el aire sobre la arena de vidrio negro, Miguel en el fondo del encuadre.
- **Plano 3** (16–24s): primer plano de la mano enguantada subiendo al pecho — corte simple de plano, sin necesidad de ocultarlo, porque la voz narrativa nunca se interrumpe y arrastra la continuidad emocional de un plano a otro.
- ... y así sucesivamente, un plano nuevo cada 5–8s de narración, generado silencioso, con Character DNA de Miguel repetido en cada prompt para que no cambie de aspecto entre planos.

Fuentes: [How to Make an AI Story Video in 2026 (Anijam)](https://www.anijam.ai/blog/how-to-make-ai-story-video/), [AI Story Video Generator — multi-scene, consistent characters, synced voiceover (Novi AI)](https://www.noviai.ai/), [Veo 3 B-Roll Generator: Cinematic Stock Footage with AI (veo3ai.io)](https://www.veo3ai.io/blog/veo-3-b-roll-generator-2026), [Veo 3 Native Audio Prompt Guide 2026 (veo3ai.io)](https://www.veo3ai.io/blog/veo-3-native-audio-prompt-guide-2026), [How to make an audiobook using AI (ElevenLabs)](https://elevenlabs.io/blog/how-to-make-an-audiobook), [ElevenLabs Audiobooks docs](https://elevenlabs.io/docs/eleven-creative/products/audiobooks), [Narrator AI Voices — ElevenLabs Voice Library](https://elevenlabs.io/voice-library/narrator-voices), [How to Sync Audio and Video in Premiere (murf.ai)](https://murf.ai/blog/how-to-sync-audio-and-video-in-premiere).

### 9.5 Refinamiento confirmado por canales de "folclore narrado" (African folktales + VEO 3.1/Flow)

El vídeo `i_KlptBTdck` pertenece a un género ya consolidado en YouTube: canales "faceless" que adaptan cuentos/folclore a vídeos largos narrados con IA. El flujo que usan estos canales (confirmado por varias fuentes coincidentes) **añade un paso que conviene incorporar al pipeline de la sección 9.2**, entre el paso 1 (guion) y el paso 4 (generar clips):

**Ancla la identidad en una imagen fija antes de animar — no generes vídeo directamente desde texto para los personajes recurrentes.**

1. Por cada personaje recurrente, genera primero **una imagen "hero" fija** con un generador de imágenes (Imagen 3 dentro de Flow, Nano Banana, Freepik, etc.) a partir de la ficha de `content/lore/personajes.md`, hasta conseguir un retrato que te convenza al 100%.
2. Construye a partir de ahí una **hoja de referencia** (turnaround: frente, perfil, 3/4, espalda) y variantes con distinta expresión/pose — esto es tu "banco de imágenes" del personaje, reutilizable en todos los capítulos.
3. Sube esas imágenes como **Ingredient / Frames-to-Video source** en Flow: cada plano se anima *desde una imagen ya validada*, no desde una descripción de texto nueva cada vez. Esto es más fiable que repetir el "Character DNA" en texto (sección 2.1) porque elimina la variabilidad de que el modelo "reinterprete" la descripción cada vez — la imagen ya fija el aspecto exacto.
4. Para el siguiente plano del mismo personaje en una pose/escena distinta, toma la **siguiente imagen del banco** (no la misma repetida) y anímala — mantiene coherencia sin producir el mismo plano congelado una y otra vez.
5. Regla de consistencia textual complementaria: nunca describas al personaje de forma distinta entre prompts (si lleva "armadura dorada agrietada" en el plano 1, no lo llames "armadura plateada" en el plano 5) — la imagen ancla lo visual, pero el texto del prompt de animación debe seguir siendo coherente con ella.

Esto encaja de forma natural con el pipeline narrado: como cada plano bajo narración dura solo 5–8s y cambia con cada frase, tener un banco de 5–10 imágenes ya validadas por personaje (distintas poses/expresiones) es más rápido y barato que generar cada plano a ciegas desde texto, y es exactamente lo que permite a estos canales sacar episodios de 15-20 minutos con personajes que no "derivan" de aspecto entre escena y escena.

Fuentes: [The Only VEO3 Workflow That Actually Keeps Your Character Consistent (Medium)](https://medium.com/@anup.karanjkar08/the-only-veo3-workflow-that-actually-keeps-your-character-consistent-e7634278b75a), [Veo 3 Image Reference Workflow 2026 (veo3ai.io)](https://www.veo3ai.io/blog/veo-3-image-reference-workflow-2026), [Master Veo 3: Pro Image-to-Video Techniques Guide (arsturn)](https://www.arsturn.com/blog/how-to-use-veo-3s-image-to-video-feature-like-a-pro), [AI Character Consistency: 5 Methods Compared 2026 (Flick)](https://flick.art/blog/img2img-consistent-character), [n8n workflow: consistent character videos with Veo 3.1, GPT-4o, Nano Banana](https://n8n.io/workflows/11594-creating-consistent-character-videos-with-veo-31-gpt-4o-and-google-nanobanana/), búsqueda sobre canales de folclore narrado con VEO 3.1 + Flow (confirmando el género y flujo general: guion → imágenes → narración TTS → animación → montaje en CapCut).

---

## 10. Anexo: plantillas de prompts concretas (formato "2025 Professional" + trucos de repos)

Extraído directamente del repositorio [snubroot/Veo-3-Prompting-Guide](https://github.com/snubroot/Veo-3-Prompting-Guide) (README completo) y contrastado con varios packs comerciales de Gumroad. Es una plantilla de **7 componentes en inglés natural** (no JSON puro, pensada para pegar directo en el cuadro de texto de Flow/Veo3):

1. **Subject** — descripción física exacta y estable del personaje (edad, rasgos, vestuario, marcas distintivas) — es tu "Character DNA" de la sección 2.1, aquí formalizado.
2. **Action** — movimientos y comportamiento concretos.
3. **Scene** — entorno, atrezzo, montaje de iluminación.
4. **Style** — tipo de cámara, ángulo, movimiento, estética.
5. **Dialogue** — con indicador de tono emocional.
6. **Sounds** — elementos de audio y ambiente.
7. **Technical** — prompt negativo (qué excluir).

**Trucos concretos que aporta este repo y que no habíamos documentado:**

- **Truco de posición de cámara**: añadir literalmente la frase *"(that's where the camera is)"* después de describir un punto del espacio mejora mucho el acierto de dónde coloca Veo3 la cámara — un hallazgo empírico reportado por la comunidad, no algo "oficial" de Google, pero replicado por varios creadores.
- **Diálogo sin subtítulos falsos**: confirma lo ya documentado — dos puntos antes de la cita (`El detective mira a cámara y dice: "Algo no va bien aquí." Su voz transmite sospecha y determinación.`) en vez de comillas sueltas.
- **Método "This Then That" para extensión de escena**: en vez de solo repetir el Character DNA al extender un clip, describe una **progresión emocional explícita** de un estado a otro dentro del mismo prompt de extensión — ej.: *"El personaje empieza confuso e inseguro, luego se vuelve gradualmente confiado y decidido, y termina con una sonrisa satisfecha."* Esto le da al modelo un arco claro para el clip completo en vez de una instantánea estática, y ayuda a que el "extend" no se sienta como una repetición plana del clip anterior.
- **Audio explícito para evitar alucinaciones sonoras**: describir el paisaje sonoro esperado línea por línea (`Audio: tráfico lejano, bocinas ocasionales, pasos sobre el pavimento, conversaciones apagadas, ambiente de ciudad`) reduce que Veo3 invente sonidos incongruentes con la escena — aplicable directamente a tus escenas celestiales/infernales (ej. "Audio: zumbido grave de energía angelical, eco de catedral vacía, viento cálido de desierto").
- **Librería de 10+ movimientos de cámara con nombre técnico** (dolly, pan, tilt, tracking, crane, zoom, handheld, orbit) — usar el término técnico exacto en el prompt (no "muévete hacia él" sino "dolly-in lento de plano general a plano medio") da resultados más consistentes.
- **Prompt negativo estándar reutilizable**: `no text overlays, no watermarks, no cartoon effects, no unrealistic proportions, no blurry faces` — plantilla de partida que se puede ampliar con `no subtitles` (sección 4).

**Nota honesta sobre los packs de pago (Gumroad)**: existen decenas de "packs de prompts JSON" de pago (ej. *Google VEO 3.1 Master Prompts Pack*, *100+ AI Ads JSON Prompts*) — están orientados casi todos a **anuncios de producto/marketing viral**, no a narrativa de ficción/fantasía épica, así que su utilidad directa para adaptar la novela es baja; el valor real está en la estructura (los 7 campos de arriba), que ya queda documentada aquí sin necesidad de comprar nada.

Fuentes: [snubroot/Veo-3-Prompting-Guide (README)](https://github.com/snubroot/Veo-3-Prompting-Guide), [LCKuo/veo-3-prompting-guide (fork)](https://github.com/LCKuo/veo-3-prompting-guide), [shijincai/veo3-prompt-generator](https://github.com/shijincai/veo3-prompt-generator), [Free Veo 3.1 AI Video Prompts Library (Filmora)](https://filmora.wondershare.com/ai-prompt/veo3-1-prompt.html), [Best Veo 3 Prompt Examples (UlazAI)](https://ulazai.com/veo3-prompt-examples/).

---

## 11. Resumen ejecutivo / próximos pasos recomendados

1. **El formato objetivo es narrado (sección 9), no dramatizado** — esto simplifica el problema de "cortes en escenas largas" porque el audio maestro es la voz en off continua, no diálogo con lip-sync. Empezar por ahí antes de invertir en las técnicas más complejas de las secciones 2–3.
2. **Pilotar con un solo párrafo/escena corta** (el primer párrafo de B1C01, ejemplo en 9.4) antes de intentar un capítulo entero: valida narración → segmentación → generación de planos → montaje en un ciclo pequeño.
3. **Fijar una única voz de narrador para todo el proyecto** en ElevenLabs (Multilingual v2/Studio) + diccionario de pronunciación con los nombres propios del universo — inversión única que se reutiliza en todos los capítulos.
4. **Convertir las fichas de `content/lore/personajes.md` en "Ingredients" visuales** reutilizables (una imagen de referencia limpia por personaje) para que se vean iguales en los planos silenciosos de cada capítulo.
5. **Decidir el "look" de color del proyecto una vez** (LUT + reglas de iluminación por facción: Cielo=luz fría/dorada, Infierno=cálido/rojo-sombra, coherente con las fichas ya escritas) y documentarlo como referencia para cada prompt.
6. **Reservar la dramatización con diálogo/lip-sync (secciones 2–3) para 1–2 momentos de clímax por capítulo**, como mejora opcional una vez el pipeline narrado esté rodando, no como requisito desde el primer vídeo.
7. Evaluar si conviene generar el diseño de sonido/ambiente por completo en post (DaVinci Fairlight/Audition) en vez de depender de que Veo3 lo mantenga consistente entre clips.
8. Si se decide automatizar parte del pipeline (texto de capítulo → guion de narración → segmentos → prompts de plano) podría integrarse como un flujo adicional dentro de `src/`/`config/flows/`, en la línea de lo que ya hace el proyecto para generación de prosa — pero eso sería una fase posterior, no parte de esta investigación.
