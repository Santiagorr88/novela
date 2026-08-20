# Council transcript — evaluación del rediseño de plataforma

Fecha: 2026-08-06
Brief evaluado: [reports/09_council_brief.md](09_council_brief.md)

## Pregunta enmarcada

Evaluar el rediseño de la plataforma de producción de novelas serializadas → vídeo narrativo (resumido en 09_council_brief.md) antes de invertir semanas/meses construyéndola, dado que un intento anterior del mismo proyecto ya fracasó por causas estructurales ya auditadas (estado duplicado, memoria por truncado, validadores simbólicos que no validaban nada, pipeline nunca probado de punta a punta, cero tests). Perspectivas solicitadas: arquitectura de software, sistemas multiagente, escritura de ficción, continuidad a largo plazo, gestión del canon, producción audiovisual, dirección de voces, consistencia visual, experiencia del espectador, crecimiento de audiencia, publicación, monetización, costes, seguridad, derechos de autor/licencias, dependencia de proveedores, escalabilidad, mantenimiento.

## Respuestas de los asesores

### El Contrarian
El defecto fatal no es técnico, es de secuenciación: este rediseño invierte semanas en arquitectura (13 agentes, 11 validadores, pipeline de 23 pasos) antes de validar la premisa de negocio: que alguien quiere ver un "audiolibro visual" narrado por una sola persona, y que esa persona puede sostener el ritmo de escritura de decenas de capítulos con calidad suficiente. El MVP propuesto no prueba eso — prueba que el pipeline corre de punta a punta con un capítulo desechable. Faltan criterios de éxito cualitativos, solo hay checklist de "no se rompió nada".

La causa raíz real del fracaso anterior no fueron los regex ni el estado duplicado — esos son síntomas. Fue que un operador único intentó sostener solo un sistema de complejidad de equipo. Este rediseño no reduce esa complejidad, la certifica: 13 agentes y 11 validadores siguen siendo 13+11 piezas que un humano solo debe mantener y aprobar capítulo a capítulo, sin estimar el cuello de botella de tiempo humano a escala de cientos de capítulos.

Evalúan story-skills como "muy cercano" a los validadores diseñados pero deciden construir los propios de todos modos — NIH disfrazado de rigor.

### El Pensador de Primeros Principios
La pregunta real no es "¿corrige este rediseño los fallos estructurales del anterior?" sino "¿por qué un operador único necesita 13 agentes, 23 pasos de pipeline y 11 validadores para escribir una novela y grabarla?".

El fracaso anterior fue deuda de diseño no gestionada (disciplina de ingeniería), no falta de agentes. El remedio propuesto es más complejidad organizativa — la misma enfermedad con mejor vocabulario. La pregunta de fondo: ¿existe siquiera una novela que alguien quiera leer? Se puede escribir una novela entera en Markdown plano con checklist manual en una tarde. Si eso no funciona, ningún pipeline de 23 pasos lo va a salvar, solo dará meses de ingeniería que sustituye a escribir.

### El Expansionista
¿Por qué limitar esto a UNA novela? El aislamiento multi-workspace ya diseñado es la característica más infravalorada: si el pipeline funciona una vez, el coste marginal de la novela 2, 3, 10 cae en picado (capital fijo amortizado por repetición) — es una fábrica de IP serializada. El capítulo como "activo canónico reutilizable" está infrautilizado si el único destino es YouTube: Wattpad/Royal Road/Kindle Vella, audiolibro puro, traducción asistida, licenciamiento del propio sistema. El modo simulado de costes es la piedra angular para escalar a paralelismo real.

### El Outsider
La cura para "complejidad accidental que fracasó" es más complejidad, solo que diseñada — para un operador único que nadie más podría mantener si se ausenta una semana. Confunden "estructurado" con "simple". "Sin infraestructura nueva, archivos+Git" pero describen un pipeline reanudable con estado por artefacto y control de versión de manifest — eso ES infraestructura, reinventada a mano en vez de usar SQLite.

Más grave: el problema original era coherencia a *cientos* de capítulos; el MVP prueba *uno*. Van a invertir semanas de infraestructura y nunca van a ver el fallo real (drift narrativo del capítulo 40) hasta después. Ausente por completo: nadie va a ver esto — no hay una línea sobre por qué un espectador elegiría este vídeo sobre cualquier otro "audiolibro visual" de YouTube.

### El Executor
El diagnóstico raíz no está resuelto, está reetiquetado. 13 agentes y 11 validadores multiplican la superficie donde puede volver a pasar exactamente lo mismo que antes.

Lo que se hace el lunes no es escribir el agente 1 de 13: es ejecutar el pipeline de 23 pasos a mano, sin ningún agente, para un capítulo de prueba — narración, imagen, voz, subtítulos, montaje, todo con las herramientas sueltas (ElevenLabs, FFmpeg) directamente desde la terminal. Si tardas dos días en hacerlo a mano y el resultado es aceptable, sabes qué automatizar primero. Si a mano ya es un infierno de fricción, ningún orquestador de 13 agentes lo va a salvar.

El MVP tal como está escrito no es un MVP, es el sistema completo con una novela desechable. El primer criterio de éxito real: ¿el validador de continuidad detectó un error de continuidad que tú insertaste a propósito? Si no, hay teatro, no validadores.

## Revisión por pares — síntesis

5 de 5 revisores identificaron el mismo punto ciego mayor: **la respuesta del Expansionista (multi-novela/fábrica de IP) responde una pregunta distinta a la que se hizo** — optimiza escala sobre una base que ni el propio Council considera probada, ignorando el cuello de botella real (el operador humano único).

4 de 5 revisores identificaron la respuesta del **Executor como la más fuerte**, por ser la única que convierte el diagnóstico en un experimento falsable y ejecutable de inmediato (ejecutar el pipeline a mano antes de automatizar nada).

Puntos que se les pasó a las cinco respuestas, señalados por los revisores:
- Ningún criterio explícito de abandono/kill-switch para este segundo intento.
- Sin estimación del coste de cómputo/API a escala de cientos de capítulos (solo se habló de tiempo humano).
- Ninguna cuestiona la causa *humana* real del fracaso anterior (¿burnout, pérdida de interés, o solo deuda técnica?) — la auditoría previa solo examinó código, no por qué la persona lo abandonó.
- La dimensión creativa/motivacional: automatizar en exceso puede matar el disfrute de escribir, causando abandono igual que la vez anterior, independientemente de la calidad de la arquitectura.
- La mitad "vídeo/audiencia" del proyecto queda casi sin examinar por los cinco asesores — nadie aborda dinámica del algoritmo de YouTube, adquisición de audiencia, ni precedente de monetización de ficción serializada narrada por IA.

## Veredicto del Chairman

### Dónde coincide el council
- El rediseño responde a la sobre-ingeniería del intento anterior con **más complejidad estructurada** (13 agentes, 11 validadores, 23 pasos), no con menos — riesgo real de estar certificando el mismo problema en vez de resolverlo (Contrarian, Primeros Principios, Outsider, Executor convergen en esto de forma independiente).
- El MVP tal como está diseñado prueba que **la fontanería del pipeline funciona una vez**, no prueba lo que realmente importa: si el operador puede sostener el ritmo de escritura, si el validador de continuidad detecta algo real, ni si alguien quiere ver el resultado.
- Hay una acción concreta, barata y ejecutable de inmediato que ningún asesor contradice: **ejecutar el pipeline completo a mano, sin agentes, para un capítulo de prueba**, antes de construir cualquier orquestación.

### Dónde choca el council
El Expansionista defiende que el diseño multi-novela ya contemplado (Fase 3) es el activo más infravalorado y que pensar en escala (varias novelas, licenciar el sistema) es visión, no distracción. Los otros cuatro asesores —y 5/5 revisores en la ronda de pares— consideran que es optimización prematura sobre una premisa no probada, y que ignora que el cuello de botella real es el tiempo/energía de un único operador humano.
**Resolución**: ambos tienen parte de razón, pero en planos distintos. El aislamiento multi-novela ya es barato de mantener en el diseño (Fase 3) porque es básicamente estructura de carpetas — no cuesta nada extra dejarlo como está. Pero **ninguna decisión de alcance del MVP ni del roadmap inmediato debe justificarse por "porque escala a más novelas"**. Se mantiene el diseño, se descarta la priorización.

### Puntos ciegos que el council detectó entre sí (ronda de pares)
- No hay criterio de abandono/kill-switch para este segundo intento — el proyecto original tampoco lo tuvo y por eso se alargó sin control.
- No hay estimación de coste de cómputo/API a escala de cientos de capítulos (Fase 12, aunque el diseño de Fase 8 sí tiene control de presupuesto por entorno, falta la proyección numérica a largo plazo).
- Nadie ha verificado la causa *humana* real del abandono anterior (¿deuda técnica, o fatiga/pérdida de interés del propio operador?) — la auditoría de Fase 2 solo miró código.
- Riesgo de que automatizar en exceso mate el disfrute de escribir, causando abandono por motivo distinto al técnico.
- La mitad "audiencia/vídeo" del proyecto (algoritmo de YouTube, adquisición de audiencia, precedente de monetización de ficción narrada por IA) queda sin examinar.

### La recomendación
No se descarta el rediseño (Fases 3-11 siguen siendo la arquitectura correcta si el proyecto avanza), pero **se cambia el orden de ejecución de la Fase 13**: antes de construir el primer agente, se inserta un **Paso 0 manual** — producir un capítulo de prueba de principio a fin sin ningún agente ni orquestación, usando las herramientas sueltas directamente (escritura manual, ElevenLabs directo para narrador + 1 personaje, un generador de imagen reference-based directo, FFmpeg directo para montaje). Esto:
1. Valida en 1-2 días, no semanas, si el operador puede sostener el proceso y si el resultado es mínimamente viable — antes de construir nada.
2. Da una estimación real de coste y de tiempo por capítulo.
3. Revela qué pasos son realmente repetitivos/dolorosos — eso, y solo eso, es lo que se automatiza primero, no los 13 agentes de golpe.

Se incorpora también: un criterio de abandono explícito (si el Paso 0 no es sostenible o el resultado no es mínimamente aceptable, no se avanza a construir agentes), y se pospone cualquier decisión o trabajo orientado a "escalar a más novelas" hasta que exista al menos una novela real con capítulos aprobados.

### Lo primero que hay que hacer
Antes de escribir código de ningún agente: producir un capítulo corto de la novela de prueba **completamente a mano**, de texto a vídeo, cronometrando cada paso y registrando el coste real. El plan de la Fase 13 (`/autoplan`) se reescribe para partir de ese Paso 0, no de la construcción del primer agente.
