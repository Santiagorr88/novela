# Arquitectura de workspace multi-novela

Fecha: 2026-08-06
Estado: propuesta para revisión del usuario

## 1. Principio de diseño

Separar estrictamente cinco cosas que en el proyecto anterior estaban mezcladas (ver [reports/01_repo_audit.md](01_repo_audit.md), puntos 3 y 5): **código**, **configuración**, **prompts**, **datos narrativos por novela** y **artefactos de producción por novela**. Cada novela es un directorio autocontenido; nada narrativo vive fuera de `novels/<id>/`. El código de la plataforma nunca contiene datos de una novela concreta.

No se adopta la estructura propuesta por el usuario tal cual, se ajusta en tres puntos, justificados abajo:
1. Se separa `canon/` de `lore/`: `lore/` es material de worldbuilding en bruto (pueden ser ideas o ensayos), `canon/` es lo confirmado y versionado que los agentes pueden citar como verdad. Confundir ambos fue una causa directa de la falta de coherencia en el proyecto anterior (biblia duplicada sin fuente única de verdad).
2. Se añade `state/` como única fuente de verdad del estado narrativo actual (personajes vivos/muertos, ubicación de objetos, relaciones) — en el proyecto anterior este estado estaba duplicado en dos rutas distintas con datos contradictorios; aquí se fuerza a que solo pueda existir un `state/current.json` por novela.
3. Se añade `production/<chapter-id>/` en vez de carpetas globales `storyboards/`, `visual-assets/`, `audio/`, `subtitles/`, `videos/` sueltas a nivel de novela — cada capítulo agrupa sus propios artefactos de producción, lo que hace trivial reanudar el pipeline de un capítulo concreto sin tocar los demás (requisito explícito de la Fase 8). Los recursos verdaderamente reutilizables entre capítulos (fichas visuales de personajes, registro de voces) sí quedan a nivel de novela, en `assets/` y `voices/`, porque deben ser estables a través de todos los capítulos.

## 2. Estructura propuesta

```
novelas/                          # raíz del repo (ya movida aquí)
  platform/                       # código compartido, sin datos de ninguna novela
    agents/                       # definiciones de agentes narrativos y de producción (Fase 7)
    engine/                       # motor de flujo (sustituye/depura src/flow_engine.py actual)
    tools/                        # wrappers de proveedores: LLM, TTS, imagen, FFmpeg
    validators/                   # validadores de continuidad, lógica, ritmo (Fase 6)
    prompts/                      # prompts versionados de los agentes (una sola copia por rol)
    cli/                          # create-novel y demás comandos guiados (Fase 4)
  novels/
    <novel-id>/
      project.yaml                # identidad, estado del ciclo de vida, config de pipeline y presupuesto
      interview/                  # transcripción íntegra de la entrevista de creación (auditable)
      lore/                       # worldbuilding en bruto: propuestas, ideas, borradores
      canon/                      # confirmado y versionado: mundo, personajes, localizaciones, reglas, poderes
        proposals/                # cambios de canon propuestos, pendientes de aprobación
        approved/                 # historial de cambios ya aprobados (append-only)
      state/
        current.json              # ÚNICA fuente de verdad del estado actual (fuente única, no duplicar)
        history/                  # snapshots por capítulo, para auditar cómo evolucionó el estado
      timeline/                   # cronología global y por personaje
      plots/                      # trama principal, subtramas, arcos, misterios/pistas/promesas
      characters/                 # fichas narrativas (no confundir con fichas visuales, que van en assets/)
      chapters/
        drafts/                   # en escritura/revisión
        approved/                 # texto final aprobado, versionado
      assets/                     # fichas visuales persistentes (Fase 9): personajes, localizaciones, objetos
      voices/                     # registro de voces persistente (Fase 10): narrador + personajes
      production/
        <chapter-id>/
          script/                 # adaptación a narración oral, narrador/diálogos separados
          storyboard/
          images/
          audio/
          subtitles/
          video/
          artifact_manifest.json  # id, versión, estado, coste, dependencias, aprobación (Fase 8)
      publishing/                 # metadatos y estado de publicación por plataforma
      reports/                    # informes de calidad por capítulo (Fase de revisión)
  config/
    budgets.yaml                  # presupuestos por entorno: desarrollo/pruebas/producción/regeneración/publicación
    providers.yaml                # qué proveedor usa cada capacidad (LLM, TTS, imagen) — sin credenciales
  reports/                        # informes a nivel de plataforma (este mismo directorio, ya en uso)
  .env                            # credenciales locales, nunca versionado (ya en .gitignore)
```

## 3. Por qué archivos estructurados + Git alcanzan para el MVP

- Cada entidad de canon (personaje, localización, regla) es un archivo Markdown/YAML con front-matter versionable por Git; el historial de Git ya da control de versiones y auditoría de quién cambió qué y cuándo, sin montar una base de datos.
- La recuperación de contexto "solo lo relevante" (Fase 6) se resuelve en el MVP con filtros deterministas (por `novel_id`, personaje, localización, arco) sobre estos archivos — no requiere embeddings todavía. Se deja documentado como próxima iteración si el volumen de canon crece lo suficiente para que el filtrado por metadatos deje de bastar.
- `artifact_manifest.json` por capítulo cubre el registro de coste/versión/estado que pedía la Fase 8, sin necesitar una tabla ni un servicio aparte.
- Una cola de tareas o servicio externo solo se justificaría si la producción se paraleliza a gran escala; fuera de alcance del MVP y de esta fase.

## 4. Migración desde el estado actual

No se ejecuta en esta fase (es diseño, no implementación — eso corresponde al plan de Fase 13). Cuando se implemente:
- `src/lore/` y `content/lore/` (hoy duplicados idénticos) se consolidan en `novels/<id>/lore/` y `novels/<id>/canon/`, eligiendo una única copia como origen.
- `output/state.json` y `data/state/state.json` (hoy contradictorios) se reconcilian manualmente una vez y de ahí en adelante solo existe `novels/<id>/state/current.json`.
- Los prompts duplicados en `src/agents/` (identificados en el informe de auditoría) se reducen a una versión por rol en `platform/prompts/`, y las versiones descartadas se eliminan, no se archivan indefinidamente.
- El código Python reutilizable (`chapter_assembler.py`, `export_pdf.py`, etc.) se audita función por función antes de moverse a `platform/`; nada se migra solo porque ya existía.

## 5. Novela de prueba para el MVP

Para no arrastrar el lore real de la saga anterior (con sus inconsistencias ya documentadas) al validar el pipeline nuevo, el MVP usa una **novela de prueba mínima y desechable** (`novels/_mvp-test/`), con un mundo trivial y 1 capítulo corto, pensada solo para probar que el flujo completo funciona de punta a punta. La novela real se retoma después, ya sobre la plataforma validada.
