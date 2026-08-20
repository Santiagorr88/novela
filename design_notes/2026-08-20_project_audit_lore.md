# Auditoría de `content/lore/` — estado de los 35 archivos

Fecha: 2026-08-20 · Alcance: solo lectura/investigación, ningún archivo movido ni borrado.
Método: para cada archivo, grep de su nombre en todo el repo (`content/`, `design_notes/`, `reports/`, `.claude/skills/`) para distinguir "referenciado activamente" de "sin referencias entrantes", más lectura del contenido cuando el nombre no bastaba para decidir. Comparación `git diff main v2-rebuild --stat -- content/lore/` para la sección 4.

---

## 1. Archivos de `content/lore/` (fuera de `archive/` y `revision_antigua/`)

| Archivo | Estado | Evidencia | Recomendación |
|---|---|---|---|
| `arco_argumental_completo.md` | **Activo** | Outline canónico, 428 entradas, editado hoy mismo (mtime más reciente que casi todo el directorio). `.claude/skills/chapter-review/SKILL.md` lo usa junto con `archive/arco_argumental_Duplicado.md` para confirmar orden/títulos de beats. | Mantener. Ver caveat en §3 sobre doble fuente de verdad para el final de la trilogía (ya documentado en `design_notes/2026-08-19_overnight_audit.md`, no es hallazgo nuevo). |
| `expansion_guidelines.md` | **Activo — fuente de verdad declarada** | Tracker cronológico único de las 3 partes del Libro I + Libro II completo + Libro III completo + auditorías. Citado como origen de reglas (target de palabras, densidad de beats) por casi todos los demás archivos. | Ver veredicto dedicado en §3. |
| `prompt_universo.md` | **Activo, con hallazgo de duplicación** | Guía de estilo + leyes fundamentales, sección "FULL CHARACTER DOSSIERS" (líneas 552-2925, ~2.373 líneas de las 2.925 totales, >80% del archivo) es prácticamente idéntica carácter a carácter a `personajes.md`. `v2-rebuild` ya diagnosticó y corrigió exactamente esta duplicación el 2026-08-17 (ver §4). | El bloque narrativo/leyes (líneas 1-551) es la parte realmente activa y sin duplicar. Considerar aplicar en `main` la misma poda que ya existe en `v2-rebuild`: sustituir los dossiers completos por punteros a `personajes.md`. |
| `personajes.md` | **Activo** | Fuente única real de fichas de personaje; citado constantemente por los `book*_expanded_beats.md`. Es la versión "definitiva" según el propio `v2-rebuild`. | Mantener. |
| `personajes_muertes_reencarnaciones.md` | **Activo** | Decisión canónica de la subtrama Nael/Nathaniel Vale (ubicación en Libro II), citado por `ideas_pendientes.md` y `book1_new_subplots_candidates.md`. | Mantener. |
| `book1_part1_expanded_beats.md` | **Activo** | Prosa APPROVED del Cap. 3 ya la usa como fuente; parte del tracker "PARTE 1 DEL LIBRO I COMPLETA" en `expansion_guidelines.md`. | Mantener. |
| `book1_part2_expanded_beats.md` | **Activo** | Beats reales de los 10 capítulos "originales" de la Parte 2; progreso rastreado en `expansion_guidelines.md`. | Mantener. |
| `book1_part3_expanded_beats.md` | **Activo** | Corrección de continuidad de "The Victor's Burden" citada y verificada contra `archive/arco_argumental_Duplicado.md`. | Mantener. |
| `book1_lament_arc.md` | **Activo** | Arco L1-L6 APPROVED por Codex; citado como fuente terminológica canónica ("Weeping Sepulcher") y como referencia cruzada verificada por `reports/16_auditoria_consistencia_libro1.md`. | Mantener. |
| `book1_new_subplots_beats.md` | **Activo** | Desarrollo beat a beat aprobado de las 5 tramas nuevas; fuente citada por `book1_part2_master_order.md`, `book1_part3_expanded_beats.md`, `expansion_guidelines.md` y `.claude/skills/beat-planner/SKILL.md`. | Mantener. |
| `book1_new_subplots_candidates.md` | **Histórico-útil, no redundante** | Es el documento de *propuesta/razonamiento* (por qué esas 5 tramas), distinto en función de `book1_new_subplots_beats.md` (el *desarrollo* aprobado). Sigue citado por nombre en `reports/16` y en `personajes_muertes_reencarnaciones.md` como referencia del cálculo del déficit de beats del Libro I. | Conservar donde está; es la traza de la decisión, no un duplicado de contenido. |
| `book1_part2_master_order.md` | **Activo** | `expansion_guidelines.md` lo llama explícitamente "tracker vivo... confirmado con el usuario (2026-08-14)" de los 41 capítulos-unidad restantes. | Mantener — es el orden de lectura real en uso. |
| `b1c14_beats_expanded.md` | **Activo** (pese al nombre hiperespecífico) | Principio de diseño de Belial/Lament citado y verificado contra `book1_part2_expanded_beats.md` (beat B1C20) y contra `book1_lament_arc.md` (L5); `reports/16` confirma que los nombres de beat coinciden exactamente. | Mantener — no es un experimento puntual, es la base de un principio de caracterización que otros documentos dan por sentado. |
| `beat_density_test.md` | **Activo** (pese al nombre de "test") | `expansion_guidelines.md` lo cita como la fuente de la métrica medida (~342-450 palabras/beat) que sostiene una regla dura de planificación. | Mantener. |
| `book1_part1_restructure_proposal.md` | **Redundante — candidato claro a archivar** | Única referencia entrante es la propia `expansion_guidelines.md`, y esa referencia dice literalmente que su target de palabras está "superada". Ninguna otra dependencia. | Archivar (mover a `content/lore/archive/`, no borrar). |
| `book1_part2_restructure_proposal.md` | **Casi redundante — histórico de procedencia** | Su contenido (mapeo + notas obligatorias) ya está absorbido en `book1_part2_expanded_beats.md`, que la cita como "fuente del material original". Sigue citada también por `book1_lament_arc.md` y `reports/16`. | Buena candidata a archivar: ya cumplió su función, las citas restantes son de procedencia, no de dependencia activa. |
| `book2_structure_proposal.md` | **Parcialmente redundante — el propio archivo se autodeclara superado** | Encabezado explícito: "⚠️ SUPERADO (2026-08-11)... La arquitectura de abajo queda descartada... Se conserva únicamente la sección 'Hilo explícito: el sistema de reencarnación'". | Recomendación: extraer solo esa sección vigente a otro documento (o a `personajes_muertes_reencarnaciones.md`) y archivar el resto; o dejarlo tal cual, ya que se autodocumenta correctamente. |
| `book1_part1_expanded_beats.md`, `book2_part1..3`, `book3_part1..3` (grupo `expanded_beats`) | **Activos** | Todos son la fuente de beats operativa citada en `expansion_guidelines.md`, con timestamps de modificación de hoy (Libro III, Parte 2 modificado hace minutos). | Mantener todos. |
| `ideas_pendientes.md` | **Desactualizado — necesita revisión, no exactamente redundante** | De 8 ideas: 3 marcadas explícitamente RESUELTO por el propio documento (#6-8); pero además la #1 y #3 aparecen ya desarrolladas en otros documentos (`b1c14_beats_expanded.md`/`book1_lament_arc.md` para la #1; Trama 5 de `book1_new_subplots_beats.md` para la #3) sin que el documento lo refleje; la #5 ("desastres naturales") está marcada "pendiente de integrar" pero `book1_lament_arc.md` línea 78 dice textualmente "cumplida en L4... y L6". Solo la #2 y la #4 (norma de estilo general) siguen genuinamente abiertas/evergreen. | Actualizar los estados de las ideas 1, 3 y 5 a RESUELTO con puntero al documento donde se cumplieron; no archivar, sigue siendo el buzón de ideas sueltas vivo. |

**Nota sobre `book1_part2_restructure_proposal.md` vs `book2_structure_proposal.md` vs `book1_part1_restructure_proposal.md`**: los tres nombres sugieren la misma categoría ("propuesta de reestructuración"), pero su estado real difiere: el de Libro I Parte 1 está objetivamente descartado (solo una cita residual reconociendo su obsolescencia); el de Libro I Parte 2 cumplió su función de mapeo y quedó como registro de procedencia; el de Libro II está parcialmente vigente (una sección) por declaración explícita propia. No conviene tratarlos como un lote homogéneo.

---

## 2. `archive/` y `revision_antigua/`

### `content/lore/archive/` (6 archivos, confirmado histórico por nombre — con matiz)
- `arco_argumental_Duplicado.md` (366 KB) y sus splits `_part1.md`, `_part2.md`, `_part3.md`
- `arco_argumental_completo_detallado.md`
- `capitulos_renumerados.md`

**Matiz importante**: `arco_argumental_Duplicado.md` (y sus partes) no es solo "se usó como fuente en sesiones anteriores" — sigue siendo la **fuente operativa primaria activa** para el beat-planning de los tres libros. Está citado explícitamente como fuente de origen en `book1_part1_expanded_beats.md`, `book1_part2_expanded_beats.md`, `book2_part1..3_expanded_beats.md`, `book3_part1..3_expanded_beats.md`, y en `.claude/skills/chapter-review/SKILL.md`, donde se instruye usar "`Duplicado.md`'s richer per-beat summaries as primary source for the chapter's own beats". Es decir: vive en una carpeta llamada `archive/` (que implica "cerrado/histórico") pero un skill de producción sigue leyéndolo activamente hoy. Esto no es un problema de contenido huérfano — al contrario, es la evidencia de que archivar sin verificar referencias entrantes habría sido un error. Se documenta aquí solo como nota de nomenclatura: el nombre de la carpeta es engañoso respecto a su rol real.

`arco_argumental_completo_detallado.md` y `capitulos_renumerados.md` no tienen referencias entrantes detectadas fuera de `archive/` — consistentes con ser snapshots verdaderamente históricos.

### `content/lore/revision_antigua/` (5 archivos, confirmado histórico, sin matices)
- `arco_1.md`, `arco_argumental_all_books.md`, `arco_argumental_book01.md`, `arco_argumental_expand_1_al_10.md`, `reducido_chapter_01.md`

**Cero referencias entrantes** detectadas en todo el repo (código, lore, reports, design_notes, skills). A diferencia de `archive/`, esta carpeta parece completamente huérfana — ningún documento activo la menciona ni siquiera como procedencia histórica reconocida. Candidata más limpia de las dos para consolidar/cerrar si en algún momento se decide reducir el directorio, aunque la tarea es solo de auditoría.

---

## 3. Veredicto: `expansion_guidelines.md`

**186.793 bytes, 453 líneas, 9 secciones de nivel `##`** que abarcan: reglas de Libro I, "Libro II completo", "Libro III completo — trilogía completa", "repaso final completo", "Parte 1 del Libro I completa", pase de pulido, auditoría de incoherencias, y la sesión de hoy mismo (Marbas/Raum/Valefar/Vine).

**Opinión honesta**: el documento ha dejado de ser lo que su nombre y su primera línea dicen que es ("Directrices de expansión — Libro I (y luego II-III)"). Empezó como guía de reglas para el Libro I y ha crecido hasta ser, a la vez: (a) un libro de reglas transversal a la trilogía, (b) un log cronológico append-only de todo lo aprobado en las tres partes de los tres libros, y (c) un registro de auditorías de continuidad. Estas tres funciones tienen ciclos de vida distintos — las reglas son estables, el log de progreso crece sin parar, las auditorías son eventos puntuales — y hoy comparten un único archivo de 187 KB que cualquier consulta (humana o de agente) tiene que atravesar entero o hacer grep para encontrar lo relevante.

No ha llegado todavía a un tamaño técnicamente inmanejable (sigue siendo legible con grep/Read por secciones), pero la tendencia de crecimiento de esta sesión (pasó a tener contenido de Libro III completo, más las verificaciones de captains de hoy) sugiere que seguirá creciendo al mismo ritmo según avance la prosa real. **Recomendación**: dividir en al menos dos ejes — (1) reglas/convenciones estables (target de palabras, categorías de expansión aprobadas, reglas de consistencia) que rara vez cambian, y (2) un tracker de progreso por libro (`expansion_progress_libro1.md`, `_libro2.md`, `_libro3.md`, o similar) que crece con cada capítulo aprobado. Alternativa más simple: dejar las reglas donde están y mover las secciones ya "🎉 COMPLETA/TERMINADO" (Libro II completo, Libro III completo, repaso final) a un archivo de histórico separado, ya que esas secciones no van a volver a cambiar. La decisión final es del usuario — esto es una recomendación, no una acción tomada.

---

## 4. Veredicto: `main` vs `v2-rebuild`

`git diff main v2-rebuild --stat -- content/lore/` (30 archivos con diferencias, +2.520/-12.359 líneas) confirma la premisa: `v2-rebuild` es una rama más antigua (último commit 2026-08-18 19:55) frente al HEAD actual de `main` (2026-08-20 13:56) y su contenido de outline ya está superado por el trabajo posterior en `main` — casi todos los `book*_expanded_beats.md` y ambas carpetas `archive/`/`revision_antigua/` no existen en `v2-rebuild` porque `main` los añadió después de la bifurcación.

**Pero hay un hallazgo real, no trivial**: `v2-rebuild` tiene 4 archivos que **no existen en `main` bajo ningún nombre**:
- `narrator_patterns.md` — librería de 13 patrones narrativos por capítulo, derivados empíricamente del corpus v1.
- `style_tics_denylist.md` — lista de tics de estilo medidos sobre 142 capítulos del corpus v1 (cadencia de frase, secuencias repetidas), pensada como input de un futuro `saga_sentinel`.
- `personajes_celestial.md` y `personajes_demoniacos.md` — resultan ser un **split exacto** de `personajes.md` (verificado por diff línea a línea: solo cambios cosméticos menores), hecho el 2026-08-17 en `v2-rebuild` para separar bandos. No es contenido nuevo, es una reorganización no adoptada en `main`.

De estos, `narrator_patterns.md` y `style_tics_denylist.md` referencian una arquitectura de pipeline (`story_architect`, `chapter_planner`, `saga_sentinel`) que no existe en `main` — son diseño para una reconstrucción completa del proceso de generación (`v2-rebuild`) que nunca se materializó en `main`, donde el pipeline real sigue siendo `beat-planner`/`chapter-review` (ambos sí existen en `.claude/skills/` de `main`). Es decir, es contenido de diseño de un camino alternativo no tomado, no una laguna de `main` que haya que rellenar urgentemente.

**Hallazgo colateral confirmado por este mismo diff, y que sí importa para `main`**: la nota interna de `v2-rebuild`'s `prompt_universo.md` (fechada 2026-08-17) documenta que los dossiers de personaje se retiraron de `prompt_universo.md` "por ser un duplicado exacto (verificado carácter a carácter)" de `personajes.md`, dejando solo punteros. **Esa limpieza nunca se aplicó en `main`** — `main`'s `prompt_universo.md` sigue teniendo el duplicado completo de 2.373 líneas (ver §1). `v2-rebuild` diagnosticó correctamente un problema real de `main` que sigue sin resolverse ahí.

**Conclusión sobre la relación de ramas**: es seguro considerar `v2-rebuild` histórica/cerrable en cuanto a outline y estructura de capítulos (todo eso ya vive, mejorado, en `main`). No es seguro decir que no tiene nada de valor: los 4 archivos únicos son diseño de proceso descartado (bajo riesgo de pérdida real) salvo por el diagnóstico de duplicación de `prompt_universo.md`/`personajes.md`, que sí es una mejora concreta pendiente de portar a `main` si se decide hacerlo. No se ha hecho merge ni se ha tocado la rama, conforme a las instrucciones.

---

## Resumen ejecutivo

- **Archivos candidatos a archivar/redundantes** (fuera de `archive/`/`revision_antigua/`): **2 claros** — `book1_part1_restructure_proposal.md` (autodeclarado superado) y `book1_part2_restructure_proposal.md` (contenido absorbido, solo valor de procedencia). **2 parciales** — `book2_structure_proposal.md` (superado salvo una sección) y `ideas_pendientes.md` (no es redundante en sí, pero tiene ≥3 de 8 entradas con estado desactualizado que deberían marcarse RESUELTO). El resto (20 de 24 archivos activos) tiene referencias entrantes activas verificadas y ninguno de los nombres "sospechosos" señalados en el encargo (`b1c14_beats_expanded.md`, `beat_density_test.md`, `book1_part2_master_order.md`, `book1_new_subplots_candidates.md`) resultó ser redundante — todos siguen citados y usados pese a sus nombres hiperespecíficos.

- **Los 3 hallazgos más importantes**:
  1. **`prompt_universo.md` duplica ~80% de su contenido (2.373 líneas) con `personajes.md`**, carácter por carácter. `v2-rebuild` ya diagnosticó y corrigió exactamente este problema el 2026-08-17 dejando solo punteros cruzados — esa limpieza nunca se portó a `main`. Es la redundancia de mayor volumen encontrada en todo el directorio, mayor que cualquiera de los documentos de "propuesta" señalados en el encargo.
  2. **`content/lore/archive/arco_argumental_Duplicado.md` no es solo histórico** — pese a vivir en una carpeta llamada `archive/`, sigue siendo la fuente primaria activa de beat-planning para los tres libros, citada explícitamente como fuente operativa en `.claude/skills/chapter-review/SKILL.md` y en prácticamente todos los `book*_expanded_beats.md`. El nombre de la carpeta no refleja su rol real en el pipeline actual.
  3. **`expansion_guidelines.md`** ha crecido más allá de su alcance original (Libro I) hasta cubrir reglas + progreso + auditorías de la trilogía completa en un solo archivo de 187 KB; mezcla contenido estable (reglas) con un log append-only que seguirá creciendo. Recomendado dividir por función (reglas vs. progreso por libro) antes de que se vuelva difícil de navegar, aunque hoy todavía es manejable.

- `content/lore/revision_antigua/` está completamente huérfana (cero referencias entrantes en todo el repo) — la más limpia candidata a considerar cerrada de las dos carpetas históricas, si se decide actuar sobre alguna.
