# Escena piloto — El ruego del Concilio (Miguel / Gabriel), Capítulo 1

> Fecha: 2026-09-16
> Primera escena a producir de principio a fin, para validar que los assets canónicos reales (Miguel, Gabriel) funcionan en Flow con el estilo "3D-Animation" antes de comprometer el capítulo completo.
> Texto fuente: `Libro1/audiolibro/en/capitulo_01.txt` (fragmento correspondiente a la llegada y despedida de Gabriel).
> Voces de personaje (de `content/lore/personajes.md`): **Miguel** — grave y serena, autoridad que no necesita alzarse, cansancio noble en las pausas. **Gabriel** — dulce, cálida, fraternal, la armonía se oye antes que la intención.

---

## 1. Por qué esta escena y no otra

- Es la más larga y emocionalmente densa del capítulo (~520 palabras, ~3:20 min de las ~13-15 min totales).
- Usa solo 2 personajes, ambos ya con banco de imágenes canónico completo — cero trabajo de diseño pendiente.
- Contiene el reto técnico central de este documento: diálogo sostenido entre dos personajes que debe leerse fluido, más un flashback incrustado (Onyx Gates) que rompe el espacio/tiempo de la escena — buena prueba de las técnicas de corte de la investigación general.
- Si funciona aquí, el resto del capítulo (mayoritariamente B-roll narrado de un solo personaje) es más simple, no más complejo.

## 2. Decisión de formato: dramatizado, no narrado puro

A diferencia del resto del capítulo (que puede ir en narración pura sobre B-roll), esta escena se dramatiza con **voces de personaje propias** en vez de que el narrador lea el diálogo integrado — es la escena que más se beneficia de oírse como una conversación real entre hermanos. El resto del capítulo (marcha, carretera enterrada, arboleda, Centinela, fresno) se queda en narración pura tal como se generó en el audiolibro estándar.

**Implicación de voz**: esta escena necesita 3 pistas de audio distintas (narrador + Miguel + Gabriel), no 1. Las voces piloto de Azure ya elegidas (`en-US-AndrewMultilingualNeural` para narrador) sirven para el resto del capítulo; para Miguel y Gabriel aquí hace falta decidir/asignar voces de personaje diferenciadas (Azure Neural u otro proveedor) — pendiente de decisión, no bloqueante para montar el storyboard visual primero.

## 3. Guion segmentado en planos

Convención de bloque: **N — [ROL] duración aprox. — técnica**. ROL = `NARR` (narrador), `MIGUEL`, `GABRIEL`, `FLASHBACK` (inserto visual del recuerdo de Onyx Gates, sin diálogo nuevo, solo lo que ya se está narrando/hablando por encima).

| # | Rol | Línea / contenido | Plano | Técnica |
|---|---|---|---|---|
| 1 | NARR | "The stillness of the plain broke on a chord of harmony... Gabriel arrived..." | Luz suave entrando por el borde del encuadre sobre Miguel de espaldas | Corte oculto por entrada de luz (cut-hide, §2.2 investigación) |
| 2 | NARR | "...his robe of blue and silver free of the armor's heaviness." | Plano medio de Gabriel apareciendo, alas plegándose | — |
| 3 | NARR | "Miguel felt love, and close behind it, the weight of his own pride..." | Primer plano de Miguel, expresión mixta (alivio/vergüenza) | Usar `supporting_references/expressions.png` de Miguel como referencia de la expresión exacta |
| 4 | NARR | "He straightened. The exhaustion would not be hidden." | Miguel se yergue, cámara capta el peto agrietado (nota de continuidad, §1 del plan de capítulo) | — |
| 5 | GABRIEL | "The Council is concerned, Miguel." | Primer plano de Gabriel, voz dulce/cálida con la tensión de la súplica ya audible | Shot/reverse-shot arranca aquí |
| 6 | GABRIEL | "They fear this is a deception... Your absence puts fear in the Host." | Gabriel, mismo plano o leve variación de ángulo | — |
| 7 | MIGUEL | "They think me a fool. Or a traitor." | Reverse-shot, primer plano de Miguel, voz grave/áspera ("rough, like sand dragged by the wind" — detalle explícito del texto) | — |
| 8 | GABRIEL | "They think you are their general." + el gesto del pergamino sellado | Plano medio de Gabriel, la mano se mueve y **se ve fugazmente el pergamino sellado con cera negra contra sus costillas** — no lo nombra, no lo muestra del todo | Detalle visual nuevo — clave para el lore, no estaba en mi plan anterior |
| 9 | NARR | "The shift from envoy to brother struck deeper than any order could have." | Plano de los dos juntos, más cercano que antes | — |
| 10 | FLASHBACK | "Onyx Gates had cost him his wing..." — fortaleza cayendo, Gabriel arrodillado 3 noches cauterizando el ala con su propia luz | Textura visual distinta: luz de fuego/naranja en vez de la luz fría de Serephis, cámara más inestable | Corte de entrada/salida del flashback oculto en un destello de luz (cut-hide) |
| 11 | FLASHBACK (voz en off, Gabriel del pasado) | "Because you don't yell for help in the voice you use for people you love. You go yourself." | Primer plano de Gabriel más joven/mismo diseño, luz cálida de la cauterización | Única línea de diálogo del flashback — el resto es narración |
| 12 | NARR | vuelta al presente — "Gabriel's gaze softened; his hand rose, hesitated... and fell back" | Vuelta a la luz fría de Serephis, plano de la mano de Gabriel bajando sin completar el gesto | Salida del flashback con el mismo tipo de corte oculto que la entrada (simetría) |
| 13 | GABRIEL | "Come home. Whatever this wound is, we face it together. As we always have." | Primer plano de Gabriel, máxima calidez | — |
| 14 | MIGUEL | (silencio, duda) — "For a moment Miguel wavered..." | Miguel, primer plano, conflicto visible | — |
| 15 | MIGUEL | "I cannot. This call is a command more fundamental than any the Council can give me. It is a truth I must find, or I am nothing." | Miguel, resolución "terrible y cristalina" — mirar directamente a Gabriel por primera vez desde que llegó | Momento de mayor intensidad — candidato a plano más largo/lento |
| 16 | NARR | "Gabriel did not argue. His light dimmed a fraction. A single tear of light traced his cheek." | Primer plano de Gabriel, la lágrima de luz | — |
| 17 | GABRIEL | "May you find what you seek, brother." | Último plano de Gabriel, ya empezando a disolverse "en el espacio entre mundos" | — |
| 18 | NARR | "Miguel stood looking at the empty space, wondering what exactly he had just been spared." | Plano final, Miguel solo, el hueco donde estaba Gabriel | Cierre de escena — transición a la siguiente (marcha hacia la arboleda) |

**Total: 18 planos × ~5-8s ≈ 2:00-2:30 min visual**, más los tramos donde el diálogo se alarga dentro de un mismo plano (5, 8, 15) — encaja con la estimación de ~3:20 de la tabla del plan de capítulo.

## 4. Prompts de plano trabajados (estilo "3D-Animation", convención real del proyecto)

Siguiendo la convención real observada en `character_library/*/prompts/*.txt` (prosa en inglés, referencia explícita a las imágenes canónicas adjuntas como autoridad de identidad) — **no** el formato JSON de 7 campos de la investigación general, que era una convención genérica mía antes de conocer la convención real del proyecto.

**Plano 5 (Gabriel, primer plano, arranque del diálogo):**
```
Use the attached canonical face and body references for GABRIEL as absolute identity authorities. Preserve exactly his long black hair parted at the center falling past his chest, natural sapphire-blue eyes with no supernatural glow, calm fraternal expression carrying a soldier's fatigue. He wears his sapphire-blue and silver robe with feather-motif silver embroidery, silver pauldrons, holding Vox Aeternum loosely in his right hand.

Action: Gabriel speaks with gentle, warm concern, the strain of a plea just audible beneath the harmony of his voice.

Scene: same Serephis wasteland, sickly-colored sky, soft cool light spreading from Gabriel pushing back the gloom around him.

Style: close-up, eye-level camera, static with a barely perceptible breathing drift, 3D-Animation style matching the canonical references exactly.

Dialogue: Gabriel says: "The Council is concerned, Miguel."

Sounds: a low harmonic chord under his voice, faint desert wind.

Technical: no subtitles, no on-screen text, no watermark.
```

**Plano 7 (Miguel, reverse-shot):**
```
Use the attached canonical face and body references for MIGUEL as absolute identity authorities. Preserve exactly his ash-grey swept-back hair, electric-cyan glowing eyes concentrated in iris and pupil, severe handsome weathered face. Show his radiant-gold armor with a visible crack across the breastplate near the sternum star emblem (Onyx Gates damage — this shot requires the cracked variant, not the pristine base form).

Action: Miguel's jaw tightens, voice rough with disuse.

Scene: same Serephis wasteland, harsh flat light, no shadows from the grove yet.

Style: close-up reverse-shot matching plano 5's eyeline, static camera, 3D-Animation style.

Dialogue: Miguel says: "They think me a fool. Or a traitor."

Sounds: same faint wind bed as previous shot, no music.

Technical: no subtitles, no on-screen text, no watermark.
```

**Plano 10 (flashback, Onyx Gates — textura distinta a propósito):**
```
Use the attached canonical face and body references for GABRIEL and MIGUEL as absolute identity authorities, applying MIGUEL's active-battle-damage variant for this shot (NOT the cold/healed `states/burned_left_wing/` — that one is explicitly scarred-and-old; this flashback needs fresh fire/embers/smoke, see `../variantes_por_personaje/Miguel.md` for the exact edit prompt, pendiente de generar).

Action: a fortress collapsing into an abyss, orange firelight, Gabriel kneeling beside a fallen Miguel, cauterizing a broken wing with his own light, three nights compressed into one continuous gesture.

Scene: burning fortress interior, unstable ground, embers drifting.

Style: handheld camera, warmer and rougher than the rest of the chapter — this is a memory, it should feel visually distinct from the cold present-day light of Serephis. 3D-Animation style.

Dialogue: (none in this shot — narration plays over it)

Sounds: distant structural groaning, fire crackling, muffled.

Technical: no subtitles, no on-screen text, no watermark.
```

## 5. Nota de continuidad importante

El plano 4/7 requiere la **variante de armadura agrietada** de Miguel (grieta desde Onyx Gates, explícita en el texto: *"the cracked gold of his armor, plate no armorer in the Host had ever managed to weld shut since the Onyx Gates campaign"*). El README actual de Miguel describe la forma base **sin** grieta ("La forma base no lleva bandolera, no tiene una grieta en el peto"). Esto no es una contradicción — es el estado narrativo correcto para *este* capítulo específicamente, pero hay que generarlo como variante explícita, no como la imagen `canonical/body_reference.png` a secas.

**Ver `../variantes_por_personaje/Miguel.md`** para el registro completo de todas las variantes de Miguel necesarias en este capítulo (armadura agrietada + la variante distinta de herida activa del flashback del plano 10) y su estado de generación — esa es ahora la fuente de verdad de estos prompts, no este documento.

## 6. Siguiente paso

Con este storyboard ya se puede generar el primer lote de imágenes fijas (planos 1-18) en Flow usando los canonical de Miguel y Gabriel, y después animarlas con Frames-to-Video. En cuanto tengas 2-3 planos generados, los reviso contra este documento antes de seguir con el resto.

## 7. Cómo generarlo en Flow, paso a paso

1. **Entra en `labs.google/flow`** con la cuenta Google que tenga la suscripción (Pro/Ultra) o usa la cuota gratuita de 50 puntos/día si solo quieres probar el plano 5 primero.
2. **Crea un proyecto nuevo** para este capítulo (ej. "Cap01 — Escena diálogo").
3. **Sube los Ingredients de los dos personajes** — panel de "Ingredients" (o icono `+`): sube `character_library/angeles/Miguel/canonical/face_reference.png` y `body_reference.png` como un Ingredient llamado `Miguel_canonical`; haz lo mismo con Gabriel → `Gabriel_canonical`. Esto te deja referenciarlos luego escribiendo `@Miguel_canonical` / `@Gabriel_canonical` en cualquier prompt del proyecto.
4. **Resuelve primero el problema de la armadura agrietada (plano 4/7)**: antes de generar vídeo, sube `body_reference.png` de Miguel a la edición de imagen conversacional de Flow (Nano Banana) y pide: *"the same Miguel, but with a visible crack across the gold breastplate near the sternum emblem, from the Onyx Gates campaign — everything else identical."* Cuando la imagen resultante te convenza, guárdala como Ingredient nuevo `Miguel_cracked_armor` y úsala en los planos que lo necesiten (4, 7, y cualquier otro de Miguel en este capítulo, ya que la grieta es su estado durante todo el capítulo 1).
5. **Selecciona calidad "Quality" (Veo 3 completo)**, no "Fast" — estos planos llevan diálogo con audio y lip-sync, que Fast no genera bien.
6. **Genera plano a plano**, en orden (1→18): para cada uno, pega el prompt correspondiente de la sección 4 de este documento (o escribe el resto siguiendo el mismo patrón), referenciando `@Miguel_canonical`/`@Miguel_cracked_armor`/`@Gabriel_canonical` según toque. Como son cortes distintos (cambios de plano, no una toma continua), genera cada uno como clip nuevo desde el Ingredient — **no** hace falta Frames-to-Video encadenado aquí, eso es solo para cuando quieras alargar un mismo plano más allá de 8s sin corte.
7. **Revisa cada clip contra la ficha** antes de pasar al siguiente: ¿la cara/pelo/armadura coinciden con el canonical? ¿la voz suena "grave y serena" (Miguel) / "dulce y cálida" (Gabriel) como pide `personajes.md`? Si algo deriva, regenera ese plano repitiendo el Ingredient, no sigas adelante con un plano que no cuadra.
8. **Descarga cada clip** y nómbralo `cap01_esc_dialogo_plano01.mp4`, `...plano02.mp4`, etc., siguiendo la numeración de la tabla — así al montar en DaVinci/Premiere el orden es evidente.
9. Cuando tengas los 18 descargados, pásamelos (o dime que están listos) y reviso el conjunto antes de pasar a generar el audio de las voces de Miguel/Gabriel y montar la escena completa.
