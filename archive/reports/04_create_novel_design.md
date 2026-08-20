# Diseño de la creación guiada de novelas (`create-novel`)

Fecha: 2026-08-06
Estado: propuesta para revisión del usuario (diseño, no implementación — la implementación es tarea de Fase 13)

## 1. Modelo de interacción

`create-novel` no es un formulario. Es una conversación de diseño narrativo conducida por un único agente (el "Director creativo" de la Fase 7) contra un **banco de preguntas** determinista y versionado. La distinción importa:

- El **banco de preguntas** (sección 3) es fijo y auditable: garantiza que ningún campo necesario para generar el paquete inicial se quede sin preguntar, y hace la entrevista reproducible/depurable.
- El **agente** decide, dentro de cada sección, en qué orden formular las preguntas core, qué preguntas condicionales activar según las respuestas ya dadas, y qué *sub-preguntas de seguimiento* generar dinámicamente cuando una respuesta es vaga, contradictoria o interesante y merece profundizar (p. ej. si el usuario dice "el protagonista tiene un miedo irracional al fuego", el agente puede preguntar de dónde viene ese miedo, aunque esa sub-pregunta no esté en el banco fijo).
- Nunca se presentan más de ~2-4 preguntas por turno. Cada sección se cierra con un resumen corto que el usuario puede corregir antes de pasar a la siguiente ("Hasta aquí tengo esto — ¿lo dejamos así o ajustamos algo?").

Esto evita los dos extremos malos: un formulario gigante (lo que el usuario pidió evitar explícitamente) y una conversación completamente libre sin garantías de cobertura (que arriesgaría dejar huecos en el paquete inicial).

## 2. Secciones (orden fijo, con dependencia entre ellas)

1. **Identidad del proyecto** — siempre primero, define metadatos base.
2. **Género y propuesta** — condiciona el tono de las preguntas siguientes.
3. **Mundo** — puede saltarse/abreviarse si el género es "contemporáneo realista sin elementos especulativos" (detectado en la sección 2).
4. **Personajes** — usa el mundo ya definido como contexto.
5. **Estructura narrativa** — usa personajes y premisa ya definidos.
6. **Identidad audiovisual** — última, porque depende de tono/género/mundo ya fijados (p. ej. el estilo visual y musical se sugiere como default a partir de lo anterior, y el usuario solo confirma o corrige, en vez de partir de cero).

Cada sección tiene: preguntas **core** (siempre se hacen), preguntas **condicionales** (dependen de una respuesta anterior) y espacio para **follow-ups adaptativos** del agente.

## 3. Banco de preguntas

### 3.1 Identidad del proyecto (core, todas obligatorias)
Título provisional · idioma · público objetivo · plataforma principal · frecuencia prevista de publicación · duración aproximada de cada capítulo · duración prevista de cada vídeo.

### 3.2 Género y propuesta (core)
Género principal · premisa (una frase) · gancho principal · tono.
Condicionales: subgéneros (si el usuario menciona más de un género al describir la premisa) · temas (siempre se pregunta, pero se sugieren candidatos a partir de la premisa) · nivel de violencia/romance/contenido adulto (siempre, porque condiciona plataforma y monetización) · referencias creativas (opcional, se ofrece pero no se insiste) · elementos a evitar (siempre se pregunta explícitamente, es una restricción dura para todos los agentes posteriores).

### 3.3 Mundo (condicional a que el género no sea "contemporáneo realista puro")
Core: tipo de mundo · época · reglas especiales relevantes a la trama.
Condicionales: si hay magia/poderes → sistema de poderes + limitaciones (obligatorio profundizar, es fuente típica de contradicciones futuras); si hay facciones/política relevante a la premisa → facciones + conflictos; tecnología, geografía, culturas, religiones, economía, historia se preguntan solo si la premisa o el gancho ya los menciona o si el usuario quiere expandirlos — no se interroga exhaustivamente un mundo que la trama no va a usar.

### 3.4 Personajes (core)
Protagonista: objetivos, motivaciones, defectos, miedos, conflicto interno, conflicto externo.
Antagonista: igual esquema reducido.
Condicionales: aliados/relaciones (si hay más de un personaje mencionado) · arcos previstos (siempre, es clave para Fase 5) · punto de vista y voz narrativa (siempre, condiciona directamente el agente Narrador de Fase 7).

### 3.5 Estructura narrativa (core)
Tipo de historia · final cerrado o abierto · nivel de planificación deseado (¿el usuario quiere planificar arcos completos de antemano o improvisar capítulo a capítulo dentro de un marco?).
Condicionales: número estimado de arcos y duración (si el nivel de planificación es alto) · misterios/revelaciones/progresión de poder/evolución de relaciones (se activan según lo que ya haya salido en Mundo/Personajes) · tipo de ganchos entre capítulos (siempre, es un requisito de formato para el escritor de escenas).

### 3.6 Identidad audiovisual (core)
Estilo visual · relación de aspecto · voz del narrador (idioma/acento/tono) · estilo musical.
Condicionales: nivel de movimiento, uso de estático/animado, iluminación, paleta, intensidad de SFX, estilo de subtítulos — se preguntan con una propuesta por defecto derivada del tono/género (sección 2), y el usuario aprueba o corrige en bloque en vez de responder una a una. Esto reduce fatiga de entrevista sin perder cobertura.

## 4. Persistencia y reanudación

Cada entrevista es una sesión con id propio, independiente de si la novela ya tiene `novel-id` asignado:

```
novels/<novel-id>/interview/
  session.yaml         # estado de la sesión: sección/pregunta actual, estado (en_curso/completa)
  transcript.jsonl      # log íntegro append-only: cada entrada = {timestamp, seccion, pregunta, respuesta}
  draft_answers.yaml    # respuestas estructuradas derivadas del transcript, por campo
```

- `transcript.jsonl` **nunca se edita ni se borra** — es el registro de auditoría de cómo se construyó el proyecto, tal como pide la Fase 4 del encargo original. Si el usuario corrige una respuesta más tarde, se añade una entrada nueva al transcript referenciando cuál corrige, no se reescribe la anterior.
- `session.yaml` guarda el puntero exacto (sección, índice de pregunta, condicionales ya resueltas) para que `resume-interview <novel-id>` continúe exactamente donde se dejó, incluso en otra sesión de Claude Code.
- `draft_answers.yaml` es lo que el agente usa para generar el paquete inicial — se puede regenerar en cualquier momento a partir del transcript, nunca es la fuente de verdad.

## 5. Paquete inicial generado al finalizar la entrevista

Al completar las 6 secciones, el agente genera el borrador dentro de `novels/<novel-id>/`, todo en estado **propuesto, no canon**:

| Elemento del encargo | Dónde se materializa |
|---|---|
| Identificador único | `novel-id` (slug), asignado al crear la sesión |
| Título provisional, descripción, premisa, sinopsis, público objetivo | `project.yaml` |
| Guía de tono | `canon/proposals/tone_guide.md` |
| Biblia inicial del mundo | `canon/proposals/world.md` (+ subcarpetas si aplica: facciones, poderes, historia) |
| Fichas iniciales de personajes | `characters/*.md` (borrador) |
| Reglas narrativas | `canon/proposals/narrative_rules.md` (ganchos, ritmo, nivel de planificación, tipo de final) |
| Guía visual | `canon/proposals/visual_guide.md` |
| Guía de voces | `canon/proposals/voice_guide.md` |
| Estructura inicial de arcos | `plots/arcs_outline.md` |
| Riesgos de coherencia | `reports/coherence_risks.md` — generado automáticamente: el agente señala explícitamente contradicciones o ambigüedades detectadas durante la propia entrevista (p. ej. "dijiste tono ligero pero nivel de violencia alto — confirmar que es intencional") |
| Preguntas todavía pendientes | `reports/open_questions.md` — todo lo que el usuario dejó sin resolver o pospuso |
| Configuración del pipeline | `project.yaml` (sección `pipeline:`) |
| Presupuesto inicial estimado | `project.yaml` (sección `budget:`), calculado a partir de duración de capítulo/vídeo y frecuencia declaradas |
| Archivos y directorios necesarios | se crean todos los directorios de la Fase 3 (`lore/`, `state/`, `timeline/`, `chapters/`, `assets/`, `voices/`, `production/`, `publishing/`) aunque estén vacíos, con un `.gitkeep` o README breve explicando su propósito |

Este paquete queda en estado de novela **Configuración inicial** (Fase 3).

## 6. Revisión y aprobación

El usuario recibe el paquete como un resumen navegable (no un volcado de 15 archivos sin más) y puede:
- Editar cualquier campo directamente en los archivos generados.
- Pedir al agente que regenere una sección concreta con instrucciones nuevas.
- Aprobar. Al aprobar: todo `canon/proposals/*` se mueve a `canon/approved/` con fecha y referencia a la sesión de entrevista que lo originó (trazabilidad exigida por la Fase 7: ningún cambio de canon sin propuesta→revisión→aprobación, ni siquiera el primero). El estado de la novela pasa de **Configuración inicial** a **Preproducción**.

Nada pasa a canon solo por haber terminado la entrevista — la aprobación es un paso explícito y separado, igual que cualquier otro cambio de canon posterior.

## 7. Operaciones auxiliares

- **`resume-interview <novel-id>`** — carga `session.yaml` y continúa desde el puntero guardado.
- **`modify-novel <novel-id>`** — no edita el canon directamente: abre una entrevista corta y dirigida ("¿qué quieres cambiar?") cuyo resultado entra como una propuesta nueva en `canon/proposals/`, sujeta al mismo flujo de aprobación de la Fase 7. Evita cambios de canon silenciosos.
- **`clone-novel <source-id> <new-id>`** — copia `project.yaml`, `canon/approved/`, `characters/`, `voices/` (config, no muestras de audio) como punto de partida; resetea `state/`, `chapters/`, `production/`, `publishing/` a vacío; registra `cloned_from: <source-id>` en `project.yaml`.
- **`create-variant <source-id> <variant-id>`** — igual que clone, pero mantiene un vínculo explícito y visible de linaje (`variant_of: <source-id>`) pensado para spin-offs o líneas temporales alternativas que el usuario quiere tratar como universo propio pero relacionado.
- **`import-lore <novel-id> --source <ruta>`** — ingiere material externo (markdown, texto plano) como una propuesta en `canon/proposals/imported/`, nunca directo a `canon/approved/`; pasa por el mismo control de calidad/coherencia que cualquier otra propuesta antes de aceptarse.
- **`export-bible <novel-id>`** — compila `canon/approved/` en un único documento legible (Markdown o PDF) para consulta externa o respaldo.
- **`archive-novel <novel-id>`** — transición de estado a **Archivada** (Fase 3); no borra nada; opcionalmente comprime `production/*/video` y `production/*/audio` a almacenamiento frío si el usuario lo pide explícitamente.

## 8. Qué valida esto de la causa raíz del proyecto anterior

- El transcript append-only + `canon/proposals` vs `canon/approved` cierra directamente el hueco que causó la biblia duplicada y contradictoria del proyecto anterior: ahora es estructuralmente imposible que algo llegue a canon sin pasar por una aprobación registrada.
- Los "riesgos de coherencia" detectados al final de la entrevista son el primer punto de control de continuidad del sistema — antes incluso de escribir el primer capítulo, no después de detectar el problema en el capítulo 20.
