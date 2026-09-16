# Pasada de diálogo modo Rothfuss — Libro1, capítulos 01-13 (EN+ES)

Fecha: 2026-08-25
Tramo: Libro1/EN/01-13 y Libro1/ES/01-13

## Calibración

Antes de editar, releí `content/craft/06_dialogos.md` (norma de la casa sobre
acotaciones) y el informe previo `design_notes/2026-08-22_audit_dialogos_L1a.md`
(auditoría de diálogos y voz para caps. 01-27, EN), que ya había diagnosticado este
mismo tramo con criterios afines. Ese informe señalaba el tramo 01-13 como
"deliberadamente escaso en diálogo" y solo marcaba problemas concretos de glosa/cadena
en el cap. 12 (H1, H5) — el resto de los capítulos de este tramo no aparecía en sus
hallazgos de gravedad 🟠/🟡. Confirmé esa lectura con mi propia relectura completa de
los 13 capítulos en EN antes de tocar nada.

## Hallazgo principal: el tramo 01-13 ya cumple el modelo Rothfuss casi en su totalidad

Conteo de líneas de diálogo real vs. etiquetas "said"/"dijo" (solo como marca de
atribución, no como verbo narrativo genérico) por capítulo, antes de esta pasada:

| Cap | Título | Diálogo real (líneas) | Etiquetas "said/dijo" | Nota |
|-----|--------|------------------------|------------------------|------|
| 01 | A Wound in the World | 6 (Gabriel/Miguel) + 1 (Miguel/figura) | 2 | Ya en modelo: ancla 1ª réplica, re-ancla tras la interrupción larga (Onyx Gates), resto en beat. |
| 02 | The Tree Outside Time | 2 (cortesanos) + 1 (Lucifer, monólogo) | 0 tags reales (1 "murmuró" con beat) | Diálogo mínimo, ya sin etiquetas mecánicas. |
| 03 | Verdict of Dawn | 4 (ayudante/Rafael) + 1 (Uriel, sin etiqueta) | 1 ("ventured"/"aventuró", verbo variado) | Ping-pong limpio. |
| 04 | The First Swing | 6 (Camael/soldado) + 7 (consejo de guerra) | 2 (ambas como ancla de apertura de escena) | Ejemplar: 2/13 réplicas etiquetadas. |
| 05 | Solmire's Judgment | 2 (Joran/Nael) + 4 (Rafael/Miguel) | 1 ("Raphael said" de apertura) | Ping-pong sin atribuir tras el ancla. |
| 06 | Whispers in the Burning Halls | 1 (superviviente) + 2 (Foras/Belial) + 4 (Belial/Lucifer, F1) | 3 | Escena F1 (biblioteca) marcada como fortaleza por el informe previo — intocable. |
| 07 | Hunter of Echoes | 3 (Camael/Sariel) | 0 tags reales | Ejemplar, puro beat. |
| 08 | The Weight of a Crown of Light | 3+4+3 (tres escenas de dos) | 4 (una por escena como ancla) | Cumple objetivo de frecuencia en las tres escenas. |
| 09 | The Price of Knowledge | 2 (ayudante/Belial) | 0 tags reales | Sin cadena que cazar. |
| 10 | A Crack in the Divine | 2 (Corven/Tamas) | 0 tags reales | Sin cadena que cazar. |
| 11 | Crossings | 2 (Jeremiel/Camael) + 2 (Aziel/Sariel) | 2 (anclas de apertura) | Cumple objetivo. |
| 12 | A Silence in Heaven | 5 (Gabriel/Uriel, observatorio) | **5 → 2 tras esta pasada** | **Único capítulo con cadena mecánica real — ver edición abajo.** |
| 13 | The Devil's Gambit | 4 (Belial/Aamon, negociación) | 3 (anclas + re-ancla tras interrupción) | Registro formal/manipulador; anclas justificadas. |

## Edición aplicada: Cap. 12 — A Silence in Heaven (observatorio, Gabriel/Uriel)

Este era el único punto del tramo con el patrón exacto que describe el encargo: una
escena de dos hablantes con alternancia ya establecida, donde **las 5 réplicas** de
la escena llevaban etiqueta ("Uriel said", "Uriel said finally", "Gabriel said",
"Uriel agreed", "Gabriel said") — 100% atribuido, muy por encima del objetivo de
≤1 de cada 3. El informe previo ya había señalado la primera de estas etiquetas
como candidata a redundancia (H1: "It was not a question, and Gabriel did not
answer it as one" es glosa que ya se lee en la línea — pero esa instancia está
protegida: es la única superviviente designada de la fórmula "not quite a
question" tras la pasada D1 de estilo, así que no se tocó).

Cambios (EN, luego espejados a ES con la misma solución):

1. **"He killed a neutral, Gabriel," Uriel said finally, [...]** → se movió la
   información del beat ("voz baja, despojada de su fuego habitual") a una oración
   previa a la cita, eliminando la etiqueta "Uriel said finally". Ninguna palabra de
   la réplica cambió.
   - EN: `His voice, when he finally spoke again, was low and stripped of its usual fire. "He killed a neutral, Gabriel. On a hunch..."`
   - ES: `Cuando por fin volvió a hablar, su voz sonaba baja, despojada de su fuego habitual. —Mató a un neutral, Gabriel. Por una corazonada...`

2. **"He is still our commander," Gabriel said. "Still our brother."** → se retiró
   "Gabriel said" por completo; el párrafo anterior ("Gabriel let the accusation
   settle... aware that whatever he said next...") ya ancla inequívocamente al
   hablante.
   - EN: `"He is still our commander. Still our brother."`
   - ES: `—Sigue siendo nuestro comandante. Sigue siendo nuestro hermano.`

3. **"He is," Uriel agreed.** → se retiró "Uriel agreed"; el beat inmediatamente
   anterior ("Uriel turned from the window at last, and Gabriel found... only the
   same exhausted uncertainty...") ya deja claro que habla Uriel.
   - EN: `"He is. But if the sword is leading him somewhere none of us can follow..."`
   - ES: `—Lo es. Pero si la espada lo está llevando a algún lugar...`

**Se conservaron 2 etiquetas** en la misma escena, deliberadamente:
- La primera réplica de Uriel ("You felt it too, then," Uriel said, without turning)
  — ancla de apertura de la escena, y "without turning"/"sin volverse" añade
  información física real (Uriel evita mirar a su hermano), no es un "said" desnudo.
- La última réplica de Gabriel ("If it comes to that," Gabriel said) — re-ancla
  legítima: la precede un párrafo entero de interrupción narrativa (el gesto hacia
  el pergamino sellado) y marca el punto de giro emocional de la escena (el voto).

Resultado: la escena pasa de 5/5 réplicas atribuidas (100%) a 2/5 (40%). No llegué
al ≤33% estricto porque las dos anclas restantes están explícitamente justificadas
por la regla 2 (primera réplica + re-ancla tras interrupción) y por la regla 5
(prueba de "¿sé quién habla?"): forzar su eliminación habría dejado la línea del
voto — el clímax de la escena — sin ancla tras una pausa narrativa larga, arriesgando
ambigüedad en un momento que no debe leerse dos veces para entenderse.

## Verificación

- **Palabras de diálogo**: cero cambios. Se verificó carácter por carácter que las
  cinco réplicas (EN y ES) conservan el texto exacto entre comillas/rayas.
- **Estructura EN↔ES**: cap. 12 mantiene 47 líneas y el mismo número de separadores
  `---` en ambos idiomas tras la edición (verificado con `wc -l` y `grep -c "^---$"`).
- **Convención de raya ES**: se respetó el patrón ya normalizado en el corpus (beat
  narrativo termina en punto → la raya abre el diálogo directamente, sin repetir la
  cita mid-frase con `—dijo X—` donde ya no hace falta).
- **Prueba de la voz tapada**: releída la escena completa tras la edición — en
  ningún punto queda duda de quién habla; los dos anclas restantes bastan para
  seguir el intercambio en una escena de solo dos hablantes.

## Capítulos sin cambios (y por qué)

Los 12 capítulos restantes (01-11, 13) no requirieron intervención:

- **02, 07, 09, 10**: diálogo mínimo (1-3 líneas por capítulo) sin ninguna cadena de
  etiquetas — no hay nada que cazar sin inventar problemas donde no los hay.
- **01, 03, 04, 05, 08, 11**: escenas de dos (o corales breves) que ya siguen el
  modelo — primera réplica anclada, resto en beat, verbos variados donde hace falta
  ("agreed"/"concedió", "ventured"/"aventuró"), objetivo de frecuencia (≤1/3) ya
  cumplido antes de esta pasada.
- **06**: la escena F1 (Belial/Lucifer en la biblioteca, cap. 6) es la fortaleza
  explícitamente señalada por el informe previo como el mejor intercambio del tramo
  — "said, without preamble" y "Lucifer agreed" son exactamente las etiquetas que
  *sí* pagan su sitio (la primera es la única instancia legítima de la fórmula
  "without preamble"/"sin preámbulo" que sobrevive en el tramo). No se tocó una
  palabra ni una acotación de esta escena.
- **13**: la negociación Belial/Aamon usa registro formal y manipulador por diseño
  (Belial construyendo una actuación calculada); las 3 etiquetas que aparecen son
  anclas de apertura para cada hablante o re-anclas tras un párrafo completo de
  interrupción narrativa — no una cadena mecánica.

Ninguna fórmula denylist ("That was X" / "Esa era X", "X's voice—" desnudo, "La voz
de X" desnuda) aparece en cadena en este tramo. Las 6 apariciones de "'s voice"/"la
voz de" encontradas (caps. 01, 04, 05, 08) llevan siempre información nueva (tono,
gesto) y están repartidas entre distintos personajes — no constituyen tic
transversal en este tramo.

## Conclusión

El tramo 01-13 llegó a esta pasada ya muy cerca del modelo Rothfuss objetivo: la
auditoría previa del 22-08 y la pasada de estilo D1 (23-08, que ya redujo "not quite
a question" a una sola instancia superviviente en todo el libro, precisamente la del
cap. 12) habían dejado el terreno preparado. Se aplicó **una única intervención
quirúrgica** — la escena Gabriel/Uriel del cap. 12 — que era el único punto real de
atribución mecánica en cadena de los 13 capítulos. Se prefirió no "llenar cuota"
retirando etiquetas ya justificadas en los otros 12 capítulos: cazar cadenas, no
exterminar acotaciones que ya cumplen su función.
