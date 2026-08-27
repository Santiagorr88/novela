# Las Crónicas del Juicio — instrucciones permanentes

Trilogía de fantasía bilingüe (EN original, ES espejo). **Lee `ESTADO.md` primero**: ahí está la fase actual, lo hecho y lo pendiente.

## Reglas de trabajo del autor (no negociables)

1. **Paso a paso, libro a libro**: las pasadas se aplican al Libro I, se aprueban, y solo entonces II y III.
2. **Audio congelado por defecto**: no generar NINGÚN audio hasta que el autor lo pida. Cuando lo pida: borradores con edge-tts (gratis) primero; ElevenLabs (`.env`, claves — jamás imprimirlas ni commitearlas) solo tras su aprobación. Créditos limitados: calcular coste ANTES de gastar.
3. **PDFs/HTML congelados** hasta que el autor declare todo perfecto.
4. **ES nunca por delante de EN**: EN es el original; toda edición EN primero y ES espejo inmediato con la misma solución. Paridad de párrafos y separadores `---` EN↔ES obligatoria por capítulo.
5. **Réplicas de diálogo intocables** en pasadas de estilo (rayas, comillas, cursivas de habla). Tags "dijo/said" planos — jamás sinónimos ornamentales.
6. **Canon**: `content/lore/grafo_conocimiento.md` es el árbitro de quién sabe qué y cuándo. `personajes.md` y `prompt_universo.md` son las fichas. No inventar rasgos fuera de ellas.
7. **Voz de la prosa**: calibre B (`content/craft/12_calibre_b.md`) — una imagen ganada por escena, hecho + efecto, sin niebla ni calcos. Presencia por efecto (`13_presencia_cinematografica.md`), vector único por personaje, sin fórmulas repetidas.
8. **QA doble al cierre de cada fase**: verificación contra el texto real + revisión independiente con Codex (`codex exec --sandbox read-only`), y QA transversal de densidad/repetición en capítulos multi-pasada.
9. Los commits llevan mensajes en español describiendo la decisión del autor que los origina.

## Estructura

- Prosa canónica: `Libro{1,2,3}/{EN,ES}/NN_Titulo.md` + `_manifest.json` + `_actos.md` (actos con epígrafes del Codex).
- Narración audiolibro: `Libro*/audiolibro/{en,es}/capitulo_NN.txt` — regenerar tras cada edición de prosa (script en los commits).
- Casting de voces: `audiolibro_casting.json` (IDs ElevenLabs, dirección de actor, bandas) + fichas «Voz (audiolibro)» en `personajes.md`.
- Informes de cada pasada: `design_notes/AAAA-MM-DD_*.md`.
- Metodología: `content/craft/00-13`.
- Archivo histórico de generación: `content/lore/archive/fase_generacion/`.

## Cómo trabajar

Pasadas grandes = agentes Sonnet por tramos con brief detallado (modelo de calibración + reglas + zonas sagradas + verificación con git diff), el orquestador verifica muestras contra el texto real antes de commitear. Decisiones de trama/estilo/casting: SIEMPRE del autor — presentar muestras u opciones y esperar su elección.
