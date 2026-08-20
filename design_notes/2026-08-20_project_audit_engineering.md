# Auditoría de ingeniería: pipeline Python vs. proceso de skills

**Fecha**: 2026-08-20
**Alcance**: rama `main`, solo lectura. Cubre `src/`, `config/flows/`, `prompts/`, `manual_register.py`, `requirements.txt`, `.env`, `.venv/`, `README_Saga_Functions.md`, `PROJECT_STRUCTURE.md`, y su relación con `project/Chronicles_of_the_Sundering_Judgment/chapters/EN/` y `.claude/skills/{beat-planner,chapter-review}`.
**Metodología**: lectura de docstrings/cabeceras, `git log -1 --format="%ai %an" -- <archivo>` por archivo, grep de referencias cruzadas, inspección de `.gitignore` y del mensaje del commit de reorganización (`60e58f7`, 2026-08-13). No se ejecutó ningún script.

---

## Hallazgo de contexto (léase primero)

El propio repositorio ya contiene un veredicto explícito del autor. El commit `60e58f7` ("Reorganize project structure and add complete Books II-III prose", 2026-08-13, mismo commit que introduce `.claude/skills/beat-planner/SKILL.md` y `.claude/skills/chapter-review/SKILL.md`) dice en su mensaje:

> "Excludes leftover cache/state/logs from the **abandoned automated generation pipeline** and machine-local Claude Code settings via .gitignore, without touching them on disk."

Y `.gitignore` (añadido en el mismo commit) contiene:

```
# Legacy automated-pipeline cache/state/logs (superseded by the current manual + Codex-review workflow)
data/
artifacts/logs/
src/chapters/
```

Todo lo que sigue es la verificación técnica de esa afirmación, componente por componente — y confirma que no es solo una etiqueta en un mensaje de commit: el pipeline está objetivamente roto en su estado actual (imports que fallan, rutas que ya no existen), no solo "sin usar".

---

## 1. Documentación

### `README_Saga_Functions.md`
- **Estado**: LEGACY / desactualizado.
- **Evidencia**: último cambio 2025-07-24 (el commit más antiguo de todo el árbol auditado salvo `src/__init__.py`). Documenta `beat_planner.py`, `theme_manager.py`, `mystery_tracker.py`, `prophecy_manager.py`, `saga_state.py` y `prompt_universo.md` como "scripts que orquestan la generación narrativa" — **ninguno de esos cinco `.py` existe** en `src/scripts/` ni en ningún otro sitio del repo (verificado con `find`). Describe un diseño que o nunca se terminó de implementar o fue borrado antes de julio 2025, y nadie lo actualizó desde entonces pese a la reorganización de agosto 2026.
- **Recomendación**: archivar o borrar. Si se conserva, marcarlo explícitamente como histórico/aspiracional — en su estado actual induce a error a cualquiera que lo use como mapa del sistema real.

### `PROJECT_STRUCTURE.md`
- **Estado**: INDETERMINADO, con fuerte sesgo a "aspiracional, no descriptivo".
- **Evidencia**: escrito de cero en el mismo commit de reorganización (2026-08-13), por lo que en teoría debería reflejar el estado post-reorg. Pero documenta tres entrypoints — `launch_flow.py`, `generate_next_chapter.py`, `validate_yaml.py` — que **no existen en `main`**. `launch_flow.py` y `validate_yaml.py` existieron brevemente en un commit "my book" anterior (2025-10-16) y fueron eliminados; `generate_next_chapter.py` no aparece nunca en el historial de ninguna rama. También documenta `data/state/`, `data/cache/`, `data/chapters/` — directorios que no existen en disco y que el propio `.gitignore` etiqueta como "legacy automated-pipeline". Es decir: el documento describe una estructura de entrypoints planeada que nunca llegó a materializarse en `main` (podría existir parcialmente en la rama `v2-rebuild`, no explorada a fondo por estar fuera del alcance de esta auditoría de `main`).
- **Recomendación**: corregir o marcar como plan/diseño, no como inventario real. Si se mantiene, quitar las referencias a los tres entrypoints inexistentes.

---

## 2. Motor y utilidades (`src/`)

### `src/flow_engine.py`
- **Estado**: LEGACY, actualmente roto.
- **Evidencia**: último cambio 2025-07-24. Importa `from src.utils.llm_wrappers import run_llm_gemini` a nivel de módulo. `llm_wrappers.py` lee `src/secrets.json` en tiempo de import (`secrets_path.read_text()`), y **ese archivo no existe en el repo**. Resultado: cualquier intento de importar `flow_engine.py` hoy lanza `FileNotFoundError` antes de llegar a ejecutar nada.
- **Recomendación**: archivar. No es ejecutable en el estado actual del repo sin reconstruir `src/secrets.json` primero.

### `src/utils/llm_wrappers.py`
- **Estado**: LEGACY, roto (ver arriba). Además, la fuente de credenciales que espera (`src/secrets.json`) es distinta de la que expone `.env` (`API_KEY_GEMINI`) — hay dos mecanismos de configuración de API key inconsistentes entre sí, y ninguno de los dos está conectado al workflow actual.
- **Recomendación**: archivar.

### `src/agents/agents.py` (+ `src/__init__.py`, `src/agents/__init__.py`)
- **Estado**: LEGACY, código muerto sin ninguna conexión al proyecto.
- **Evidencia**: cabecera `# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates` — es boilerplate sin adaptar del framework upstream `bytedance/deer-flow` (declarado como dependencia `-e git+...` en `requirements.txt`, y de donde probablemente se partió para construir este pipeline). Importa `src.prompts`, `src.llms`, `src.config` — **ninguno de esos tres paquetes existe** en este repo. Nada fuera de `src/agents/__init__.py` lo referencia. `src/__init__.py` (autor "He Tao", 2025-04-17) es la fecha más antigua de todo el árbol — también boilerplate del template original, jamás tocado desde entonces.
- **Recomendación**: candidato claro a borrar. Es código huérfano de un scaffold externo que nunca se integró.

---

## 3. `src/scripts/` — uno por uno

Todos comparados contra `git log --oneline -20` del proyecto: la sesión de escritura activa (capítulos de Book II/III, auditorías POV, verificaciones de personajes) cubre commits del **18-20 de agosto de 2026**, todos posteriores en semanas/meses a la última vez que se tocó cualquiera de estos scripts salvo por el movimiento mecánico del reorg del 13 de agosto.

| Script | Último cambio | Estado | Evidencia clave |
|---|---|---|---|
| `chapter_assembler.py` | 2025-10-16 | LEGACY | Único consumidor: `main.yml`. Los capítulos EN actuales no llevan ninguna huella de su formato (`assemble_full_chapter_h1_h3`); usan H1+H2 simple sin metadata. |
| `chapter_recap_writer.py` | 2025-08-14 | LEGACY, roto | Hardcodea `src/chapters/recap/` — exactamente el directorio que `.gitignore` etiqueta como "old ad-hoc src/ layout" y que ya no se usa. |
| `character_tracker.py` | 2025-07-24 | LEGACY, roto | Hardcodea `output/state.json`; `output/` no existe en el repo. |
| `continuity.py` | 2025-07-24 | LEGACY | Acepta `state_path` como parámetro (así lo llama `main.yml`, con `data/state/state.json`), pero `data/` está en `.gitignore` como legacy y no existe en disco. |
| `export_pdf.py` | 2025-07-24 | LEGACY / posible utilidad standalone | Conversor md→PDF genérico vía `weasyprint`, documentado también como comando manual en `README_Saga_Functions.md`. No hay PDFs generados en `project/`. Podría seguir siendo útil de forma aislada (bajo riesgo, sin dependencias rotas propias) si alguien quisiera exportar un capítulo aprobado, pero no forma parte de ningún flujo activo. |
| `lore_utils.py` | 2025-09-05 | LEGACY | Único consumidor: `main.yml`. |
| `lore_diff_tracker.py` | 2025-07-24 | LEGACY, roto | `LORE_PATH = Path("src/lore/prompt_universo.md")` — ruta pre-reorg; el archivo real está en `content/lore/prompt_universo.md` desde el 13-08-2026. El nodo `lore_checker` en `main.yml` invoca `check_lore_conflicts` **sin pasar `lore_path`**, así que usaría el default roto si se ejecutara hoy. |
| `memory_plan.py` | 2025-09-05 | LEGACY, roto | `RECAP_DIR = Path("src/chapters/recap")` — mismo problema de ruta pre-reorg que `chapter_recap_writer.py`. |
| `path_utils.py` | 2026-08-13 (reorg) | LEGACY | Tocado solo por el movimiento mecánico del reorg, no por desarrollo activo. Único consumidor: `main.yml`. |
| `postedit.py` | 2025-10-16 | LEGACY | Único consumidor: `main.yml` (repetition sentinel / rhythm coach). |
| `progress_tracker.py` | 2025-09-05 | LEGACY | Depende de `data/` (gitignored/legacy). |
| `quality_guard.py` | 2026-08-13 (reorg) | LEGACY | Igual que `path_utils.py`: tocado solo por el reorg mecánico. |
| `run_flow.py` | 2025-07-24 | LEGACY, roto | Importa `src.flow_engine`, que a su vez falla al importar por el `secrets.json` faltante. No ejecutable hoy. |
| `timeline.py` | 2025-07-24 | LEGACY, roto | Hardcodea `output/state.json`. |
| `title_utils.py` | 2025-07-24 | LEGACY | Utilidad pequeña (`slugify`, `extract_title_line`), usada solo por `path_utils.py`/`main.yml`. |
| `io_utils.py` | 2025-09-05 | LEGACY | `save_text_to_file` usado por `main.yml` para persistir capítulos EN/ES; incluye una función `multiply_ints` sin relación aparente con el resto del módulo (posible resto de pruebas). |

### `src/scripts/archive/` (ya marcado como archivo explícitamente)
- `slugify.py` (2026-08-13) y `chapter_splitter.py` (2026-08-13): **confirmado por grep** que nada fuera de esta carpeta los referencia. `chapter_splitter.py` es literalmente un stub ("Simula división y guardado de partes de un capítulo"). `slugify.py` duplica funcionalidad de `title_utils.slugify`.
- **Recomendación**: correctamente archivados; candidatos a borrar sin riesgo si se quiere reducir superficie.

---

## 4. `manual_register.py` (raíz)

- **Estado**: LEGACY, roto de forma garantizada.
- **Evidencia**: importa `src.scripts.theme_manager`, `src.scripts.memory_io`, `src.scripts.mystery_tracker` — **los tres módulos no existen** en el repo (confirmado con `find`). Cualquier invocación falla con `ImportError` en la línea 5-9, antes de llegar al `if __name__ == "__main__"`. Último cambio: 2025-07-24, trece meses antes de la sesión de escritura actual. El propio `README_Saga_Functions.md` lo documenta como el comando para "lanzar manualmente los capítulos y registrarlos", pero ese flujo manual descrito ya no es el que se usa — el registro/aprobación actual pasa por la skill `chapter-review`, no por este script.
- **Recomendación**: borrar o archivar. No es recuperable sin reconstruir tres módulos que nunca se llegaron a implementar (a diferencia de las rutas rotas de otros scripts, aquí ni siquiera existió el módulo destino).

---

## 5. `config/flows/`

### `config/flows/main.yml`
- **Estado**: LEGACY EN USO REAL, aunque es el artefacto mejor construido de todo el pipeline.
- **Evidencia**: es una orquestación coherente y completa — progreso → carga de lore → planner LLM → narrator LLM → post-edición (repetition sentinel, rhythm coach) → ensamblado markdown → gates de continuidad/lore/calidad con LLM-fixers condicionales → extracción de eventos → recap → título/filename → export PDF EN → traducción ES → export PDF ES → persistencia de texto y memoria/progreso. Referencia prácticamente todos los scripts de `src/scripts/` listados arriba y 10 de los 11 prompts activos.
- Pero: (a) depende de al menos dos rutas rotas (`lore_diff_tracker.py` default, `chapter_recap_writer.py`/`memory_plan.py` hardcodes) que no se actualizaron en el reorg de rutas del 13-08-2026 aunque el propio `main.yml` sí fue tocado ese día; (b) su dependencia transitiva (`flow_engine.py` vía `run_flow.py`) no es importable hoy por el `secrets.json` faltante; (c) el último cambio real es exactamente el commit que el autor describe como archivado del pipeline "abandonado" — es decir, se tocó por el movimiento mecánico de `flow.yml` → `config/flows/main.yml`, no por desarrollo activo; (d) ningún capítulo EN escrito desde 2025-10-16 (fecha del último toque real a `chapter_assembler.py`/`postedit.py`) muestra evidencia de haber pasado por este flujo — ver sección 6.
- **Recomendación**: mover a `config/flows/archive/` junto con `local.yml` y `fixed.yml`, salvo que el usuario tenga intención concreta de retomar la generación automática (en cuyo caso habría que arreglar primero las rutas rotas y `secrets.json` antes de poder ejecutarlo).

### `config/flows/archive/local.yml`, `config/flows/archive/fixed.yml`
- **Estado**: LEGACY, correctamente archivados.
- **Evidencia**: sin referencias fuera de su propia carpeta (confirmado por grep).
- **Recomendación**: mantener como están o borrar; no hay ambigüedad sobre su estado.

---

## 6. `prompts/`

De los 11 prompts en `prompts/` (fuera de `archive/`), **9 están referenciados exclusivamente por `main.yml`**: `chapter_planner.md`, `narrator.md`, `repetition_sentinel.md`, `rhythm_contrast.md`, `continuity_fixed.md`, `lore_fixer.md`, `length_fixer.md`, `event_extractor_chapter.md`, `recap_writer.md`, `translator.md` (son 10, no 9 — corrección: los diez prompts arriba están todos referenciados en `main.yml`, confirmado por grep de `system_prompt_path`). Como `main.yml` es legacy (sección 5), estos 10 prompts son legacy por asociación aunque técnicamente "referenciados desde un sitio" — ese sitio no se ejecuta.

Dos casos adicionales, más graves porque están **huérfanos incluso dentro de su propio directorio activo**:
- `prompts/fixer.md`: no referenciado por `main.yml` ni por ningún script (grep negativo). No está en `archive/` pese a no tener consumidor.
- `prompts/event_extractor.md`: superado por `event_extractor_chapter.md` (el propio `main.yml` lo anota: `# <- renombrado`). Tampoco está en `archive/`.

`prompts/archive/*.md` (5 archivos: `chapter_planner_duplicate.md`, `narrator_duplicado.md`, `chapter_planner_bien.md`, `narrator_duplicate_bien.md`, `narrator_duplicate.md`): correctamente archivados, sin referencias externas confirmadas por grep.

- **Recomendación**: mover `fixer.md` y `event_extractor.md` a `prompts/archive/` para que la carpeta `prompts/` refleje honestamente solo lo consumido por un flujo (aunque ese flujo mismo se recomiende archivar — ver sección 5). El resto, tratar igual que `main.yml`.

---

## 7. `content/lore/archive/` — contraejemplo importante

A diferencia de `prompts/archive/` y `config/flows/archive/`, **`content/lore/archive/` NO está muerto**. Grep confirma que `archive/arco_argumental_Duplicado.md` (y sus partes 1-3) se cita activamente y con frecuencia en los documentos de planificación vigentes: `content/lore/expansion_guidelines.md`, `content/lore/book1_part1_expanded_beats.md`, `content/lore/book2_part3_expanded_beats.md`, y explícitamente en `.claude/skills/chapter-review/SKILL.md` como fuente primaria de beats ("use `Duplicado.md`'s richer per-beat summaries as primary source"). Es una carpeta de "material de referencia histórico pero todavía consultado", no un archivo muerto — no debe tratarse igual que los otros dos `archive/` del repo.

---

## 8. `requirements.txt`, `.env`, `.venv/`

- **`requirements.txt`**: INDETERMINADO con sesgo a legacy. Sin cambios desde 2025-07-24. Incluye `-e git+https://github.com/bytedance/deer-flow.git@...#egg=deer_flow` — confirma que el pipeline se construyó sobre (o copiando de) el framework `deer-flow` de ByteDance, lo cual explica el código huérfano de `src/agents/agents.py`. El resto de dependencias (`langchain`, `langgraph`, `google-generativeai`, `weasyprint`, etc.) corresponden 1:1 con lo que usa el pipeline Python, no con nada del workflow de skills.
- **`.venv/`**: existe, con 314 paquetes instalados (creado 2025-07-24, confirmando que el pipeline llegó a tener un entorno real y funcional en algún momento, no solo teórico). No se instaló nada nuevo aparentemente desde entonces.
- **`.env`**: contiene una sola variable, `API_KEY_GEMINI`. **Grep confirma que ningún archivo `.py` del repo (fuera de `.venv/`) llama a `load_dotenv`, `os.environ` u `os.getenv`** — es decir, `.env` no está conectado a nada, ni siquiera al pipeline roto (que además espera credenciales en `src/secrets.json`, no en variables de entorno). Doble vestigio: ni el mecanismo de configuración coincide entre los propios archivos del pipeline, ni nada lo lee hoy.
- **Recomendación**: si se decide archivar el pipeline, `requirements.txt` y `.venv/` pueden documentarse como "entorno del pipeline legacy, no requerido para el workflow de skills" y eventualmente eliminarse para liberar espacio; `.env` puede borrarse sin impacto verificable.

---

## 9. ¿Algún capítulo de prosa reciente pasó por el pipeline?

No se encontró evidencia de ello, y sí evidencia positiva de lo contrario:

- **Traducción ES abandonada desde antes del reorg**: `project/.../chapters/ES/` solo contiene 2 archivos (`B1C01_ES_v2.md`, `B1L01_ES.md`), ambos con último cambio real en 2025-10-16 ("my book") — nunca tocados desde entonces pese a que `chapters/EN/` ha crecido a 158 archivos con 68+ commits solo en los últimos días. Si el pipeline (que genera EN **y** ES en el mismo flujo, ver `main.yml` líneas 379-420) siguiera activo, cabría esperar ES creciendo en paralelo a EN. No lo hace.
- **Sin PDFs**: no se encontró ningún `.pdf` bajo `project/`, pese a que `main.yml` exporta PDF de cada capítulo EN y ES.
- **Sin huella de `chapter_assembler.py`**: los capítulos actuales son Markdown simple (H1 título + H2 secciones separadas por `---`), sin la estructura H1/H3 que sugiere el nombre de `assemble_full_chapter_h1_h3`, ni metadata/frontmatter alguno.
- **`project/.../chapters/EN/reports/`** contiene archivos `*_review.md` (p. ej. `B2C36.5_review.md`) cuyos nombres coinciden exactamente con la numeración de interludios usada en los commits recientes de la sesión de escritura (B2C35, B2C36, B2C36.5...) y con el formato de salida descrito en `.claude/skills/chapter-review/SKILL.md` ("produces one verdict... with concrete, evidence-backed fixes"). Esto es la huella del workflow de skills, no del pipeline Python (que no tiene ningún paso que escriba a una carpeta `reports/` dentro de `chapters/`).

**Conclusión de esta sección**: el pipeline de Python y el proceso de skills son dos caminos completamente paralelos y desconectados sobre el mismo contenido narrativo (`content/lore/`), no una cadena de traspaso. El pipeline dejó de tocar prosa real en octubre de 2025; el proceso de skills es quien ha escrito y revisado la totalidad de Books II y III.

---

## Resumen ejecutivo

El pipeline de Python (`src/`, `config/flows/`, `prompts/` activos, `manual_register.py`) está **abandonado**, y no es una inferencia mía: el propio commit de reorganización del 13-08-2026 lo llama textualmente "abandoned automated generation pipeline" y lo excluye vía `.gitignore` como legacy. La verificación técnica confirma esa etiqueta con creces: el motor (`flow_engine.py`) no es importable hoy porque falta `src/secrets.json`; varios scripts (`lore_diff_tracker.py`, `chapter_recap_writer.py`, `memory_plan.py`, `character_tracker.py`, `timeline.py`) siguen apuntando a rutas pre-reorg (`src/lore/`, `src/chapters/`, `output/`) que ya no existen; `manual_register.py` importa tres módulos que nunca existieron; y `src/agents/agents.py` es boilerplate sin adaptar del framework externo `deer-flow` del que se partió. `README_Saga_Functions.md` documenta cinco scripts que jamás existieron en el árbol auditado, y `PROJECT_STRUCTURE.md` documenta tres entrypoints que tampoco existen en `main`. No hay ningún rastro de que la prosa reciente (158 capítulos EN, escritos en la última sesión) haya pasado por este pipeline: la traducción ES que el flujo produce en paralelo lleva sin tocarse desde octubre de 2025, no hay PDFs generados, y las carpetas `reports/` dentro de `chapters/EN/` llevan la huella del workflow de skills (`chapter-review`), no la del pipeline. El proceso de skills (`beat-planner` + `chapter-review`, introducido en el mismo commit que declara el pipeline abandonado) es su **sucesor de facto**, no un complemento: opera sobre el mismo lore base (`content/lore/`) pero por un camino manual/asistido totalmente distinto, sin generación automática end-to-end. La única excepción real de "archivo todavía vivo" es `content/lore/archive/arco_argumental_Duplicado.md`, citado activamente como fuente por el propio `chapter-review`. Mi recomendación es archivar formalmente todo el árbol `src/`, `config/flows/main.yml` y los prompts activos (mover a las carpetas `archive/` ya existentes, siguiendo el patrón que el propio proyecto ya usa), y evaluar borrar `manual_register.py`, `requirements.txt`, `.venv/` y `.env` si no hay intención de revivir la generación automática — la decisión final, como siempre, es del usuario.
