# Auditoría de coherencia — mini-arcos de Libro I + interludios sueltos

**Fecha**: 2026-08-22
**Alcance**: Hilo 04 (Turein), Hilo 05 (Necrópolis), Hilo 06 (Hollowseam), Hilo 27 (interludios de Orifiel/Ezequiel/Laila, Raguel/Hadriel, Anael), según el reparto de `2026-08-22_coherence_audit_thread_map.md`.
**Método**: lectura completa, en orden, de los 15 capítulos asignados (`Libro1/EN/28-34`, `Libro1/EN/39-42`, `Libro1/EN/53`, `Libro2/EN/04-05`, `Libro2/EN/32`), más lectura de verificación de `Libro3/EN/47_The_Final_Verse.md` (fuera de la lista, autorizada por el encargo) y greps de nombre propio sobre los 159 capítulos para confirmar reapariciones o su ausencia.

Resultado: **2 hallazgos reales**, ambos promesas narrativas abiertas que nunca se cierran en página. El resto del material (Turein, Hollowseam, los interludios de un solo capítulo) es internamente coherente y coincide con lo que el mapa de referencia predice.

---

## Hallazgo 1 — La estrofa de la Necrópolis (Hilo 05) nunca se recoge

**Archivos**: `Libro1/EN/30_What_Remains_Unnamed.md` (promesa) vs. `Libro3/EN/47_The_Final_Verse.md` (candidato a pago, leído para verificar)

**Pasaje que abre la promesa** (`Libro1/EN/30`, líneas finales):
> "It would remain there, Daith supposed, until further evidence made a defensible reading possible — not lost, not destroyed, only unresolved. Someday, perhaps, someone might possess enough evidence and understanding to finish what the two of them had chosen, deliberately, to leave undone."

Esto es una promesa explícita y concreta: un fragmento específico del himno del Coro Silencioso —una palabra/nombre que se resiste a pronunciarse limpiamente, la primera mención corrupta de lo que luego se revela como Thamorak (confirmado por el propio mapa de referencia, sección Hilo 25)— queda deliberadamente sellado como "illegible" en el registro oficial, con la expectativa narrativa explícita de que alguien lo terminará.

**Por qué es incoherencia real**: `Libro3/EN/47_The_Final_Verse.md` es el único capítulo de los 159 que trata sobre "un verso final que se completa en el Codex", y es el candidato obvio para pagar esta promesa. Pero al leerlo completo, lo que ocurre ahí es un evento distinto: una página *en blanco* del Codex (nunca mencionada en `Libro1/30`, sin relación con el himno dañado de Kurel/Daith) se llena sola con un verso dictado por Azael sobre los tres Forgotten y Michael. No hay ninguna referencia a Kurel, a Daith, a la Necrópolis, al himno del Coro Silencioso, a la palabra que se resistía a pronunciarse, ni al hecho de que ese fragmento seguía archivado como "illegible". Iofiel —la misma Capitana que recibió el informe redactado en `Libro1/30`— es quien presencia el verso de `Libro3/47`, lo cual hace que la ausencia de cualquier callback sea más notoria, no menos: es el personaje con memoria institucional exacta para haber hecho la conexión, y el texto no la hace.

Confirmé además, con grep sobre los 159 capítulos, que **Kurel y Daith no vuelven a aparecer en ningún capítulo posterior** (ni en Libro II ni en Libro III), y que no hay ninguna otra escena que mencione una estrofa redactada, un renglón tachado del archivo, o cualquier variante de "illegible"/"redacted" ligada a la Necrópolis. La promesa queda genuinamente huérfana.

**Arreglo mínimo propuesto**: no requiere reescribir prosa nueva de gran escala. Bastaría con una frase adicional en `Libro3/EN/47_The_Final_Verse.md` —en el momento en que Iofiel identifica la caligrafía de Azael o inmediatamente después de leer el verso— donde ella recuerde brevemente el himno dañado y la estrofa sellada por Kurel y Daith, y reconozca (para sí misma, sin necesidad de una escena completa) que esta nueva escritura no es esa estrofa, o que finalmente confirma lo que aquella dejó sin resolver. Con dos o tres frases de reconocimiento explícito basta para cerrar el hilo sin inventar una subtrama nueva. Alternativa más barata aún: anotar en el propio mapa de hilos que la promesa se considera intencionalmente abierta/huérfana (como Nyx o Vorlag) y no un error — pero dado que el texto de `Libro1/30` la formula como promesa activa ("alguien la terminará algún día"), la opción de cerrarla con una frase es más fiel a la intención original.

---

## Hallazgo 2 — La búsqueda organizada de Solmire (Orifiel/Laila) nunca se cierra en página

**Archivos**: `Libro2/EN/04_The_First_Breach.md`, `Libro2/EN/05_What_the_Hands_Are_For.md` (apertura e inversión narrativa) vs. `Libro2/EN/45_Three_Anomalies.md` (confirmación de que sigue sin resolver) vs. resto de la obra (ausencia total de cierre)

**Pasaje relevante** (`Libro2/EN/05`, Orifiel a Laila):
> "Raphael needs trackers who can feel the sword's resonance if the field search stumbles across so much as an echo of it... Half your active roster. I would not ask if I thought there were slack anywhere else to find first."

Y el cierre parcial en `Libro2/EN/45` (Gabriel a Camael):
> "We keep watching for it the same way we decided to watch after the battlefield, patient rather than desperate."

**Por qué es incoherencia real**: `Libro2/04-05` no es un interludio decorativo — es una escena con coste narrativo real: Orifiel debilita deliberadamente la guarnición de Amaranth (lo que después *causa* la brecha del capítulo 4) y Laila cede la mitad de su plantel activo de entrenamiento, elige personalmente al equipo (Karin, Yaron, Renn), y el capítulo 5 dramatiza una pista falsa con peso emocional propio (el hallazgo de Yaron, la decepción). Es una inversión de recursos y personajes con nombre propio, no una mención de pasada. Confirmé por grep que **Laila, Karin, Yaron, Renn y Ezequiel no vuelven a aparecer en ningún capítulo posterior** de los 159 (Orifiel sí reaparece, pero nunca en relación con esta búsqueda). El propio mapa de referencia ya señala que el hilo queda "confirmado sin resolver" en `Libro2/45` — pero el problema no es que quede sin resolver en ese momento del libro, sino que **nunca se resuelve en absoluto**, ni siquiera quedando implícito.

Esto es narrativamente extraño porque Solmire *sí* se resuelve — Michael la reclama en `Libro3/EN/07_The_Sword_Remembers.md` y regresa a testificar ante el Consejo del Cielo en `Libro3/EN/22_A_Council_of_War_and_Faith.md` (verifiqué ambos capítulos: ninguno menciona la búsqueda de Amaranth, a Orifiel, Laila o su equipo). El Consejo que había invertido recursos reales en "la búsqueda" —el mismo Gabriel que le aseguró a Camael "seguimos vigilando"— nunca aparece en pantalla enterándose de que la espada ya fue recuperada y que la búsqueda puede darse por terminada. Es el mismo patrón que el hallazgo #4 ya catalogado en el mapa maestro para Corin Vasse: una promesa con inversión narrativa real que se anuncia como "hilo abierto" y luego simplemente se apaga sin que el texto lo reconozca.

**Arreglo mínimo propuesto**: no hace falta una escena nueva completa. En `Libro3/EN/22_A_Council_of_War_and_Faith.md` (o en cualquier escena de Libro III donde Gabriel/Orifiel estén presentes tras la recuperación de Solmire), bastaría una línea breve —de Gabriel dando de baja formalmente "la búsqueda", o de Orifiel reasignando por fin la mitad de guarnición que llevaba libros enteros perdida— para cerrar el hilo sin gastar más de un párrafo. Alternativa igual de válida: una frase en `Libro3/EN/48_The_Parting_of_Ways.md` o en el montaje final de `Libro3/EN/52_The_Silent_Guardians.md` que mencione, de pasada, que la guarnición de Amaranth volvió a su fuerza completa, o que Laila recuperó a su gente. Cualquiera de las dos opciones paga la inversión emocional de `Libro2/05` sin requerir que Orifiel, Laila o su equipo reaparezcan como personajes activos.

---

## Verificaciones sin hallazgo (para que quede constancia de lo comprobado)

- **Turein (Hilo 04, `L1/31-34`)**: coherente y bien pagado. La lectura de Cassiel se cita textualmente por Iofiel en `Libro1/EN/43_Three_Were_Forged.md` para conectar a Solmire con la profecía de las tres armas — es uno de los hilos mejor cerrados de todo el reparto. Cassiel reaparece consistentemente en `L1/43` y `L1/54` sin contradicción de rol o de mando (sigue bajo Orifiel).
- **Selm**: no vuelve a aparecer tras `L1/34`, lo cual coincide con lo previsto por el mapa ("Vivo. No reaparece"). No hay mención explícita en el capítulo de que sirva bajo Leraje, pero tampoco hay ningún dato en el propio texto que lo contradiga — es simplemente información que el mapa trae de otra fuente (fichas de personaje) y que la prosa no necesitaba repetir.
- **Hollowseam (Hilo 06, `L1/39-42`)**: coherente. Orwick (el soldado de Vem afectado por la anomalía) se recupera dentro del propio arco de cuatro capítulos gracias a Thoria/Alther — no queda ligado al Vacío/Thamorak (que en el mapa de referencia solo se nombra por primera vez en `Libro3/EN/17`), y no genera ninguna contradicción cronológica con el hilo del Vacío.
- **Interludios de Libro I/II (Anael `L1/53`, Raguel/Hadriel `L2/32`)**: ambos coinciden exactamente con su ficha en `content/lore/personajes.md` (Anael, Captain/Emotion & Inspiration; Ezihel, Squad Leader/Spirit Reanimator; Selaphiel consistentemente femenina en `L2/32` y `L2/46`) y con la única mención previa de Anael en `Libro1/EN/54_The_Echo_of_the_Sword.md` ("small sparks of feeling in hands too numb to ask for them" — cita casi literal del título del capítulo 53). Ninguno de los personajes de un solo capítulo (Ezihel, Kadan, Renn, Karin, Yaron) reaparece, lo cual es coherente con que el propio mapa los agrupa explícitamente como "interludios de un solo capítulo, autocontenidos".
- No se encontraron motivaciones ni eventos internamente contradictorios dentro de los propios capítulos leídos.
