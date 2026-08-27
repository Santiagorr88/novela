# Doble corrección — poda de densidad y antirrepetición de voz (2026-08-27)

Segunda pasada sobre las inserciones recientes (presentaciones, subtramas, voces), a pedido del autor: «quiero evitar que sea repetitiva la prosa» + los embudos de densidad detectados por QA (Codex, informe en `/tmp/.../codex_densidad.txt`). Aplicado en ES+EN, réplicas intocadas, paridad de párrafos/separadores verificada con `git diff --stat` (todos los archivos muestran mismo número de inserciones y borrados: sustitución línea a línea, sin fusión ni división de párrafos).

## Tarea 1 — Poda de densidad (12/12 hallazgos aplicados)

Los 12 hallazgos de QA se verificaron en contexto contra `content/craft/12_calibre_b.md` (una imagen por escena, hecho+efecto). Ninguno se descartó — los 12 sostenían un embudo real. Un par se extendió ligeramente más allá de la cita literal de QA cuando la poda mínima propuesta dejaba una cláusula colgando sin antecedente (ver notas).

| # | Archivo | Poda aplicada | Nota |
|---|---|---|---|
| 1 | L1/03 (Rafael) | Quitado «Los heridos solían calmarse...sentirse visto» | Tal como QA lo pidió |
| 2 | L1/03 (Uriel) | Quitado «armadura incandescente...ojos del color de carbones encendidos, un cráneo labrado como adorno en el cinto» | Extendido para incluir también «, resto de alguna guerra sobre la que Miguel había dejado de preguntar» — esa cláusula modificaba al cráneo eliminado y quedaba huérfana si se cortaba solo hasta «cinto» |
| 3 | L1/04 (Remiel) | Quitado «tenía fama de decir poco y de tener razón...» | Tal como QA lo pidió |
| 4 | L1/06 (Belial) | Quitado «ojos dorados que no dejaban pasar nada que valiera la pena atrapar» | Tal como QA lo pidió |
| 5 | L1/06 (Foras) | Quitado «Sentirse observado por él siempre se parecía...» | Tal como QA lo pidió |
| 6 | L1/06 (archivero) | Fusionado en «Un archivero marchito lo interceptó cerca del séptimo rellano y preguntó qué asunto podía tener allí» | Tal como QA lo pidió |
| 7 | L1/17 (Zadkiel) | Quitado «ojos plateados con la costumbre de posarse...antes de decir una palabra» | Tal como QA lo pidió |
| 8 | L2/01 (Mikel) | Quitado «y tan poco memorable en sí misma que ningún alumno...» | Tal como QA lo pidió |
| 9 | L2/03 (Gabriel) | Quitado «el pelo oscuro peinado por nada más que costumbre» | Tal como QA lo pidió |
| 10 | L2/03 (Rafael) | Quitado «ojos esmeralda con un aire apenado incluso en reposo, tal como Gabriel lo había visto hacer tantas veces antes» | Tal como QA lo pidió |
| 11 | L3/11 (Sachael) | Fusionado en «La voz de Sachael se elevó en la última palabra; la punta crepitó, y él cerró el puño hasta apagarla» | Tal como QA lo pidió |
| 12 | L3/21 (Uriel) | Quitado «su propia armadura incandescente en cada costura, las alas arrastrando finas cintas de fuego, un cráneo ornamentado balanceándose apenas contra su cadera a cada paso» | Tal como QA lo pidió |

Los 12 se aplicaron en ES y se localizó y podó el espejo EN exacto de cada uno (mismas cláusulas, misma poda).

## Tarea 2 — Antirrepetición de menciones de voz

Barrido de las 46 inserciones de voz (`design_notes/2026-08-26_voz_en_prosa.md` + capítulos citados) contra las fichas «Voz (audiolibro)» de `content/lore/personajes.md` y `content/lore/prompt_universo.md`. Regla aplicada: cada patrón se queda en el personaje al que mejor le calza por ficha; el resto se reescribe con ángulo distinto (efecto en el oyente, comparación propia, ritmo) fiel a su propia ficha.

### Patrón «(la) voz baja y pareja/nivelada»
Ganador: **Rafael** (L1/03) — su ficha es literalmente «Baja, paciente, clínica»; sin cambios.

| Personaje | Cap. | Antes | Después (ES) | Ficha usada |
|---|---|---|---|---|
| Belial | L1/06 | «la voz en ese registro bajo y parejo que nunca necesitaba alzar para dar en el blanco» | «el desprecio asentado en su voz como una música de fondo que jamás necesitaba subir de volumen para dar en el blanco» | Gélida y arrogante; el desprecio como música de fondo |
| Anael | L1/50 | «la voz siempre baja y pareja, sin alzarse ni un poco» | «la ternura de su voz sosteniendo cada palabra sin que hiciera falta alzarla» | Suave pero firme; la ternura como forma de autoridad |
| Thaeriel | L3/09 | «la voz pareja y baja, sin que el fuego se agitara todavía debajo» | «cada palabra medida y contenida, el fuego todavía quieto debajo de ellas» | Tensa y contenida; fuego bajo la calma, palabras medidas que pesan |
| Mikel/Miguel | L3/01 | «grave y pareja, sin necesitar volumen real para abrirse paso entre el ruido» | «la voz grave cortando el bullicio sin necesitar alzarse del todo» | Grave y serena; autoridad que no necesita alzarse |

*(hallazgo adicional vía barrido, no listado originalmente: Belial reusaba la construcción casi palabra por palabra — su propia ficha, de todos modos, apunta a «desprecio como música de fondo», no a «pareja», así que la reescritura lo acerca más a su canon.)*

### Patrón «palabras cortadas al ras / recortadas»
Ganador: **Iofiel** (L2/03) — sin cambios.

| Personaje | Cap. | Antes | Después (ES) | Ficha usada |
|---|---|---|---|---|
| Balam | L2/12 | «las palabras secas y cortadas al ras, la misma economía...» | «sin gastar aliento en preámbulos, la misma economía...» | «...nunca gasta aliento en preámbulos» (cita casi literal de su ficha) |
| Sariel | L3/26 | «las palabras recortadas a exactamente lo que el momento exigía» | «cada palabra ya decidida de antemano, sin una sílaba de sobra» | «...cada una ya decidida de antemano» |
| Camael | L3/12 | «la pregunta recortada a su única palabra imprescindible» | «la palabra cayendo sola y seca como cualquier orden suya» | Frases cortas como golpes de martillo (mismo campo semántico que su otra inserción en L2/11, sin repetir «recortada») |

### Patrón «sin prisa»
Ganador: **Vual** (L1/25 y L2/51 — mismo personaje en ambos libros, coherencia intencional, sin cambios).

| Personaje | Cap. | Antes | Después (ES) | Ficha usada |
|---|---|---|---|---|
| Lucifer | L1/06 | «Pasó una página, sin prisa» / «cerrando el libro con cuidado sin prisa» | «paladeando el gesto como una palabra más» / «con el mismo cuidado que le daba a cada palabra» | Sedosa y sin prisa, cada palabra saboreada — coherente con «saboreando las palabras» ya establecido para él en L1/51 (zona sagrada, no tocada, solo confirma canon) |
| Stolas | L3/30 | «sin prisa y con un desdén perceptible» | «la pausa antes de las palabras claramente saboreada, el desdén perceptible» | Lenta y desdeñosa, saborea la pausa antes de soltar la observación que más duele |
| Sariel | L2/17 (bonus) | «la voz tan escueta y sin prisa como todo lo demás en él» | «la voz tan escueta como todo lo demás en él» | Económica y seca — se quita «sin prisa», que no está en su ficha y competía con Vual |
| Mikel | L2/01 (bonus) | «grave, sin prisa, apenas lo bastante alta...» | «grave, con un cansancio discreto en cada pausa, apenas lo bastante alta...» | Cansancio noble en las pausas (ángulo distinto del usado en L3/01 para el mismo personaje) |

## Verificación final

- `git diff --stat`: 32 archivos (ES+EN), cada uno con igual número de líneas añadidas y borradas — sustitución dentro de la misma línea/párrafo, sin alterar la estructura.
- `git diff` completo revisado línea a línea: todos los cambios caen en acotación/narración; ninguna réplica de diálogo (texto tras raya o entre comillas) fue tocada.
- Zonas sagradas (L1/51 + espejo B1C28, L3/25, 38-40, 42, 47, 48) no aparecen en el diff.
- Espejos EN aplicados uno a uno junto con cada cambio ES, misma poda/reescritura.
