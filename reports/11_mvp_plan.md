# Plan de implementación del MVP (Fase 13)

Fecha: 2026-08-06
Nota: no hay un comando `/autoplan` instalado en este entorno de Claude Code (no aparece en las skills disponibles de la sesión). Este plan reproduce manualmente el mismo objetivo — fases pequeñas, verificables, ordenadas por dependencias — incorporando el veredicto del Council ([reports/10_council_transcript.md](10_council_transcript.md)): se antepone un **Paso 0 manual sin agentes** a la construcción de cualquier automatización, con un criterio de abandono explícito antes de seguir.

Clasificación usada: **MVP** (imprescindible para el flujo mínimo), **Posterior al MVP**, **Opcional**, **Investigación**, **Deuda técnica**.

---

## Grupo 0 — Cierre de seguridad pendiente (MVP, bloqueante)

### T0.1 — Force-push del historial limpio y rotación de la API key
- **Objetivo**: eliminar la API key filtrada también del remoto, no solo del repo local.
- **Justificación**: la Fase 1 purgó el historial local; el remoto público sigue teniendo la clave hasta que el usuario haga push. La clave sigue siendo válida hasta que se rote en Google Cloud Console.
- **Prioridad**: crítica, bloqueante para cualquier trabajo público posterior.
- **Dependencias**: ninguna (ya ejecutado localmente en Fase 1).
- **Archivos afectados**: ninguno nuevo (ya hecho: `.gitignore`, purga de historial).
- **Componentes**: repositorio Git, Google Cloud Console.
- **Entradas**: comandos ya proporcionados al usuario en el cierre de Fase 1.
- **Salidas**: historial remoto limpio, clave rotada.
- **Pruebas**: `git log origin/main -- src/secrets.json` vacío tras el push; la clave antigua responde con error de autenticación tras rotarla.
- **Criterios de aceptación**: ambos confirmados por el usuario.
- **Riesgos**: si no se rota la clave, sigue siendo explotable por cualquiera que ya la haya visto/scrapeado antes de la purga.
- **Costes externos**: ninguno.
- **Reversión**: N/A (acción del usuario, fuera de mi ejecución).
- **Estado esperado al finalizar**: repo remoto sin secretos en el historial; clave antigua inválida.

---

## Grupo 1 — Paso 0: validación manual sin agentes (MVP, gate obligatorio)

### T1.1 — Escribir a mano un capítulo corto de la novela de prueba
- **Objetivo**: confirmar que existe una historia mínimamente viable y que el operador puede producirla sin fricción insostenible.
- **Justificación**: veredicto del Council — ningún pipeline arregla la ausencia de una novela que alguien quiera leer.
- **Prioridad**: máxima, primer paso real del proyecto.
- **Dependencias**: T0.1 no bloquea esto (puede hacerse en paralelo).
- **Archivos afectados**: `novels/_mvp-test/chapters/approved/ch01.md` (creación manual del directorio mínimo).
- **Componentes**: ninguno de plataforma — solo el operador escribiendo.
- **Entradas**: premisa mínima (puede definirse en el momento, no requiere la entrevista completa de Fase 4 todavía).
- **Salidas**: un capítulo corto en Markdown.
- **Pruebas**: el propio operador lo relee y decide si lo aprobaría como si fuera de otro autor.
- **Criterios de aceptación**: capítulo terminado en un tiempo razonable (objetivo: mismo día), el operador lo aprobaría.
- **Riesgos**: si esto ya es difícil o no genera satisfacción, es la señal de abandono más temprana y barata posible.
- **Costes externos**: ninguno (o coste mínimo de LLM si se usa de apoyo puntual, sin agente formal).
- **Reversión**: descartar y reintentar con otra premisa, sin coste hundido relevante.
- **Estado esperado al finalizar**: 1 capítulo aprobado manualmente.

### T1.2 — Producir el vídeo de ese capítulo completamente a mano
- **Objetivo**: validar el pipeline audiovisual paso a paso con herramientas directas, sin ninguna orquestación de agentes.
- **Justificación**: veredicto del Council (respuesta más votada) — revela fricción real y coste real antes de automatizar.
- **Prioridad**: máxima.
- **Dependencias**: T1.1.
- **Archivos afectados**: `novels/_mvp-test/production/ch01/*` (creado manualmente).
- **Componentes**: ElevenLabs (vía MCP oficial, T-por-definir en Grupo 2), un proveedor de imagen reference-based, FFmpeg en terminal.
- **Entradas**: capítulo de T1.1, adaptado a guion oral a mano.
- **Salidas**: vídeo final corto, subtítulos, coste real registrado a mano en una tabla simple.
- **Pruebas**: el vídeo se reproduce correctamente, audio/imagen/subtítulos sincronizados.
- **Criterios de aceptación**: vídeo terminado, tiempo total invertido y coste registrados.
- **Riesgos**: proceso tedioso puede revelar que el formato no es viable para un operador único sin automatización — información valiosa, no un fracaso del plan.
- **Costes externos**: crédito de ElevenLabs (tier gratuito probablemente suficiente para una prueba corta), coste de generación de imagen (2-6 imágenes), coste de cómputo LLM puntual.
- **Reversión**: ninguna necesaria, es un experimento aislado en `_mvp-test/`.
- **Estado esperado al finalizar**: vídeo corto exportado + registro de tiempo/coste por paso.

### T1.3 — Gate de decisión: ¿se automatiza o se para?
- **Objetivo**: aplicar el criterio de abandono explícito que el Council señaló como ausente.
- **Justificación**: evitar repetir el patrón del proyecto anterior (invertir en arquitectura sin verificar la premisa).
- **Prioridad**: máxima — bloquea todo el Grupo 2 en adelante.
- **Dependencias**: T1.1, T1.2.
- **Archivos afectados**: `reports/12_step0_verdict.md` (nuevo, a escribir tras el experimento).
- **Componentes**: ninguno técnico — decisión del usuario.
- **Entradas**: resultado y coste/tiempo de T1.1-T1.2.
- **Salidas**: decisión documentada: continuar / ajustar alcance / pausar.
- **Pruebas**: N/A.
- **Criterios de aceptación**: el usuario confirma explícitamente que quiere seguir antes de que se escriba código de ningún agente.
- **Riesgos**: seguir sin pasar este gate reproduce exactamente el patrón que el Council marcó como causa de riesgo.
- **Costes externos**: ninguno.
- **Reversión**: N/A.
- **Estado esperado al finalizar**: decisión explícita registrada.

---

## Grupo 2 — Fundaciones mínimas de plataforma (MVP, solo tras pasar T1.3)

### T2.1 — Estructura de carpetas mínima + `project.yaml` de la novela de prueba
- **Objetivo**: crear en código la estructura de la Fase 3, aplicada solo a `novels/_mvp-test/`.
- **Justificación**: base para que cualquier agente futuro tenga dónde leer/escribir.
- **Prioridad**: alta. **Dependencias**: T1.3 (aprobado).
- **Archivos afectados**: `novels/_mvp-test/**` (creación de directorios), `platform/` (esqueleto vacío).
- **Componentes**: ninguno externo.
- **Entradas**: diseño de Fase 3.
- **Salidas**: estructura de carpetas real, `project.yaml` con los datos ya conocidos del capítulo de prueba.
- **Pruebas**: script simple que valida que existen todas las carpetas esperadas.
- **Criterios de aceptación**: estructura creada, sin datos de la saga anterior mezclados.
- **Riesgos**: bajo. **Costes externos**: ninguno.
- **Reversión**: `rm -rf novels/_mvp-test` sin impacto (es descartable por diseño).
- **Estado esperado al finalizar**: workspace de novela de prueba operativo.

### T2.2 — Integración ElevenLabs vía MCP oficial
- **Objetivo**: conectar `elevenlabs/elevenlabs-mcp` (Fase 11) como la vía de TTS.
- **Justificación**: fuente oficial, evita reinventar wrapper (causa de deuda técnica anterior).
- **Prioridad**: alta. **Dependencias**: T2.1.
- **Archivos afectados**: `.env` (variable `ELEVENLABS_API_KEY`, nunca commiteada), `config/providers.yaml`.
- **Componentes**: servidor MCP de ElevenLabs.
- **Entradas**: API key del usuario (provista por él, nunca generada ni vista por el agente).
- **Salidas**: voz de prueba generada vía MCP, confirmando la integración.
- **Pruebas**: generación de un audio corto de prueba.
- **Criterios de aceptación**: audio generado, credenciales no aparecen en ningún archivo versionado.
- **Riesgos**: requiere autorización interactiva del usuario (`claude mcp add` / `/mcp`), no se puede completar en una sesión no interactiva.
- **Costes externos**: consumo de créditos de ElevenLabs (tier gratuito).
- **Reversión**: desconectar el servidor MCP, sin efectos colaterales.
- **Estado esperado al finalizar**: TTS operativo bajo demanda.

### T2.3 — Auditoría profunda de la skill de FFmpeg preferente
- **Objetivo**: pasar el checklist completo de la Fase 11 sobre `MastroMimmo/ffmpeg-skill` (candidato principal) antes de usarla.
- **Justificación**: restricción explícita del encargo — no ejecutar código comunitario sin revisar.
- **Prioridad**: alta. **Dependencias**: ninguna, puede ir en paralelo a T2.2.
- **Archivos afectados**: ninguno del repo (auditoría externa), `reports/13_skill_audit_ffmpeg.md` (nuevo).
- **Componentes**: el repositorio candidato.
- **Entradas**: checklist de la Fase 11.
- **Salidas**: veredicto de adopción o descarte, con motivo.
- **Pruebas**: ejecución manual en entorno aislado antes de integrar.
- **Criterios de aceptación**: checklist completo, sin hallazgos bloqueantes.
- **Riesgos**: código comunitario no mantenido o con permisos excesivos.
- **Costes externos**: ninguno.
- **Reversión**: descartar el candidato y pasar al siguiente de la lista de la Fase 11 sin impacto en lo demás.
- **Estado esperado al finalizar**: decisión de adopción documentada.

### T2.4 — Estimación de coste a escala (token/API a cientos de capítulos)
- **Objetivo**: cerrar el punto ciego señalado por el Council — proyectar coste real, no solo por capítulo de prueba.
- **Justificación**: sin esto, el presupuesto de la Fase 8/3 es teórico.
- **Prioridad**: alta. **Dependencias**: T1.2 (coste real de un capítulo).
- **Archivos afectados**: `reports/14_cost_projection.md` (nuevo), `config/budgets.yaml`.
- **Componentes**: ninguno técnico, cálculo con los datos ya obtenidos.
- **Entradas**: coste real medido en T1.2, frecuencia de publicación declarada.
- **Salidas**: proyección a 10/50/100 capítulos, con rangos.
- **Pruebas**: N/A.
- **Criterios de aceptación**: proyección revisada y aceptada por el usuario como presupuesto realista.
- **Riesgos**: si el coste proyectado es inasumible, hay que revisar alcance (menos voces, imágenes más baratas, capítulos más cortos) antes de seguir.
- **Costes externos**: ninguno (es solo cálculo).
- **Reversión**: N/A.
- **Estado esperado al finalizar**: presupuesto realista documentado.

---

## Grupo 3 — Primer agente real, mínimo (MVP)

### T3.1 — Un único agente: Revisor de continuidad, probado con un error insertado a propósito
- **Objetivo**: construir solo el agente que el Council identificó como el verdadero criterio de éxito ("¿detecta lo que le insertas?"), antes que cualquier otro.
- **Justificación**: es el punto exacto donde falló el proyecto anterior (validadores que no validaban nada) — se prueba primero y de forma aislada.
- **Prioridad**: máxima dentro de este grupo. **Dependencias**: T2.1, T2.4 (gate de presupuesto superado).
- **Archivos afectados**: `platform/validators/continuity.py` (o equivalente), `novels/_mvp-test/state/`.
- **Componentes**: 1 agente (Fase 7, agente 7), sin el resto del roster todavía.
- **Entradas**: resumen estructurado del capítulo de T1.1, `state/current.json` con un dato deliberadamente contradictorio insertado.
- **Salidas**: entrada en `reports/continuity_log.yaml` señalando la contradicción insertada.
- **Pruebas**: **prueba de falsabilidad explícita** — se inserta un error conocido (p. ej. un personaje en dos localizaciones a la vez) y se confirma que el validador lo detecta; si no lo detecta, no se avanza.
- **Criterios de aceptación**: detección confirmada con evidencia concreta, no solo "corrió sin errores".
- **Riesgos**: si este primer validador falla la prueba, es la señal de parar y rediseñar antes de construir los 10 agentes restantes — exactamente el criterio que faltaba en el proyecto anterior.
- **Costes externos**: coste de LLM del propio agente (bajo, una ejecución).
- **Reversión**: trivial, es un único módulo aislado.
- **Estado esperado al finalizar**: primer validador de continuidad probado y confiable.

### T3.2..T3.N — Resto de agentes, uno a la vez, solo si T1.2 reveló que ese paso concreto era doloroso a mano
- **Objetivo**: añadir automatización incrementalmente, priorizando por fricción real observada en el Paso 0, no por el roster completo de la Fase 7 de una vez.
- **Justificación**: veredicto del Council — automatizar de golpe sin evidencia de qué merece la pena es el mismo error de origen.
- **Prioridad**: media, secuencial, uno por uno.
- **Dependencias**: T3.1 aprobado, y evidencia concreta de fricción en T1.1/T1.2 para ese paso específico.
- **Resto de campos**: se instancian igual que T3.1 cuando se aborde cada agente concreto — no se detallan aquí de antemano para no repetir el mismo patrón de "planificar 13 agentes antes de necesitarlos" que el Council señaló.

---

## Posterior al MVP

- Recuperación semántica (embeddings) sobre el canon — solo si el volumen de una novela real lo justifica.
- Roster completo de 13 agentes — se completa incrementalmente según fricción observada, no de una vez.
- `create-novel` como entrevista guiada completa (Fase 4) — para el Paso 0 basta una premisa mínima; la entrevista completa se construye cuando se arranque la primera novela real, no la de prueba.
- Publicación adaptada a Royal Road/Patreon del mismo capítulo canónico.
- Clonado/variantes de novela, importación de lore externo.

## Opcional

- Música y efectos de sonido (el propio diseño de Fase 8 los marca como "solo si aportan valor", no obligatorios).
- Traducción asistida multi-idioma.
- LoRA de personaje para mayor consistencia visual, si el enfoque reference-based no basta.

## Investigación

- Auditoría profunda de `story-skills` (Fase 11) como posible base del validador de continuidad, en paralelo a T3.1 — si resulta sólida, sustituye o acelera ese trabajo.
- Causa humana real del abandono del proyecto anterior (punto ciego del Council) — conversación breve con el propio usuario, no un artefacto técnico.
- Evidencia de mercado/precedente de monetización de ficción serializada narrada por IA en YouTube, antes de dimensionar expectativas de audiencia.

## Deuda técnica (heredada, no se arrastra al MVP)

- Todo el código Python del repositorio original permanece sin usar hasta que se audite función por función (Fase 2) — no se migra por inercia.
- `README_es.md` genérico y `README_Saga_Functions.md` desactualizado — se reescriben cuando la nueva arquitectura esté estable, no antes.

---

## Resumen del orden de dependencias

```
T0.1 (seguridad, en paralelo)
T1.1 → T1.2 → T1.3 (gate) ──┬─→ T2.1 → T2.2
                              ├─→ T2.3
                              └─→ T2.4
                                   │
                                   ▼
                                 T3.1 (validador, con prueba de falsabilidad)
                                   │
                                   ▼
                              T3.2..T3.N (uno a la vez, solo si hay fricción real)
```

Nada del Grupo 2 en adelante se ejecuta sin pasar T1.3. Ese es el cambio de fondo que introduce el Council respecto al plan que tenía antes de la Fase 12.
