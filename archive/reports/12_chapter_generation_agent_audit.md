# Auditoría quirúrgica: agentes necesarios para "generar un capítulo"

Fecha: 2026-08-08
Alcance: **pipeline de generación de texto** de un capítulo, desde "aquí está el plan de beats" hasta "capítulo aprobado y su estado canónico actualizado". No cubre el pipeline audiovisual (Fase 8, `reports/07_audiovisual_pipeline.md`) — eso es una fase posterior y separada.
Rutas: ancladas a la estructura **real actual** del repo (`content/lore/`, `project/Chronicles_of_the_Sundering_Judgment/`), no a la estructura `novels/<id>/` de la Fase 3, que todavía no se ha materializado (`novels/` existe pero está vacía). Al final hay una nota de mapeo para cuando se migre.

## Principio rector (de dónde sale esto)

No parto del roster completo de 13 agentes de la Fase 7 y lo doy por bueno. Parto de lo que el Council nos obligó a hacer y de lo que ya construimos y probamos de verdad esta sesión (el skill `chapter-review`, ejecutado contra B1C01 con resultados reales). Cada pieza de abajo lleva un estado: **CONSTRUIDO** (ya existe y se probó), **NECESARIO AHORA** (falta, pero no se puede generar un capítulo sin él), o **DIFERIR** (existe en el diseño de Fase 7 pero no hay evidencia todavía de que haga falta — no se construye hasta que un caso real lo demuestre necesario, tal como pedía el veredicto del Council).

## Secuencia completa, paso a paso

### Paso 0 — Resolución del plan de capítulo
**Tipo**: código determinista, NO es un agente.
**Estado**: NECESARIO AHORA (no existe todavía como función aislada, pero es trivial).
**Entrada**: identificador de capítulo (p. ej. `B1C01`).
**Fuente de datos**: `content/lore/archive/arco_argumental_Duplicado.md` — ya designado como fuente operativa única de beats (ver `content/lore/personajes.md` y el resto de esta sesión). `content/lore/arco_argumental_completo.md` queda solo como índice de referencia, no se lee en este paso.
**Salida**: estructura en memoria con los N "Narrative Parts" del capítulo, su función narrativa, y el objetivo de palabras (2.600-3.600, acordado esta sesión).
**Código reutilizable**: `src/scripts/lore_utils.py::get_part_titles_for_chapter` / `get_chapter_title` — están bien escritos (ver auditoría de scripts) pero apuntan a `arco_argumental_completo.md`, no a `Duplicado.md`. Hay que adaptarles la fuente y el parser (`Duplicado.md` tiene una estructura de "Narrative Parts" numeradas dentro de cada capítulo, distinta a la de beats sueltos de `completo.md`).

### Paso 1 — Recuperación de contexto
**Tipo**: código determinista con filtros, NO es un agente (según diseño ya acordado en Fase 6, B.2).
**Estado**: NECESARIO AHORA, no existe.
**Entrada**: personajes/localizaciones que aparecen en el plan del Paso 0, número de capítulo.
**Fuentes**: `content/lore/prompt_universo.md` (solo las fichas de los personajes en escena — usar grep por nombre, no cargar el archivo entero de 2.900 líneas), estado narrativo actual (ver nota de estado más abajo — **hoy no existe `state/current.json`**, solo `output/state.json` y `data/state/state.json`, duplicados y desincronizados, sin reconciliar todavía por decisión tuya), y el recap del capítulo anterior si existe.
**Salida**: paquete de contexto acotado + un log de qué se recuperó y por qué (`retrieval_log`, ya diseñado en Fase 6).
**Bloqueante real no resuelto**: no se puede filtrar por "estado actual del personaje" de forma fiable hasta reconciliar `output/state.json` vs `data/state/state.json`. Este es el primer punto donde la limpieza pendiente (que decidiste posponer) se convierte en un bloqueante funcional, no solo estético.

### Paso 2 — Planificador narrativo
**Tipo**: agente (Claude subagent).
**Estado**: **DIFERIR**. El diseño de Fase 7 lo incluye (agente #3), pero la revisión que ya hicimos de B1C01 usó el plan de `Duplicado.md` directamente, sin una capa de planificación adicional, y el "Revisor de Ritmo y Estructura" del skill `chapter-review` verificó cobertura de beats perfectamente bien contra ese plan crudo. No hay evidencia todavía de que un capítulo generado directamente desde `Duplicado.md` necesite un agente intermedio que lo replanifique. Se construye solo si, al escribir varios capítulos reales, se observa que el plan crudo no basta (p. ej. si hace falta decidir dinámicamente qué promesas narrativas de `plots/promises.yaml` tocar — pero ese archivo tampoco existe todavía).

### Paso 3 — Escritor de escenas
**Tipo**: agente (Claude subagent). **El único verdaderamente imprescindible de todo el pipeline.**
**Estado**: NECESARIO AHORA. Hoy este paso lo hago yo manualmente en el chat (así se escribió B1C01_EN_v2.md) — no existe como agente invocable de forma repetible.
**Entrada**: plan del Paso 0, contexto del Paso 1, y **solo la sección de estilo** de `prompt_universo.md` (Global Generation Directive + House Style + Language & Diction + Dialogue & Subtext + Scene & Beat Mechanics + Influence — no el documento completo, mismo principio de acotar grounding que ya aplicamos en el diseño del skill de revisión).
**Salida**: `project/Chronicles_of_the_Sundering_Judgment/chapters/EN/<id>_v1.md`.
**Nota de coste**: es el paso más caro (genera 2.600-3.600 palabras con contexto amplio). Candidato a modelo de mayor capacidad; no lo abarates a costa de calidad, es el corazón del producto.

### Paso 4 — Editor (estilo y diálogo)
**Tipo**: agente (Claude subagent).
**Estado**: NECESARIO AHORA, aunque puede fusionarse operativamente con el Paso 3 en una primera iteración (una sola llamada que escribe y se autopule) — **diferir la separación en dos llamadas hasta ver si el Escritor solo no alcanza el nivel de pulido**. Cuando hicimos la revisión de B1C01, el "Revisor de Voz y Estilo" encontró fallos reales (imagen de ozono repetida 3 veces) que un Escritor+Editor separados probablemente habrían evitado — así que hay evidencia a favor de separar esto, a diferencia del Paso 2.
**Entrada/Salida**: mismo patrón que el Escritor, opera sobre el draft.

### Paso 5 — Revisión (continuidad + estilo + ritmo + diálogo + lectura independiente)
**Tipo**: **Skill**, no agentes sueltos.
**Estado**: **CONSTRUIDO Y PROBADO** — `.claude/skills/chapter-review/SKILL.md`, ejecutado contra B1C01_EN_v2.md con resultado real (PASS WITH FIXES, 3 fixes bloqueantes encontrados por convergencia de hasta 3 revisores independientes). Esto **sustituye directamente** a los agentes #6 (Revisor narrativo) y #7 (Revisor de continuidad) del diseño original de Fase 7 — no hace falta construirlos aparte, ya están implementados como los 5 reviewers de este skill.
**Coste**: los 4 reviewers Claude + 1 llamada a Codex, en paralelo. Ya se demostró que el coste es razonable para ejecutarse en cada capítulo (ver "Cost discipline" en el propio SKILL.md).
**Pendiente real**: automatizar el paso 6 del propio SKILL.md (aplicar los fixes bloqueantes), hoy se hace a mano tras leer el veredicto.

### Paso 6 — Aplicación de fixes
**Tipo**: agente (reutiliza el Editor del Paso 4, con el informe de revisión como instrucción adicional) o intervención humana directa.
**Estado**: **DIFERIR la automatización completa**. Hoy funciona bien como bucle humano-en-el-medio (yo aplico los fixes que el informe pide, como con B1C01). Automatizar "aplica estos fixes sin supervisión" antes de tener 3-4 ciclos reales de este bucle sería repetir el error de over-engineering que señaló el Council.

### Paso 7 — Aprobación humana
**Tipo**: humano. No es un agente y nunca debe serlo (ya establecido en Fase 7: "responsable del canon" es un gate, no un creador; la aprobación siempre es humana).
**Estado**: ya funciona (es exactamente lo que hemos hecho tú y yo con cada pregunta de confirmación esta sesión).

### Paso 8 — Actualización de estado y propuesta de canon
**Tipo**: código determinista (diff de estado) + agente "Responsable del canon" solo si hay cambios de canon reales (personaje nuevo, localización nueva, regla de mundo nueva).
**Estado**: **DIFERIR el agente**, **NECESARIO AHORA el diff determinista básico** (actualizar `state.json` con lo que cambió: quién apareció, qué localizaciones se visitaron, qué objetos cambiaron de estado). El código legacy más cercano a esto es `src/scripts/timeline.py` y `character_tracker.py` — tienen el modelo de datos correcto (ver auditoría de scripts) pero hoy nadie los alimenta con eventos reales; alimentarlos desde el capítulo recién aprobado es el trabajo real pendiente, no reescribir el modelo de datos desde cero.

## Resumen: qué construir ya vs. qué esperar

| Pieza | Tipo | Estado | Por qué |
|---|---|---|---|
| Carga de plan de capítulo | Código | Necesario ahora | Trivial, adaptar `lore_utils.py` |
| Recuperación de contexto filtrada | Código | Necesario ahora | Bloqueado por reconciliar `state.json` duplicado |
| Planificador narrativo | Agente | **Diferir** | Sin evidencia de que el plan crudo no baste |
| Escritor de escenas | Agente | Necesario ahora | Único paso verdaderamente imprescindible |
| Editor de estilo/diálogo | Agente | Necesario ahora | Evidencia real de B1C01: separarlo detecta más fallos |
| Revisor narrativo + continuidad | **Skill** | **Ya construido y probado** | `chapter-review`, corrido contra B1C01 |
| Aplicación de fixes | Agente/humano | Diferir automatización | Mantener humano-en-el-medio hasta 3-4 ciclos reales |
| Aprobación | Humano | Ya funciona | Nunca debe automatizarse |
| Diff de estado | Código | Necesario ahora | Modelo de datos ya existe en `timeline.py`/`character_tracker.py`, solo falta alimentarlo |
| Responsable del canon | Agente | Diferir | Solo hace falta cuando de verdad haya una propuesta de canon que gatee |
| Director creativo, Arquitecto de mundo | Agente | Fuera de alcance | Solo se usan en `create-novel`, no en generación de capítulo |

## Skills vs. Agentes — el criterio que se confirma con esta auditoría

Un **Skill** tiene sentido cuando el paso es: (a) invocable de forma independiente por ti directamente ("revisa este capítulo"), (b) compuesto de varias llamadas con un protocolo fijo (paralelo → cruce → síntesis), y (c) reutilizable sin cambios entre capítulos. Eso es exactamente `chapter-review`.
Un **Agente suelto** (parte de una orquestación, no invocable solo) tiene sentido cuando el paso es una única transformación con un rol claro (escribir, editar) que no necesita protocolo propio.
**Código sin LLM** tiene sentido siempre que la tarea sea determinista — contar palabras, cargar un plan, diffear estado — y esta auditoría confirma que varios pasos que "suenan" a agente (recuperación de contexto, diff de estado) en realidad no necesitan uno.

## Nota de migración a `novels/<id>/`

Cuando se materialice la estructura de la Fase 3, los mapeos de ruta son: `content/lore/prompt_universo.md` → `novels/<id>/canon/approved/` (fragmentado por entidad), `content/lore/archive/arco_argumental_Duplicado.md` → `novels/<id>/plots/`, `project/.../chapters/` → `novels/<id>/chapters/`, `output/state.json`+`data/state/state.json` (reconciliados) → `novels/<id>/state/current.json`. Esta auditoría sigue siendo válida sobre esa estructura nueva, solo cambian las rutas, no la secuencia de pasos.
