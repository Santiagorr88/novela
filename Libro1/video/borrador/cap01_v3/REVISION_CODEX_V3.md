# Tercera revisión independiente — Las Crónicas del Juicio, capítulo 1

Fecha: 2026-09-20. Revisor: Codex. Auditoría documental de planificación; no se han generado ni visionado clips. Único archivo escrito: este informe.

**Veredicto: mejora real y considerable respecto a v2, pero todavía no aprobado para producción ni para extender el pipeline sin correcciones a más capítulos.** Se recuperan los 123 contratos de continuidad y el contenido de Solmire. No obstante, hay falsos negativos graves: guante que desaparece y reaparece, peto que pierde sus grietas, bastón recuperado sin acción y reinicios de iluminación entre escenas. El 10,6 % de bloqueos mide decisiones del sistema, no la tasa real de defectos.

**Alcance y método.** Contrasté los capítulos ES/EN —35 párrafos narrativos cada uno—, las acciones de los 123 planos, sus estados y diagnósticos, las seis escenas y el ensamblado, el script temporal indicado, los documentos 18 y 14, los informes v1/v2 y S6 de v2. Recorrí íntegramente S4 y S6 para manos, objetos, heridas y vestuario, con comprobaciones adicionales en S1/S2/S3/S5. Revisé prompts completos, incluidos los dos añadidos de S6. Las comprobaciones de Flow se hacen contra las reglas locales y las pruebas del autor solicitadas, no como certificación actual de la interfaz del proveedor.

En las citas siguientes, `S6_P14` abrevia `B1C01_S6_P14`; los campos de estado se encuentran bajo `planos[].continuidad`. La igualdad de estados se evalúa semánticamente para hechos persistentes y por separado como igualdad literal de JSON: un cambio de encuadre puede cambiar visibilidad, pero no reparar un guante ni trasladar un objeto.

**Inventario verificado**

| Escena | Planos | Continuidad estructurada | Bloqueados | Registros Flow |
| --- | ---: | ---: | ---: | ---: |
| S1 | 20 | 20 | 0 | 20 |
| S2 | 20 | 20 | 4 | 16 |
| S3 | 15 | 15 | 4 | 12 |
| S4 | 24 | 24 | 4 | 20 |
| S5 | 24 | 24 | 1 | 23 |
| S6 | 20 | 20 | 0 | 20 |
| Total | 123 | 123 | 13 | 111 |

Los 123 IDs de plano son únicos. Las seis escenas individuales coinciden como objetos JSON con `guion_completo.escenas`, incluida la corrección de S6. La duración suma 930 s y coincide con el ensamblado. Los rangos 1–9 / 10–17 / 18–21 / 22–27 / 28–32 / 33–35 cubren el capítulo sin huecos ni solapamientos de segmentación.

Hay 110 planos marcados listos y 111 registros Flow porque S3_P14 tiene variantes ES y EN explícitamente identificadas como alternativas. No es un plano extra ni un error de mezcla de idiomas; conviene que la clave del paquete sea `(id_plano, idioma)` y que el exportador seleccione la pista. No hay prompts para los 13 IDs bloqueados ni IDs listos sin algún prompt.

**A. S6: el bug de sustitución por Ónice sí está corregido**

En v2, sus veinte acciones representaban reconocimiento de Gabriel, fortaleza, cauterización y regreso al desierto. En v3, el reparto real es:

| Planos | Correspondencia con la fuente |
| --- | --- |
| P01–P04 | Corazón de la arboleda, fresno negro, raíces y estanque: párrafo 33. |
| P05–P06 | Espada clavada, luz viva con contorno y peso: párrafo 33. |
| P07–P08 | Silencio del hueco al verla y reconocimiento de Solmire: párrafo 33. |
| P09–P15 | Detención, mano temblorosa, duda de identidad y zumbido: párrafo 34. |
| P16 | Contacto piel–empuñadura: párrafo 35. |
| P17–P20 | Onda, disolución y cierre en vacío luminoso: desarrollo añadido del desenlace. |

**No hay mezcla narrativa del flashback.** Las menciones negativas a quemaduras o curación no constituyen escenas de Ónice. El personaje actuante es Miguel; Gabriel no reaparece como sujeto del hallazgo.

Esto no equivale a fidelidad perfecta. P14 añade una respuesta luminosa a la proximidad que no está en el pasaje. Más relevante: P16 termina con el contacto; P17 dedica otro plano a una onda por la espada; P18 entra con fresno y estanque todavía íntegros y comienza la disolución; P19 la completa. El texto ES y EN hace desaparecer la arboleda **en el instante del contacto**. Los enlaces no declaran repetición del mismo instante ni dilatación subjetiva: presentan sucesión continua. Debe unificarse el disparador con el comienzo de la desaparición o documentarse y aprobarse esa adaptación temporal. El vacío luminoso y el sostenido final también son decisiones de adaptación, no contenido literal demostrado por el párrafo 35.

**B. Pérdida de datos: corregida en esta entrega; el significado de los trece bloqueos requiere matices**

Confirmo **0 `ERROR_ENTREGA`**, tanto en el campo exterior de los planos como en `continuidad.tipo_bloqueo`. Hay 123/123 objetos con entrada y salida prevista estructuradas, frente a 14/131 en v2. No quedan contratos `null` ni bloqueos de ensamblado «Sin datos de continuidad generados».

El recuento efectivo coincide con `bloqueados_por_tipo`: 9 `CONTRADICCION_CONTINUIDAD`, 1 `CONTRADICCION_NARRATIVA` y 3 `REFERENCIA_PENDIENTE`.

Pero **no confirmo que los trece sean trece contradicciones reales específicas**. S2_P02 es una referencia visual pendiente; S2_P03/P04 son dependencias de ella. Sus motivos usan una plantilla, pero nombran al predecesor exacto y son bloqueos de dependencia legítimos, no pérdida de datos disimulada. S2_P06, en cambio, tiene una justificación narrativa insuficiente. Véase E. La existencia de una explicación larga no garantiza que sea cierta.

La comparación correcta con v2 es recuperación de cobertura, no prueba de que el sistema haya pasado de 92 % a 10,6 % de errores físicos. Tampoco esta entrega prueba por sí sola que el reintento se ejecutara o fuera el responsable de la recuperación: para eso hacen falta trazas de las llamadas.

**C. Corrección manual de la herida de Miguel**

**El evento elegido es correcto.** `S6_P07.accion_principal` dice expresamente «Miguel ve la espada por primera vez» y vincula a ello el silencio. P05/P06 revelan la espada a cámara; eso no obliga a que Miguel ya la haya visto. P06 ahora lo distingue en su salida: «la espada ya es visible en cámara, pero Miguel todavía no la ha visto».

Comprobé los cuarenta estados de entrada/salida de S6:

| Tramo | Estado del hueco |
| --- | --- |
| P01–P06, entrada y salida | Activo, sin silenciar. |
| P07, entrada | Activo, heredado de P06. |
| P07, salida | Silenciado por completo, no curado; transición durante este plano. |
| P08–P20, entrada y salida | Silenciado, sin curación ni nueva activación. |

**Las 19 uniones conservan semánticamente ese estado.** No hay igualdad literal universal: la lista completa `heridas` coincide exactamente en 11/19 uniones y la cadena `.estado` en 14/19. Las diferencias restantes en este campo son redacción y visibilidad, no otra activación o curación. No debe informarse `==` literal donde solo se ha confirmado equivalencia narrativa.

La reparación tiene estas limitaciones:

- **Disparador dentro de P07 todavía ambiguo.** Su `estado_entrada.direccion_mirada` conserva perfil/marcha y dirección de pantalla «aún sin resolver». `cambios_autorizados` cambia la mirada hacia la espada y la sostiene todo el plano. El nuevo prompt empieza mirando fijamente hacia la espada y corta la inhalación a mitad de los siete segundos, sin cambio de mirada. Para hacer inequívoco «en el instante», situar la primera visión y la reacción en el mismo punto temporal —por ejemplo, en el corte de entrada— o describir el instante de adquisición de la mirada.
- **Prompts P07/P08: formato general válido, acabado insuficiente.** Ambos son EN, tienen una imagen existente, negaciones explícitas y ninguna etiqueta organizativa de guion. Sin embargo, `ajustes` solicita Ingredients to Video / Veo 3.1 Fast / **7 s**, sin generar 8 s y recortar; contradice la matriz local del documento 14. Separar duración generada y duración retenida.
- **Contradicción literal de P07.** Dice que ninguna parte de «skin, chest, or armor» está en cuadro, pero muestra la cara. Esa negación incluye piel visible. También excluye hombros, de modo que la quietud de hombros prevista en la acción no puede ser un criterio visual de esa toma.
- **P08 cambia iluminación por cambiar encuadre.** P07 ilumina media cara en cálido; P08 prescribe piel neutra-fría y solo un punto cálido en el ojo. `cambios_autorizados.entorno.luz` lo justifica por el encuadre extremo. Un recorte puede excluir una zona iluminada, pero no cambia por sí mismo la luz sobre la misma piel conservada; hace falta precisar composición o continuidad de la fuente.
- **Estado QA inválido tras la intervención.** P07/P08 usan `control_calidad.resultado: "resuelto"`, fuera del enum del contrato y del script (`pendiente/aprobado/rechazado`). P08 además conserva `revision: "sin_revision"`. Resolver una incidencia de planificación debe registrarse aparte; la revisión del clip sigue pendiente.
- **QA y derivados.** Las escenas y el ensamblado sí están sincronizados. El objeto `qa_inter_escenas`, en cambio, conserva la incidencia antigua y S5→S6 como falsa sin anotación de resolución ni nueva versión. Los prompts P01–P06 no ordenan ya un silencio prematuro, pero el paquete necesita un QA posterior identificado como tal.

**D. Segunda comprobación de las cinco fronteras**

No ratifico «cuatro coherentes y una ya corregida» como aprobación global. El método reducido no es necesariamente incorrecto; su paquete y sus criterios no retuvieron todo lo necesario, en particular el último estado del presente antes del flashback.

| Frontera | Veredicto independiente y evidencia |
| --- | --- |
| S1_P20 → S2_P01 | **Incoherente en luz.** S1 cierra con cielo cubierto, luz cenital difusa neutra-fría, sin sombra definida; S2 abre con sol bajo, luz dura ámbar y sombra larga. S2 declara «Sin elipsis». Marcha, manos vacías y herida activa son compatibles; el cambio de hora/cielo no está autorizado. |
| S2_P20 → S3_P01 | **Compatible como flashback.** El paso al pasado permite otra localización, noche y ala herida. S2 no vuelve a desplegar veinte planos de Ónice como en v2. La escena S3 está explícitamente marcada como flashback; sería mejor que su enlace identificase también la transición temporal, en lugar de limitarse a «inicio_escena». |
| S3_P15 → S4_P01, recuperando S2_P20 | **No aprobada.** El ala sana sí se conserva, pero P15 ya acaba en el presente con `heridas: []` y armadura «sin grieta»; S4 introduce grieta y una supuesta perforación cicatrizada. Además, S2 terminó con sol rasante y S4 reinicia mediodía cenital despejado: las noches del recuerdo no transcurren en la conversación presente. Gabriel pasó de izquierda vacía y pergamino contra la túnica en S2 a sujetarlo con la izquierda en S4, sin entrega ni gesto registrado. |
| S4_P24 → S5_P01 | **Marcha/elipsis compatibles; herida no aprobada como contrato completo.** Días de marcha permiten cambiar lugar y luz. S5 conserva que el silencio aún no se activa. Pero S4 venía describiendo `tipo: "hueco/perforación antigua"`, `estado: "cerrada, cicatrizada"` en P01 y «cerrada» al final; S5 vuelve al vacío no físico. No es un silencio prematuro en S5, sino una representación errónea previa que la aprobación omitió. |
| S5_P24 → S6_P01 | **Corregida en el estado del hueco y compatible en desplazamiento.** Miguel sigue hacia el centro, manos vacías, alas intactas; el guardián puede permanecer atrás fuera de esta escena. No queda silencio anticipado en P01. No apruebo por ello toda S6: P02 pide sombras móviles de troncos en `prompt`, contradiciendo la arboleda sin sombras del párrafo 28 y S5; tampoco debe cambiarse por defecto el dosel metálico pálido a iluminación verde de bosque ordinario. |

El fallo S3→S4 exige recuperar **S2 como escena marco**, no tratar el final del pasado como única memoria física disponible. El pergamino no se transfiere por un cambio de cámara; el capítulo dice que Gabriel no lo toca. La elección de S4 de ponerlo en su mano izquierda crea además una ocupación artificial que agrava el bloqueo del bastón.

La afirmación del QA «todos los planos relevantes tenían continuidad estructurada completa» excede lo demostrado: tenían objetos de continuidad, pero no el contrato completo ni todos los hechos persistentes resueltos.

**E. Auditoría de bloqueos y errores no bloqueados**

Seleccioné cinco bloqueados con `random.Random(20260920).sample(..., 5)`: S4_P04, S4_P06, S3_P05, S2_P04 y S3_P08. Después amplié la revisión a los trece para no depender de la muestra.

| Bloqueados | Evaluación |
| --- | --- |
| S2_P02 | **Referencia pendiente real**, no contradicción narrativa. El peto agrietado es focal y la referencia base no define esa grieta. El criterio es inconsistente con S1_P04 y S2_P12, aprobados pese a mostrarla. Debe existir un único estado visual aprobado o un procedimiento explícito de creación/validación de arranque. |
| S2_P03/P04 | **Dependencias justificadas** de P02→P03. El motivo exterior identifica al predecesor. Pero `continuidad.listo_para_generar` sigue en `true` en ambos: el script solo cambió el flag exterior. Dos consumidores pueden obtener decisiones distintas. |
| S2_P06 | **Falso positivo como contradicción narrativa demostrada.** El párrafo 11 compara la llegada con una ráfaga; no prohíbe caminar tras aparecer. La salida mediante pliegue del párrafo 26 tampoco obliga a una entrada sin pasos. Los borradores v1/v2 no son autoridad para prohibir una puesta en escena nueva. Puede faltar definir materialización y aproximación, pero no procede exigir que cambiar la entrada obligue a cambiar la salida. |
| S3_P05/P06/P07 | **Conflicto de datos real, origen mal localizado.** El estado de P04 impone blanco-plateado provisional, pero su propio `luz.color_temperatura` ya prescribe cálido dorado; no nace en P05. Continuidad inventó una alternativa a un dato que ya recibió de Luz. Unificar P04 y sus derivados; no tratar toda discrepancia entre agentes como decisión pendiente del autor. |
| S3_P08 | **Bloqueo de color válido por herencia.** El otro argumento, riesgo de regeneración instantánea, requiere matiz: hay `enlace.tipo: elipsis` y cambio de noche autorizado. Es una exigencia de arranque y verificación, no una contradicción narrativa por el mero hecho de sanar entre planos. |
| S4_P03/P04 | **Conflicto de utilería real.** La derecha pasa de sujetar bastón a quedar vacía y P04 VFX lo ubica en la izquierda sin transferencia. Que la izquierda ya lleve pergamino procede de otro problema de adaptación; no invalida el salto del bastón. |
| S4_P06/P07 | **Bloqueos correctos.** El encuadre exige bastón en derecha y la herencia no permite recuperarlo; P07 continúa el problema. Ocultarlo no resuelve dónde está. |
| S5_P22 | **Bloqueo correcto y específico.** Cámara fija, troncos inmóviles y Sentinel sin traslación no producen la oclusión progresiva solicitada. Corregir encuadres inicial/final o introducir movimiento de cámara motivado. |

**Falsos negativos prioritarios:** S6_P14/P16 admiten piel desnuda pese al guante previo; S6_P17 repone guante y elimina grieta; S4_P17 repone el bastón sin gesto; S3_P04 ya contiene el conflicto de color que solo bloquea a P05–P08. Además, S3_P09 vuelve a usar resplandor cálido con `control_calidad.incidencias: []`, sin resolución documentada del conflicto anterior. Un cambio de ángulo no resuelve esos hechos.

**F. Continuidad interna: recorrido completo de S4 y S6**

| S4 | Resultado de manos, objetos, heridas y vestuario |
| --- | --- |
| P01–P02 | Miguel conserva manos vacías y guantes. Gabriel tiene bastón en derecha y pergamino en izquierda; esta segunda ocupación ya difiere del presente anterior. La herida de Miguel se redefine indebidamente como perforación cicatrizada. |
| P03 | La derecha de Gabriel se alza vacía; el bastón queda `SIN RESOLVER`. Bloqueado correctamente. |
| P04 | Mano cae sin recuperar bastón. VFX lo sitúa en izquierda; Continuidad rechaza esa transferencia. Bloqueado. |
| P05 | Mantiene derecha vacía y bastón sin localización, pero está listo por cambiar de encuadre. No se ha resuelto la dependencia física. |
| P06–P07 | El bastón requerido en cuadro sigue sin ubicación. Bloqueados. |
| P08–P13 | Miguel vacila y habla con manos vacías; Gabriel y el bastón persisten como pendientes fuera de cuadro. No desaparece anatómicamente una mano, pero se sustituye repetidamente su posición por «Sin cambios». |
| P14–P16 | Giro de Miguel, atenuación de Gabriel y lágrima. Derecha de Gabriel sigue vacía y bastón pendiente. El vestuario base se conserva. |
| P17 | **Reaparición injustificada del bastón.** `cambios_autorizados` cambia derecha vacía a bastón porque «la acción de P17 vuelve a mostrar» el objeto. Eso no es una recogida ni una transferencia. El prompt exige que aparezca desde el primer fotograma. Está listo. |
| P18 | Gabriel desaparece con bastón y pergamino; salida de objetos registrada. No hay entrega a Miguel. |
| P19–P22 | Miguel solo, manos vacías; reacción y arrepentimiento. La salida de Gabriel se conserva; la herida sigue mal tipificada como cerrada. |
| P23–P24 | Reanuda marcha, guantes y alas conservados; huellas/polvo registrados. No nace arma en sus manos. |

S4 demuestra exactamente el defecto estructural temido: el objeto no resuelto durante la oclusión reaparece al volver a ser visible, y la reaparición se declara «resuelta» usando la acción que debía auditarse como su propia justificación.

| S6 | Resultado de manos, objetos, heridas y vestuario |
| --- | --- |
| P01–P02 | Ambas manos vacías con guantes completos, peto agrietado; herida activa. |
| P03–P06 | Inserts de corteza, raíces y espada: Miguel permanece registrado fuera de campo, guantes y grieta conservados. El inventario incorpora Solmire en P05; conviene conservarla ya oculta desde P01, pues no se materializa al revelarla. |
| P07–P08 | Herida pasa a silencio correctamente. Las manos siguen físicamente presentes, pero sus posiciones degeneran a «Sin observación directa; sin datos de nueva posición». La falta de imagen no borra el último estado previsto. |
| P09 | General recupera manos junto a muslos, guantes y grieta. No hay mutilación, pero la posición se vuelve a concretar tras haber perdido precisión. |
| P10–P11 | Derecha se alza y tiembla; izquierda vacía al muslo. P11 conserva explícitamente `Guante (mano derecha): Intacto`. |
| P12–P13 | Mano queda fuera de campo; ningún plano muestra retirada de guante ni registra su destino. |
| P14 | `cambios_autorizados` asume que el guante se retiró **antes de P13**, fuera del lote. No existe esa acción en P01–P12. Su salida exige «piel desnuda (sin guante)» y `vestuario_visible: []`. La propia incidencia manda confirmar la premisa, pero está listo. |
| P15–P16 | Heredan mano desnuda; P16 toca la empuñadura y la registra en derecha. Falta inventario del guante retirado. Contacto no equivale por sí solo a extraer la espada del tronco; deben conservarse ambas relaciones hasta la desaparición. |
| P17 | **Doble reinicio físico:** `vestuario_visible` incluye guante derecho íntegro y peto «Íntegro, sin grieta». La salida anterior era piel en contacto y la armadura venía agrietada. No hay causa autorizada para ninguno de los cambios. |
| P18–P20 | Propagan guantes y peto sin grieta; la derecha sigue sujetando Solmire y la izquierda vacía. Fresno/estanque se disuelven y permanecen registrados como disueltos, sin reaparecer. La herida sigue silenciada, no curada. |

No atribuyo una amputación observada a estos JSON: no hay vídeo. Sí hay fallos de persistencia de la misma familia, ya en planificación. S6_P14 incluso detecta el riesgo y lo deja pasar a Traducción.

Como contraste favorable, S1 registra izquierda al peto en P07–P11, liberación al agacharse en P12, derecha apartando arena, apoyos hasta P18 y liberación al levantarse en P19. La lateralidad elegida no contradice el capítulo, que no la fija. Es una mejora concreta, aunque el uso abundante de abreviaciones todavía debilita el contrato.

**G. Prompts de Flow: mejor sintaxis, sin aprobación del lote**

Revisé completos, entre otros, S1_P07, S2_P09, S6_P07 y S6_P08; amplié a S3_P14, S4_P17 y S6_P16/P18 para contrastar los defectos detectados.

| Prompt | Reglas verificadas y limitaciones |
| --- | --- |
| S1_P07 | ES, una imagen, 8 s, lateralidad y negativas claras, sin rótulos de guion. «Plano medio fijo» es instrucción de cámara, no etiqueta «Plano 7». La referencia base sigue sin representar la grieta. |
| S2_P09 | EN, réplica limpia, 8 s, sin etiquetas. Usa dos referencias del **mismo Gabriel** —cara y cuerpo— sin justificar por qué no basta una composición aprobada. No rebasa el máximo de tres, pero incumple el criterio conservador por defecto. El pecho-arriba no permite comprobar la mano a altura de cadera exigida en criterios. |
| S6_P07 | EN, una referencia existente, negativas explícitas; problemas de duración, piel y sincronía del reconocimiento descritos en C. |
| S6_P08 | EN, una referencia y sin etiquetas. Recomienda reemplazar la ficha por el frame aprobado de P07, aún no asociado realmente; 7 s de Ingredients sin recorte definido y cambio lumínico pendiente. |

Los 111 registros tienen 82 listas de una referencia, 24 de dos y 5 vacías; ninguno supera tres. Todas las rutas adjuntas existen y son archivos de imagen. Las listas vacías corresponden a propuestas que no cargan una identidad; no son automáticamente un defecto. No he inspeccionado visualmente cada imagen y no equiparo existencia de ruta con compatibilidad de pose/vestuario.

La mejora frente a v2 en idioma y ausencia de encabezados organizativos es clara en la muestra. Persisten problemas operativos:

- **Referencia maestra frente a frame real.** El script obliga a que cada adjunto esté en `character_library`, mientras recomienda el último frame aprobado, que normalmente será un artefacto de vídeo fuera de esa biblioteca. El manifiesto debe distinguir identidad, composición de arranque y frame retenido; una recomendación en `ajustes` no realiza la asociación.
- **Contradicción al traducir el enlace.** S3_P14 es `cambio_angulo`, contraplano desde el OTS de P13, pero ambas variantes Flow dicen «continuando directamente del plano anterior sin cambio de encuadre». El idioma único no garantiza que la cámara sea correcta.
- **Negativas de alcance excesivo.** S6_P16 afirma que en cualquier otro momento de la secuencia ambas manos están vacías, aunque P17–P20 mantienen la derecha en Solmire. Limitar la prohibición a armas adicionales y a momentos anteriores al contacto.
- **Conflictos ya traducidos.** S4_P17 exige bastón desde el inicio; S6_P16 exige piel desnuda sin resolver guante. Flow no debe recibir una incoherencia acompañada de una nota para comprobarla después.

**H. Ingeniería, comparación y prioridades**

El cambio de v2 a v3 sí funciona donde era más urgente: texto numerado en Dirección, lotes pequeños, presencia del campo negativo en 123/123 planos y bloqueo por ausencia diferenciado. Frente a v1, se conservan estados estructurados y se filtran muchas incidencias antes de traducir. No conviene deshacer esas mejoras.

La inspección del script muestra límites concretos:

1. **La fuente incrustada no llega a todos los supervisores.** `numerarParrafos()` incorpora `args.parrafosEs/En` en Dirección y ES en Segmentación. La extracción ocurre fuera del archivo; aquí no hay validación de paridad, rangos ni hash del texto recibido. `continuidadPrompt()` recibe identidad, lote y estado anterior, pero no el extracto ES/EN, ni `notaAlasMiguel()`, ni el resumen completo cuando hay contexto previo. No se sostiene literalmente que ningún agente necesite buscar el texto: S2_P06 invoca borradores antiguos y S4_P24 cita «párr. 55–57» de un capítulo con 35. La contaminación por fuentes secundarias sigue siendo observable.
2. **La cardinalidad está parcialmente comprobada.** `stageContinuidad()` detecta IDs faltantes con un `Set`; no rechaza duplicados ni IDs extra, ni verifica por código que cada registro tenga estados completos. `find()` toma el primero. No basta para garantizar igualdad exacta de conjuntos y cardinalidades.
3. **El reintento puede romper la herencia.** Si un lote P05–P08 devuelve P05/P07/P08 pero falta P06, `contextoRetry` sigue siendo P04, último acumulado fuera del lote. P06 se rehace desde P04, no desde P05, y P07 no se recalcula desde la salida reparada. Si faltan IDs no contiguos, se presentan como un lote consecutivo. No afirmo que sucediera aquí; es un defecto reproducible por inspección de la lógica. Rehacer el sufijo desde el primer faltante con su predecesor real, o reintentar el lote entero y validar todas las uniones.
4. **La propagación usa adyacencia y tipo de cámara, no dependencias físicas.** Solo bloquea si el plano inmediatamente anterior no está listo y `enlace.tipo === 'continuacion'`. Un `cambio_angulo` no exime de heredar bastón, guante o grieta. Tampoco sincroniza los flags interiores. Pasar al siguiente lote no autoriza resolver un dato pendiente por suposición.
5. **Contrato todavía incompleto en 123/123.** Ninguno contiene dentro de `continuidad` `id_escena`, `fuente_narrativa`, `generacion`, `estado_salida_observado`, `frame_final`, `enlace.frame_heredado` ni `control_calidad.evidencias`. El booleano `estado_salida_observado_pendiente` existe en todos, pero no sustituye los campos reales a `null`. Los 123 tienen versión de esquema y negativas, mejora respecto a v2. Siguen listas donde el contrato propone mapas, identificadores de personaje variables (`miguel`/`Miguel`) y posiciones «Sin cambios». Debe versionarse la adaptación del esquema y validarse realmente, no pedir «contrato completo» con un schema que lo omite.
6. **QA sin integración de reparaciones.** `qaPrompt()` todavía serializa todas las escenas completas; el método reducido externo no está incorporado al script inspeccionado. El fallo por 1,2 M tokens es información aportada por el usuario, no una cifra de ejecución que yo haya medido. El riesgo de volumen sí se ve en el código. El QA binario y su redacción sobre `no_verificable` tampoco representan con claridad una dependencia pendiente. Tras editar S6, no se versionó/recalculó el resultado guardado.

Priorizaría, antes de otro capítulo:

1. **Reparar esta entrega y sus derivados:** guante y peto de S6; recuperación del bastón y pergamino de S4; luz común del presente S1/S2/S4; estado no físico del hueco; color de curación desde S3_P04; contacto y desaparición de la arboleda sincronizados. Revisar el bloqueo interpretativo de S2_P06.
2. **Un estado persistente por línea temporal y decisiones de adaptación explícitas.** Recuperar el presente desde S2 al salir del flashback. Conservar objetos y vestuario ocultos; separar estado físico de encuadre. Una aparición en cámara no es causa física.
3. **Validación e invalidación efectivas.** IDs/cardinalidad/esquema, comparación de hechos entre planos, coherencia Dirección–Luz–VFX–Continuidad–Flow, bloqueos transitivos por campo y versión, y un único estado de autorización. Reparar el reintento antes de confiar en él.
4. **QA acotado pero suficiente:** fronteras con estado persistente completo, incidencias abiertas, cambios autorizados, luz y fuente narrativa; añadir el estado previo del presente en flashbacks. Recalcular tras cualquier reparación, manteniendo el diagnóstico antiguo como historial y no como resultado vigente.
5. **Paquetes de generación concretos y ensayo corto.** Duración generada/retención, idioma seleccionado, referencia de arranque compatible y frame real identificado. Después, probar general → mano oculta → general y contacto con utilería, revisando el clip entero y registrando tomas rechazadas. Esa prueba es necesaria para evaluar el problema original; no está acreditada por estos JSON.

**Decisión final:** aprobado como avance de ingeniería y material para una nueva corrección localizada; no aprobado como paquete fiable de producción. La pérdida masiva de datos y la sustitución de Solmire están resueltas en el artefacto auditado. Lo que falta ahora es impedir que una contradicción detectada, una ocultación o un nuevo lote se conviertan en permiso para inventar el estado siguiente.
