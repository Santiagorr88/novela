# Agentes narrativos y de producción (Fase 7)

Fecha: 2026-08-06
Estado: propuesta para revisión del usuario (diseño, no implementación)

## Criterio de consolidación

El encargo original lista 19 responsabilidades posibles. Consolido a **13 agentes**, fusionando las que comparten entrada/salida y solo se diferencian en granularidad o en ser pasadas secuenciales sobre el mismo artefacto (p. ej. editor de diálogos y editor de estilo son dos pasadas de edición sobre el mismo borrador, no dos roles con entradas distintas). Mantengo separados los que difieren en el **tipo de dato que consumen** (prosa vs. datos estructurados), porque mezclarlos fue parte del problema original: el revisor de continuidad anterior intentaba leer prosa libre con regex en vez de datos estructurados.

## Roster — lado narrativo

### 1. Director creativo
- **Responsabilidad**: conduce la entrevista `create-novel`, media decisiones creativas ambiguas, es el único agente que interactúa directamente con el usuario en fase de diseño.
- **Entradas**: respuestas de entrevista, canon existente (si aplica, en `modify-novel`).
- **Salidas**: paquete inicial (Fase 4), decisiones creativas registradas.
- **Herramientas**: lectura/escritura en `interview/`, `canon/proposals/`. Sin acceso a `canon/approved/` en escritura.
- **Criterios de aceptación**: cobertura completa del banco de preguntas (Fase 4); riesgos de coherencia detectados y listados.
- **Restricciones**: no escribe canon aprobado directamente.
- **Recuperación de errores**: si el usuario abandona la entrevista, el estado queda en `session.yaml` (resumible); no hay estado a medias en canon.

### 2. Arquitecto de mundo y personajes
- **Responsabilidad**: desarrolla la biblia del mundo y las fichas de personajes a partir de la premisa aprobada.
- **Entradas**: `project.yaml`, `canon/approved/tone_guide.md`.
- **Salidas**: `canon/proposals/world.md`, `characters/*.md` (borrador).
- **Herramientas**: lectura de canon aprobado, escritura solo en `proposals/`.
- **Criterios de aceptación**: cada regla de mundo/poder declarada es verificable (no ambigua); cada personaje tiene motivación, defecto y conflicto explícitos (nunca solo descripción física).
- **Restricciones**: no puede introducir reglas que contradigan `canon/approved/` existente sin marcarlo explícitamente como cambio de canon (no como añadido nuevo).
- **Recuperación**: si el revisor de continuidad rechaza una regla por contradicción, vuelve a este agente con la evidencia concreta, no se descarta en silencio.

### 3. Planificador narrativo
- **Responsabilidad**: estructura arcos y planifica capítulos (beats, gancho de apertura/cierre, qué misterios/pistas se introducen o resuelven, POV).
- **Entradas**: canon aprobado, `plots/promises.yaml` (para saber qué hay pendiente de resolver), resumen del arco anterior.
- **Salidas**: `plots/arcs_outline.md`, plan de capítulo individual (`chapters/drafts/<id>/plan.yaml`).
- **Herramientas**: lectura de canon + resúmenes estructurados (Fase 6, A.3); no lee prosa completa de capítulos salvo que lo pida explícitamente.
- **Criterios de aceptación**: todo plan de capítulo declara gancho de cierre y al menos una conexión con una promesa narrativa abierta o el arco en curso.
- **Restricciones**: no puede cerrar una promesa narrativa sin que el plan explicite cómo.
- **Recuperación**: si el crítico narrativo marca el ritmo como plano, este agente replanifica antes de que el escritor de escenas empiece.

### 4. Escritor de escenas
- **Responsabilidad**: redacta la prosa del capítulo a partir del plan y el contexto recuperado (Fase 6, B.2).
- **Entradas**: plan de capítulo, contexto filtrado (personajes/localización/tiempo/arco), `state/knowledge/<character-id>.yaml` (qué sabe cada personaje en escena).
- **Salidas**: `chapters/drafts/<id>/draft_v<n>.md`.
- **Herramientas**: solo lectura del contexto ya filtrado — deliberadamente **no** tiene acceso de lectura libre a todo `canon/`, para forzar que use el mecanismo de recuperación (y que sea auditable qué vio y qué no).
- **Criterios de aceptación**: la escena cubre el plan; ningún personaje actúa con información que `state/knowledge/` no le atribuye.
- **Restricciones**: no decide trama nueva no planificada; si necesita desviarse del plan, lo señala en vez de improvisar en silencio.
- **Recuperación**: reintento con feedback específico del editor/revisor, no regeneración ciega desde cero.

### 5. Editor (estilo y diálogo)
- **Responsabilidad**: pasadas de pulido — naturalidad de diálogo, repeticiones léxicas, ritmo de frase, voz narrativa consistente con la guía de tono.
- **Entradas**: borrador del escritor de escenas, guía de tono/voz narrativa.
- **Salidas**: `draft_v<n+1>.md` con cambios trazables (diff, no sobrescritura ciega).
- **Restricciones**: no cambia trama ni hechos — solo forma. Si detecta que arreglar la forma requeriría cambiar un hecho, lo devuelve al escritor de escenas en vez de decidir por su cuenta.
- **Recuperación**: si el crítico narrativo sigue marcando diálogo poco natural tras esta pasada, se añade el ejemplo concreto al prompt del editor como caso a evitar (aprendizaje por instrucción explícita, no automático).

### 6. Revisor narrativo (lógica, ritmo, crítica)
- **Responsabilidad**: evalúa el borrador editado contra criterios de calidad narrativa: lógica de escena, ritmo, exposición excesiva, claridad, calidad del gancho, resolución de escenas.
- **Entradas**: borrador editado, plan de capítulo, resumen del arco.
- **Salidas**: veredicto pass/fail por criterio + evidencia concreta (no "no me convence" sin más) + corrección propuesta.
- **Restricciones**: no edita el texto directamente, solo evalúa — separación deliberada entre quien escribe/edita y quien audita, para que la crítica no se autoapruebe.
- **Recuperación**: fallo → vuelve al escritor de escenas o al editor según la naturaleza del fallo (trama vs. forma).

### 7. Revisor de continuidad
- **Responsabilidad**: ejecuta los validadores estructurados de la Fase 6, Parte C (personajes en lugares imposibles, errores temporales, información indebida, objetos, cambios físicos, poderes, relaciones, personalidad, tramas olvidadas, repeticiones, resurrecciones).
- **Entradas**: resumen estructurado del capítulo, `state/current.json`, `canon/approved/`, `state/knowledge/`.
- **Salidas**: entradas en `reports/continuity_log.yaml`, con evidencia y propuesta de corrección.
- **Restricciones**: opera solo sobre datos estructurados, nunca sobre heurísticas de texto libre (la causa raíz del fallo del sistema anterior) — si un chequeo requiere criterio narrativo en vez de un hecho verificable, ese chequeo pertenece al Revisor narrativo, no a este agente.
- **Recuperación**: cualquier fallo bloquea la aprobación del capítulo (no hay aprobación parcial).

### 8. Responsable del canon
- **Responsabilidad**: único agente con permiso de escritura en `canon/approved/`. Aplica el flujo de propuesta → revisión → aprobación (sección "Control de canon" más abajo).
- **Entradas**: propuestas en `canon/proposals/`, veredictos de los revisores, aprobación explícita del usuario.
- **Salidas**: commit de canon aprobado, con referencia a la propuesta y la aprobación que lo originó.
- **Restricciones**: no propone contenido propio — es un gate, no un creador.
- **Recuperación**: propuestas rechazadas quedan archivadas en `canon/proposals/rejected/` con el motivo, nunca se borran (auditoría).

## Roster — lado audiovisual (Fase 8-10)

### 9. Adaptador audiovisual
- **Responsabilidad**: convierte el capítulo aprobado en guion de narración oral — separa narrador/diálogo, ajusta frases para lectura en voz alta, marca pausas e interpretación.
- **Entradas**: `chapters/approved/<id>/text.md`.
- **Salidas**: `production/<id>/script/narration_script.yaml` (segmentos con hablante, texto, indicaciones de interpretación).
- **Criterios de aceptación**: cada segmento tiene un hablante único asignado; duración estimada calculada.

### 10. Director de storyboard
- **Responsabilidad**: divide el guion en escenas y planos, genera prompts visuales por plano, calcula duración estimada.
- **Entradas**: guion de narración, fichas visuales de personajes/localizaciones (Fase 9).
- **Salidas**: `production/<id>/storyboard/shots.yaml` (por plano: descripción, prompt visual, prompt negativo, duración estimada, referencias de personaje/localización usadas).
- **Restricciones**: todo prompt visual de un personaje/localización recurrente debe referenciar su ficha (Fase 9), no inventar descripción libre cada vez — es la garantía de consistencia visual.

### 11. Supervisor visual
- **Responsabilidad**: valida que las imágenes generadas respeten la ficha visual del personaje/localización antes de aprobarlas; detecta desviaciones relevantes.
- **Entradas**: imagen generada, ficha visual de referencia.
- **Salidas**: aprobación o solicitud de regeneración con motivo concreto.
- **Restricciones**: no genera imágenes, solo evalúa — mismo principio de separación que el Revisor narrativo.

### 12. Director de voces
- **Responsabilidad**: mantiene el registro de voces (Fase 10), genera audio de narrador y personajes, aplica diccionario de pronunciación, valida consistencia de voz entre capítulos.
- **Entradas**: guion de narración, `voices/registry.yaml`.
- **Salidas**: `production/<id>/audio/*.wav` (o formato equivalente) + actualización de `voices/registry.yaml` si es la primera vez que habla un personaje nuevo (requiere aprobación del usuario antes de fijar una voz nueva como definitiva).
- **Restricciones**: nunca asigna una voz nueva a un personaje que ya tiene una asignada sin aprobación explícita — la estabilidad de voz es el requisito, no una sugerencia.

### 13. Supervisor de producción
- **Responsabilidad**: orquesta el pipeline audiovisual completo (los 23 pasos de la Fase 8), gestiona reanudación, coste, reintentos, montaje final y exportación.
- **Entradas**: estado de `artifact_manifest.json` por capítulo.
- **Salidas**: vídeo exportado, miniatura, metadatos, coste total registrado.
- **Restricciones**: no regenera un artefacto ya aprobado salvo que sus dependencias hayan cambiado (comparación de hash/versión, no regeneración ciega).
- **Recuperación**: reintento acotado por paso (no reinicia el pipeline completo ante un fallo puntual); tras N reintentos fallidos, marca el paso como bloqueado y notifica en vez de generar un artefacto de baja calidad silenciosamente.

## Control de canon: propuesta → revisión → aprobación

Esto es lo que responde directamente al requisito de evitar modificaciones concurrentes sin control:

1. **Solo se escribe en `canon/proposals/`**, nunca se edita `canon/approved/` in-place. Cada propuesta es un archivo nuevo, versionado, que referencia explícitamente sobre qué versión de canon se basa (`based_on_version:` en el front-matter).
2. **Índice de propuestas pendientes** por entidad (`canon/proposals/_index.yaml`): antes de escribir una propuesta sobre una entidad (p. ej. un personaje concreto), cualquier agente consulta el índice; si ya hay una propuesta pendiente sobre esa misma entidad, la nueva se marca como **conflicto a resolver** en vez de coexistir en silencio con la primera.
3. **Concurrencia optimista**: si `canon/approved/` avanzó desde que se creó la propuesta (`based_on_version` desactualizado), el Responsable del canon la marca como obsoleta y la devuelve para rebase antes de poder aprobarla.
4. **Aprobación siempre humana**: ningún capítulo ni cambio de canon se marca aprobado solo porque todos los revisores automáticos pasaron — es condición necesaria, no suficiente. El usuario aprueba explícitamente (Fase 3-4).
5. **Nada se sobrescribe**: propuestas rechazadas y canon superado se conservan con su historial (Git ya da esto gratis si cada propuesta/aprobación es un commit).

## Qué agentes NO se crean (y por qué)

No hay un agente por cada validador individual de continuidad (uno para localización, otro para tiempo, etc.) — son funciones dentro del Revisor de continuidad, porque comparten entrada (resumen estructurado + estado) y no se benefician de ser agentes separados, solo añadirían coordinación sin valor. Tampoco se separan editor de diálogo y editor de estilo, ni Arquitecto de la historia/Diseñador del mundo/Diseñador de personajes en tres agentes — mismo motivo.
