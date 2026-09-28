# Revisión independiente — Libro I, capítulo 1

Fecha: 2026-09-17. Revisor: Codex, segunda opinión sobre el piloto.

**Veredicto: borrador útil de preproducción, no aprobado para generación en cadena.** El reparto de especialidades es razonable y produce advertencias valiosas. Sin embargo, el ensamblado conserva contradicciones que sus propios agentes detectaron, incumple partes esenciales del contrato del documento 18 y todavía no demuestra continuidad en vídeo. El QA automático acierta en varios problemas, exagera otros y deja pasar errores importantes.

## Alcance y método

Contrasté el capítulo completo ES y EN, las seis fichas de escena, las acciones de sus 122 planos, las cinco fronteras, sus estados y las fuentes solicitadas: documentos 14–18, `grafo_conocimiento.md`, fichas de Miguel/Gabriel de `personajes.md` y README del Pewter Sentinel. Consulté además los README de Gabriel y del estado `burned_left_wing` para aclarar discrepancias invocadas por el propio guion. Examiné prompts completos, con revisión principal de S2_P08, S4_P20 y S6_P22, y comprobaciones adicionales donde había conflictos.

Para la revisión interna elegí **S5 y S2** mediante una selección pseudoaleatoria reproducible: `random.Random(20260917).sample(range(1, 7), 2)`. Recorrí sus 25 y 19 planos respectivamente. Añadí comprobaciones dirigidas en otras escenas; no presento estas últimas como una auditoría exhaustiva de todos sus raccords.

Los identificadores abreviados `Sx_Pyy` de este informe corresponden a `B1C01_Sx_Pyy`. Los párrafos se cuentan por bloques separados por línea en blanco, excluyendo el título. Hay **35 en ambos idiomas**. Los 122 IDs son únicos; las seis escenas de `guion_completo.json` coinciden, como objetos JSON, con los seis archivos individuales. Sus duraciones suman 930 segundos: 150 + 150 + 120 + 180 + 180 + 150.

Esta es una auditoría documental: `frame_final_descripcion` describe un resultado deseado, no un fotograma inspeccionado. No se han generado ni visto clips. La compatibilidad de los prompts se evalúa **contra la guía 14 entregada**, no como certificación de la interfaz actual de Flow. No se modifica ningún original ni se resuelve ninguna decisión del autor.

## A) Fidelidad al texto y segmentación

La división dramática es defendible: desierto y llamado; encuentro con Gabriel; recuerdo; negativa y despedida; guardián; Solmire. **La cobertura numérica no equivale a cobertura fiel de los acontecimientos.**

| Escena | Párrafos declarados ES/EN | Correspondencia real |
| --- | --- | --- |
| S1 | 1–9 | S1_P14–P19 ya adaptan el párrafo 10: tirón autoritario, detención, ojos cerrados y giro. |
| S2 | 10–17 | S2_P01–P02 vuelven a representar esa detención/giro. Hay duplicación del mismo beat, no dos llamados distintos en el texto. |
| S3 | 18–21 | El recuerdo corresponde principalmente a 18–20; 21 ya escucha la voz en el presente. S3_P16 ejecuta además el regreso del recuerdo del párrafo 22. |
| S4 | 22–27 | S4_P01–P02 recuperan material de 21. El gesto de 22 se altera: el texto afloja primero la mandíbula de Miguel y después Gabriel ablanda la mirada, alza y baja la mano; S4 coloca la mano en P05–P06 y la mandíbula en P07. |
| S5 | 28–32 | Cubre entrada y guardián; contiene repeticiones internas y anticipa indebidamente el silencio de la herida. |
| S6 | 33–35 | S6_P01–P04 vuelven sobre la marcha, la línea que no llega y la mirada del guardián del párrafo 32, ya resueltos en S5_P18–P25. |

**Omisiones y pérdida de significado:**

- **Párrafo 6:** la hipótesis del desierto como arma de un pueblo que destruyó su propia tierra, la doctrina frente al recuerdo y el cambio de incredulidad a reconocimiento no quedan comunicados por una conducta o narración suficiente. S1_P11 pide a un Miguel inmóvil «comprendiendo que un reino existió aquí antes de la Caída», pero su prompt prescribe quietud, viento y ningún diálogo. Eso no comunica al espectador la historia concreta de la autodestrucción.
- **Párrafo 8:** se pierde el portal imaginado para dejar pasar un ejército y su relación con una civilización que no contemplaba retirarse. S1_P09–P11 muestran el trazado y su escala, pero no esa idea. Puede aceptarse una condensación audiovisual, pero debe reconocerse como adaptación, no como cobertura íntegra del párrafo.
- **Párrafo 9:** S1_P12 conserva la frase del «latido cómplice» en `accion_principal`, pero exige ausencia de movimiento o correlato visual y solo viento en audio. El hecho queda escrito para el operador sin una traducción perceptible clara.

**Alteraciones relevantes:**

1. **Herida silenciada antes de tiempo, grave.** `S5.escena.estado_canon_entrada[0].heridas` afirma que está silenciada por la cercanía de la espada. S5_P01 y P10 lo repiten en `continuidad.heridas_visibles`. El párrafo 33 fija el desencadenante: **ver la espada**, no entrar en la arboleda ni acercarse a ella. La observación entre paréntesis de S5 sobre revelarlo después no corrige el cambio de causalidad. S6_P10–P11 sí sitúan el reconocimiento y el silencio en el momento pertinente.
2. **Gabriel adquiere armadura.** En S2_P04/P16, `continuidad` dice túnica azul y plata «sin armadura». S4_P01 introduce «peto delgado de plata pulida bajo la túnica», también en el prompt. La ficha de `personajes.md` especifica `no armor`; el capítulo contrapone su túnica a la pesadez del acero. El README visual de Gabriel contiene ese peto, pero avisa que su descripción es una versión anterior. Hay un conflicto de fuentes que debe resolverse; no autoriza a cambiar el vestuario entre dos mitades del mismo encuentro.
3. **Curación del ala más determinada que el texto.** S3_P10–P14 construyen un avance hasta ala «cicatrizada/cerrada» y reutilizan la coloración de daño antiguo. El capítulo dice cauterizar el ala rota durante tres noches, sin describir esa graduación ni una restauración completa. El propio agente deja pendiente el aspecto de cierre reciente. No llamaría a esto regeneración de una extremidad demostrada: el estado conserva daño distal. Sí es una concreción no validada que no debe convertirse en canon por repetición. Tampoco el capítulo afirma expresamente que el ala del presente esté intacta; S5_P01 la fija «sin daño». Debe establecerse el estado narrativo, sin confundir cierre de una herida con recuperación de plumas o anatomía.
4. **Efectos añadidos:** la vibración de la hoja en S6_P20 y el destello/chasquido de S6_P22 son decisiones de adaptación. El párrafo 34 sitúa el zumbido detrás de los ojos de Miguel; no dice que la hoja vibre. Pueden proponerse, pero no atribuirse al texto como hechos literales. La desaparición instantánea de la arboleda sí procede del párrafo 35.

La protección del misterio está mejor resuelta: el pergamino no se abre ni revela su contenido; Solmire no se entrega a Miguel antes del hallazgo. S6 mantiene el reconocimiento instintivo sin introducir en diálogo a Ereloth ni la explicación posterior de las armas. La nota de `grafo_conocimiento.md` sobre el pergamino respalda mantenerlo cerrado, aunque ese documento lo enumera entre hechos todavía no cubiertos por su seguimiento completo: no es una ficha exhaustiva del objeto.

Los 930 segundos son una suma correcta de duraciones propuestas. La afirmación de segmentación «sin necesidad de relleno artificial» no queda acreditada: hay beats repetidos y largos sostenidos de reacción. Por ejemplo, S4_P01–P08 consumen 64 segundos antes de «Vuelve a casa». El ritmo necesita una revisión editorial aparte.

## B) Segunda verificación de las cinco fronteras

### S1_P19 → S2_P01: rechazo editorial; diagnóstico físico del QA sobredimensionado

El QA acierta al señalar que S2_P01 dice «se detiene» en `accion_principal`, pero `continuidad.estado_entrada` ya lo da detenido; `vfx_principal` incluso afirma que no hay pisada. Debe fijarse el instante de corte y el frenado.

**No está demostrado el regreso espacial que afirma el QA.** S1_P19 se aleja en una nueva dirección, pero no establece una distancia ni una posición que obliguen a abandonar todo el camino. S1_P09 lo extiende hacia el horizonte. El capítulo, párrafo 25, vuelve a situar piedras bajo sus pies durante el diálogo. «Junto a los bloques» no prueba volver al mismo bloque descubierto. Falta geografía verificable: registrar anclas y rumbo; no inventar una teleportación.

Tampoco caminar → estar detenido exige siempre un plano puente: puede resolverse mediante corte y una transición breve definida. El problema confirmado de esta unión es sobre todo **la repetición del giro de párrafo 10** en S1_P15–P18 y S2_P02, que el QA no identifica. La ausencia de alas en la ficha inicial de S2 es un dato incompleto, no evidencia de pérdida física; en esto la salvedad del QA es correcta.

### S2_P19 → S3_P01: coherente como cambio temporal declarado

Confirmo el resultado. S3 anuncia pasado y Puertas de Ónice; P01 encuadra la fortaleza, mantiene a Miguel fuera de campo y sitúa a Gabriel aún sin llegar a su lado. Cambiar lugar, luz, lesión y presencia del pergamino es legítimo en este recuerdo. Que los personajes no salgan en el primer plano no prueba por sí solo continuidad; la justificación es el salto temporal explícito.

La aprobación de esta frontera no valida la anatomía o la curación de los planos posteriores de S3. Al salir del recuerdo hay que recuperar el estado del **presente de S2**, como exige el documento 18.

### S3_P16 → S4_P01, recuperando S2_P19: incoherente, pero por razones más sólidas que parte del QA

- **Pergamino: alerta válida.** S2_P19 lo deja visible contra el costado. S4_P01 lo declara bajo la tela «sin asomar», no simplemente fuera del encuadre. Una tela podría volver a cubrirlo, pero ese cambio no está registrado: `cambios_autorizados: []`. Hay un raccord por resolver, no pérdida del objeto. S3_P16, centrado en la cara, no puede servir de prueba de su desaparición.
- **Falso negativo de iluminación, importante.** `S2_P19.luz.fuente_luz` conserva sol cenital; S3_P16 promete recuperar la luz ya establecida en la escena marco. `S4_P01.luz` cambia a sol del atardecer, casi rasante del poniente, ámbar rojizo y sombras largas. Las tres noches transcurren en el pasado, no durante la conversación del presente. No hay elipsis del presente que autorice este cambio. El QA lo omite.
- **Falso negativo de vestuario, importante.** El peto de Gabriel de S4_P01 contradice el «sin armadura» de S2. Aunque quede bajo la túnica, el estado físico cambia sin causa. También debe rechazarse como conflicto de canon, no solo de montaje.
- **«Todavía suplicando» no prueba habla ininterrumpida.** S3_P16 lo describe expresamente como estado emocional; no asigna diálogo. El QA lo convierte en `acción (habla)` en curso y diagnostica una interrupción. Eso es un falso positivo interpretativo. Conviene aclarar expresión y audio, pero una mirada suplicante puede mantenerse en silencio.
- **Mirada perdida → mirada a Gabriel:** el regreso del recuerdo, expresado por S3_P16 y por el párrafo 22, justifica recuperar atención. No exige por sí solo otro plano. La fase exacta queda por fijar, pero no la elevaría a incoherencia física confirmada.

La incidencia `PENDIENTE` de S3_P16 es real y está bien conservada. No es, por sí misma, prueba de contradicción ni prueba histórica de que nadie revisara nada después: el QA del ensamblado constituye precisamente una revisión posterior, aunque no haya cerrado la dependencia.

### S4_P20 → S5_P01: aprobación automática incompleta; falso negativo sobre la herida

Confirmo continuidad de manos vacías, marcha, ausencia de Gabriel y armadura agrietada. La elipsis de «más días» autoriza el cambio de lugar y condiciones ambientales.

**No autoriza silenciar la herida.** S4 mantiene el hueco y acaba la marcha sin curación ni evento que lo calle; S5_P01 lo da ya silenciado incluso en su entrada, todavía en el desierto antes de pisar musgo. El desencadenante canónico está en S6, al ver Solmire. Es el inicio del mismo error que el QA solo detecta en S5→S6. Por ello **no apruebo esta frontera como plenamente coherente**.

Además, el QA afirma que las alas se mantienen consistentes, pero S4_P20 no las describe explícitamente en sus estados; S5_P01 sí fija dos alas sin daño. La primera afirmación sobre las alas excede la evidencia del extremo revisado. Deben heredarse desde un registro completo, no suponerse aprobadas por omisión.

### S5_P25 → S6_P01: contradicción de herida confirmada; movimiento menos concluyente

S5_P25 resume «herida y vestuario sin cambio» respecto a la cadena iniciada con el silencio prematuro. S6_P01 introduce vibración activa y la mantiene hasta el reconocimiento. Confirmo el fallo principal.

Matiz de precisión: el QA dice que `heridas_visibles` describe el silencio durante toda S5. No lo repite literalmente en todos los planos: P25 solo dice «oculto bajo el peto — sin efecto visible». El silencio se arrastra por el estado inicial y la ausencia de un cambio posterior. **No visible no significa silenciado.** La contradicción existe, pero debe citarse mediante esa herencia.

El supuesto reinicio del paso es una ambigüedad menor: S6_P01 escribe «iniciando la marcha», pero también muestra entrada por la izquierda y cámara siguiendo a su velocidad. Puede ser el inicio de su recorrido dentro del encuadre. Pediría continuidad de fase, sin afirmar una parada real no mostrada. La ocultación del guardián está correctamente conservada. El problema editorial adicional es repetir en S6_P01–P04 acciones del párrafo 32 ya cubiertas por S5.

**Balance:** solo S2→S3 queda aprobada sin esas reservas. S1→S2 necesita corregir el beat duplicado y definir el corte; S3→S4 tiene conflictos de luz, vestuario y visibilidad del pergamino; S4→S5 y S5→S6 están afectadas por el silencio prematuro. El resumen «3 incoherentes / 2 coherentes» resulta demasiado favorable en S4→S5 y demasiado categórico en algunas causas de S1→S2 y S3→S4.

## C) Continuidad dentro de las escenas muestreadas

### S2: recorrido completo P01–P19

| Planos | Manos, objetos, heridas y vestuario |
| --- | --- |
| P01 | Derecha de Miguel sube vacía al peto; izquierda vacía al muslo. Guantes y grietas definidos; hueco interno sin herida abierta. |
| P02–P03 | Conserva derecha en el pecho. P03 mantiene explícitamente la izquierda físicamente presente fuera de cuadro. |
| P04 | Gabriel aparece; ambas manos vacías, pergamino oculto contra el costado, no sujetado. Miguel conserva el contacto con el peto. |
| P05 | Miguel retira y baja la derecha al enderezarse; el cambio está registrado. |
| P06–P12 | Manos vacías de ambos, persistentes incluso en primeros planos. Pergamino oculto; Gabriel sin heridas ni armadura; peto de Miguel sin nueva fractura. |
| P13 | Cambio de postura/tela revela el pergamino sellado. Gabriel no lo toca; ambas manos siguen en los costados. |
| P14 | La derecha de Gabriel pasa a describirse «cerca del pergamino», dedos en el aire junto a la tela, sin contacto. No se registra desplazamiento. |
| P15–P19 | Conserva esa derecha cercana al pergamino; izquierda vacía. Miguel mantiene manos a los muslos. Pergamino visible e intacto, herida y ropa sin alteración declarada. |

**No encuentro una mano perdida y recuperada ni transferencia de objeto.** P13→P14 deja una ambigüedad de pose: «sin acercarse» frente a «cerca». Puede ser la misma mano al costado vista en detalle, puesto que allí está el pergamino; sin altura o ancla corporal no se puede confirmar un salto. Se debe precisar, no contabilizar como amputación o cambio de portador. La falta de seguimiento explícito de alas impide extender este resultado favorable a toda la anatomía.

### S5: recorrido completo P01–P25

| Planos | Manos, objetos, heridas y vestuario |
| --- | --- |
| P01 | Ambas manos de Miguel vacías y enguantadas; peto agrietado, alas plegadas. Error canónico inicial: hueco ya silenciado. |
| P02 | Manos fuera del detalle de botas, declaradas físicamente presentes. |
| P03 | Ambas reaparecen vacías con los mismos guantes; buena distinción entre recorte y ausencia. |
| P04–P07 | Manos persisten fuera de cuadro o a escala pequeña; no nace ningún objeto, daño o cambio de ropa. |
| P08–P09 | La hoja se rompe y los fragmentos permanecen registrados; manos de Miguel sin cambio. |
| P10–P11 | Guardián: manos vacías, primero poco resolubles por distancia y después visibles por aproximación. No es regeneración. Miguel se detiene y gira, sin adquirir objetos. |
| P12 | Cara del guardián; manos fuera de cuadro conservadas. |
| P13–P17 | Ambos mantienen manos vacías. Guardián sin prendas/armas; herida y vestuario de Miguel se heredan. |
| P18–P19 | Miguel retoma marcha; guardián gira sin desplazarse, con manos al costado. P19 completa el giro. |
| P20 | Las manos no cambian, pero el giro vuelve a empezar en curso y a completarse. Miguel sigue avanzando en el fondo. |
| P21–P22 | Miguel conserva manos y alas al verse desde atrás. Guardián queda oculto por troncos, físicamente presente en su sitio. |
| P23–P24 | Manos fuera de encuadre en cara/botas, conservadas vacías. Huellas del musgo persisten. |
| P25 | Manos parcialmente visibles por distancia, vacías; ropa y herida heredadas; guardián sigue oculto. |

**Tampoco hay pérdida/reaparición anatómica en estos datos. Sí hay fallos internos de tiempo y espacio:**

- **P01→P02:** P01 termina con Miguel ya cruzada la línea y sobre musgo; P02 entra con el pie derecho a punto de apoyar en arena y luego vuelve a cruzar. Falta definir un corte sobre el mismo paso o recortar el final de P01. Tal como están las salidas previstas, se repite el umbral.
- **P19→P20:** `P19.estado_salida_previsto` completa el giro; `P20.estado_entrada` vuelve al giro en curso de P18, mientras Miguel sí hereda su alejamiento posterior a P19. No es un simple insert simultáneo bien resuelto: mezcla fases temporales de dos personajes. El agente lo detecta en `checklist_incidencias`, pero el guion ensamblado conserva el problema. Además, P20 omite a Miguel de `personajes_en_plano` pese a mostrarlo desenfocado en `accion_fondo`.
- **P10→P11:** Miguel pasa de cuarenta pasos a «media distancia» al girar, sin avance registrado. Puede ser una expresión de composición, pero el estado la atribuye al personaje. La aproximación de cámara no reduce la distancia entre personajes. Hace falta un ancla espacial inequívoca.

### Hallazgo dirigido adicional: mano enguantada → piel en S6

S6_P01 fija cuero oscuro con protecciones doradas en la derecha. P15–P19 conservan el guantelete y no describen retirada ni dedos descubiertos. **S6_P22 exige contacto de piel con la empuñadura**, mientras declara `Vestuario: sin cambios` y mantiene visible el guantelete.

El capítulo también pasa de «mano enguantada» a «piel»: la adaptación debe resolver esa elipsis o concretar una cobertura compatible. No corresponde inventar aquí que el guante desaparece o que era sin dedos. Es un **conflicto de cobertura/contacto pendiente**, exactamente de la familia de fallos que se busca evitar, aunque no sea una amputación. Falta estado del guante retirado, si esa fuese la solución autorizada, y un evento de cambio que lo justifique. P22→P23 conserva adecuadamente el contacto ya iniciado, pero aún debe fijar el corte para que la desaparición no parezca ocurrir varios segundos después del contacto canónico instantáneo.

## D) Pewter Sentinel: contradicción real y bloqueo razonable

El README fecha el rediseño en **2026-09-16** y afirma que **sustituye** la estatua de metal sólido para producción futura. No dice que solo se aplique a apariciones posteriores dentro de la historia. «Hoy» en la segmentación es una referencia de su ejecución; no debe confundirse con la fecha de esta revisión.

En párrafo 30, el capítulo describe una figura del material pálido de la arboleda y rostro liso «sin un solo rasgo». El README prescribe cuerpo de niebla/vapor, parte inferior disuelta sin piernas separadas, flotación, ojos blancos y sugerencia de facciones. Hay una incompatibilidad material y facial real. Conviene precisar que el capítulo **no describe expresamente piernas, pies ni manos**: la segmentación exagera al atribuirle una anatomía completa explícita. La lectura sólida es muy fuerte y el README reconoce el diseño anterior, pero no toda la anatomía detallada de S5 procede literalmente del pasaje.

**S5 actúa razonablemente al bloquear:** `requiere_aprobacion_autor: true`, `motivo_aprobacion`, S5_P10/P11 en `checklist_incidencias` y `prompts_flow.ajustes` con «NO ENVIAR A GENERACIÓN». Prepara la alternativa sólida de forma provisional; no hay evidencia de que haya aprobado o generado una resolución por su cuenta.

**El paquete no queda utilizable solo por aprobar verbalmente esa alternativa.** S5_P10/P11 llaman a sus referencias «diseño literal sólido», pero `referencias_adjuntas` apunta a los archivos que el README identifica como el rediseño de niebla. Hay que preparar y asociar referencias compatibles si se elige sólido; si se elige niebla, revisar anatomía, cara, giro y física de todos los planos afectados. El «uso inmediato» anunciado en ajustes es prematuro.

## E) Usabilidad de los prompts de Flow

**No están listos como lote para copiar y pegar.** Su estructura suele incluir cámara, sujetos, acción, luz, audio y criterios de aceptación. Los cuatro bloques de entrega del documento 14 están representados por `ajustes`, `referencias_adjuntas`, `prompt` y `criterios_aceptacion`; no hace falta imitar literalmente sus rótulos. El problema es el contenido y la resolución operativa.

| Prompt leído completo | Qué está bien | Qué impide usarlo directamente |
| --- | --- | --- |
| **S2_P08** | Hombro izquierdo de Miguel, posiciones de pantalla y manos fuera de cuadro explícitos. Propone generar 8 s y recortar a 7. | Pega **la réplica ES y la EN dentro de la misma instrucción**. Hay que elegir idioma. Las 26 palabras ES en 7 s exigen aproximadamente 223 palabras/minuto, sin pausas: riesgo claro para la voz fraternal cansada. Además, exige terminar la frase antes del recorte sin aportar toma que lo compruebe. |
| **S4_P20** | Define recorrido de grúa, manos vacías, ausencia de Gabriel y persistencia de huellas. | Solicita cuatro imágenes, dos de Gabriel ausente; no respeta el presupuesto conservador de tres referencias de la guía. Pide 18 s con base de 8 + unos 10 de Extend, o dos clips, sin prompts separados ni estado de empalme. Dos bases de hasta 8 s tampoco cubren 18 s. La guía no establece un «rango de Extend documentado con garantías» que este ajuste invoca. Faltan decisión de operación, continuación desde una salida concreta y audio explícito. |
| **S6_P22** | Precisa derecha en contacto, izquierda presente fuera de campo y destello localizado. | `ajustes` combina **Ingredients to Video y 6 s**, cuando la tabla de la guía 14 reserva 8 s para Ingredients. Debe generar 8 y recortar, o seleccionar otro modo compatible. Persiste el conflicto guante/piel; la referencia corporal no sustituye una imagen aprobada del contacto y de la empuñadura. El prompt incluye «Vigilar sobreexposición», observación de revisión que conviene trasladar a criterios y expresar como resultado visible. |

Otros defectos comprobados:

- **Diálogo contaminado con narrador:** S4_P09 hace pronunciar «—Vuelve a casa —suplicó Gabriel ahora—…» e incluye también la versión EN con `Gabriel pleaded now`. Debe separarse la acotación de la réplica. S3_P14 reconstruye una pregunta desde estilo indirecto y lo advierte: propuesta legítima, pero no cita literal ya validada.
- **Referencias sin normalizar:** en S3 hay entradas de `referencias_adjuntas` que son rutas a README y rutas con comentarios añadidos entre paréntesis. Un README no es una imagen adjuntable; esas cadenas tampoco son rutas exactas. Los archivos base pueden existir sin que esas entradas constituyan un manifiesto operativo.
- **Presupuesto de referencias:** 42 de los 122 registros contienen más de tres entradas en `referencias_adjuntas` (11 de S3, 20 de S4, 11 de S5). Algunas entradas son instrucciones o documentos, no imágenes. Esto demuestra ausencia de selección final, no que Flow tenga necesariamente hoy un límite absoluto de tres. La guía exige seleccionar recursos, asignar funciones y comprobar su asociación real.
- **Imagen frente a texto contradictorio:** peto agrietado frente a referencia base sin grieta; bastón de Gabriel que los prompts piden ignorar; guardián sólido frente a referencia de niebla. Los documentos 14 y 17 dicen expresamente que no se confíe en que una frase venza al estado de la imagen. Hace falta un panel/estado aprobado compatible.
- **Dependencias textuales:** «ver P01», «sin cambio» o «mismo punto de siempre» no son estados completos para una generación independiente. En S5_P11/P15 y S3_P08 hay ejemplos claros. La información crítica debe expandirse en cada entrega; escribir un ID anterior no demuestra que Flow reciba ese plano.

Hay también instrucciones de cámara que necesitan depuración conforme al documento 16: S1_P19 se llama «plano fijo con leve retroceso», y S3_P16 usa `rack focus` para una transición temporal y espacial. El cambio de foco por sí solo no cambia de localización: debe decidirse si es montaje/disolución o transformación generativa. No son fallos anatómicos, pero aumentan la ambigüedad operativa.

## F) Valoración del diseño del pipeline y condiciones para continuar

**Mantendría las especialidades, pero corregiría la integración antes de otro piloto completo.** Hay aportaciones concretas: laterales anatómicos, estados de manos ocultas, ausencia de bastón, conservación de pergamino y fragmentos, causalidad de efectos, y advertencias de límites. El doble QA demuestra utilidad al encontrar errores distintos.

No obstante, el resultado revela una debilidad estructural de la entrega: **se concatenan diagnósticos y prompts sin convertir las incidencias en requisitos efectivos de revisión y bloqueo**. S5_P20 reconoce que completa dos veces un giro y sigue en la secuencia; S3_P16 no recibe el estado presente que necesita; S4 reinicia luz y vestuario; S5 propaga un estado inicial falso. Más agentes o más prosa no resuelven eso por sí solos. Los archivos no permiten afirmar cómo está implementado el orquestador; la observación se refiere al contrato que efectivamente entrega este piloto.

El incumplimiento del documento 18 es comprobable en **los 122 planos**: `estado_entrada` y `estado_salida_previsto` son cadenas, no el estado estructurado prescrito; faltan en `continuidad` `estado_salida_observado`, `frame_final`, `control_calidad`, `enlace` y versionado de plano/herencia. No se exige vídeo ya producido en un borrador: la guía pide que las observaciones existan como **`null`** y que impidan aprobar dependencias. Una descripción prevista no sustituye esos campos.

Antes de continuar:

1. **Consolidar un estado narrativo común por escena y tiempo.** Separar presente/recuerdo; fijar herida, alas, guantes, ropa, pergamino, luz y geografía. Cada cambio debe remitir a un acontecimiento del capítulo o a una decisión de adaptación identificada.
2. **Corregir cobertura y cortes.** Eliminar duplicaciones de párrafos 10 y 32, resolver umbral y giro repetidos, conservar el orden causal de la reacción fraternal y revisar el ritmo sin forzar duración mediante sostenidos redundantes.
3. **Reconciliar las salidas de los especialistas antes de traducir.** Comprobar que `accion_principal`, `encuadre`, `luz`, `vfx`, `continuidad`, prompt y storyboard describen el mismo plano. Si cambia uno, revisar sus dependientes. Los errores de canon tienen prioridad sobre el deseo de heredar un estado erróneo.
4. **QA interno y entre escenas con tres resultados:** coherente, incoherente, pendiente por falta de datos. Recuperar el estado del presente a través del flashback; una elipsis no exime de conservar heridas u objetos sin causa de cambio. Distinguir recorte de ausencia y expresión suplicante de habla real.
5. **Preparar paquetes operativos por generación.** Un idioma y réplica limpia; modo/duración definidos; referencias de imagen seleccionadas y compatibles; prompts separados para base y continuación; versiones, corte retenido y criterios verificables. Las incidencias bloqueantes deben impedir enviar el plano y sus dependientes afectados.
6. **Hacer una prueba visual corta antes de producir los 930 s.** Ensayar general → mano fuera de cuadro → general; después un contacto con objeto y una unión entre escenas. Revisar inicio, desarrollo y final, registrar rechazos y medir conservación de estados. El caso presente no contiene una amputación de mano: no acredita que el sistema ya resuelva ese caso. Si se prueba una ausencia anatómica, usar un ensayo técnico separado del canon.

**Conclusión de aprobación:** aprobado como material para corregir y ensayar el método; rechazado como guion listo para producción. El enfoque de especialistas más revisión independiente merece continuar, pero necesita una fuente común de estados, una fase de resolución de incidencias y validación de clips. Este piloto demuestra capacidad de describir y detectar algunos fallos; todavía no demuestra capacidad de impedirlos.
