# Auditoría de coherencia — Interludios de comandantes/capitanes de una sola escena
## Hilo 15 (Selaphiel/Raziel), Hilo 16 (Balam), Hilo 17 (Kushiel)

**Fecha**: 2026-08-22
**Alcance**: `Libro2/EN/12_The_Silence_That_Doesnt_Break.md`, `Libro2/EN/13_What_the_Ring_Corrects.md`, `Libro2/EN/32_What_the_Staff_Weighs.md`, `Libro2/EN/46_A_Verse_Withheld.md`, `Libro2/EN/49_No_One_Trained_to_Hear_It.md`, `Libro3/EN/11_Readiness_Not_Disobedience.md`, `Libro3/EN/49_The_New_Pantheon.md` (mención de Balam). Solo lectura, sin ediciones de prosa.
**Fuente de referencia**: `2026-08-22_coherence_audit_thread_map.md` (mapa de hilos, sección 2 Hilos 15-17, y registro de vida/muerte sección 3).
**Método adicional**: grep de nombres propios (Raziel, Selaphiel, Malphas, Kushiel, Thariel, Sachael, Kemuel) sobre los 159 capítulos de prosa, y cotejo puntual contra `content/lore/arco_argumental_completo.md` para ver qué planeaba el outline en los puntos donde la prosa deja algo abierto.

---

## Hallazgo 1 — El verso que Raziel se guarda nunca se resuelve, y él desaparece de la obra

**Archivos**: `Libro2/EN/46_A_Verse_Withheld.md`, `Libro2/EN/49_No_One_Trained_to_Hear_It.md`

**Pasaje**: en `L2/46`, Raziel se niega explícitamente a entregar un verso más profundo del Codex incluso a Gabriel — *"there is a verse deeper in that text than either of them has reached yet, Gabriel, and I am not giving it to this council tonight... You'll have it when I judge you ready to survive knowing it."* Gabriel acepta esperar: *"For now... Not forever."* En `L2/49`, Raziel manda a sus tres capitanes (Eshriel, Jahiel, Zaphiel) a investigar una segunda resonancia en un santuario en ruinas (el Ashgrave); el reporte que traen de vuelta contiene una segunda cláusula que Raziel lee a solas, reconoce *"close enough to the shape of a verse he had already decided, weeks ago and for reasons he had given no one, not even Gabriel, he was not yet ready to speak aloud"*, y el capítulo cierra con Raziel preguntándose si acaba de proteger a sus capitanes o de usarlos.

**Verificación hecha**: grep de "Raziel" y "Selaphiel" sobre los tres libros completos. Ambos personajes existen **exclusivamente** en estos tres capítulos (`L2/32`, `L2/46`, `L2/49`) — cero apariciones en Libro I y cero en Libro III, incluido `Libro3/EN/47_The_Final_Verse.md`, el capítulo donde el Codex efectivamente se completa (verso final dictado por Azael, recibido por Iofiel). Ese verso final trata la tríada de los Forgotten y a Michael como catalizador; no hace ninguna referencia a Raziel, a su verso retenido, ni al hallazgo del Ashgrave. `Eshriel`, `Jahiel` y `Zaphiel` (los tres capitanes de Raziel) tampoco reaparecen en ningún otro capítulo.

**Por qué es incoherencia real**: esto no es un hilo suelto atmosférico como los de Turein o Hollowseam (que el propio mapa de hilos documenta como cierres deliberadamente silenciosos). Es una promesa narrativa activa y con nombre propio: Raziel *le dice a Gabriel en su cara* que existe un secreto y que se lo dará "cuando lo juzgue listo" — una bomba de relojería narrativa explícita, no un rumor de fondo. El capítulo 49 además introduce una segunda pieza de evidencia (la cláusula del Ashgrave) que Raziel decide no compartir ni siquiera con los lectores del texto completo. Ninguna de las dos promesas se cobra. El Codex se cierra en `L3/47` por una vía completamente distinta (revelación directa de Azael a Iofiel) que no necesita ni menciona el material de Raziel, dejando la escena de `L2/46` como una amenaza cargada que nunca se dispara.

**Contexto del outline (no vinculante, pero confirma que no es descuido de lectura)**: `content/lore/arco_argumental_completo.md` (líneas ~1638-1643) planeaba efectivamente una continuación en Libro III: Raziel reconociendo la Lágrima de Fe de Gabriel como "un cuarto arma primordial" y exigiendo que se catalogara antes de salir del salón del consejo (`B3-raziel-01`), además de una objeción de Selaphiel al mismo episodio (`B3-selaphiel-01`). La escena de prosa real equivalente, `Libro3/EN/23_The_Tear_of_Faith.md`, se reescribió por completo — es Camael, no Gabriel, quien forja y entrega la Lágrima, y ni Raziel ni Selaphiel aparecen en ella. Esto no contradice la advertencia de fuente del mapa de hilos (el outline no es canon), pero sí confirma que el plan original de traer a Raziel de vuelta se abandonó sin que la prosa dejara ningún gesto de cierre en su lugar.

**Arreglo mínimo propuesto** (no aplicado): una línea en cualquier capítulo tardío del Libro III que ya involucre a Gabriel y el Codex — por ejemplo en `L3/47_The_Final_Verse.md`, cuando Iofiel reflexiona sobre correcciones que deberá enviar a "lesser archives" — podría anotar que el verso de Raziel nunca llegó a catalogarse, o que Raziel mismo no ha vuelto a presentarse ante el consejo desde la disolución de Belial. Bastaría una frase para convertir el silencio en elección narrativa reconocible en vez de en cabo suelto.

---

## Hallazgo 2 — El robo de tropas de Kushiel a Camael no tiene consecuencia ni reaparición

**Archivo**: `Libro3/EN/11_Readiness_Not_Disobedience.md`

**Pasaje**: Kushiel, sin autorización, reasigna "a quarter" de la reserva de Camael (lanceros de Sachael, vanguardia de Kemuel, la guarnición que el propio estado mayor de Camael llevaba en libros como reserva) hacia la frontera del Valle Invertido, invocando la doctrina de Gabriel de que el consejo ya "no es el protagonista" de la guerra. Sachael le advierte explícitamente sobre el "Rite of Questioned Command" — *"I sat beside Malakiel when the Rite broke him for less than this"* — y Kushiel responde que asumirá la responsabilidad si se lo preguntan. Camael descubre el faltante tres días después revisando su libro de batalla, manda un corredor a rastrear la orden, no obtiene respuesta, y cierra el capítulo marchando de todos modos: *"He marched anyway, and trusted the men he still had."*

**Verificación hecha**: grep de "Kushiel", "Thariel", "Sachael" y "Kemuel" sobre los 159 capítulos — los cuatro existen **exclusivamente** en este capítulo. Grep de "Rite of Questioned Command" en el resto del corpus: aparece dos veces más, pero en un episodio completamente distinto y anterior (`Libro2/EN/36_The_Councils_Fracture.md` y `Libro2/EN/45_Three_Anomalies.md`), donde Uriel invoca el mismo instrumento contra Gabriel — no hay ninguna conexión textual con el incidente de Kushiel. Revisé también los capítulos de batalla de Camael en la frontera (`L3/29`, `L3/34`, `L3/35`, `L3/41`) buscando cualquier mención de un déficit de tropas, una guarnición faltante o una reasignación no autorizada: no aparece nada — el "reserve" que sí se menciona en esos capítulos se refiere a un ala de la flota de Kushiel o a contención emocional, no al mismo hecho.

**Por qué es incoherencia real**: el capítulo no se presenta como un interludio cerrado sobre sí mismo — termina con Camael marchando con una fuerza reducida y sin respuesta de su corredor, un gancho explícito hacia una escena de rendición de cuentas que nunca llega. La amenaza de Sachael sobre el "Rite" que "rompió a un buen comandante" por mover tres escuadrones sin firma queda sin pagar tanto en un sentido (Kushiel nunca enfrenta esa institución) como en el otro (nunca se muestra si el faltante de tropas realmente le costó algo a Camael en la batalla que sigue).

**Contexto del outline**: `arco_argumental_completo.md` (líneas 1382-1387, 1686-1687, 1742) confirma que esto no era ambigüedad deliberada del autor sino una pieza sin terminar: el plan original incluía a Thariel (la propia capitana de Kushiel) reportando al nuevo consejo de iguales que Kushiel intentaba interceptar sin autorización a un enviado de Naamah, y a Camael, Raphael e Iofiel deteniéndolo juntos — "el primer juicio formal del consejo de iguales", explícitamente etiquetado como el pago de "B3-kushiel-01's need for a consequence/reckoning". Esa escena de "reckoning" nunca se escribió; ni Kushiel ni ninguno de sus tres capitanes vuelven a aparecer después de `L3/11`.

**Arreglo mínimo propuesto** (no aplicado): no hace falta escribir la escena completa del outline. Bastaría con una línea en cualquier capítulo posterior donde Camael reflexione sobre la campaña de la frontera (`L3/29` o `L3/41`, ambos ya centrados en Camael) reconociendo que el déficit nunca se explicó formalmente, o una mención de pasada en `L3/49_The_New_Pantheon.md` (que ya hace un repaso panorámico de Cielo en paz) señalando que Kushiel fue apartado o reasignado tras la tregua. Cualquiera de las dos cerraría el gancho sin requerir una escena de acción nueva.

---

## Hallazgo 3 — Malphas (`B3-malphas-01`): confirmado que NO deja cabo suelto perceptible en la prosa

**Archivo revisado**: `Libro2/EN/13_What_the_Ring_Corrects.md` (única aparición de Malphas en los 159 capítulos — verificado por grep, cero resultados en cualquier otro archivo, incluidos los capítulos de la caída de Malignus en Libro III: `L3/09_Judgment_Not_Wrath.md` y alrededores).

**Lo que dice el outline**: `arco_argumental_completo.md` (líneas 1362-1363) describe a Malphas como "Balam's own architect of dark structures, who designed part of Malignus's fortifications", presenciando el colapso de esa ciudad y dudando por primera vez de su axioma de que ninguna estructura suya es "a prueba de injusticia".

**Lo que dice la prosa**: en `L2/13`, Malphas es un ingeniero de trampas del frente fronterizo bajo Balam, sin ninguna mención de Malignus ni de fortificaciones para esa ciudad. Su arco en ese capítulo ya tiene su propia crisis de certeza autocontenida: un soldado celestial convierte su propia captura en la herramienta de la fuga de sus compañeros — una variable que ninguna de sus geometrías había contemplado — y Orobas corrige el resultado con su anillo *Reversus*. El capítulo cierra con Malphas archivando la duda deliberadamente: *"the uncertainty stayed exactly where he'd put it: on tonight's soldier, on tonight's shelf, nowhere near the rest of a career he had no present cause to doubt."*

**Conclusión**: el arco de Malphas tal como está escrito se sostiene solo. No hace ninguna promesa hacia Malignus, no menciona fortificaciones, y su duda profesional ya tiene una escena completa con planteamiento y cierre dentro del mismo capítulo. El gancho de `B3-malphas-01` es una idea de outline que nunca llegó a tocar la prosa en ningún punto — ni una palabra de conexión, ni un cabo suelto detectable para un lector que solo tenga el texto publicado delante. Esto corresponde a la opción (c) que el propio mapa de hilos plantea: archivar la entrada de outline como descartada, sin necesidad de tocar la prosa existente.

---

## Observación menor (no elevada a hallazgo) — la interrogación sin quiebre de Barbas

**Archivo**: `Libro2/EN/12_The_Silence_That_Doesnt_Break.md`

Barbas interroga a una centinela celestial capturada y, por primera vez en su carrera, no logra quebrarla — encuentra algo bajo el miedo que su aguja *Dolorim* no sabe medir, y nunca averigua qué protegía la prisionera ni por qué resistió. Esto sí alimenta el capítulo siguiente (`L2/13`: Balam le pide a Malphas cerrar el mismo tramo de terreno "before they cross it", en referencia directa a esta centinela), así que el hilo no queda completamente huérfano — se resuelve *dentro del propio díptico* Hilo 16, aunque el contenido específico de lo que ella guardaba nunca se revela. Considero esto consistente con el patrón ya documentado en el mapa de hilos (varios interludios de un solo capítulo cierran deliberadamente en ambigüedad — Turein, Hollowseam, Nyx, Vorlag) y no lo elevo a hallazgo porque no introduce un objeto, promesa o amenaza con nombre propio que el resto de la obra debiera recoger; es textura de personaje, no una bomba de relojería como la de Raziel. Se menciona aquí solo para que quede registrado que se revisó.

---

## Resumen

| # | Elemento | Estado | Severidad |
|---|---|---|---|
| 1 | Verso retenido de Raziel + cláusula del Ashgrave (`L2/46`, `L2/49`) | Sin resolver, personaje y capitanes nunca reaparecen | **Real — alta** (promesa explícita, con nombre, hecha directamente a Gabriel) |
| 2 | Robo de reserva de Kushiel a Camael (`L3/11`) | Sin resolver, personaje y capitanes nunca reaparecen | **Real — media-alta** (gancho de consecuencia institucional explícito, sin pagar) |
| 3 | `B3-malphas-01` (duda profesional de Malphas ante Malignus) | Nunca escrito en prosa | **No es hallazgo** — el arco existente de Malphas (`L2/13`) es autocontenido y no lo necesita |
| — | Centinela sin quebrar de Barbas (`L2/12`) | Ambigüedad deliberada, parcialmente resuelta dentro del mismo díptico | Menor / cosmético, consistente con el patrón de la obra |

Ningún otro elemento (objeto, promesa, amenaza) introducido en `L2/32`, `L2/46`, `L2/49`, `L2/12`, `L2/13` o `L3/11` queda sin recoger más allá de lo ya listado. La mención de Balam en `L3/49_The_New_Pantheon.md` es coherente con su arco previo (ahora reporta a Asmodeus, reuniendo inteligencia sobre los pretendientes al trono vacío de Belial) y no introduce contradicciones.
