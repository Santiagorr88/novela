# Brief resumido para Council — plataforma de novelas serializadas → vídeo narrativo

## Qué es
Plataforma personal (operador único) para escribir novelas serializadas de largo recorrido (decenas/cientos de capítulos) manteniendo coherencia narrativa auditable, y convertir cada capítulo aprobado en una producción audiovisual tipo "audiolibro visual": narración completa + imágenes de escena con consistencia visual + voz de narrador estable + voz propia por personaje + música/SFX opcionales + subtítulos + montaje final para YouTube. El capítulo escrito es el activo canónico reutilizable; el vídeo es una derivación.

## Por qué (causa raíz del intento anterior, ya auditado)
Proyecto previo (fork abandonado de un framework de investigación web, reconvertido a generación narrativa) falló por: estado canónico duplicado y contradictorio entre dos rutas, memoria por truncado de caracteres sin criterio semántico, validadores de continuidad simbólicos (regex en inglés sobre prosa, comparación de cadenas) que no detectaban nada real, ≥3 versiones contradictorias del prompt del narrador sin control de versión, pipeline de producción roto (funciones inexistentes, credenciales inconsistentes) que nunca se probó de punta a punta, y cero tests/CI. Además se encontró y purgó una API key filtrada en el historial de un repo público.

## Rediseño propuesto
- **Multi-novela con aislamiento estricto**: cada novela es un workspace independiente (canon, personajes, presupuesto, estado propios); nada narrativo se comparte entre novelas.
- **Separación canon/proposals vs canon/approved**: ningún cambio de canon se aplica sin propuesta→revisión→aprobación humana explícita; único agente ("Responsable del canon") puede escribir canon aprobado; índice de propuestas pendientes evita ediciones concurrentes sin control.
- **Única fuente de verdad de estado** (`state/current.json`) en vez de estado duplicado.
- **Memoria por recuperación filtrada** (novela/personaje/localización/tiempo/arco) sobre resúmenes estructurados por capítulo, no por truncado de texto libre; recuperación semántica (embeddings) se pospone hasta que el volumen lo justifique, no se introduce en el MVP.
- **11 validadores de continuidad estructurados** (localización imposible, error temporal, información indebida por personaje, objetos, cambios físicos, poderes, relaciones, personalidad, tramas olvidadas, repeticiones, resurrecciones no explicadas) operando sobre datos estructurados, no heurísticas de texto libre.
- **13 agentes especializados** (consolidados desde 19 roles posibles), separando estrictamente quien escribe/genera de quien audita/aprueba.
- **Pipeline audiovisual de 23 pasos, reanudable e idempotente**, con manifest de coste/versión/aprobación por artefacto, sin regenerar lo ya aprobado salvo cambio de dependencias.
- **Fichas visuales y registro de voces persistentes** por personaje/localización/objeto, con guía visual global por novela y diccionario de pronunciación.
- **Sin infraestructura nueva en el MVP**: todo son archivos estructurados (YAML/JSON/Markdown) + Git; se documenta el punto exacto donde se justificaría una base vectorial o una cola de tareas más adelante, no se introduce ahora.
- **Control de coste desde el diseño**: presupuestos por entorno (desarrollo/pruebas/producción/regeneración/publicación), confirmación explícita antes de pasos caros, modo simulado para pruebas sin gasto real.
- Skills externas evaluadas (no instaladas todavía): ElevenLabs MCP oficial (adoptar), una skill de FFmpeg entre varias candidatas (elegir una, no varias), una skill de storyboard, y muy especialmente `story-skills` (github.com/danjdewhurst/story-skills), que ya implementa un concepto de "biblia de historia como contrato verificable" muy cercano al validador de continuidad diseñado aquí.

## MVP acotado
Novela de prueba desechable (`novels/_mvp-test/`), 1 capítulo corto, recorriendo el flujo completo: entrevista guiada → biblia inicial → personajes → arco corto → plan de capítulo → escritura → revisión de continuidad → revisión narrativa → aprobación → adaptación a guion de audio → escenas → storyboard → imágenes → voz de narrador → al menos 2 voces de personaje → subtítulos → montaje → exportación → registro de coste → archivo de recursos → reanudación probada → informe final de calidad.

## Pido evaluación desde
Arquitectura de software · diseño de sistemas multiagente · escritura de ficción · continuidad a largo plazo · gestión del canon · producción audiovisual · dirección de voces · consistencia visual · experiencia del espectador · crecimiento de audiencia · publicación · monetización · costes · seguridad · derechos de autor/licencias · dependencia de proveedores · escalabilidad · mantenimiento.

## Pido específicamente
Críticas concretas, riesgos, supuestos no validados, funcionalidades ausentes, complejidad innecesaria, alternativas, validación del alcance del MVP propuesto, criterios de éxito, motivos por los que este proyecto podría fracasar y medidas para reducir esos riesgos.
