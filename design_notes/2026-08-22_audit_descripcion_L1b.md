# Auditoría de descripción e inmersión — Libro 1, capítulos 28–54 (EN)

Fecha: 2026-08-22 · Tramo: `Libro1/EN/28_*.md` a `54_*.md` (27 capítulos, ~61.500 palabras) · Protocolo: `content/craft/10_auditoria_editorial.md` · Criterios: `content/craft/07_descripcion.md`

**Regla fundamental aplicada**: cada hallazgo está clasificado como error real / debilidad / oportunidad / decisión estilística válida, y respaldado con archivo + pasaje. No hay hallazgos 🔴 en este tramo: nada de lo detectado rompe lógica, continuidad ni comprensión. Los problemas dominantes son de **carencia** y **monotonía de registro**, no de exceso.

---

## 1. Diagnóstico general

El tramo invierte el problema típico: casi nunca hay "bloques que paralizan la tensión" — hay **escasez sistemática de descripción sensorial**, desplazada por interioridad analítica. La cámara vive dentro de las cabezas: los personajes *leen, juzgan, sopesan, catalogan y archivan* la escena en lugar de percibirla. Cuando la prosa sí baja a los sentidos (38, 45, 46, 50, 53, 54), el nivel sube de inmediato — la capacidad está, pero se usa poco entre 28 y 44.

Los capítulos 53–54 pertenecen visiblemente a otra pasada de escritura (o a otro estándar): paleta sensorial variada, símiles frescos, densidad adverbial a la mitad. Son la referencia interna de lo que el resto del tramo podría ser.

**Lo que funciona y debe decirse**:
- El clímax bélico (47–52) **no comete el pecado que la auditoría buscaba**: la descripción nunca frena el combate. Causa-efecto siempre visible, verbos concretos (48 es ejemplar: pulso → Jeremiel cae → Camael levanta soldados a la fuerza → vuelven a caer → mensaje).
- Cada mini-arco tiene identidad sensorial propia y (con una excepción, ver H5) no se pisan entre sí.
- Cap. 46 (The Summit) es una decisión estilística válida: un capítulo entero de descripción estática como interludio antes de la guerra. Funciona como cambio de respiración; solo su tramo medio se diluye (ver H6).

---

## 2. Identidad sensorial por mini-arco

| Arco | Capítulos | Entorno | Ancla dominante | Sentidos presentes | Veredicto |
|---|---|---|---|---|---|
| Necrópolis/archivo (Codex) | 28–30 | Scriptorium | el pergamino mismo; casi nada más | vista (mínima), 1 tacto interoceptivo, 1 sonido (clic del cajón) | ⚠️ identidad casi ausente (H1) |
| Turein | 31–34 | Isla espiral | crecimiento en espiral (14 menciones), luz cambiante, risa fosilizada | vista, oído, tacto (Silens en la palma) | ✔️ identidad clara |
| Foras/Vepar | 35–37 | Corte infernal / estanque | piedra fría, tiza-sangre-ceniza; estanque negro, hilo de sangre, marea | vista, tacto | ✔️ identidad clara; pide olfato a gritos (H2) |
| Hollowseam | 39–42 | Fisura entre planos | suelo "sin decidir su textura", luz en pulsos lentos e irregulares | vista, tacto (suelo), oído | ✔️ identidad clara, pero comparte ancla de luz con Turein (H5) |
| Clímax bélico | 47–52 | Frentes / llanura de ceniza | ceniza gris, silencio como material, pantallas cristalinas | vista, oído, tacto | ✔️ |
| Secuelas | 53–54 | Templo / playa | respiración, campana, lira; aire salobre, gaviotas, hielo en el vaso | vista, oído, tacto, +olfato/gusto por fin | ✔️ el mejor del tramo |

La verificación pedida (¿Turein huele igual que la Necrópolis?) da un resultado irónico: **ningún entorno huele a nada** (ver H2).

---

## 3. Hallazgos

### H1 · 🟠 Carencia sensorial casi total en el arco 28–30
- **Ubicación**: 28_What_the_Choir_Wont_Sing.md, 29_The_Discrepancy.md, 30_What_Remains_Unnamed.md.
- **Problema**: tres capítulos consecutivos de discusión Daith/Kurel donde el único objeto con presencia física es el fragmento del himno. El scriptorium no recibe un solo rasgo sensorial hasta el penúltimo párrafo del cap. 28 ("The scriptorium had gone quiet around them at some point… the light… beginning to fade"). En 29, el único detalle de entorno es "the faint discoloration where both their hands had rested". El pasillo nocturno de Daith (29, §33-37) — su momento de duda privada — transcurre en un corredor sin una sola imagen.
- **Por qué importa**: el lector flota en diálogo + paráfrasis mental durante ~6.500 palabras. El arco pierde el contraste que su propio tema ofrece (un archivo de muertos, siglos de polvo, un himno quemado) y la duda de Daith no tiene mundo contra el cual resonar.
- **Gravedad**: 🟠 (afecta inmersión de un arco entero, no la comprensión).
- **Solución sugerida**: 2–4 anclas concretas por capítulo, sin tocar la estructura: olor a pergamino viejo/tinta, el sonido de la pluma de Daith contra el silencio de Kurel recitando, frío de piedra del archivo profundo en 30. Lo que ya hay (la presión tras el esternón en 30 §9; el clic metálico final en 30 §45) marca el registro correcto — falta multiplicarlo.

### H2 · 🟠 Paleta sensorial monocorde: cero olfato y gusto en 61.500 palabras
- **Ubicación**: todo el tramo. Verificado por grep: `smell|scent|odor|reek|stench|aroma` no aparece **ni una vez** en 28–54 (los únicos matches son subcadenas de "de**scent**"/"a**scent**"). "Taste" solo en usos abstractos (33: "never developed much taste for…").
- **Problema**: la casa pide "paleta sensorial variada" y el checklist de 07 pregunta por "tramos largos donde el único sentido presente es la vista". Aquí el tramo largo es el libro entero: vista + algo de oído + tacto ocasional. El colmo: el cap. 36 se titula **"What the Tide Smells"** y no contiene un solo olor.
- **Por qué importa**: los entornos más olfativos imaginables (cámara ritual con tiza, sangre y ceniza en 35; estanque negro de Vepar en 36; campo de batalla de ceniza en 50–52; enfermería en 53) quedan planos donde una sola nota olfativa daría profundidad inmediata. Recién en 54 §99 aparece "the briny air" — y ese pasaje se siente instantáneamente más vivo que todo lo anterior.
- **Gravedad**: 🟠.
- **Solución sugerida**: no sembrar olores por cuota; elegir 5–6 puntos de máximo rendimiento: (a) 35, ritual de Corvin — ceniza y sangre; (b) 36, el estanque — agua estancada/salobre que justifique el título; (c) 48/50, ceniza y tierra removida del frente; (d) 53, la enfermería (cera, vendas, piedra fría). Una imagen buena por escena, siguiendo la regla de la casa: una > tres.

### H3 · 🟠 La interioridad analítica desplaza a la percepción (franja 31–44)
- **Ubicación**: patrón general; caso extremo 34_What_Neither_of_Them_Keeps.md (standoff Cassiel/Selm).
- **Problema**: la escena se narra mediante verbos cognitivos en cadena — *read as, judged, weighed, catalogued, filed away, turned it over* ("turn/turning X over": 24 apariciones en el tramo; 4 en 36 y 4 en 42). En el standoff de 34, casi cada párrafo es evaluación ("He studied the demon's bearing… as far as Cassiel could judge… Selm judged… weighing the shape of the fight…"): dos personajes se leen mutuamente durante ~2.000 palabras con un solo detalle físico nuevo (el arco ni alzado ni bajado).
- **Por qué importa**: es la causa raíz de H1/H2. La paráfrasis mental produce prosa correcta pero uniforme: todos los POV (un archivista, un cazador, una centinela, un demonio caótico) *piensan con la misma sintaxis*. La regla de prioridad de la casa (interioridad → capas sensoriales → micro-acciones → subtexto) se queda clavada en el primer escalón.
- **Gravedad**: 🟠 como patrón acumulado. Aplicando la regla fundamental: en cualquier capítulo aislado sería decisión estilística defendible (el registro es consistente y deliberado); lo que lo convierte en debilidad es la acumulación 31–44 sin variación de dieta sensorial.
- **Solución sugerida**: en revisión, convertir 1 de cada 3–4 evaluaciones mentales en micro-acción o percepción ("read the delay as…" → mostrar el retraso). No tocar los capítulos donde el registro analítico ES el personaje (Selm en 32 funciona precisamente por su frialdad contable).

### H4 · 🟠 Adverbios y muletillas de intensidad: acumulación medible
- **Ubicación**: pico en 35–40; conteo bruto `\w*ly\b` por capítulo: 35 → 90/2.387 palabras, 40 → 89/2.218, 36 → 85/2.339, 39 → 82, 37 → 78, 38 → 76 (~3,8% del texto). Contraste interno: 54 → 22/2.697, 46 → 33, 53 → 36.
- **Problema**: el grueso no son adverbios de manera sino **intensificadores de cobertura** que repiten o acolchan: "actually" ~180 veces en el tramo (13 solo en 37; 10 en seis capítulos distintos), "exactly" ~140 (14 en 38), "simply" (7+ en 36 y 40), "entirely", "fully", "genuinely", "considerably" (36 veces). Clasificación según el protocolo:
  - **Necesarios**: adverbios de manera en combate y ritual ("sharply", "slowly" con contraste real) — minoría.
  - **Útiles**: algunos "finally/eventually" que marcan duración en escenas de paciencia (Turein).
  - **Prescindibles**: la mayoría de "actually/exactly/simply/entirely" — la frase sobrevive sin ellos en >70% de los casos. Ej.: 37 §7 "the distinction mattered more than the trespass itself" no pierde nada sin el "actually" que lleva al lado; 40 §23 "suddenly, completely rigid" → "rigid" ya lo dice el contexto.
  - **Redundantes**: pares fósiles — "faint but unmistakable" (28 §31, 34 §3, 45 §…), "quietly and precisely", "carefully and deliberately".
- **Muletillas hermanas** (mismo mecanismo, no adverbios): "unhurried" 25 veces (5 en el cap. 33), "long service" 26 (6 en el cap. 40), "the better part of" 6 veces solo en 31–32, "particular(ly)" ~100 (8 en 30 y 52), conector de símil "the way…" (8 en 33, 7 en 34 — ahí es tic; 8 en 53 — ahí cada uno es una imagen distinta y funciona).
- **Por qué importa**: 07_descripcion es explícito — "se multiplican sin que nos demos cuenta". A 3,8% el lector oye el patrón aunque no lo nombre; y "unhurried" repetido aplana justamente el tema del arco de Turein (la paciencia) al decirla en vez de mostrarla.
- **Gravedad**: 🟠 en 35–40; 🟡 en el resto.
- **Solución sugerida**: pasada mecánica de "praxis obligada" (releer y tachar) sobre los seis capítulos pico con lista fija: actually / exactly / simply / entirely / fully / genuinely / considerably / particular. Objetivo realista: bajar a ~50/capítulo (el nivel de 53) sin tocar voz.

### H5 · 🟡 Ancla repetida entre mini-arcos: la "luz extraña que cambia arriba"
- **Ubicación**: Turein 31–34 ("the light overhead shifted/moved through its familiar strange colors": 31 §33/§35, 32 §45, 33 §3/§47, 34 §41) y Hollowseam 39–42 ("strange, shifting light" / "strange light": 39 §27/§31, 40 §13/§45/§47, 41 §49, 42 §3/§9).
- **Problema**: dentro de cada arco la repetición es motivo deliberado (válido). Entre arcos, los dos entornos "imposibles" del libro comparten su ancla principal casi con las mismas palabras — escenas de arcos consecutivos con la misma imagen, exactamente lo que 07 pide evitar ("al repetir, variar la imagen, no solo la palabra").
- **Por qué importa**: Turein y la fisura deben sentirse como dos anomalías distintas; hoy su rasgo más citado es intercambiable.
- **Gravedad**: 🟡.
- **Solución sugerida**: Hollowseam ya tiene su imagen propia y mejor — la luz "in slow, uneven pulses" y el suelo "still deciding what texture it actually intended to have" (39 §17/§27). Apoyarse en el pulso y el suelo indeciso, y reservar "shifting light overhead" para Turein.

### H6 · 🟡 Cap. 46: el interludio se re-declara
- **Ubicación**: 46_The_Summit.md, §3–§23.
- **Problema**: la inmovilidad de la figura se afirma cuatro veces con material casi idéntico (§3, §5, §7, §9: "had not shifted… It had not moved… Nothing about the shape suggested… It simply persisted") y la inaccesibilidad de la cumbre tres veces en registro expositivo (§15, §17, §21: nadie la escaló / el aire no alcanza / no tiene nombre). El capítulo es una decisión estilística válida como pausa hipnótica; su tramo medio la diluye con explicación.
- **Por qué importa**: es el único lugar del tramo donde la descripción sí ralentiza — no una escena de tensión, sino su propio efecto. La letanía funciona a 2 repeticiones; a 4 se vuelve inventario.
- **Gravedad**: 🟡 (⚪ si el autor quiere el ritmo incantatorio completo).
- **Solución sugerida**: compactar §15–§23 (~30%). Conservar intactos §9 (el canto rodado en el lecho del río) y §45 (la fisura como signo de interrogación) — son las dos mejores imágenes del capítulo.

### H7 · 🟡 El duelo (51): combate físico en resumen abstracto
- **Ubicación**: 51_The_Fall.md §3–§11.
- **Problema**: la fase física del duelo central del libro se narra por sumario ("Blow answered blow, parry answered parry", "the same maddening precision", "testing a different angle") — cero coreografía visualizable hasta el empuje final. La regla de combate de la casa (verbos concretos, causa-efecto visible) se cumple en el plano psicológico (el quiebre por la pregunta de Belial está perfectamente causado) pero no en el físico.
- **Por qué importa**: parcialmente deliberado — el duelo se decide con palabras, y el sumario lo subraya. Pero un solo intercambio concreto (un ángulo, una distancia, un pie que resbala en ceniza) en §3–§9 daría cuerpo al empate sin alargar. Tal como está, el lector no puede ver ni un golpe del combate más esperado del libro.
- **Gravedad**: 🟡 (debilidad, no error; la intención es legible).
- **Solución sugerida**: 2–3 frases de choreografía concreta en la fase de tablas; dejar intacto el desenlace verbal.

### H8 · 🟡 Fórmula de apertura repetida: "X found Y exactly where…"
- **Ubicación**: 36 §3 ("Stolas found Vepar exactly where he expected to find him"), 37 §3 ("Malthus found Stolas exactly where his own informants had finally placed him"), 44 §3 ("Gabriel found his brother exactly where he had feared he might"), 47 §37 ("Gabriel found his brother exactly where he expected to"). Variante en 31 §3 ("Cassiel found the wounded soul exactly where Silens told him it would be").
- **Problema**: cinco aperturas de escena con el mismo molde en un tramo de 17 capítulos; dos de ellas con el mismo par de personajes (44/47).
- **Gravedad**: 🔵 (corrección fácil).
- **Solución**: variar dos de las cinco; la de 31 puede quedarse (ahí el molde caracteriza a Silens).

### H9 · 🔵 Ecos verbales menores
- "more observation than question / than accusation": 28 §9, 28 §15, 30 §5 — tres veces el mismo giro en tres capítulos.
- "over their years working the same archive": dos veces casi verbatim dentro del cap. 28 (§7, §17).
- "moving through its familiar strange colors": 33 §47 y 34 §41 en capítulos consecutivos.
- **Gravedad**: 🔵. Sustituciones puntuales.

---

## 4. Registro de adverbios -ly por capítulo (bruto, `\w*ly\b`)

28: 61 · 29: 46 · 30: 57 · 31: 67 · 32: 40 · 33: 66 · 34: 69 · **35: 90** · **36: 85** · 37: 78 · 38: 76 · **39: 82** · **40: 89** · 41: 72 · 42: 65 · 43: 63 · 44: 73 · 45: 71 · 46: 33 · 47: 67 · 48: 51 · 49: 58 · 50: 59 · 51: 73 · 52: 54 · **53: 36** · **54: 22**

Top de los picos (excluidos only/family/likely/holy…): 35 → actually 8, exactly 7, rarely 5, simply 4; 36 → exactly 11, actually 10, simply 7; 40 → actually 10, exactly 9, simply 7, entirely 6. El patrón es de intensificadores, no de adverbios de manera — ver H4.

---

## 5. Pasajes especialmente buenos (conservar tal cual)

1. **38 §29–§31** — el POV fugaz del demonio que corre hacia los árboles: "His lungs burned with every stride, the air tearing raw and hot going in… only the trees, only the reaching them. He did not see the light come." La única vez del tramo en que la masacre se siente desde el cuerpo; el corte a "and then nothing" es el mejor momento de montaje del libro.
2. **46 §9 y §45** — "the way a boulder settles into a riverbed until the current has worn a permanent course around it"; la grieta "curved… into something that would have resembled a question mark carved into the heart of the world". El interludio en su mejor versión.
3. **50 §13** — el choque de conceptos hecho físico sin abstracción: "Colors briefly drained from the grey plain… gravity stuttered underfoot… and sound itself died for one suspended instant before the world remembered how to carry it again."
4. **53 §3–§7** — Anael: el soldado cuyo nombre "produced no more reaction than the sound of rain against a window he had already stopped believing was his to open"; el coraje que prende "the way a struck flint catches dry grass"; la nota afinada a la respiración ajena. El capítulo entero es la referencia de paleta sensorial del tramo.
5. **54 §99–§109** — la playa: "the briny air came off the water like a slow, cool breath… a boat knocked twice against a dock"; el hielo que "rang soft and small, like a bell heard underwater". Primer olfato del tramo y cierre de libro con los cinco sentidos por fin en juego. También §5: "cracked pillars propped against each other like soldiers holding a line no one had ordered them to hold".
6. *(Mención)* **45 §49** — "Lament's edge catching what little light the fortress offered and turning it the color of old grief" + "We will not break their shields… We will break their hearts."

Nota de oficio: en todo el tramo **no hay símiles encadenados** — cuando aparece una metáfora, viene sola. Ese ítem del checklist queda limpio.

---

## 6. Prioridades del tramo

1. 🟠 **H2** — inyectar olfato/gusto en 5–6 puntos de máximo rendimiento (35, 36, 48/50, 53). Máximo efecto por palabra invertida.
2. 🟠 **H4** — pasada mecánica de intensificadores en 35–40 (actually/exactly/simply/entirely + unhurried/particular). Riesgo cero para la voz.
3. 🟠 **H1** — dar cuerpo sensorial al scriptorium en 28–30 (2–4 anclas por capítulo).
4. 🟠 **H3** — en revisión profunda (segunda fase, con aprobación por hallazgo): diversificar evaluación mental → percepción/micro-acción en la franja 31–44.
5. 🟡 H5–H7 según apetito: luz de Hollowseam, compactar 46 §15–§23, 2–3 frases de coreografía en 51.

**Notas por área (solo descripciones/inmersión, este tramo)**: Descripciones 6/10 (28–44) → 8,5/10 (45–54); Inmersión 6,5/10 de promedio, con 53–54 en 9. Las tres cosas que más subirían la calidad: olfato en los entornos fuertes, la poda de intensificadores, y el scriptorium con cuerpo.
