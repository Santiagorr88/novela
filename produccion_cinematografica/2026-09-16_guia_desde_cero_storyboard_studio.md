# Guía definitiva — empezar Storyboard Studio desde cero (capítulo 1)

> Fecha: 2026-09-16. Consolida todo lo aprendido con el intento anterior (proyecto "A Wound in the World"), para no repetir los mismos tropiezos. Sigue esta guía en orden.

## 0. Qué se reutiliza y qué se reinicia

- **Se reutiliza (no tocar)**: los personajes ya creados y aprobados en la pestaña "Caracteres" del proyecto de Flow — Miguel (con la variante de armadura agrietada + ala chamuscada), Gabriel, Lucifer, Pewter Sentinel. Son horas de trabajo ya validadas, no se recrean.
- **Se reinicia**: el proceso de Storyboard Studio en sí (Script → Assets → Storyboard) — el intento anterior mezcló español/inglés, el agente reescribió el guion sin pedírselo, y el reparto de shots por escena no coincidía con lo que necesitábamos.
- **Recomendación**: crea un **proyecto nuevo** en vez de borrar el anterior ("A Wound in the World") — así conservas el primero como referencia por si algo del nuevo sale peor, sin arriesgar nada.

## 1. Antes de pegar nada: prepara el material

Todo esto ya existe, solo hay que tenerlo a mano:

- **Guion en inglés, ya con precisión de dirección**: `produccion_cinematografica/2026-09-16_capitulo_1_planos_EN.md` — 38 shots, Visual/Camera/Sound/Dialogue por cada uno, en inglés.
- **Personajes que deben reconocerse por nombre exacto**: `MIGUEL`, `GABRIEL`, `PEWTER SENTINEL` (o `Pewter_Sentinel`, comprueba cuál usa tu proyecto), `LUCIFER` (no aparece en este capítulo, pero está en la lista de personajes por si el agente lo detecta en el guion original).
- **Localizaciones y props clave**: Serephis, The Buried Road, The Grove, The Ash Tree Clearing, Onyx Gates (flashback), Solmire, Vox Aeternum, Council Order — descripciones completas en `2026-09-16_storyboard_studio_cap01_extraido.md` secciones 4-5, por si el agente las genera mal y hay que corregirlas a mano.

## 2. Crear el proyecto

1. Nuevo proyecto en Storyboard Studio, nómbralo claramente (ej. "CAP01_v2" para distinguirlo del intento anterior).
2. Estilo: **3D-Animation** (el mismo que ya tienen todos los personajes aprobados — si el proyecto usa otro por defecto, cámbialo antes de generar nada).

## 3. Pestaña Assets — vincular, no recrear

Antes de tocar el Script, comprueba si Assets te deja **vincular personajes ya existentes del proyecto de Flow** en vez de generarlos de cero a partir del texto. Si Storyboard Studio comparte el mismo pool de "Caracteres" que vimos en el proyecto CAP01 original, Miguel/Gabriel/Pewter Sentinel deberían aparecer disponibles para enlazar directamente — eso evita que el agente les invente una versión nueva (que es probablemente el origen del problema de las alas).

Si no hay forma de vincular y el agente crea personajes nuevos desde el guion, tendrás que sustituirlos a mano por los ya aprobados antes de generar ningún panel.

## 4. Pestaña Script — pegar guion + instrucción, juntos

**No pegues solo el guion.** Pega primero esta instrucción, y justo después el contenido de `2026-09-16_capitulo_1_planos_EN.md`:

> *This is a finished, shot-by-shot technical script with exact camera direction, already in English. Do not rewrite, summarize, paraphrase, or reinterpret any of it. Structure it into scenes and shots exactly as written — one storyboard shot per numbered shot, in the same order. Use the Visual/Camera/Sound/Dialogue text of each shot as its panel description, unchanged. When a shot mentions @Miguel, @Gabriel, or @Pewter_Sentinel, link it to the existing character asset with that name in this project — do not create new characters or generate alternative physical descriptions for them.*

**Todo en inglés, sin mezclar con español** — ya lo tienes así en el archivo EN.

## 4.5. Lección de campo (2026-09-16): el campo "frames" NO se deriva del texto pegado

Confirmado en la práctica: aunque el Script pegado tenga exactamente 3 bloques "Shot" para una escena, Autofill Scene generó 6 — el campo numérico "frames" (arriba a la derecha del panel de escena) es independiente del texto y usa su propio valor por defecto, rellenando de más con contenido inventado (títulos que no existen en el guion, fuego que no está descrito, etc.) para llegar a esa cifra.

**Antes de pulsar Autofill Scene en cada escena**, poner manualmente el campo "frames" al número exacto de shots de esa escena según el guion (tabla ya usada en el prompt de generación): Escena 01=3, 02=4, 03=5, 04=4, 05=7, 06=5, 07=6, 08=6, 09=6, 10=6. Corregir el número después de generar no evita el problema — el objetivo es que no llegue a inventar los shots de más desde el principio.

Aun con el número correcto, un shot individual puede seguir reinterpretándose (visto: "Journey Through Ash" sin fuego generado con fuego, título cambiado). Para ese caso, no reintentar con el botón normal — usar `Mockup`/`Whisk` con los planos ya válidos de la misma escena como referencia de fondo/personaje, y pegar el texto del shot literal.

## 5. Revisar Assets generados (antes de generar ni un solo panel)

- Comprueba que **no se hayan duplicado** los personajes (que no haya un "Miguel" nuevo generado por el agente además del que ya tenías aprobado).
- Comprueba que el número de shots por escena coincide razonablemente con los 38 del guion — si el agente vuelve a reagrupar distinto (como pasó antes: 6+5+6+6+6+6=35), no es grave, pero anota la correspondencia como hicimos la vez anterior antes de rellenar cada casilla.

## 6. Pestaña Storyboard — generar panel a panel, con protocolo de fallo

Para cada shot, en este orden:

1. Genera el panel normal (texto → imagen).
2. **Revisa inmediatamente**: ¿el personaje tiene todas sus partes (alas incluidas)? ¿el fondo es el que toca?
3. **Si falla** (como pasó con las alas de Miguel): no sigas insistiendo con el mismo botón de generar. Cambia a:
   - `Mockup` — compón la imagen ya aprobada del personaje directamente sobre el fondo de la localización correspondiente.
   - o `Whisk` — sujeto (personaje) + escena (localización) + estilo, como alternativa a Mockup.
   - `Mask Magic` — si el fallo es puntual (falta un ala, un detalle del fondo), corrige solo esa zona por segmentación en vez de regenerar toda la imagen.
4. **Una vez tengas un panel de una escena perfecto**: usa `Shot Explorer` para sacar los demás ángulos de esa misma escena a partir de esa imagen ya validada, en vez de generar cada uno desde texto y arriesgarte a que falle otra vez.

## 7. De Storyboard a vídeo final

Storyboard Studio **no genera el vídeo final por su cuenta** — solo produce los paneles de imagen fija. Para cada panel ya aprobado:

1. Pásalo al flujo normal de **Escenas**.
2. `Vídeo → Fotogramas` (subiendo el panel como fotograma) o `Vídeo → Ingredientes` (si el personaje está bien vinculado) — modelo **Omni 1.1 Flash** por defecto (12 puntos/clip, con audio y lip-sync correctos, validado ya con los planos 5 y 7 del capítulo).
3. Menciona `@Miguel`/`@Gabriel`/`@Pewter_Sentinel` explícitamente en el texto del prompt de vídeo, no solo seleccionados.
4. Genera, revisa contra la ficha, añade a la línea de tiempo con "+ Añadir vídeo".
5. Reserva `Veo 3.1 - Lite/Quality` + "Alargar" (o Fotogramas encadenados) solo para los shots 35-37 (el push-in sobre Solmire) — el único tramo que necesita continuidad real de más de 8s.

## 8. Orden de trabajo recomendado

No generes los 38 shots de golpe. Sigue este orden, validando cada bloque antes de pasar al siguiente:

1. **Piloto**: 1 solo shot (ej. shot 16, Gabriel con diálogo) de principio a fin — Storyboard → Escenas → vídeo final. Si todo el flujo funciona bien aquí, escala.
2. Resto de la Escena 2 (shots 14-28, el diálogo completo).
3. Escenas 3-4 (transición a la arboleda + el Centinela).
4. Escena 5 (el fresno y Solmire — el único tramo con continuidad real).
5. Montaje final: unir los 38 clips en orden, pase de color, música/ambiente por facción.
