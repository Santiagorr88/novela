# Presencia cinematográfica — Libro 1, capítulos 01–26 (EN + ES)

FASE 2 del encargo `content/craft/13_presencia_cinematografica.md`. Fuente única de vectores, rasgos y primeras apariciones: `content/lore/presencia_biblia.md`. Voz vigente: `content/craft/12_calibre_b.md`.

Verificación aplicada a cada capítulo tocado: paginación EN=ES (mismo número de párrafos, mismos separadores `---`), diálogo/hechos/beats/canon intocables, y `git diff --stat` confirma que **únicamente** los 7 capítulos listados abajo cambiaron (14 archivos, EN+ES) — el resto del tramo (05, 08–16, 18–26) queda byte-idéntico a HEAD.

---

## Lista de inserciones

| Cap. | Personaje / lugar | Inserción (1 línea) |
|---|---|---|
| 01 | Miguel | Presentación en el párrafo de apertura: 2,25 m, armadura dorada agrietada, ojos azul tenue; vector *autoridad que se contagia* mostrado vía el hábito de los reclutas de enderezarse antes de que él dé la orden — irónico aquí, porque está solo en el desierto. |
| 01 | Serephis (escenario) | Nuevo párrafo dramatizando el "antes" del reino enterrado: camino ancho para diez de frente, cimientos de un portal para ejércitos — la grandeza que el texto solo mencionaba en abstracto ("doctrina, no recuerdo"). |
| 01 | Gabriel | Presentación en el momento en que llega: 1,95 m, túnica azul/plata, pelo negro, ojos de lapislázuli; vector *armonía que precede a la figura* (la nota llega medio paso antes que él). |
| 02 | Lucifer | Presentación al entrar en su cámara: 2,20 m, pelo blanco-plateado, ojos rojo vino, alas negras; vector *belleza corrupta* + "vaciar una sala con solo entrar en ella" (pagado de inmediato por la reacción de los cortesanos, ya existente en el texto). |
| 03 | Bastión (escenario, estado intacto) | Añadido a la vista de Tamiel: la bóveda sin grietas y los estandartes a toda su largura ceremonial — contraste deliberado con la bóveda herida y los estandartes a media asta del L1/51 (leído para confirmar el daño exacto). |
| 03 | Rafael | Presentación al cruzar la cámara: 2,00 m, túnica blanca/verde, ojos esmeralda; vector *calma que diagnostica*, con el giro de que esta vez su quietud no calma a nadie. |
| 03 | Uriel | Presentación reubicada aquí (ver Desviaciones) al cerrar distancia con Miguel: 2,10 m, armadura incandescente, alas en llamas; vector *calor que se anuncia antes de verlo*. |
| 04 | Camael | Presentación en la apertura del capítulo: 2,10 m, torso desnudo con runas vivas, ojos como rayo atrapado; vector *fuerza legítima*, efecto en los compañeros de entrenamiento que se detienen a mitad de ejercicio. |
| 06 | Belial | Presentación en la primera escena de corte: 2,40 m, armadura negra viva, tatuajes; vector *miedo aprendido de la corte* — nadie se acerca a diez pasos de él, sin que él lo haya ordenado. |
| 06 | Foras | Presentación junto a Belial: piel agrietada oscura, más de un par de ojos dorados; vector *mirada múltiple que nunca parpadea* — sensación de estar observado por más gente de la que hay en la sala. |
| 06 | Torre de los Eternos (escenario) | Una frase añadida sobre su altura, filtrada por el propio Belial (comparada con "cualquier cosa que él hubiera mandado construir"), reforzando el testigo POV ya presente en el capítulo. |
| 07 | Sariel | Presentación integrada en el gesto ya existente (paño sobre la lanza sin mirar): 1,90 m, economía de movimiento, "recluta que olvida que entró en la sala". |
| 07 | Arin (forma humana de Thaeriel) | Presentación al aparecer en el muro: pelo negro corto, cicatriz en la garganta, ~40 años; vector *contenido a la fuerza* — no logra relajarse ni en zona segura. |
| 07 | Navarion (escenario) | Nombrado explícitamente en el párrafo descriptivo (antes decía solo "the university grounds") — testigo POV confirmado por lectura completa: Sariel, no Mikel (que no existe aún en L1). |
| 09 | Sepulcro Doliente (primera mención) | Leído completo — la prosa existente ya cumple el encargo (impresión POV de Belial, sin niebla poética); **no se insertó nada nuevo** para no violar el presupuesto de una imagen por escena. |
| 17 | Iofiel | Presentación en la apertura: casi 2 m, bastón *Memnón/Memnon*, vector *quietud de archivo* — calma de quien ya ha leído suficientes finales. |
| 17 | Zadkiel | Presentación al romper el estancamiento: 2,15 m, armadura de obsidiana clara, ojos plateados; vector *mirada que ya sentenció*, pagado con la reacción de Uriel, que evita esa mirada dos veces. |

**Total: 15 inserciones** (9 personajes, 1 escenario con dramatización nueva, 2 escenarios con refuerzo menor, 1 escenario confirmado sin necesidad de inserción, 2 testigos POV confirmados por lectura completa).

---

## Desviaciones del encargo original (con justificación)

1. **Uriel movido de c01 a c03.** La biblia listaba c01 como primera aparición por un grep que capturó solo una mención de pasada en un recuerdo de Miguel ("a joke about Uriel's temper") — Uriel no está físicamente en la escena. Su primera aparición real en cuerpo y diálogo es c03, en la misma escena que Rafael. Presentarlo ahí es coherente con la técnica de "presencia por efecto": no se puede mostrar el efecto de alguien que no está presente.
2. **Vepar no se presenta en c05 (no aparece).** Grep completo de Libro1/EN confirma que Vepar no aparece en ningún capítulo antes del 31 (`Libro1/EN/31_The_One_Already_Watching.md`). La celda de la biblia (L1 = 5) es incorrecta. No se inventó una aparición inexistente; recomiendo corregir la biblia y que el tramo que cubra los capítulos 27–51 presente a Vepar en su primera aparición real (c31).
3. **Sepulcro Doliente (c09) sin inserción nueva.** Es solo "primera mención" (Belial recordando el nombre), no una visita física con escenario completo. El texto ya cumple hecho + impresión POV sin niebla. Añadir más habría violado el presupuesto de una imagen por escena en un capítulo que ya gasta su imagen en la revelación de Lamentum/Solmire como pareja.
4. **Testigos POV confirmados por lectura completa** (pendientes en la biblia §3): Torre de los Eternos → Belial (ya era el único visitante en la escena); Navarion → Sariel, no Mikel/Arin como especulaba la biblia (Mikel no existe todavía en Libro I; Arin está en el campus pero no es el investigador).

---

## Tres citas EN/ES para muestra al autor

**1. Miguel, c01 — vector "autoridad que se contagia" en contraste con su soledad:**

> EN: *"None of that slowed him — not the heat, not the weight of gold armor scarred with cracks no armorer had ever fully closed over two and a quarter meters of frame, not eyes that burned faint blue under hair gone ash-white long before its time. Recruits fresh to the Host swore they could feel him crossing a yard before they turned to look, the whole line straightening before anyone gave the order. Here there was no line to straighten, only sand."*
>
> ES: *"Nada de eso lo frenaba —ni el calor, ni el peso de una armadura dorada marcada por grietas que ningún armero había logrado cerrar del todo sobre sus dos metros y cuarto de altura, ni unos ojos que ardían en un azul tenue bajo un pelo blanco-ceniza envejecido antes de tiempo—. Los reclutas nuevos de la Hueste juraban que lo sentían cruzar un patio antes de girarse a mirarlo, toda la fila enderezándose antes de que nadie diera la orden. Aquí no había fila que enderezar, solo arena."*

**2. Serephis, c01 — la grandeza dramatizada que el texto solo mencionaba:**

> EN: *"For a moment he let himself see it whole: the road wide enough for ten abreast, worn to a shine down its center by feet that had crossed it every day for centuries; somewhere along its buried length, footings too broad for any single door, the ghost of a gate built to pass an army through at once rather than turn one back. Whoever raised this had not built to survive a retreat. They had built to never need one."*
>
> ES: *"Por un instante se permitió verlo entero: el camino lo bastante ancho para diez de frente, pulido hasta brillar en el centro por pies que lo habían cruzado cada día durante siglos; en algún punto de su trazado enterrado, cimientos demasiado anchos para una sola puerta, el fantasma de un portal construido para hacer pasar un ejército entero de una vez, no para detener uno. Quien levantó esto no construyó pensando en la retirada. Construyó para no necesitarla jamás."*

**3. Zadkiel, c17 — vector "la mirada que ya sentenció", pagado en la misma escena:**

> EN: *"It was Zadkiel who finally broke the deadlock, and not in either direction the table had been pulling toward — two meters and change of pale obsidian armor, silver eyes that had a way of landing on a person like a verdict already reached before he'd said a word. [...] Uriel, mid-argument, had twice glanced toward him and twice looked away before finishing the thought, as though some part of him already knew how the sentence would be graded."*
>
> ES: *"Fue Zadkiel quien finalmente rompió el estancamiento, y no en ninguna de las dos direcciones hacia las que tiraba la mesa —dos metros y algo de armadura de obsidiana clara, ojos plateados con la costumbre de posarse sobre alguien como un veredicto ya alcanzado antes de decir una palabra—. [...] Uriel, a mitad de su argumento, había mirado dos veces hacia él y apartado la vista dos veces antes de terminar la frase, como si alguna parte de él ya supiera cómo iba a calificarse esa oración."*

---

## Verificación final

- `git diff --stat` confirma cambios únicamente en 01, 02, 03, 04, 06, 07 y 17 (EN+ES), 14 archivos, ninguno fuera del tramo asignado.
- Paridad de párrafos y separadores EN↔ES verificada línea a línea en cada diff (mismo número de inserciones en la misma posición relativa en ambos idiomas).
- Ninguna réplica de diálogo, hecho, beat o política de armas fue tocada — todas las inserciones son narración pura (descripción o interioridad sin diálogo).
- Ningún rasgo usado fuera de lo consignado en `presencia_biblia.md`; ninguna altura se dio como cifra sin traducir a efecto salvo como referencia interna breve ("2,25 m" etc.) integrada siempre junto al efecto concreto, siguiendo el propio modelo de la biblia y de capítulos ya aprobados en `12_calibre_b.md`.
- Ningún vector se repitió entre personajes (verificado contra los ya usados en este tramo: contagio moral/colectivo, tono/armonía, calor, diagnóstico-calma, fuerza legítima, miedo aprendido, vigilancia múltiple, economía de movimiento, nunca-se-relaja, quietud de archivo, mirada-veredicto, belleza-que-vacía-la-sala).

## Flags para el autor

- **Corregir `presencia_biblia.md`**: la celda "Vepar — L1 = 5" es errónea; su primera aparición real es L1/31 (fuera de este tramo).
- **Uriel**: recomiendo actualizar la biblia para que su primera aparición registrada en L1 sea c03, no c01, dado que c01 solo lo menciona de pasada sin presencia física en la escena.
