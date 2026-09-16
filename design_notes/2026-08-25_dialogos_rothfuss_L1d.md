# Pasada de diálogo modo Rothfuss — Libro1, capítulos 40-50 (EN+ES)

Fecha: 2026-08-25
Tramo: Libro1/EN/40-50 y Libro1/ES/40-50 (el 51 no se tocó — usado solo como modelo)

## Calibración

Antes de tocar nada, releí `git show 816b738` (el commit del autor sobre el cap. 51,
espejado EN↔ES) y el capítulo 51 completo en ambos idiomas. Conclusión: los retoques
del autor son *quirúrgicos* — variación de verbo ("said"→"replied", "dijo"→"replicó"),
recorte de ripios en los beats, y una reestructuración puntual de un beat-antes-de-cita
("Camael's voice — había venido después de todo...", "era la voz de Camael..."). No hay
exterminio de atribuciones ni reescritura de réplicas.

## Hallazgo principal: el corpus 40-50 ya es mayormente narración, no diálogo

Conteo de "said"/"dijo" (solo como etiqueta de atribución, no como verbo narrativo
genérico) por capítulo:

| Cap | EN said | ES dijo | Diálogo real (líneas) |
|-----|---------|---------|------------------------|
| 40  | 1       | 1       | 1 (única línea de todo el capítulo) |
| 41  | ~6      | ~6      | 7 (repartidas en 65 párrafos de interioridad) |
| 42  | 1       | 1       | 1 (única línea) |
| 43  | 0       | 0       | 0 (capítulo puramente descriptivo, sin diálogo) |
| 44  | 1→0*    | 1→0*    | 1 (única línea) |
| 45  | 2→1*    | 3→2*    | 3 (escena Camael/Jeremiel) |
| 46  | 0 (tags reales) | 0 | 4 (intercambio Gabriel/ayudante, ya sin etiquetas) |
| 47  | 0 (tags reales) | 0 | 1 (única línea, ya con verbo variado "muttered"/"murmuró") |
| 48  | 1→0*    | 1→0*    | 3 (duelo — réplicas protegidas) |
| 49  | 1       | 1       | 5-6 (Gabriel/Uriel/heraldo, ya con beats y verbos variados) |
| 50  | 4       | 4       | ~15 (Anael/Barachiel, Anael/Ezihel — ya en estilo Rothfuss ejemplar) |

(*) tras mi edición de hoy.

La mayoría de los "said"/"dijo" que arrojaba el grep bruto eran usos narrativos
genéricos del verbo ("that silence itself said more...", "he said nothing further",
"podría decirse que...") y no etiquetas de diálogo — no requerían tocarse.

## Ediciones aplicadas (6 archivos, un cambio quirúrgico cada uno)

Todas espejadas EN→ES el mismo día, mismo criterio.

1. **Cap. 44 — La Víspera de la Ruina**
   `"Gabriel said quietly, "He has the spear. He is breaking them.""` →
   `"Gabriel kept his voice quiet. "He has the spear. He is breaking them.""`
   (beat en vez de etiqueta; réplica intacta)
   ES espejo: `Gabriel dijo en voz baja:` → `Gabriel mantuvo la voz baja.`

2. **Cap. 45 — El Frente de la Desesperación**
   Se retiró el `"...," he said. "..."` redundante en la respuesta de Camael a
   Jeremiel ("Fear is just another enemy[, he said.] I haven't given this one a
   name yet."), porque el beat previo ("Camael considered the question...") ya
   ancla al hablante sin ambigüedad — ping-pong de dos limpio.
   ES espejo: se retiró `—dijo—` del mismo lugar.
   (La línea de apertura de Jeremiel, "If Hell's cooks are half as bad as ours,"
   he said — se dejó intacta: es la primera réplica del intercambio de dos y debe
   quedar anclada, regla 5.)

3. **Cap. 48 — La Caída (duelo — réplicas protegidas)**
   `"This power was never yours," Belial said, Lament held steady, [...]` →
   `Belial held Lament steady. "This power was never yours." The words carried [...]`
   Solo se movió la etiqueta a un beat previo y se convirtió el resto en oración
   propia; **las palabras exactas de las dos réplicas protegidas no se tocaron**:
   "This power was never yours." / "Then tell me whose it is." (ES: "Este poder
   nunca fue tuyo." / "Entonces dime de quién es.") Se verificó que la nota del
   autor sobre este duelo ("réplicas protegidas... etiquetas podés aligerar pero
   jamás sus palabras") se respetó al pie de la letra.

## Capítulos sin cambios (y por qué)

- **40, 42**: una sola línea de diálogo en todo el capítulo — no hay cadena que cazar.
- **43**: cero diálogo — capítulo enteramente descriptivo (la Cumbre).
- **41**: coral de 3 (Gabriel/Miguel/Iofiel) pero con solo 7 líneas de diálogo
  repartidas en un capítulo dominado por narración interior; cada primera réplica
  ya está anclada (por etiqueta o por beat previo), tal como pide la regla 5 para
  corales. No detecté cadena mecánica que ameritara intervención sin inventar beats.
- **46, 47, 49, 50**: ya ejemplifican el modelo objetivo — beats en vez de etiquetas,
  verbos variados donde hay etiqueta ("asked", "muttered"/"murmuró", "added"/"añadió",
  "repeated"/"repitió"), primera réplica anclada en escenas de dos o corales, resto
  sin atribuir. El cap. 50 en particular (Anael/Barachiel, Anael/Ezihel) es el más
  denso en diálogo de todo el tramo y ya tiene ≤1 de cada 3 réplicas atribuida, con
  solo 4 "said" reales en ~15 líneas de diálogo — no requería ninguna intervención.

## Verificación

- Estructura EN↔ES: los 6 diffs son paralelos línea por línea, mismo número de
  archivos, mismo punto de edición.
- "¿Sé quién habla?": en los 3 puntos editados, el hablante sigue siendo inequívoco
  (beat de acción o contexto previo inmediato).
- Contenido: cero cambios a hechos, POV, separadores de escena o palabras de diálogo
  fuera de las etiquetas. Las ediciones de continuidad protegidas (40, 43, 48 duelo,
  50) quedaron intactas en su contenido; solo el cap. 48 recibió un toque de
  atribución, explícitamente permitido por la consigna.

## Conclusión

El tramo 40-50 no tenía el problema de "cadena mecánica" en la escala esperada:
es un tramo dominado por narración/interioridad más que por diálogo dramatizado,
y los pocos intercambios que existen (Camael/Jeremiel en 45, Gabriel/ayudante en 46,
Gabriel/Uriel/heraldo en 49, Anael/Barachiel/Ezihel en 50) ya seguían, en su mayor
parte, el modelo Rothfuss antes de esta pasada. Se aplicaron 3 correcciones puntuales
(6 archivos) donde una etiqueta "said/dijo" era claramente redundante contra un beat
ya presente. No se forzaron cambios adicionales para "llenar cuota" — cazar cadenas,
no exterminar.
