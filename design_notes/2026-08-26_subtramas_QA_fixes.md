# QA de las 8 mini-escenas de subtramas — correcciones (2026-08-26)

**Fecha**: 2026-08-26
**Tipo**: corrección de prosa, EN + ES espejo. Aplicado sobre las mini-escenas insertadas en Libro I según `design_notes/2026-08-26_diseno_subtramas_L1.md`, a partir de una auditoría QA independiente (10 hallazgos).
**Marco**: `content/craft/12_calibre_b.md` (filtros de calibre — presupuesto de imagen, lectura literal, lo intocable) + los límites de canon fijados en el diseño (H13, H23 del grafo de conocimiento, y el misterio del pergamino de Gabriel).

---

## 1. Cronología rota (cap. 4 — la apuesta Uriel/Camael)

**Antes** (EN): `"Miguel already said days, not months." Camael did not break stride. "That's not a wager. That's just agreeing with him loudly."`
**Antes** (ES): `—Miguel ya dijo días, no meses. —Camael no rompió el paso—. Eso no es una apuesta. Eso es solo estar de acuerdo con él en voz alta.`

Problema: Camael cita una frase que Miguel pronuncia recién más tarde, en la sala de guerra ("Zaphor'el falls in days, not months") — en el pasillo, ese diálogo todavía no ha ocurrido.

**Después** (EN): `"Everyone in the garrison already expects days, not months." Camael did not break stride. "That's not a wager. That's just agreeing with the mood out loud."`
**Después** (ES): `—Ya toda la guarnición espera días, no meses. —Camael no rompió el paso—. Eso no es una apuesta. Eso es solo estar de acuerdo con el ambiente en voz alta.`

Camael da la ofensiva por corta por cuenta propia (el rumor de la guarnición, ya establecido antes en el capítulo), sin citar una frase que Miguel aún no ha dicho. La línea de Miguel en la sala de guerra queda intacta, ahora como eco involuntario en vez de cita imposible.

---

## 2. Metáfora apilada (cap. 11 — Camael/Jeremiel)

**Antes** (EN): *"...the way he offered most things — sideways, timed to land exactly where it was needed rather than where it was expected... a letter kept dry through a storm nobody had ordered them to survive... and Camael let himself be read."*
**Antes** (ES): *"...del modo en que ofrecía la mayoría de las cosas —de lado, calculado para aterrizar exactamente donde hacía falta... una carta mantenida seca a través de una tormenta... y Camael se dejó leer."*

Tres imágenes en un mismo párrafo (trayectoria/aterrizaje, la carta, ser leído).

**Después**: se conserva **una sola imagen** — la carta mantenida seca a través de la tormenta, la más concreta y la que mejor ilustra el método de Jeremiel. El resto pasa a hecho seco: "not directly, but exactly when it mattered, not when it was expected" / "no de frente, sino exactamente cuando hacía falta, no cuando se esperaba"; y "Camael did not stop him" / "Camael no lo detuvo" en vez de "let himself be read" / "se dejó leer".

---

## 3. ES roto (cap. 12 — Remiel y el Espiral)

**Antes**: *"...esperaba que ella cargara con las tres sin que se le dijera cuál confiar."*
**Después**: *"...esperaba que ella cargara con las tres sin que nada le dijera en cuál confiar."*

Reformulación natural pedida por el propio informe QA, aplicada literalmente.

---

## 4. CANON H13 (cap. 27 — Zadkiel, vínculo causal prohibido)

**Antes** (EN): *"It was long enough for Zadkiel to confirm what he had already suspected... that the number she had given him weeks before and the fact now sitting in this room did not fit together in the shape he had expected them not to fit. He had hoped... that the two would disagree in some ordinary way..."*
**Antes** (ES): equivalente — el narrador declara explícitamente que la cifra de reencarnación y la noticia de Lamentum "no encajaban".

Problema: el narrador liga explícitamente la estadística de Zadkiel (cap. 17) con la noticia de que Belial tiene Lamentum — insinuación causal hacia H13 (Thamorak), prohibida hasta Libro III.

**Después** (EN): *"It was long enough for something in Zadkiel to go still, the particular quiet he wore when a thought closed a door on itself before it reached his face. He said nothing of it to Iofiel then, and gave no sign he intended to."*
**Después** (ES): *"Fue tiempo suficiente para que algo en Zadkiel se quedara quieto, la particular calma que llevaba puesta cuando un pensamiento se cerraba sobre sí mismo antes de llegarle al rostro. No le dijo nada de eso a Iofiel entonces, ni dio señal de que fuera a hacerlo."*

Zadkiel ahora solo reacciona y calla; su réplica siguiente ("El margen que me permito... se ha reducido más rápido este año que en los últimos cien") queda intacta y es la única pista — el lector conecta solo, sin narrador mediando la comparación.

---

## 5. CANON pergamino (cap. 27 — Gabriel, revelación de contenido)

**Antes** (EN): *"He knew what it authorized without needing to unfold it to remember. Command of Heaven's armies, his to claim the moment he judged Miguel unfit to hold it."*
**Antes** (ES): *"Sabía lo que autorizaba sin necesidad de desdoblarlo para recordarlo. El mando de los ejércitos del Cielo, suyo para reclamarlo en el momento en que juzgara a Miguel incapaz de sostenerlo."*

Problema: nombra explícitamente el contenido del sello ("mando de los ejércitos del Cielo") — rompe el misterio protegido por auditoría de coherencia previa.

**Después** (EN): *"He knew exactly what it authorized. He did not need to unfold it to be reminded, and he did not unfold it now."*
**Después** (ES): *"Sabía exactamente lo que autorizaba. No necesitó desdoblarlo para repasarlo, y no lo desdobló."*

Gabriel sabe; el lector no. Sin nombrar mando ni ejércitos, siguiendo la fórmula exacta sugerida por QA.

---

## 6. CANON H23 (cap. 29 — Iofiel, sospecha de deshonestidad)

**Antes** (EN): *"...whether a hundred honest gaps looked, from outside, indistinguishable from one dishonest one, and whether she would ever have cause to learn the difference."*
**Antes** (ES): *"...si un centenar de vacíos honestos se veían, desde fuera, indistinguibles de uno deshonesto, y si alguna vez tendría motivo para aprender la diferencia."*

Problema: contempla explícitamente la posibilidad de que la redacción fuera deshonesta — H23 exige que solo Kurel y Daith sepan que fue deliberada.

**Después** (EN): *"...how many drawers in this archive held that same single word standing in for something no one had ever gone back to recover, and whether anyone, in a hundred years or a thousand, would ever open one of them again."*
**Después** (ES): *"...cuántos cajones de este archivo guardaban esa misma palabra sola en lugar de algo que nadie había vuelto jamás a recuperar, y si alguien, dentro de cien años o de mil, volvería alguna vez a abrir uno de ellos."*

La duda de Iofiel queda en puro volumen y olvido institucional — cero noción de engaño.

---

## 7. Calco (cap. 29 ES — "estrofa redactada")

**Antes**: "mirando la estrofa redactada..." / "tocando la línea redactada..." / "Leyó una vez más la estrofa redactada..."
**Después**: "mirando la estrofa ilegible..." / "tocando la línea ilegible..." / "Leyó una vez más la estrofa ilegible..."

Se corrigieron las tres apariciones del calco (no solo la señalada, sino también "línea redactada" con el mismo problema), usando la palabra que el propio informe de Kurel y Daith emplea en la escena ("*ilegible*"), reforzando la consistencia interna del capítulo.

---

## 8. Calcos (cap. 33 ES — Nocthel)

**Antes**: *"...cada pasada añadiendo un adorno que su voz no habría podido justificar del todo sin ensayar la primera vez."* / *"Nocthel pretendía, para la tercera nota, que tuvieran su respuesta."*
**Después**: *"...cada pasada añadiendo un adorno que su voz nunca habría logrado justificar si no lo hubiera ensayado antes."* / *"Nocthel había querido que, para la tercera nota, ya tuvieran su respuesta."*

Reformulados con naturalidad, sin calco de "intended" ni de "un-rehearsed".

---

## 9. CANON H23 otra vez (cap. 40 — Iofiel, atribución de intención)

**Antes** (EN): *"...the private arithmetic of deciding how much of a half-understood thing belonged in a permanent record, and how much was safer left to stand as a gap no one would think twice about."*
**Antes** (ES): *"...y cuánto era más seguro dejar como un vacío en el que nadie volvería a pensar dos veces."*

Problema: "was safer left" atribuye la omisión a una decisión deliberada de seguridad.

**Después** (EN): *"...and how much simply had to remain a gap, unresolved, with nothing more honest yet to put in its place."*
**Después** (ES): *"...y cuánto simplemente tenía que quedar como un vacío, sin resolver, porque no había nada más honesto todavía que poner en su lugar."*

El eco queda como sensación de sostener verdades a medias, sin atribuir intención a nadie.

---

## 10. ES roto (cap. 46 — Rafael y el soldado)

**Antes**: *"Había sanado el duelo antes simplemente sobreviviendo más que la resistencia de un hombre a él, un trabajo paciente..."*
**Después**: *"Había sanado duelos antes simplemente aguantando más que la resistencia del hombre, un trabajo paciente..."*

Reformulación natural (*outlasting a man's resistance* = esperar a que la resistencia se agote), plural "duelos" en vez del singular calcado "el duelo".

---

## Verificación final

- **Paridad de párrafos EN=ES** en los 8 archivos tocados (04, 11, 12, 27, 29, 33, 40, 46): recuento de líneas de prosa/diálogo idéntico en cada par EN/ES tras los cambios.
- **Réplicas preexistentes intactas**: ninguna edición tocó diálogo fuera de las mini-escenas señaladas por QA; la única réplica modificada (cap. 4, Camael) es parte de la escena nueva de la apuesta, no una réplica preexistente del capítulo original. La línea preexistente de Miguel en la sala de guerra ("Zaphor'el falls in days, not months" / "Zaphor'el cae en días, no en meses") permanece intacta.
- **Relectura completa de las escenas de Zadkiel (cap. 17 + 27), Gabriel (cap. 27) e Iofiel (cap. 29 + 40)** tras las correcciones: no queda ninguna insinuación causal hacia H13 (Zadkiel constata solo su propia estadística y calla; el capítulo 17, no tocado, ya era limpio — pregunta puramente administrativa sobre cifras de reencarnación), ninguna revelación de contenido del pergamino de Gabriel (H-misterio del sello), y ninguna sospecha de deliberación en las dos escenas de Iofiel sobre H23 (cap. 29 y 40 ahora hablan solo de volumen de archivo y olvido institucional).

## Archivos tocados

- `Libro1/EN/04_The_First_Swing.md` + `Libro1/ES/04_The_First_Swing.md`
- `Libro1/EN/11_Crossings.md` + `Libro1/ES/11_Crossings.md`
- `Libro1/ES/12_A_Silence_in_Heaven.md` (solo ES — hallazgo 3 era exclusivo de ES)
- `Libro1/EN/27_A_Fissure_in_the_Light.md` + `Libro1/ES/27_A_Fissure_in_the_Light.md`
- `Libro1/EN/29_What_Remains_Unnamed.md` + `Libro1/ES/29_What_Remains_Unnamed.md`
- `Libro1/ES/33_The_Price_of_Absence.md` (solo ES — hallazgo 8 era exclusivo de ES)
- `Libro1/EN/40_Three_Were_Forged.md` + `Libro1/ES/40_Three_Were_Forged.md`
- `Libro1/ES/46_The_Sundered_Sky.md` (solo ES — hallazgo 10 era exclusivo de ES)
