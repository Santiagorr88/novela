# Pipeline audiovisual, consistencia visual y voces (Fases 8-10)

Fecha: 2026-08-06
Estado: propuesta para revisión del usuario (diseño, no implementación)

## Parte A — Pipeline (Fase 8)

### A.1 Principio de reanudabilidad

Cada capítulo tiene un único `production/<chapter-id>/artifact_manifest.json` que registra, por artefacto, el esquema completo pedido en el encargo: `id, version, estado, fecha_creacion, herramienta, modelo, prompt, parametros, coste, archivos_entrada, archivos_salida, dependencias, estado_aprobacion`. El Supervisor de producción (agente 13) recorre el pipeline paso a paso; antes de ejecutar un paso comprueba si ya existe un artefacto con estado `aprobado` cuyas dependencias no cambiaron (comparando hash de las entradas) — si es así, lo salta. Esto resuelve directamente el requisito "no debe regenerar recursos aprobados salvo que hayan cambiado sus dependencias" y "el pipeline debe poder reanudarse desde el último paso completado".

### A.2 Pasos del pipeline, mapeados a agente responsable y artefacto de salida

| # | Paso | Agente | Salida |
|---|---|---|---|
| 1 | Seleccionar capítulo aprobado | Supervisor de producción | referencia en manifest |
| 2 | Adaptar a narración oral | Adaptador audiovisual | `script/narration_script.yaml` |
| 3 | Separar narrador y diálogos | Adaptador audiovisual | (incluido en el mismo script) |
| 4 | Dividir en escenas | Director de storyboard | `storyboard/scenes.yaml` |
| 5 | Dividir en planos | Director de storyboard | `storyboard/shots.yaml` |
| 6 | Generar storyboard | Director de storyboard | miniaturas/bocetos por plano |
| 7 | Calcular duración estimada | Director de storyboard | campo `duracion_estimada` por plano y total |
| 8 | Crear prompts visuales | Director de storyboard | prompt + prompt negativo por plano, referenciando fichas (Fase 9) |
| 9 | Generar/seleccionar imágenes | Proveedor de imagen (herramienta, no agente) | `images/shot_<n>.png` |
| 10 | Validar consistencia visual | Supervisor visual | aprobación o regeneración con motivo |
| 11 | Generar voz del narrador | Director de voces | `audio/narrator/*.wav` |
| 12 | Generar voces de personajes | Director de voces | `audio/characters/<id>/*.wav` |
| 13 | Añadir pausas e interpretación | Director de voces | metadatos SSML/parámetros en el script |
| 14 | Crear música y efectos | Proveedor de audio (herramienta) | `audio/music/`, `audio/sfx/` — solo si aportan valor (criterio explícito del Director de voces/Supervisor de producción, no automático por defecto) |
| 15 | Mezclar audio | Supervisor de producción (vía FFmpeg) | `audio/mix.wav` |
| 16 | Generar subtítulos | Herramienta de subtitulado (a partir del script + timestamps del audio) | `subtitles/<id>.srt` |
| 17 | Sincronizar imagen/audio/subtítulos | Supervisor de producción | timeline de montaje |
| 18 | Montar vídeo | Supervisor de producción (FFmpeg) | `video/draft.mp4` |
| 19 | Validar resultado | Supervisor de producción + revisión humana | pass/fail con evidencia |
| 20 | Exportar vídeo | Supervisor de producción | `video/final.mp4` |
| 21 | Generar miniatura | Supervisor de producción | `video/thumbnail.png` |
| 22 | Generar título/descripción/metadatos | Adaptador audiovisual | `publishing/<platform>/metadata.yaml` |
| 23 | Archivar recursos y configuración | Supervisor de producción | manifest final, congelado |

### A.3 Control de coste (Fase "Gestión de costes" del encargo)

`config/budgets.yaml` define límites por entorno: desarrollo, pruebas, producción, regeneraciones, publicación. Antes de cualquier paso con coste (9, 11, 12, 14), el Supervisor de producción compara el coste estimado contra el presupuesto restante de la novela (`project.yaml → budget:`) y **pide confirmación explícita si el paso supera un umbral configurable** — no hay generación cara silenciosa. Modo de prueba: `providers.yaml` permite marcar un proveedor como `simulado` (devuelve un artefacto placeholder de coste cero) o forzar resolución/calidad reducida, para poder validar el pipeline completo sin gasto real antes de la producción final.

## Parte B — Consistencia visual (Fase 9)

### B.1 Ficha visual persistente

Una ficha por entidad recurrente (personaje, localización, criatura, vehículo, arma, artefacto, símbolo), en `assets/<tipo>/<id>.yaml`: rasgos físicos, edad aparente, altura, complexión, rostro, pelo, ojos, marcas distintivas, vestuario, accesorios, paleta visual, expresiones/posturas habituales, variaciones permitidas, cambios relacionados con la historia (con capítulo en que ocurrieron — enlazado a `state/history/`), imágenes de referencia, prompt base, prompt negativo, semilla/identificador del proveedor cuando esté disponible.

### B.2 Guía visual global de la novela

`canon/approved/visual_guide.md`: estilo visual, relación de aspecto, nivel de movimiento, estático vs. animado, iluminación, paleta general — se genera en la entrevista (Fase 4) y todo prompt visual de un plano debe ser consistente con ella salvo excepción justificada.

### B.3 Detección de desviación visual

El Supervisor visual (agente 11) compara cada imagen generada contra la ficha de referencia antes de aprobarla — en el MVP esto es una revisión guiada por LLM-as-judge con visión (describe la imagen generada y la compara campo a campo contra la ficha), no un clasificador entrenado a medida; se deja documentado como posible mejora futura si la tasa de falsos negativos es alta en la práctica.

## Parte C — Voces y ElevenLabs (Fase 10)

### C.1 Registro de voces persistente

`voices/registry.yaml`, una entrada por personaje recurrente + una para el narrador: `character_id, proveedor, voice_id, modelo, idioma, acento, edad_vocal, timbre, ritmo, intensidad, estabilidad, parametros_proveedor, guia_interpretacion, pronunciaciones_especiales, historial_cambios, muestras_aprobadas`. Una vez fijada, una voz no cambia salvo aprobación explícita del usuario (ver agente 12, restricciones) — la estabilidad de voz es un requisito de producto, no una opción.

**Regla de asignación (2026-08-08, decisión del usuario)**: una única voz narradora principal, fijada una vez y usada para todo el hilo narrativo. Cada personaje con diálogo propio recibe su propia voz la primera vez que habla en un capítulo: el agente de voces compara la ficha del personaje (edad, personalidad, timbre implícito en su descripción física/de carácter en `prompt_universo.md`/`personajes.md`) contra el catálogo de voces disponibles del proveedor (edad vocal, timbre, acento, tono) y asigna la que mejor encaje — no se pide selección manual salvo que el usuario quiera revisar el match antes de fijarlo en el registro. Una vez asignada y aprobada, esa voz queda fija para el personaje bajo la misma regla de estabilidad de C.1.

### C.2 Diccionario de pronunciación

`voices/pronunciation_dictionary.yaml`: nombres propios, lugares, idiomas ficticios, hechizos, términos inventados, con su pronunciación fonética/SSML. Se alimenta desde `canon/approved/` (cualquier nombre propio nuevo introducido en canon dispara una entrada pendiente aquí) para que nunca se generen dos pronunciaciones distintas del mismo nombre entre capítulos.

### C.3 Licencias y credenciales

- Ninguna voz se genera clonando la voz de una persona real sin autorización explícita — restricción dura, verificada antes de fijar cualquier `voice_id` nuevo en el registro.
- Todo proveedor de voz/imagen/música usado debe tener licencia compatible con publicación y monetización en YouTube — se verifica y se anota en `providers.yaml` (`licencia: comercial|no-comercial|revisar`) antes de adoptarlo, no después de generar contenido con él.
- **Credenciales**: `ELEVENLABS_API_KEY` y equivalentes viven solo en `.env` (ya en `.gitignore`, ver auditoría Fase 2) o en un gestor de secretos si se pasa a producción real. Nunca aparecen en `providers.yaml`, en prompts almacenados, en logs, en informes ni en archivos de ejemplo — los wrappers de proveedor leen la variable de entorno en tiempo de ejecución y el resto del sistema solo referencia el nombre de la variable, nunca el valor. Este punto es más estricto de lo habitual precisamente porque la Fase 2 ya encontró una clave real filtrada en este mismo repositorio.

## Justificación de por qué esto no requiere infraestructura nueva

Todo el pipeline es archivos + un orquestador que lee/escribe `artifact_manifest.json` y llama a wrappers de proveedor (funciones Python, no servicios). No se introduce cola de tareas: en el MVP la ejecución es secuencial y local; si el volumen de producción crece lo suficiente para justificar paralelismo real entre capítulos, ese es el punto documentado donde se evaluaría una cola — no antes.
