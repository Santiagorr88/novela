# Arquitectura narrativa, memoria persistente y canon (Fases 5-6)

Fecha: 2026-08-06
Estado: propuesta para revisión del usuario (diseño, no implementación)

## Parte A — Arquitectura narrativa

### A.1 Jerarquía estructural

```
Novela
  └─ Temporada/Libro (opcional, solo si el usuario lo declaró en la entrevista)
       └─ Saga (opcional)
            └─ Arco
                 └─ Capítulo
                      └─ Escena
```

No todos los niveles son obligatorios — una novela corta puede tener solo Arco→Capítulo→Escena. El nivel de estructura se fija en la entrevista (`create-novel`, sección Estructura narrativa) y queda en `project.yaml`. Cada nivel tiene su propio resumen estructurado (ver A.3), de forma que un agente que planifica el capítulo 40 puede leer "resumen del arco" sin tener que leer los 39 capítulos anteriores completos.

### A.2 Elementos que vive cada nivel

| Elemento | Vive en | Ejemplo de campo |
|---|---|---|
| Premisa, género, tono, temas, público | Novela (`project.yaml`, `canon/approved/tone_guide.md`) | fijado en la entrevista, cambia rara vez |
| Trama principal | Novela/Saga (`plots/main.md`) | objetivo global, antagonista global |
| Subtramas | Arco (`plots/subplots/<id>.md`) | estado: activa / resuelta / abandonada (nunca "desaparecida" sin más) |
| Arcos de personaje | Personaje, referenciado desde Arco (`characters/<id>.md#arc`) | punto de partida, punto de llegada, capítulos clave |
| Ritmo narrativo | Arco | curva de tensión declarada por capítulo (baja/media/alta/clímax) |
| Ganchos iniciales/finales | Capítulo | gancho de apertura, gancho de cierre — campo obligatorio del plan de capítulo |
| Misterios, pistas, promesas, revelaciones | Novela, con estado por elemento | ver A.4 |
| Evolución de relaciones/habilidades/mundo | `state/history/` (snapshots por capítulo) | ver Parte B |

### A.3 Resúmenes estructurados (no prosa libre)

Cada capítulo aprobado genera un resumen estructurado (JSON/YAML, no un párrafo de texto libre) con: eventos ocurridos, personajes presentes, localización(es), objetos que cambiaron de estado, información revelada (y a quién), tiempo transcurrido desde el capítulo anterior, gancho de cierre. Este resumen — no el texto completo del capítulo — es lo que normalmente se recupera al planificar capítulos futuros (ver B.2). El texto completo solo se recupera cuando el filtro de recuperación determina que hace falta detalle literal (p. ej. para mantener la voz de un diálogo específico).

Esto es la corrección directa del problema identificado en la auditoría: la memoria anterior truncaba texto libre por número de caracteres; aquí se recupera por campos estructurados, así que "olvidar" un capítulo antiguo nunca significa perder un hecho canónico, como mucho significa no recuperar la prosa literal.

### A.4 Registro de promesas narrativas

Todo misterio, pista o promesa introducida se registra explícitamente en `plots/promises.yaml` en el momento en que se introduce (no se reconstruye a posteriori): `{id, tipo: misterio|pista|promesa, introducido_en: capítulo, estado: abierto|parcial|resuelto, capítulo_resolución, notas}`. El revisor narrativo (Fase 7) puede así detectar promesas abiertas hace 30 capítulos sin resolver, en vez de depender de que alguien se acuerde. Esto ataca directamente "tramas abandonadas", uno de los problemas reportados originalmente.

## Parte B — Memoria persistente y canon

### B.1 Qué se guarda (mapeado a la estructura de la Fase 3)

Biblia del mundo, biblia de personajes, cronología global y por personaje, registro de eventos, relaciones, localizaciones, facciones, objetos relevantes, reglas del mundo/sistema de poderes → `canon/approved/`, cada entidad en su propio archivo versionado por Git.
Estado actual de cada personaje, registro de muertes/heridas/cambios → `state/current.json` (única fuente de verdad) + `state/history/<chapter-id>.json` (snapshot inmutable tras cada capítulo aprobado).
Resumen estructurado de cada capítulo/escena, hechos canónicos → `chapters/approved/<id>/summary.yaml`.
Misterios abiertos, promesas pendientes, conflictos activos, pistas → `plots/promises.yaml`, `plots/conflicts.yaml`.
Información conocida por cada personaje → `state/knowledge/<character-id>.yaml` (ver B.4).
Registro de contradicciones, historial de revisiones → `reports/continuity_log.yaml` (ver B.5).

### B.2 Recuperación de contexto — qué se envía al modelo y por qué

Antes de escribir una escena, el sistema nunca envía la novela completa. El proceso de recuperación:

1. **Filtro por identidad**: `novel_id` obligatorio en toda consulta — aislamiento estricto entre novelas (ver Fase 3, sección 6).
2. **Filtro por personajes presentes** en la escena a escribir: se recupera `characters/<id>.md`, `state/current.json` (solo las entradas de esos personajes) y `state/knowledge/<id>.yaml` de cada uno.
3. **Filtro por localización**: ficha de la localización + eventos previos registrados ahí.
4. **Filtro temporal**: solo eventos/estado hasta el punto temporal de la escena — crítico para evitar que un agente use información "del futuro" de la trama (p. ej. en flashbacks o líneas temporales paralelas).
5. **Filtro por arco**: resumen del arco actual + resumen del arco anterior si hay continuidad directa; no se traen arcos no relacionados.
6. **Priorización del canon**: `canon/approved/` siempre tiene prioridad sobre `canon/proposals/` o `lore/` en caso de conflicto; si hay conflicto detectado entre fuentes, se marca como riesgo de coherencia en vez de resolverse silenciosamente a favor de una.
7. **Recuperación semántica** (embeddings) se reserva para cuando el volumen de canon aprobado supere lo que los filtros deterministas (1-6) puedan acotar razonablemente — no se introduce en el MVP (ver Fase 3, sección 3). Cuando se active, se usa **solo como ranking dentro del subconjunto ya filtrado** por metadatos, nunca como sustituto del filtrado — así nunca puede "traer" contenido de una novela o arco equivocado por similitud semántica.
8. **Control de versiones**: cada elemento recuperado incluye su versión/commit de origen.
9. **Identificación de fuente**: cada elemento recuperado se etiqueta con su ruta de archivo exacta.
10. **Registro de por qué se recuperó**: cada consulta de recuperación escribe un log corto (`reports/retrieval_log/<scene-id>.yaml`) con qué filtros se aplicaron y qué se recuperó — permite auditar por qué un agente "no supo" algo que sí estaba en el canon (bug de recuperación) vs. por qué inventó algo que contradice el canon (bug de generación) — son problemas distintos y esto los distingue.

### B.3 Separación de capas de contenido

| Capa | Dónde vive | Quién puede promoverla a la siguiente |
|---|---|---|
| Ideas propuestas | `lore/` | Usuario o agente, libremente |
| Planes futuros | `plots/*.md` (sección "planeado, no escrito") | Planificador de arcos/capítulos |
| Borradores | `chapters/drafts/` | Escritor de escenas |
| Contenido aprobado | `chapters/approved/` | Usuario (aprobación explícita) |
| Canon confirmado | `canon/approved/` | Usuario, vía flujo de propuesta→revisión (Fase 7) |
| Contenido descartado | `chapters/discarded/` (no se borra, se mueve) | Usuario |

Ninguna capa se salta pasos: un borrador no puede convertirse en canon sin pasar por aprobado; una idea no puede convertirse en canon sin pasar por propuesta revisada.

### B.4 Secretos e información asimétrica

Este es el punto que más directamente ataca "personajes que saben algo que no deberían" y "diálogos poco naturales" (un personaje que habla como si supiera todo el lore es poco natural):

- `state/knowledge/<character-id>.yaml`: lista de hechos que ese personaje concretamente conoce, con el capítulo en que lo aprendió y la fuente narrativa (cómo lo aprendió).
- Campo `creencia_falsa`: hechos que el personaje **cree** ciertos pero que el canon real contradice (p. ej. cree que su hermano está muerto). El escritor de escenas debe usar `state/knowledge/`, no `canon/approved/`, para decidir qué puede saber o decir un personaje en una escena — son fuentes distintas a propósito.
- `canon/approved/secrets.yaml`: secretos con dos niveles de visibilidad — `para_lector` (el lector no lo sabe todavía, pero el narrador en tercera persona omnisciente sí podría) y `para_personajes` (lista de qué personajes lo conocen). El validador de continuidad (Parte C) puede así detectar automáticamente si una escena hace que un personaje revele o actúe sobre información que, según `state/knowledge/`, no debería tener.

### B.5 Validadores de continuidad

Cada validador corre sobre el resumen estructurado del capítulo (A.3) más el estado antes/después (B.1), no releyendo prosa libre con regex como en el proyecto anterior — la implementación usa un agente revisor (LLM-as-judge) con acceso exclusivamente a los campos estructurados relevantes, comparando contra `state/current.json` y `canon/approved/`:

- Personajes en lugares imposibles → compara localización declarada en el resumen del capítulo contra la última localización conocida y el tiempo transcurrido.
- Errores temporales → compara `timeline/` contra las fechas/duraciones declaradas en el resumen del capítulo.
- Información que un personaje no debería conocer → compara diálogo/acciones del personaje contra `state/knowledge/<id>.yaml`.
- Objetos duplicados o desaparecidos → compara el registro de objetos en `state/current.json` antes/después del capítulo.
- Cambios físicos injustificados → compara ficha de personaje (rasgos físicos, Fase 9) contra cualquier cambio no declarado como evento canónico.
- Poderes usados fuera de sus reglas → compara la acción contra `canon/approved/power_system.md`.
- Relaciones contradictorias → compara el estado de relación declarado en la escena contra `state/current.json`.
- Personalidades inconsistentes → compara tono/decisiones del personaje en la escena contra su ficha (`characters/<id>.md`, incluyendo motivaciones/miedos/defectos) — este es el chequeo que ataca directamente "cambios injustificados en la personalidad" del problema original.
- Tramas olvidadas → cruza `plots/promises.yaml` contra capítulos transcurridos sin actividad relacionada, con umbral configurable de aviso.
- Repetición de acontecimientos → compara el resumen estructurado del capítulo actual contra resúmenes previos del mismo arco (eventos, no solo texto).
- Resurrecciones o cambios de estado no explicados → compara `state/current.json` (p. ej. `vivo: false`) contra cualquier acción posterior del personaje sin un evento canónico que lo explique.

Cada fallo de validador genera una entrada en `reports/continuity_log.yaml` con: qué falló, evidencia (qué campos concretos entraron en conflicto), y una propuesta de corrección — nunca se aprueba el capítulo automáticamente si un validador falla (ver Fase 7, flujo de aprobación).

## Por qué esto no es sobre-ingeniería para el MVP

Todo lo anterior son archivos estructurados (YAML/JSON/Markdown) + un agente que los lee con filtros deterministas. No hay base de datos, no hay motor vectorial en el MVP — se activa recuperación semántica solo si el volumen lo justifica más adelante, y ya está diseñado el punto exacto donde se conectaría sin rehacer el resto (ranking dentro del subconjunto filtrado, nunca sustituyendo el filtrado).
