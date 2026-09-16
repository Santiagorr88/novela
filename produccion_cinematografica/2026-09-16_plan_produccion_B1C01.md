# Plan de producción — Vídeo narrado del Capítulo 1 "A Wound in the World"

> Fecha: 2026-09-16 (revisión 2, reemplaza la versión anterior de este mismo archivo)
> **Motivo de la reescritura**: la versión anterior de este plan se hizo sin saber que ya existe un pipeline de producción real (`character_library/`, `Libro1/audiolibro/`, `video_production/pipeline/`). Esta versión usa los activos reales del proyecto en vez de asumir que había que crearlos desde cero.

---

## 0. Qué cambia respecto al plan anterior

1. **El capítulo 1 real es más corto de lo que asumí antes.** El capítulo canónico actual (`Libro1/EN/01_A_Wound_in_the_World.md`, guion limpio en `Libro1/audiolibro/en/capitulo_01.txt`) **termina en el cliffhanger** "the grove vanished" — el descubrimiento de la espada, la visión cósmica y Lucifer están en el **Capítulo 2** ("The Tree Outside Time"), que es un vídeo aparte. No mezclar los dos en un solo plan.
2. **La narración ya está escrita, limpia y lista para TTS** — no hace falta adaptarla. `Libro1/audiolibro/en/capitulo_01.txt` (2.005 palabras, ≈13-15 min a ritmo audiolibro) es el guion definitivo, con convenciones ya fijadas (líneas de escena, cursivas aplanadas, sin markdown).
3. **Ya existe un piloto de audio real** (`capitulo_01_PILOTO.mp3` + `.srt`), aunque **desactualizado**: coincide con una versión anterior del texto (pre "pasada de estilo"), no con `capitulo_01.txt` actual. El `.srt` sirve como referencia de cómo se segmenta (frase a frase, con timestamps en ms), pero **hay que regenerar el audio contra el texto actual antes de fijar timings de plano**.
4. **Las voces ya elegidas no son ElevenLabs**, como asumía mi investigación general — son voces neuronales de Azure/Edge TTS: `en-US-AndrewMultilingualNeural` (EN) y `es-ES-AlvaroNeural` (ES), ya probadas en piloto. Mantener esa elección salvo que se decida cambiar.
5. **El banco de imágenes de personaje ya existe** para los 3 que aparecen en este capítulo — no hay que generarlo, solo usarlo:
   - `character_library/angeles/Miguel/canonical/` (face + body reference)
   - `character_library/angeles/Gabriel/canonical/` (face + body reference)
   - `character_library/otros/Pewter Sentinel/canonical/` (face + body reference) — **esta es la entidad sin rostro de la arboleda**, rediseñada hoy mismo (2026-09-16) de estatua de metal sólido a espíritu de niebla/vapor plateado. En el pipeline interno (`blocks.py`) se la conocía como bloque `GUARDIAN`.
6. **Estilo visual oficial: "3D-Animation"** (render 3D estilizado tipo cinemática de videojuego/Pixar-realista), **no** la ilustración pintada/anime que describen los `.txt` de `character_library/*/prompts/` — esos prompts están **desactualizados**, igual que el texto "Identidad inmutable" de los README (describen estados anteriores al rediseño de hoy). Confirmé el estilo actual viendo directamente las imágenes `canonical/face_reference.png` de Miguel, Gabriel y Pewter Sentinel.
7. **Sigue faltando `design_notes/2026-09-16_flow_storyboard_studio_cap01.md`** — los tres README (Miguel, Gabriel, Pewter Sentinel) lo señalan como la autoridad final del prompt de generación usado hoy en Flow. No está pusheado. Todo lo que propongo aquí sobre prompts de plano es mi mejor reconstrucción a partir de las imágenes canónicas reales, **no una copia de ese documento** — en cuanto lo tengas, lo reviso contra esto.

---

## 1. Identidad visual confirmada (visto directamente en las imágenes canónicas)

### Miguel (`character_library/angeles/Miguel/canonical/`)
Hombre adulto, pelo corto gris-plateado peinado hacia atrás con volumen, ojos con brillo cian eléctrico concentrado en iris/pupila, rostro anguloso y serio. Armadura dorada ceñida con hombreras en forma de ala grabadas con plumas, capa interior azul medianoche, emblema de estrella de ocho puntas cian-blanca luminosa en el pecho. Dos alas blancas enormes con leve iridiscencia azulada. **Nota de continuidad de la escena**: en este capítulo el peto lleva "cracked gold... plate no armorer... ever managed to weld shut since Onyx Gates" — la armadura debe mostrarse con una grieta visible (contradice la versión "sin grietas" que describe el README viejo; confirmar en el prompt final que esta escena específica necesita la variante agrietada).

### Gabriel (`character_library/angeles/Gabriel/canonical/`)
Hombre adulto, pelo negro largo liso con raya al centro (cae hasta el pecho, más largo de lo que decía el README viejo), ojos azul zafiro naturales sin brillo sobrenatural, rostro sereno y fraterno. Túnica azul zafiro con bordado de plata en motivos de pluma, hombreras de plata pulida, alas blancas inmaculadas. Lleva `Vox Aeternum` (bastón de plata liso, ~1,9 m) — en esta escena concreta el texto dice que lleva además **un pergamino sellado con cera negra oculto contra las costillas**, que no muestra ni menciona — detalle visual a incluir en los planos donde se le vea de perfil/espalda.

### Pewter Sentinel / GUARDIAN (`character_library/otros/Pewter Sentinel/canonical/`)
Silueta humanoide alta y esbelta de niebla plateada y vapor color peltre, sin piernas definidas (se disuelve en humo), flota sobre el suelo. Rostro liso y casi sin rasgos, dos ojos tenues blanco frío brillando desde la bruma. Fragmentos metálicos en forma de hoja y cintas de peltre fusionados en hombros/pecho. Sin ropa convencional.

**Localización — la Arboleda y Serephis**: no tiene ficha propia en `character_library`; usar la descripción del texto (árboles de metal pálido sin sombra, luz uniforme; desierto de vidrio negro, cielo enfermizo) de forma consistente en todos los planos exteriores.

---

## 2. Desglose real en escenas (capítulo 1 completo, `capitulo_01.txt`)

| # | Escena | Contenido real | Técnica recomendada |
|---|---|---|---|
| 1 | **La marcha (apertura)** | 12 días cruzando Serephis, armadura agrietada desde Onyx Gates, el vacío en el pecho, "¿qué me fue arrebatado?" | Narrado / B-roll, plano general + primeros planos de detalle (mano al pecho, grieta en el peto) |
| 2 | **La carretera enterrada** | Descubre piedra bajo la arena, teoría de que Serephis fue un reino que se autodestruyó como arma | Narrado / B-roll, planos de detalle de la piedra + plano general del "camino ancho para diez" |
| 3 | **Llegada de Gabriel** | Acorde de armonía, Gabriel aparece, alivio físico de Miguel, vergüenza | Transición — luz suave entrando en el encuadre |
| 4 | **El diálogo completo** | Preocupación del Concilio, el pergamino sellado no usado, "me creen un necio", flashback de Onyx Gates (3 noches, "no gritas pidiendo ayuda..."), "vuelve a casa" / "no puedo" | Shot/reverse-shot clásico — **candidata a dramatización con voces propias** (es la escena más larga y emocional del capítulo) |
| 5 | **Despedida de Gabriel** | Luz que se atenúa, lágrima de luz, desaparece con el pergamino sin usar | Plano corto, Gabriel se disuelve en el "espacio entre mundos" |
| 6 | **Marcha hacia la arboleda** | Transición sensorial (arena caliente → musgo frío), llegada a la arboleda de metal sin sombras | Narrado / B-roll atmosférico, cámara lenta constante |
| 7 | **El Centinela (nueva escena, no estaba en mi plan anterior)** | La figura de niebla aparece a 40 pasos, Miguel dice "vengo por lo que es mío", el Centinela no responde, se gira para seguir mirándolo mientras pasa | Plano fijo/lento — el Centinela casi no se mueve, contraste deliberado con el resto |
| 8 | **El fresno y Solmire (cierre del capítulo)** | El gran fresno, la espada de luz viva, Miguel duda, toca la empuñadura | **"Oner" con Frames-to-Video encadenado** — este capítulo termina en cliffhanger justo aquí ("the grove vanished"), sin resolver — no se ve la espada desenvainada todavía |

**Duración estimada total: ~13:20-15:00 min** (2.005 palabras ÷ ~140-150 ppm), consistente con el piloto de audio antiguo (14:56 min para un texto de longitud similar).

---

## 3. Próximos pasos concretos (en orden)

1. **Conseguir `design_notes/2026-09-16_flow_storyboard_studio_cap01.md`** — sigue siendo el bloqueo principal para tener prompts de plano 100% fieles en vez de mi reconstrucción visual. Si puedes pushearlo (o pegarlo aquí), reviso y ajusto todo lo de la sección 1.
2. **Regenerar el audio piloto** contra el texto actual de `capitulo_01.txt` (el `.srt` existente usa una versión de texto ya superada por la pasada de estilo) — con eso se fija el timing real de los 8 bloques de la tabla.
3. **Escena piloto**: producir primero la **Escena 4** (el diálogo completo Miguel/Gabriel) de principio a fin — es la más larga, la más emocional, y la que mejor valida que los assets canónicos de Miguel y Gabriel funcionan bien en Flow con el estilo "3D-Animation".
4. Si se confirma que el bloque `GUARDIAN` de `blocks.py` ya tiene lógica de generación para el Pewter Sentinel, reutilizarla en vez de generar los planos de la Escena 7 a mano.
5. Seguir con el resto de escenas en orden narrativo, montaje final con narración continua de fondo (nunca cortada) y planos visuales cortando en los límites de frase del `.srt` regenerado.

---

## 4. Lo que sigue igual de la investigación general

Las técnicas transversales del documento `produccion_cinematografica/2026-09-15_veo3_investigacion.md` (encadenado de clips sin corte visible, J-cuts/L-cuts, prompt sandwich, cut-hide technique, retención/pacing) siguen aplicando igual — lo único que cambia aquí es que ahora se aplican sobre activos y guion **reales del proyecto**, no sobre una reconstrucción mía.
