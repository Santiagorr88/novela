# Definición de producto — Plataforma de novelas serializadas → vídeo narrativo

Fecha: 2026-08-06
Estado: propuesta para revisión del usuario (no es canon hasta que se apruebe)

## 1. Visión

Una plataforma personal de producción que permite crear, mantener y publicar **novelas serializadas de largo recorrido** (decenas o cientos de capítulos) manteniendo coherencia narrativa auditable, y convertir cada capítulo aprobado en una **producción audiovisual tipo audiolibro visual** (narración completa + imágenes de escena + voces + música + subtítulos), lista para YouTube y adaptable a Royal Road/Patreon.

El capítulo escrito es el activo canónico y reutilizable; el vídeo es una derivación de ese activo, no al revés. Esto permite: (a) republicar o volver a montar el vídeo si mejora el pipeline audiovisual sin tocar la historia, y (b) seguir vendiendo/publicando el texto en plataformas de lectura aunque el foco principal pase a vídeo.

## 2. Por qué existe (lecciones del intento anterior)

El proyecto original (ver [reports/01_repo_audit.md](01_repo_audit.md)) falló por causas estructurales, no por mala escritura puntual:

- Ausencia de una única fuente de verdad para el canon (estado duplicado y contradictorio).
- Memoria por truncado de texto, no por relevancia.
- Validadores de continuidad simbólicos que no validaban nada real.
- Prompts duplicados/contradictorios sin control de versión.
- Cero pruebas, cero forma de detectar regresiones antes de gastar en generación real.

La nueva plataforma existe para resolver específicamente estos cinco puntos antes de escalar volumen. **No es un rediseño estético, es un rediseño de las garantías de coherencia.**

## 3. Usuario y alcance

- Usuario único: el propio operador (Santiago), como autor/productor. No es una plataforma multiusuario ni un SaaS — al menos no en el alcance actual.
- El sistema asiste la escritura y producción; no reemplaza el juicio editorial. Todo cambio de canon y toda aprobación de capítulo/vídeo requiere una decisión humana explícita (ver Fase 5-7, flujo de propuesta→revisión→aprobación).
- Explícitamente **no** es un motor de generación masiva. Prioriza calidad y coherencia sobre velocidad; el volumen se escala solo después de validar que la calidad se sostiene.

## 4. Qué produce, por capítulo aprobado

1. Texto del capítulo (canon, versionado, reutilizable).
2. Guion adaptado a narración oral (narrador + diálogos separados).
3. Storyboard por escenas/planos.
4. Imágenes de escena con consistencia visual de personajes/localizaciones/objetos.
5. Audio: voz de narrador estable + voz propia por personaje recurrente + música/SFX cuando aporten valor.
6. Subtítulos sincronizados.
7. Vídeo montado, exportado, con miniatura y metadatos (título/descripción) para YouTube.
8. Registro de coste, versión y aprobación de cada artefacto (trazabilidad completa).
9. Opcionalmente: versión adaptada para Royal Road/Patreon a partir del mismo capítulo canónico.

## 5. Qué NO hace (por diseño, al menos en el MVP)

- No publica automáticamente sin aprobación humana.
- No clona voces de personas reales.
- No mezcla el canon de una novela con el de otra.
- No depende de un único proveedor de LLM/TTS/imagen sin capa de abstracción (para poder sustituirlo).
- No introduce base de datos, cola de tareas ni sistema vectorial en el MVP — se justifica solo si los archivos estructurados + Git dejan de ser suficientes (ver Fase 5-6, deuda técnica esperada más adelante, no ahora).

## 6. Multi-novela: aislamiento de universos

Cada novela es un **workspace independiente**: canon propio, personajes propios, presupuesto propio, estado de pipeline propio. Nada se comparte entre novelas salvo el código de la plataforma (agentes, motor de flujo, herramientas de producción) y, opcionalmente, guías de estilo globales del operador (no del universo ficticio). Esto evita el riesgo real de que el contexto de una novela contamine a otra al recuperar memoria — un fallo fácil de introducir si el sistema de recuperación no filtra por `novel_id` de forma estricta.

## 7. Estados del ciclo de vida de una novela

| Estado | Qué significa | Requisito de entrada | Qué puede pasar en este estado |
|---|---|---|---|
| **Idea** | Concepto informal, sin workspace propio todavía | Se registra una línea en el backlog de ideas | Nada automatizado; solo anotación |
| **Configuración inicial** | Entrevista guiada (`create-novel`) en curso o recién terminada | Se decide promover la idea | Se genera `project.yaml` + paquete inicial en borrador (biblia, personajes, arcos) — ver Fase 4 |
| **Preproducción** | El paquete inicial fue revisado y aprobado por el usuario | Aprobación explícita del paquete inicial | Se congela la biblia v1 como canon; se planifica el primer arco y el primer capítulo; se configura presupuesto y pipeline |
| **En desarrollo** | Escritura y producción activas | Preproducción completa | Capítulos en escritura/revisión; producción audiovisual de capítulos aprobados |
| **En publicación** | Ya se ha publicado al menos una vez | Al menos un capítulo o vídeo publicado | Cadencia de publicación activa; puede seguir "en desarrollo" en paralelo |
| **Pausada** | Desarrollo detenido temporalmente | Decisión explícita del usuario | Se conserva todo el estado; sin actividad de agentes salvo mantenimiento (p. ej. migraciones de esquema) |
| **Finalizada** | La historia llegó a su conclusión narrativa planeada | Arco final resuelto y aprobado | Puede seguir publicándose lo pendiente, pero no se planifican arcos nuevos |
| **Archivada** | Sin más actividad prevista | Decisión explícita del usuario | Solo lectura; recursos pesados (vídeo/audio/imágenes) pueden moverse a almacenamiento frío |

Todas las transiciones son explícitas (registradas en `project.yaml` con fecha y motivo), nunca implícitas por inactividad. Esto es deliberado: evita que el sistema "decida" archivar o publicar algo sin que el usuario lo pida.

## 8. Criterios de éxito del MVP (ver también reports/ de Fase 13)

- Un capítulo corto de una novela de prueba recorre el pipeline completo (texto → vídeo) sin intervención manual en pasos intermedios, salvo las aprobaciones de calidad deliberadas.
- El pipeline es reanudable: interrumpir y reanudar no regenera artefactos ya aprobados.
- El coste de cada artefacto queda registrado y es consultable.
- Un validador de continuidad detecta al menos una clase real de error (no cosmético) antes de que el capítulo se dé por aprobado.
- Nada de esto requiere una base de datos ni infraestructura nueva más allá de archivos estructurados + Git.

## 9. Riesgos de producto (no técnicos) a vigilar

- **Coste por capítulo en vídeo es mucho mayor que en texto** (imágenes + TTS por personaje + montaje). Sin control de presupuesto desde el primer capítulo, el coste puede descarrilar el proyecto antes de validar si el formato funciona con audiencia.
- **Derechos/licencias de voces e imágenes**: cualquier proveedor usado debe permitir explícitamente uso comercial/monetización en YouTube; esto se valida antes de adoptar un proveedor, no después.
- **Dependencia de un único proveedor de TTS/imagen**: mitigar con una capa de abstracción desde el diseño del pipeline (Fase 8), no como refactor posterior.
