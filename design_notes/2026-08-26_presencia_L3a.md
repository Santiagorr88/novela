# Presencia cinematográfica — Libro III, tramo a (cap. 01-26)

Fase 2 de la pasada de presencia. Fuente: `content/craft/13_presencia_cinematografica.md`, `content/lore/presencia_biblia.md`. Voz vigente: `content/craft/12_calibre_b.md`.

## Método

Lectura completa de los capítulos con carga de reparto asignada (01, 03, 04, 05, 07, 10, 11, 12, 21, 22) en EN y ES, más grep dirigido de Thaeriel/Arin, Belial, Foras, Zadkiel, Rafael/Raphael, Gabriel, Uriel, Camael, Vepar, Azael, "Celestial City" y "Dis" en los 26 capítulos del tramo, para no dar por buena ninguna cita de la biblia sin verla en prosa. Inserciones hechas primero en EN, luego espejadas en ES en la misma posición y con la misma solución. Verificación final: recuento de líneas y de separadores `---` idéntico EN/ES en los 8 capítulos tocados; `git diff --quiet` confirmando que los 18 capítulos restantes del tramo (02, 04, 06, 08, 09, 10, 13-20, 23-26) quedaron byte-idénticos contra HEAD; revisión línea a línea de que ningún diff cae dentro de una réplica de diálogo (rayas `—`).

## Desviaciones de la biblia verificadas por lectura (antes de insertar)

La biblia es un informe de grep de primera coincidencia, no de lectura completa (lo dice su propio §8). Al leer el tramo completo aparecieron cuatro discrepancias entre el capítulo que la biblia asigna y el capítulo donde el personaje realmente tiene cuerpo en la página:

1. **Thaeriel/Arin**: la biblia lo marca en c01, pero en c01 solo es nombrado dentro del pensamiento de Mikel ("like Arin, like Thaeriel"), sin aparición física. Su primera aparición corporal real en L3 es **c03** (*A Path to Hell*), en forma celestial, cruzando hacia el Infierno. La presentación se hizo ahí.
2. **Gabriel y Uriel**: la biblia los marca en c11, pero en c11 solo aparecen citados en el reporte de Thariel ("Gabriel addressed his council") — no están físicamente en la escena. Su primera aparición corporal real es **c21** (*The Commander's Return*), en las puertas de la Ciudad Celestial. La presentación se hizo ahí.
3. **Foras**: no aparece en ningún capítulo del tramo 01-26 (confirmado por grep EN/ES). Su primera aparición real con voz propia es c32, fuera de este tramo. Sin acción en este informe.
4. **Zadkiel**: no aparece físicamente en ningún capítulo del tramo — solo se le nombra de pasada en el diálogo de Thariel en c11 ("Zadkiel's law"). Sin cuerpo en la página, no hay dónde anclar una presentación sin inventar una aparición. Sin acción en este informe.

También verificado: **Kushiel es celestial** en la prosa de c11 (reporta a un consejo del Cielo, cita el "Rite of Questioned Command"), confirmando el aviso ya registrado en la biblia de que el craft 13 tiene un lapsus de bando al listarlo entre los señores del Infierno.

## Inserciones realizadas

### 1. Milo/Ereloth — cap. 01
Ya tenía ojos dispares ámbar/plata y pies descalzos. Faltaba el efecto del vector *"carisma errático: calidez o inquietud, nunca neutralidad"*. Se insertó una frase entre las dos oraciones existentes sobre el público de la taberna: mitad de la sala se inclina hacia él sin notarlo, la otra mitad ríe tarde sin decidir si el calor que desprende es invitación o advertencia — nadie queda indiferente. Un solo párrafo, sin tocar diálogo.

### 2. Mikel Ardon — cap. 01
Cero presencia física en todo el capítulo pese a ser su primera aparición formal en L3. Se insertó el vector de inconspicuidad que exige el craft (guantes, pelo blanco prematuro, "cara que la sala deja pasar sin registrar") en la primera oración del capítulo, antes de que se lo describiera cruzando la taberna.

### 3. Thaeriel — cap. 03 (reubicado desde c01, ver arriba)
Su forma celestial no tenía ni una sola línea de cuerpo en el capítulo entero, pese a ya estar la escena construida sobre su efecto en el entorno (llamas que retroceden, demonios que huyen). Se insertó el vector *"fuego contenido a la fuerza"* — fuego pálido bajo la piel, cadenas como votos y no como ataduras, alas melladas, rostro partido entre serenidad e ira — en la primera oración donde camina como lo que ahora es.

### 4. Belial — cap. 03 (refresco)
Cero presencia física en su escena de la cámara privada. Se insertó armadura negra viva en los hombros, tatuajes que se avivan con el temperamento, ojos dorados con más cálculo que arrogancia de lo habitual — en el gesto de levantarse de la silla, sin tocar el beat del temblor de la lanza.

### 5. Lucifer — cap. 05
Capítulo entero desde su punto de vista, pero sin una sola línea de su cuerpo. Se insertó el vector *"belleza corrupta y voz"* del craft justo tras la primera mención de su nombre: pelo blanco-plateado, ojos rojo vino, alas negras, y el efecto pedido explícitamente por la biblia — la sala se reordena a su alrededor antes de que hable.

### 6. Miguel/Mikel — cap. 07 (punto de fusión, resuelto el `[verificar]` de la biblia)
La biblia marcaba como candidato el rango c01-07 para el instante exacto en que las dos posturas (General / profesor) se funden en un solo cuerpo. Por lectura completa, **c07 es el capítulo** — coincide con el título (*The Sword Remembers*), con el regreso completo de la memoria, y con el propio texto declarando la fusión en abstracto ("he was both of those men at once"). Faltaba solo el ancla física que pide el craft cinematográfico: se insertó una frase de postura ("stood straighter than the professor had ever stood and stiller than the Commander had ever managed to be, as though both postures had finally agreed... to share a single spine") justo antes del párrafo que ya declaraba la fusión emocional.

### 7. Kushiel — cap. 11 (refresco)
El campo de instrucción ya tenía el vector completo que pide la biblia (cráteres, terreno como historial disciplinario, testigo el propio comandante). Faltaba el cuerpo de Kushiel mismo: se añadió una frase mínima (armadura ceniza-y-brasa, braseros tras los ojos) en su primera mención por nombre.

### 8. Camael — cap. 11 y no repetido en cap. 12
Cero presencia física en su aparición del ledger nocturno (c11, cierre del capítulo). Se insertó: torso desnudo bajo una coraza a medio poner, runas vivas reducidas a brasa apagada "del modo en que siempre corrían cuando trabajaba en vez de combatir" — coherente con la nota de consistencia de `personajes.md` (ya no es el guerrero impulsivo, es contención profesional). No se repitió en c12 (su escena principal, inmediatamente después) para no violar la regla de "no repetición literal" dentro del mismo libro.

### 9. Vepar — cap. 12 (refresco)
Ya tenía muy bien resuelto el vector *"calma pragmática"* del craft (el trato del tridente *Aestus*, el "So am I" ante la espera). Solo faltaba un rasgo de ficha: el pelo que flota incluso en tierra. Se añadió a la frase ya existente sobre su piel translúcida, sin abrir párrafo nuevo.

### 10. Gabriel — cap. 21 (reubicado desde c11, ver arriba)
Primera aparición corporal real. Ya tenía "robes catching the gate's light"; se completó con pelo negro liso, ojos de zafiro, y la idea de que sus túnicas nunca necesitaron armadura para sostener una sala — siembra del vector *"armonía que precede a la figura"* que se paga más adelante en el propio capítulo, cuando su única frase ("He speaks the truth. I believe him.") basta para apagar armas encendidas.

### 11. Uriel — cap. 21 (reubicado desde c11, ver arriba)
Se insertó el vector *"calor que se anuncia antes de verlo"* pedido por la biblia: el aire se calienta varios grados antes de que la falange sea visible, en el mismo hueco donde el texto ya describía pasos acorazados acercándose. Se completó su cuerpo (armadura incandescente, alas con cintas de fuego, cráneo ornamentado al cinto) en la frase donde ya se describía su arma ardiendo.

### 12. Rafael — cap. 22 (refresco)
Única aparición física de Rafael en todo el tramo (grep de "Rafael"/"Raphael" en 01-26 solo da c22). Tenía diálogo con autoridad propia pero cero cuerpo. Se añadió túnica blanca y verde, brazaletes luminosos, en la misma frase donde ya se lo nombraba en la fila de arcángeles — sin abrir oración nueva ni tocar el diálogo que sigue tres párrafos después.

## Escenarios (verificados, sin inserción adicional)

- **Ciudad Celestial**: dentro del tramo 01-26 su estado es de guerra en curso, no de posguerra — puertas doradas, luz sin fuente, patio de piedra dorada (c21). Coherente con la biblia: la ruina y los estandartes a media asta llegan en L3/49, fuera de este tramo. No se insertó nada adicional; el estado ya presentado en c21 es correcto para el punto de la trama.
- **Campo de instrucción de Kushiel (c11)**: ya satisface el requisito de la biblia por completo (cráteres, terreno leído como historial de castigo, testigo el propio comandante). Solo se tocó el cuerpo de Kushiel (inserción 7), no el escenario.
- **Dis**: tensión creciente ya bien cubierta por el texto existente en c03, c05, c12, c18-20 (el temblor de la lanza, el miedo de Lucifer ante "la ausencia", el punto muerto de la flota en el Entremedio). No requirió inserción adicional dentro de este tramo.

## Tres mejores citas (EN / ES)

**1. Lucifer (cap. 05)**
> EN: *"He sat at its center the way a held breath sits in a chest: silver-white hair, wine-dark eyes, a face too flawlessly beautiful to belong to anyone trustworthy, wings black as the space between stars folded still at his back. No one in the hall needed telling to keep their eyes low; the room simply reorganized itself around him before he had said a word."*
> ES: *"Se sentaba en su centro del modo en que un aliento contenido se sienta en un pecho: pelo blanco-plateado, ojos rojo vino, un rostro demasiado perfectamente hermoso como para pertenecer a alguien digno de confianza, alas negras como el espacio entre las estrellas plegadas e inmóviles a su espalda. Nadie en la sala necesitaba que le dijeran que mantuviera la mirada baja; la sala sencillamente se reordenaba a su alrededor antes de que él dijera una sola palabra."*

**2. Miguel/Mikel — el punto de fusión (cap. 07)**
> EN: *"He stood straighter than the professor had ever stood and stiller than the Commander had ever managed to be, as though both postures had finally agreed, without argument, to share a single spine."*
> ES: *"Se irguió más recto de lo que el profesor jamás se había erguido, y más quieto de lo que el Comandante jamás había logrado estar, como si ambas posturas por fin hubieran acordado, sin discusión, compartir una sola columna."*

**3. Thaeriel (cap. 03)**
> EN: *"He walked it, too, as what he now was rather than what he had been — pale fire banked beneath his skin, wrapped in chains that moved with him like vows rather than anything meant to hold a prisoner, wings scorched and jagged at their edges, a face divided cleanly down its length between a serenity he no longer entirely trusted and a wrath he'd stopped bothering to hide."*
> ES: *"Lo recorría, además, como lo que ahora era y no como lo que había sido —fuego pálido latiendo bajo la piel, envuelto en cadenas que se movían con él como votos y no como nada pensado para retener a un prisionero, las alas chamuscadas y mellizas en los bordes, el rostro partido limpiamente por la mitad entre una serenidad en la que ya no confiaba del todo y una ira que había dejado de molestarse en ocultar—."*

## Archivos tocados

- `Libro3/EN/01_The_Divine_Jester.md` / `Libro3/ES/01_The_Divine_Jester.md`
- `Libro3/EN/03_A_Path_to_Hell.md` / `Libro3/ES/03_A_Path_to_Hell.md`
- `Libro3/EN/05_A_Council_of_Fear.md` / `Libro3/ES/05_A_Council_of_Fear.md`
- `Libro3/EN/07_The_Sword_Remembers.md` / `Libro3/ES/07_The_Sword_Remembers.md`
- `Libro3/EN/11_Readiness_Not_Disobedience.md` / `Libro3/ES/11_Readiness_Not_Disobedience.md`
- `Libro3/EN/12_The_In-Between_War.md` / `Libro3/ES/12_The_In-Between_War.md`
- `Libro3/EN/21_The_Commanders_Return.md` / `Libro3/ES/21_The_Commanders_Return.md`
- `Libro3/EN/22_A_Council_of_War_and_Faith.md` / `Libro3/ES/22_A_Council_of_War_and_Faith.md`

Resto del tramo (02, 04, 06, 08, 09, 10, 13-20, 23-26) verificado sin cambios (`git diff --quiet` contra HEAD). Nota especial sobre **c10**: ya tenía una presentación de Azael extremadamente completa y ya conforme al craft (quietud cósmica, viento que espera, mitad oro/mitad vacío estrellado, el nombre no aparece antes de este capítulo en ningún punto del tramo) — se dejó intacto a propósito para no diluir una escena que ya cumple el encargo por sí sola.

## Pendiente para el autor

- Confirmar si **Foras** y **Zadkiel** deben ganar una aparición física nueva en algún punto del tramo 01-26 (ninguno de los dos tiene cuerpo en la página actualmente) o si su presentación queda pospuesta al capítulo donde de verdad entran en escena (Foras: c32; Zadkiel: sin capítulo confirmado con grep en toda la trilogía dentro de L3).
- Los archivos `Libro3/{EN,ES}/33_The_Nexus_Path.md`, `41_The_Quiet_Battlefield.md`, `45_The_Echo_of_Pride.md`, `47_The_Final_Verse.md`, `49_The_New_Pantheon.md` aparecían ya modificados en el working tree al empezar esta sesión — **no fueron tocados por este agente**, caen fuera del tramo 01-26 y corresponden al trabajo paralelo del agente de L3b.
