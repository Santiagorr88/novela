---
name: storyboard-production
description: "Convert a finished, approved chapter of Chronicles of the Sundering Judgment into a full shot-by-shot cinematic production package (technical script, Storyboard Studio JSON, EN markdown, audit checklist) via a panel of specialist agents — cinematography, sound/atmosphere, continuity/canon — coordinated into one source-of-truth JSON, ready to paste into Google Flow's Storyboard Studio. MANDATORY TRIGGERS: 'produce el capitulo X para video', 'genera el storyboard de', 'pasada de produccion cinematografica', 'convierte este capitulo a guion tecnico'. Runs per-chapter, one invocation per chapter. Only after the chapter's prose has passed chapter-review — never on a draft that can still change."
---

# Storyboard Production Council

Formaliza como skill lo que hicimos a mano para el capítulo 1: convertir un capítulo de prosa aprobado en un guion técnico shot-a-shot (cámara, sonido, continuidad) listo para Storyboard Studio. Es la tercera pieza del sistema multiagente del proyecto (`content/craft/11_sistema_agentes.md`) — misma forma que `chapter-review` y `beat-planner`: coordinador + especialistas paralelos sobre una memoria compartida, nunca un agente por capricho de detalle.

## Mapeo de especialidades — por qué solo 3 agentes

Un equipo real de Hollywood tiene ~15 roles (showrunner, guionista, DoP, production designer, concept artist, storyboard artist, costume, VFX, sound designer, compositor, ADR, casting, actores, continuity, editor, colorista, mezcla). Para este pipeline (Flow/Veo3/Storyboard Studio, personajes ya diseñados y castings) la mayoría ya está resuelta o no aplica:

- **Ya resuelto, no requiere agente**: casting/actores (voces en `audiolibro_casting.json`, audio congelado por defecto), concept art y costume (referencias aprobadas en `character_library/` y `produccion_cinematografica/variantes_por_personaje/`), guion de adaptación (el propio shot breakdown de este skill).
- **No aplica a generación AI shot-a-shot**: VFX supervisor (el fuego/alas los genera Veo3 desde el texto de cámara, no un departamento aparte), compositor (no hay score continuo entre shots).
- **Fase posterior, no parte de este skill**: editor de montaje, colorista, mezcla de sonido — entran cuando ya existan los clips generados, no al producir el guion.
- **Lo que sí queda como trabajo real, un agente cada uno**: dirección de fotografía, sonido/atmósfera, continuidad y canon.

## Cuándo correr esto

- Solo sobre un capítulo cuya prosa ya pasó `chapter-review` con PASS (o PASS WITH FIXES ya aplicados). Nunca sobre un borrador que puede cambiar — produce vídeo de algo inestable.
- Regla del autor (CLAUDE.md #1): paso a paso, libro a libro. Se corre sobre Libro I, se aprueba con el autor, y solo entonces se escala a Libro II/III — no adelantar capítulos de otro libro sin luz verde explícita.

## Inputs requeridos

- Prosa EN del capítulo: `Libro{N}/EN/NN_Titulo.md` (fuente canónica).
- Narración de audiolibro EN: `Libro{N}/audiolibro/en/capitulo_NN.txt` (diálogo ya limpio, referencia de ritmo).
- `content/lore/personajes.md` y `content/lore/grafo_conocimiento.md` — quién sabe qué, estado de cada personaje en este punto de la trama.
- `character_library/**/canonical/*.png` — referencias visuales aprobadas. No se regeneran ni reinterpretan.
- `produccion_cinematografica/variantes_por_personaje/*.md` — variantes visuales ya decididas por el autor (p.ej. ala chamuscada de Miguel).
- Si ya existe un JSON de storyboard previo para el capítulo en `storyboard_studio_exports/`, se usa como base a enriquecer — nunca se recrea desde cero.
- `audiolibro_casting.json` solo si el autor ha activado audio explícitamente (por defecto, congelado).

## Paso 1 — Comprensión: shot breakdown (memoria compartida)

Antes de lanzar especialistas, construir (o actualizar, si ya existe) la lista maestra: escenas del capítulo → shots dentro de cada escena, numeración estable, quién aparece, qué ocurre, dónde. Nada de cámara/sonido fino todavía.

Esta lista es la memoria compartida que leen los tres especialistas del Paso 2. Sin ella, cada uno "produce un capítulo ligeramente distinto" — mismo riesgo que ya documentó `11_sistema_agentes.md` para la auditoría editorial.

Regla dura (aprendida en la pasada manual del capítulo 1): **un shot = una imagen**. Nunca un "cut to X" dentro de la descripción de un mismo shot — si dos encuadres son necesarios, son dos shots consecutivos, no uno compuesto.

## Paso 2 — Análisis paralelo: 3 especialistas, misma memoria

Cada uno recibe SOLO el shot breakdown del Paso 1 más su documento de referencia — no el canon completo, para que el brief sea barato y enfocado (mismo principio que `chapter-review`). Lanzarlos en paralelo, no en serie.

### Especialista 1 — Dirección de fotografía
Grounding: shot breakdown + `character_library/` (rasgos físicos exactos) + variantes ya aprobadas.
Añade a cada shot: encuadre, movimiento de cámara, luz, foco emocional. Una imagen ganada por shot (calibre B, `content/craft/12_calibre_b.md`), nunca descripción genérica. Presencia por efecto, no por fórmula repetida (`13_presencia_cinematografica.md`).
Respeta la regla de un-shot-una-imagen del Paso 1; si necesita un encuadre nuevo, propone un shot adicional, no lo comprime en la descripción existente.

### Especialista 2 — Sonido y atmósfera
Grounding: shot breakdown + descripciones de localización del capítulo (props, clima, textura del lugar).
Añade `audioDescription` por shot: ambiente, textura física (viento, cristal, pasos, peso de objetos/armadura). Sin música original — fuera de alcance de este pipeline (ver mapeo arriba).

### Especialista 3 — Continuidad y canon
Grounding: `grafo_conocimiento.md`, `personajes.md`, variantes aprobadas.
Verifica, shot a shot: estado físico de cada personaje coherente con lo ya ocurrido en el capítulo (armadura, heridas, alas — no puede aparecer intacto después de dañarse); que ningún shot muestre a un personaje actuando sobre algo que el grafo de conocimiento dice que aún no sabe; marca cualquier localización/prop sin ficha existente para que el autor decida si hace falta un asset nuevo.

## Paso 3 — Coordinación: fusión + QA doble

El orquestador (no un agente) recibe los 3 informes:
- Resuelve conflictos entre especialistas (p.ej. fotografía pide un plano que continuidad marca como imposible por el estado del personaje en ese punto) — alguien tiene que decidir, igual que el editor jefe en `11_sistema_agentes.md`.
- Fusiona todo en el JSON único (`storyboard_studio_exports/capNN_storyboard_studio_FECHA.json`), añadiendo/editando `frames` sin tocar la estructura ya validada.
- Regenera desde el JSON — nunca al revés — el markdown EN legible y el checklist de auditoría.
- QA doble (CLAUDE.md regla #8): verificación contra el texto real del capítulo + revisión independiente vía `codex exec --sandbox read-only`; QA transversal de densidad/repetición si el capítulo ya llevaba varias pasadas.
- Presenta el resultado al autor antes de cerrar la pasada. Decisiones de estilo visual o de casting de voz siempre las decide él — este skill nunca las toma por su cuenta.

## Paso 4 — Guardar y reportar

- JSON, markdown y checklist actualizados en `produccion_cinematografica/`.
- Informe de la pasada en `design_notes/AAAA-MM-DD_produccion_capNN.md`.
- Commit con mensaje en español describiendo la decisión del autor que originó la pasada (CLAUDE.md regla #9).
- Resumen corto en chat — nunca pegar el JSON completo en el mensaje.

## Relación con otras skills

- Corre DESPUÉS de que `chapter-review` dé PASS a la prosa del capítulo — nunca antes, para no producir vídeo de una escena que aún puede cambiar.
- No sustituye a `chapter-review` ni a `beat-planner` — aquellas trabajan la prosa; esta traduce prosa ya cerrada a plano/vídeo.

## Escalado a "serie"

Validado el capítulo 1 del Libro I con este proceso, el mismo skill se reinvoca capítulo a capítulo sin rediseñar nada: es la base para que la suma de los capítulos de un libro sea una temporada, y los tres libros, la serie completa. No adelantar a Libro II/III sin aprobación explícita del autor (regla #1).
