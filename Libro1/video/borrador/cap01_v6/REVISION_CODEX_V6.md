# Sexta revisión independiente — Las Crónicas del Juicio, capítulo 1

Fecha: 2026-09-25. Revisor: Codex. Auditoría documental y pruebas locales de funciones JavaScript; no se generaron ni visionaron clips. Único archivo escrito por esta revisión: este informe.

**Veredicto: no apruebo v6 como paquete completo listo para pasar a Flow.** Los seis defectos narrativos principales señalados en S4/S5/S8 están corregidos en sus eventos previstos, pero quedan errores reales: iluminación contradictoria entre campos, prompts de S2 todavía soleados, sombras persistentes en S7, postura incompatible en S1→S2, un nuevo salto de marcha en S5, cambio de idioma hablado en S5 y zumbido de S8 desplazado al contacto. El comodín del validador introduce además un falso negativo reproducible. El 3,6 % no mide estos problemas.

Las correcciones necesarias son localizadas. Después de reconciliar los datos y derivados afectados sí tendría sentido ensayar clips concretos, especialmente la retirada del guante y el contacto simultáneo con la disolución. Un ensayo técnico aislado no equivaldría a aprobar el capítulo ni su continuidad global.

**Alcance y nomenclatura.** Contrasté los capítulos ES/EN, los ocho JSON individuales, el ensamblado, RESUMEN, la revisión v5, las funciones indicadas del script temporal y los documentos 14/18. Recorrí las acciones de los 165 planos; en S4, los estados de ambas alas; en S5, manos, bastón y lágrima; en S8, mirada, herida, guantes y contacto. Revisé las siete fronteras con contexto interior, incluidos todos los esquemas de luz de S7. Leí cinco registros Flow completos como muestra principal: S2 P02, S4 P07, S5 P04, S5 P17 y S8 P20; amplié a los prompts de los problemas encontrados. No certifico la interfaz actual de Flow: aquí compruebo la entrega contra las reglas locales, sin convertir la documentación histórica en una prueba nueva del producto.

`S5 P19` abrevia `B1C01_S5_P19`. S1 y S8 guardan IDs cortos; otras escenas emplean IDs completos. `estado_entrada`, `estado_salida_previsto`, `enlace` y `cambios_autorizados` se encuentran bajo `planos[].continuidad`; los prompts están en `prompts_flow[]`.

**Inventario comprobado.**

| Escena | Planos | Bloqueados | Registros Flow | Duración |
| --- | ---: | ---: | ---: | ---: |
| S1 | 20 | 2 | 18 | 151 s |
| S2 | 10 | 2 | 8 | 140 s |
| S3 | 31 | 0 | 31 | 210 s |
| S4 | 18 | 0 | 18 | 140 s |
| S5 | 27 | 2 | 25 | 197 s |
| S6 | 15 | 0 | 15 | 120 s |
| S7 | 21 | 0 | 18 | 149 s |
| S8 | 23 | 0 | 23 | 170 s |
| Total | 165 | 6 | 156 | 1277 s |

Los ocho objetos de escena coinciden exactamente con `guion_completo.escenas`. Hay cuatro `CONTRADICCION_CONTINUIDAD`, dos `REFERENCIA_PENDIENTE` y **cero discrepancias entre los 165 flags internos y externos**. La segmentación conserva los rangos 1–4, 5–9, 10–17, 18–20, 21–27, 28–29, 30–32 y 33–35.

**159 planos listos no son 156 prompts:** S7 P06, P08 y P13 están desbloqueados, pero siguen sin registro Flow. No son tres bloqueos adicionales; falta regenerar su traducción tras la revalidación. `qa_inter_escenas` sigue siendo `null`. RESUMEN anticipa que esta entrega «pasa una auditoría externa sin encontrar bugs de contenido reales» mientras declara la revisión pendiente: esa afirmación no era evidencia y este informe la contradice. La cifra histórica de v4=50 tampoco resuelve la discrepancia de procedencia ya documentada en v5. La duración sigue siendo 21 min 17 s, fuera del objetivo de 8–15 min.

**A. Lateralidad del ala de Miguel: corregida.**

Recorridos los 18 planos y sus 36 estados. P01–P06 mantienen la quemadura/rotura del último tercio del **ala izquierda**; P07 inicia la curación por contacto de la izquierda de Gabriel; P09 aclara el borde a gris; P11–P12 avanzan la recuperación; P13 termina con la izquierda íntegramente blanco perla. P14–P16 conservan ese resultado, P17 la repliega y P18 mantiene ambas sanas. La eliminación de la entrada de herida desde la salida de P13 corresponde a la curación narrada, no a una omisión sin causa.

`extremidades[parte=ala_derecha].posicion` mantiene la derecha intacta en todos los estados. Los 18 prompts no invierten el daño: cuando identifican el ala tratada, corresponde a la izquierda; los encuadres que no la muestran no siempre repiten su lado. Por tanto, **coherencia semántica sí; presencia literal de «ala izquierda» en cada prompt, no**. P13/P17/P18 explicitan el resultado sano. También se corrigió la acotación del narrador convertida en diálogo: S4 P08 dice únicamente «El silencio es lo que deja a una herida decidir que es mortal».

**B. Silenciamiento de la herida: corregido en P09.**

Recorridos los 23 planos. P01–P04 muestran el claro y la espada a cámara sin Miguel visible. P05–P06 orientan el avance hacia el fresno; P07 especifica que aún no fija directamente la espada; P08 encuadra los pasos. No hay una afirmación anterior equivalente a la observación directa de v5.

S8 P09 `accion_principal`, `direccion_mirada`, transición de `heridas[].estado` y prompt hacen coincidir primera fijación consciente y silencio. Entrada: «activo al entrar en el plano»; salida: «silenciado por completo en este instante». **P10–P23 conservan explícitamente el estado silenciado en entrada y salida**, sin retorno a «activo» o «sin silenciar». No hay curación física afirmativa del hueco en ese recorrido.

La puesta en escena deberá hacer legible que mirar hacia el fresno antes no equivale a haber reconocido la espada; el texto de v6 ahora permite hacerlo. Esto es una condición de comprobación del clip, no el retraso afirmativo que fallaba en v5.

**C. Bastón y lágrima de Gabriel: corregidos, con entrega Flow incompleta en la desaparición.**

En S5 P01–P18 y entrada de P19, `objetos_en_mano.mano_derecha` conserva `baston_vox_aeternum`; la izquierda queda libre para el gesto de P06. `objetos_escena` mantiene portador Gabriel y ubicación en su derecha, incluso fuera de encuadre. P19 autoriza expresamente que el bastón se marche con Gabriel; desde su salida no queda un bastón abandonado ni «sin resolver». P20–P27 no lo devuelven.

`objetos_escena[id_objeto=lagrima_de_luz]` nace en la salida de P17; P18 y entrada de P19 conservan su recorrido ya completado, visible y sin disolverse ni secarse. Desaparece con Gabriel en P19. P20 no la restaura. Los prompts P17/P18 sostienen la misma evolución. **P19/P20 carecen de prompt por sus bloqueos**: apruebo aquí el evento de guion y contrato, no una traducción de esos planos que aún no existe.

Nuevo error independiente: **S5 P15→P16 adelanta la marcha**. P15 salida, `miguel.posicion_escena`: «solo ha pivotado sobre sí mismo, no ha caminado (eso empieza en P25)». P16 entrada, `pose_corporal`: «se aleja caminando … tras el giro de P15». P16–P20 lo mantienen alejándose. P21 incluso añade una detención y vuelta en el corte; P25 vuelve a iniciar la marcha. El cambio contradice el estado explícito anterior y añade una salida/retorno innecesarios antes de la despedida. Mantenerlo inmóvil hasta P25 o declarar y reconciliar otra adaptación completa. El arreglo del bastón no corrige este nuevo raccord.

**D. Guante, contacto y disolución: corregidos conforme a la nueva pauta de adaptación.**

S8 P15–P17 conservan ambos guantes y niegan contacto. **P18 muestra la retirada completa del guante derecho con la mano izquierda**; salida: derecha desnuda, izquierda aún enguantada y sujetando `guante_derecho_miguel`. P19–P23 conservan ese inventario. No queda un guante con destino desconocido. La derecha no necesita registrar la espada como objeto portado por el mero roce: no hay extracción narrada.

P19 aproxima sin tocar. **P20 introduce simultáneamente contacto de piel e inicio de pérdida de definición de raíces/estanque**, en acción, VFX, estados y prompt. P21 continúa y P22 completa la disolución; P23 sostiene el espacio resultante. No encontré una disolución afirmada antes de P20 ni un plano posterior que retrase su inicio.

Esto satisface `notaEscenaSolmire()` y la pauta expresamente comunicada para v6. No equivale a desaparición completa literalmente instantánea: P20–P22 duran 8 s cada uno, y P23 añade otros 8 s. La desaparición progresiva es una adaptación explícita ahora, no el bug anterior de respuesta sin disparador. Conviene conservar esa distinción al valorar fidelidad y ritmo.

**E. Siete fronteras de luz y atmósfera: corrección parcial, no siete aprobadas.**

| Frontera | Evidencia y dictamen |
| --- | --- |
| **S1→S2** | `luz` de los diez planos de S2 sí mantiene cielo cubierto. Pero P01 `estado_entrada.entorno` aún dice «Sol alto de media mañana, cielo despejado» y «sombras cortas y definidas»; salida también conserva sol y cielo despejado. Los prompts P01–P03 piden expresamente ese sol duro. **No corregida en la entrega completa.** Además S1 P18 se incorpora, P20 está de pie; S2 P01 ya está arrodillado con dedos apoyados, con enlace «Sin elipsis». Persiste el salto de postura señalado en v5. |
| **S2→S3** | Los campos `luz` son ahora compatibles. S2 P10 `estado_salida_previsto.entorno.luz`, sin embargo, conserva «Mismo sol, contraluz parcial» y sombra oblicua de Miguel y sus alas. S3 recupera cielo azufrado sin sol. **No corregida entre todas las representaciones.** Marcha→detención es plausible por el párrafo 10, pero el arranque inmóvil de S3 aún requiere precisar el corte. |
| **S3→S4** | Flashback identificado; noche, fuego, humo y fortaleza tienen causa narrativa. La lateralidad ya es correcta. **Compatible.** |
| **S4→S5** | El regreso debe recuperar S3. Los 27 campos `luz` y los 25 prompts disponibles de S5 ya recuperan cielo azufrado sin sol. **Los contratos no:** P01 entrada dice «Sol de mediodía», «luz dura», «Cielo despejado»; salida lo conserva. P05 conserva «dureza fuerte»; P18/P19 aún describen sombra solar en la mejilla; P27 sigue heredando el sol. **Corrección del texto de generación, pero contrato contradictorio.** |
| **S5→S6** | El párrafo 28 autoriza días de marcha y luego arena→musgo. Esa elipsis permite que el desierto soleado de S6 P01/P02 difiera del cielo cubierto de S5. Pero S6 P01 `enlace.tiempo_transcurrido` dice «Sin elipsis; abre la escena». **Transición justificable por el capítulo, enlace erróneo pendiente de corregir.** El bastón ya no queda pendiente. |
| **S6→S7** | S6 establece musgo, aire limpio sin partículas y luz sin sombras ni dirección. S7 P01 reinicia suelo polvoriento, polvo a cada paso y bruma baja dominante; no declara traslado a otro suelo ni cambio ambiental. **Sigue sin reconciliarse.** Las sombras tampoco se resolvieron en todos los campos y planos; detalle debajo. |
| **S7→S8** | S7 P13/P21 anticipan el centro cálido; S8 presenta fresno/estanque luminoso. El paso a otro claro y la permanencia del Sentinel atrás son compatibles. S8 impide añadir niebla; puede corresponder al claro, pero conviene fijar el límite con la bruma de S7. **No encuentro aquí un salto duro equivalente a S1/S2; compatible como cambio local de espacio.** |

La comprobación de S7 no se limita a P19/P20:

- **P19:** el campo superior `luz` ahora niega franjas y sombras. `continuidad.estado_salida_previsto.entorno.luz` aún ordena «recortada por los propios troncos, franjas alternas de luz y sombra más marcadas». El contrato contradice directamente el parche. Su prompt usa oclusión geométrica, no afirma esas sombras, pero tampoco incorpora la nueva prohibición explícita.
- **P20:** el campo `luz` diferencia correctamente ocultación y sombra; el prompt mantiene resplandor difuso entre troncos. No lo cuento como otra sombra afirmada por el prompt.
- **P12:** `luz.direccion`, `luz.dureza`, el entorno del contrato y el prompt introducen sombras más marcadas bajo cejas/nariz y menos relleno para expresar incertidumbre. S6 P06 había establecido explícitamente que ni pómulos ni cuencas generan sombra propia. **Persiste una contradicción independiente de los troncos.** La emoción del personaje no justifica que la fuente cambie.
- **P07:** endurece la luz para marcar metal frente a vapor. **P16:** su dirección lateral «cambiando con el travelling» tampoco fija una fuente espacial estable. Son decisiones que requieren reconciliación con la regla uniforme; no equiparo por sí solo un reflejo metálico a una sombra proyectada.
- Los ojos propios del Sentinel y su vapor en P04/P05/P18 sí pueden justificar efectos locales. No justifican convertir todo el suelo de musgo en polvo ni introducir bruma ambiental general sin transición. P14/P17/P19/P21 ya la describen como ambiental, no solo corporal.

**F. Los seis bloqueos restantes: motivos completos y decisión individual.**

| Plano | Motivo real registrado | Dictamen |
| --- | --- | --- |
| **S1 P08** | Desaparecen «guante izquierdo» **y «sabatón izquierdo»** de las listas. | El macro conserva solo peto y guante derecho; omisión de inventario oculto, no retirada física. Corregir/heredar el inventario y desbloquear por este motivo. |
| **S1 P09** | Aparecen «guante izquierdo», **«faldones» y «sabatón izquierdo»**. | Reencuadre y recuperación de detalle; no hay puesta de prendas. Mismo falso positivo físico. Normalizar la herencia antes de liberar. |
| **S2 P05** | Aparecen «guantes» **y «grebas y escarpes sabatones»**. | Entrada agrupa «resto de la armadura y faldones» y cuerpo oculto; salida detalla piezas puestas. Granularidad, sin desaparición/reaparición física demostrada. El plano sí necesita corrección de su entorno solar por otro motivo. |
| **S2 P06** | Dependencia de P05, enlace `continuacion`. | No hay contradicción propia de esos objetos. Reevaluar tras resolver P05; también reconciliar el clima despejado de su contrato. |
| **S5 P19** | Desaparecen «hombreras de tela» **y «sandalias»**. | **Falso positivo por salida autorizada de Gabriel completo**, no meramente prendas fuera de encuadre. Entrada contiene ambas; salida no contiene a Gabriel. `cambios_autorizados` narra su desaparición con pertenencias. El detector no comprende esa cobertura. Liberable por utilería tras resolver el contrato solar y generar su prompt. |
| **S5 P20** | Dependencia de P19, enlace `continuacion`. | No reaparece Gabriel ni la lágrima ni el bastón. Cascada mecánica de la raíz anterior; falta además traducirlo y reconciliar su «Sol cenital». |

RESUMEN omite calzado/faldones en los motivos y caracteriza mal P19. Mover hombreras de visible a oculto no resolvería esa comparación: el detector combina ambas listas, y el personaje sale de la localización. Como medidas provisionales de revisión, los flags pueden permanecer pendientes; **no los avalo como seis contradicciones físicas genuinamente ambiguas**. La política declarada en `IDENTITY_NOTES` ordena heredar omisiones secundarias sin bloquear. Tampoco propongo liberarlos ciegamente mientras contienen otros errores.

**G. Validador: pruebas ejecutadas, fixes parciales y falso negativo nuevo.**

Ejecuté Node con `fs.readFileSync` y `vm.runInContext`, extrayendo `normalizarTexto()` y el bloque desde `RASGOS_PERMANENTES_EXCLUIDOS` hasta antes de `// NUEVO 2026-09-22`. No importé ni ejecuté el workflow, no llamé al LLM y no escribí fixtures. Ruta auditada: `/tmp/claude-1000/-home-sszark-Escritorio-proyectos-novelas--claude-worktrees-cinematographic-skill-c4d6b6/8f911d88-29ac-45f3-8cce-d5bee1c755cd/scratchpad/workflow_cinematografia.js`.

| Llamada / caso | Resultado observado | Evaluación |
| --- | --- | --- |
| `esRasgoPermanente('rostro')` | `true` | Correcto. |
| `esRasgoPermanente('peto frontal y rostro')` | `false` | Fix concreto confirmado. |
| `esRasgoPermanente('guante y rostro')` | `false` | Correcto. |
| `esRasgoPermanente('armadura/peto y rostro')` | `true` | **Falso negativo de rastreo:** el filtro todavía separa solo por espacio; pierde ambos objetos antes de llegar a la tokenización corregida. |
| `esRasgoPermanente('espada y rostro')` / `('anillo y piel')` | `true` / `true` | Objetos reales fuera de su lista cerrada quedan descartados junto al rasgo anatómico. |
| `palabrasSignificativas('armadura/peto torso')` | `['armadura','peto','torso']` | Separación por `/` confirmada en esta función. |
| `coincideAlgunaClave('armadura/peto',['peto'])` | `true` | Correcto para el caso pedido. |
| `coincideAlgunaClave('guante izquierdo',['guante derecho'])` | `false` | Fix de lados opuestos confirmado. |
| `coincideAlgunaClave('guante izquierdo',['sabaton izquierdo'])` | `true` | **Falso negativo:** compartir «izquierdo» basta para confundir objetos distintos. |
| `coincideAlgunaClave('espada_solmire',['conjunto completo'])` | `true` | El comodín cubre indebidamente un arma, no solo vestuario oculto. |
| `coincideAlgunaClave('conjunto completo',['baston_vox_aeternum'])` | `true` | La simetría permite que un solo bastón represente todo el conjunto. |

Probé además `detectarCambiosSinCausa()` con estados sintéticos del mismo personaje y `cambiosAutorizados=[]`:

```js
const estado = (mano, piezas = []) => ({ personajes: [{
  id_personaje: 'miguel',
  objetos_en_mano: { mano_derecha: mano, mano_izquierda: [] },
  vestuario_visible: piezas.map(pieza => ({ pieza })),
  vestuario_oculto: [], heridas: []
}] });
```

- Entrada `estado([])` → salida `estado(['espada_solmire'])`, dirección `reaparicion`: una alerta con **«aparece»**. El caso inverso, dirección `desaparicion`: una alerta con **«desaparece»**. Direcciones corregidas.
- Entrada `estado([], ['conjunto completo'])` → salida `estado(['espada_solmire'], ['conjunto completo'])`, dirección `reaparicion`, campo `objetos`: **`[]`, ninguna alerta**. La derecha estaba vacía y adquiere espada sin causa. Esto responde directamente a la pregunta del comodín: **sí, oculta una aparición real**.

El comodín de la línea 671 no recibe visibilidad, categoría ni presencia física; se aplica tanto a prendas como a objetos de mano y antes de verificar lados. Debe restringirse a herencia de vestuario previamente conocido y oculto; nunca convertirlo en autorización para adquirir utilería. La lateralidad debe ser un atributo de la identidad, no una palabra suficiente para hacer coincidir dos piezas.

`stageContinuidad()` sí sincroniza flag y tipo tras el override y tras la cascada. Su resultado coincide en los datos entregados. `notaAlasMiguel()` fija izquierda y derecha intacta; `notaEscenaSolmire()` fija correctamente los tres disparadores pedidos. La regla de objetos soltados exige destino antes de terminar la escena: es una instrucción al LLM, **no una comprobación determinista de inventario de escena**.

Persisten otras limitaciones de v5: `extraerClaves()` no rastrea `objetos_escena`; fusiona las dos manos al comparar claves; `detectarRupturasEntrePlanos()` sigue sin invocarse. El comentario que afirma que entrada→salida de B detecta una herencia incorrecta de A sigue siendo falso. El nuevo P15→P16 de S5 ilustra otra vez la necesidad de comparar hechos entre planos.

También repetí los dos casos de curación `sin dolor. La herida está cerrada` y `sin dolor, pero la herida está curada`, con Miguel y zona esternón: ambos devuelven cero alertas. El defecto de alcance de negación de v5 persiste. Estos son contraejemplos de código, no curaciones encontradas en los clips ni prueba de que tales frases estén en v6.

**H. Flow: referencias existentes, pero formato y contenido aún fallan.**

La muestra principal completa da este resultado:

| Prompt | Idioma / referencias | Resultado |
| --- | --- | --- |
| S2 P02 | ES / una referencia corporal existente | Negativas claras, sin IDs de guion; **ordena sol de media mañana y luz dura**, contradiciendo el nuevo campo `luz`. |
| S4 P07 | ES / dos referencias corporales existentes | Contacto de izquierda de Gabriel con ala izquierda de Miguel; bastón derecho conservado. Sin ID de plano ni rótulo organizativo en el texto. |
| S5 P04 | EN / una referencia corporal existente | Cielo azufrado sin sol y negativas en la prosa. No mezcla idiomas dentro del prompt. La frase sobre nada visible u oculto bajo la túnica convendría limitarla a visibilidad, pues el pergamino sí existe oculto. |
| S5 P17 | EN / una referencia facial existente | Lágrima única, mejilla seca al empezar, persistencia al terminar; luz difusa sin sol. Sin IDs ni etiquetas. |
| S8 P20 | ES / sin adjuntos, Extend de P19 | La falta de imagen adjunta es coherente con extender un clip. Contacto/disolución simultáneos bien traducidos; **incluye el rótulo «Sonido ambiente:» y desplaza el zumbido**. |

Comprobé la existencia en disco de **todas las rutas de `referencias_adjuntas` de los 156 registros**: ninguna falta. Esto no certifica composición ni estado visual correcto; las imágenes de identidad y los frames/ clips aprobados siguen siendo cosas distintas. Para S4 P07, por ejemplo, la referencia corporal celestial no acredita por sí sola una imagen de inicio con el ala dañada y la mano colocada.

Los 25 prompts de S5 son **EN**; todos los demás registros son **ES**. La luz de S5 ya coincide con el cielo cubierto; no encontré restos afirmativos de sol duro en sus prompts. Sin embargo, S5 P07 ordena «Gabriel says in English» y P18 vuelve a ordenar diálogo en inglés, mientras S3/S4 hablan español. Cada prompt es monolingüe, pero **el episodio cambia de idioma sin motivación ni una entrega bilingüe separada**. Para una salida ES, regenerar esas réplicas y sus instrucciones; para EN, entregar también el resto en EN. No confundir `idioma` por registro con continuidad lingüística del capítulo.

La búsqueda de IDs tipo `P18` dentro de los 156 textos finales no devolvió coincidencias: el defecto específico de ID de v5 está corregido. En cambio **S8 conserva «Sonido ambiente:»** como rótulo repetido; es la misma clase de etiqueta organizativa que el documento 14 exige retirar. Integrar el sonido en una frase natural. «Plano detalle» como descripción de cámara no es por sí mismo una etiqueta prohibida.

**Nuevo desplazamiento del zumbido:** el párrafo 34 ES/EN sitúa su crecimiento antes del contacto, detrás de los ojos. Los prompts S8 P15–P19 piden silencio; P20 dice «un zumbido grave y sostenido que nace en el instante del contacto; silencio previo». Se ha creado otro disparador falso. Introducir el zumbido subjetivo antes del contacto y mantenerlo según el arco narrativo; no confundirlo con reactivación del hueco silenciado.

También sigue pendiente separar duración retenida de duración generada: S5 P06 pide Ingredients de 7 s y P17 de 6 s sin explicar generación/recorte, frente a la pauta del documento 14 para esa operación. Es una inconsistencia con la guía local; no una nueva comprobación de los controles disponibles hoy. S8 P20 necesita un clip P19 real aprobado antes de ejecutar Extend; el registro actual solo lo planifica.

**I. Cierre de los hallazgos de v5 y condiciones para el piloto.**

Quedan **corregidos** el lado del ala, bastón, reinicio de lágrima, momento del silencio, retirada de guante, comienzo de disolución, verbos invertidos, flags internos/externos, ID de plano en prompt y acotación audible del diálogo de S4. La tokenización y el filtro anatómico mejoran ejemplos concretos, pero no son arreglos completos. La reducción de cascada se conserva.

Quedan **pendientes** la postura S1→S2, la coherencia ambiental completa, la elipsis de días S5→S6, el QA selectivo entre planos, los límites de negación y equivalencia de objetos, la normalización de inventario, los ajustes de generación y la duración objetivo. Hay **nuevos errores o regresiones** en marcha de S5, idioma hablado de S5, zumbido de S8, comodín demasiado amplio y traducción ausente de tres planos desbloqueados.

Antes de pasar esta versión como paquete a Flow:

1. Reconciliar `luz`, estados de entorno, frames previstos y prompts en S2/S5/S7; resolver musgo/polvo/bruma y las sombras de P12, no solo P19/P20. Regenerar derivados afectados, no todo el capítulo por defecto.
2. Corregir postura S1→S2 y marcha S5 P15→P16; declarar los días de elipsis de S6. Mantener intactos los disparadores corregidos de S8 y adelantar únicamente el zumbido a su lugar narrativo.
3. Entregar un idioma hablado consistente, retirar rótulos y completar los cinco prompts faltantes de S5/S7 después de resolver sus estados. Los cuatro faltantes de S1/S2 completarán los nueve ausentes totales.
4. Resolver manualmente los seis motivos de bloqueo con inventario y salida de personaje explícitos; restringir el comodín y comprobar identidad/lado sin coincidencia por adjetivo. No perseguir una tasa cero de bloqueos a costa de ocultar objetos nuevos.
5. Seleccionar entonces los clips de prueba, preparar sus composiciones y registrar operación/duración real. Revisar inicio, interior, final y empalmes observados conforme al documento 18.

**No confirmo «cero problemas reales pendientes».** Confirmo una mejora concreta en los seis eventos prioritarios y una entrega todavía inconsistente entre sus propias representaciones. El siguiente paso útil es cerrar esas contradicciones localizadas; la validación audiovisual vendrá después y no puede sustituirlas.
