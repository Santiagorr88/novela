# Verificación Laila / Raguel / Hadriel (Captains sin escena, Orifiel/Selaphiel) — 2026-08-20

**Alcance**: solo lectura sobre `main` (confirmado con `git branch --show-current`), sin cambio de rama. Continúa la disciplina fijada por `2026-08-20_naamah_verification.md` y la auditoría nocturna del 2026-08-19: no usar material de outline sin cotejarlo contra la prosa ya escrita, y si no hay outline, diseñar contra fichas + prosa real en vez de inventar en el vacío.

**Motivo**: tres Captains fichados en `content/lore/personajes.md` con cero apariciones en los 148 capítulos: **Laila** (Captain / Guardian of Bearers, bajo Orifiel, línea 537), **Raguel** (Captain / Peace Justice, bajo Selaphiel, línea 559), **Hadriel** (Captain / Veil Watcher, bajo Selaphiel, línea 579).

## Paso 1 — Verificación

`grep -rn -i "laila\|raguel\|hadriel" content/lore/arco_argumental_completo.md` → **cero resultados para los tres nombres**. El outline nunca les asignó entradas propias (a diferencia de Ezequiel, Selaphiel, Raziel, Naamah, que sí tenían material diseñado, correcto o no). No hay nada que verificar contra la prosa porque no hay nada propuesto — se pasa directamente al diseño original que pide el encargo para este caso.

`grep -rln -i "laila\|raguel\|hadriel"` sobre `project/Chronicles_of_the_Sundering_Judgment/chapters/EN/` → cero coincidencias. Confirmado: cero apariciones reales, tal como se afirmaba en el encargo.

Fuentes leídas completas para anclar el diseño en prosa real ya aprobada: `B2C03pt5_EN.md` (Orifiel/Ezequiel — precedente de voz/formato para Orifiel), `B2C36pt5_EN.md` (Selaphiel/Raziel/Jophiel — precedente para Selaphiel), `B2C10pt5_EN.md` y `B2C11_EN.md` (el episodio Malthus/Milo Ray y el despacho de Sariel a la Torre de los Eternos — para no pisar ese hilo de investigación), `B2C23_EN.md` (la demostración judicial de Zadkiel y los "dos signales" que persigue Zadkiel — para no duplicar su función ni su tipo de veredicto), `B2C25_EN.md`/`B2C28_EN.md` (la interrogación de Arin al explorador y el punto de cruce de Navarion — para no cruzar el hilo mortal de Mikel/Arin), `content/lore/book2_part1_expanded_beats.md` y `book2_part2_expanded_beats.md` (estado de producción y numeración de sufijos ya en uso).

## Decisiones de diseño

### Laila (Orifiel) — ancla: "the search" por Solmire, ya establecida en B2C03 y nunca resuelta en Libro II

`B2C03_EN.md` línea 9 fija que "the search" que convoca al consejo entero significa dos cosas a la vez: Solmire, la espada perdida, y Miguel, el alma reencarnada — y que ninguna de las dos se resuelve institucionalmente en todo el Libro II (`B2C36_EN.md` línea 43, cierre del libro: "Does this change anything about Solmire?", pregunta sin respuesta). La ficha de Laila —*Tenura*, guantes que "empower and shield chosen ones," "creates synergy between wielder and relic"— es exactamente el tipo de capacidad que Heaven emplearía para intentar reconocer la resonancia de un arma primordial en un candidato humano o angélico. Su escuadra ya fichada (Emeth, Karin "Synergy Link", Yaron, Davi "Keeper of Sacred Heirlooms", Saphil) confirma que su dominio es precisamente esta clase de trabajo: sinergia portador-reliquia y custodia de reliquias sagradas, no defensa de muralla (eso es Orifiel/Ezequiel) ni maestría marcial (eso es Ezequiel).

Se descarta cualquier conexión con la revelación de Milo Ray/Malthus (B2C10.5) para no tocar el hilo de investigación ya asignado a Sariel (B2C11) ni arriesgar el reveal-pacing de la identidad de Ereloth. Laila persigue en cambio pistas de la propia espada — resonancias, objetos, lugares — no de Milo Ray como persona. Se sitúa **inmediatamente después de B2C03.5** (mismo día, misma orden de reasignación de Orifiel hacia "the search" que libera la guarnición de Amaranth) como una consecuencia paralela y distinta de la misma orden: si Orifiel libera manpower defensivo, también reorganiza el trabajo activo de búsqueda de Laila, cuyo personal es escaso y muy especializado. Nueva entrada de escritor: un patrón narrador nuevo (14→ ahora **15**, ver Paso 3 de escritura) para esta clase de capítulo: vigilia institucional sin resolución, coherente con que Heaven nunca encuentra Solmire en este libro.

**Archivo**: `B2C03pt6_EN.md` (sufijo verificado libre; `B2C03pt5` ya existe, `B2C03pt6` no colisiona con ningún otro capítulo de la carpeta al momento de escribir esto).

### Raguel + Hadriel (Selaphiel) — escena compartida: incursión en el Velo + veredicto de conducta

Ambos sirven bajo el mismo comandante y sus dominios se conectan funcionalmente sin forzarlo: Hadriel (*Umbría*, "manipulates spatial rifts; guards interplanar access points") detecta y responde a una incursión real; Raguel (*Equitas*, "weighs guilt in battle," "strikes where guilt is heaviest") es la autoridad de facto para juzgar la conducta de un soldado propio en el calor de esa misma incursión. Se usa un escuadrón ya fichado bajo Hadriel (Kadan, "Portal Sentinel," "methodical, binary, sees only thresholds," *"You pass, or you don't. There is no maybe"*) como el punto de fricción: su personalidad ya establecida —binaria, sin término medio— es la fuente natural de un conflicto de conducta con un prisionero que se rinde, sin necesidad de inventar un personaje nuevo.

Se verificó explícitamente para no cruzar dos hilos ya escritos:
- **No es el punto de cruce de Navarion.** Ese cruce es un hilo mortal (Mikel/Arin, B2C24-28), geográficamente anclado a un campus universitario concreto y a un ward que Arin ya cataloga en detalle. La incursión de Hadriel ocurre en un punto del Velo distinto y sin nombre propio, en cualquier otro frente de la guerra — Heaven defiende muchos puntos débiles a la vez, no solo ese. Ningún personaje de la nueva escena menciona ni conoce Navarion.
- **No es el mismo tipo de veredicto que Zadkiel.** `B2C23_EN.md` establece a Zadkiel juzgando la estabilidad *metafísica* de entidades con "unstable forms" ligadas a la fuga de reencarnación — un fenómeno cósmico. Raguel aquí juzga la *conducta* de un soldado concreto frente a un prisionero concreto — ética de guerra, no metafísica. Ambos roles judiciales coexisten sin solaparse: Zadkiel es "Commander of Just Retribution" con jurisdicción sobre el fenómeno mayor; Raguel es un Captain cuyo dominio ficha explícitamente el peso de la culpa individual en combate.

**Punto de inserción**: después de `B2C23` ("The Unseen War in Heaven," la demostración de Zadkiel, clima de consejo fracturado) y antes de `B2C24` (capítulo mortal, Mikel). B2C24-27 no tocan la trama celestial en absoluto, así que no hay colisión temática ni de continuidad; situar la escena aquí también deja que el tono de tensión institucional de B2C23 (bordes exhaustos, consejo dividido) motive de forma natural por qué Hadriel opera con una guarnición reducida y por qué Raguel debe intervenir personalmente en vez de delegarlo.

**Archivo**: `B2C23pt5_EN.md` (sufijo verificado libre).

## Verificación de sufijos libres (para no chocar con procesos paralelos)

`ls project/Chronicles_of_the_Sundering_Judgment/chapters/EN/ | sort -V` (ejecutado justo antes de escribir, 2026-08-20): sufijos `.pt5`/`.pt6` ya en uso son B2C03pt5, B2C07pt5, B2C08pt5, B2C10pt5, B2C21pt5, B2C36pt5, B2C36pt6, además de B3C10pt5, B3C28pt5, B3C31pt5. **B2C03pt6 y B2C23pt5 no existen todavía** — libres para esta sesión. Se relista el directorio inmediatamente antes de cada `Write` para confirmar que ningún proceso paralelo los haya tomado entretanto.
