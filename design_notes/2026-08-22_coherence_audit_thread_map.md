# Mapa de hilos narrativos y registro de vida/muerte — preparación de la auditoría de coherencia

**Fecha**: 2026-08-22
**Propósito**: repartir la auditoría de coherencia narrativa (muertes/reapariciones, promesas sin resolver, motivaciones que no cuadran) entre agentes paralelos, uno por hilo.
**Alcance**: 159 capítulos-unidad (Libro I: 54, Libro II: 53, Libro III: 52).
**Método**: índices (`_manifest.json`, `_index.md`), `book1_part2_master_order.md`, los cuatro `expansion_progress_*.md`, los beat-plans (`book1/2/3_part*_expanded_beats.md`, `book1_lament_arc.md`, `book1_new_subplots_beats.md`), `prompt_universo.md`, `personajes.md`, más un conteo de menciones de personaje sobre los 159 archivos de prosa y lectura directa de los capítulos donde ocurren muertes/transformaciones.

**Advertencias de fuente aplicadas**:
- `arco_argumental_completo.md` está marcado como **SUPERADO desde la entrada B3C087 hasta el final** (nota explícita del autor, 2026-08-20, líneas ~1572-1589): la prosa aprobada `B3C30_EN.md`–`B3C45_EN.md` resuelve el clímax y el destino de Belial, Ereloth, Thaeriel, Foras y Vepar de forma incompatible con esas entradas. **Todo lo de este documento sale de la prosa, no del outline.**
- Además, `expansion_progress_libro3.md` documenta dos veces (casos B3C087-125 y B3C049-052/Naamah) que el outline **tampoco es fiable en tramos no marcados como superados** si se diseñó sin cotejar contra prosa existente. Los auditores deben tratar el outline como material de referencia histórica, nunca como canon.
- `personajes_muertes_reencarnaciones.md` **contradice la prosa** (ver Hallazgo previo #1 al final de este documento). No usarlo como fuente sin verificar.

---

# 1. TRAMA PRINCIPAL

## Protagonista central: Miguel → Mikel Ardon → Michael

Confirmado contra la sinopsis (`prompt_universo.md`, secciones "META NARRATIVE" y las tres sinopsis de libro) y contra la prosa. **Miguel es el protagonista central, pero NO es uno de los tres Forgotten** — esta distinción es canon duro y fue un fix mayor de Codex (`book3_part1_expanded_beats.md`, "Nota crítica #1"): los tres Forgotten son Ereloth, Thaeriel y Azael; Miguel/Michael es su aliado esencial de nivel Apex y el catalizador, nunca el cuarto forjador. `B3C42` (Libro3/47) lo fija explícitamente en el verso final del Codex.

**Arco a través de los 3 libros**:
- **Libro I** — General de la Hueste Celestial. Encuentra *Solmire* en el Árbol Fuera del Tiempo; sus victorias son decisivas pero sus veredictos son inhumanos (el suelo de Zaphor'el queda estéril). La espada lo va guiando más de lo que él la guía; se aísla de la compasión y de la comunión divina. Cae ante Belial en el duelo de `51_The_Fall`. Cierra en `54_The_Echo_of_the_Sword`: Cielo se retira, Solmire perdida en la Tierra, Miguel destinado a reencarnar sin memoria.
- **Libro II** — Reencarnado como **Mikel Ardon**, profesor de historia militar en la Universidad de Navarion (nueve años de carrera docente — cifra unificada en una auditoría previa). Arco de despertar: fugas de memoria, sueños, la búsqueda de "la risa"/el tercero, y la convergencia con Arin Cross. Cierra buscando activamente al creador de Solmire.
- **Libro III** — Reclama Solmire en `07_The_Sword_Remembers` (Libro3/07) y a partir de `15_The_Convergence` (B3C14) la nomenclatura pasa a **Michael**, cambio deliberado tras cerrar su integración de identidad. Regresa al Cielo, testifica ante el consejo, consigue la Lágrima de Fe de Camael, viaja al Nexo, acepta su propia falibilidad en la forja de Aetheris, y termina eligiendo una vida retirada en la Tierra con Solmire enterrada bajo su colina.

### Archivos en orden de lectura (ancla POV o peso central)

**Libro I** (`/home/sszark/Escritorio/proyectos/novelas/Libro1/EN/`)
- `01_A_Wound_in_the_World.md`
- `02_The_Tree_Outside_Time.md`
- `03_Verdict_of_Dawn.md`
- `04_The_First_Swing.md` *(POV Camael; Miguel central en escena)*
- `05_Solmires_Judgment.md` *(POV Joran/Raphael/Uriel; Miguel es el objeto del capítulo)*
- `08_The_Weight_of_a_Crown_of_Light.md`
- `10_A_Crack_in_the_Divine.md`
- `11_Crossings.md` *(peso secundario)*
- `12_A_Silence_in_Heaven.md` *(POV Gabriel; peso secundario)*
- `14_Dreams_of_Laughter.md`
- `27_A_Fissure_in_the_Light.md` *(POV coral, Consejo de Emergencia)*
- `38_The_Irreverent_Judgment.md`
- `44_A_Truth_Offered.md` *(POV coral: Iofiel, Miguel, Gabriel)*
- `47_The_Eve_of_Ruin.md` *(POV coral)*
- `49_The_Sundered_Sky.md` *(multi-POV)*
- `50_The_Resonance.md`
- `51_The_Fall.md` *(su caída; POV Belial)*
- `52_The_Sound_of_Retreat.md` *(POV Gabriel; Miguel ausente pero es el hueco del capítulo)*
- `54_The_Echo_of_the_Sword.md` *(cierre de libro)*

**Libro II** (`/home/sszark/Escritorio/proyectos/novelas/Libro2/EN/`)
- `01_The_Professor_of_Lost_Things.md`
- `08_An_Echo_in_the_Archives.md`
- `14_The_Herb_of_Stillness.md`
- `19_The_Isle_of_Whispers.md`
- `22_The_Riddle_of_the_Laughing_Smith.md`
- `24_The_Path_of_Laughter.md`
- `33_Legends_in_the_Stacks.md`
- `35_The_Jesters_Tune.md` *(POV Milo Ray; Mikel observado)*
- `37_The_Convergence_Point.md` *(dual POV Mikel/Arin)*
- `38_Nexus_Navarion.md` *(dual POV)*
- `39_The_Professor_and_the_Hunter.md` *(dual POV)*
- `40_Ambush_Below_the_Halls.md` *(dual POV)*
- `41_A_Song_of_Wrath_and_Reason.md` *(dual POV)*
- `42_The_Still_Point_of_the_Turning_World.md` *(dual POV)*
- `43_A_Memory_of_Three.md` *(dual POV)*
- `44_Two_Roads_from_a_Crossroads.md` *(dual POV)*
- `52_The_Weight_of_a_Name.md`
- `53_The_Voices_Gather.md` *(montaje final)*

**Libro III** (`/home/sszark/Escritorio/proyectos/novelas/Libro3/EN/`)
- `01_The_Divine_Jester.md`
- `04_The_First_Lesson_Laughter.md`
- `06_The_Storm_of_Sorrows.md`
- `07_The_Sword_Remembers.md`
- `14_Reading_the_Scars.md` *(POV Azael; el choque Michael-Lucifer se revela como co-causa)*
- `15_The_Convergence.md` *(primer capítulo con "Michael")*
- `16_The_Three_Forgotten.md`
- `17_The_Sages_Plan.md`
- `21_The_Commanders_Return.md`
- `22_A_Council_of_War_and_Faith.md`
- `23_The_Tear_of_Faith.md`
- `33_The_Nexus_Path.md`
- `36_The_Fallens_Debt.md`
- `37_The_Nexus_of_All_Things.md`
- `38_The_Forge_of_Balance.md` *(POV Azael; Michael acepta su falibilidad)*
- `39_The_Final_Confrontation.md` *(POV Azael; ofrenda de esperanza de Michael)*
- `40_The_Sundering_Judgment.md` *(POV Azael; Michael recibe su fragmento del Vacío)*
- `48_The_Parting_of_Ways.md`
- `52_The_Silent_Guardians.md` *(capítulo final de la trilogía)*

---

# 2. SUBTRAMAS / HILOS SECUNDARIOS

> Rutas abreviadas: `L1/` = `/home/sszark/Escritorio/proyectos/novelas/Libro1/EN/`, `L2/` = `.../Libro2/EN/`, `L3/` = `.../Libro3/EN/`.

---

## Hilo 01 — El arco de Lament (Libro I, L1-L6)
**Ancla**: Belial (POV en 5 de 6). Secundarios: Iofiel, Nyx, Foras.
**Arco**: Belial, tras asesinar a Aamon para abrir el portal, desciende al Sepulcro del Dolor cruzando umbrales que cobran precio psicológico, reclama la lanza *Lament* y descubre que ganarla le cuesta cargar permanentemente con el dolor que la lanza contiene. Cielo detecta el evento sin entenderlo.
- `L1/16_The_First_Threshold.md` *(POV Belial)*
- `L1/17_What_the_Council_Wont_Decide.md` *(POV Iofiel — respuesta angélica)*
- `L1/18_Those_Waiting_for_a_Stumble.md` *(POV Belial/Nyx)*
- `L1/19_The_Descent.md` *(POV Belial + testigos mortales/angélicos)*
- `L1/20_The_True_Tomb.md` *(POV Belial — reclama Lament)*
- `L1/21_What_Winning_Costs.md` *(POV Belial + convergencia angélica)*

## Hilo 02 — El arco completo de Belial (Libros I-III)
**Ancla**: Belial. Secundarios: Aamon, Lucifer, Foras, Vepar, Thaeriel.
**Arco**: de Lord del Orgullo ambicioso → traidor que asesina a un Comandante par para abrir un portal → portador ilegítimo de Lament (que nunca le pertenece de verdad) → derrota de Miguel → progresiva erosión en el Libro II (pierde a su Enforcer ante algo que no puede nombrar, abandona la cosecha de almas, se fortifica) → desarme y humillación por Thaeriel en el Libro III → colapso metafísico ordinario en la irrelevancia, alma liberada al ciclo ya reescrito.
- `L1/06_Whispers_in_the_Burning_Halls.md`
- `L1/09_The_Price_of_Knowledge.md`
- `L1/13_The_Devils_Gambit.md` *(planifica la traición a Aamon)*
- `L1/15_The_Price_of_Truth.md` *(mata a Aamon; abre el portal)*
- `L1/16_The_First_Threshold.md` … `L1/21_What_Winning_Costs.md` *(arco de Lament, Hilo 01)*
- `L1/45_The_Master_of_Lament.md`
- `L1/48_The_Despairing_Front.md` *(POV Camael; Belial como amenaza)*
- `L1/50_The_Resonance.md`
- `L1/51_The_Fall.md`
- `L1/54_The_Echo_of_the_Sword.md` *(referido)*
- `L2/09_The_Soul_Reapers.md`
- `L2/10_What_Even_He_Does_Not_Know.md` *(POV Lucifer; ni Lucifer sabe el origen de Lament)*
- `L2/17_A_Mission_into_Memory.md` *(Cielo investigándolo)*
- `L2/23_A_Thiefs_Legacy.md` *(POV Sariel; reconstrucción del robo)*
- `L2/34_An_Unseen_Interrogation.md`
- `L2/50_The_Unaccounted_Variable.md` *(pierde al Enforcer; decreto de abandono de la cosecha)*
- `L3/03_A_Path_to_Hell.md`
- `L3/05_A_Council_of_Fear.md`
- `L3/13_The_Heart_of_Hell.md`
- `L3/18_The_Road_to_Dis.md`
- `L3/19_The_Duel_of_Truth_and_Pride.md`
- `L3/20_The_Spark_of_Defiance.md` *(desarmado; su chispa de desafío capturada en cristal)*
- `L3/45_The_Echo_of_Pride.md` *(POV Belial; su disolución)*
- `L3/49_The_New_Pantheon.md` *(vacío de poder que deja)*

## Hilo 03 — Trama Vual: el reencarnado que dos bandos se disputan (Libro I, V1-V5)
**Anclas**: Corin Vasse (humano), Vual (Captain demoníaco), Sariel (Captain angélico), Krass (Squad Leader demoníaco).
**Arco**: Krass muere en una escaramuza sobre terreno sin valor; su indignación moral final es la semilla. Un humano corriente, Corin Vasse, empieza a manifestar un don sin explicación; Vual intenta seducirlo y Sariel intenta protegerlo, y Corin acaba rechazando ambas ofertas sin entender qué ha rechazado. **Hilo explícitamente marcado como "retomable en Libro II/III" — verificar si alguna vez se retoma.**
- `L1/22_What_Should_Not_Have_Burned.md` *(POV Krass)*
- `L1/23_A_Gift_With_No_Name.md` *(POV Corin Vasse)*
- `L1/24_The_Trail_That_Shouldnt_Be_There.md` *(POV Sariel)*
- `L1/25_What_Desire_Promises.md` *(POV Vual)*
- `L1/26_Two_Offers.md` *(POV compartido Corin/Sariel)*

## Hilo 04 — Isla de Turein: la pista sobre Ereloth (Libro I, T1-T4)
**Anclas**: Cassiel (Captain angélico bajo Orifiel), Selm (Squad Leader demoníaco bajo Leraje).
**Arco**: dos exploradores rivales, uno de cada bando, buscan la resonancia dejada en Turein; ninguno se mata, ambos se van con la mitad de una respuesta. Cassiel entrega a Iofiel la primera prueba de que el origen de Solmire no es el oficial. Conecta directamente con el hilo del Codex Mortalis.
- `L1/31_The_Island_That_Appears_on_No_Map.md` *(POV Cassiel)*
- `L1/32_The_One_Already_Watching.md` *(POV Selm)*
- `L1/33_The_Riddles_With_No_Answer.md` *(POV Cassiel, Selm observando)*
- `L1/34_What_Neither_of_Them_Keeps.md` *(dual POV; cierre)*

## Hilo 05 — Necrópolis / el Coro Silencioso (Libro I, N1-N3)
**Anclas**: Kurel y Daith (Squad Leaders bajo Iofiel).
**Arco**: dos archivistas traducen un himno dañado del Coro Silencioso, encuentran una discrepancia que no pueden justificar, y eligen deliberadamente dejar la última estrofa sin lectura defendible — la primera mención corrupta de Thamorak queda archivada sin nombre. **Promesa deliberadamente abierta: "alguien lo terminará algún día". Verificar si se recoge.**
- `L1/28_What_the_Choir_Wont_Sing.md`
- `L1/29_The_Discrepancy.md`
- `L1/30_What_Remains_Unnamed.md`

## Hilo 06 — Hollowseam: la tregua que nadie admite (Libro I, H1-H4)
**Anclas**: Thoria (Squad Leader angélica, Centinela del In-Between), Vem (Squad Leader demoníaco, Desestabilizador de Entornos).
**Arco**: una fisura inestable obliga a dos patrullas enemigas a cooperar en silencio; ninguno de los dos lo reporta. Es el primer precedente en la obra de cooperación Cielo-Infierno, mucho antes del Concordato de Ceniza del Libro III.
- `L1/39_The_Rift_That_Shouldnt_Exist.md` *(POV Thoria)*
- `L1/40_What_Not_Even_He_Can_Control.md` *(POV Vem)*
- `L1/41_A_Truce_Neither_Will_Admit_To.md` *(dual POV)*
- `L1/42_What_Goes_Unspoken.md` *(cierre)*

## Hilo 07 — Foras vs. Vepar, semilla del cisma (Libro I, F1-F3)
**Anclas**: Malthus (Captain bajo Foras), Stolas (Captain bajo Vepar), Foras, Vepar.
**Arco**: con Belial ausente en el Sepulcro, sus dos comandantes se disputan territorio; Foras impide a Malthus matar a Stolas porque un Captain muerto daría a Vepar la excusa que busca. Primera grieta real del frente unido del Infierno. Continúa en el Hilo 12.
- `L1/35_The_Price_of_Absence.md` *(POV Malthus)*
- `L1/36_What_the_Tide_Smells.md` *(POV Stolas)*
- `L1/37_A_War_Nobody_Declares.md` *(cierre)*

## Hilo 08 — El arco de Gabriel
**Ancla**: Gabriel. Secundarios: Uriel, Zadkiel, Raphael, Camael, Iofiel, Lucifer, Vepar.
**Arco**: de segundo de Miguel y voz del Consejo → líder de facto de un Cielo descabezado y fracturado → el que elige creer públicamente a un Michael que vuelve sin credenciales → negociador del Concordato de Ceniza con Lucifer → gestor de la crisis de identidad de un Cielo sin General ni enemigo claro.
- `L1/01_A_Wound_in_the_World.md`
- `L1/03_Verdict_of_Dawn.md`
- `L1/08_The_Weight_of_a_Crown_of_Light.md`
- `L1/12_A_Silence_in_Heaven.md`
- `L1/14_Dreams_of_Laughter.md`
- `L1/27_A_Fissure_in_the_Light.md`
- `L1/38_The_Irreverent_Judgment.md`
- `L1/44_A_Truth_Offered.md`
- `L1/49_The_Sundered_Sky.md`
- `L1/52_The_Sound_of_Retreat.md`
- `L1/54_The_Echo_of_the_Sword.md`
- `L2/03_A_Throne_of_Fractured_Light.md`
- `L2/11_A_Petition_of_Scars.md` *(POV Camael, en el consejo de Gabriel)*
- `L2/16_A_Category_No_One_Has.md`
- `L2/17_A_Mission_into_Memory.md`
- `L2/21_A_World_Awakened.md`
- `L2/26_Report_from_the_Abyss.md`
- `L2/31_The_Unseen_War_in_Heaven.md`
- `L2/36_The_Councils_Fracture.md`
- `L2/45_Three_Anomalies.md`
- `L2/46_A_Verse_Withheld.md`
- `L2/53_The_Voices_Gather.md`
- `L3/21_The_Commanders_Return.md`
- `L3/22_A_Council_of_War_and_Faith.md`
- `L3/24_A_Truce_of_Shadows_and_Light.md`
- `L3/27_The_World_That_Was.md`
- `L3/28_The_Concordat_of_Ash.md`
- `L3/42_The_Sovereigns_Farewell.md`
- `L3/44_The_Tempered_Flame.md` *(POV Uriel; Gabriel presente)*
- `L3/49_The_New_Pantheon.md`

## Hilo 09 — Thaeriel / Arin Cross
**Ancla**: Arin Cross → Thaeriel.
**Arco**: mercenario cazador de criminales de guerra en la Tierra → detecta el "olor del Vacío" y a Charon Corp → despierta como Thaeriel, el Olvidado del Sufrimiento Justo → abandona el oficio, invoca una imagen fantasma de Lament, entra al Infierno → juzga la ciudad de Malignus, desarma a Belial y recupera Lament → aporta la aceptación de su propia crueldad a la forja de Aetheris → se queda en el Sepulcro, esta vez por elección.
- `L1/07_Hunter_of_Echoes.md` *(mención; Sariel rastrea)*, `L1/11_Crossings.md`, `L1/12_A_Silence_in_Heaven.md`, `L1/50_The_Resonance.md`, `L1/54_The_Echo_of_the_Sword.md` *(siembra)*
- `L2/02_The_Ghost_of_the_Balkans.md`
- `L2/07_The_Scent_of_the_Void.md`
- `L2/15_Infiltration.md`
- `L2/18_Wrath_of_the_Just.md`
- `L2/25_The_Hunter_and_the_Hunted.md`
- `L2/30_City_of_Whispering_Shadows.md`
- `L2/34_An_Unseen_Interrogation.md`
- `L2/37_The_Convergence_Point.md` … `L2/44_Two_Roads_from_a_Crossroads.md` *(dual POV con Mikel; ver Hilo principal)*
- `L2/51_The_Vow_of_the_Just.md` *(abraza el nombre Thaeriel)*
- `L2/53_The_Voices_Gather.md`
- `L3/03_A_Path_to_Hell.md`
- `L3/09_Judgment_Not_Wrath.md`
- `L3/13_The_Heart_of_Hell.md`
- `L3/16_The_Three_Forgotten.md`
- `L3/17_The_Sages_Plan.md`
- `L3/18_The_Road_to_Dis.md`
- `L3/19_The_Duel_of_Truth_and_Pride.md`
- `L3/20_The_Spark_of_Defiance.md`
- `L3/33_The_Nexus_Path.md`, `L3/36_The_Fallens_Debt.md`, `L3/37_The_Nexus_of_All_Things.md`, `L3/38_The_Forge_of_Balance.md`, `L3/39_The_Final_Confrontation.md`, `L3/40_The_Sundering_Judgment.md`
- `L3/46_The_Whispering_Dawn.md`
- `L3/48_The_Parting_of_Ways.md`
- `L3/52_The_Silent_Guardians.md`

## Hilo 10 — Ereloth / Milo Ray
**Ancla**: Milo Ray → Ereloth.
**Arco**: bardo errante y aparentemente inofensivo que observa desde lejos → desintegra a un Captain de Hell sin levantar un arma (el evento que rompe la categoría de ambos bandos) → decide dejar de esperar e intervenir → se revela como Ereloth, el Forjador Risueño, mentor caótico de Mikel → aporta la alegría creativa a la forja → termina caminando el mundo como bardo otra vez, ahora por elección.
- `L1/50_The_Resonance.md` *(primera mención)*, `L1/54_The_Echo_of_the_Sword.md` *(cierre en la playa, décadas después)*
- `L2/16_A_Category_No_One_Has.md` *(POV Camael; mata a Malthus)*
- `L2/17_A_Mission_into_Memory.md` *(consecuencia: Cielo lo busca)*
- `L2/27_The_Wandering_Bard.md`
- `L2/24_The_Path_of_Laughter.md` *(encuentro no reconocido con Mikel — head-hop deliberado, ver nota de proceso)*
- `L2/35_The_Jesters_Tune.md`
- `L2/53_The_Voices_Gather.md`
- `L3/01_The_Divine_Jester.md` *(primera revelación en página de Milo = Ereloth)*
- `L3/04_The_First_Lesson_Laughter.md`
- `L3/06_The_Storm_of_Sorrows.md`, `L3/07_The_Sword_Remembers.md`
- `L3/15_The_Convergence.md`, `L3/16_The_Three_Forgotten.md`, `L3/17_The_Sages_Plan.md`
- `L3/21_The_Commanders_Return.md`, `L3/22_A_Council_of_War_and_Faith.md`
- `L3/33_The_Nexus_Path.md`, `L3/36_The_Fallens_Debt.md`, `L3/37_The_Nexus_of_All_Things.md`, `L3/38_The_Forge_of_Balance.md`, `L3/39_The_Final_Confrontation.md`, `L3/40_The_Sundering_Judgment.md`
- `L3/48_The_Parting_of_Ways.md`
- `L3/52_The_Silent_Guardians.md`

> ⚠️ **Punto de auditoría conocido**: el repaso final cruzado registró una "desaparición sin explicar de Ereloth" en el Libro III Parte 2 como hallazgo corregido — verificar que la corrección quedó completa.

## Hilo 11 — Azael y los tres Forgotten como tríada
**Anclas**: Azael (el Sabio de la Cumbre), Ereloth, Thaeriel.
**Arco**: cada uno cree ser el único superviviente del Primer Sundering; se reúnen por primera vez desde entonces en `L3/16`. Azael revela que el Vacío es "nuestro hijo" (eco desequilibrado de sus propios principios), diseña el plan de reforja de Aetheris, y termina disolviéndose *hacia dentro* para convertirse en el equilibrio mismo — consciente, no ausente.
- `L1/43_Three_Were_Forged.md` *(la profecía entra en escena, sin nombres)*
- `L1/46_The_Summit.md` *(la figura de la cumbre, deliberadamente sin nombrar — cero nombres propios en el archivo)*
- `L2/06_Whispers_of_the_Summit.md` *(POV Azael, sin nombrar)*
- `L2/14_The_Herb_of_Stillness.md` *(⚠️ corrección KG 2026-08-22: NO hay visita de Mikel al Sabio en la prosa — el capítulo es la intervención remota durante el ataque del callejón, par de `L2/06`)*
- `L2/42_The_Still_Point_of_the_Turning_World.md`, `L2/43_A_Memory_of_Three.md` *(la revelación cuidadosa de Azael)*
- `L3/10_The_Summits_End.md` *(primer POV directo de Azael; "Azael" liberado como término)*
- `L3/14_Reading_the_Scars.md`
- `L3/16_The_Three_Forgotten.md` *(reunión completa, silenciosa)*
- `L3/17_The_Sages_Plan.md` *("Thamorak" y "Aetheris" revelados por primera vez)*
- `L3/33_The_Nexus_Path.md`
- `L3/37_The_Nexus_of_All_Things.md`
- `L3/38_The_Forge_of_Balance.md` *(AETHERIS REFORJADO)*
- `L3/39_The_Final_Confrontation.md`
- `L3/40_The_Sundering_Judgment.md` *(transformación de Azael)*
- `L3/47_The_Final_Verse.md` *(el verso de Azael en el Codex)*
- `L3/48_The_Parting_of_Ways.md`
- `L3/52_The_Silent_Guardians.md`

## Hilo 12 — Rivalidad Vepar vs. Foras (3 libros, con sus capitanes)
**Anclas**: Foras (Commander/Peste Espiritual), Vepar (Commander/Control Marítimo). Capitanes: Malthus, Marbas, Raum (bajo Foras); Stolas, Valefar, Vine (bajo Vepar).
**Arco**: rivalidad soterrada bajo Belial → la muerte de Malthus debilita políticamente a Foras → sus propios capitanes lo prueban → Vepar asciende por pragmatismo (llega a aliarse con comandantes angélicos) mientras Foras se hunde en el dogma y fracasa repetidamente. Al cierre del Libro III, Foras marcha por cuarta vez sobre una fortaleza vacía y fracasa por cuarta vez; Vepar ni siquiera compite por el trono vacío de Belial.
- `L1/35_The_Price_of_Absence.md`, `L1/36_What_the_Tide_Smells.md`, `L1/37_A_War_Nobody_Declares.md` *(Hilo 07)*
- `L1/18_Those_Waiting_for_a_Stumble.md`, `L1/21_What_Winning_Costs.md`, `L1/45_The_Master_of_Lament.md` *(Foras junto a Belial)*
- `L1/32_The_One_Already_Watching.md` *(Selm operando para el aparato de Vepar)*
- `L2/28_The_Tide_Remembers.md` *(POV Vepar, con Foras — el cisma explícito)*
- `L2/29_The_Grief_They_Mistook_for_Softness.md` *(Marbas/Raum prueban a Foras herido)*
- `L2/50_The_Unaccounted_Variable.md` *(ambos bajo el decreto de Belial)*
- `L3/12_The_In-Between_War.md` *(POV Camael/Vepar)*
- `L3/24_A_Truce_of_Shadows_and_Light.md` *(Vepar negocia con Gabriel)*
- `L3/29_The_Uneasy_Vanguard.md` *(Camael/Vepar)*
- `L3/30_Whose_Idea_This_Was_Already.md` *(Naamah se apropia del crédito de Vepar)*
- `L3/34_The_Fleet_of_Dawn_and_Dusk.md`, `L3/35_The_War_Against_Nothingness.md`, `L3/41_The_Quiet_Battlefield.md`
- `L3/49_The_New_Pantheon.md`
- `L3/50_What_the_Cube_Found.md` *(Foras fracasando, visto desde fuera)*
- `L3/51_The_Door_No_One_Sealed.md` *(Valefar/Vine bajo Vepar; primera aparición de ambos)*

## Hilo 13 — Naamah y sus capitanes
**Anclas**: Naamah (Commander/Manipulación Social). Capitanes: Gusion, Phenex, Leraje, más Ronove y Dantalion (heredados de Aamon).
**Arco**: comandante política que opera por apropiación de crédito y reclutamiento oportunista; absorbe la legión huérfana de Aamon (muerto en el Libro I y nunca reasignada en prosa) aprovechando el vacío burocrático de una Hell fracturada en tres cortes.
- `L3/30_Whose_Idea_This_Was_Already.md` *(POV Naamah; primera aparición; Gusion)*
- `L3/31_What_No_One_Came_Back_For.md` *(POV Naamah; recluta a Ronove y Dantalion)*
- `L3/32_Two_Ways_to_Ruin_a_Man.md` *(POV Naamah; Phenex y Leraje)*
- Contexto obligatorio: `L1/13_The_Devils_Gambit.md` y `L1/15_The_Price_of_Truth.md` (muerte de Aamon, legión "scattered and leaderless")

## Hilo 14 — Agares y su red
**Anclas**: Agares (Commander/Manipulación del Lenguaje). Capitanes: Vual, Flauros, Amy. Squad Leader: Nymos.
**Arco**: Agares fabrica un Codex Mortalis falsificado y lo hace llegar al inframundo mortal antes que el texto real de Cielo, ganando una guerra de información que Cielo no eligió; Lucifer aprueba el texto después. En el Libro III, tras la disolución de Belial, cataloga la vacilación de cada soldado. **Agares se mantiene deliberadamente fuera de cámara hasta `L3/50`.**
- `L2/47_A_Truth_Told_First.md` *(POV Vual; Nymos; el falso Codex se planta)*
- `L2/48_A_Familiar_Shape_in_Borrowed_Words.md` *(POV Lucifer; aprueba el texto)*
- `L3/50_What_the_Cube_Found.md` *(POV Amy/Flauros; primera presencia real de Agares)*
- Contexto: la trama Vual del Libro I (Hilo 03) — mismo personaje, misma red de informantes mortales

## Hilo 15 — Selaphiel / Raziel y sus capitanes
**Anclas**: Selaphiel (Commander/Guardián de la Oración), Raziel (Commander/Portador del Conocimiento Prohibido). Capitanes: Eshriel, Jahiel, Zaphiel (bajo Raziel); Raguel, Hadriel, Jophiel (bajo Selaphiel).
**Arco**: doctrina de revelación controlada — Raziel se guarda deliberadamente un verso del Codex; sus tres capitanes recuperan una inscripción cuya cadencia coincide con lo que él calla, sin que ninguno esté entrenado para oírlo.
- `L2/32_What_the_Staff_Weighs.md` *(dual POV Hadriel/Raguel; primera aparición de ambos)*
- `L2/46_A_Verse_Withheld.md` *(POV Selaphiel/Raziel; primera aparición de ambos)*
- `L2/49_No_One_Trained_to_Hear_It.md` *(POV Raziel/Eshriel/Jahiel/Zaphiel; primera aparición de los tres capitanes)*

## Hilo 16 — Balam y sus capitanes
**Anclas**: Balam (Commander/Tormentas y Furia). Capitanes: Barbas, Orobas, Malphas.
**Arco**: frente fronterizo; un interrogatorio que no se quiebra, y una trampa de destino invertido. Cerrado en el Libro II; **Malphas tiene una entrada de outline reservada y nunca escrita** (`arco_argumental_completo.md`, B3C038, sub-beat `B3-malphas-01`: su crisis de duda profesional al presenciar la caída de Malignus) — deliberadamente no adelantada.
- `L2/12_The_Silence_That_Doesnt_Break.md` *(POV Balam/Barbas; primera aparición de ambos)*
- `L2/13_What_the_Ring_Corrects.md` *(POV Malphas/Orobas; primera aparición de ambos)*
- `L3/49_The_New_Pantheon.md` *(Balam mencionado en el vacío de poder)*

## Hilo 17 — Kushiel y sus capitanes
**Anclas**: Kushiel (Commander/Destructor Divino). Capitanes: Thariel, Sachael, Kemuel.
**Arco**: un solo interludio — la disciplina de "preparación, no desobediencia": Kushiel mantiene a su gente lista sin cruzar la línea de la insubordinación mientras el Consejo se fractura.
- `L3/11_Readiness_Not_Disobedience.md`

## Hilo 18 — Iofiel y el Codex Mortalis
**Ancla**: Iofiel (Captain/Guardiana de la Sabiduría, femenina). Secundarios: Kurel, Daith, Cassiel, Gabriel, Zadkiel, Raziel.
**Arco**: reconstrucción fragmentaria del Codex → la profecía de las tres armas forjadas antes del tiempo entra en el Consejo → recibe pruebas dispersas (Turein, la discrepancia del himno) que no puede aún llevar a Gabriel → cierra la trilogía escribiendo el verso final que Azael dicta.
- `L1/17_What_the_Council_Wont_Decide.md`
- `L1/21_What_Winning_Costs.md`
- `L1/28-30` *(Necrópolis, Hilo 05 — sus Squad Leaders)*
- `L1/34_What_Neither_of_Them_Keeps.md` *(recibe el informe de Cassiel)*
- `L1/43_Three_Were_Forged.md` *(POV Iofiel; la profecía)*
- `L1/44_A_Truth_Offered.md`
- `L1/54_The_Echo_of_the_Sword.md`
- `L2/26_Report_from_the_Abyss.md`
- `L2/46_A_Verse_Withheld.md`
- `L2/49_No_One_Trained_to_Hear_It.md`
- `L3/47_The_Final_Verse.md` *(POV Iofiel; el Codex se completa)*

## Hilo 19 — El arco de Camael
**Ancla**: Camael (Commander/Fuerza Pura). Secundarios: Jeremiel, Vepar, Michael.
**Arco**: comandante contenido y práctico (explícitamente NO impulsivo — ese rasgo es de Uriel) → pierde soldados y a Jeremiel en la caída del Libro I → presencia la muerte de Malthus a manos de algo sin categoría → jura lealtad a Michael entregando su Lágrima de Fe (un guardapelo) → coopera con Vepar hasta construir una confianza provisional real → ordena la retirada gemela cuando llega la ola de equilibrio.
- `L1/04_The_First_Swing.md`
- `L1/07_Hunter_of_Echoes.md`, `L1/11_Crossings.md`
- `L1/48_The_Despairing_Front.md`
- `L1/54_The_Echo_of_the_Sword.md`
- `L2/11_A_Petition_of_Scars.md`
- `L2/16_A_Category_No_One_Has.md`
- `L2/17_A_Mission_into_Memory.md`
- `L3/12_The_In-Between_War.md`
- `L3/23_The_Tear_of_Faith.md`
- `L3/29_The_Uneasy_Vanguard.md`
- `L3/34_The_Fleet_of_Dawn_and_Dusk.md`
- `L3/35_The_War_Against_Nothingness.md`
- `L3/41_The_Quiet_Battlefield.md`
- `L3/49_The_New_Pantheon.md`

## Hilo 20 — El arco de Uriel
**Ancla**: Uriel (Arcángel del Fuego Celestial).
**Arco**: militante dogmático que respalda la ofensiva de Miguel y luego no consigue nombrar su propia duda → acusa a Michael de impostor desenvainando *Ignis Lux* ante el consejo → se transforma en guardián de una paz frágil en un campo de refugiados mixto. **Arco confirmado explícitamente NO reversible en `L3/49`.**
- `L1/03_Verdict_of_Dawn.md`, `L1/04_The_First_Swing.md`, `L1/05_Solmires_Judgment.md`
- `L1/12_A_Silence_in_Heaven.md`
- `L1/17_What_the_Council_Wont_Decide.md`
- `L1/27_A_Fissure_in_the_Light.md`
- `L1/47_The_Eve_of_Ruin.md`
- `L1/49_The_Sundered_Sky.md` *(combate real con Ignis Lux, beat añadido vía llm-council)*
- `L1/52_The_Sound_of_Retreat.md`, `L1/54_The_Echo_of_the_Sword.md`
- `L2/03_A_Throne_of_Fractured_Light.md`, `L2/11_A_Petition_of_Scars.md`
- `L2/31_The_Unseen_War_in_Heaven.md`, `L2/36_The_Councils_Fracture.md`, `L2/45_Three_Anomalies.md`
- `L3/21_The_Commanders_Return.md`, `L3/22_A_Council_of_War_and_Faith.md`
- `L3/44_The_Tempered_Flame.md` *(POV Uriel; su transformación)*
- `L3/49_The_New_Pantheon.md` *(refuerzo explícito, no reversión)*

## Hilo 21 — El arco de Lucifer
**Ancla**: Lucifer (Príncipe Infernal Absoluto).
**Arco**: soberano que observa y no golpea → ni él sabe el origen de Lament → reconoce algo en el Codex falsificado sin poder articularlo (eco de su papel no revelado en el origen de Thamorak) → convence a su corte de que la alianza es autopreservación → guía remotamente a los cuatro viajeros por un pasaje de su propia Caída → se despide de Gabriel advirtiendo de una "guerra más interesante" por venir.
- `L1/02_The_Tree_Outside_Time.md`, `L1/06_Whispers_in_the_Burning_Halls.md`, `L1/09_The_Price_of_Knowledge.md`, `L1/21_What_Winning_Costs.md`
- `L2/10_What_Even_He_Does_Not_Know.md` *(primer POV en todo el proyecto; incluye el beat "Tribute from a Vassal")*
- `L2/48_A_Familiar_Shape_in_Borrowed_Words.md`
- `L2/50_The_Unaccounted_Variable.md` *(7º beat, dual POV)*
- `L3/05_A_Council_of_Fear.md`
- `L3/14_Reading_the_Scars.md` *(su choque con Michael, co-causa del Vacío)*
- `L3/25_The_Logic_of_the_Adversary.md`
- `L3/27_The_World_That_Was.md`
- `L3/28_The_Concordat_of_Ash.md`
- `L3/36_The_Fallens_Debt.md`
- `L3/42_The_Sovereigns_Farewell.md`

## Hilo 22 — Sariel, la cazadora de reencarnaciones
**Ancla**: Sariel (Captain/Cazador de Reencarnaciones, bajo Camael). Secundario: Andras (Captain demoníaco).
**Arco**: rastrea ecos de almas reencarnadas desde el Libro I → protege a Corin Vasse del hilo Vual → reconstruye para el Consejo cómo Belial obtuvo Lament → es enviado a buscar al "mortal sin categoría" → termina en misión de reconocimiento conjunta con un capitán demoníaco, cerrando en respeto mutuo a regañadientes.
- `L1/07_Hunter_of_Echoes.md`
- `L1/11_Crossings.md`, `L1/12_A_Silence_in_Heaven.md`
- `L1/24_The_Trail_That_Shouldnt_Be_There.md`, `L1/26_Two_Offers.md`
- `L2/17_A_Mission_into_Memory.md`
- `L2/20_The_Price_of_Revelation.md`
- `L2/23_A_Thiefs_Legacy.md`
- `L2/26_Report_from_the_Abyss.md`
- `L2/36_The_Councils_Fracture.md`, `L2/45_Three_Anomalies.md`, `L2/53_The_Voices_Gather.md`
- `L3/26_The_Unlikely_Scouts.md` *(dual POV Sariel/Andras)*

## Hilo 23 — Raphael y el hilo de la cosecha de almas / Charon Corp
**Ancla**: Raphael (Arcángel de la Sanación y el Velo). Secundarios: Belial, Orifiel, Ezequiel, Anael.
**Arco**: el primero en detectar el coste oculto de Solmire (suelo estéril tras Zaphor'el) → gestiona el desgaste del Cielo → se le da un uso puntual de la función oscura de *Veritas* (aprisionar almas) ligada a la cosecha de Charon Corp.
- `L1/03_Verdict_of_Dawn.md`, `L1/05_Solmires_Judgment.md`, `L1/08_The_Weight_of_a_Crown_of_Light.md`, `L1/14_Dreams_of_Laughter.md`
- `L1/27_A_Fissure_in_the_Light.md`, `L1/49_The_Sundered_Sky.md`, `L1/53_Sparks_for_the_Numb.md`, `L1/54_The_Echo_of_the_Sword.md`
- `L2/03_A_Throne_of_Fractured_Light.md`, `L2/04_The_First_Breach.md`, `L2/05_What_the_Hands_Are_For.md`
- `L2/09_The_Soul_Reapers.md` *(POV Belial; la operación Charon Corp)*
- `L2/07_The_Scent_of_the_Void.md`, `L2/15_Infiltration.md` *(Arin infiltra Charon Corp)*
- `L2/21_A_World_Awakened.md`, `L2/26_Report_from_the_Abyss.md`, `L2/31_The_Unseen_War_in_Heaven.md`, `L2/53_The_Voices_Gather.md`
- `L3/22_A_Council_of_War_and_Faith.md`

## Hilo 24 — Zadkiel y el hilo del ciclo de reencarnación medido
**Ancla**: Zadkiel (Commander/Retribución Justa, arma *Decretum*).
**Arco**: el que mide institucionalmente cuánto se ha doblado el ciclo; juzga con Decretum a la "entidad" capturada, mostrando que su poder es literalmente judicial y no retórico. **Su línea de `L1/54` ("el ciclo no está roto, pero está doblado más de lo que he medido nunca... no sé lo que cuesta devolverlo") es una promesa narrativa explícita — verificar si se paga.**
- `L1/17_What_the_Council_Wont_Decide.md`, `L1/27_A_Fissure_in_the_Light.md`, `L1/54_The_Echo_of_the_Sword.md`
- `L2/03_A_Throne_of_Fractured_Light.md`, `L2/11_A_Petition_of_Scars.md`
- `L2/31_The_Unseen_War_in_Heaven.md` *(el juicio con Decretum)*
- `L2/45_Three_Anomalies.md`

## Hilo 25 — Thamorak / el Vacío, y sus testigos mortales y menores
**Anclas rotativas**: Lyra (centinela), Barachiel (Captain), el guardián sin nombre de Elysia Minor, Seren (piloto novata), Margaret Hollis (bibliotecaria), la archivista, Elena Voss / Dr. Amara Osei / Padre Dominic.
**Arco**: manifestaciones escaladas del Vacío desde una patrulla fronteriza hasta una nebulosa → revelación de su origen (el choque Michael-Lucifer *dio carácter*, pero la resonancia accidental de las tres armas fue la causa mecánica — jerarquía causal de dos capas, ver riesgo documentado en B3C13) → reintegración como entropía natural → efectos del nuevo equilibrio en el mundo mortal.
- `L1/30_What_Remains_Unnamed.md` *(la primera mención corrupta, sin nombre)*
- `L1/43_Three_Were_Forged.md` *(la profecía de las tres armas — ⚠️ corrección KG 2026-08-22: la cláusula "si los tres despiertan, ÉL despertará también" NO existe en la prosa de este capítulo ni de ninguno; es herencia del lore file. En prosa, el vínculo armas→Vacío lo establece Azael en `L3/17`)*
- `L2/50_The_Unaccounted_Variable.md` *(el Enforcer "negado, no muerto")*
- `L3/02_The_Unraveling.md` *(POV Lyra)*
- `L3/08_The_Whispering_Scars.md` *(POV Barachiel; muere enviando el aviso)*
- `L3/12_The_In-Between_War.md`
- `L3/14_Reading_the_Scars.md` *(revelación del origen)*
- `L3/17_The_Sages_Plan.md` *("Thamorak" nombrado por primera vez)*
- `L3/27_The_World_That_Was.md` *(caída de Elysia Minor)*
- `L3/34_The_Fleet_of_Dawn_and_Dusk.md` *(POV Seren)*
- `L3/35_The_War_Against_Nothingness.md`
- `L3/39_The_Final_Confrontation.md`, `L3/40_The_Sundering_Judgment.md`
- `L3/41_The_Quiet_Battlefield.md`
- `L3/43_The_Unchained_Soul.md` *(POV Margaret Hollis; el ciclo reescrito visto desde un alma humana)*
- `L3/46_The_Whispering_Dawn.md` *(montaje del mundo mortal)*

## Hilo 26 — El eje diplomático Cielo-Infierno (Concordato de Ceniza)
**Anclas**: Gabriel, Lucifer, Vepar, Camael, Asmodeus.
**Arco**: de dos treguas soterradas y no reportadas (Hollowseam en el Libro I, Turein) → la primera negociación explícita de Gabriel con el Infierno → el Concordato de Ceniza como alianza utilitaria, no reconciliación → la vanguardia mixta → el nuevo panteón de grises. **Se audita por separado del Hilo 08 porque la aritmética de encuentros (Camael-Vepar cuarto encuentro; Gabriel "primer trato con el Infierno") ya ha producido contradicciones detectadas.**
- `L1/39-42` *(Hollowseam, Hilo 06 — precedente)*
- `L3/24_A_Truce_of_Shadows_and_Light.md`
- `L3/25_The_Logic_of_the_Adversary.md`
- `L3/28_The_Concordat_of_Ash.md`
- `L3/29_The_Uneasy_Vanguard.md`
- `L3/34_The_Fleet_of_Dawn_and_Dusk.md`
- `L3/42_The_Sovereigns_Farewell.md`
- `L3/49_The_New_Pantheon.md` *(dual POV Gabriel/Asmodeus; primera aparición real de Asmodeus)*

## Hilo 27 — Interludios sueltos de un solo capítulo (agrupados)
Se agrupan por función (dar primera escena a personajes fichados sin apariciones), no por trama compartida. Cada uno es autocontenido; auditarlos juntos permite comprobar si alguno introduce material que el resto de la obra nunca recoge.

**27a — Orifiel / Ezequiel / Laila (órbita de Orifiel, Libro II)**
- `L2/04_The_First_Breach.md` *(POV Orifiel/Ezequiel)*
- `L2/05_What_the_Hands_Are_For.md` *(POV Laila; ligada a "la búsqueda" de Solmire, hilo abierto en `L2/03` y confirmado sin resolver en `L2/45`)*

**27b — Raguel / Hadriel (órbita de Selaphiel, Libro II)** — ver también Hilo 15
- `L2/32_What_the_Staff_Weighs.md`

**27c — Anael (Libro I)**
- `L1/53_Sparks_for_the_Numb.md` *(POV Anael; cierra su única aparición previa, una frase de montaje en `L1/54`)*

## Hilo 28 — Aamon y la legión huérfana
**Anclas**: Aamon (Commander/Maestro Militar), Belial, Naamah, Ronove, Dantalion.
**Arco**: Aamon es asesinado por Belial en el Libro I como precio de un ritual; su legión queda "scattered and leaderless" y **nunca se reasigna en prosa hasta el Libro III**, donde Naamah la absorbe. Se audita por separado porque es el caso canónico de "muerte con consecuencias diferidas dos libros" y porque hay una nota de proceso que lo sitúa erróneamente en B2C37.
- `L1/13_The_Devils_Gambit.md`
- `L1/15_The_Price_of_Truth.md`
- `L2/23_A_Thiefs_Legacy.md`, `L2/26_Report_from_the_Abyss.md`, `L2/50_The_Unaccounted_Variable.md` *(referencias póstumas)*
- `L3/31_What_No_One_Came_Back_For.md`
- `L3/32_Two_Ways_to_Ruin_a_Man.md`

## Hilo 29 — El destino de las tres armas primordiales
**Objeto-ancla**: Solmire, Lament/Lamentun, Aetheris.
**Arco**: Solmire (Ereloth → Miguel → perdida en la Tierra → resonancia en Turein → reclamada por Michael → enterrada bajo su colina); Lament (Thaeriel → robada por Belial → recuperada por Thaeriel → reposa en el Sepulcro); Aetheris (Azael → rota en el Primer Sundering → reforjada en el Nexo → indistinguible del equilibrio). Se audita por separado porque los tres destinos finales fueron un fix explícito de Codex y porque la ubicación de Lament ya produjo una contradicción detectada entre `L3/46` y `L3/52`.
- `L1/02_The_Tree_Outside_Time.md`, `L1/20_The_True_Tomb.md`, `L1/31-34` *(Turein)*, `L1/43_Three_Were_Forged.md`, `L1/45_The_Master_of_Lament.md`, `L1/50-51`, `L1/54`
- `L2/05_What_the_Hands_Are_For.md`, `L2/19_The_Isle_of_Whispers.md`, `L2/23_A_Thiefs_Legacy.md`, `L2/45_Three_Anomalies.md`, `L2/51_The_Vow_of_the_Just.md`
- `L3/06_The_Storm_of_Sorrows.md`, `L3/07_The_Sword_Remembers.md`, `L3/18-20`, `L3/33_The_Nexus_Path.md`, `L3/37-40`, `L3/46_The_Whispering_Dawn.md`, `L3/52_The_Silent_Guardians.md`

---

# 3. REGISTRO DE VIDA / MUERTE / REENCARNACIÓN

> **Nota metodológica**: el número de capítulo usado es el del sistema nuevo (`LibroN/EN/NN_Titulo.md`). Los estados finales están tomados de la prosa aprobada, no del outline.

| Nombre | Estado inicial | Evento de muerte / reencarnación / transformación (capítulo) | Estado final al cierre del Libro III |
|---|---|---|---|
| **Miguel / Mikel Ardon / Michael** | General de la Hueste Celestial, portador de Solmire | Cae ante Belial en `Libro1/EN/51_The_Fall.md`; su reencarnación humana se confirma en `Libro1/EN/54_The_Echo_of_the_Sword.md`. Renace como **Mikel Ardon**, profesor en Navarion (todo el Libro II). Reclama Solmire y recupera su identidad en `Libro3/EN/07_The_Sword_Remembers.md`; pasa a llamarse **Michael** desde `Libro3/EN/15_The_Convergence.md`. Acepta un fragmento del Vacío (duda/falibilidad) en `Libro3/EN/40_The_Sundering_Judgment.md` | Vivo. Retirado en la Tierra, sin rango, con Solmire enterrada bajo su colina (`Libro3/EN/52_The_Silent_Guardians.md`). No es "el cuarto forjador": catalizador |
| **Ereloth / Milo Ray** | Olvidado (Luz Irreverente), forjador de Solmire; encarnado como bardo errante | Nunca muere. Revelación de identidad en `Libro3/EN/01_The_Divine_Jester.md`. Acepta su fragmento del Vacío (apatía/vanidad) en `Libro3/EN/40_The_Sundering_Judgment.md` | Vivo. Camina el mundo como bardo, por elección (`Libro3/EN/52`). NO cae en las Sombras Sin Nombre |
| **Thaeriel / Arin Cross** | Olvidado (Sufrimiento Justo), forjador de Lament; encarnado como mercenario | Nunca muere. Abraza su nombre real en `Libro2/EN/51_The_Vow_of_the_Just.md`. Acepta su fragmento (crueldad/juicio ciego) en `Libro3/EN/40` | Vivo, con memoria intacta (confirmado explícitamente en `Libro3/EN/46_The_Whispering_Dawn.md` — no es un doble amnésico). Reside en el Sepulcro con Lament, por elección. NO cae en Thae'Zakar |
| **Azael** | Olvidado (Equilibrio), forjador de Aetheris; encarnado como el Sabio de la Cumbre | Se disuelve *hacia dentro* en `Libro3/EN/40_The_Sundering_Judgment.md` — transformación, NO muerte ni desaparición (fix mayor explícito de Codex) | Presencia consciente difusa, distribuida por todo el equilibrio. Habla en primera persona en `Libro3/EN/48_The_Parting_of_Ways.md`. NO cae en Azeloth |
| **Belial** | Lord del Orgullo y el Poder, arma *Ruach* | Asesina a Aamon en `Libro1/EN/15_The_Price_of_Truth.md`. Reclama Lament en `Libro1/EN/20_The_True_Tomb.md`. Derrotado y desarmado por Thaeriel en `Libro3/EN/20_The_Spark_of_Defiance.md`. **Colapso metafísico ordinario en `Libro3/EN/45_The_Echo_of_Pride.md`** — su forma se disuelve por agotamiento de voluntad, sin violencia | **No muere de Muerte Final.** Su forma demoníaca colapsa; su alma entra en el ciclo de reencarnación ya reescrito, y encuentra el pull antiguo ausente. Destino deliberadamente abierto: descanso, regreso o guardianía, a su elección |
| **Aamon** | Commander / Maestro Militar, bajo Leviathan; arma *Skarth* | **Muere en `Libro1/EN/15_The_Price_of_Truth.md`** — Belial lo empuja sobre un sigilo, drena su esencia y le clava Ruach en el corazón | Muerto. Su legión queda "scattered and leaderless" y no se reasigna hasta que Naamah la absorbe en `Libro3/EN/31_What_No_One_Came_Back_For.md`. ⚠️ Nota interna en `book3_part1_expanded_beats.md` lo sitúa erróneamente como "muerto en B2C37" — el error está en la nota, no en la prosa |
| **Malthus** | Captain / Rituales Oscuros, bajo Foras | **Muere en `Libro2/EN/16_A_Category_No_One_Has.md`** — ataca a Milo Ray creyéndolo Miguel y es desintegrado junto a su guardia. ⚠️ **No muere en el Libro I**: en `Libro1/EN/37_A_War_Nobody_Declares.md` está vivo y es el POV | Muerto/deshecho. Referenciado después en `Libro2/EN/17`, `Libro2/EN/23`, `Libro2/EN/28` y `Libro2/EN/29` como la causa de la debilidad política de Foras |
| **Nael** | Squad Leader / Motivación de Batalla, bajo Jeremiel → Camael; arma *Coragio* | Cae herida en `Libro1/EN/05_Solmires_Judgment.md` y **es sanada por Raphael — SOBREVIVE** ("Word of Nael's survival had already spread") | ⚠️ **Contradice `personajes_muertes_reencarnaciones.md`**, que declara su muerte en ese capítulo y construye sobre ella toda una subtrama de reencarnación (Foras vs. Raphael persiguiendo a "Nathaniel Vale"). "Nathaniel" tiene **cero apariciones** en los 159 capítulos. Ver Hallazgo #1 |
| **Krass** | Squad Leader / Fletcher de Emoción, bajo Leraje | **Muere en `Libro1/EN/22_What_Should_Not_Have_Burned.md`**, en combate, sobre terreno sin valor estratégico | Muerto. Su indignación moral final es la semilla temática de la trama Vual, pero él no vuelve |
| **Jeremiel** | Captain / Moral y Táctica, bajo Camael; arma *Diké* | Muere en el clímax del Libro I (implícito entre `Libro1/EN/48_The_Despairing_Front.md` y `Libro1/EN/54`); Camael pule su espada como duelo en `Libro1/EN/54_The_Echo_of_the_Sword.md` | Muerto. Sin reaparición ni reencarnación mostrada |
| **Barachiel** | Captain / Comunicaciones Angélicas | **Consumido por el Vacío en `Libro3/EN/08_The_Whispering_Scars.md`**, junto a su torre de vigilancia entera (40 soldados, Halaliel, Ophaniel) — "un-written", no muerto en el sentido ordinario | Borrado. Su mensaje final (*"It's not killing us, it's un-writing us!"*) es el aviso que llega al Cielo |
| **Vorlag** | Duque demoníaco de Malignus | No muere. Su ciudad colapsa cuando Thaeriel invalida la mentira estructural que la sostenía (`Libro3/EN/09_Judgment_Not_Wrath.md`) | Vivo, destruido políticamente, en pie sobre sus propias ruinas. **No vuelve a aparecer** — hilo abierto |
| **Corin Vasse** | Humano corriente con un don sin explicar (posible alma reencarnada) | No muere. Rechaza las ofertas de Vual y Sariel en `Libro1/EN/26_Two_Offers.md` | Vivo, sin resolver. **No reaparece en Libros II ni III** pese a que el hilo se marcó como "retomable" — promesa abierta |
| **Selm** | Squad Leader / Sombra Acechante, bajo Leraje | No muere. Se retira del enfrentamiento con Cassiel en `Libro1/EN/34_What_Neither_of_Them_Keeps.md` | Vivo. No reaparece |
| **Cassiel** | Captain / Explorador Espiritual, bajo Orifiel | No muere | Vivo. Entrega la primera prueba contra el origen oficial de Solmire; aparece por última vez en `Libro1/EN/54` |
| **Kurel / Daith** | Squad Leaders bajo Iofiel | No mueren | Vivos. Archivan el himno sin lectura defendible (`Libro1/EN/30_What_Remains_Unnamed.md`); no reaparecen |
| **Thoria / Vem** | Squad Leaders (angélica / demoníaco) | No mueren | Vivos. Su tregua no reportada queda solo entre ellos (`Libro1/EN/42_What_Goes_Unspoken.md`); no reaparecen |
| **Lyra** | Ángel centinela menor | No muere; única superviviente de su puesto (`Libro3/EN/02_The_Unraveling.md`). Sus compañeros **Corym** y **Othiel** son consumidos por el Vacío en ese mismo capítulo | Viva. ⚠️ El repaso final registró un "hilo de Lyra sin recoger" como hallazgo — verificar que la corrección quedó cerrada |
| **Seren** | Piloto angélica novata | No muere (`Libro3/EN/34_The_Fleet_of_Dawn_and_Dusk.md`) | Viva. Personaje de un solo capítulo, sin arco pendiente |
| **Margaret Hollis** | Bibliotecaria humana anciana, moribunda | **Muere en `Libro3/EN/43_The_Unchained_Soul.md`** y, bajo el ciclo ya reescrito, **elige** permanecer como espíritu guardián de su biblioteca en vez de descanso o nueva vida | Guardiana consciente de su biblioteca. Es la demostración íntima del nuevo mecanismo del ciclo |
| **El "Enforcer" de Belial** (sin nombre) + su escuadra (8 soldados) | Fuerza de élite de Belial | **"Denegados", no muertos, en `Libro2/EN/50_The_Unaccounted_Variable.md`** — sin cuerpos, sin esencia recuperable; la piscina de escrutinio se niega tres veces a mostrar el momento | Borrados. Belial nunca averigua qué ocurrió. ⚠️ Hilo abierto: el texto nunca confirma la causa *(corrección KG 2026-08-22: el candidato en página es el Vacío o **Azael** — la congelación gris de `L2/42-43` —, no Ereloth)* |
| **Foras** | Commander / Peste Espiritual, bajo Belial | No muere. Debilitado políticamente por la muerte de Malthus (`Libro2/EN/28`, `Libro2/EN/29`) | Vivo. Marchando una cuarta vez sobre la fortaleza vacía de Belial y fracasando una cuarta vez (`Libro3/EN/50`, `Libro3/EN/51`) — hundido en el dogma |
| **Vepar** | Commander / Control Marítimo, bajo Belial (masculino, translúcido, tridente *Marea*) | No muere. Negocia con Gabriel (`Libro3/EN/24`), construye confianza real con Camael (`Libro3/EN/29`) | Vivo y ascendente. Rehúsa competir por el trono vacío de Belial, ocupado con la flota y su lealtad a comandantes angélicos (`Libro3/EN/49`, `Libro3/EN/51`) |
| **Camael** | Commander / Fuerza Pura, espada *Ramiel* | No muere. Entrega su Lágrima de Fe (un guardapelo) en `Libro3/EN/23_The_Tear_of_Faith.md` | Vivo. Ordena la retirada gemela con Vepar (`Libro3/EN/41`); su arco fue explícitamente cerrado tras detectarse "sin cierre" en el repaso final |
| **Uriel** | Arcángel del Fuego Celestial, arma *Ignis Lux* | No muere. Transformación de guerrero dogmático a guardián de una paz frágil en `Libro3/EN/44_The_Tempered_Flame.md` | Vivo, transformado. Arco **no revertido** en `Libro3/EN/49` (verificación explícita) |
| **Gabriel** | Arcángel de la Voz Divina, arma *Vox Aeternum* | No muere | Vivo. Líder de facto de un Cielo en crisis de identidad; se despide de Lucifer en `Libro3/EN/42` |
| **Lucifer** | Príncipe Infernal Absoluto | No muere | Vivo. Advierte de una "guerra más interesante" por venir (`Libro3/EN/42`) — gancho deliberado hacia una posible Saga II |
| **Raphael** | Arcángel de la Sanación y el Velo, arma *Veritas* | No muere | Vivo (`Libro3/EN/22`) |
| **Zadkiel** | Commander / Retribución Justa, arma *Decretum* | No muere | Vivo. Última aparición en `Libro2/EN/45_Three_Anomalies.md` — no aparece en el Libro III pese a su promesa narrativa sobre el ciclo doblado |
| **Iofiel** | Captain / Guardiana de la Sabiduría (femenina) | No muere | Viva. Escribe el verso final del Codex en `Libro3/EN/47_The_Final_Verse.md` |
| **Sariel** | Captain / Cazador de Reencarnaciones | No muere | Vivo (`Libro3/EN/26_The_Unlikely_Scouts.md`) |
| **Andras** | Captain / Sabotaje Rápido, bajo Aamon | No muere | Vivo (`Libro3/EN/26`). ⚠️ Corrección aplicada en el repaso final: mostraba su rostro pese a su rasgo de ficha "nunca muestra su cara" |
| **Naamah** | Commander / Manipulación Social | No muere | Viva. Ha absorbido la legión huérfana de Aamon (`Libro3/EN/30-32`) |
| **Asmodeus** | Lord del Deseo y la Corrupción Emocional | No muere; primera aparición real en `Libro3/EN/49_The_New_Pantheon.md` | Vivo. Percibe un universo de infinitos tonos de gris |
| **Agares** | Commander / Manipulación del Lenguaje | No muere; deliberadamente fuera de cámara hasta `Libro3/EN/50_What_the_Cube_Found.md` | Vivo. Catalogando la vacilación de cada soldado tras la disolución de Belial |
| **Vual** | Captain / Seductor de Almas Reencarnadas, bajo Agares | No muere | Vivo. Última aparición en `Libro2/EN/47_A_Truth_Told_First.md` |
| **Balam, Barbas, Orobas, Malphas** | Commander + Captains | Ninguno muere | Vivos. Todos con una única escena (`Libro2/EN/12`, `Libro2/EN/13`) |
| **Kushiel, Thariel, Sachael, Kemuel** | Commander + Captains | Ninguno muere | Vivos. Una única escena (`Libro3/EN/11`) |
| **Selaphiel, Raziel, Eshriel, Jahiel, Zaphiel, Raguel, Hadriel, Jophiel** | Commanders + Captains | Ninguno muere | Vivos (`Libro2/EN/32`, `Libro2/EN/46`, `Libro2/EN/49`) |
| **Orifiel, Ezequiel, Laila, Anael** | Commander + Captains | Ninguno muere | Vivos (`Libro2/EN/04`, `Libro2/EN/05`, `Libro1/EN/53`) |
| **Marbas, Raum, Stolas, Valefar, Vine** | Captains bajo Foras / Vepar | Ninguno muere | Vivos (`Libro1/EN/36`, `Libro2/EN/29`, `Libro3/EN/51`) |
| **Gusion, Phenex, Leraje, Ronove, Dantalion** | Captains bajo Naamah / Aamon | Ninguno muere | Vivos, todos operando bajo Naamah al cierre (`Libro3/EN/30-32`) |
| **Flauros, Amy, Nymos** | Captains + Squad Leader bajo Agares | Ninguno muere | Vivos (`Libro2/EN/47`, `Libro3/EN/50`) |
| **Nyx** | Presencia asociada al descenso de Belial | No muere | Sin resolver — única aparición en `Libro1/EN/18_Those_Waiting_for_a_Stumble.md`. ⚠️ Hilo abierto, sin seguimiento |
| **Joran** | Soldado angélico (POV de un solo capítulo) | No muere (`Libro1/EN/05`) | Vivo. Sin reaparición |
| **El ciclo de reencarnación (como "personaje" estructural)** | Contención impuesta tras el Primer Sundering, sin memoria ni elección | **Reescrito en `Libro3/EN/40_The_Sundering_Judgment.md`**: consciencia preservada; descanso, regreso o guardianía pasan a ser elección | Vigente en su forma nueva. Demostrado desde dentro por Margaret Hollis (`Libro3/EN/43`) y por Belial (`Libro3/EN/45`) |

---

# 4. HALLAZGOS PRELIMINARES DETECTADOS AL CONSTRUIR ESTE MAPA

No son la auditoría — son cosas que aparecieron solas al cotejar y que conviene pasar a los agentes como puntos de partida.

1. **Nael: el documento de canon contradice la prosa.** `content/lore/personajes_muertes_reencarnaciones.md` declara que Nael muere en el capítulo 5 del Libro I y construye sobre esa muerte una subtrama completa de reencarnación (renace como "Nathaniel Vale"; Foras la persigue, Raphael la busca; su Death-State Polarity decide el desenlace). En la prosa real de `Libro1/EN/05_Solmires_Judgment.md`, **Nael es herida, sanada por Raphael, y sobrevive explícitamente**. "Nathaniel" tiene cero apariciones en los 159 capítulos y la subtrama nunca se escribió. Además, la ficha de Nael en `personajes.md` no marca género, pero la prosa la trata en femenino ("her voice", "she fell"). Decidir: (a) corregir el documento de tracking, (b) escribir la subtrama, o (c) archivarla como descartada.
2. **Malthus muere en el Libro II, no en el Libro I.** El encargo asumía Libro I; la prosa lo mata en `Libro2/EN/16`. En `Libro1/EN/37` está vivo y es el POV. No es una incoherencia de la obra, pero sí de la memoria del proyecto.
3. **Aamon: nota interna errónea.** `book3_part1_expanded_beats.md` dice "Aamon (muerto en B2C37)". La prosa lo mata en `Libro1/EN/15`. `personajes.md` (línea ~1349) sí lo tiene bien.
4. **Corin Vasse queda sin resolver.** La trama Vual se cerró marcada como "hilo retomable en Libro II/III" y nunca se retomó. Un humano con un don sin explicar, disputado por Cielo e Infierno, desaparece de la obra sin cierre.
5. **La estrofa sin resolver de la Necrópolis nunca se recoge.** `Libro1/EN/30` promete explícitamente que alguien terminará esa lectura algún día. Verificar si `Libro3/EN/47_The_Final_Verse.md` lo paga o si es otra cosa.
6. **La promesa de Zadkiel sobre el ciclo doblado.** En `Libro1/EN/54` dice no saber lo que cuesta devolverlo. El coste real se paga en `Libro3/EN/40`, pero Zadkiel no aparece en el Libro III — verificar si la promesa se cobra con el personaje adecuado o queda huérfana.
7. **Vorlag y Nyx desaparecen sin cierre.** Ambos son presencias con peso en su escena y sin ninguna reaparición.
8. **El "Enforcer" de Belial nunca se identifica.** Su desaparición es el motor de todo el tercer acto del Libro II para Belial y el texto nunca confirma la causa.
9. **Malphas tiene una entrada de outline reservada y nunca escrita** (`B3-malphas-01`, su duda profesional al presenciar la caída de Malignus). Deliberadamente no adelantada — decidir si se escribe o se archiva.

---

# 5. RECUENTO

- **Hilos identificados**: **29** (1 trama principal + 28 subtramas/hilos secundarios, contando los tres subgrupos del Hilo 27 como uno solo; si se cuentan por separado, 31).
- **Personajes en el registro de vida/muerte**: **52 entradas nominales** (+ 5 filas agrupadas que cubren 25 capitanes/comandantes adicionales sin evento de muerte, + 1 entrada estructural para el ciclo de reencarnación). Total de personajes cubiertos: **~78**.
- **Muertes/borrados confirmados en prosa**: Aamon, Malthus, Krass, Jeremiel, Barachiel (+ Halaliel, Ophaniel y 40 soldados), Corym, Othiel, Margaret Hollis (muerte con elección), el Enforcer de Belial y su escuadra de 8.
- **Transformaciones de estado (no muertes)**: Miguel→Mikel→Michael (reencarnación completa), Azael (disolución consciente en el equilibrio), Belial (colapso de forma + alma liberada al ciclo reescrito), Uriel (transformación de carácter), los tres Forgotten (aceptación de fragmentos del Vacío), el ciclo de reencarnación mismo.
- **Reencarnaciones centrales**: solo una completa y mostrada en página — Miguel → Mikel Ardon. Las de los tres Forgotten son encarnaciones humanas *sin* pasar por el ciclo ordinario (sus almas quedaron fuera de él), no reencarnaciones en sentido estricto — distinción canon que la auditoría debe respetar.
