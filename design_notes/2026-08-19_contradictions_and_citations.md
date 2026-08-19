# Contradicciones de destino de personaje y verificación ampliada de citas — 2026-08-19

**Alcance**: auditoría de solo lectura sobre `main` (confirmado con `git branch --show-current`, sin cambios de rama, sin comandos git de escritura). No se ha modificado ningún archivo del proyecto salvo la creación de este informe. Continúa el trabajo de `design_notes/2026-08-19_overnight_audit.md` (Hallazgo 1: la sección "Consecuencias y transformación" B3C108-125 nunca se escribió como prosa; Hallazgo 2: el destino de Belial en el outline contradice `B3C40_EN.md`). Ninguno de los dos hallazgos se repite aquí; esta auditoría busca **otros** personajes y **otras** entradas.

Fuentes leídas por completo antes de empezar: `design_notes/2026-08-19_overnight_audit.md` (Hallazgos 1 y 2), `content/lore/arco_argumental_completo.md` líneas 1540-1727 (secciones "El clímax de convergencia" y "Consecuencias y transformación", B3C083-125), y `B3C38_EN.md` a `B3C45_EN.md` completos. Para Parte 2 se leyeron además, completos, `B3C32_EN.md` y 15 capítulos de prosa de Libro II (`B2C16`-`B2C28`, incluyendo `B2C21pt5` y `B2C36pt6`), cotejados contra sus ~140 entradas de outline correspondientes (`B2C035`-`B2C138`, más las entradas `B2C144-152` relacionadas con `subplot_id`s pendientes).

---

## PARTE 1 — Contradicciones de destino de personaje (outline vs. prosa ya escrita)

### Hallazgo A — Ereloth/Milo Ray conserva su memoria completa; el outline exige que la pierda

**Personaje**: Ereloth / Milo Ray — **Severidad: BLOQUEANTE** (misma categoría que el caso Belial)

El outline (`arco_argumental_completo.md`, B3C102, línea 1632-1634) establece como sacrificio central de Ereloth en el clímax: *"He intends to give up his memory of being Ereloth, keeping only Milo, as his own contribution... choosing to forget, deliberately, for a reason."* Esto se paga explícitamente en B3C118 (línea 1698-1700): *"Milo Ray — no longer, inside himself, Ereloth — wakes on Earth with no memory of a mountain, a forge, or two brothers... Michael visits him sometimes... and tells him stories about a laughing god as if they were just stories."*

La prosa ya escrita contradice esto de forma absoluta. En `B3C43_EN.md` ("The Parting of Ways"), Ereloth se presenta en el fulcro con plena identidad y memoria intactas, dialoga usando su propio nombre y recuerdos ("*Nor the weight*, Ereloth added... *I used to think the song did all the carrying for me*"), y se despide conscientemente de Michael y Thaeriel. En `B3C45_EN.md`, Ereloth recupera su vieja guitarra, decide vagar cantando, y **reflexiona explícitamente sobre los destinos de Michael y Thaeriel por su propia cuenta** ("*I hadn't witnessed either man's choice directly... Michael, steady and searching... Thaeriel, patient with other people's wounds*"), algo imposible para un personaje amnésico. `grep -l "Milo Ray" B3C*.md` no devuelve ningún resultado en los capítulos 30-45: el nombre "Milo Ray" (post-amnesia) no aparece nunca en la prosa del clímax; solo "Ereloth", consistentemente con memoria plena.

**Evidencia**: `project/Chronicles_of_the_Sundering_Judgment/chapters/EN/B3C43_EN.md` líneas 9-47; `B3C45_EN.md` líneas 35-45.

---

### Hallazgo B — Thaeriel se instala en el Sepulcro del Llanto, no en el Valle Invertido; el outline exige lo segundo

**Personaje**: Thaeriel/Arin Cross — **Severidad: BLOQUEANTE**

El outline (B3C106, línea 1648-1650) resuelve el arco de Thaeriel así: *"Thaeriel volunteers to stay — not to guard against a returning enemy, but to be the wound's living keeper, binding himself to the valley..."* Y B3C119 (línea 1702-1704) lo confirma como destino final: *"Thaeriel is there [en el Valle Invertido], as he chose to be, tending a wound instead of hunting a criminal... Lament, for the first time in the whole trilogy, is described as quiet."*

La prosa ya escrita coloca a Thaeriel en un lugar completamente distinto. En `B3C41_EN.md`, tras la duda con Belial, Thaeriel se convierte en consejero de veteranos bajo el nombre "Arin Cross" en "una ciudad distante y anodina", sin mención alguna del Valle Invertido. En `B3C45_EN.md` ("The Silent Guardians"), Thaeriel cierra su consultorio y se instala permanentemente en el **Sepulcro del Llanto** (`the Weeping Sepulcher`) — un lugar preexistente en la mitología de la saga (donde originalmente estaba sellado Lament, según `B1C031`), no el Valle Invertido: *"Sorrow still needs a guardian... I will not impose justice. But I will keep its memory."* Lament queda apoyado contra una piedra del Sepulcro, no "silencioso en el Valle". `grep -l "Valley Inverted" B3C30-45.md` no da ningún resultado: la localización central del destino de Thaeriel según el outline no aparece ni una sola vez en los capítulos finales realmente escritos.

**Evidencia**: `B3C41_EN.md` líneas 27-37; `B3C45_EN.md` líneas 19-31.

---

### Hallazgo C — Foras nunca obtiene el mando de las legiones de Belial; el outline dice que Lucifer se lo concede formalmente

**Personaje**: Foras — **Severidad: MAYOR**

El outline (B3C113, línea 1678-1680) cierra así el arco de Foras: *"Foras... reads the real vacancy B3C112 leaves and makes his move: he petitions Lucifer formally for direct command of Belial's former legions... framing three books of patient positioning as simple administrative necessity."* Esto depende directamente de la premisa ya refutada (Hallazgo 2 de la auditoría previa) de que Belial sobrevive humillado bajo Lucifer.

La prosa ya escrita (`B3C44_EN.md`, sección POV Asmodeus) da un resultado incompatible incluso si se ignora la premisa de Belial: *"Hell without Belial had become... a court of lesser lords, each one marching on the fortress the old Lord of Pride had left standing empty... Asmodeus had watched three separate claimants make that march already, each... having accomplished nothing... Foras preached his usual sermons about the purity of dominance to soldiers whose eyes... had stopped following him the way eyes once followed a man they actually expected to lead them back to war."* Foras es explícitamente uno de los pretendientes **fracasados**; no hay petición formal a Lucifer, no hay concesión de mando, y la escena entera transcurre bajo la supervisión de **Asmodeus**, no de Lucifer, que ni siquiera aparece en el capítulo.

**Evidencia**: `B3C44_EN.md` líneas 21-23.

---

### Hallazgo D — Vepar nunca pide ni recibe autoridad autónoma de Lucifer; declina competir por su cuenta

**Personaje**: Vepar — **Severidad: MODERADA** (relacionado con Hallazgo C, pero verificable de forma independiente)

El outline (B3C114, línea 1682-1684) exige que Vepar *"joins the petition... he demands, in exchange for his support, autonomous control of the maritime and vital-fluid routes... Lucifer... grants both requests."* La prosa (`B3C44_EN.md` línea 23) da: *"Vepar, characteristically, had simply declined to compete at all, occupied instead with the fleet and the particular loyalty he'd apparently built with certain angelic commanders during the peace talks."* No hay petición a Lucifer, no hay concesión formal; es una decisión unilateral de Vepar, sin que Lucifer intervenga.

Este hallazgo se refuerza con `B2C21pt5_EN.md` ("The Tide Remembers"), un interludio ya escrito de Libro II que muestra a Foras y Vepar como **rivales calculadores**, no aliados: Vepar espera fríamente a que Foras se hunda solo tras la muerte de un capitán (Malthus) para heredar su territorio ("*A man who already knows he's drowning doesn't need to be pushed*"), exactamente lo opuesto a la "alianza táctica implícita" que el outline planta en Libro I (`B1C036`, `B1-vepar-01`) y que se supone culmina en el reparto pacífico del mando de Belial (`B3C114`). Ver también Parte 2, Hallazgo F.

**Evidencia**: `B3C44_EN.md` línea 23; `B2C21pt5_EN.md` líneas 33-41.

---

### Hallazgo E — El mecanismo entero de "la Lágrima" que activa el clímax es distinto e incompatible entre outline y prosa

**Personajes**: Michael, Gabriel, Camael — **Severidad: MAYOR** (afecta al mecanismo causal del clímax, no solo a un personaje aislado)

El outline dedica una sección completa (`La misión de Miguel`, B3C087-099) a construir la "Lágrima de Fe" como un objeto que se produce en una escena de consejo: Zadkiel se niega a legislar la fe (B3C093), Gabriel renuncia al cargo de Comandante Supremo y una lágrima suya se cristaliza en el acto (B3C097-098), dejando el "asiento vacío" que después estructura todo el "consejo de iguales" de Cielo. Esta Lágrima es uno de los tres ingredientes usados para reforjar Aetheris (B3C099, B3C103-104).

La prosa ya escrita (`B3C32_EN.md`, líneas 49-51) usa el mismo objeto argumental — "the Tear of Faith" — pero con un origen completamente distinto: *"He thought, watching the light catch against the fulcrum's own quiet stillness, of Camael's own words the night he'd handed this locket over — that he didn't offer anything lightly, that this tear had come from the faith which followed his despair rather than the despair itself."* La lágrima proviene de un **guardapelo de Camael**, entregado en una escena de Libro II ya establecida (`grep -l "locket" B3C*.md` → `B3C22`, `B3C29`, `B3C31pt5`, `B3C32`, `B3C33`), no de una renuncia de Gabriel en un consejo de Cielo.

Confirmación por ausencia total: se comprobó con `grep -l` sobre los 20 archivos de prosa `B3C*.md` (todo Libro III) que las cadenas **"Supreme Commander"**, **"Naamah"**, **"council of equals"** / **"council-of-equals"**, **"empty seat"** y **"Ezequiel"** no aparecen ni una sola vez en ningún capítulo escrito. El mecanismo institucional entero que el outline usa para producir la Lágrima —consejo, Zadkiel, renuncia de Gabriel, asiento vacío— no solo no se ha escrito (esto ya lo documentaba el Hallazgo 1 de la auditoría previa), sino que **el objeto que ese mecanismo debía producir ya existe en la prosa con un origen narrativo distinto e incompatible**. Esto no es una laguna; es una bifurcación ya resuelta de dos maneras contradictorias.

**Evidencia**: `B3C32_EN.md` líneas 49-51; grep negativo confirmado sobre los 20 archivos `B3C*.md`.

---

### Hallazgo F (menor) — El destino físico de Solmire: enterrada vs. en un paragüero

**Personaje**: Michael/Mikel Ardon — **Severidad: COSMÉTICA**

El outline (B3C124, línea 1722-1723) describe la imagen final de Michael así: *"a professor who used to be an archangel grades essays in an office with a sword in the umbrella stand."* La espada permanece visible, guardada como recuerdo doméstico.

La prosa (`B3C45_EN.md`, líneas 11-15) muestra a Mikel **enterrando** Solmire bajo una colina, como "un monumento silencioso": *"He knelt at the hill's base and dug... He laid Solmire into the shallow trench... He did not think of it... as burying a weapon. He thought of it instead as laying a monument."* Son dos imágenes finales físicamente incompatibles para el mismo objeto (visible en una oficina vs. enterrada bajo tierra en una colina distinta). Severidad baja porque es un detalle decorativo, no estructural, pero es una contradicción real y fácilmente verificable.

**Evidencia**: `B3C45_EN.md` líneas 11-15.

---

### Verificaciones limpias (control negativo, incluidas por completitud)

- **Uriel**: el outline (B3C110-111) pide que Uriel termine al mando de un campo de refugiados mixto, transformando su fuego de arma de guerra en calor de hogar. **Esto SÍ está instalado en la prosa**, casi palabra por palabra, en `B3C39_EN.md` ("The Tempered Flame") — Gabriel le asigna el campo, Uriel inicialmente se resiste, y el capítulo cierra con la misma imagen de "fuego que calienta en vez de quemar". Sin contradicción.
- **Azael**: el outline (B3C104) pide que se convierta en una presencia sin cuerpo, el "Guardián de la Luz Verdadera". La prosa (`B3C43_EN.md` línea 31, `B3C45_EN.md` línea 43) da una imagen compatible: una voz difusa que "se ha vuelto lo bastante grande para que 'desaparecido' ya no signifique lo mismo", fundida con el báculo/balance en el fulcro. Diferencia menor de localización (fulcro vs. "borde del valle") pero no una contradicción de fondo.

---

## PARTE 2 — Verificación ampliada de citas huérfanas

**Método**: se leyeron íntegras las 428 entradas del rango `B2C035`-`B2C138` del outline (líneas 677-1096 de `arco_argumental_completo.md`, ~104 entradas) y se cotejaron contra 15 capítulos de prosa completos (`B2C16` a `B2C28`, incluyendo los interludios `B2C21pt5` y `B2C36pt6`), que cubren ese mismo tramo comprimido en la numeración actual. Esto excede ampliamente la muestra de 40-50 entradas pedida (se verificaron efectivamente ~104 entradas de outline contra su prosa correspondiente). Se comprobaron además, específicamente, los `subplot_id` pendientes de verificación: `B2-agares-01`, `B1-foras-01`/`B1-vepar-01` (cruzado con Parte 1), `B3-jeremiel-01`, `B3-jophiel-01`.

### Resultado general: el tramo B2C035-138 (Libro II, Parte 2) está mayoritariamente bien instalado

A diferencia del cierre de Libro III, este tramo de Libro II resultó **fiel** en la inmensa mayoría de los casos muestreados: la búsqueda de Mikel (anvil, inscripción, folclore de Navarion, mapa de convergencia), la infiltración de Sariel en la Torre de los Eternos (estudio oculto, diario de Belial, sacrificio de Aamon, el informe a Gabriel, la extracción de Raphael), la huida y caza de Arin en Navarion, y la convergencia de los tres hacia la puerta sellada, están todas presentes en la prosa con una adaptación fiel (comprimida pero sin huecos de contenido ni contradicciones). No se reportan aquí, por tanto, decenas de "huecos" — el tramo está sano. Los hallazgos reales son dos, más una nota lateral:

---

### Hallazgo G — `B2-agares-01`: la mitad final del hilo (la guerra de información en el mundo mortal) nunca se dramatiza

**Severidad: MENOR**

El outline plantea el hilo de Agares en dos beats: B2C148-149 (Agares redacta una versión falsificada del Codex y la hace llegar al "inframundo mortal" **antes** de que Cielo autorice la versión real, de modo que "*by the time Gabriel's people are ready to consider releasing the real text, Agares's distortion is already the version most people who've heard anything have heard*") y B2C150 (Lucifer aprueba el texto sin cambiar una sílaba).

Solo la segunda mitad está escrita: `B2C36pt6_EN.md` ("A Familiar Shape in Borrowed Words") dramatiza fielmente la aprobación de Lucifer, casi con el mismo título que el outline. Pero `grep -l "counterfeit\|distortion\|three primordials" B2C*.md` no devuelve ningún capítulo que muestre el texto falsificado llegando al mundo mortal ni a Cielo enterándose de que ha perdido la carrera de la narrativa. El "coste" que el outline promete explícitamente para Cielo (heredar una guerra de información que no eligió) no aparece en ningún capítulo de Libro II ni III. Es un hueco real, aunque de severidad menor porque la mitad más dramática (la aprobación de Lucifer, con su ironía) sí está pagada.

**Evidencia**: `B2C36pt6_EN.md` (completo); ausencia confirmada por grep en todos los `B2C*.md`.

---

### Hallazgo H — Nota lateral: contenido en prosa sin entrada correspondiente en el outline ("huérfano inverso")

**Severidad: INFORMATIVA, no bloqueante**

`B2C21pt5_EN.md` construye un subargumento completo alrededor de la muerte de un capitán llamado "Malthus" en "un cruce de caminos", que desencadena la rivalidad fría entre Foras y Vepar citada en el Hallazgo D de la Parte 1. `grep -n "Malthus" content/lore/arco_argumental_completo.md` no devuelve ningún resultado: el nombre no existe en ningún lugar del outline de 428 entradas. Esto no es una cita huérfana en el sentido pedido (outline sin prosa), sino el caso inverso — prosa sin outline —, y confirma que la desviación entre ambos documentos va en las dos direcciones, no solo en la de "contenido prometido y no entregado". Se incluye como contexto útil para entender por qué el hilo Foras/Vepar del Hallazgo D no es un simple "olvido": la prosa ya escrita construyó su propia continuidad (rivalidad, no alianza) de forma independiente al outline más reciente.

**Evidencia**: `B2C21pt5_EN.md` completo; grep negativo sobre `arco_argumental_completo.md`.

---

### `subplot_id`s adicionales verificados sin hallazgos nuevos

- **`B3-jeremiel-01`** (B3C008) y **`B3-jophiel-01`** (B3C074): ambos son "plantas" de una sola frase en capítulos tempranos de Libro III ya escritos, cuyo pago explícito es el propio B3C097-098 (el mecanismo de consejo/renuncia de Gabriel) — es decir, dependen exactamente del mismo vacío ya documentado en el Hallazgo E de la Parte 1 y en el Hallazgo 1 de la auditoría previa. No constituyen huecos independientes nuevos.
- Los `subplot_id`s de Libro I (`B1-foras-01`, `B1-vepar-01`) quedan fuera del alcance de esta verificación porque su tramo de origen (`B1C032-038`) cae dentro del rango `B1C001-135` ya confirmado fiel a `Duplicado.md` en sesiones anteriores; su hallazgo relevante aquí es el de pago (Parte 1, Hallazgos C-D), no el de plantación.

---

## Resumen ejecutivo

**Parte 1 — Contradicciones de destino de personaje** (sin repetir el caso Belial ya documentado): **6 hallazgos**, de los cuales **2 son bloqueantes** (misma severidad que Belial) y comparten su causa raíz — la sección "Consecuencias y transformación" y la sección "La misión de Miguel" del outline actualizado nunca se convirtieron en prosa, y donde la prosa ya resolvió esos mismos destinos por su cuenta, lo hizo de forma incompatible con el outline:

- **Ereloth/Milo Ray** (bloqueante) — el outline exige amnesia; la prosa (`B3C43`, `B3C45`) le da memoria completa.
- **Thaeriel/Arin** (bloqueante) — el outline lo ata al Valle Invertido; la prosa (`B3C41`, `B3C45`) lo instala en el Sepulcro del Llanto, un lugar distinto.
- **Foras** (mayor) — el outline le hace heredar el mando de Belial vía Lucifer; la prosa (`B3C44`) lo muestra fracasando, bajo la corte de Asmodeus.
- **Vepar** (moderada) — el outline exige negociación formal con Lucifer; la prosa lo muestra actuando solo, sin petición ni concesión.
- **El mecanismo de la Lágrima/clímax de Miguel** (mayor) — orígenes narrativos incompatibles (Camael vs. consejo/Gabriel).
- **La espada de Michael** (cosmética) — enterrada vs. guardada visible.

El hallazgo más grave de la Parte 1 es un empate técnico entre **Ereloth** (amnesia vs. memoria intacta) y **Thaeriel** (Valle Invertido vs. Sepulcro del Llanto): ambos son, como Belial, contradicciones absolutas y no matices — la prosa ya aprobada dice una cosa, el outline dice la contraria, sobre el estado final de un protagonista de primer nivel.

**Parte 2 — Verificación ampliada de citas huérfanas**: se verificaron ~104 entradas del outline en el rango `B2C035`-`B2C138` (más del doble de lo pedido) contra 15 capítulos de prosa completos. El tramo resultó **mayoritariamente sano** — **2 huecos reales**, ambos de severidad menor: (G) la mitad final del hilo `B2-agares-01` (la guerra de información llegando al mundo mortal) nunca se dramatiza, aunque la mitad de Lucifer sí; (H) una nota informativa sobre contenido de prosa (el subargumento Malthus) sin entrada correspondiente en el outline, que ayuda a explicar por qué la rivalidad Foras/Vepar de la Parte 1 no es un simple descuido sino una continuidad ya construida de forma independiente. El hallazgo más grave de la Parte 2 es el (G), aunque de severidad claramente menor comparado con cualquiera de los hallazgos de la Parte 1.

**Conclusión combinada**: los seis hallazgos de la Parte 1 refuerzan la recomendación ya hecha en la auditoría previa — antes de escribir nada más sobre el cierre de la trilogía, el autor necesita decidir explícitamente si el outline actualizado (`arco_argumental_completo.md`, secciones B3C087-125) sigue siendo vinculante, porque en al menos cinco puntos concretos (Belial, Ereloth, Thaeriel, Foras, y el mecanismo de la Lágrima) ya no describe lo que la prosa aprobada realmente dice.
