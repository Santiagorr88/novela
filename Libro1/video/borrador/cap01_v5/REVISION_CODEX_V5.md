# Quinta revisión independiente — Las Crónicas del Juicio, capítulo 1

Fecha: 2026-09-25. Revisor: Codex. Auditoría documental independiente de v5; no se generaron ni visionaron vídeos. Único archivo escrito: este informe.

**Veredicto: v5 mejora considerablemente la entrega y reduce la cascada, pero no está lista para producción ni para extender el pipeline sin correcciones. No confirmo el QA «7 de 7 fronteras coherentes».** Los ocho bloqueos automáticos directos no demuestran ocho discontinuidades físicas; hay falsos positivos de inventario, visibilidad y salida de personaje. Entretanto pasan errores reales: el bastón queda sin resolver en S5, una lágrima reaparece, el flashback cambia el lado canónico del ala, varias escenas reinician la iluminación y Solmire vuelve a separar sus disparadores de sus consecuencias. El 5,7 % mide bloqueos, no errores residuales.

**Alcance y método.** Leí los capítulos ES/EN, las acciones de los 159 planos, los estados de herida de Miguel en las ocho escenas, los nueve motivos completos y sus entradas/salidas, las siete fronteras con su contexto de escena, el ensamblado, ambos resúmenes y las funciones solicitadas del script temporal. El recorrido interno completo de manos, objetos, heridas y vestuario se concentra en S2, S5 y S8, con comprobaciones adicionales en S1, S3, S4 y S7. Revisé cuatro prompts principales completos de distintas escenas y amplié la lectura a los prompts de los defectos encontrados. Contrasté el contrato 18 y las reglas locales verificadas por el autor del documento 14; esta auditoría no certifica la interfaz actual de Flow. Consulté asimismo la revisión v3 y el README del estado `burned_left_wing` para resolver la lateralidad.

En las citas, `S5 P06` significa el plano P06 del archivo `B1C01_S5.json`, aunque su ID almacenado sea solo `P06`. Los campos `estado_entrada`, `estado_salida_previsto`, `enlace` y `cambios_autorizados` están bajo `planos[].continuidad`. La equivalencia se evalúa semánticamente; no equiparo diferencia de redacción a cambio físico.

**Inventario y procedencia comprobados.**

| Escena | Planos | Bloqueados | Registros Flow | Duración |
| --- | ---: | ---: | ---: | ---: |
| S1 | 20 | 2 | 18 | 151 s |
| S2 | 10 | 2 | 8 | 140 s |
| S3 | 31 | 0 | 31 | 210 s |
| S4 | 12 | 0 | 12 | 140 s |
| S5 | 28 | 1 | 27 | 200 s |
| S6 | 15 | 0 | 15 | 120 s |
| S7 | 21 | 3 | 18 | 149 s |
| S8 | 22 | 1 | 21 | 170 s |
| Total | 159 | 9 | 150 | 1280 s |

Las ocho escenas individuales coinciden como objetos JSON con `guion_completo.escenas`. Hay 159 contratos de continuidad, sin pérdida de entrega; el agregado confirma 8 `CONTRADICCION_CONTINUIDAD` y 1 `REFERENCIA_PENDIENTE`. Los rangos 1–4 / 5–9 / 10–17 / 18–20 / 21–27 / 28–29 / 30–32 / 33–35 cubren los 35 párrafos narrativos, sin huecos de segmentación. Ambos textos sostienen los dos disparadores decisivos: silencio al ver la espada y desaparición de la arboleda al tocarla. La adaptación de niebla del Sentinel procede de las notas de identidad, no del texto literal sólido.

Hay dos discrepancias de procedencia que impiden aceptar las métricas históricas sin reservas:

- **El v4 actualmente disponible no contiene 50 bloqueos.** `cap01_v4/guion_completo.json` contiene 153 planos y **142 bloqueados (92,8 %)**: 81 de continuidad, 57 de referencia y 4 narrativos. Su `RESUMEN.md` dice 50, distribuidos 10/35/5. La cifra 32,7 % puede describir otra pasada, pero no es reproducible con el ensamblado entregado. No deduzco cuándo ni por qué divergieron.
- **`cap01_v5/guion_completo.json.qa_inter_escenas` es `null`.** El «7/7» está afirmado en el resumen; no hay resultados estructurados de ese agente en este ensamblado. Además, `segmentacion.incidencias` dice que P35 queda fuera de S8 en una nota, aunque el rango y los planos sí lo incluyen. Debe corregirse el resumen de procedencia, no regenerarse el capítulo por esa frase.

**A. Fix de «cicatriz»: útil para el caso observado, insuficiente como guarda semántica.**

`estaNegadoEnContexto()` (script, línea 571) usa `indexOf(palabra)` y toma los 45 caracteres anteriores. No comprueba frase, cláusula, sujeto ni alcance de la negación. Peor: `detectarCuracionFisicaHuecoMiguel()` le entrega texto pasado por `normalizarTexto()`, que elimina puntos, comas, punto y coma y dos puntos. Por tanto, la descripción «en su misma frase» del resumen no corresponde a la implementación.

Ejecuté en Node únicamente las funciones extraídas del archivo, sin ejecutar el Workflow ni modificar archivos. Resultados reproducidos con `id_personaje: "miguel"`, `zona: "esternón"`:

| `heridas[].estado` de prueba | Resultado actual | Evaluación |
| --- | --- | --- |
| `sin marca física, cicatriz ni perforación visible` | No bloquea | Correcto: resuelve el bug comunicado. |
| `la herida está cerrada` | Bloquea | Correcto. |
| `sin dolor. La herida está cerrada` | No bloquea | Falso negativo: otra frase protege una curación real. |
| `sin dolor, pero la herida está curada` | No bloquea | Falso negativo: negación de dolor, no de curación. |
| `no está cerrada; ahora sí está cerrada` | No bloquea | Falso negativo: solo se inspecciona la primera aparición de la palabra. |
| `no presenta, en toda la superficie anteriormente examinada con cuidado y bajo iluminación uniforme, cicatriz` | Bloquea | Falso positivo: la negación real queda fuera de ventana. |
| `herida sanada` | No bloquea | Vocabulario equivalente no cubierto. |

Ampliar los 45 caracteres reduciría unos falsos positivos y aumentaría las negaciones ajenas que protegen afirmaciones: no soluciona el problema. Tampoco basta segmentar por puntos: la adversativa dentro de una frase y las enumeraciones requieren alcance. Conviene conservar la puntuación para este análisis, recorrer todas las ocurrencias y separar una validación estructurada del estado metafísico de la revisión lingüística del texto libre.

Hay límites adicionales: solo inspecciona `h.estado`, solo reconoce el hueco por `zona` con esternón o `tipo` con «hueco», y no valida el momento del silenciamiento. Una afirmación contradictoria en `accion_principal`, `visibilidad` o `prompt` queda fuera de esta guarda. Una localización equivalente sin esos términos también puede eludirla.

**Resultado sobre v5:** recorrí los 318 estados de entrada/salida y reproduje cero alertas de esta guarda. La lectura de las variantes de herida no encontró una curación física afirmativa del hueco que hubiera pasado indebidamente. Las curaciones afirmativas de S4 pertenecen al ala, que es una herida distinta. S1–S7 conservan el hueco metafísico; S5 usa «permanente, sin cicatrización física». S8 declara el cambio en P08 y no declara curación física después. Esto valida el caso concreto, no la suficiencia general del fix. El fallo real de S8 es temporal, detallado en E.

**B. Cascada: reducción real, protección incompleta.**

Confirmado en `stageContinuidad()`: `const TIPOS_QUE_HEREDAN = new Set(['continuacion'])`. `cambio_angulo` no propaga bloqueos. Solo hay una dependencia bloqueada, **S2 P06 desde P05**; P07 cambia de ángulo y queda listo. No se observa ninguna escena arrastrada entera. Una vez reparado el falso positivo de P05, P06 debería reevaluarse y liberarse: carece de contradicción propia demostrada. La propagación es correcta respecto al flag de entrada, aunque su raíz sea errónea.

La función `detectarRupturasEntrePlanos()` **sigue definida**, pero ya no se invoca. El comentario que justifica su desactivación afirma que entrada→salida de B detectaría también una herencia incorrecta desde A: eso es falso. Si A termina sin objeto y B empieza y termina con él, B es internamente estable. El caso de la lágrima S5 P19→P20 demuestra la laguna en estos mismos datos.

El agente conserva contexto del vecino al cambiar de lote. `BATCH=4`; el reintento incorpora `parcialesConocidos`, elimina duplicados/IDs inesperados y solo pide faltantes. Es una mejora razonable. Los datos completos demuestran que esta entrega no perdió contratos; sin trazas no atribuyo esa integridad a un reintento efectivamente ejecutado.

Persisten dos problemas de integración:

- En **los nueve bloqueados**, el flag exterior `listo_para_generar` es `false`, pero `continuidad.listo_para_generar` sigue en `true`. Validador y propagación no sincronizan la decisión interna. La traducción actual filtra por el exterior; otro consumidor puede aprobarlos por el interior.
- La propagación consulta el elemento anterior del array, no resuelve un grafo por `id_plano_anterior` y versión. Restringir dependencia visual a una continuación es razonable; la herencia del estado físico debe verificarse también al cambiar de ángulo, sin volver a bloquear por cada omisión textual.

**C. Los nueve bloqueados: revisión individual.**

Antes de evaluar sus motivos, hay un **bug de diagnóstico reproducible por lectura del código**: las direcciones están invertidas. Para `reaparicion`, `detectarCambiosSinCausa()` recorre las claves de entrada y busca en salida, pero informa «aparece en salida». Para `desaparicion` hace lo contrario. Se ejecutan ambas direcciones, por lo que aún detecta diferencias de conjuntos, pero cuenta el suceso al revés. Esto explica varios motivos aparentemente incompatibles con el JSON.

| Plano | Evidencia concreta | Dictamen sobre el bloqueo registrado |
| --- | --- | --- |
| **S1 P08** | Entrada enumera ambos sabatones y guantes; salida del macro enumera solo peto y guante derecho. El motivo dice que el sabatón izquierdo «aparece» cuando deja de enumerarse. No hay retirada física del calzado. | Falso positivo como discontinuidad física; omisión de inventario oculto que conviene reparar. No es una reaparición real. |
| **S1 P09** | Sale del macro, baja la mano y retoma la marcha. Salida vuelve a enumerar ambos sabatones y añade `faldones`; motivo los llama desaparición. | Falso positivo por cobertura del inventario y reencuadre. El motivo también incluye faldones, omitidos en el resumen. |
| **S2 P05** | Entrada usa `resto de la armadura y faldones` y `vestuario_oculto: resto del cuerpo por debajo del hombro`; salida detalla guantes y `grebas y escarpes (sabatones)`, puestos. | Falso positivo de granularidad. Tampoco desaparecen: se detallan al abrir encuadre. |
| **S2 P06** | Entrada hereda guantes y calzado de salida de P05; siguen puestos al final. Bloqueo solo por `continuacion`. | Dependencia mecánica de un falso positivo. Revisar tras reparar P05. |
| **S5 P21** | Gabriel está presente en entrada y sale de `personajes` al completar su desaparición. `cambios_autorizados` declara la salida del personaje completo. Túnica, halo, lágrima y pergamino salen con él; el motivo dice que «aparecen». | Falso positivo por salida autorizada del personaje y falta de cobertura jerárquica. **No es simplemente un sinónimo de túnica.** No corrige los errores previos del bastón y la lágrima. |
| **S7 P06** | Miguel pasa de `conjunto completo` oculto a hombrera/peto posterior visible y `peto frontal y rostro` oculto. | Falso positivo de inventario/visibilidad. `conjunto completo` es de Miguel, no del Sentinel. |
| **S7 P08** | Contraplano del rostro de Miguel: peto posterior/hombrera pasa a `peto (borde inferior)`; el Sentinel sale de cuadro y se registra `conjunto completo` oculto. | Falso positivo de representación. Afecta a ambos personajes, no solo al atuendo del Sentinel. |
| **S7 P13** | Sentinel oculto en ambos estados: entrada `conjunto completo (ojos, zarcillos de peltre)`; salida `conjunto completo`. | Falso positivo provocado además por el filtro anatómico: la entrada se descarta por contener `ojos`/`zarcillos`, la salida genérica no. No cambia ningún cuerpo ni traje. |
| **S8 P05** | El tilt abandona el hombro de Miguel. Salida conserva armadura, guantes, sabatones y alas, y añade `Cuerpo completo de Miguel` oculto. | Falso positivo de visibilidad y clasificación de cuerpo como prenda. No desaparece físicamente Miguel. |

La tabla del resumen que afirma **«0 planos bloqueados por falso positivo de validador» queda refutada**. Son ocho decisiones automáticas directas sin discontinuidad física demostrada por esos motivos y una dependencia derivada. Algunas revelan datos insuficientemente normalizados, lo cual sí merece reparación del contrato; no justifica describirlas como prendas que desaparecen realmente.

Ampliar un diccionario de sinónimos no basta. `coincideAlgunaClave()` acepta una sola palabra significativa compartida y substrings, sin identidad ni lateralidad. Probé `guante izquierdo` contra `guante derecho`: devuelve `true`. El filtro anatómico también descarta cualquier etiqueta que contenga «rostro», aunque sea `peto frontal y rostro`. Y `extraerClaves()` no recorre `objetos_escena`: un bastón soltado puede quedar sin ubicación fuera de sus controles. Se necesita distinguir identidad, estado, portador, presencia y visibilidad; no seguir acumulando equivalencias de palabras.

**D. Siete fronteras: no confirmo el veredicto global del agente ligero.**

| Frontera | Verificación con contexto completo | Veredicto |
| --- | --- | --- |
| **S1 P20 → S2 P01** | P18–P20 de S1 ya dejaron a Miguel de pie. S2 abre arrodillado, con dos dedos apoyados, y declara «Sin elipsis». Además pasa de cielo cubierto, luz suave neutra-fría, a cielo despejado, sol de media mañana y sombras duras. Guantes y sabatones agrietados sí persisten. | **Incoherente en postura y ambiente.** S1 se incorpora demasiado pronto respecto al tramo contemplativo siguiente. |
| **S2 P10 → S3 P01** | Peto, calzado y hueco continúan. Marcha→detención es un gesto plausible pero no queda resuelto en el empalme. El sol duro blanco-dorado se sustituye por cielo cubierto azufrado, suave verde-amarillento, sin cambio de tiempo justificado. | **Incoherente en luz; precisar detención.** |
| **S3 P31 → S4 P01** | Entrada al recuerdo explícita en escena/flag y enlace; fortaleza nocturna, Miguel caído y ala herida no son una regeneración inversa del presente. El hueco permanece. | **Transición temporal coherente**, pero el ala derecha elegida en S4 contradice el estado canónico izquierdo; véase E. |
| **S4 P12 → S5 P01** | El ala termina completamente sanada; el regreso la conserva intacta. Para el presente corresponde recuperar S3 P31, como exige el contrato 18: bastón derecho y pergamino contra túnica sí vuelven correctamente. Pero S5 vuelve con sol duro/cielo despejado y luego aire quieto, frente al cielo cubierto y viento de S3. | **Incoherente en el ambiente de la escena marco**, aunque el salto temporal y la recuperación del ala sean comprensibles. |
| **S5 P28 → S6 P01** | Miguel continúa solo, vestido y con hueco metafísico. Arena caliente→musgo y luz sin sombras están motivados por el párrafo 28. No vuelve Gabriel ni aparece el bastón en su mano. | **Compatible en el cuerpo de Miguel y el cambio de lugar, con reserva:** el texto dice «durante días», pero el enlace afirma «Sin elipsis». El bastón sigue sin destino resuelto en S5 y no puede darse por cerrado ese inventario. |
| **S6 P15 → S7 P01** | S6 deja a Miguel inmóvil sobre musgo, sin partículas, con luz sin dirección. S7 entra ya caminando por suelo polvoriento, con bruma y cenital filtrada. Su desarrollo confirma polvo a cada paso y en P19 franjas de luz y sombra proyectadas por troncos. | **Continuidad ambiental no resuelta y contradicción con la arboleda sin sombras.** No basta conservar armadura y hueco. |
| **S7 P21 → S8 P01** | Miguel desaparece detrás de los troncos y entra al espacio del fresno. Continúan guantes, grietas y alas sanas; el cálido del centro se motiva con el estanque. El hueco no entra silenciado. El Sentinel permanece atrás: no es una desaparición física. | **Empalme corporal/narrativo compatible.** No certifica el evento interior de S8 ni su iluminación posterior. |

El frío o silencio ambiental de la arboleda no se confundió aquí con silenciamiento de la herida. Tampoco considero que una diferencia entre pasado y presente sea por sí sola un error. Los problemas marcados son hechos concretos no justificados por el enlace o por el texto. El resultado no puede resumirse como siete fronteras aprobadas.

**E. Continuidad interna: tres escenas completas y defectos adicionales.**

**S2 — diez planos recorridos.** P01 mantiene dedos derechos sobre piedra e izquierda en muslo; P02 barre arena; P03 retira los dedos; P04–P07 conservan manos y cuerpo mientras se encuadran rostro, camino y cimientos. P08 sube la derecha al peto, P09 la retira al incorporarse y libera la izquierda, P10 marcha con ambas vacías. No encontré mano ausente ni objeto adquirido sin acción. El montículo se forma en P02, permanece en P03–P08 y aumenta al desprenderse arena de las rodilleras en P09; P10 lo conserva mientras añade polvo de pisadas. Los cimientos se revelan en P06 y P07 cubre una esquina con arena, heredada por P08–P10. El hueco sigue activo.

P05/P06 no localizan un fallo físico; los problemas principales son la entrada desde S1 y el inventario de ropa demasiado agregado. `grebas y escarpes (sabatones)` termina describiendo «agrietados en las rodilleras»: mezcla regiones del traje y debilita el rastreo de las grietas del calzado, aunque no afirma que se reparen. El arranque del ascenso de mano de P08 también debería enlazarse con su reposo en P07, sin usar el cambio de ángulo como sustituto del comienzo del gesto.

**S5 — veintiocho planos recorridos.** P01–P05 conservan Vox Aeternum en la derecha de Gabriel y la izquierda vacía; Miguel mantiene ambas manos vacías, guantes y armadura agrietada. P06 elige la derecha para el gesto vacilante del texto y añade soltar el bastón. Su salida registra `objetos_en_mano.mano_derecha: []` y `objetos_escena[baston_vox_aeternum].estado: "Sin resolver, pendiente de un plano que lo muestre o narre su destino"`. P07–P17 mantienen la mano vacía; P18 lo recuerda expresamente como sin resolver. P19–P20 sostienen esa ausencia; P21 hace desaparecer a Gabriel. P22–P28 conservan el bastón con ubicación desconocida y portador ninguno, mientras Miguel se aleja.

**Es un fallo real de planificación no bloqueado en P06.** La acción de soltar está narrada en el prompt, de modo que no lo llamo desaparición mágica: el problema es que el propio guion admite desconocer dónde queda un objeto persistente, contradice la pauta de bastón derecho de `IDENTITY_NOTES` y nunca resuelve su destino. El párrafo 22 no obliga a usar la derecha; la izquierda libre evita el conflicto. Si se mantiene la elección, hace falta narrar apoyo/recogida y resolver su salida. No reaparece arbitrariamente en esta pasada, pero tampoco se ha conseguido un inventario resuelto hasta la salida de Gabriel.

**Hay además una reaparición real en S5 P19→P20.** P19 `vfx_principal`, `cambios_autorizados`, salida de `vestuario_visible` y prompt dicen que la lágrima llega al mentón y **se disuelve**. P20 entrada y prompt dicen que **sigue visible sobre la mejilla**, «sin haberse reabsorbido ni desaparecido», y su enlace exige heredar el último frame de P19 para conservarla. Ambos planos están listos. No es granularidad: es un reinicio del efecto, heredado luego por P21. La solución es escoger una única evolución y sincronizar VFX, estados y prompts.

P21 sí autoriza que desaparezcan Gabriel y sus prendas; no es el origen de esos dos defectos. El pergamino se mantiene contra la túnica, sin pasar a las manos, y termina fuera de escena con Gabriel. P22–P26 dejan a Miguel solo; P27 inicia la marcha y P28 la continúa. No hay amputación/reaparición de manos ni curación física del hueco en los 56 estados de esta escena.

**S8 — veintidós planos recorridos.** P01–P03 llevan a Miguel al fresno y lo detienen con manos vacías. P04/P05 revelan la espada a cámara; P06 ya lo muestra observándola, P07 mantiene esa mirada. P08 silencia el hueco; P09/P10 desarrollan el reconocimiento. P11 inicia la elevación de la derecha, P12 la lleva cerca del hombro, P13 la conserva; P14 acerca dedos, P15/P16 mantienen la proximidad y P17 queda a un centímetro. P18 introduce roce, P19 cierra agarre y registra `espada_solmire` en la derecha; P20–P22 conservan agarre mientras desaparece visualmente el entorno. La izquierda permanece presente y vacía. La espada sigue clavada: no hay extracción narrada.

Tres problemas impiden aprobar esta secuencia:

1. **Silencio tardío.** S8 P06 `accion_principal`, `direccion_mirada` y prompt dicen que Miguel **observa la espada**, durante un plano de 8 s. Su herida dice «Sigue sin silenciarse». P07 mantiene la misma mirada y la herida sin silenciar; P08 introduce por fin el silencio. No es el caso admisible «la ve cámara, Miguel aún no»: el observador está identificado. Tampoco se declara repetición temporal. P06 incluso sitúa el silencio «en el plano siguiente», pero P07 lo aplaza otra vez. Corregir el disparador desde la primera visión real, o impedir explícitamente esa visión en los planos anteriores.
2. **Guante puesto y contacto de piel incompatibles sin resolución.** P14 explicita guante puesto; P17–P22 siguen declarando `guantes: Puestos, sin cambio`. P18 salida/prompt describe piel de dedos **y dorso** rozando la empuñadura; P19 describe fusión de luz con piel y simultáneamente exige que el guante no atraviese el objeto. No hay retirada, apertura de guante ni estado aprobado que deje esos puntos de piel descubiertos. Es el mismo conflicto de contacto que ya se había señalado en revisiones anteriores. Debe resolverse en guion y referencia, no dejar que Flow invente la anatomía.
3. **Desaparición diferida.** El primer contacto ya ocurre en P18; P19 dedica otro plano a cerrar el agarre con el estanque todavía «Brillo estático continuo; sin cambios». La disolución comienza en P20 y se completa en P21/P22. Los enlaces son continuaciones y los ajustes piden Extend. La frase «en el instante» no vuelve simultáneos clips sucesivos. ES/EN hacen desaparecer la arboleda al contacto; un desarrollo dilatado requiere una decisión explícita de adaptación, o sincronizar contacto y desaparición dentro del mismo evento.

Después de P09, el texto de la herida suele degradarse a «metafísico… sin cambio», en vez de conservar «silenciado». No encontré una reactivación afirmada, y el zumbido de P15 sí procede del párrafo 34. Pero el estado deja de ser autocontenido: un consumidor aislado no puede saber qué conserva «sin cambio». Es especialmente frágil con el alcance de vecino inmediato.

**Hallazgo adicional en S4: ala derecha inventada como variante narrativa.** Los 24 estados de entrada/salida de S4 asignan la herida del ala al lado `derecho`; el prompt P05 coloca la izquierda de Gabriel sobre el ala derecha de Miguel. `referencias_personajes` de P01 llega a decir que no debe confundirse con `states/burned_left_wing`, al que atribuye otro estado del presente. El contrato 18 y el README de ese estado fijan **ala izquierda anatómica** y derecha intacta. Los textos ES/EN no introducen una segunda lesión de ala derecha y `notaAlasMiguel()` no autoriza cambiar de lado. La lesión fresca puede necesitar arte distinto del daño antiguo de la referencia; eso no permite inventar otra lateralidad. P12 sí termina sanándola completamente, pero sana el lado incorrectamente seleccionado. Corregir esta decisión antes de generar el flashback.

**F. Prompts de Flow: formato generalmente mejor, contenido aún inseguro.**

Muestra principal completa: **S2 P02, S4 P05, S5 P06 y S7 P16**. Los cuatro tienen idioma ES, negativas dentro de la prosa y ausencia de rótulos de sección como «Audio de fondo». Los términos técnicos prestados no son una segunda pista de diálogo. S2 P02 y S5 P06 llevan una imagen; los dos planos de pareja, S4 P05 y S7 P16, llevan dos, justificadas por dos identidades. S7 P16 camina de perfil con travelling lateral. S2 P02 tiene a Miguel arrodillado; los otros dos no piden marcha frontal. En esta muestra se respetan las reglas básicas solicitadas.

Pero respetar el formato no equivale a poder copiar y producir:

- S4 P05 hace decir a Gabriel **«El silencio —le había dicho Gabriel entonces— es lo que deja…»**. Se ha incluido una acotación del narrador dentro de la réplica audible. Además reproduce el ala derecha errónea. Debe extraerse solo el diálogo del personaje.
- S5 P06 envía la suelta del bastón con destino sin resolver y pide 7 s como ajuste nativo, sin explicar generación/recorte. S2 P02 sí separa clip base y extensión para su duración de 14 s; no hay una pauta uniforme de duración generada frente a duración retenida.
- La ampliación a S8 P19 encuentra **`P18` dentro del texto final**: «desde el roce final de P18». Incumple la eliminación de identificadores de guion y no aporta significado visual al generador. Sus menciones a un «recuerdo posterior» también están fuera de lugar: el flashback ya ocurrió.
- S8 P08 no incluye una negativa explícita de «sin arma/vaina», aunque la nota global la exige siempre. Su texto dedica espacio a cauterización y a ese «recuerdo posterior», mientras deja ambiguo el instante real de adquisición de la mirada.
- Los adjuntos son referencias de biblioteca, y varios `ajustes` ordenan sustituirlos por un último frame aún inexistente. Esto es un paquete de planificación. En cambios de ángulo, por ejemplo S8 P08 desde el gran plano P07, debe construirse una composición nueva compatible con el estado, no asumir que el frame ancho ya sirve de primer plano facial. Para Extend debe identificarse el clip aprobado que se extiende.

En los 150 registros Flow hay 122 con una referencia, 27 con dos y uno sin adjuntos; ninguno supera tres. La preferencia por una imagen sí está implantada en cantidad. No demuestra que ya estén resueltas las referencias de estado ni que los 150 prompts sean aptos para copiar sin revisión. Los defectos narrativos y de contacto anteriores ya están propagados a texto de generación.

**G. Comparación y prioridades.**

V5 es la mejor de las cifras comunicadas en **cobertura y reducción de bloqueo operativo**, y la cascada de una sola referencia frente a escenas enteras es una mejora demostrada. No la certificaría como la mejor continuidad global: v3 ya tenía corregido explícitamente su instante de silencio y v5 vuelve a introducir una observación previa incompatible. La revisión v3 también detectó fallos que su QA agregado no recogía; comparar solo 4/5 con 7/7 o 10,6 % con 5,7 % no mide calidad. La comparación cuantitativa con el v4 de 50 bloqueos requiere recuperar ese artefacto exacto.

El siguiente trabajo debería priorizarse así:

1. **Corregir los errores reales del capítulo:** lateralidad de S4; mano/bastón y lágrima de S5; primera visión, guante/contacto y desaparición de S8; postura y ambiente de las fronteras identificadas. Regenerar únicamente sus datos y derivados afectados, conservando trazabilidad.
2. **Separar estado físico persistente de visibilidad y texto.** IDs de piezas por lado; estado del hueco explícito `activo/silenciado`, sin convertirlo en curación; portador y ubicación del bastón; salidas de personajes que cubran sus pertenencias. Una omisión puede heredar; una contradicción explícita o un destino «sin resolver» no puede convertirse en aprobación.
3. **Restituir QA interplano selectivo**, independiente de la cascada de frames: comparar hechos persistentes y cambios declarados, incluida la escena marco al volver del flashback. No reactivar el cotejo de nombres de tolerancia cero. Añadir casos de regresión del bastón, lágrima, mano izquierda/derecha, negación ajena, negación larga y segunda ocurrencia afirmativa. Estas pruebas pueden ejecutarse sobre fixtures pequeños antes de otra pasada completa.
4. **Unificar decisiones y evidencias:** un solo estado de preparación; corregir verbos invertidos del detector; conservar resumen/ensamblado de cada pasada con versión o hash; publicar el QA de fronteras estructurado y su alcance. Dividir ese QA con inventario heredado y eventos, no enviar ocho escenas completas ni limitarse a cuatro planos sin memoria del presente.
5. **Ensayar clips una vez corregido el guion.** El contrato exige revisar interior del clip, empalme, estado observado y frame final aprobado. Esta entrega solo demuestra planificación. Resolver además duración: 1280 s son 21 min 20 s, fuera del objetivo de 8–15 min; fusionar nombres de escenas no reduce por sí solo el metraje.

**¿Merecen ingeniería los nueve bloqueos restantes? Sí, pero no otra ronda centrada solo en sinónimos.** Su volumen permite resolverlos manualmente para este piloto. Sin embargo, el detector muestra direcciones invertidas, filtros anatómicos que eliminan prendas y coincidencias que confunden lados: no conviene trasladar eso a más capítulos. La prioridad es recuperar sensibilidad ante los fallos reales sin volver al bloqueo masivo. El piloto puede continuar tras corrección localizada y revisión manual; la aprobación de producción sigue pendiente.
