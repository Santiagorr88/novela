# Investigación de skills especializadas (Fase 11)

Fecha: 2026-08-06
Estado: **shortlist de descubrimiento, no auditoría completa**. Para cada candidato comunitario he verificado únicamente nombre/fuente/descripción/actividad aparente vía búsqueda web — **no he clonado ni leído `SKILL.md`, scripts, dependencias ni permisos de ninguno todavía**. Ese es el paso obligatorio previo a instalar cualquiera de ellos (checklist completo al final de este informe), y debe hacerse antes de la Fase 13, no como parte de este descubrimiento.

## 1. Voz / ElevenLabs — TTS

| Campo | Valor |
|---|---|
| Nombre | `elevenlabs-mcp` (servidor MCP oficial) |
| Fuente | Repositorio oficial de ElevenLabs |
| Repositorio | github.com/elevenlabs/elevenlabs-mcp |
| Licencia | MIT (uso comercial permitido) |
| Actividad | v0.11.0, julio 2026 — activamente mantenido |
| Función | Expone TTS, clonado de voz, transcripción y más como herramientas MCP para Claude |
| Nivel de confianza | Alto — es el proveedor oficial, no un wrapper de terceros |
| Decisión propuesta | **Adoptar** como integración principal de voz (Fase 10), sustituyendo la necesidad de un wrapper HTTP propio. Requiere autorización vía `claude mcp add` / `/mcp` en una sesión interactiva (esta sesión no puede completar OAuth/config de credenciales por sí misma) y una `ELEVENLABS_API_KEY` en `.env`, nunca en el repo. |
| Motivo | Fuente oficial, licencia permisiva, mantenimiento activo — evita reinventar el wrapper que ya causó parte de la deuda técnica original (`call_gemini.py` con lectura de credenciales inconsistente). |

Hay también un fork de terceros (`199-mcp/mcp-elevenlabs`, "funciones conversacionales mejoradas") — **descartado** por defecto: no hay necesidad de conversación en tiempo real para este pipeline, y añadir un fork no oficial encima del oficial no aporta valor sin una razón concreta.

## 2. Vídeo / FFmpeg

Varios candidatos activos, todos resuelven el mismo problema (traducir intención de edición a comandos FFmpeg):

| Nombre | Repositorio | Función declarada | Nota |
|---|---|---|---|
| `ffmpeg-skill` | github.com/MastroMimmo/ffmpeg-skill | 18 comandos de alto nivel (cortar, fusionar, comprimir, subtitular, GIF, marca de agua, velocidad, estabilizar) + acceso FFmpeg crudo | Candidato principal — cobertura más amplia declarada |
| `video-editing-skill` | github.com/6missedcalls/video-editing-skill | Trim, jump cut, captions, overlays, cambio de velocidad; Bash + FFmpeg + Whisper | Solapa con el anterior + con subtítulos (sección 4) |
| `claude-ffmpeg-skill` | github.com/ychoi-kr/claude-ffmpeg-skill | 20+ operaciones con presets para YouTube/Instagram/TikTok/Twitter | Los presets de YouTube son directamente relevantes para la Fase 8 (exportación) |
| `Claude-Code-Video-Toolkit` | github.com/wilwaldon/Claude-Code-Video-Toolkit | Vídeo programático (Remotion, Manim), grabación de pantalla, recorte de YouTube, postproducción FFmpeg | Más amplio de lo que necesitamos (no hacemos vídeo programático ni grabación de pantalla) |

**Decisión propuesta**: evaluar en profundidad **solo uno** como base (candidato preferente: `MastroMimmo/ffmpeg-skill` por cobertura + simplicidad "zero dependencies" declarada) antes de la Fase 13, en vez de instalar los cuatro — instalar varios que resuelven lo mismo va contra la restricción explícita del encargo. Si tras la auditoría no es idóneo, pasar al siguiente de la lista, no acumular ambos.

## 3. Storyboard

| Nombre | Repositorio | Función | Nota |
|---|---|---|---|
| `ai-video-storyboard-skill` | github.com/aicontentskills/ai-video-storyboard-skill | Convierte briefs en planes de producción multi-plano, con prompts cinematográficos, consistencia visual y checklist de postproducción | Encaja directamente con el rol "Director de storyboard" (Fase 7, agente 10) — candidato principal a auditar |

## 4. Subtítulos

| Nombre | Repositorio | Función |
|---|---|---|
| `claude-skills` (jianshuo) | github.com/jianshuo/claude-skills | 13 skills de producción de vídeo: transcribir, traducir, doblar, multicámara, subtítulos, reencuadre |
| `skill-caption-clip` | github.com/kwindla/skill-caption-clip | Subtitulado de clips cortos vía Deepgram + FFmpeg |
| `clipify` | github.com/louisedesadeleer/clipify | Recorte a formato 9:16 con seguimiento facial + subtítulos estilo "opus" |

**Decisión propuesta**: `jianshuo/claude-skills` es el candidato más alineado (cubre transcripción+subtítulos+doblaje, relevante también para la posible versión ES/EN del mismo capítulo). Los otros dos están orientados a clips cortos verticales (formato distinto al nuestro, capítulo completo en 16:9) — **descartados** por desajuste de formato, no por calidad.

## 5. Escritura de ficción / continuidad narrativa

Este es el hallazgo más relevante de la investigación:

| Nombre | Repositorio | Función declarada | Relevancia |
|---|---|---|---|
| `story-skills` | github.com/danjdewhurst/story-skills | Formato de proyecto compartido (biblia de historia, personajes, worldbuilding, facciones, artefactos, arcos, estado de escena, preguntas de continuidad, promesas/pagos, cronologías, borradores). CLI que trata la biblia como **contrato verificable**: detecta "personajes muertos caminando", pagos narrativos que llegan antes que su setup, "armas de Chekhov" sin disparar, y estado de historia obsoleto | **Coincide casi exactamente con el diseño de la Fase 5-6 de este proyecto** (validadores de continuidad estructurados, registro de promesas). Candidato prioritario a auditar a fondo — si la implementación es sólida, podría evitar construir el validador de continuidad desde cero |
| `creative-writing-skills` (haowjy) | github.com/haowjy/creative-writing-skills | Agentes especializados: brainstorming, escritura, crítica, revisión, con continuity-checker y style-creator | Se solapa con nuestro roster de agentes (Fase 7) — útil como referencia de diseño aunque no se adopte literal |
| `fiction` (howells) | github.com/howells/fiction | Plugin con agentes: arquitectura, personajes, prosa, revisión, edición, continuidad, preparación de publicación | Roster de agentes muy similar al propuesto en Fase 7 — comparar antes de construir el propio |
| `Claude-Book` (ThomasHoussin) | github.com/ThomasHoussin/Claude-Book | Framework multiagente para escribir novelas completas con Claude Code | Evaluar como referencia arquitectónica, no como dependencia directa (alcance muy amplio, probablemente asume su propia estructura de carpetas) |
| `novel-writer-english` (JeroTan) | github.com/JeroTan/novel-writer-english | Consistencia de historia, personajes, ritmo, worldbuilding; rastrea reglas de mundo/sistemas de magia | Traducción de otra skill — verificar autoría y calidad de la traducción antes de considerar |
| `author-toolkit` (rhavekost) | github.com/rhavekost/author-toolkit | Incluye "Continuity Tracker" (cronología, hechos de mundo, consistencia interna) | Candidato secundario, función solapada con `story-skills` |

**Decisión propuesta**: auditar primero `story-skills` en profundidad (parece la más cercana al diseño ya hecho en Fase 5-6); si pasa la auditoría, usarla como referencia de implementación o base directa del validador de continuidad en vez de construirlo desde cero. Las demás quedan como referencia de diseño, no se instalan varias en paralelo para el mismo rol.

## 6. Producción "faceless" de referencia arquitectónica

| Nombre | Repositorio | Función | Nota |
|---|---|---|---|
| `claude-faceless-shorts-creator` | github.com/hassancs91/claude-faceless-shorts-creator | Fábrica de YouTube Shorts sin presentador: visuales en Remotion (TSX), voz ElevenLabs con subtítulos exactos por palabra, diseño de sonido | Formato distinto al nuestro (shorts verticales cortos vs. capítulos largos horizontales), pero la arquitectura (Remotion + ElevenLabs + captions exactos) es una referencia útil para la fase de montaje (paso 18 del pipeline, Fase 8) |

## 7. Consistencia visual de personajes (no es una "skill" de Claude, es elección de proveedor)

No es una skill instalable sino una decisión de proveedor de imagen para la Fase 9: en 2026 los enfoques dominantes son *reference-based* (subir 1+ imágenes del personaje, el modelo fija la identidad — p. ej. Gemini "Nano Banana Pro", FaceID Plus v2) y *LoRA-based* (entrenar un adaptador con 15-30 imágenes, más control pero más coste/tiempo de preparación). **Recomendación para el MVP**: empezar con un proveedor *reference-based* (menor fricción, sin entrenamiento previo) y dejar LoRA como mejora futura si la consistencia no es suficiente en la práctica. Esto se decide y documenta en `config/providers.yaml` (Fase 3), no aquí.

## 8. Qué NO se encontró y por tanto se construye internamente

No apareció ninguna skill que cubra el **flujo de aprobación de canon (propuesta→revisión→aprobación) específico de este proyecto**, ni el **registro de coste por artefacto con manifest reanudable** tal como se diseñó en la Fase 8. Estas dos piezas son suficientemente específicas del producto que se construyen como código propio de `platform/`, no como skill externa — coincide con la instrucción del encargo de no forzar una skill genérica donde no encaja bien.

## Checklist de auditoría obligatoria antes de instalar cualquier candidato (pendiente, no ejecutada aún)

Para cada uno de los candidatos marcados como "auditar": leer `SKILL.md` completo, revisar todos los scripts ejecutables, comprobar dependencias declaradas, comprobar qué permisos/archivos toca, comprobar qué datos transmite a servicios externos, comprobar ausencia de comandos destructivos por defecto, verificar licencia compatible con uso comercial, verificar fecha de última actividad y señales de mantenimiento, buscar instrucciones ocultas o código ofuscado. Ninguno de los candidatos comunitarios listados aquí se instala ni se ejecuta hasta pasar esta checklist — se deja como tarea explícita previa a (o al inicio de) la Fase 13.
