# Auditoría de estructura del proyecto — fuera de `content/lore/` y del pipeline Python

Fecha: 2026-08-20
Alcance: `project/`, `reports/` (raíz), `design_notes/` (raíz), ramas de git, archivos sueltos en raíz, `.gitignore`. No se tocó `content/lore/` ni `src/`/`config/`/`prompts/` (cubiertos por otros dos agentes en paralelo). Auditoría de solo lectura — no se movió, borró ni editó ningún archivo.

---

## 1. `project/Chronicles_of_the_Sundering_Judgment/` — estructura completa

Estructura real (profundidad 3):

```
project/Chronicles_of_the_Sundering_Judgment/
└── chapters/
    ├── ES/
    └── EN/
        └── reports/
```

No hay archivos sueltos fuera de `chapters/EN` y `chapters/ES` (no hay nada directamente en `project/Chronicles_of_the_Sundering_Judgment/` ni directamente en `chapters/`).

### 1a. Traducción al español — muy por detrás

`chapters/ES/` existe pero contiene **solo 2 archivos**, ambos con fecha del 18 de agosto (el día del gran reestructuro), sin tocar desde entonces:

- `B1C01_ES_v2.md`
- `B1L01_ES.md`

Frente a los **157 archivos** en `chapters/EN/` (que cubren los 3 libros completos, más las decenas de capítulos añadidos hoy y ayer). La carpeta ES traduce, en la práctica, un único capítulo del Libro I (`C01`) y un interludio (`L01`, arco "Lament"). No hay ni rastro de Libro II ni Libro III en español. **Conclusión: la traducción ES no está "algo por detrás", está esencialmente abandonada/nunca se retomó** tras el arranque inicial — 155 capítulos de diferencia y ningún commit de traducción en las últimas ~30h de trabajo intensivo en inglés.

### 1b. `chapters/EN/reports/` — cobertura de revisión

Contiene **19 archivos** de revisión (`*_review.md`), fechados entre el 18 y el 20 de agosto. No hay duplicados por capítulo — cada informe corresponde a un identificador de capítulo distinto (p. ej. `B2C36.5`, `B2C36.6`, `B2C36.7` no son tres revisiones del mismo capítulo, sino revisiones de tres sub-capítulos/inserciones distintas: 36.5, 36.6 y 36.7). En ese sentido la carpeta está "limpia" — no hay señales de revisiones repetidas sobre el mismo archivo.

Lo que sí llama la atención es la **cobertura muy parcial**: de 157 archivos de capítulo, solo 19 tienen un `_review.md` asociado, y son casi exclusivamente capítulos "sueltos"/insertados con sufijo `.5`, `.6`, `.7` (contenido añadido a posteriori entre capítulos existentes) más `B1C01` y `B1L01`. La inmensa mayoría de los ~150 capítulos troncales (`B1C11`…`B3C45`) generados en la sesión larga **no tiene informe de revisión en esta carpeta**. Si el flujo de trabajo espera un review por capítulo, aquí falta casi todo; si el review solo se aplica a inserciones puntuales, la carpeta está haciendo su trabajo correctamente — pero no es evidente cuál de los dos es el caso desde la estructura sola.

### 1c. Archivo suelto que no encaja / hallazgo estructural importante: colisión de numeración en Libro I

`chapters/EN/` mezcla **dos convenciones de nombrado distintas para el mismo rango de capítulos del Libro I**:

- Estilo antiguo (`ago 18 20:01`, 12 archivos): `B1Cap01_EN.md` … `B1Cap12_EN.md`
- Estilo nuevo (`ago 20 00:04-00:05`, empieza en 11): `B1C11_EN.md`, `B1C12_EN.md`, `B1C13_EN.md`, `B1C15_EN.md`...

**`B1Cap11_EN.md` y `B1C11_EN.md` coexisten con contenido completamente distinto**: el primero es "Chapter 11 — Crossings / The First Doubt", el segundo es "B1C11 – The Devil's Gambit". Lo mismo ocurre con el par 12 (`B1Cap12` vs `B1C12`). Es decir, hay **dos capítulos "11" y dos capítulos "12" distintos en el mismo libro**, bajo prefijos de nombre distintos, sin que ninguno esté marcado como obsoleto o renombrado. Los libros II y III no tienen este problema — usan únicamente el prefijo `C` de forma consistente.

Esto no es solo un problema cosmético de nombrado: cualquier script, informe o referencia cruzada que apunte a "capítulo 11 del Libro I" es ambigua. Recomiendo que el usuario decida si `B1Cap01-12` son la versión legada que debe archivarse/renombrarse (p. ej. a `B1Cap01_OLD_EN.md` o moverse fuera de `chapters/EN/`), o si en realidad `B1C11`/`B1C12` deberían haberse numerado de otra forma para no chocar con capítulos preexistentes.

También cabe notar que dentro de `chapters/EN/` hay varios prefijos de una sola letra por libro (`C`, `F`, `H`, `L`, `N`, `T`, `V` en Libro I) que parecen representar arcos narrativos distintos (p. ej. `L` = arco "Lament", visto en `B1L01`). Esto en sí no es un problema — parece intencional — pero junto con la colisión `Cap`/`C` hace que la convención de nombrado del Libro I sea más difícil de auditar automáticamente que la de Libros II y III.

---

## 2. `reports/` en la raíz del repo (17 archivos)

Esta carpeta es claramente de una **fase anterior y distinta** del proyecto — la fase de diseño de producto/plataforma, no la de escritura de la novela. Fechas: la mayoría del 6-8 de agosto, con una excepción (`15_council_palabras_capitulo.md`) del 16 de agosto. Nada aquí es de la sesión larga de las últimas 24-30h.

Contenido (según los nombres y una lectura de las primeras líneas):

| Archivo | Fecha | Contenido |
|---|---|---|
| `01_repo_audit.md` | 6 ago | Auditoría técnica del repo (fase inicial) |
| `02_product_definition.md` | 6 ago | Definición de producto — "Plataforma de novelas serializadas → vídeo narrativo" |
| `03_workspace_architecture.md` | 6 ago | Arquitectura del workspace |
| `04_create_novel_design.md` | 6 ago | Diseño del flujo de creación de novela |
| `05_narrative_memory_canon.md` | 6 ago | Diseño de memoria narrativa/canon |
| `06_agents_design.md` | 6 ago | Diseño de agentes |
| `07_audiovisual_pipeline.md` | 6 ago | Pipeline audiovisual |
| `08_skills_research.md` | 6 ago | Investigación de skills |
| `09_council_brief.md` | 6 ago | Brief para consejo de IA |
| `10_council_report.html` | 6 ago | Informe de consejo (HTML) |
| `10_council_transcript.md` | 6 ago | Transcripción del consejo |
| `11_mvp_plan.md` | 6 ago | Plan de MVP |
| `12_chapter_generation_agent_audit.md` | 8 ago | Auditoría quirúrgica de agentes para "generar un capítulo" |
| `13_council_parte1_transcript.md` | 6 ago | Transcripción de consejo, parte 1 |
| `14_council_avance_expansion.md` | 6 ago | Avance de expansión |
| `15_council_palabras_capitulo.md` | 16 ago | Consejo sobre extensión de capítulos |
| `16_auditoria_consistencia_libro1.md` | 8 ago | Auditoría de consistencia — Libro I (planificación acumulada) |

Esto es evidentemente el historial de diseño del **pipeline Python/plataforma** (probablemente relacionado con lo que el otro agente está auditando en `src/`/`config/`/`prompts/`) — decisiones de producto y arquitectura tomadas antes de que existiera el grueso del contenido narrativo actual. No hay señales de que se siga escribiendo aquí: la actividad de auditoría se trasladó a `design_notes/` a partir del 19 de agosto, con una convención de nombrado distinta (fecha ISO + tema, en vez de número secuencial + tema).

**Recomendación:** esta carpeta ya cumplió su función de fase de diseño. Tiene sentido archivarla (p. ej. `reports/archive/` o `design_notes/archive/reports_fase1/`) para dejar claro que es historial, no una carpeta activa — pero la decisión final, y si hay contenido aquí que el otro agente auditando el pipeline Python todavía necesita como referencia viva, corresponde al usuario.

---

## 3. `design_notes/` en la raíz — auditoría de sí misma

Listado completo (`ls -la`) en el momento de esta auditoría — 9 archivos, todos del 19-20 de agosto (incluye los que los otros dos agentes en paralelo pueden estar escribiendo o actualizando ahora mismo; no se leyó su contenido, solo se cuentan):

| Archivo | Fecha/hora |
|---|---|
| `2026-08-19_contradictions_and_citations.md` | 19 ago 23:58 |
| `2026-08-19_overnight_audit.md` | 19 ago 23:45 |
| `2026-08-19_overnight_summary.md` | 20 ago 07:39 |
| `2026-08-20_captains_verification.md` | 20 ago 09:44 |
| `2026-08-20_fresh_audit_book2.md` | 20 ago 13:48 |
| `2026-08-20_fresh_audit_book3.md` | 20 ago 13:49 |
| `2026-08-20_marbas_raum_valefar_vine_verification.md` | 20 ago 10:21 |
| `2026-08-20_naamah_verification.md` | 20 ago 08:04 |
| `2026-08-20_orobas_malphas_flauros_amy_verification.md` | 20 ago 10:19 |

(Nota: los agentes en paralelo probablemente están añadiendo archivos como el que corresponde al pipeline Python y a `content/lore/`, y posiblemente también este mismo informe estructural — el conteo de arriba es un snapshot del momento de esta auditoría, no un total definitivo.)

**Opinión (no ejecutada):** varios de estos informes son, por su nombre, verificaciones puntuales ya resueltas — p. ej. `..._captains_verification.md`, `..._naamah_verification.md`, `..._marbas_raum_valefar_vine_verification.md`, `..._orobas_malphas_flauros_amy_verification.md` parecen checks de consistencia de personajes específicos (probablemente ya aplicados a los capítulos correspondientes, a juzgar por los commits recientes en `main` como "Add first scenes for Marbas, Raum, Valefar, and Vine..." y "Fix findings from fresh audit..."). Si esos hallazgos ya se aplicaron y confirmaron en el contenido, esos informes han cumplido su función y son candidatos naturales a mover a `design_notes/archive/` — mantienen valor como registro histórico pero no necesitan estar al mismo nivel que las auditorías activas/recientes (`overnight_summary`, `fresh_audit_book2/3`, que parecen ser el estado más actual y probablemente aún accionable).

Igual que en el punto 2, esto es una recomendación, no una acción — y dado que hay dos agentes escribiendo en esta misma carpeta ahora mismo, cualquier reorganización debería esperar a que terminen para no pisar su trabajo.

---

## 4. Ramas de git

```
* main
  v2-rebuild
  claude/serialized-novels-video-platform-116335   (solo local, sin remoto)
  remotes/origin/main
  remotes/origin/v2-rebuild
```

### `main`
- 675 commits totales. Último commit: `a3f023c "Fix findings from fresh audit of today's 5 Book III chapters"` (20 ago 13:56).
- Últimos 5 commits, todos de la sesión reciente:
  - `a3f023c` Fix findings from fresh audit of today's 5 Book III chapters
  - `96d7b2e` Fix 16 POV violations found in fresh audit of today's 5 Book II chapters
  - `393c982` Add first scenes for Marbas, Raum, Valefar, and Vine (Foras/Vepar captains)
  - `cf1ba71` Add first scenes for Orobas, Malphas, Flauros, and Amy (Balam/Agares captains)
  - `49e06cb` Add first scenes for Eshriel, Jahiel, and Zaphiel (Raziel's captains)
- Rama activa, al día, con la última sesión de trabajo intensiva.

### `v2-rebuild`
- 671 commits. Diverge de `main` en el commit `6b422a5 "Fix B1L02: Michael -> Miguel naming inconsistency"` (15 ago 2026), es decir, hace ~5 días respecto a hoy.
- Último commit: `1d89d3f "v2-rebuild: add main-branch prose audit (informs Aamon reconciliation + migration strategy)"` (18 ago 19:55).
- Últimos 5 commits muestran trabajo activo de reconciliación de canon (fechas de personajes, migración de material del Libro III, resolución de arcos huérfanos del Libro II):
  - `1d89d3f` add main-branch prose audit
  - `8fbd78b` reconcile Aamon's fate with main (dies in Book I, not Book III)
  - `226ab7e` recover Book III climax material from Duplicado.md
  - `ca16d76` install 6 orphaned Book II setups + resolve Sariel
  - `a7b2c26` fix B2C142 citation error
- **No se ha tocado desde el 18 de agosto**, mientras que `main` ha seguido recibiendo commits masivamente hasta hoy (20 ago). Es decir, `v2-rebuild` lleva ~2 días parada mientras `main` avanzaba con ~4 commits diarios de contenido nuevo — la brecha entre ambas ramas probablemente ha crecido, no se ha cerrado. Existe también en remoto (`origin/v2-rebuild`).
- Esta rama merece atención del usuario: parece ser un esfuerzo paralelo de reconciliación/reconstrucción de canon que se ha quedado descolgado del ritmo de `main`.

### `claude/serialized-novels-video-platform-116335`
- 412 commits. **Solo existe en local, no en remoto.**
- Punto clave: `git merge-base main claude/serialized-novels-video-platform-116335` devuelve exactamente el hash del HEAD de esta rama (`981b81b`). Esto significa que **la rama entera ya está contenida dentro del historial de `main`** — no tiene ni un solo commit propio que no esté ya en `main`. No es un experimento con trabajo perdido por fusionar; es, literalmente, un punto antiguo de la historia que `main` ya superó y absorbió.
- Los commits van desde abril 2025 (`feat: lite deep researcher implementation`, `feat: support arxiv & brave search`, etc. — claramente el andamiaje original del framework "deer-flow" de investigación, del que este repo de novelas parte/deriva) hasta octubre 2025 (varios commits genéricos `"my book"`).
- **Conclusión: es un checkpoint histórico ya fusionado, no un experimento abandonado con trabajo único.** Se puede borrar sin pérdida de trabajo si el usuario quiere limpiar `git branch -a`, aunque no urge — no estorba al no tener remoto ni ser rama por defecto.

---

## 5. Archivos sueltos en la raíz del repo

`ls -la` en la raíz, más allá de lo ya documentado por el otro agente (`.env`, `.gitignore`, `manual_register.py`, `PROJECT_STRUCTURE.md`, `README_Saga_Functions.md`, `requirements.txt`):

```
assets/          content/         project/
.claude/         design_notes/    prompts/
config/          .git/            reports/
                 .idea/           src/
                                  .venv/
```

No se encontraron archivos sueltos adicionales sin documentar (no hay logs, cachés, archivos `.DS_Store`, backups `*.bak`/`*~`, ni configuración de editor fuera de `.idea/`, que ya está correctamente ignorada — ver punto 6). La raíz está razonablemente ordenada dado el volumen de trabajo reciente.

---

## 6. `.gitignore` — evaluación

Contenido relevante:

```
.venv
venv/
.env
secrets.json
**/secrets.json
.idea/
.claude/settings.local.json
.claude/settings.local.json.tmp.*
.claude/worktrees/
data/
artifacts/logs/
src/chapters/
```

Verificación cruzada con `git status --short` (árbol de trabajo limpio, sin salida) y `git status --ignored --short`:

```
!! .claude/settings.local.json
!! .claude/settings.local.json.tmp.63091.368d73f893ea
!! .env
!! .idea/
!! .venv/
```

Todo lo que debería estar ignorado, lo está: `.venv/`, `.idea/`, `.env` se confirman excluidos correctamente, y no hay tampoco ningún archivo `.tmp` residual filtrándose al tracking. **No hay nada sin rastrear que debería ignorarse y no lo está, ni nada rastreado que probablemente debería estar en `.gitignore`.** El árbol de trabajo está completamente limpio (sin cambios pendientes de commit) en el momento de esta auditoría. El `.gitignore` está bien configurado y no requiere cambios.

Nota: la entrada `src/chapters/` (comentada como "legacy automated-pipeline cache/state/logs, superseded by the current manual + Codex-review workflow") confirma en el propio archivo que hubo una migración de flujo de trabajo — coherente con lo observado en los puntos 1 y 2 (el contenido activo ahora vive en `project/Chronicles_of_the_Sundering_Judgment/`, no en `src/`).

---

## Resumen ejecutivo

1. **Ramas:** `main` está al día y activa (último commit hoy). `v2-rebuild` es un esfuerzo de reconciliación de canon real y en curso, pero **lleva ~2 días parada** mientras `main` seguía añadiendo capítulos — la brecha entre ambas probablemente ha crecido; merece decisión del usuario sobre si retomarla, fusionarla o abandonarla. `claude/serialized-novels-video-platform-116335` es historia ya absorbida por `main` (0 commits únicos) — se puede borrar sin pérdida, no es un experimento con trabajo pendiente.
2. **Basura sin ignorar en el repo:** ninguna. `git status --short` está limpio y `.gitignore` cubre correctamente `.venv/`, `.idea/`, `.env` y los archivos temporales de `.claude/`. No hay archivos sueltos sospechosos en la raíz.
3. **Los 3 hallazgos más importantes:**
   - **Colisión de numeración en Libro I:** `B1Cap11_EN.md`/`B1Cap12_EN.md` (contenido antiguo, 18 ago) coexisten con `B1C11_EN.md`/`B1C12_EN.md` (contenido nuevo, 20 ago) — dos capítulos "11" y dos "12" completamente distintos y sin desambiguar. Riesgo real de confusión/citas cruzadas erróneas.
   - **Traducción ES prácticamente inexistente:** solo 2 de 157 capítulos EN tienen versión en español (~1.3%), sin actividad desde el 18 de agosto pese a la explosión de contenido en inglés.
   - **`v2-rebuild` estancada:** rama de reconciliación de canon activa y con trabajo genuino, pero sin commits desde el 18 de agosto mientras `main` avanzaba con fuerza — decisión pendiente sobre su futuro antes de que la brecha sea inmanejable.

Recomendaciones adicionales (no ejecutadas): archivar `reports/` (raíz, fase de diseño de producto ya superada) y considerar mover a `design_notes/archive/` los informes de verificación puntual ya aplicados dentro de `design_notes/` — ambas son decisiones del usuario, no acciones tomadas por esta auditoría.
