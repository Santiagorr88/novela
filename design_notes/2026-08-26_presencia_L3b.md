# Presencia cinematográfica — Libro III, tramo b (cap. 27-52)

Fase 2 de la pasada de presencia. Fuente: `content/craft/13_presencia_cinematografica.md`, `content/lore/presencia_biblia.md`. Voz vigente: `content/craft/12_calibre_b.md`. Tramo de los ESTADOS FINALES (biblia §4): menos primeras apariciones, más inflexión de cierre.

## Método

Lectura completa de los 26 capítulos (27-52) en EN y ES antes de tocar nada, para localizar por cita textual — no por grep — cada punto que pide el encargo y verificar los candidatos `[verificar en fase 2]` que dejó la biblia. Fichas de `content/lore/personajes.md` consultadas para Iofiel (1,96 m, bastón *Memnón*), Raziel (2,00 m, *Ignotus*, ojos que arden con sabiduría peligrosa) y Asmodeo/Asmodeus (1,60-2,10 m variable, siempre bello, siempre inquietante). Inserciones hechas primero en EN, en narración pura (nunca en diálogo), luego espejadas en ES en la misma posición y con la misma solución. Revisadas contra `content/lore/style_tics_denylist.md` para no reintroducir muletillas del corpus v1. Verificación final: recuento de párrafos idéntico EN/ES en los 5 capítulos tocados (`awk` con `RS=""`), y `git diff --quiet` confirmando que los 21 capítulos restantes del tramo quedaron byte-idénticos contra HEAD — incluidos los seis explícitamente marcados intocables (forja c38, ofrenda c39, POV de Miguel c40, diálogo Lucifer-Gabriel c42, despedida de Azael c48, patrón de armas c52).

## Verificación de candidatos de la biblia

- **Disolución de Belial**: la biblia marcaba rango candidato c38-44 `[verificar]`. Confirmado por lectura: es el **capítulo 45** completo (*The Echo of Pride*) — desde el trono vacío hasta la disolución real. El estado previo lo anuncia una sola línea suelta en cap. 32 ("Belial's crumbling court", boca de Naamah) y queda confirmado como hecho consumado en cap. 49 (Asmodeo: "the man's quiet, unremarkable dissolution"). No hizo falta anclar más el "antes" porque cap. 45 es autocontenido y ya trae el arco completo del craft (orgullo → vacío → disolución).
- **Fusión de posturas de Miguel**: la biblia proponía candidato c01-07 (fuera de mi tramo) para el instante exacto. Dentro de 27-52, Miguel ya opera como un solo registro en toda la travesía del Nexo (c33-40) y culmina explícitamente en c52 ("Mikel Ardon había hecho las preguntas. Miguel había vivido las respuestas... simplemente ambos a la vez") — intocable por patrón de armas. Se reforzó el patrón "un cuerpo, dos registros" en su primera aparición del tramo (c33), como pide el encargo, usando el modelo de imagen de c35 sin repetir su fórmula literal (esa línea es de la flota de Camael, no de Miguel).
- **Raziel c47**: no tiene aparición física en el tramo — solo se le nombra en el pensamiento de Iofiel. Se presentó por esa vía (recuerdo vívido, no invención de una escena que no existe), respetando la restricción de no tocar hechos.

## Inserciones realizadas

### 1. Miguel — cap. 33 (`33_The_Nexus_Path`)
Primera aparición de Miguel en el tramo. Se reforzó el patrón "un cuerpo, dos registros" (modelo: c35, "la flota respondió como un solo cuerpo") con un hecho concreto: lee el polvo del santuario a la vez como un general mide terreno sin defender y como un maestro simplemente nota lo que una sala lleva tiempo diciendo — una sola atención donde antes hacían falta dos hombres. Sin tocar diálogo.

### 2. Camael — cap. 41 (`41_The_Quiet_Battlefield`)
Puente hacia el patrón ya resuelto en c49 ("armadura sin motivo"). Se añadió el gesto que faltaba en el momento exacto en que la guerra termina: no se quita la armadura al dar la orden de volver a casa, y solo nota horas después, de pie en un terreno que ya no necesita defensa, que sigue sin habérsela quitado. Siembra el motivo antes de que c49 lo pague.

### 3. Belial — cap. 45 (`45_The_Echo_of_Pride`)
Inflexión de cierre confirmada (ver arriba). Se insertó una sola pincelada física de continuidad con el canon ya establecido (la mano quemada de L1/51): la flexiona por vieja costumbre, sin ya ninguna batalla que la justifique — la única parte de él que la edad y el desuso no lograron suavizar. No se inventa herida nueva ni se toca el hecho de la disolución.

### 4. Iofiel — cap. 47 (`47_The_Final_Verse`)
Primera aparición de Iofiel en el libro. Vector fijado según instrucción explícita del encargo: **memoria vigilante**, no quietud (ese sabor es de Azael). Hecho: su altura de ficha (bastón *Memnón* — arma que "invoca la memoria antigua" — apoyado al alcance de la mano sin mirar) + efecto: los guardianes más jóvenes bajan la voz cerca de ella igual que un soldado cerca de un oficial revisando un informe de campo, no por miedo sino porque intuyen que ella ya leyó alguna versión del final. El verso del Codex que lee en voz alta queda intocado palabra por palabra.

### 5. Raziel — cap. 47 (`47_The_Final_Verse`)
Presentado por la única vía que el capítulo permite sin inventar una escena: el recuerdo de Iofiel, en el mismo párrafo donde ya lo menciona el texto original. Vector de la biblia (*"saber que quema al tocarlo"*): luz de fuego moviéndose sobre una página que nadie más tiene permitido leer, símbolos en la túnica que parecen desplazarse si se los mira demasiado fijo.

### 6. Gabriel — cap. 49 (`49_The_New_Pantheon`)
Inflexión de cierre pedida explícitamente: el desgaste de sostener la paz. Su vector de ficha es "armonía que precede a la figura" (voz que resuena incluso en silencio); aquí se invierte con esfuerzo — mantener esa misma calma ya no le sale gratis, le cuesta un esfuerzo privado que nadie en la terraza le nota, y él mismo lo cataloga con distancia, como el cansancio de otro. Doblado con el testigo POV que ya pedía la biblia para la terraza posguerra (Gabriel observando a Camael y al consejo dividirse).

### 7. Asmodeo — cap. 49 (`49_The_New_Pantheon`)
Primera aparición de Asmodeo en el libro III (confirmado: no aparece antes en el tramo ni en capítulos previos de L3). Vector de ficha: **la forma que nunca se fija** (1,60-2,10 m variable, siempre bello, siempre inquietante). Presentado en su propia sección POV al no haber testigo externo disponible en esta escena: cambia de estatura y rasgos entre audiencias, nadie logra jurar después si trató con un hombre, una mujer o algo que se negó a elegir — y él mismo lee la ambigüedad como herramienta, no como vanidad.

### 8. Lucifer — cap. 49 (`49_The_New_Pantheon`)
Inflexión de cierre pedida explícitamente: de soberano indiscutido a monarca que archiva deserciones. Lucifer no aparece físicamente en el tramo 49-50 (confirmado por lectura), así que se insertó vía la reflexión de Asmodeo, que ya está pensando en la política de la corte infernal en ese mismo pasaje: un trono que antes no necesitaba anunciarse ahora exige horas de repasar listas de nombres, marcando deserciones una a una — más contabilidad que soberanía.

## Escenarios

- **Dis disputada / trono vacío**: ya bien cubierto por el texto existente de c45 (salón vacío, polvo, estandartes sin nadie que los salude) y c49 (la corte disputada de pretendientes menores). No se insertó escenario adicional para no sobrecargar — craft pide una imagen por escena y c45/c49 ya la gastan en la disolución de Belial y en la forma de Asmodeo respectivamente.
- **El Nexo (c33)**: la presentación conceptual ya vive en el diálogo de Azael (intocable) con narración de apoyo ya sólida (la proyección, las fracturas). Verificado suficiente; sin inserción adicional.
- **Sepulcro Doliente (c52), terraza posguerra (c49)**: verificados por lectura completa — ambos ya tienen tratamiento cinematográfico fuerte en el texto existente (el reposo final de Thaeriel; el paseo de Camael que observa Gabriel). c52 queda intocado por completo por el candado de "patrón de armas"; no se insertó nada ahí.

## Tres mejores citas (EN / ES)

**1. Camael — cap. 41**
> EN: *"He held the weight of it steady regardless, the same way he'd held every prior loss across this long war, and gave the order to bring his battered fleet home. He did not remove the armor before he gave it. He only noticed, hours later, standing on ground that no longer needed defending, that he still hadn't."*
> ES: *"Sostuvo el peso de ello con firmeza de todos modos, del mismo modo en que había sostenido cada pérdida anterior a lo largo de esta larga guerra, y dio la orden de traer a casa a su flota maltrecha. No se quitó la armadura antes de dar la orden. Solo notó, horas después, de pie sobre un terreno que ya no necesitaba defensa, que todavía no se la había quitado."*

**2. Iofiel — cap. 47**
> EN: *"Younger keepers passing her alcove had learned, without ever being told outright, to lower their voices the way soldiers lower them near an officer reviewing a field report — not from fear, but from the plain sense that whatever she was reading, she had already read some version of its ending once before."*
> ES: *"Los guardianes más jóvenes que pasaban junto a su rincón habían aprendido, sin que nadie se lo dijera nunca en voz alta, a bajar la voz del modo en que los soldados la bajan cerca de un oficial que revisa un informe de campo: no por miedo, sino por la sensación llana de que, fuera lo que fuese lo que estuviera leyendo, ella ya había leído alguna versión de su final una vez antes."*

**3. Lucifer (vía Asmodeo) — cap. 49**
> EN: *"A king who spent his evenings archiving his own desertions one name at a time was still a king. He no longer looked, to anyone paying close attention, like an undisputed one."*
> ES: *"Un rey que pasaba las tardes archivando sus propias deserciones un nombre a la vez seguía siendo un rey. Ya no parecía, para quien prestara verdadera atención, un rey indiscutido."*

## Archivos tocados

- `Libro3/EN/33_The_Nexus_Path.md` / `Libro3/ES/33_The_Nexus_Path.md`
- `Libro3/EN/41_The_Quiet_Battlefield.md` / `Libro3/ES/41_The_Quiet_Battlefield.md`
- `Libro3/EN/45_The_Echo_of_Pride.md` / `Libro3/ES/45_The_Echo_of_Pride.md`
- `Libro3/EN/47_The_Final_Verse.md` / `Libro3/ES/47_The_Final_Verse.md`
- `Libro3/EN/49_The_New_Pantheon.md` / `Libro3/ES/49_The_New_Pantheon.md`

Resto del tramo (27-32, 34-40, 42-44, 46, 48, 50-52) verificado sin cambios (`git diff --quiet` contra HEAD) — incluye los seis capítulos marcados intocables por el encargo.

## Nota para el autor

- El working tree tiene otros capítulos de Libro3 modificados (01, 03, 05, 07, 11, 12, 21, 22) que **no fueron tocados por este agente** — caen fuera de mi tramo (27-52) y corresponden al trabajo paralelo del agente de L3a (cap. 1-26). Se dejan intactos.
- No se tocó Leviathan (fuera del reparto, según restricción explícita) ni ningún escenario o personaje nuevo sin precedente en ficha.
