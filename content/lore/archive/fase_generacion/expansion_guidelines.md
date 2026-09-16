# Directrices de expansión — reglas estables (Libro I, II, III)

Fecha de esta división: 2026-08-20 — este documento se dividió en un archivo de reglas estables (este) y trackers de progreso por libro, porque el archivo combinado original (`expansion_guidelines.md`, 453 líneas) mezclaba reglas que casi nunca cambian con un log de progreso cronológico que crecía con cada capítulo aprobado, dificultando su navegación de un tirón. Ver `design_notes/2026-08-20_project_audit_lore.md` (sección 3) para el diagnóstico que motivó la división.

## Progreso de escritura — ver documentos separados

Este archivo contiene SOLO las reglas estables (categorías de expansión, regla de consistencia, objetivo de duración/densidad de beats). El log cronológico de qué se escribió, qué rondas de Codex pasó y qué se corrigió vive ahora en:

- Libro I: `expansion_progress_libro1.md`
- Libro II: `expansion_progress_libro2.md`
- Libro III: `expansion_progress_libro3.md`
- Sesiones/auditorías que cruzan varios libros a la vez (no un solo libro): `expansion_progress_cruzado.md`

Fecha: 2026-08-08
Contexto: para llegar a 600-800 páginas por libro sin relleno, hace falta ~duplicar el número de beats (128 → ~230-285 para el Libro I). Estas son las categorías de contenido nuevo aprobadas, a aplicar sistemáticamente capítulo a capítulo, no solo en el Capítulo 1.

## Categorías de expansión aprobadas

1. **Desarrollo de otros personajes** — no solo Miguel/Belial/Gabriel. Personajes ya nombrados en el elenco (Camael, Raphael, Uriel, Zadkiel, Iofiel, Sariel, y los cientos de Squad Leaders sin usar en `prompt_universo.md`) ganan escenas propias donde el esquema actual solo los menciona de pasada.
2. **Explicar el sistema de reencarnación dentro de la historia** — hoy el ciclo de reencarnación (Fundamental Laws) es conocimiento del lector implícito por el canon, pero **ningún personaje lo explica en escena**. Añadir momentos donde esto se articule narrativamente (p. ej. Iofiel explicándoselo a alguien, o un personaje humano descubriéndolo) en vez de asumir que el lector ya lo sabe.
3. **Aclarar quién es quién** — con tantos nombres, dar a los personajes secundarios un momento de presentación más claro cuando aparecen (no solo nombre + una frase), para que el lector no se pierda.
4. **Nuevas localizaciones** — más allá de las 5 ya fichadas (Navarion, Turein, Silent Choir, Weeping Sepulcher, Valley Inverted), es aceptable introducir localizaciones nuevas menores con criterio (una posada, un puesto fronterizo, un barrio de la Tierra) siempre que no contradigan nada ya establecido.
5. **Más conversaciones** — diálogos extendidos entre personajes que hoy solo interactúan en una frase o dos; usar el diálogo para caracterizar, no solo para transmitir plot.
6. **Batallas más épicas** — las secuencias de combate existentes (Zaphor'el, la Ambush de Aamon, el asalto final de Belial) pueden ganar más planos de acción, más POVs secundarios dentro de la misma batalla, sin cambiar el resultado.

## Regla de consistencia que sigue aplicando a toda expansión

Cualquier beat nuevo debe, antes de aceptarse: (a) no contradecir ninguna Ley Fundamental ni ficha de personaje ya fijada, (b) si introduce lore nuevo (localización, evento histórico, entidad), marcarlo explícitamente como invención nueva para poder rastrearla después, y (c) si reintroduce un elemento (arma, personaje, lugar) que no vuelve a aparecer, decidir explícitamente si se deja como textura atmosférica intencionada o si necesita un pago narrativo más adelante — nunca dejarlo colgado por descuido.

## Objetivo de duración por capítulo (2026-08-08, sustituye cualquier target anterior)

**Cada capítulo se planifica para 15-20 minutos de vídeo narrado (~2.250-3.000 palabras), con 12 minutos (~1.800 palabras) como mínimo excepcional, nunca como objetivo.** Ver `reports/15_council_palabras_capitulo.md`.

**La palanca es el número de beats, no la longitud de cada beat.** A la densidad real medida (~342-450 palabras/beat, ver `beat_density_test.md`), el objetivo se traduce en una regla de planificación dura:

> **Ningún capítulo se plancha con menos de 6 beats. El rango objetivo al planificar es 6-8 beats/capítulo.**

Esto es deliberado y va en contra del instinto de "si falta longitud, escribe más por beat": el chapter-review de B1L01 (Codex + revisor de estilo, de forma independiente) ya detectó sobreescritura cuando se intentó ganar extensión dentro de un beat ya cerrado — acumulación de imágenes, símiles encadenados. Añadir contenido narrativo real (más beats) evita ese riesgo; estirar la prosa de un beat que ya se cerró, no.

**Checklist antes de dar por buena la planificación de beats de un capítulo nuevo:**
1. ¿Tiene al menos 6 beats? Si no, faltan escenas/movimientos narrativos reales, no relleno de prosa.
2. ¿Cada beat nuevo sigue viniendo de una categoría aprobada de la lista de arriba (no relleno arbitrario)?
3. ¿La suma esperada a densidad real (beats × ~342-450) cae en 1.800-3.000 palabras?

## Notas de referencia cruzada (reglas de POV citadas por número de línea en informes anteriores)

Dos lecciones de disciplina de POV se citan en varios `design_notes/*.md` de la sesión del 2026-08-19/20 por número de línea exacto de la versión combinada de este documento (p. ej. "línea 151", "línea 344"). Tras la división del 2026-08-20, esas lecciones ya no viven en este archivo de reglas estables — nacieron como hallazgos puntuales dentro del log de progreso de un capítulo concreto, no como reglas fundacionales de la lista de arriba. Quedan documentadas íntegras en su ubicación original de contenido:

- **Regla B3C20** ("generalizaciones del propio POV sobre el carácter de un tercero deben enmarcarse como memoria/pregunta/inferencia, nunca como hecho narrado") — capítulo del Libro III, ver `expansion_progress_libro3.md`, entrada B3C20 ("The Commander's Return").
- **Regla B1C15** ("la misma disciplina aplica a adverbios de certeza — 'plainly', 'clearly', 'obviously' — pegados a estados internos de terceros, incluida la otra mitad de un POV dual") — capítulo del Libro I, ver `expansion_progress_libro1.md`, entrada B1C15 ("A Fissure in the Light").

Los informes que citan estas reglas por número de línea (`design_notes/2026-08-19_overnight_audit.md` línea 103, `design_notes/2026-08-20_fresh_audit_book3.md` línea 32) son informes ya cerrados y no se han editado retroactivamente; esta nota deja constancia de la nueva ubicación para quien los consulte después de la división.
