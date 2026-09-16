# Plan de producción — Vídeo narrado del capítulo B1C01 "El Árbol Fuera del Tiempo"

> Fecha: 2026-09-16
> Basado en: `design_notes/2026-09-15_veo3_video_cinematografico_investigacion.md` (investigación completa) y el texto real de `project/Chronicles_of_the_Sundering_Judgment/chapters/ES/B1C01_ES_v2.md` (2.244 palabras).
> Formato: **narrado** (voz en off continua + B-roll de Veo3), con 1 escena candidata a dramatización opcional (§9.3 del documento de investigación).

---

## 1. Por qué B1C01 es un buen piloto

- 2.244 palabras ÷ 145-155 palabras/min de narración ≈ **~15 minutos** — encaja justo en el target de 15-20 min sin necesitar cortar ni alargar apenas nada.
- Ya tiene **8 escenas naturales** con tonos muy distintos (soledad/marcha, diálogo, descubrimiento, clímax visual, caos cósmico, villano) — es un buen "stress test" de casi todas las técnicas documentadas en la investigación, no solo B-roll plano.
- Los 3 personajes que aparecen (Miguel, Gabriel, Lucifer) ya tienen ficha visual completa en `content/lore/personajes.md` — no hace falta diseño de personaje desde cero, solo traducir la ficha a prompt.

## 2. Desglose en escenas (guion de narración = prosa casi literal, sección 9.2 paso 1)

La prosa del capítulo ya está escrita en narrador en tercera persona con diálogo integrado (`—dijo Miguel—`), así que el guion de narración **no necesita reescritura**, solo la decisión de leer los diálogos con inflexión narrativa (guion 9.2) salvo que se dramatice la Escena 2 (ver más abajo). No se recorta nada: la prosa ya tiene ritmo ajustado (ver `expansion_guidelines.md`/`beat-planner` del proyecto).

| # | Escena | Contenido | Palabras aprox. | Duración aprox. | Técnica recomendada | Planos aprox. (5-8s c/u) |
|---|---|---|---|---|---|---|
| 1 | **La marcha por Serephis** | Miguel caminando por el desierto agrietado, dolor interno, monólogo sobre lo que le falta | ~410 | ~2:40 | Narrado / B-roll, montaje normal (§9.2) | 20-24 |
| 2 | **Encuentro con Gabriel** | Llegada de Gabriel, diálogo completo, decisión de Miguel de continuar solo | ~520 | ~3:20 | Shot/reverse-shot clásico (§3) — **candidata a dramatización opcional** con voces propias de Miguel/Gabriel (§9.3) | 20-26 |
| 3 | **Camino a la arboleda** | Transición del desierto a la arboleda de metal, atmósfera, tensión de "emboscada" | ~380 | ~2:30 | Narrado / B-roll atmosférico, cámara lenta constante | 18-22 |
| 4 | **El fresno y Solmire** | Descubrimiento de la espada, acercamiento, duda antes de tocarla | ~380 | ~2:30 | **"Oner" con Frames-to-Video encadenado** (§2.2) — es el primer clímax visual del capítulo | 15-18 (planos más largos, algunos extendidos >8s) |
| 5 | **La visión cósmica** | Expulsión del cuerpo, caos cósmico, la risa, la verdad de la espada | ~380 | ~2:30 | **Montaje rápido con cortes visibles a propósito** (§7.3 — el corte abrupto ayuda al caos, no ocultarlo) | 25-30 (planos muy cortos, 3-5s) |
| 6 | **Desenvaina la espada** | Vuelta al cuerpo, desenvaina, el árbol gime, el poder lo llena | ~330 | ~2:10 | Oner corto (§2.2) + primeros planos de reacción | 12-15 |
| 7 | **Lucifer en su cámara** | Escena corta de contraste, Lucifer siente el eco, sonríe | ~150 | ~1:00 | Plano corto, estático, casi sin movimiento (contraste deliberado con el resto) | 6-8 |
| 8 | **Cierre** | Vuelta a la arboleda, línea de cierre | ~40 | ~0:20 | Plano único, fundido a negro | 1-2 |

**Total estimado: ~2.590 palabras narradas efectivas (incluye diálogo leído) ≈ 15:40-16:30 min, ~117-145 planos.** Coincide con la estimación de coste de la sección 8 de la investigación (~110-150 clips, ~$675-900 vía API o ~1 mes de cuota Ultra).

## 3. Banco de imágenes de personaje necesario (sección 9.5 / 15.2 de la investigación)

Antes de generar un solo plano de vídeo, construir el banco de imágenes fijo por personaje (reutilizable en *todos* los capítulos futuros, no solo este):

| Personaje | Ficha base (`personajes.md`) | Imágenes mínimas a generar |
|---|---|---|
| **Miguel** | 2.25m, armadura dorada radiante con grietas antiguas, cabello blanco cenizo, ojos de llama azulada, alas radiantes, espada *Solmire* (luz viva, no metal) | Hero (plano medio, luz neutra) + perfil + 3/4 + cuerpo completo + variante "dolor/agotamiento" (para Escena 1) + variante "determinación" (Escenas 4-6) + variante con Solmire ya desenvainada |
| **Gabriel** | 1.95m, túnicas azul/plata sin armadura, cabello negro liso, ojos de zafiro puro | Hero + perfil + 3/4 + variante "luz suave alrededor" (llegada) + variante "pena/despedida" (final del diálogo) |
| **Lucifer** | 2.20m, belleza celestial corrupta, cabello blanco plateado, ojos rojo vino, piel pálida impecable, alas negras como el vacío | Hero (sentado, cámara oscura) + variante "sonrisa lenta" (única imagen que necesita realmente, la escena es corta y casi estática) |

**Localizaciones/objetos recurrentes** (tratar igual que un personaje, mismo banco): el desierto de Serephis (cielo color moretón, arena de vidrio negro), la arboleda de metal pálido sin sombras, el fresno con Solmire incrustada, la cámara oscura de Lucifer con el "instrumento de relojería".

**Cómo generarlas**: imagen hero con Imagen 3/Flow o Nano Banana → variantes conversacionales con Nano Banana pidiendo "el mismo Miguel, ahora de perfil / con expresión X / en pose Y" (§15.2) → subir todo el banco a Flow como Ingredients.

## 4. Ejemplos de prompt trabajados (plantilla de 7 campos, sección 10)

Uno por escena representativa, para usar como molde del resto de planos de esa escena:

**Escena 1 — plano de apertura:**
```
Subject: Miguel, Comandante Supremo — 2.25m, armadura dorada radiante con grietas antiguas, cabello blanco cenizo corto, ojos de llama azulada, alas radiantes plegadas, sin arma visible en la mano
Action: camina despacio por arena vidriada negra, mano derecha sube instintivamente al pecho
Scene: desierto de Serephis, cielo color moretón en curación, estrellas palpitando fuera de ritmo, calor visible deformando el aire
Style: plano general, lente 35mm, cámara estática con leve deriva orgánica, tono cinematográfico oscuro
Dialogue: (ninguno)
Sounds: viento seco constante, crujido de vidrio bajo las botas, silencio opresivo de fondo
Technical: no subtitles, no on-screen text, no watermark, no blurry faces
```

**Escena 2 — plano de Gabriel (reverse-shot):**
```
Subject: Gabriel, Arcángel de la Voz Divina — 1.95m, túnica fluida azul y plata sin armadura, cabello negro liso, ojos de zafiro puro
Action: habla con preocupación contenida, una mano se alza hacia Miguel y vacila antes de bajar
Scene: mismo desierto de Serephis, luz suave dorada floreciendo alrededor de Gabriel rompiendo la penumbra
Style: primer plano, 50mm, cámara estática, foco en el rostro
Dialogue: Gabriel dice: "El Concilio está preocupado, Miguel."
Sounds: acorde de armonía suave al fondo, viento del desierto atenuado
Technical: no subtitles, no on-screen text, no watermark
```

**Escena 4 — el fresno (plano largo, candidato a Frames-to-Video encadenado):**
```
Subject: el gran fresno — corteza de lava enfriada, raíces bebiendo de un estanque de luz estelar; incrustada en el tronco, Solmire: no metal, luz viva solidificada
Action: push-in lento y constante hacia la espada, sin corte
Scene: arboleda de metal pálido, luz uniforme sin sombras, quietud pesada y atenta
Style: plano medio a primer plano, dolly-in lento continuo, 35mm
Dialogue: (ninguno, narración en off por encima)
Sounds: zumbido grave apenas audible, silencio de "biblioteca", ausencia total de brisa
Technical: no subtitles, no on-screen text, no watermark
```

**Escena 5 — visión cósmica (plano corto, corte visible intencional):**
```
Subject: campo estelar caótico, supernovas apagándose como acero al rojo sumergido en oscuridad, un martillo del tamaño de una estrella
Action: la gravedad se dobla como herramienta, no como ley; destellos rápidos de escala imposible
Scene: espacio cósmico amoral, sin horizonte, sin referencia de escala humana
Style: planos muy cortos (3-4s), cámara handheld errática, cortes duros intencionados
Dialogue: (ninguno)
Sounds: risa jubilosa e indiferente entrelazada con un tañido de yunque cósmico
Technical: no subtitles, no on-screen text, no watermark, no text overlays
```

**Escena 7 — Lucifer:**
```
Subject: Lucifer — 2.20m, belleza celestial corrupta, cabello blanco plateado, ojos rojo vino, piel pálida impecable, alas negras como el vacío, sin armadura, ropa de corte elegante oscuro
Action: deja un pequeño instrumento de relojería, ladea la cabeza escuchando, sonrisa lenta y genuina
Scene: cámara privada tallada en sombra, ambición antigua, muy poca luz, velas o luz ambarina puntual
Style: primer plano estático, casi sin movimiento de cámara, contraste deliberado con el resto del capítulo
Dialogue: Lucifer dice: "Así que... una de las viejas canciones se está cantando de nuevo. Qué interesante."
Sounds: silencio casi total, tictac apenas perceptible del instrumento
Technical: no subtitles, no on-screen text, no watermark
```

## 5. Narración: configuración de voz

- Modelo: ElevenLabs Multilingual v2/Studio (o v3 si se necesita IPA para nombres propios — sección 13).
- Voz: elegir una de la colección "Epic Voices" o "Narrator Voices", probar con el párrafo de apertura real del capítulo antes de comprometerse.
- Stability: modo "Robust" / alto (~70-80%), similarity ~75%, style en 0 al inicio.
- Diccionario de pronunciación mínimo para este capítulo: `Miguel, Gabriel, Serephis, Solmire, Lucifer` (los demás nombres del universo no aparecen en B1C01, se puede ampliar capítulo a capítulo).
- Generar por escena (8 llamadas, no una sola de 15 min) con la misma configuración exacta guardada como preset.

## 6. Orden de producción recomendado (próximos pasos concretos)

1. **Banco de imágenes**: generar hero + variantes de Miguel y Gabriel primero (son los que más planos necesitan). Lucifer puede esperar.
2. **Piloto real**: producir solo la **Escena 2** completa (diálogo Miguel/Gabriel, ~3:20 min, ~20-26 planos) de principio a fin — narración, planos, montaje, color — como ya habíamos acordado antes de comprometer el capítulo entero. Sirve para calibrar tiempo real por plano y validar que el banco de imágenes funciona.
3. Si el piloto de la Escena 2 sale bien, seguir con el resto de escenas en el orden de la tabla (1, 3, 4, 5, 6, 7, 8).
4. Montaje final: unir las 8 escenas, pase de color (§5 del documento de investigación) y capa de música/ambiente por facción (§14.1).

---

¿Empezamos por el banco de imágenes de Miguel y Gabriel, o prefieres que primero te deje el guion de narración de la Escena 2 ya troceado en las líneas exactas que irían a ElevenLabs?
