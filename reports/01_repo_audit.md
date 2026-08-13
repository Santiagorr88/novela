# Informe de auditoría técnica — repositorio "novelas"

Fecha: 2026-08-06
Alcance: estado del repositorio tras el movimiento a `/home/sszark/Escritorio/proyectos/novelas`, incluyendo el código comiteado y los directorios sin trackear (`content/`, `data/`, `prompts/`, `config/`, `project/`, `assets/`, `.claude/`, `generate_next_chapter.py`, `PROJECT_STRUCTURE.md`, `src/scripts/archive/`, `src/scripts/quality_guard.py`), que representan el estado de trabajo real más reciente.

## 1. Stack técnico

Python puro. `requirements.txt` incluye `langgraph`, `langchain` y una dependencia editable a `bytedance/deer-flow` — vestigios del scaffold original (el repo nació como fork de un framework de investigación web con agentes), **no usados** en el pipeline narrativo real. El motor de ejecución es un intérprete YAML casero (`src/flow_engine.py` + `src/scripts/run_flow.py`) que resuelve nodos `llm`/`python`/`router`/`file_loader`/`passthrough` con plantillas Jinja2. El único LLM invocado es **Google Gemini** (`gemini-2.5-pro` / `gemini-2.5-flash`) vía `src/utils/llm_wrappers.py`. No hay grafo de estados real (LangGraph no se usa pese a estar en dependencias).

## 2. Agentes (`src/agents/*.md`, `prompts/`)

18 prompts en markdown con duplicación confirmada por diff:
- **Activos** (referenciados por `config/flows/main.yml`): `narrator.md`, `chapter_planner.md`, `repetition_sentinel.md`, `rhythm_contrast.md`, `continuity_fixed.md`, `lore_fixer.md`, `event_extractor_chapter.md`, `recap_writer.md`, `translator.md`, `length_fixer.md`.
- **Duplicados/basura confirmados**: `chapter_planner_bien.md` (idéntico a `chapter_planner.md`), `narrator_duplicado.md` / `narrator_duplicate.md` (idénticos entre sí, versión recortada de `narrator.md`), `narrator_duplicate_bien.md` (reescritura completa distinta, más antigua), `chapter_planner_duplicate.md` (formato de salida distinto). Ya aislados en `prompts/archive/` en la reorganización nueva, pero siguen sueltos en `src/agents/`.
- `fixer.md` y `event_extractor.md` solo se usan en los flujos legacy (`flow_fixed.yml`/`flow_local.yml`), no en el de producción.

Invocación: pipeline lineal (no grafo), condicionales resueltas con `eval()` sobre el YAML — no explotable hoy, pero patrón de riesgo si alguna vez una condición incorporase texto generado por el LLM.

## 3. Sistema de memoria/contexto

**No existe recuperación semántica (embeddings/vectorial) en ningún punto.** Todo es concatenación de texto plano/JSON:
- `memory_plan.py::get_rolling_memory` trunca el historial **por número de caracteres desde el final** (`max_chars=12000`) cuando crece — pierde contexto temprano sin criterio semántico, pudiendo cortar a mitad de frase.
- `continuity.py::check` detecta personajes "muertos activos" con regex en **inglés únicamente**, trivialmente evadible.
- `lore_diff_tracker.py::check_lore_conflicts` compara líneas del capítulo contra el lore con similitud de cadenas (`difflib`, cutoff 0.7) — como la prosa narrativa rara vez calca literalmente el lore, tiende a generar falsos positivos masivos o a no dispararse nunca según el umbral real usado.
- `mystery_tracker.py` tiene una lista **hardcodeada de solo 6 misterios** y busca la palabra clave española "respuesta" dentro de texto que se genera **en inglés** — el chequeo de resolución nunca puede activarse.
- `mystery_tracker.py`, `timeline.py` (parcial) y `theme_manager.py` no están conectados al flujo de producción actual.
- El lore vive **duplicado** en `src/lore/` (tracked) y `content/lore/` (untracked, la copia "activa" según `PROJECT_STRUCTURE.md`) — contenido idéntico hoy, pero sin mecanismo que impida que diverjan.

## 4. Flujo de generación — roto en el punto de entrada "de producción"

- `generate_next_chapter.py` espera `ok, ctx = run_flow(...)`, pero `run_flow()` (`src/scripts/run_flow.py`) **no tiene ningún `return`** → `TypeError` garantizado en cualquier ejecución real.
- `config/flows/main.yml` invoca `memory_plan.get_recent_chapters_text`, función que **no existe** en `memory_plan.py` (confirmado por grep) → `AttributeError` en el segundo nodo si se arreglara el punto anterior.
- `launch_flow.py` (el otro entrypoint) sigue apuntando a rutas legacy (`flow.yml`, `src/lore/prompt_universo.md`), no a la estructura nueva (`config/flows/main.yml`, `content/lore/`) — nunca se actualizó tras la reorganización.
- Credenciales inconsistentes: `call_gemini.py` lee `GOOGLE_API_KEY` de `.env`; `llm_wrappers.py` (el que usa el flujo real) lee `src/secrets.json`, **archivo que ya no existe** → `FileNotFoundError` al importar. El `.env` real usa la variable `API_KEY_GEMINI`, que no coincide con ninguna de las dos convenciones del código.
- Sin límite de tokens/coste acumulado ni contador de gasto.

**Conclusión**: el pipeline "de producción" actual no es ejecutable tal cual está. Nunca se probó de punta a punta tras el último refactor de carpetas.

## 5. Almacenamiento

100% archivos planos (JSON/YAML/Markdown), sin base de datos. Estado canónico **duplicado y contradictorio**: `output/state.json` (tracked, capítulo 3) vs `data/state/state.json` (untracked, capítulo 1) contienen datos distintos sobre el mismo objeto narrativo (arma "Solmire": propietario y estado difieren entre ambas copias). Mismo problema con `position.json`. Cualquier agente que lea "el estado" puede recibir hechos opuestos según qué copia esté activa.

## 6. Pruebas y automatización

Confirmado: no existe `tests/` ni `.github/workflows/`. Única verificación: `validate_yaml.py` (solo sintaxis YAML de `flow.yml`, hardcodeado al legacy, no valida `config/flows/main.yml`) y `src/scripts/quality_guard.py` (conteo de palabras/párrafos, sin verificación semántica).

## 7. Duplicación / código abandonado

`flow.yml` / `flow_fixed.yml` / `flow_local.yml` (raíz) son casi idénticos a `config/flows/main.yml` y sus archivos en `config/flows/archive/`, difiriendo solo en rutas legacy vs nuevas. `src/scripts/archive/` contiene versiones anteriores de `chapter_splitter.py` y `slugify.py` con rutas viejas. `README_es.md` es **el README genérico sin editar del template original** (bytedance/deer-flow — badges, LangGraph Studio, Tavily/Brave Search, TTS — nada relativo a novelas). `README_Saga_Functions.md` documenta una API (`beat_planner.py`, `prophecy_manager.py`, `saga_state.py`) que **no existe en el código actual**.

## 8. Seguridad

- **Resuelto en esta sesión**: API key de Google expuesta en el historial de git (commit con `src/secrets.json`) — purgada del historial local con `git-filter-repo`, pendiente de que el usuario haga `force-push` y rote la clave en Google Cloud Console.
- No se encontraron más claves hardcodeadas en el código fuente actual (`src/`, `config/`, `content/`, `prompts/`, `project/`).
- `flow_engine.py::run_node` y `run_flow.py::should_run` usan `eval()` sobre condiciones del YAML — no explotable hoy (el YAML es de confianza), pero es un patrón a evitar si alguna vez el contenido generado por el LLM alimentara esas expresiones.

## 9. Documentación vs. implementación

La documentación describe una reorganización de carpetas (`content/`, `data/`, `prompts/`) que **nunca se completó a nivel de código**: varios scripts activos (`memory_plan.py`, `chapter_recap_writer.py`, `lore_diff_tracker.py`, `character_tracker.py`, `continuity.py`, `mystery_tracker.py`, `theme_manager.py`) siguen hardcodeando rutas antiguas (`src/chapters/`, `src/lore/prompt_universo.md`, `output/state.json`).

## 10. Causas probables de la incoherencia narrativa reportada

1. **Estado canónico duplicado y contradictorio** (`output/` vs `data/state/`) — fuente de verdad ambigua.
2. **Memoria por truncado de caracteres, no por relevancia semántica** — pérdida de contexto temprano sin aviso, sin forma de recuperar un detalle específico de capítulos anteriores.
3. **Validadores de continuidad triviales y en gran parte inoperantes** (regex en inglés, similitud de cadenas, palabra clave en español buscada en texto inglés) — no detectan contradicciones reales; el pipeline de producción además está roto (funciones inexistentes, imports que fallan), lo que sugiere que nunca llegó a ejecutarse completo tras el último refactor.
4. **Prompts duplicados y contradictorios** — coexisten ≥3 versiones del narrador y 2 del planificador con reglas de estilo distintas; si se invocó la versión equivocada en algún momento, explica cambios de tono/personalidad entre capítulos.
5. **Sin control de versiones del canon** — el lore vive en copias idénticas hoy pero sin mecanismo que impida divergencia futura; `mystery_tracker.py` es una lista fija sin extensión, no un canon vivo y auditable.
6. **Ausencia total de tests/CI** — ningún cambio en prompts, flujos o trackers se valida antes de ejecutarse contra el LLM real; las regresiones (como las aquí detectadas) solo se detectan al fallar en producción o al leer manualmente el capítulo.

## Componentes reutilizables

- El patrón general del pipeline YAML + Jinja2 + nodos tipados es una base razonable, pero necesita un motor más robusto (estado tipado, validación de esquema, checkpoints).
- Los prompts "activos" identificados en el punto 2 (una vez elegida una única versión por rol) son un punto de partida válido para los nuevos agentes narrativos.
- La idea de trackers especializados (continuity, lore diff, mystery, timeline) es correcta conceptualmente; la implementación debe rehacerse con comprensión semántica real (LLM-as-judge o embeddings), no regex/difflib.

## Componentes a descartar

- Dependencias LangGraph/LangChain/deer-flow no usadas.
- Los ≥6 prompts duplicados/abandonados en `src/agents/`.
- `flow.yml`/`flow_fixed.yml`/`flow_local.yml` en la raíz (superados por `config/flows/`).
- `README_es.md` (plantilla genérica sin relación con el proyecto).
- El doble almacenamiento de estado (`output/` vs `data/state/`) — unificar en una sola fuente de verdad.
- `mystery_tracker.py`, `continuity.py`, `lore_diff_tracker.py`, `timeline.py` en su forma actual (rehacer, no adaptar).

## Deuda técnica y riesgos principales

- Pipeline de producción no ejecutable (funciones inexistentes, credenciales inconsistentes).
- Sin tests ni CI — cualquier cambio es un salto al vacío.
- Sin control de coste/presupuesto de tokens.
- Documentación desalineada con el código (README genérico, API documentada que no existe).
- Riesgo de seguridad de patrón `eval()` sobre condiciones (bajo, pero a eliminar en el rediseño).
