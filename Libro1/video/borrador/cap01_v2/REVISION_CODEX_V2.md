# Segunda revisión independiente — capítulo 1, pipeline v2

Fecha: 2026-09-18. Revisor: Codex. Auditoría documental, sin generación ni visionado de clips.

**Veredicto: mixta en diseño, regresión operativa y narrativa en la entrega. No aprobada para producción.** El bloqueo efectivo evita traducir datos ausentes y algunas contradicciones reales, pero no demuestra que haya mejorado la continuidad. S6 pierde por completo el hallazgo de Solmire. El contrato sigue incompleto incluso en los planos con estados estructurados.

Las dos hipótesis iniciales necesitan matices: **CANON_NOTES es un riesgo plausible, no una causa demostrada; la confusión entre líneas y párrafos es otra explicación concreta. El volumen de salida es un riesgo evidente, pero hay archivos intermedios con todas las entradas de cinco escenas: no se puede afirmar que los agentes no las produjeran.**

## Alcance y comprobaciones

Leí el capítulo ES completo, las acciones de los 131 planos, las seis escenas individuales y el ensamblado; examiné los 14 bloques de continuidad conservados y los diez prompts de Flow. Comparé S3/S6 de v1 y el informe anterior, el script indicado y el contrato del documento 18, incluida la incorporación de las pruebas del autor; contrasté también la sección correspondiente del documento 14. Para investigar la pérdida de datos inspeccioné archivos JSON intermedios situados junto al script. No utilicé el log de otra revisión como evidencia.

El capítulo tiene 35 párrafos narrativos, excluido el título. Las seis escenas individuales coinciden como objetos JSON con las del ensamblado. Los 131 IDs son únicos, aunque su formato varía (`S1_P01`, `S2-P01`, `S4_01`). Las duraciones suman **932 s**, frente a 930 s previstos; la diferencia está en S4 (182 frente a 180). No se modificó ningún archivo salvo este informe.

Las referencias a campos son rutas dentro del archivo de escena correspondiente. Conservo los IDs reales, incluidos guiones. «Con datos» significa que hay un objeto `continuidad` con ambos estados estructurados; **no significa cumplimiento del contrato completo**.

## A. S6: alcance del error y diagnóstico del prompt

### No son cuatro planos: son veinte

`B1C01_S6.escena` declara correctamente título «Solmire», arboleda, Miguel como único personaje y párrafos ES/EN 33–35. Esos párrafos contienen fresno, estanque, espada, silencio del hueco al verla, mano temblorosa y desaparición de la arboleda al tocar la empuñadura.

En cambio:

- `B1C01_S6_P01.accion_principal`: «El rostro de Miguel se afloja un instante al reconocer a Gabriel como hermano y no como emisario; la mirada se pierde hacia dentro».
- P02 entra al recuerdo; P03 hunde la fortaleza; P04 muestra el ala quemada; P05 incorpora a Gabriel con bastón.
- P06–P17 representan cauterización y recuperación durante las tres noches.
- P18–P20 regresan al desierto y muestran el ala intacta.

**Ninguno de los veinte planos adapta el hallazgo de Solmire.** Es contenido del final del encuentro/flashback/regreso, principalmente párrafos 16–22. Cambiar el ID o el rango de S6 para acomodarlo, como sugiere su propio `control_calidad`, sería la reparación equivocada: dejaría sin adaptar el cierre del capítulo y duplicaría otras escenas. Hay que regenerar Dirección de S6 desde 33–35 e invalidar sus derivados.

### Reconstrucción y límites de procedencia

El apéndice incluye el prompt completo reconstruido mediante `direccionPrompt()` y el objeto real `escenas[5].escena`. Las rutas ES/EN se sustituyen por las del capítulo auditado. **Es una reconstrucción del script disponible, no una transcripción certificada de la llamada histórica:** no se dispone aquí de un registro inmutable del prompt enviado, de `args` y de la revisión del script usada en esa llamada. Esta cautela importa porque las salidas incumplen un campo que el script actual declara obligatorio.

El prompt **no contiene el texto de los párrafos**. Contiene rutas y la orden:

> Lee los parrafos 33-35 de Libro1/ES/01_A_Wound_in_the_World.md (texto de referencia) y su equivalente EN, parrafos 33-35 de Libro1/EN/01_A_Wound_in_the_World.md, para el texto exacto y cualquier dialogo textual.

El código no hace extracción de párrafos ni verificación de qué contenido leyó el agente. Sí suministra el JSON correcto y una duración de 150 segundos. No hay en `direccionPrompt` un error visible de índice que sustituya S6 por S3. `stageDireccion` conserva `{ escena, planos: r.planos }`; eso no permite excluir errores del runtime `pipeline()`, cuya implementación no está en el archivo, pero tampoco los demuestra.

### Dos explicaciones concretas, no una atribución causal segura

**1. Contaminación por canon narrativo: plausible.** El bloque global comienza diciendo que las notas «tienen PRIORIDAD sobre cualquier imagen o texto de referencia que las contradiga». Incluye:

> durante el flashback, Miguel SI tiene el ala quemada/rota, y se puede y se debe mostrar una curacion visual progresiva y visible mientras Gabriel la cauteriza con su luz a lo largo de las tres noches.

Y Dirección lo repite:

> Si esta escena es el flashback de las Puertas de Onice, incluye planos que muestren la curacion visual progresiva del ala de Miguel a lo largo de las tres noches (regla de canon de arriba).

Es material narrativo muy específico y ajeno a S6, repetido y dotado de autoridad. La frase final «No inventes personajes ni hechos que no esten en el texto leido **o en el canon**» tampoco exige pertenencia al pasaje asignado. Eso facilita usar un hecho canónico verdadero en la escena equivocada. Sin embargo, la condición «Si esta escena es el flashback» es explícita y S6 no lo es: el prompt no ordena literalmente sustituir Solmire por Ónice. No puedo demostrar el mecanismo interno del error solo por semejanza temática.

**2. Confusión línea/párrafo: indicio especialmente específico.** En el archivo ES real:

| Unidad | Texto/contenido |
| --- | --- |
| Línea 33, párrafo 16 | «El cambio de emisario a hermano lo golpeó más hondo que cualquier orden.» |
| Línea 35, párrafo 17 | «Ya había vivido una versión de este momento. Por eso no podía obligarse a dar la vuelta.» |
| Línea 37, párrafo 18 | Comienza el recuerdo de las Puertas de Ónice. |
| Párrafos 33–35, líneas 67, 69 y 71 | Hallazgo de Solmire, mano y desaparición. |

El arranque de S6 reproduce precisamente el contenido de la **línea 33**, no del párrafo 33. Una lectura por números de línea seguida de ampliación al flashback vecino explicaría P01–P03 de forma muy concreta; CANON_NOTES podría haber reforzado esa ampliación. No consta la llamada de lectura histórica, por lo que esto sigue siendo una hipótesis, no un hecho confirmado. Es al menos tan importante de investigar como la contaminación semántica.

Además, S6_P01.`control_calidad.incidencias` invoca «parrafos ~23-53» de un capítulo de 35 y atribuye a 33–35 «The figure did not answer», que corresponde al párrafo 32. El diagnóstico de contenido equivocado es correcto, pero sus citas numéricas no son fiables. Hay un problema observable de anclaje a la fuente, no solo una sospecha sobre el estilo de las notas.

**Conclusión A:** confirmo el error y el riesgo del bloque global; no confirmo su causalidad exclusiva. La causa de ingeniería demostrable es que no se entrega ni valida un extracto numerado y verificable del pasaje, ni se rechaza una lista de planos incompatible con su escena.

## B. Bloqueo masivo: medición y causa

| Escena | Planos | Con continuidad estructurada | `continuidad: null` y «Sin datos…» | Bloqueados con diagnóstico | Marcados listos |
| --- | ---: | ---: | ---: | ---: | ---: |
| S1 | 20 | 5 (P01–P05) | 15 | 1 | 4 |
| S2 | 20 | 1 (S2-P01) | 19 | 0 | 1 |
| S3 | 18 | 1 (P01) | 17 | 0 | 1 |
| S4 | 27 | 1 (S4_01) | 26 | 1 | 0 |
| S5 | 26 | 4 (P01–P04) | 22 | 0 | 4 |
| S6 | 20 | 2 (P01–P02) | 18 | 2 | 0 |
| **Total** | **131** | **14** | **117** | **4** | **10** |

Por tanto, **117 de los 121 bloqueos (96,7 %) son ausencia de datos**, no contradicciones de continuidad detectadas. Los cuatro restantes son S1_P04 (referencia del peto agrietado), S4_01 (referencia del ala y conflicto de entrada), S6_P01/P02 (fuente narrativa incorrecta). No todos son saltos físicos: también hay problemas de referencias y de fidelidad.

La cadena causal inmediata está en `stageContinuidad`:

```js
const c = cont ? cont.planos_finales.find((x) => x.id_plano === p.id_plano) : null
// ...
continuidad: c || null,
listo_para_generar: c ? c.listo_para_generar : false,
motivo_bloqueo: c ? c.motivo_bloqueo || '' : 'Sin datos de continuidad generados'
```

Ese mensaje lo escribe el ensamblador, **no el supervisor tras examinar un raccord**. Puede significar respuesta ausente o ID no encontrado; el JSON final por sí solo no distingue respuesta corta, pérdida en extracción, IDs distintos o truncamiento. No existe comprobación de igualdad entre el conjunto de IDs solicitado y el recibido, ni reintento para cubrir faltantes. `CONTINUIDAD_SCHEMA.planos_finales` permite cualquier longitud, incluso cero: carece de una cardinalidad adaptada al lote.

### Evidencia adicional: hay salidas extensas en disco

En el mismo directorio temporal del script encontré:

| Archivo intermedio | Escena identificada por sus IDs | Registros con ambos estados objeto | Tamaño en bytes |
| --- | --- | ---: | ---: |
| `planos_s1.json` | S1 | 20/20 | 222461 |
| `partial.json` | S2 | 20/20 | 331931 |
| `planos_compact.json` | S3 | 18/18 | 288133 |
| `s4_final_output.json` (`planos_finales`) | S4 | 27/27 | 705987 |
| `final_output.txt` (array JSON) | S5 | 26/26 | 496613 |

Los conjuntos de IDs coinciden exactamente con los de sus escenas finales. Además, **ocho de los doce bloques retenidos de S1–S5 son idénticos como objetos** a sus homólogos intermedios: S1_P01/P02/P03/P05, S2-P01 y S5_P01/P02/P03. S1_P04, S3_P01, S4_01 y S5_P04 presentan diferencias; no afirmo que todos esos archivos sean el objeto exacto devuelto al runtime, ni que cumplan el contrato.

Esto cambia el diagnóstico: hay evidencia de trabajo estructurado para escenas enteras que **no llegó íntegro a la entrega**. Debe investigarse primero el paso archivo de trabajo → respuesta final estructurada → valor devuelto por `agent()` → ensamblado. No basta con decir que el agente «no completó la continuidad». Los archivos podrían ser revisiones intermedias; sin trazas no puedo localizar el punto exacto de pérdida.

El volumen sí es preocupante: los bloques conservados ocupan aproximadamente **7.398–22.616 caracteres cada uno** serializados con `ensure_ascii=False`; copiar dos estados completos por plano produce salidas enormes. Eso hace plausibles límites de respuesta, extracción o serialización, además del coste de razonamiento. Pero **no hay evidencia de `finish_reason`, límite de tokens o error de parser que confirme una causa concreta**. Tampoco hay relación monótona simple: S5 retiene cuatro planos de 26, S3 uno de 18.

**Conclusión B:** regresión de entrega/cobertura confirmada; causa exclusivamente «el modelo no pudo completar el esquema» no confirmada y debilitada por los intermedios. El bloqueo por ausencia es una protección correcta; presentar esos 117 casos como mejora de calidad sería incorrecto.

## C. Calidad de los pocos bloques conservados frente a v1

### Mejoras reales, pero parciales

En v1 los estados eran cadenas; ahora los 14 objetos contienen personajes, anatomía por lado, inventario, entorno y cámara. S1_P03 conserva las diez partes de Miguel físicamente presentes aunque queden fuera del detalle de pies. S5_P02 conserva a Miguel y al Sentinel fuera de campo; la anatomía del Sentinel representa su forma de niebla, sin piernas/pies físicos definidos. Esto es más verificable que la prosa libre.

`estado_salida_observado_pendiente: true` y `control_calidad.resultado: pendiente` distinguen planificación y vídeo. El filtro de Traducción excluye los 121 bloqueados: los diez prompts corresponden a los diez IDs marcados listos. Sus referencias adjuntas existen y ninguna lista supera tres archivos. S2-P01 describe explícitamente a Gabriel sin armadura. El rediseño del Sentinel aparece en Dirección/VFX de S5, aunque los planos de su revelación no llegaron a tener continuidad estructurada.

### El «contrato completo» todavía no existe

**0/14** bloques contienen `id_escena`, `fuente_narrativa`, `generacion`, `estado_salida_observado` o `frame_final`. Tampoco existen `enlace.frame_heredado` ni `control_calidad.evidencias`. `version_esquema` solo aparece en 12/14; hay 11/14 con `id_plano_anterior` y `version_anterior`, y se usan cadenas de texto para algunos primeros planos en lugar de `null` justificado.

El propio esquema omite varios de esos campos, hace opcionales otros que el contrato requiere (`cambios_autorizados`, `vestuario_oculto`, metadatos de versión, campos de cámara/entorno…) y cambia mapas por listas sin una adaptación explícita de versión. El booleano de observación pendiente y `frame_final_previsto` son útiles, pero **no sustituyen los campos reales inicializados a `null`** que exige el documento 18. Ninguno de los catorce cumple literalmente todo el contrato.

### Fallos concretos dentro de los datos disponibles

- **S1_P02 → S1_P03:** P02 sale con `objetos_escena` incluyendo `esquirlas_vidrio_paso`; P03 entra con inventario vacío y `entorno.estado_decorado: "Vidrio intacto en el punto exacto de apoyo, aun sin romperse"`. Su enlace dice «mismo instante de la zancada»; su salida crea `fragmentos_vidrio_p03`. No se define otro apoyo ni un retroceso temporal autorizado. Se vuelve a romper una superficie ya rota y se pierde la identidad del residuo. Ambos están listos; `cambios_autorizados` está vacío.
- **S1_P04 bloqueado → S1_P05 listo:** P05 declara «Continuacion directa del rostro revelado al cierre del tilt de P04». El ensamblador no propaga el bloqueo. Su traductor decide construir una imagen independiente y dice «no se usa ni se menciona el plano anterior, bloqueado y fuera de este lote». No actualiza el enlace contractual ni aprueba el nuevo arranque: el filtrado altera implícitamente la cadena.
- **S5_P01–P04:** `vestuario_visible` impone «Peto sin grieta… Sin daño ni suciedad del desierto», frente al peto agrietado del capítulo y S1/S2. Es un reinicio a la referencia base, no una reparación autorizada. Se exporta literalmente al prompt de S5_P01.
- **S5_P03:** la incidencia sobre el pie izquierdo afirma que su fase no se fija porque está fuera de cuadro y «se retomará con datos propios» cuando sea visible. Eso debilita precisamente la persistencia requerida: ocultación no autoriza inventar la fase al reaparecer. También hay sol de mediodía en S5_P01 frente a «Sol rasante y bajo del desierto» en S5_P03, sin elipsis declarada.
- **S6_P01 → P02:** aunque bloqueados correctamente, P02 elimina a Gabriel y ambos objetos del estado (`personajes` solo Miguel; `objetos_escena: []`) mientras su enlace dice que Gabriel «permanece presente sin cambios». No es un contrato persistente completo.
- Persisten abreviaciones prohibidas: S5_P04.`estado_salida_previsto.entorno.luz` y `.clima` dicen «Sin cambio»; S1_P04 termina con `estado_decorado: "Sin cambios."`.

### Restricciones negativas: el campo no se entregó

**`restricciones_negativas` aparece en 0/14 objetos de continuidad, y en ningún plano final.** No hay casos en los que evaluar su buen uso como campo. Es especialmente grave porque está en `CONTINUIDAD_SCHEMA.required` del script disponible: las salidas no superan ese esquema. Eso requiere averiguar si faltó validación efectiva o si la revisión de script ejecutada era otra; no se puede asumir validación estricta solo por pasar `{ schema }` al agente.

Sí hay negaciones útiles en los prompts de S1_P01/P02 y S5_P01/P04: ausencia de arma/vaina, edificios, daño del ala y figuras adicionales. Son aciertos del texto final, **no evidencia de que haya funcionado el transporte del nuevo campo**. S2-P01 conserva manos vacías pero no formula expresamente la prohibición completa de arma/vaina en cadera/espalda de Miguel. No hay aplicación uniforme.

Algunas lecciones de la prueba de Flow siguen incumplidas: los cuatro prompts de S1 y S2-P01 contienen etiquetas `[ENCUADRE Y CÁMARA]`, `[ACCIÓN]`, `[CONTINUIDAD Y AUDIO]`; S2-P01 incluso `Vfx principal:`. S1_P01/P02/P03, declarados `idioma: ES`, insertan cláusulas completas en inglés («Absolutely no buildings…», «No buildings, no ruins…»). S5_P03 solicita Ingredients de 6 s y S5_P02 de 7 s, sin resolver generación/recorte según la matriz de la guía local. Es evaluación contra los documentos entregados, no una comprobación actual de la interfaz de Flow.

**Conclusión C:** mejor representación y bloqueo local; calidad semántica mixta, persistencia todavía defectuosa y cobertura mucho peor. Diez flags `true` no equivalen a diez planos listos para generación encadenada.

## D. CANON_NOTES y errores de alcance entre escenas

**Sí recomiendo separar canon de identidad y reglas narrativas con alcance explícito.** No hace falta cambiar decisiones del autor: hay que aplicarlas en el tiempo y escena correctos.

- Identidad visual por personaje presente/activo: Gabriel sin armadura y bastón en la mano fijada; Sentinel de niebla; Miguel sin arma/vaina añadida, conservando los objetos que autorice la acción. No convertir «sin arma portada» en «no puede haber una espada en la escena de Solmire».
- S3: regla de progresión de la curación, con su estado de entrada/salida autorizado.
- S4: regla breve de entrada al presente, «alas intactas, sin VFX de curación». No volver a narrar tres noches de cauterización como material que deba representarse.
- Resto de escenas presentes: alas intactas como estado local, sin biografía del daño ni instrucciones de mostrar el flashback.

La premisa «todos los agentes» no es literal: `luzPrompt` no interpola CANON_NOTES; `qaPrompt` tampoco lo incluye completo. Sí lo reciben Segmentación, Dirección, VFX, Continuidad y Traducción. Luz hereda las acciones ya contaminadas. Dirección recibe además la repetición específica del flashback. Limitar esas notas es recomendable, pero insuficiente sin verificación de fuente.

Hay otros fallos de alcance en v2: S2-P13 ya muestra la fortaleza y los siguientes planos continúan el recuerdo fuera de su rango 10–17; S3_P18 ya ejecuta el retorno/mandíbula del párrafo 22; S4_01 vuelve a cerrar un ala cuya curación S3_P11/P15 ya daba terminada. Son fallos editoriales observables aunque sus contratos falten. S1 no adapta en sus acciones el giro del párrafo 10 y S2 arranca directamente con Gabriel: el resumen de S1 anticipa ese beat sin que el reparto de planos lo asegure.

En S6 hay además una contradicción **anterior a Dirección**: `escena.resumen` sitúa el silencio del hueco «en el instante en que la ve», pero `estado_canon_entrada[0].notas` dice «sigue activo hasta el contacto con la espada». El capítulo fija ver, no tocar. Incluso regenerando los planos correctos, ese estado inicial debe corregirse a partir del texto.

## Segunda opinión sobre el QA automático

Acierta al detectar datos ausentes, S6 incorrecta, vestuario reiniciado y conflicto de S4. Pero no merece aceptación literal:

1. Compara «último plano con datos» con primera entrada de otra escena, saltándose 15–26 planos. Eso permite identificar un hueco, **no demostrar que no haya un alto, giro o desplazamiento durante los planos omitidos**. La afirmación S1_P05 → S2-P01 de salto de pose «sin ningún plano intermedio» es incorrecta: existen P06–P20, aunque sin contrato.
2. Marca S2→S3 `coherente: true` pese a carecer de la salida final de S2. Debe ser `no_verificable` con observación de que el flashback autoriza conceptualmente el cambio temporal.
3. Llama a S4_01 primer plano del presente. Dirección lo declara «instante final del recuerdo» y S4_03 es el primer presente inequívoco. El fallo demostrado es reinsertar/repetir el cierre del flashback después del retorno de S3 y contradecir la entrada de S4; no se ha demostrado un ala quemada **en el presente de S4_03**.
4. Asegura que la grieta de S4_01 es «consistente con S1/S2/S3», pero S3_P01 dice «intacta, sin grieta». Que la campaña origine el daño no localiza automáticamente el momento de aparición en la secuencia.
5. En S6 repite la numeración imposible «~23-53» y la orientación de reparación equivocada del supervisor.

`qaPrompt` parte de que «la continuidad dentro de cada escena ya se resolvio». Esa premisa es falsa para 117 planos sin datos. Además, el QA se ejecuta **después** de Traducción y su resultado solo se devuelve: no invalida los flags ni retira prompts. Detectar un fallo al final no equivale a impedir su exportación.

## E. Recomendaciones de ingeniería antes de v3

Prioridad 0, antes de otro capítulo completo:

1. **Anclar la fuente con código.** Extraer párrafos una sola vez, excluir el título y entregar texto literal ES/EN numerado con IDs estables, rango, hash y versión del capítulo. Conservar el prompt efectivo de cada llamada. Dirección debe devolver IDs de párrafo/beat por plano. Rechazar personajes, escenario, tiempo y acontecimientos fuera del pasaje salvo adaptación registrada. S6 constituye una prueba de regresión directa; también distinguir línea 33 de párrafo 33.
2. **Auditar el canal de entrega.** Conservar respuesta bruta, salida estructurada, archivos producidos, número de registros, IDs y diagnóstico de finalización. Comparar los intermedios hallados con el valor real devuelto por `agent()`. Si el agente escribe un JSON validable, cargarlo por archivo; no obligarlo a copiar cientos de kilobytes de nuevo en una respuesta final ni aceptar silenciosamente un prefijo.
3. **Lotes pequeños y reanudables de Continuidad.** Empezar con 1–3 planos, ajustar por número de personajes y presupuesto medido, pasar la salida validada del lote anterior y el inventario persistente. Paralelizar escenas independientes si procede, pero mantener la herencia entre lotes consecutivos. El tamaño propuesto es inicial, no un umbral demostrado por este piloto.
4. **Reducir repetición durante el cálculo, expandir en la entrega.** Conservar estado base y cambios tipados; materializar determinísticamente `estado_entrada` y `estado_salida_previsto` completos antes de exportar. El documento 18 ya ejemplifica reutilización con expansión. Un delta interno no autoriza enviar «sin cambios» al generador.
5. **Validación determinista obligatoria.** Esquema versionado completo; cardinalidad exacta por lote; igualdad de conjuntos de IDs, sin duplicados ni ajenos; referencias existentes; anatomía aplicable completa; objetos sujetados presentes en inventario; negativos obligatorios; estados reales/frame inicialmente `null`; coherencia de campos entre Dirección/Luz/VFX/Continuidad. Rechazar o reintentar faltantes con error de ingeniería explícito. Separar `ERROR_ENTREGA`, `CONTRADICCION_NARRATIVA`, `CONTRADICCION_CONTINUIDAD` y `REFERENCIA_PENDIENTE`.
6. **Separar aprobación de planificación y habilitación real.** Un plano puede estar preparado para traducción sin poder generarse aún. La continuación solo queda habilitada cuando tiene antecesor, toma/corte y frame aprobados. Propagar bloqueos por dependencias. S1_P05 no puede saltarse P04 por decisión unilateral del traductor.
7. **QA narrativo antes de Luz/VFX y QA de estados antes de exportar.** Usar tres resultados: válido, inválido y no verificable. Mantener la línea temporal presente/flashback y recuperar el estado correspondiente. No usar el último registro disponible como si fuera el cierre real. Aplicar el resultado del QA a las salidas, no solo adjuntarlo como comentario.
8. **Validador del prompt final.** Sin etiquetas organizativas, idioma consistente, negaciones preservadas, operación/duración compatibles con la guía del proyecto y referencias con función clara. Las negaciones no deben prohibir objetos narrativos necesarios: Solmire sigue clavada en el fresno hasta el contacto autorizado.

Pruebas mínimas de aceptación: S6 conserva exclusivamente los beats 33–35; un lote incompleto no se presenta como completado; omitir `restricciones_negativas` falla validación; un plano bloqueado invalida continuaciones dependientes; el cambio de encuadre conserva inventario y partes ocultas; S3→S4 no repite curación ni arrastra daño al presente. Solo después, ensayo corto con clips y revisión íntegra de cada toma conforme al documento 18.

**Decisión:** conservar el enfoque estructurado y el cierre preventivo ante datos ausentes, pero reparar fuente, extracción/entrega, validación y dependencias antes de v3. V1 tenía problemas reales; v2 no los supera como producto utilizable y añade la pérdida completa del desenlace. No procede resolverlo relajando bloqueos ni reabriendo canon ya decidido.

## Apéndice: prompt reconstruido de Dirección para S6

Reproducido del script disponible y del JSON de escena; rutas de capítulo sustituidas como se indica en A. No contiene el texto narrativo del capítulo, solo la instrucción de leerlo.

```text
Eres el agente de Direccion/Previz del pipeline cinematografico de "Las Cronicas del Juicio".
Lee primero content/craft/16_camara_y_luz.md (vocabulario de camara) y content/craft/17_vfx_y_fisica_entorno.md (tecnica de capas primer plano/fondo simultaneas).

NOTAS DE CANON YA RESUELTAS POR EL AUTOR (2026-09-18) - tienen PRIORIDAD sobre cualquier imagen o texto de referencia que las contradiga, incluido lo que digan los README de character_library si no se han actualizado:
- Gabriel: SIN armadura ni peto metalico, nunca, en ninguna escena. Tunica azul y plata con hombreras de tela ribeteadas en plata. Bastón "Vox Aeternum" en la mano derecha. (character_library/angeles/Gabriel/README.md ya esta corregido para coincidir con esto).
- Pewter Sentinel (guardian de la arboleda): usar el diseno de niebla/vapor tal cual character_library/otros/Pewter Sentinel/canonical/ (ojos blancos brillantes, rostro casi sin rasgos entre la bruma, cuerpo que se disuelve en vapor sin piernas ni pies definidos, flota ligeramente sobre el suelo, zarcillos de peltre y hojas plateadas fusionados en los hombros) en TODAS sus apariciones, capitulo 1 incluido -aunque el texto del capitulo describa una figura solida de metal palido con "un solo rostro liso". No adaptes visualmente la descripcion solida del texto; si hace falta, adapta la ACCION narrada (que gira, que observa, que no bloquea el paso) al cuerpo de niebla, no al reves.
- Ala de Miguel en el flashback de las Puertas de Onice (escena de las tres noches con Gabriel cauterizando el ala): durante el flashback, Miguel SI tiene el ala quemada/rota, y se puede y se debe mostrar una curacion visual progresiva y visible mientras Gabriel la cauteriza con su luz a lo largo de las tres noches. Pero al VOLVER del flashback al presente (primer plano de la escena siguiente que ocurre en el presente), el ala de Miguel debe estar intacta, SIN dano ni marca de quemadura visible - no arrastres un estado de "cicatrizandose" o "recien cerrada" al presente, el ala del presente en el capitulo 1 esta sana.
- Miguel NUNCA lleva arma, vaina ni objeto en la cadera o la espalda (character_library/angeles/Miguel/README.md). En una prueba real de generacion en Flow se coló una espada alucinada pese a esto: cualquier plano de Miguel debe declarar explicitamente "sin arma" en restricciones_negativas.

VERIFICADO POR EL AUTOR EN GOOGLE FLOW (prueba real, 2026-09-18) - aplica a Direccion, Continuidad y Traduccion:
- Evitar planos de un personaje caminando DE FRENTE A CAMARA (bug real: el personaje camino hacia atras pese a "walking forward, facing camera", persistio incluso insistiendo). Para ciclos de marcha, usar perfil/lateral o camara seguendo por detras, con direccion explicita ("from left to right", "seen from behind").
- Preferir UNA SOLA referencia de imagen por plano de continuacion (el ultimo frame aprobado del plano anterior). Combinar varias referencias a la vez (cuerpo completo + ultimo frame + textura) causo movimiento estatico/incorrecto en una prueba real.
- El modo "imagen de inicio + imagen de fin" es poco fiable para movimiento continuo (en una prueba real el clip se quedo casi estatico y dio un salto de corte al final en vez de interpolar) - preferir continuacion desde una sola imagen + descripcion completa de la accion en texto.
- Las restricciones negativas SI funcionan escritas directamente en el prompt normal (sin campo dedicado): ej. "Absolutely NO large buildings, NO Greek columns, NO temple walls. Open desert landscape only." corrigio una alucinacion de fondo real.
- Nunca dejar etiquetas de guion (nombres de escena/plano, "Audio de fondo", etc.) dentro del texto final del prompt - el modelo intenta renderizarlas como letras flotantes en el vídeo (fallo real observado).
- Un salto de continuidad puede ocurrir DENTRO de un mismo clip de 8s, no solo entre planos (ej. alas ausentes en el fotograma 0 y presentes en el segundo 4 del mismo clip) - no basta revisar primer/ultimo fotograma.

Escena a desglosar (JSON): {"id_escena":"B1C01_S6","titulo":"Solmire","resumen":"En el corazón de la arboleda, ante el gran fresno de corteza como lava enfriada junto a un estanque de luz estática, Miguel encuentra clavada una espada que no es metal forjado sino luz viva con peso, filo y forma propios. En el instante en que la ve, el vacío bajo su pecho enmudece: reconoce el nombre Solmire no como un recuerdo sino como una ley que siempre estuvo ahí — eso es lo que le fue arrebatado. Alza la mano temblorosa hacia la empuñadura, dudando si al tocarla seguirá siendo el General de la Hueste o se convertirá en otra cosa. En el instante en que su piel toca el pomo, la arboleda desaparece.","localizacion":"Corazón de la Arboleda — el gran fresno junto al estanque de luz estática","personajes":["Miguel"],"parrafos_en":{"desde":33,"hasta":35},"parrafos_es":{"desde":33,"hasta":35},"duracion_objetivo_seg":150,"estado_canon_entrada":[{"id_personaje":"Miguel","forma":"celestial","heridas":[],"objetos":[],"notas":"Alas intactas y sanas, sin heridas visibles. El 'hueco' bajo el esternón sigue activo hasta el contacto con la espada, que lo silencia por completo. Mano temblorosa al alzarla; por un latido el propio nombre 'Miguel' se siente como un título prestado."}],"requiere_aprobacion_autor":false}

Lee los parrafos 33-35 de Libro1/ES/01_A_Wound_in_the_World.md (texto de referencia) y su equivalente EN, parrafos 33-35 de Libro1/EN/01_A_Wound_in_the_World.md, para el texto exacto y cualquier dialogo textual.

Divide esta escena en una secuencia de PLANOS (shot list) que sumen aproximadamente 150 segundos en total. Los clips individuales de Flow duran hasta 8s cada uno (ver content/craft/14_google_flow.md) asi que planifica varios planos por escena, nunca un plano unico salvo que la escena sea muy breve.

Para cada plano indica: tipo de plano, angulo, movimiento de camara (vocabulario del doc 16), encuadre inicial y final, personajes presentes, la ACCION PRINCIPAL (lo que ocupa el foco) y, cuando corresponda, una ACCION DE FONDO/SECUNDARIA simultanea (un evento que ocurre a la vez pero no es el foco, siguiendo la tecnica de capas del doc 17). Si esta escena es el flashback de las Puertas de Onice, incluye planos que muestren la curacion visual progresiva del ala de Miguel a lo largo de las tres noches (regla de canon de arriba). Si hay dialogo textual del capitulo en ese plano, copialo EXACTO (nunca lo parafrasees ni resumas) en dialogo_es, y su equivalente EN en dialogo_en -las replicas de dialogo son intocables, regla no negociable del proyecto-.

No inventes personajes ni hechos que no esten en el texto leido o en el canon.
```

Script examinado: `/tmp/claude-1000/-home-sszark-Escritorio-proyectos-novelas--claude-worktrees-cinematographic-skill-c4d6b6/8f911d88-29ac-45f3-8cce-d5bee1c755cd/scratchpad/workflow_cinematografia.js`. SHA-256 del archivo leído: `0923465abe1be5f6e6268fc981e93c494995d737164ea6b08a30dd29e2789ec4`. Los archivos intermedios citados en B están en ese mismo directorio.
