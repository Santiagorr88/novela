# Correcciones QA — pasada de presencia cinematográfica (2026-08-26)

Revisión de los 10 hallazgos de la QA independiente sobre la pasada de presencia recién aplicada (`content/craft/13_presencia_cinematografica.md`, biblia en `content/lore/presencia_biblia.md`). Cada hallazgo se verificó en su contexto real antes de tocar nada — ninguno resultó falso positivo, los 10 se confirmaron y corrigieron en EN y ES en espejo. Fuente de fichas: `content/lore/personajes.md` y `content/lore/prompt_universo.md`.

**Verificación final aplicada**: paridad de párrafos EN=ES en los 32 archivos tocados (`grep -c` de líneas no vacías, recuento idéntico en las 16 parejas), ninguna edición tocó réplicas de diálogo (todas las cadenas editadas son narración, verificado por inspección — ninguna empieza con raya de diálogo), y grep final de cifras de altura ("meters", "metros", "un metro") en toda la trilogía EN/ES: **cero coincidencias reales** (los tres falsos positivos del grep — "a meter" dentro de "pudiera meter", "treinta metros" de distancia recorrida, "tantos kilómetros" — no son alturas de personaje y se dejaron intactos).

---

## 1. Alturas en cifras

**Verificado**: Miguel en Libro1/EN/01 ("two and a quarter meters of frame") y Camael en Libro1/EN/04 ("At two meters and change"), ambos con espejo ES ("dos metros y cuarto de altura", "dos metros y pico"). Confirmado como violación directa de la restricción del craft ("alturas traducidas a efecto, no a cifras").

**Corregido**:
- Miguel (L1/01): *"…armor scarred with cracks no armorer had ever fully closed over two and a quarter meters of frame, not eyes…"* → *"…armor scarred with cracks no armorer had ever fully closed, not eyes…"*. El efecto ya vivía en la misma frase (reclutas que se enderezan antes de la orden); solo sobraba la cifra.
- Camael (L1/04): *"At two meters and change, bare-chested…"* → *"At the height that made low doorways a running joke among his own men, bare-chested…"*. Autoridad física trasladada a efecto (dinteles bajos, broma entre sus hombres) sin número — ver también hallazgo 4.

**Extensión por grep** (`meters of|metros de|two meters|dos metros` en los archivos tocados, más `un metro` para el caso de Sariel): se encontraron y corrigieron **9 casos adicionales** no listados explícitamente en los 10 hallazgos, todos presentaciones de la misma pasada:

| Archivo | Personaje | Cifra retirada |
|---|---|---|
| Libro1/EN·ES/02 | Lucifer | "two meters and change of him" / "dos metros y algo de él" |
| Libro1/EN·ES/03 | Rafael | "two meters of him" / "dos metros de él" |
| Libro1/EN·ES/03 | Uriel | "two meters and change of incandescent armor" / "dos metros y algo de armadura" |
| Libro1/EN·ES/06 | Belial | "two and a half meters of him" / "dos metros y medio de él" |
| Libro1/EN·ES/06 | Foras | "over two meters of frame" / "sobre dos metros de armazón" |
| Libro1/EN·ES/07 | Sariel | "at just under two meters" / "apenas por debajo de los dos metros" |
| Libro1/EN·ES/17 | Iofiel | "just under two meters of her" / "casi dos metros de ella" (resuelto conservando el efecto: silla construida para alguien más pequeño) |
| Libro1/EN·ES/17 | Zadkiel | "two meters and change of pale obsidian armor" / "dos metros y algo de armadura" |
| Libro2/EN·ES/04 | Orifiel | "at just over two meters" / "con poco más de dos metros de altura" |
| Libro2/EN·ES/11 | Camael (refresco L2) | "at two meters and change" / "sobre sus dos metros y algo" |

En todos los casos se eliminó la cifra dejando intactos los rasgos físicos restantes de la ficha (pelo, ojos, armadura, alas), salvo Iofiel, donde se preservó el efecto físico ("silla construida para alguien más pequeño") sin el número. El caso de Sariel en Libro2/17 ("un metro noventa escaso") se trató aparte por estar ligado al hallazgo 9 (ver abajo).

---

## 2. Colisión de vector — Cassiel (Libro1/EN·ES/30)

**Verificado**: la frase *"the kind of presence that let even a soul this undone forget it was being watched"* usa inconspicuidad — vector reservado en exclusiva a Mikel humano (L2/01) según la regla de oro del craft ("un vector por personaje, sin repetir fórmula"). Confirmado contra la biblia (`presencia_biblia.md` §1.3): el vector asignado a Cassiel es *percepción rastreadora* ("la atención que ya encontró la herida antes de que el otro hable").

**Corregido**: *"…the kind of presence that let even a soul this undone forget it was being watched."* → *"…an attention that reached the wound before the soul had found any way to name it."* ES espejo: *"…una atención que llegaba a la herida antes de que el alma encontrara siquiera cómo nombrarla."* Mismo hecho previo (complexión sin nada que destacar, quietud como armadura) + el vector correcto de Cassiel.

---

## 3. Rango de Orifiel — Libro1/EN·ES/32

**Verificado**: *"his years under Orifiel — the captain whose shield had grown to his arm…"*. `personajes.md` línea 501 lo ficha como **Commander / Master of Shields**, y el resto de la trilogía (Libro2/EN/04, líneas 59 y 63: *"He found the commander alone…"*) lo trata correctamente como comandante — esta era la única instancia con el rango equivocado.

**Corregido**: "the captain whose shield…" → "the commander whose shield…" / ES: "el capitán cuyo escudo…" → "el comandante cuyo escudo…".

---

## 4. Metáfora apilada — Camael (Libro1/EN·ES/04)

**Verificado**: *"runes alive and moving across his skin like something breathing under bronze, eyes lit with the look of caught lightning that hadn't decided yet whether to strike"* — dos imágenes (runas vivas + rayo atrapado) antes del efecto en los sparrings, contra el presupuesto de una imagen por presentación del calibre B.

**Corregido**: se retuvo la imagen de las runas vivas (más distintiva de Camael frente a otros personajes con ojos-de-rayo/brasa en el reparto) y se retiró la del rayo en los ojos; el efecto en los sparrings queda intacto. Ver texto completo en hallazgo 1 (misma frase, mismo edit).

---

## 5. Metáfora apilada + traducción — Thaeriel (Libro3/EN·ES/03)

**Verificado**: *"pale fire banked beneath his skin, wrapped in chains that moved with him like vows…, wings scorched and jagged at their edges, a face divided cleanly down its length between a serenity… and a wrath…"* — cuatro imágenes encadenadas antes de seguir la escena. La ficha en `prompt_universo.md` marca explícitamente las cadenas-como-votos como *la* imagen aprobada de Thaeriel.

**Corregido**: *"He walked it, too, as what he now was rather than what he had been — a body of fire wrapped in chains that moved with him like vows rather than anything meant to hold a prisoner."* ES: *"Lo recorría, además, como lo que ahora era y no como lo que había sido —un cuerpo de fuego envuelto en cadenas que se movían con él como votos y no como nada pensado para retener a un prisionero—."* Una sola imagen (cadenas-votos) + hecho (cuerpo de fuego).

**"mellizas" → "melladas"**: el error de traducción de "jagged" (alas mellizas = gemelas, incorrecto; la ficha dice alas melladas/dentadas) vivía exactamente en la cláusula de alas que el recorte de arriba elimina por completo. Al secar la metáfora apilada, la frase con el error desaparece del texto — no queda "mellizas" en ningún punto de la trilogía (verificado por grep global, cero coincidencias).

---

## 6. Calco + personificación apilada — Lucifer (Libro3/EN·ES/05)

**Verificado**: ES *"Se sentaba en su centro del modo en que un aliento contenido se sienta en un pecho"* es un calco imposible en español natural (un aliento no "se sienta"); el EN correspondiente *"He sat at its center the way a held breath sits in a chest"* apila esa imagen más *"a face too flawlessly beautiful…"* y *"wings black as the space between stars"* — tres imágenes antes del vector aprobado (la sala que se reordena en torno a su quietud, ya presente en la misma frase siguiente).

**Corregido**: se retiró el símil del aliento contenido en ambos idiomas y se devolvió "wings black as the space between stars" a la formulación literal de ficha ("wings black as the void" / "alas negras como el vacío"), dejando la reordenación de la sala como única imagen. EN: *"He sat at its center — silver-white hair, wine-dark eyes, a face too flawlessly beautiful to belong to anyone trustworthy, wings black as the void folded still at his back."* ES espejo equivalente.

---

## 7. Tesis abstracta — Lucifer (Libro3/EN·ES/49)

**Verificado**: *"a throne that had once needed no announcing now required him to spend actual hours…"* y *"something that looked… considerably more like bookkeeping than sovereignty"* son afirmaciones tesis, no hecho+reacción — el propio calibre B las prohíbe explícitamente (filtro 1: "tesis abstractas… fuera").

**Corregido**: se sustituyó el andamiaje de tesis por un hecho concreto y repetido (Lucifer recorta él mismo su vela en vez de llamar a un paje, dos veces en la misma semana) observado por Asmodeo, con la reacción de Asmodeo como cierre en vez de la conclusión narrada directamente. EN: *"…he had caught him, more than once, bent over the same ledger of names twice in an evening no one else saw — trimming his own candle himself rather than calling a page to do it… Asmodeus, watching him do it a second time in the same week, no longer read the posture as one without rivals."* ES espejo equivalente.

---

## 8. Calcos rotos — Mikel (Libro2/ES/01)

**Verificado ambas líneas**:
- Línea ~3: *"lo miraban de lleno sin registrar jamás que habían mirado algo en absoluto"* invierte el sentido del EN correcto (*"looked straight through him without once registering they'd looked at anything at all"* = la mirada lo atraviesa sin detenerse, no lo mira "de lleno"). El EN no necesitaba corrección, solo la traducción.
- Línea ~31: *"la quietud aquí se había ganado a pulso algo que los propios edificios ya no recordaban"* — sintaxis rota (el modismo "ganarse algo a pulso" pedía un sujeto agente que la frase no daba).

**Corregido**:
- *"Noventa estudiantes por semestre lo miraban de lleno sin registrar jamás que habían mirado algo en absoluto…"* → *"Noventa estudiantes por semestre lo atravesaban con la mirada sin que esta se detuviera jamás en él, como si el aula estuviera vacía justo donde él estaba…"*.
- *"…la quietud aquí se había ganado a pulso algo que los propios edificios ya no recordaban—."* → *"…la quietud aquí había sido ganada a pulso por algo que los propios edificios ya no recordaban—."* (se añadió el agente "por algo" que la construcción pasiva necesitaba; se mantuvo el modismo, ya natural una vez corregida la sintaxis).

---

## 9. Calco + sintaxis rota — Sariel (Libro2/EN·ES/17)

**Verificado**: ES *"un metro noventa escaso que no gastaba nada en aparentar… aquí— la misma economía… absoluto—"* tenía dos problemas simultáneos: cifra de altura prohibida, y un inciso abierto con raya que se cerraba dos veces (una tras "aquí—" y otra, colgante, tras "absoluto—" sin nada después salvo el punto). El EN espejo también llevaba la cifra ("a spare 1.90 meters that spent nothing on display") — no estaba libre del problema, solo del de sintaxis.

**Corregido**: EN: *"not tall for one of his kind, a spare 1.90 meters that spent nothing on display, the spear Penumbra…"* → *"not tall for one of his kind, nothing about him spent on display, the spear Penumbra…"*. ES: *"…un metro noventa escaso que no gastaba nada en aparentar…"* → *"…sin nada en él que se gastara en aparentar…"*, y se eliminó la raya colgante final (el inciso ahora abre una vez y cierra una vez, igual que el EN, terminando en punto simple).

---

## 10. Rasgo invertido — Arin (Libro1/EN·ES/07)

**Verificado el espejo EN, tal como pedía el encargo**: tanto EN (*"he sat like someone who'd forgotten how to put a wall at his back"*) como ES (*"estaba sentado como alguien que había olvidado cómo ponerse una pared a la espalda"*) decían lo contrario de la ficha de Arin/Thaeriel — mercenario hipervigilante que nunca se relaja, ni en zona civil (carga lanza "even in civilian zones"). El problema no era solo de traducción: el EN original ya tenía el sentido invertido.

**Corregido en ambos idiomas**: EN: *"…he sat like someone who'd picked that spot on the wall for the sightline it gave him, not the view…"*. ES: *"…estaba sentado como alguien que había elegido ese lugar del muro por el ángulo de visión que le daba, no por las vistas…"*. Mantiene el rasgo correcto (elige el asiento que vigila, no se relaja) sin recurrir a "pared a la espalda" que habría chocado con que está sentado literalmente sobre un muro de piedra en un patio abierto, no contra una pared interior.

---

## Archivos tocados en esta pasada de correcciones (16 capítulos × EN+ES = 32 archivos)

Libro1: 01, 02, 03, 04, 06, 07, 17, 30, 32 (EN+ES)
Libro2: 01 (ES only — EN ya correcto), 04, 11, 17 (EN+ES)
Libro3: 03, 05, 49 (EN+ES)

Ningún otro archivo de la pasada de presencia fue tocado; el resto de capítulos modificados en el diff original (Libro1/36, 50, 51; Libro2/02, 03, 10, 18, 23, 32, 46, 51, 52; Libro3/01, 07, 11, 12, 21, 22, 33, 41, 45, 47) no forma parte de los 10 hallazgos ni del grep de cifras de altura, y se dejaron intactos.
