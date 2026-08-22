# 11 — Sistema multiagente de auditoría y las tres bases compartidas

Fuente: diseño de arquitectura de la conversación de referencia del autor (2026-08-22), adaptado a cómo trabaja realmente este proyecto (agentes paralelos + documentos de verdad compartida en `design_notes/` y `content/lore/`).

## Principio: 5-6 especialistas + 1 coordinador, en tres fases

No un agente por criterio (15-20 agentes generan ruido, duplicación y recomendaciones contradictorias). La estructura:

**Fase 1 — Comprensión**: un agente de mapeo construye/actualiza la memoria compartida de la obra (equivalente al thread map de 2026-08-22: hilos + registro de vida/muerte).

**Fase 2 — Análisis paralelo** de especialistas, todos leyendo la MISMA memoria compartida:
- **Trama y estructura** (causalidad, subtramas, clímax, deus ex machina, escenas prescindibles)
- **Narrador y POV**
- **Personajes** (ver subsistema abajo)
- **Mundo y cronología** (continuidad factual)
- **Diálogos y voz** (⚠️ debe consultar la biblia de personajes — ver abajo)
- **Descripción e inmersión**

**Fase 3 — Consolidación**: el coordinador (editor jefe) recibe todos los informes, **resuelve conflictos entre especialistas** (uno considera una escena lenta; otro la considera necesaria para el personaje — alguien tiene que decidir), filtra duplicados y produce el informe único.

Reglas heredadas de `10_auditoria_editorial.md`: nadie reescribe en primera pasada; cada hallazgo con cita real; el coordinador re-verifica contra la prosa antes de aceptar un hallazgo (lección Zadkiel/Zadquiel: los informes de agentes se comprueban, no se creen).

## Sin memoria compartida, más agentes = peor resultado

Cada agente sin memoria común acaba auditando "una novela ligeramente distinta". La memoria compartida se actualiza tras cada bloque e incluye: personajes, relaciones, cronología, lugares, preguntas abiertas, subtramas, objetos importantes, reglas del mundo, contradicciones ya detectadas.

> Ya validado en la práctica: la auditoría de coherencia funcionó precisamente porque los 19 agentes leían el mismo thread map como verdad de referencia antes de tocar su hilo.

## El subsistema de personajes (obligatorio con elencos grandes)

Con ~78 personajes fichados en la trilogía (y creciendo en obra futura), "un agente de personajes" se queda corto: es un **subsistema con responsabilidades separadas** (no necesariamente agentes separados — un módulo con datos separados):

| Responsabilidad | Qué mantiene |
|---|---|
| **Registro** | Todos los personajes, alias, apodos, títulos, variantes de nombre; una ficha única por personaje, cero duplicados *(lección real: Zadkiel/Zadquiel, Lament/Lamentun/Lamentum)* |
| **Perfiles** | La ficha viva de cada uno (plantilla: `03_ficha_personaje_plantilla.md`) |
| **Grafo de relaciones** | Familia, lealtades, jerarquías, enemistades, romances, conocimiento mutuo — y su evolución con capítulo de cambio |
| **Grafo de conocimiento** | Quién sabe qué, desde cuándo, por qué vía (ver abajo) |
| **Arcos** | Solo personajes importantes: cambios psicológicos preparados y culminados en página |
| **Relevancia** | Redundantes, abandonados, introducidos y nunca usados, confundibles entre sí |

### Niveles de análisis (no todo personaje merece lo mismo)

| Nivel | Tipo | Profundidad de análisis |
|---|---|---|
| **A** | Protagonistas | Máxima: arco completo, psicología, voz |
| **B** | Secundarios importantes | Alta: estructura dinámica + voz |
| **C** | Recurrentes | Continuidad + función |
| **D** | Incidentales | Identidad + continuidad básica (que el posadero tuerto del cap. 8 siga siendo tuerto si reaparece 400 páginas después) |

*(Mapea sobre la jerarquía de `02_personajes.md`: A/B ≈ principales, C ≈ secundarios, D ≈ terciarios. En la trilogía: A ≈ Miguel/Michael, los tres Forgotten, Belial, Gabriel; B ≈ Lucifer, Camael, Uriel, Iofiel, Vepar, Foras…; C ≈ capitanes recurrentes; D ≈ squad leaders de una escena.)*

### El grafo de conocimiento: la clase de error que nada más detecta

Muchos errores de novela larga no son de trama sino de **propagación de información**: un personaje actúa sobre algo que nunca se le contó.

> Cap. 12: Laura descubre que Marcos es el traidor → cap. 14: se lo cuenta a Daniel → cap. 16: Daniel a Irene → cap. 17: **Carlos** acusa a Marcos. *¿Cómo lo sabe Carlos?* Con 10 personajes te acuerdas; con 78+, imposible sin registro.

Formato mínimo por hecho relevante:

```
HECHO: "Lament fue forjada por Thaeriel"
  - Iofiel: lo sabe desde L1/43 (Codex, reconstrucción propia)
  - Gabriel: parcial desde L2/26 (informe: "relic robado, forjador desconocido");
             completo desde L3/22 (testimonio de Michael)
  - Belial: desde L3/19 (se lo dice el propio Thaeriel en el duelo)
  - Lucifer: NUNCA completo (establecido en L2/10; verificado en auditoría)
```

Ese ejemplo es real: la comprobación "¿Gabriel actúa en algún capítulo como si ya supiera quién forjó Lament?" fue exactamente una auditoría de grafo de conocimiento hecha a mano (2026-08-22, hilo de Gabriel — resultado limpio). El grafo lo vuelve sistemático: **cada revelación importante se registra al escribirse la escena**, con personaje, capítulo y vía (observación directa / se lo contaron / lo dedujo).

### El agente de diálogos consulta la biblia

"Este diálogo no suena a Alejandro" es opinión; contra una ficha de voz es verificable:

> Agares: nunca pide directamente, pliega la petición en una observación más larga · voz bífida · disfruta los mecanismos que diseñó. Ereloth: acertijos, paradojas, miente para proteger. Vepar: clipped, profesional, cero teatro. — Si una réplica nueva viola la ficha de voz, es hallazgo con evidencia, no gusto.

Por eso la plantilla de ficha (03) tiene el campo **"Forma de hablar"** como obligatorio para todo personaje con diálogo.

## Estado de implementación en el proyecto

- ✅ Memoria compartida de hilos y vida/muerte: `design_notes/2026-08-22_coherence_audit_thread_map.md`
- ✅ Fichas centralizadas: `content/lore/personajes.md` (registro + perfiles)
- ✅ Patrón coordinador + especialistas paralelos: probado en las tres auditorías de 2026-08
- ⏳ Grafo de conocimiento sistemático: no existe todavía como documento — **construirlo es prerequisito recomendado antes de escribir Saga II** (y opcionalmente retro-construirlo para la trilogía como pasada de auditoría del área 11 de `10_auditoria_editorial.md`)
- ⏳ Grafo de relaciones explícito: hoy está implícito en `personajes.md`; formalizarlo cuando el elenco de la obra nueva lo pida
- ⏳ Fichas de voz por personaje A/B: los rasgos existen dispersos en la prosa; consolidarlos en las fichas al empezar obra nueva
