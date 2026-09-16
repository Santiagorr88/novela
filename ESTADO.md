# Estado del proyecto — actualizado 2026-09-01

## Fase actual

**Los tres libros han pasado ya por una pasada completa de calibración editorial** (dirección de trama + bucle de capítulos con NotebookLM + aplicación a los archivos reales + QA de canon), por decisión explícita del autor de avanzar los tres en la misma sesión en lugar de esperar turno por turno. Pendiente: veredicto final del autor sobre el conjunto (texto + audio) antes de dar la trilogía por cerrada.

- **Libro I**: calibrado y aplicado íntegro (51 capítulos).
- **Libro II**: calibrado y aplicado íntegro (53 capítulos); conflictos resueltos vía NotebookLM (Turein/V-TUREIN original, duplicación caps. 22/24).
- **Libro III**: diagnóstico editorial + dirección de trama + bucle de 52 capítulos completado y aplicado. Conflictos reales detectados y resueltos vía NotebookLM: violación V-TUREIN (heredada al Libro III, cerrada en `L3/04` y `L3/06`), filtración del nombre "Thamorak" antes de tiempo, duplicación de la reforja de Aetheris (resuelta: solo ocurre en `L3/38`), contradicción sobre la posesión de Lamentum. **Pendiente real de contenido**: el capítulo del origen de los tres Olvidados (por qué se ocultaron en la Tierra tras el Primer Cisma) no tiene hogar en los 52 capítulos existentes — decisión de dónde insertarlo en curso.

## Lo hecho (histórico, Libro I)

- **Trama**: el duelo final es Miguel vs LUCIFER (la excepción épica; Belial encuentra y entrega la lanza, la recibe de vuelta). Solmire elige portador (forjada por Ereloth). Doctrina de la Ley Divina sembrada (Sariel 07, Rafael 08). Arin y Milo ANÓNIMOS en L1 (sus nombres llegan en el II). Cap. 42 = «La Apuesta Larga».
- **Estructura**: 4 actos con epígrafes del Codex (fragmentos I, IV, II + verso no catalogado). Reparto de fragmentos para II y III planificado en `_actos.md` (Frag VI abre el II; Frag V reservado a la Forja del III).
- **Estilo (trilogía entera)**: calibre B (-9,4% L1), muletillas variadas, sinsentidos corregidos, armas latinizadas y reducidas, diálogos Rothfuss + registro Martin infernal.
- **Elenco (L1)**: presencia cinematográfica + 9 mini-subtramas + 46 menciones de voz (trilogía) + poda de densidad/antirrepetición.
- **Voces**: 67 fichas «Voz (audiolibro)» canónicas; reparto ElevenLabs cerrado por el autor (ver `audiolibro_casting.json`); dirección de actor + banda tenebrosa infernal.
- **Audio**: Acto I completo en multivoz ES (caps. 1, 2, 3, 5 calidad v2; cap. 4 Flash provisional).

## Pendiente inmediato

1. **Veredicto del autor sobre el Libro I** (texto + audio) → abre la fase del Libro II.
2. **~5 septiembre (renovación ElevenLabs, 131k créditos)**: retakes de caps. 1-5 con reparto final + dirección de actor + banda tenebrosa; regeneración del cap. 4 en v2. Guía: `audiolibro_casting.json` → `retakes_pendientes_al_renovar` (OJO: ese listado es pre-reparto-final; los retakes reales son TODAS las réplicas de personajes cuyo casting cambió: Miguel, Gabriel, Lucifer, Rafael, Camael, Zadkiel, Iofiel, Remiel...).
3. **Decisión menor**: huérfanos de ficha (Selke, Corin Vasse, Dez, Halaliel, Joran — con diálogo, sin ficha en el lore).

## Lista preparada para la fase del Libro II

- Escena épica de Milo en L2/16 (existe en embrión, reescribir en grande; su nombre se pronuncia en el II).
- Referencias retrospectivas del duelo («Belial venció a Miguel» → Lucifer) — lista en `design_notes/2026-08-26_audit_duelo_lucifer.md`.
- Doctrina del ciclo: Zadkiel L2/03 + callback de Mikel L2/48 (propuestas en `2026-08-26_audit_reencarnacion.md`).
- Actos del II con Frag VI + línea central del Codex + verso de la cadena.
- Subtramas del elenco del II (diseño pendiente); decisión sobre adelantar o no el regreso al Cielo (hoy en L3/21-22).
- Correcciones L2 de Solmire/jerarquía que apliquen (auditorías del 26-08).

## Contadores útiles

- ElevenLabs: plan Creator 131k/mes; capítulo en calidad v2 ≈ 11-16,5k créditos; Flash a mitad. Los créditos no usados caducan al renovar.
- La trilogía completa en ES ≈ 700k créditos/libro en v2.


## 2026-09-09 — Prólogo del Libro I
Creado `Libro1/{EN,ES}/00_Prologue.md` («What the Tree Kept» / «Lo que guardó el árbol»), 14 párrafos con paridad, registrado como n=0 en ambos manifiestos. Elegido por el autor entre dos borradores (`design_notes/2026-09-09_prologo_borradores.md`); canon verificado en NotebookLM (nadie dejó a Solmire en el fresno a propósito; el árbol la guardó sin testigos). Royal Road abre con el prólogo (`publicacion/royalroad/prologo_What_the_Tree_Kept.html`). Pendiente: narración audiolibro `capitulo_00.txt` (solo cuando se retome el audio) e inclusión en compilaciones/PDF (congelados).

## 2026-09-09 — Paquetes de referencia visual
150 paquetes (41 ángeles, 34 demonios, 10 mortales, 65 armas/objetos) en `video_production/images_personajes/{angeles,demonios,mortales}/` e `images_armas/`, una sola versión por lámina con master, turnaround, expressions, poses, details e identity_lock.txt (`pipeline/gen_fichas.py`, locks en `pipeline/locks/`). ~1 GB de PNG sin commitear (ignorados en git). Locks en `pipeline/locks/grupo_0..H.json`. Pendiente: revisión del autor (Azael y Camael: pidió cambios sin concretar), backup.

## 2026-09-10 — Orden de lanzamiento (decisión del autor)
No se monta ni publica ningún capítulo en vídeo hasta que estén listas las tres cosas:
1. Capítulos publicados en Royal Road (prólogo + capítulo 1 preparados, envío pendiente de confirmación del autor).
2. Las cuatro redes sociales creadas: YouTube (canal "Chronicles of Judgment", @SunderingJudgment) hecho 2026-09-10; TikTok, Instagram y X pendientes.
3. Patreon montado (pendiente, sin empezar).
Público objetivo del canal de vídeo: inglés-americano. Narración en inglés vía ElevenLabs (plan Creator activo, 127.798 caracteres/mes, 0 gastados) cuando se retome; candidatas de voz probadas: Peter (americana, narrativa), Brian (americana, grave, par de Mario), George (británica). Sin elegir todavía. La pista en español no se descarta, se mantiene en paralelo.

## 2026-09-12 — Patreon montado
Página creada: https://patreon.com/cw/chroniclesofjudgment (Nombre "Chronicles of Judgment", cover y foto de perfil subidas, misma identidad visual que las demás redes). Niveles de mecenazgo: Witness $4 (5 cap. adelanto), Bearer $8 (10 cap.), Forger $15 (15 cap.), solo adelanto de capítulos, sin extras. Acceso YouTube (API directa), X/Instagram/TikTok (Buffer) y Patreon (sin API de publicación, posts a mano) ya montados. **Único pendiente de los tres del orden de lanzamiento: confirmar el envío/publicación en Royal Road.**

## 2026-09-12 — Royal Road publicado, condiciones de lanzamiento cumplidas
El autor ha publicado la ficción en Royal Road y el prólogo ya está en vivo. Cadencia fijada: un capítulo cada lunes (capítulo 1 previsiblemente el próximo lunes). Con esto se cumplen las tres condiciones del orden de lanzamiento (Royal Road + 4 redes + Patreon). Producción de vídeo desbloqueada, pendiente de que el autor decida cuándo empezar.

## 2026-09-12 — Cadencia y estrategia de publicación
Publicación gratuita semanal en Royal Road: **domingo tarde-noche** (no lunes). Patreon: se publica de golpe el bloque completo de capítulos 2-16 al lanzamiento (no trickle semanal), con la tabla de niveles ya fijada (2-6 Tier 1 Witness, 7-11 Tier 2 Bearer, 12-16 Tier 3 Forger). Hay 51 capítulos escritos en Libro I, material de sobra para el buffer inicial.

## 2026-09-12 — Idioma del canal: solo inglés por ahora
Decisión del autor: el vídeo se centra únicamente en inglés (coincide con Royal Road y Patreon, ambos en inglés). La lista de reproducción "Español" en YouTube (https://www.youtube.com/playlist?list=PLDUAEM4js0EM) se queda creada pero vacía, sin usar por ahora. Se retomará el español cuando exista un destino de lectura/apoyo en ese idioma (Patreon en ES, otra plataforma, etc.), no antes.

## 2026-09-12 — Narrador en inglés elegido
Voz de ElevenLabs para la narración en inglés: **James - Husky, Engaging and Bold** (ID `EkK5I93UQWFDigLMpZcX`), elegido tras comparar con Adam Stone, Peter, Brian, George y Christopher usando una frase neutra y una línea de la escena del duelo final (L1/48). Modelo: `eleven_multilingual_v2`. Narrador en español sigue siendo Mario (`OjrdP8Z2fWjVyt0scrL7`, casting existente), sin uso activo por ahora (canal centrado solo en inglés).

## 2026-09-12 — Handles confirmados y plantillas cruzadas
Verificado por API de Buffer (query GraphQL a api.buffer.com): X = @ChronOfJudgment, Instagram = @chroniclesofjudgment (sin punto), TikTok = @chronicles.judgment (con punto). Plantillas de pie de publicación con referencias cruzadas entre redes (cada una menciona las otras, nunca la propia) en `publicacion/plantillas_cruzadas.md`.

## 2026-09-12 — Lanzamiento programado: Buffer + YouTube (Capítulo 1)
Bloqueo técnico resuelto: Buffer exige URL pública para cada asset y no tiene subida propia; el autor aportó un bucket público ya existente de otro proyecto (`gs://imrich-social/`, bucket `imrich-social`, lectura pública `allUsers:objectViewer`) — se creó la carpeta `novelas/cap01/` ahí para alojar los 13 Shorts + portada de lanzamiento. Ver `[[project_bucket_gcs_publico]]`.

Programado en Buffer (confirmado por el autor antes de ejecutar, mutación `createPost` vía GraphQL en `api.buffer.com`): **20 posts** Instagram+TikTok (los 10 Parts del capítulo 1, uno por franja de 10:00/20:00 hora España, del 13/09 20:00 al 18/09 10:00) + **1 post en X** (texto + `epic_v6.png`, 13/09 20:00). Nota técnica: Instagram exige `metadata.instagram.type: "reel"` + `shouldShareToFeed` en el input o el mutation falla con «Instagram posts require a type».

Patreon (sin API de publicación, manual): anuncio redactado en `publicacion/patreon/anuncio_lanzamiento.md`, pendiente de publicación manual/browser-assist a las 20:00.

YouTube: subida del vídeo completo + 3 Shorts destacados vía `youtube_upload.py` con `--publish-at 2026-09-13T18:00:00Z` (privacyStatus queda `private` hasta esa hora), añadidos a la playlist English. Usar el intérprete del venv del proyecto (`.venv/bin/python3`), no el `python3` del sistema — le faltan los paquetes `google-api-python-client`.

Enlace de Royal Road de la ficción (dado por el autor, usado en todas las plantillas): https://www.royalroad.com/fiction/191532/chronicles-of-judgment-the-echo-of-the-sword — apunta a la ficha de la novela, no al capítulo suelto.

Subida a YouTube completada (`youtube_upload.py`, privado + `publishAt` 2026-09-13T18:00:00Z, añadidos a playlist English `PLdrfm9NvTDZE`): vídeo completo `JnA5gLtCv-Y`, Shorts `lnTll_1kx4Q` (the wound), `1fML5WIvoao` (council's fear), `VBsV0d1HwRA` (Solmire). Nota: el canal no tiene habilitada la miniatura personalizada (falta verificación por teléfono en YouTube) — subido sin thumbnail custom, usa el frame automático.

Capítulo 1 programado por el autor directamente en Royal Road (Scheduled Release, 13/9/2026 20:00) — la extensión Claude in Chrome no llegó a conectar en esta sesión, lo hizo el autor a mano. Las tres plataformas (Royal Road, Buffer, YouTube) quedan alineadas exactamente a la misma hora. Pendiente de poca importancia: capturar la URL directa del capítulo (hoy los enlaces de Patreon/X/YouTube apuntan a la ficha general de la novela, que funciona igual) para sustituirla si el autor la pasa.

## 2026-09-15 — Nuevo diseño canónico de Miguel + `character_library/` completa (150→80 identidades)

El autor rediseñó a Miguel con Google Flow/Nano Banana (ayudado por ChatGPT): armadura oro/azul con emblema cian, alas blancas intactas — nuevo estilo canónico oficial, sustituye el diseño anterior del capítulo 1. `blocks.py` (pipeline de generación por plano) ya tiene el `IDENTITY_LOCK` de Miguel actualizado a v5 con este diseño.

En paralelo, Codex empezó a organizar `character_library/` (biblioteca de referencias visuales reutilizables: `canonical/{face,body}_reference.png` + prompts de portrait/fullbody + README, separando identidad estable de formas/estados narrativos) a partir de los paquetes Character Studio ya existentes en `video_production/images_personajes/` (85 carpetas: 40 ángeles, 35 demonios, 10 mortales). Completó Miguel, Gabriel y Lucifer y se quedó parado. El autor pidió a Claude coger el testigo y terminar el resto — hecho vía 8 agentes en paralelo (+ 2 de refuerzo para huecos y para el caso Arin Cross/Thaeriel): **80/80 identidades completas** (85 carpetas de origen − 5 fusionadas como forma humana de otro personaje).

Casos de fusión de forma humana confirmados contra `content/lore/grafo_conocimiento.md` (H6-H9) y `personajes.md`: Miguel↔Mikel Ardon, Ereloth↔Milo Ray, Azael↔Sabio de la Cumbre, Thaeriel↔Arin Cross (los cuatro "Olvidados" reencarnados/ocultos como mortales) + Camael↔Cam Loren (relación de "Human Form" normal, no del mecanismo de los Olvidados). Krass↔Corin Vasse es reencarnación con amnesia y diseño visual propio, NO fusión — documentados como personajes separados con nota cruzada.

Índice completo y lista de pendientes de calidad de datos (imágenes de origen mal etiquetadas para Cam Loren y Corin Vasse, fichas casi vacías como Elom, discrepancias menores como los ojos de Leviathan) en `character_library/INDEX.md`.

## 2026-09-15 — Gabriel y Lucifer rediseñados en Flow (decisiones del autor)

Tras el nuevo Miguel, el autor rediseñó a Gabriel y Lucifer directamente en Google Flow (Character Persona Generator + generación manual de retrato/cuerpo), con Claude verificando cada resultado contra la ficha canónica antes de aceptarlo.

- **Gabriel**: rostro más refinado (sustituye el "rostro rudo" fijado el 2026-09-09) y armadura plata/azul ornamentada de cuello alto en vez de solo peto sobre túnica. `blocks.py` `IDENTITY_LOCK` actualizado a v6. Cambio de estilo de vídeo, no contradice ningún hecho de prosa.
- **Lucifer**: pelo mucho más largo (hasta el pecho, ondulado) que el "hasta los hombros" que documenta la prosa citada en `personajes.md`/`identity_lock.txt` (L1/2, L1/6, L1/42, L1/47, L1/48, L2/10, L3/5). Tratado explícitamente como **licencia de vídeo únicamente** — actualizado en `character_library/Lucifer/prompts/` pero el texto de prosa y su ficha canónica NO se han tocado, para no perder la trazabilidad del canon real de la novela.

También se generó y añadió a Flow la descripción de comportamiento (personalidad, voz, estilo de combate) de Miguel, Gabriel y Lucifer, extraída literalmente de `personajes.md` sin inventar rasgos nuevos.

Pendiente de poca prioridad: guardar las imágenes finales aprobadas de Gabriel y Lucifer en `character_library/{Gabriel,Lucifer}/canonical/` (Claude no tiene acceso de archivo a las imágenes pegadas en el chat, solo las vio).
