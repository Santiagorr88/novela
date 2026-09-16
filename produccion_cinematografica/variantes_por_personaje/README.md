# Variantes visuales por personaje y capítulo

Carpeta puente entre `character_library/` (identidad canónica base de cada personaje) y la producción de vídeo capítulo a capítulo: registra **qué variante/estado de cada personaje hace falta en qué capítulo**, si ya existe generada, y el prompt de edición exacto (Nano Banana, desde la ficha de personaje en Flow — ver `../2026-09-16_escena_piloto_dialogo.md` sección 7 para el paso a paso de la interfaz) para generarla si falta.

`character_library/<bando>/<Personaje>/states/` y `/forms/` ya documentan visualmente algunos estados narrativos (ej. `Miguel/states/burned_left_wing/`). Esta carpeta no duplica esa descripción — solo la **cruza contra capítulos concretos** para saber cuándo usarla, y añade variantes nuevas que surgen al analizar un capítulo (como la armadura agrietada de Miguel) que todavía no tienen ficha propia en `character_library`.

Un archivo por personaje. Se amplía capítulo a capítulo según se van analizando.

## Convención de la tabla

| Capítulo | Estado/variante necesaria | ¿Existe ya generada? | Prompt de edición |
|---|---|---|---|
| ... | ... | Sí / No / Por confirmar | (vacío si usa la imagen canónica base tal cual) |
