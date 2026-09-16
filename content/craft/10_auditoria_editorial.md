# 10 — Protocolo de auditoría editorial

Fuente: prompt de auditoría generado a partir del material de oficio (conversación de referencia del autor, 2026-08-22). Adaptado al proyecto. Define CÓMO se audita una novela completa — el "qué" de cada área vive en los apartados 01-09.

## Regla fundamental

No dar por hecho que existe un problema solo porque una escena podría escribirse de otra manera. **Distinguir siempre entre**:

1. **Error narrativo real** — rompe lógica, continuidad o comprensión.
2. **Debilidad narrativa** — funciona, pero por debajo de su potencial.
3. **Oportunidad de mejora** — válido tal cual; existe una versión mejor.
4. **Decisión estilística válida del autor** — no se toca ni se reporta como problema.

Respetar voz, estilo, género e intención. No convertir preferencias personales en reglas universales. **Cada crítica importante debe estar respaldada por un ejemplo concreto del texto** (archivo + pasaje citado). No buscar errores artificialmente para llenar el informe; si algo funciona bien, decirlo.

> Esta regla ya es práctica establecida del proyecto: es la disciplina "verificar contra la prosa real antes de aplicar nada" de todas las auditorías de 2026-08, y la distinción Grupo A / B / C / D del resumen de coherencia es exactamente esta taxonomía en acción.

## Sistema de gravedad

| Nivel | Significado |
|---|---|
| 🔴 **Crítico** | Rompe la lógica de la historia, el arco principal o la comprensión del lector |
| 🟠 **Importante** | Afecta significativamente a ritmo, personajes, tensión o coherencia |
| 🟡 **Moderado** | Debilita una escena, no compromete la novela |
| 🔵 **Menor** | Estilístico o de corrección fácil |
| ⚪ **Opcional** | No es problema: posible mejora |

**Formato de cada hallazgo**: Ubicación (archivo/capítulo) · Problema · Por qué importa (efecto en el lector) · Gravedad · Solución sugerida sin cambiar la esencia.

## Fase 0 — Comprensión (antes de juzgar)

Identificar y resumir: género/subgénero, tono, público, protagonistas, conflicto y objetivo principal, antagonismo, pregunta narrativa central, tramas/subtramas, estructura, POV/narrador, arcos principales, temas, estilo. *(En este proyecto, la Fase 0 ya existe materializada: `prompt_universo.md` + el mapa de hilos de `design_notes/2026-08-22_coherence_audit_thread_map.md`.)*

## Las áreas de auditoría (y su estado en la trilogía)

| # | Área | Qué busca | Estado en la trilogía (2026-08-22) |
|---|---|---|---|
| 1 | **Trama y causalidad** | Incógnita principal activa y respondida; agujeros; coincidencias convenientes; info sin preparación; subtramas abandonadas; promesas rotas; escenas sin consecuencia; deus ex machina en el final | ✅ Cubierta (auditoría de coherencia: 19 agentes; Grupos A/B corregidos) |
| 2 | **Narrador y POV** | Consistencia del punto de vista; head-hops; información imposible desde el POV; cambios no señalados | ✅ Cubierta (2 auditorías POV completas de los 159 capítulos) |
| 3 | **Personajes** | Deseo/necesidad/motivación/obstáculos; complejidad; coherencia de decisiones; evolución perceptible; estereotipos; redundantes; desapariciones | ✅ Parcial (arcos verificados por hilo; análisis psicológico individual profundo solo en principales) |
| 4 | **Diálogos** | Artificialidad; voces indistinguibles; exposición camuflada; "as-you-know"; conversaciones eliminables sin consecuencia | ⏳ Pendiente como pasada dedicada |
| 5 | **Descripciones** | Exceso/carencia; bloques que paralizan tensión; dependencia exclusiva de la vista; repeticiones | ⏳ Pendiente como pasada dedicada |
| 6 | **Adjetivos y adverbios** | Acumulaciones; redundancias; adverbios que repiten el verbo. Clasificar: necesario / útil / prescindible / redundante — señalar solo lo que debilita | ⏳ Pendiente |
| 7 | **Ritmo** | Capítulos lentos; momentos importantes despachados deprisa; falta de descanso tras escenas intensas; escenas similares consecutivas; porcentajes inicio/desarrollo/clímax/resolución (diagnóstico, no matemática) | ⏳ Pendiente |
| 8 | **Continuidad factual** | Edades, fechas, distancias, nombres, aspecto, objetos, heridas, conocimientos, clima, cronología, reglas del mundo. Tabla: Ubicación 1 · Ubicación 2 · Contradicción · Gravedad · Corrección | ✅ Cubierta (auditoría de continuidad/lore + coherencia) |
| 9 | **Escenas prescindibles** | Qué se puede reducir/fusionar/eliminar sin afectar a nada. ⚠️ No confundir "prescindible" con "tranquilo": una escena contemplativa puede ser necesaria — explicar siempre qué función cumple hoy | ⏳ Pendiente |
| 10 | **Elementos no aprovechados** | Chekhov inverso: objetos/personajes/misterios con atención suficiente para generar expectativa y sin consecuencia. Clasificar: probablemente deliberado / posible cabo suelto / cabo suelto claro. Y el inverso: eventos importantes con preparación insuficiente | ✅ Cubierta (Grupo B de la coherencia, 9 cerrados) |
| 11 | **Propagación de información** | ¿Quién sabe qué, desde cuándo, por quién? Personajes que actúan con información que nunca recibieron | ✅ Parcial ad hoc (caso Gabriel/Lament); sistemática con el Knowledge Graph de `11_sistema_agentes.md` ⏳ |

## Ficha por capítulo (análisis granular)

Para auditorías capítulo a capítulo, cada capítulo recibe:

> **Función principal** (¿qué aporta?) · **Estado inicial → Cambio → Estado final** · **Conflicto** (¿qué tensión existe?) · **Personajes relevantes** (¿qué cambia para ellos?) · **Información nueva** (¿qué aprende el lector?) · **Ritmo** (lento/equilibrado/rápido) · **Problemas detectados** · **Necesidad**: esencial / importante / útil / prescindible.

Un capítulo sin cambio de estado y sin información nueva es candidato a fusión — pero ver la advertencia del área 9.

## Protocolo por bloques (obra más larga que el contexto)

1. **Nunca fingir haber leído lo que no se recibió.** Analizar por bloques.
2. Mantener registro acumulativo: personajes, cronología, tramas, preguntas abiertas, objetos, relaciones, reglas del mundo, contradicciones.
3. Distinguir conclusiones **provisionales** de **definitivas**; ninguna evaluación global antes del final.
4. Al cerrar cada bloque, emitir **MEMORIA DE CONTINUIDAD PARA EL SIGUIENTE BLOQUE**: solo los datos necesarios para contrastar con capítulos posteriores.

> En este proyecto el protocolo se implementa con agentes paralelos por hilo/bloque + un documento de verdad compartida (patrón ya probado: el thread map). Ver `11_sistema_agentes.md`.

## Regla de fases: diagnosticar ≠ reescribir

Durante la auditoría: **NO reescribir capítulos, NO cambiar el estilo, NO inventar escenas** (salvo presentadas expresamente como posibilidad). Pequeños ejemplos de solución sí; el trabajo es diagnosticar. La reescritura es una **segunda fase separada**, tras el informe global y con aprobación del autor por hallazgo (patrón ya establecido: los AskUserQuestion del Grupo B).

## Informe final

1. Diagnóstico general · 2. Lo que mejor funciona (5-15 fortalezas concretas) · 3. Principales problemas por gravedad · 4-9. Valoración por área (trama, narrador, personajes, diálogos, descripciones, ritmo) · 10. Contradicciones · 11. Cabos sueltos · 12. Capítulos problemáticos ordenados · 13. El final (preparación, clímax, resolución, respuesta a la incógnita, satisfacción) · 14. **Prioridades de revisión** en este orden estricto: lógica y coherencia → trama → estructura → personajes → ritmo → escenas → diálogos → descripción → estilo → corrección de frases · 15. Evaluación numérica:

| Área | Nota |
|---|---|
| Trama · Estructura · Personajes · Narrador y POV · Diálogos · Descripciones · Ritmo · Coherencia · Inmersión · Final | /10 cada una |

Más nota global orientativa y **las tres cosas que más aumentarían la calidad**.
