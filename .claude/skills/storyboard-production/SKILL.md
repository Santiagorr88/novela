---
name: storyboard-production
description: "Convert a finished, approved chapter of Chronicles of the Sundering Judgment into a full shot-by-shot cinematic production package (technical script, Storyboard Studio JSON, EN markdown, audit checklist) via a complete production team of specialist agents — director, writers, story editor, cinematography, production design, concept art, storyboard/previz, costume, VFX, sound design, composer, dialogue/ADR, casting & voice direction, continuity/canon, plus a post-production pass (editor, colorist) once clips exist — coordinated into one source-of-truth JSON, ready to paste into Google Flow's Storyboard Studio. MANDATORY TRIGGERS: 'produce el capitulo X para video', 'genera el storyboard de', 'pasada de produccion cinematografica', 'convierte este capitulo a guion tecnico', 'monta el equipo de produccion para'. Runs per-chapter, one invocation per chapter. Only after the chapter's prose has passed chapter-review — never on a draft that can still change."
---

# Storyboard Production Council

El equipo de producción completo de una adaptación de Hollywood, mapeado a lo que cada rol significa cuando no hay set físico ni actores humanos: en vez de construir o fotografiar algo, cada especialista **escribe dirección precisa** que termina en un campo del JSON de Storyboard Studio. Ningún rol se elimina por "no ser indispensable" — se traduce.

| Rol de Hollywood | Agente aquí | Qué produce |
|---|---|---|
| Showrunner / director | **Dirección** | Brief de visión y tono del capítulo: qué se dramatiza, qué se corta, énfasis emocional |
| Guionista(s) de adaptación | **Guion** | Shot breakdown: prosa → escenas → shots numerados |
| Story editor | **Story editor** | Verifica que el breakdown respeta la estructura/arco del capítulo y no rompe capítulos vecinos |
| Director de fotografía | **Fotografía** | Cámara, lente, movimiento, luz por shot |
| Production designer | **Diseño de producción** | Coherencia arquitectónica/mundo entre localizaciones del capítulo |
| Concept artist | **Concept art** | Valida lo ya aprobado en `character_library/`; diseña (en texto) cualquier elemento visual nuevo que el capítulo introduzca y no exista aún |
| Storyboard artist / previz | **Composición/staging** | Encuadre y blocking dentro de cada plano (distinto de fotografía: aquí es "qué hay dentro del cuadro y dónde", no lente/movimiento) |
| Costume designer | **Vestuario** | Biblia de vestuario/armadura por personaje, y su estado exacto shot a shot (agrietada, intacta, ala chamuscada...) |
| VFX supervisor | **VFX** | Dirección de efectos sobrenaturales (fuego, alas, magia, el Sentinel) y su continuidad shot a shot |
| Sound designer | **Sonido** | Ambiente y textura física (viento, cristal, pasos, peso de objetos) |
| Compositor | **Música** | Dirección musical/leitmotiv por personaje o facción — intención, no partitura generada |
| Dialogue/ADR | **Diálogo** | Pule las líneas para timing/lip-sync, marca énfasis y pausas |
| Casting director + Actores | **Casting y dirección de voz** | Confirma el mapeo voz↔personaje ya cast (`audiolibro_casting.json`) y escribe notas de interpretación por línea (tono, ritmo, subtexto) — no hay actor físico, la "actuación" es esta dirección |
| Continuity supervisor | **Continuidad y canon** | Estado físico y de conocimiento de cada personaje shot a shot contra `grafo_conocimiento.md`/`personajes.md` |
| Editor (montaje) | **Montaje** | Plan de corte/ritmo entre shots — corre en una fase posterior, cuando ya existan clips generados |
| Colorista | **Color** | Intención de gradación por escena, coherente con el estilo global "3D-Animation" — misma fase posterior que montaje |

## Cuándo correr esto

- Solo sobre un capítulo cuya prosa ya pasó `chapter-review` con PASS (o PASS WITH FIXES ya aplicados). Nunca sobre un borrador que puede cambiar.
- Regla del autor (CLAUDE.md #1): paso a paso, libro a libro. Se corre sobre Libro I, se aprueba con el autor, y solo entonces se escala a Libro II/III.
- Decisiones de trama/estilo/casting: SIEMPRE las decide el autor (CLAUDE.md, "Cómo trabajar"). Todo lo que produzcan estos agentes es propuesta — se presenta, no se da por aprobado.

## Inputs requeridos

- Prosa EN del capítulo: `Libro{N}/EN/NN_Titulo.md` (fuente canónica).
- Narración de audiolibro EN: `Libro{N}/audiolibro/en/capitulo_NN.txt`.
- `content/lore/personajes.md`, `content/lore/grafo_conocimiento.md`, `content/lore/arco_argumental_completo.md` (o equivalente) para el story editor.
- `character_library/**/canonical/*.png` — referencias visuales aprobadas.
- `produccion_cinematografica/variantes_por_personaje/*.md` — variantes ya decididas.
- `audiolibro_casting.json` — mapeo voz↔personaje (el propio archivo de casting; el agente de voz no lo recrea, lo usa).
- Si ya existe un JSON de storyboard previo del capítulo en `storyboard_studio_exports/`, se usa como base a enriquecer, no se recrea desde cero.

## Fase 0 — Dirección: brief de visión

Un agente (o el orquestador) lee la prosa completa del capítulo y produce un brief corto, con criterios reales de dirección, no solo "tono general":
- **Tesis visual del capítulo**: una frase — qué imagen o contraste tiene que quedarse grabado (p.ej. "un ser de luz agrietándose, físicamente, delante de otro que no puede tocarlo").
- **Referentes de género/tono**: 1-2 puntos de comparación concretos (luz, ritmo, escala) para anclar a los especialistas de Fase 2 — nunca "estilo épico" sin más.
- **Qué es interior en la prosa y debe volverse imagen/acción visible** (un pensamiento no se filma; su efecto físico sí).
- **Qué se puede comprimir o fundir** sin perder el capítulo, y qué es intocable.
- **Motivos visuales a sembrar o pagar** en este capítulo si el arco general ya los estableció (consulta rápida a `arco_argumental_completo.md`).

Este brief es lo que leen Guion y Story editor a continuación — nadie más lo necesita todavía.

## Fase 1 — Guion: presupuesto de duración + shot breakdown + verificación estructural

0. **Presupuesto de duración** (antes de nada): el capítulo tiene una duración objetivo de vídeo (por defecto ~8 min, salvo que el autor indique otra por capítulo — es una decisión suya, como trama/estilo/casting). Con clips de Veo3 a 8s por shot: `duración objetivo (s) / 8 ≈ nº de shots necesarios`. Ese número es el target que Guion tiene que cubrir con contenido real de la escena — nunca rellenar con shots vacíos ni comprimir la escena en menos shots de los que necesita para no pasarse (mismo error que `beat-planner` corrige del lado de la prosa: contar primero, no escribir y ver qué sale). Si el material real de la escena no llega al número de shots necesario, la señal es que hay que dramatizar más lo que en la prosa es interior/resumen (igual que un beat-planner añade beats reales, no relleno) — nunca inventar acción que no está en el capítulo.
1. **Guion** (agente): con el brief de Fase 0, el presupuesto de shots, y la prosa, produce el shot breakdown en formato técnico real: encabezado de escena (localización + momento del día, heredado de la prosa), lista de shots numerados dentro de cada escena, quién aparece, qué ocurre, dónde, y **la función dramática del shot** (establishing / reacción / acción / transición) — esto último es lo que luego usan Fotografía y Montaje para decidir tamaño de plano y ritmo, no un dato decorativo.
2. **Story editor** (agente, tras el anterior): revisa el breakdown contra el arco argumental y los capítulos vecinos — que no se salte un beat, que no contradiga algo ya establecido en la trama; y confirma que el conteo de shots cuadra con el presupuesto de duración de la Fase 1.0. Devuelve el breakdown corregido o una lista de ajustes.

El breakdown final de esta fase es la **memoria compartida** — todo lo que sigue en Fase 2 lee esto, no la prosa cruda, y no se relee entre sí (mismo principio de `content/craft/11_sistema_agentes.md`: sin memoria común, cada agente produce un capítulo ligeramente distinto).

Regla dura (aprendida en la pasada manual del capítulo 1): **un shot = una imagen**. Ningún "cut to X" dentro de un mismo shot — si hacen falta dos encuadres, son dos shots consecutivos.

## Fase 2 — Departamentos, en paralelo

Todos reciben SOLO el shot breakdown de Fase 1 + su propio documento de referencia — nunca el canon completo, para mantener cada brief barato y enfocado. Se lanzan juntos, no en serie. Cada descripción de abajo es el contenido técnico real que va dentro del prompt de ese agente, no solo su nombre de puesto.

**Visual**

- **Fotografía** — grounding: breakdown + `character_library/`. Para cada shot decide, con vocabulario técnico real, no genérico:
  - *Tamaño de plano* (ECU/primerísimo primer plano, CU/primer plano, MCU/plano medio corto, MS/plano medio, MLS/plano medio largo, LS/plano general, ELS/gran plano general) — escalado según la función dramática que marcó Guion: establishing = LS/ELS, reacción = CU/ECU, acción = MS/MLS con movimiento.
  - *Movimiento de cámara* (estático, panorámica, tilt, dolly/push-in, travelling lateral, grúa/boom, cámara en mano) — el push-in se reserva para momentos de revelación o quiebre emocional, nunca por defecto.
  - *Elección de lente implícita*: gran angular para distorsión/intimidad claustrofóbica o para grandeza de escala; teleobjetivo para compresión/aislamiento emocional de un personaje respecto a su entorno.
  - *Luz*: calidad (dura/suave), dirección (contraluz, cenital, lateral), si es luz motivada por la escena (el resplandor de Miguel, el vacío de Onyx Gates) o ambiental.
  - *Regla de los 180°/eyeline match* en cualquier shot de diálogo con dos personajes, para que Storyboard Studio no invierta la posición de cámara entre shots consecutivos de la misma conversación.
  - *Encuadre simbólico*: centrado = poder/control; descentrado o regla de tercios = vulnerabilidad o desequilibrio — decisión consciente, no azar.
  - Una imagen ganada por shot (calibre B, `12_calibre_b.md`), presencia por efecto (`13_presencia_cinematografica.md`).

- **Diseño de producción** — grounding: breakdown + descripciones de localización existentes. Define por localización: paleta de color dominante, lenguaje arquitectónico/material (qué materiales definen Serephis frente a Onyx Gates), y relación de escala entre personaje y entorno — coherente en todos los shots de esa localización, no reinventada shot a shot.

- **Concept art** — grounding: breakdown + `character_library/` + variantes aprobadas. Confirma qué ya existe; para cualquier elemento visual nuevo del capítulo (localización, prop, criatura) sin ficha previa, propone silueta reconocible y su función icónica (qué lo hace identificable en un vistazo) para que el autor decida si genera el asset.

- **Composición/staging** — grounding: breakdown. Blocking dentro del cuadro: qué ocupa primer término/término medio/fondo, línea de fuerza que guía el ojo, uso del espacio negativo, y **continuidad del eje de acción** entre shots consecutivos de una misma escena (si un personaje mira a cuadro-derecha en un shot, mantiene esa dirección hasta que un shot de cambio de eje lo justifique). Esto es distinto de la decisión de lente/movimiento de Fotografía: aquí se decide qué hay dentro del cuadro, no cómo se filma.

- **Vestuario** — grounding: breakdown + `variantes_por_personaje/*.md`. Biblia de estado: progresión de daño como narrativa visual (la armadura no se agrieta porque sí — marca un antes/después), qué es práctico y qué es simbólico. Estado exacto de cada personaje en cada shot — nunca aparece intacto después de dañarse en un shot anterior.

- **VFX** — grounding: breakdown + `personajes.md` (poderes/rasgos). Consistencia física del efecto entre shots (si el ala de Miguel humea en el shot 12, no puede arder con llama abierta en el 13 sin un shot intermedio que lo explique), escala del efecto proporcional a la escena, y ajustado a lo que Veo3 genera de forma fiable (evitar descripciones que dependan de partículas finísimas o física imposible de mantener consistente entre shots).

**Sonido**

- **Sonido** — grounding: breakdown + localización. Distingue diegético (lo que los personajes oyen: viento, pasos, cristal, peso de la armadura) de no-diegético; construye capas de ambiente por localización, y decide dónde el silencio es la herramienta (un corte de ambiente sella una revelación mejor que un sonido añadido).

- **Música** — grounding: breakdown + facción/personaje en escena. Leitmotiv: una frase musical corta asociada a un personaje o facción que se repite reconocible a lo largo del capítulo (nunca música genérica de fondo); instrumentación que refleja el registro emocional de cada facción; marca explícitamente los shots donde la música debe estar AUSENTE, no solo dónde debe sonar — el silencio también es dirección musical.

- **Diálogo** — grounding: breakdown + líneas de diálogo del capítulo. Distingue lo que la línea dice de lo que en verdad transmite (subtexto); marca ritmo (pausas, solapamientos si dos personajes casi se interrumpen); anota énfasis por palabra para que el generador de voz no lea la línea plana.

**Actuación**

- **Casting y dirección de voz** — grounding: breakdown + `audiolibro_casting.json`. Confirma la voz ya asignada a cada personaje hablante del capítulo; para cada línea, nota de interpretación como la que un director de doblaje daría al actor: qué siente el personaje al decirlo, qué intenta ocultar o conseguir con esa línea (objetivo de la escena), y el tono físico (¿habla entre dientes, sin aliento, con calma forzada?).

**Continuidad**

- **Continuidad y canon** — grounding: breakdown + `grafo_conocimiento.md` + `personajes.md` + salida de Vestuario/VFX (para cruzar estado físico). Verifica que ningún shot muestre a un personaje sabiendo/haciendo algo que el grafo dice que aún no le corresponde, y que el estado físico declarado por Vestuario/VFX en cada shot es acumulativo y coherente (nunca retrocede sin motivo narrativo).

## Fase 3 — Coordinación: fusión + QA doble

El orquestador (no un agente) recibe todos los informes de Fase 2:
- Resuelve conflictos entre especialistas (p.ej. Fotografía pide un plano que Continuidad marca como imposible por el estado del personaje) — alguien decide, como el editor jefe en `11_sistema_agentes.md`.
- Fusiona todo en el JSON único (`storyboard_studio_exports/capNN_storyboard_studio_FECHA.json`).
- Regenera desde el JSON — nunca al revés — el markdown EN legible y el checklist de auditoría.
- QA doble (CLAUDE.md regla #8): verificación contra el texto real del capítulo + revisión independiente vía `codex exec --sandbox read-only`; QA transversal de densidad/repetición si el capítulo ya llevaba varias pasadas.
- Presenta el resultado al autor antes de cerrar la pasada. Nada de esto se da por aprobado solo — decisiones de estilo/trama/casting las decide él.

## Fase 4 — Post-producción (invocación posterior, cuando ya existan clips)

Esta fase NO corre junto con las anteriores — se dispara aparte, una vez el autor ya haya generado los clips de vídeo en Flow para el capítulo:

- **Montaje** — plan de corte/ritmo: orden y duración relativa de los clips, dónde cortar seco y dónde encadenar.
- **Color** — intención de gradación por escena, coherente con el estilo global "3D-Animation" ya usado en todos los personajes.

## Guardar y reportar

- JSON, markdown y checklist actualizados en `produccion_cinematografica/`.
- Informe de la pasada en `design_notes/AAAA-MM-DD_produccion_capNN.md`, listando qué propuso cada departamento, qué decidió el autor, y la duración final estimada (nº de shots × 8s) contra el presupuesto objetivo de la Fase 1.0.
- Commit con mensaje en español describiendo la decisión del autor que originó la pasada (CLAUDE.md regla #9).
- Resumen corto en chat — nunca pegar el JSON completo.

## Relación con otras skills

- Corre DESPUÉS de que `chapter-review` dé PASS a la prosa del capítulo.
- No sustituye a `chapter-review` ni a `beat-planner` — aquellas trabajan la prosa; esta traduce prosa ya cerrada a plano/vídeo, con el equipo de producción completo.

## Escalado a "serie"

Validado el capítulo 1 del Libro I con este proceso, el mismo skill se reinvoca capítulo a capítulo sin rediseñar nada: es la base para que la suma de los capítulos de un libro sea una temporada, y los tres libros, la serie completa. No adelantar a Libro II/III sin aprobación explícita del autor (regla #1).
