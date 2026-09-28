# 14 — Google Flow: prompts de plano y continuidad (2026-09-16)
**BORRADOR — pendiente de aprobación del autor**

Encargo: convertir fichas de plano de *Las Crónicas del Juicio / Chronicles of the Sundering Judgment* en instrucciones ejecutables en Google Flow, usando las referencias existentes de `character_library/`. El problema que hay que evitar: un personaje pierde una mano y la recupera en el plano siguiente; una herida, una prenda o un objeto cambia sin que lo cambie la historia.

**Regla de trabajo: cada plano recibe su identidad, su estado físico y su estado de salida.** Una cara reconocible no basta. La continuidad incluye anatomía, vestuario, objetos, posiciones, luz y consecuencias de la acción.

Investigación web cerrada el 2026-09-16, con más de treinta consultas en inglés y español: ayuda oficial, publicaciones de Google, foros, Reddit, X y búsquedas de tutoriales de YouTube de 2025–2026. No se han ejecutado generaciones de prueba. Las capacidades citadas son documentales; las reglas de producción y los ejemplos propios se identifican como propuestas. La consulta de vídeos tuvo acceso parcial: descripciones, capítulos y algunos prompts publicados, sin visionado completo ni transcripción íntegra.

## Qué se puede pedir a Flow y qué hay que comprobar

Flow es la interfaz; Veo es uno de sus modelos. La ayuda actual también incluye Gemini Omni. **Una demostración hecha en Flow con Omni no demuestra que Veo admita la misma operación.** Tampoco se trasladan automáticamente a Flow los parámetros de Gemini API o Vertex AI. Esta guía se centra en Veo. [Modelos de Flow](https://support.google.com/flow/answer/16352836?hl=en).

La matriz oficial consultada indica:

| Modelo en Flow | Texto / fotograma inicial / inicial y final | Ingredients to Video | Extend |
|---|---|---|---|
| Veo 3.1 Lite | 4, 6 u 8 s | 8 s | Sí; recibe clips Veo 3.1 de 8 s |
| Veo 3.1 Fast | 4, 6 u 8 s | 8 s | No como modelo ejecutor |
| Veo 3.1 Quality | 4, 6 u 8 s | No | No como modelo ejecutor |

Los tres admiten las dos orientaciones documentadas. Un clip de 8 s generado con Fast o Quality puede servir de origen para Extend, pero la matriz exige ejecutar la extensión con Lite. **Revisar el selector antes de preparar una tanda.** [Compatibilidad oficial](https://support.google.com/flow/answer/16352836?hl=en).

Otros límites que afectan a la ficha:

- **Duración:** 8 s es el máximo de una generación base de Veo en la matriz anterior. No equivale al máximo de una escena montada. Los 10 s de la ayuda actual corresponden a Omni.
- **Formato:** 16:9 horizontal o 9:16 vertical. Google anunció Ingredients vertical en enero de 2026. No dar por hecho 1:1 o 21:9 en vídeo Veo porque estén disponibles para imágenes. [Actualización de Veo 3.1](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video/).
- **Resolución:** Google confirma reescalado a 1080p y 4K en Flow. No llamarlo «4K nativo». La resolución base disponible por modo y cuenta debe comprobarse en el selector y en el archivo descargado; **720p como valor universal actual de todos los modos Veo en Flow: no confirmado / puede haber cambiado**. Las resoluciones de una API no prueban las de esta interfaz. [Anuncio oficial del reescalado](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video/).
- **Referencias:** Google documentó hasta **tres ingredientes por prompt** en junio de 2025. Es el presupuesto conservador para preparar Veo; la ayuda actual de carga no publica un máximo numérico. Un límite superior en la interfaz actual: **no confirmado / puede haber cambiado**. No confundir ingredientes de una generación con imágenes almacenadas en un perfil. [Tres ingredientes](https://blog.google/innovation-and-ai/products/flow-video-tips/).
- **Extensión acumulada:** Google anunció tomas de un minuto o más mediante Extend; eso no establece un máximo vigente. El incremento exacto por extensión y el techo acumulado actual de Flow: **no confirmado / puede haber cambiado**. No importar cifras de la API. [Anuncio de Extend con Veo 3.1](https://blog.google/innovation-and-ai/products/veo-updates-flow/).

### Créditos públicos: presupuestar por resultado

La ayuda consultada publica 50 créditos diarios; además, Plus recibe 200 mensuales, Pro 1.000 y las modalidades Ultra denominadas «$100» y «$200», 10.000 y 25.000. No son precios locales en euros. El crédito diario y el mensual no utilizado no se acumulan.

| Operación | Sin Ultra | Ultra |
|---|---:|---:|
| Veo 3.1 Lite | 10 | 5 |
| Veo 3.1 Fast | 20 | 10 |
| Veo 3.1 Quality | 100 | 100 |
| Reescalado 1080p | 0 con Plus/Pro; no disponible sin suscripción | 0 |
| Reescalado 4K | No disponible | 50 |

Se cobra por generación, no por pulsación: dos resultados consumen dos generaciones. Hay restricciones de demanda para cuentas sin suscripción. Las cifras pueden cambiar; consultar el coste mostrado antes de enviar. [Créditos de Flow](https://support.google.com/flow/answer/16526234?hl=en).

**Contradicción documental:** la tabla de precios enumera Extend bajo Fast y Quality, pero la matriz de funciones lo restringe a Lite; precios también enumera Quality de 8 s donde compatibilidad incluye 4/6/8. No interpretar una fila de facturación como permiso funcional. Para producción, comprobar la operación en la sesión y registrar el modelo efectivo. [Precios](https://support.google.com/flow/answer/16526234?hl=en) y [funciones](https://support.google.com/flow/answer/16352836?hl=en).

## Referencias: identidad estable, estado variable

En el proyecto, seleccionar vídeo e ingredientes; subir o elegir las imágenes. La ayuda permite buscar recursos cargados mediante `@`. El texto debe explicar qué aporta cada referencia. Google recomienda sujetos sobre fondo limpio, referencias compatibles y ausencia de personas accidentales en el decorado. [Crear vídeos y añadir referencias](https://support.google.com/flow/answer/16353334?hl=en).

Protocolo propuesto para la trilogía:

1. **Resolver la identidad existente.** Elegir la imagen de `character_library/` que corresponde a ese personaje y a esa forma. No mezclar forma humana y celestial como si fueran vistas del mismo estado. No hacer casting nuevo.
2. **Resolver el momento narrativo.** La ficha debe decir qué heridas, pérdidas, suciedad, prendas y objetos siguen presentes. Una referencia anterior al daño puede contradecir el plano aunque la cara sea correcta.
3. **Asignar una función a cada imagen.** Ejemplo de reparto de tres entradas: personaje A, personaje B y lugar. Si un objeto es decisivo, decidir qué referencia sustituye o preparar previamente una composición aprobada con los elementos existentes.
4. **No alimentar estados incompatibles.** Si la imagen muestra dos manos y la ficha exige una amputación, no confiar en que una frase gane a la imagen. Solicitar una referencia del estado correcto o preparar y revisar un fotograma de escena derivado de los recursos aprobados. No modificar la biblioteca canónica durante esta tarea.
5. **Repetir el bloque de continuidad.** Copiarlo sin reformulaciones entre planos contiguos; cambiar solamente los campos que la acción modifica. Google recomienda repetir detalles esenciales al preparar prompts sucesivos. [Consejos oficiales](https://blog.google/innovation-and-ai/products/flow-video-tips/).

Una ruta local escrita en el prompt **no sube una imagen**. `@Personaje` solo sirve si el recurso correspondiente está cargado y seleccionado; un nombre inventado no crea un vínculo. Entregar al operador la correspondencia entre ruta, recurso de Flow y función visual.

**Mano ausente, mano oculta y mano fuera de cuadro son estados distintos.** Si existe pero no se ve, no describirla como ausente. Si falta, especificar lado anatómico, punto de terminación visible y cobertura que realmente consten en la ficha. Nunca añadir «cinco dedos en cada mano» a un personaje amputado.

## Elegir la operación según el enlace entre planos

| Necesidad | Operación propuesta | Información que recibe |
|---|---|---|
| Nuevo plano; conservar identidad con otro encuadre | Ingredients to Video | Referencias y estado completo del plano |
| Iniciar en una composición concreta | Frames to Video, inicio | Fotograma aprobado y movimiento posterior |
| Llegar también a una composición concreta | Frames to Video, inicio y final | Dos imágenes compatibles y recorrido entre ellas |
| Prolongar la misma toma | Extend | Clip Veo compatible y continuación de la acción |
| Contraplano con corte | Nueva generación y montaje | Referencias de identidad y nueva composición que respete el eje |

Frames permite cargar inicio y final y describir lo que ocurre entre ambos. Ingredients aporta referencias; no fija por sí solo el primer fotograma. La ayuda no confirma todas las combinaciones simultáneas de ingredientes y frames en Veo: no entregar una configuración híbrida sin comprobarla. [Operaciones documentadas](https://support.google.com/flow/answer/16353334?hl=en).

### Extend: continuar la toma

Abrir el clip y elegir **Extend**; escribir qué sucede a continuación. La ayuda actual limita esta operación a vídeos generados con Veo y advierte que los clips extendidos no admiten después otros modos de edición como insertar, eliminar o cámara. [Extender vídeos](https://support.google.com/flow/answer/16935718?hl=en).

Google describe Extend como una continuación a partir de los fotogramas finales. No es equivalente a adjuntar una imagen suelta: parte del clip. [Funcionamiento descrito por Google](https://blog.google/innovation-and-ai/products/flow-video-tips/).

Procedimiento propuesto:

1. Revisar el final del clip: rostro, manos, arma, ropa, dirección y velocidad. Un error visible al final es un mal punto de partida.
2. Escribir **desde la postura final**, sin repetir la entrada ni reiniciar la acción. Si ya ha levantado un objeto, describir cómo lo mantiene o lo baja.
3. Mantener el movimiento de cámara o explicar su desaceleración. No introducir un contraplano como si fuera la prolongación de la misma toma.
4. Ver la unión a velocidad normal y después cuadro a cuadro. Comprobar también saltos de sonido y luz.
5. Rechazar la extensión si altera un hecho. No convertir un defecto generado en el nuevo estado del personaje.

### Último fotograma → primer fotograma del clip siguiente

Flow permite pausar y guardar un frame para reutilizarlo como ingrediente, inicio o final. Para esta técnica, guardarlo y asignarlo expresamente como **start frame** del siguiente clip. [Guardar fotogramas](https://support.google.com/flow/answer/16935718?hl=en).

Protocolo propuesto: elegir el último fotograma **válido y nítido** del tramo que se va a montar. Si está antes del final original, recortar el primer clip hasta él. La nueva animación debe arrancar de esa postura; conservar dirección, agarre y localización de los objetos. Revisar la velocidad del empalme: compartir una imagen no prueba continuidad de movimiento o sonido.

Para un contraplano, no usar el último frame como inicio esperando que cambie instantáneamente de cámara. Preparar otra composición coherente y unir mediante corte. Si se desea una órbita continua, los frames deben representar puntos de una trayectoria posible; entre vistas incompatibles puede aparecer una transformación o un corte imprevisto.

## Cámara: escribir una trayectoria que se pueda comprobar

Hay dos niveles. Google anunció controles de interfaz de rotación, dolly y zoom en Flow con Veo 2. Eso no demuestra que todos esos botones sigan disponibles para cada modo Veo 3.1. **Menú exacto actual por modelo: no confirmado / puede haber cambiado.** [Anuncio de controles](https://blog.google/innovation-and-ai/products/generative-media-models-io-2025/).

El otro nivel es el lenguaje del prompt. La documentación de Veo recoge este vocabulario; advierte que ciertos ángulos avanzados no tienen soporte garantizado. [Guía técnica de cámara](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide).

| Decisión | Vocabulario útil |
|---|---|
| Tamaño | `wide shot`, `full shot`, `medium shot`, `close-up`, `extreme close-up` |
| Ángulo | `eye-level`, `low-angle`, `high-angle`, `top-down`, `Dutch angle` |
| Relación | `over-the-shoulder`, `POV`, `two-shot` |
| Cámara quieta | `static shot`, `locked-off camera` |
| Giro desde un punto | `pan left/right`, `tilt up/down` |
| Desplazamiento | `dolly in/out`, `truck left/right`, `pedestal up/down` |
| Recorrido | `tracking shot`, `arc shot`, `crane shot`, `aerial shot` |
| Óptica y estabilidad | `zoom in/out`, `handheld`, `shallow depth of field`, `deep focus` |

Convención propuesta: **encuadre inicial → desplazamiento → encuadre final**, con sujeto y duración. Ejemplo propio: «Plano medio a la altura de los ojos. La cámara avanza despacio hacia A hasta un primer plano; A permanece en su sitio y mantiene la mirada hacia la derecha del encuadre».

No confundir:

- **Pan**: gira la cámara. **Truck**: se desplaza lateralmente.
- **Dolly**: se acerca físicamente. **Zoom**: cambia la focal.
- **Movimiento del actor** y **movimiento de cámara**: escribir quién ejecuta cada uno.
- **Izquierda anatómica** y **izquierda de pantalla**: la primera identifica una mano; la segunda, una posición en la imagen.

Para un movimiento complejo, indicar principio, final y elemento que permanece encuadrado. Propuesta: «La cámara describe un arco lento desde el perfil izquierdo de A hasta tres cuartos frontal; el rostro permanece en el centro y B sigue visible al fondo». Antes de ampliarlo a 180°, probar el arco corto con el mismo estado.

Las focales, grados y segundos en texto expresan intención; no son un sistema de cámara 3D con medidas verificadas. Si un botón y el texto se contradicen, corregir la configuración antes de generar. Evitar órdenes como «plano fijo con órbita» o «primer plano de ambos cuerpos enteros».

## Sintaxis: de la ficha al prompt

Google propone cámara, sujeto, acción, contexto y estilo/ambiente. También muestra diálogos entre comillas y transiciones entre frames. No publica un orden mágico que garantice obediencia. [Guía oficial de Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1).

DeepMind admite prompts cortos o detallados, descripción precisa del personaje, acciones y sonido. La precisión útil describe lo que debe aparecer y suceder. [Guía de DeepMind](https://deepmind.google/models/veo/prompt-guide/).

**Convención propuesta para este proyecto:** una generación contiene un plano y una acción principal. Es una decisión para facilitar continuidad y revisión; Veo también admite peticiones de varias acciones y Google muestra secuencias temporizadas. No tratar los timestamps como edición exacta garantizada.

### Entrada mínima del agente

```text
PLANO: identificador; plano precedente; relación: corte / continuación.
CANON: momento narrativo; forma del personaje; hechos que no pueden cambiar.
REFERENCIAS: rutas reales; recursos cargados; función de cada imagen.
ESTADO INICIAL: anatomía por lado; heridas; ropa; objetos y poseedores.
POSICIONES: ubicación, dirección de mirada, eje y posiciones en pantalla.
ACCIÓN: sujeto + verbo visible + objeto; estado que cambia.
CÁMARA: tamaño, ángulo, inicio, recorrido, final, foco.
LUZ: fuente, dirección, dureza, color y exposición que debe mantenerse.
VFX: origen, zona afectada, evolución y efecto sobre la luz.
AUDIO: ambiente; efectos; hablante; réplica exacta e idioma, si existe.
ESTADO FINAL: pose, agarres, daños y objetos al terminar.
AJUSTES: modelo, operación, duración, formato, resolución disponible, resultados.
```

Si falta un dato de canon necesario, devolver `FALTA_DATO` con el campo concreto; no inventar qué mano falta, qué arma lleva o cuándo sana. Si la ficha pide demasiadas acciones para la duración, proponer subdivisión conservando su orden y sus consecuencias.

### Salida del agente

Entregar cuatro bloques: **ajustes de interfaz**, **referencias que hay que adjuntar**, **prompt que se pegará** y **criterios de aceptación**. Los tres primeros resuelven cómo generar; el cuarto permite comprobar si ha funcionado. El esquema siguiente es editorial, no una API de Flow.

```text
[ENCUADRE Y CÁMARA]
Un único plano continuo. [Tamaño y ángulo]. La cámara [trayectoria]
desde [composición inicial] hasta [composición final].

[SUJETOS Y ESTADO]
[Recurso de A] define la identidad de A. [Recurso de B] define la de B.
A está [posición y orientación], con [anatomía, vestuario y objeto].
B está [posición y orientación], con [estado pertinente].

[ACCIÓN]
Desde esa postura, A [acción principal]. B [reacción observable].
Al terminar, [pose y ubicación de los objetos].

[ESPACIO, LUZ Y VFX]
[Lugar y referencias espaciales]. [Fuente de luz y dirección].
[VFX concreto, solo si la ficha lo requiere]. [Estilo aprobado].

[CONTINUIDAD Y AUDIO]
Durante toda la toma, [dos o tres invariantes críticos específicos].
Se oyen [sonidos]. [Hablante e idioma]: «[réplica exacta]».
```

Eliminar bloques vacíos y sustituir todos los corchetes antes de enviar. No pegar al modelo observaciones sobre costes, fuentes o dudas del agente. Usar el idioma elegido para la producción; no hay prueba aquí de que escribir todo en inglés mejore universalmente Flow. Los términos ingleses de cámara ayudan a mantener un glosario estable. Para EN/ES, mantener los mismos identificadores y traducir dirección y diálogo sin alterar los hechos.

### Lo que conviene precisar y lo que conviene quitar

| Demasiado vago o ambiguo | Reescritura propuesta |
|---|---|
| «Conserva todo» | «La daga sigue en la mano derecha de A durante toda la toma» |
| «Se nota su poder» | «Los dos guardias interrumpen su conversación y se enderezan» |
| «Cámara épica» | «La cámara asciende y descubre la fila de soldados detrás de A» |
| «Él se acerca mientras gira» | Nombrar quién camina, quién gira y hacia dónde |
| «La herida sigue» | Lugar anatómico y aspecto visible que constan en la ficha |
| «Magia espectacular» | Punto de origen, color, extensión y momento de desaparición |
| «Igual que antes» | Estado repetido y referencia efectivamente adjunta |

No añadir una lista genérica de defectos al final de todos los prompts. En la API hay técnicas de prompt negativo, pero **un campo `negativePrompt` propio de Flow: no confirmado / puede haber cambiado**. En el texto normal, describir primero el resultado visible buscado. «La manga izquierda termina cerrada a la altura de la muñeca» solo procede si ese estado es correcto en la ficha; no es una solución universal a las manos defectuosas.

En Reddit se propone elegir un estilo, un comportamiento de cámara y un beat. El autor de esa propuesta aclara que la barra de etiquetas como `/orbit` es opcional. Aprovechar la descripción cinematográfica, sin presentarla como un comando oficial ni un bloqueo de continuidad. [Propuesta comunitaria de prompts](https://www.reddit.com/r/promptingmagic/comments/1w1vkz7/the_22command_gemini_flow_cheat_sheet_for/).

## Ejemplo completo: dos personajes y un objeto persistente

**Ejemplo técnico ficticio; no incorpora hechos al canon.** Supuesto de prueba: la ficha aprobada describe a una mensajera A cuya mano izquierda falta a la altura de la muñeca, con la manga cerrada, y una llave en la mano derecha. B permanece junto a una puerta. Las imágenes de referencia ya muestran esos estados. En producción, sustituir por los datos reales, sin asignar esta lesión a un personaje de la trilogía.

**Ajustes:** Ingredients to Video; Veo 3.1 Fast si está disponible; 8 s; 16:9; un resultado; resolución comprobada en la sesión. **Adjuntos:** A en el estado correcto, B y el corredor. Identificar A y B por la referencia seleccionada y el rasgo visible que los distingue.

**Prompt propio listo para ese supuesto:**

```text
Un único plano medio de dos personajes, a la altura de sus ojos. Cámara fija.
La mensajera de la primera referencia está a la izquierda de pantalla,
mirando al guardia de la segunda referencia, situado a la derecha junto
a la puerta. Mantener sus rostros y la ropa de las imágenes adjuntas.

La mano izquierda de la mensajera falta a la altura de la muñeca; la manga
izquierda está cerrada en ese punto y permanece apoyada contra su costado.
Su mano derecha sostiene una sola llave de hierro por debajo del pecho.
La mensajera levanta lentamente la llave hasta el pecho y la mantiene allí.
El guardia baja la mirada hacia la llave; permanece en su sitio.
La llave sigue en la mano derecha de la mensajera durante toda la toma.

Usar el corredor de la tercera referencia. La puerta permanece cerrada.
Luz fría lateral desde la ventana a la izquierda de pantalla; sombras
estables. Tratamiento realista y movimiento natural. Al final, ambos
conservan sus posiciones y la llave queda quieta a la altura del pecho.
Audio: respiración suave y aire del corredor. Ambos permanecen callados.
```

**Criterios de aceptación:** la mano no reaparece; la llave no se duplica ni cambia de dueño; A y B no intercambian ropa; la puerta sigue cerrada; la cámara permanece fija. Revisar la manga también cuando se mueve el brazo derecho.

### Continuación del mismo ejemplo con Extend

Adjuntar el clip aprobado a la operación Extend; comprobar Lite como modelo ejecutor. No enviar otra vez el gesto de levantar la llave.

```text
Continuar la toma desde la postura final. La mensajera mantiene la llave
en su mano derecha a la altura del pecho. La mano izquierda sigue ausente
a la altura de la muñeca, con la misma manga cerrada contra el costado.
El guardia levanta la mirada desde la llave hasta el rostro de la mensajera.
Los dos permanecen en sus posiciones. La cámara sigue fija, con el mismo
encuadre y la misma luz fría lateral. Al final la llave continúa inmóvil
en la mano derecha. Se mantiene el aire del corredor; ambos callan.
```

Para generar esa continuación con Frames, asignar el último frame válido al campo inicial y usar la misma acción. Evaluar por separado el empalme de movimiento y el audio.

## Tutoriales y demostraciones: técnicas recuperables

Estas notas proceden del material textual accesible del creador. No se atribuye una tasa de éxito ni un resultado visual no inspeccionado. Los vídeos de 2025 sirven para estudiar el método, no para fijar la interfaz o compatibilidad de septiembre de 2026.

| Vídeo | Evidencia consultable y técnica | Aplicación a la trilogía |
|---|---|---|
| **AI Video School — Make Consistent Characters & Scenes with Google Flow’s “Jump To”**, 30-07-2025 | La descripción publica prompts: la apertura arranca detrás de una mujer y describe un arco hacia su rostro; otra toma fija altura de cámara, luz del frigorífico y sonidos. Capítulos: 00:50 Jump To, 07:21 continuidad, 09:36 extensión con Veo 2. | Describir origen y destino del movimiento y repetir el tratamiento visual. La interacción con un vendedor asigna a la protagonista una intervención concreta. No asumir disponibilidad actual de Jump To. [YouTube](https://www.youtube.com/watch?v=ubg6aNKeMjM), [descripción y prompts recuperados](https://zolotube.com/watch?v=ubg6aNKeMjM). |
| **Klever Nuts AI — How To Use Google Flow to Create Consistent AI Characters & Videos**, 20-08-2026 | La descripción propone perfiles reutilizables; capítulos: 02:19 vistas múltiples, 04:40 registro del personaje, 10:27 escenas con varios personajes. No se recuperó el prompt íntegro de esas escenas. | Reutilizar identidades cargadas para A y B; utilizar las imágenes existentes, sin rehacer el casting. La promesa de consistencia de toda una película no queda demostrada por la descripción. [YouTube](https://www.youtube.com/watch?v=n01ojTeeCsQ), [descripción recuperada](https://zolotube.com/watch?v=n01ojTeeCsQ). |
| **Maamria AI — How to Lock Consistent Characters, Voices & Avatars Using Google Flow (2026)**, 30-05-2026 | Descripción y capítulos: 02:09 segunda vista, 08:00 prueba del mismo personaje en dos escenarios, 09:10 secuencia de cuatro planos. Incluye voz y perfiles; no prueba esas funciones específicamente en Veo. | Antes de producir el episodio, probar la identidad ya aprobada en dos encuadres distintos y comparar. No extrapolar su «límite de dos imágenes» de perfil al número de ingredientes por generación. [YouTube](https://www.youtube.com/watch?v=-FcU8fwMLhg), [descripción recuperada](https://zolotube.com/watch?v=-FcU8fwMLhg). |

Como contraste técnico, Google publica una demostración de arco de 180° entre dos frames y otra de diálogo con dos personajes y un decorado como referencias. La técnica aprovechable es resolver las composiciones y repartir las intervenciones; no pedir al modelo que invente simultáneamente identidad, geografía y movimiento. Son ejemplos de Veo en una guía de Vertex, no una prueba de todos los botones de Flow. [Demostraciones oficiales](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1).

En X, la cuenta Flow by Google propone cargar una paleta como ingrediente para orientar el color. El texto se recuperó en búsqueda; la apertura directa devolvió 403. Puede servir como referencia estética si queda una entrada disponible, pero no sustituye las referencias de personaje o estado. [Publicación del 26-03-2026](https://x.com/FlowbyGoogle/status/2037271961651282233).

## Fallos documentados y respuesta de producción

Los testimonios siguientes describen casos particulares; no establecen tasas de fallo ni bugs reproducidos por esta investigación.

| Evidencia | Qué implica | Mitigación |
|---|---|---|
| Usuarios de Flow describen intercambio de ropa, instrumentos en manos del músico equivocado y personajes añadidos al regenerar. | Una corrección puede alterar partes que ya funcionaban. | Conservar la toma aprobada y comparar toda la nueva versión. Un participante describe máscaras y composición externa para corregir solo ojos u objetos. |
| En el mismo hilo, un usuario aporta inicio con farola vertical y final con farola caída; recibe un corte en vez de la caída. | Dos frames no garantizan una trayectoria física continua. | Propuesta: reducir la transformación por clip o preparar un estado intermedio verificable. |
| En el foro de desarrolladores, un usuario de Veo 3.1 denuncia herramientas inventadas y cambios de geometría dental durante movimientos de cámara, incluso con referencias y frames. | Las referencias no equivalen a una geometría bloqueada. Es un caso de API, no prueba de un fallo exclusivo de Flow. | Propuesta: reducir recorrido y oclusión, comprobar detalles al reaparecer y rechazar la toma si altera el objeto. |

Fuentes de los casos: [testimonios directos en r/GoogleFlow](https://www.reddit.com/r/GoogleFlow/comments/1w3skjc/google_flow_users_doing_narrative_work_how_are/) y [reporte en Google AI Developers Forum](https://discuss.ai.google.dev/t/veo-3-1-consistency-help-preventing-hallucinations-in-professional-dental-workflow-gemini-2-5-veo-pipeline/111898).

**No se ha confirmado un bug específico de Flow que haga reaparecer una mano amputada.** Ese caso procede del problema de producción comunicado por el autor en Storyboard Studio. Aquí se trata como un riesgo de continuidad que hay que comprobar, sin atribuirlo falsamente a un reporte externo ni prometer que un prompt lo elimina.

Orden de mitigación propuesto para manos, ropa y objetos:

1. Corregir la contradicción entre ficha, referencia y prompt.
2. Simplificar el gesto o separar acciones; mantener el beat narrativo.
3. Reducir cruces entre personajes y oclusiones de los elementos decisivos.
4. Si el plano exige precisión espacial, partir de una composición aprobada.
5. Si el defecto es local y la toma funciona, valorar composición en posproducción. No ocultar con encuadre una consecuencia que la historia necesita mostrar.
6. Cambiar una variable por intento y volver a revisar todas las invariantes. «Solo cambia X» es una petición, no una garantía.

## Aceptación del plano y entrega al montaje

Protocolo propuesto; se aplica también después de extender o corregir:

- **Inicio:** coincide con la ficha y con el estado de salida anterior, salvo el cambio de encuadre previsto.
- **Interior:** inspeccionar agarres, cruces, oclusiones, giros y reapariciones; no basta con revisar el primer y último frame.
- **Final:** registrar el estado real aprobado; no el que el prompt pretendía obtener.
- **Personajes:** misma identidad y forma, heridas persistentes, anatomía correcta por lado, ropa y accesorios.
- **Espacio:** posiciones, miradas, eje, puerta, objetos y luz compatibles entre planos.
- **Audio:** hablante correcto, texto y lengua exactos, sin réplicas añadidas. Si el diálogo canónico no cabe, subdividir; no resumirlo para que quepa.
- **Montaje:** reproducir el empalme y revisar salto de movimiento, exposición, sonido y fotogramas duplicados. Reescalar después de aprobar.

Cada entrega debería conservar: ID de plano, prompt enviado, modelo efectivo, operación, ajustes, referencias utilizadas, versión elegida y estado final aprobado. **Una frase como «mantener continuidad» no sustituye esos datos ni la inspección del vídeo.**

## Verificado por el autor (2026-09-18) — prueba real, no investigación documental

El autor generó 6 clips reales en Google Flow (Miguel cruzando Serephis) y los cruzó con una sesión de trabajo en Gemini Pro. Esto es evidencia de primera mano, más fuerte que cualquier cosa "no confirmada" de las secciones anteriores. Config real usada: **Veo, 720p, 16:9, 8s por clip, 24fps** — coincide con la matriz oficial de arriba.

- **Una sola referencia (el último frame) funciona mejor que combinar varias.** El autor mezcló referencia de cuerpo completo + último frame + textura de suelo en un mismo plano y el resultado salió estático/con movimiento incorrecto. Al dejar **una sola imagen de referencia** (normalmente el último frame aprobado del plano anterior), el movimiento se resolvió con fluidez. Regla de producción: para un plano de continuación, preferir 1 referencia; usar 2-3 solo cuando de verdad haga falta anclar más de una identidad a la vez, nunca por defecto.
- **"Frames to Video" (imagen de inicio + imagen de fin) no garantiza una interpolación fluida.** En una prueba real, el clip quedó casi estático durante ~7 de los 8 segundos y dio un salto de corte brusco en el último instante para encajar con la imagen final, en vez de interpolar el movimiento. Para planos con movimiento continuo (caminar, girar), es más fiable usar **Ingredients/último-frame como único punto de partida** y describir la acción completa en texto, que fijar un frame final exacto.
- **Las restricciones negativas SÍ funcionan escritas directamente en el prompt normal**, sin necesidad de un campo dedicado: `"Absolutely NO large buildings, NO Greek columns, and NO temple walls in the background. Open desert landscape only."` corrigió una alucinación real (el modelo interpretó bloques de piedra tallada como ruinas de un templo clásico). Esto resuelve lo que antes quedaba como "no confirmado" en la sección de referencias: **usar negaciones explícitas dentro del prompt principal es la técnica que funciona hoy**, no hace falta un campo `negativePrompt` separado.
- **Los planos de personaje caminando de frente a cámara son poco fiables**: en una prueba real, el personaje caminó hacia atrás pese a pedir explícitamente "walking forward, facing the camera, stepping towards the viewer" — repetido dos veces, el fallo persistió. Se resolvió cambiando el tipo de plano a **perfil o cámara siguiendo por detrás**, con dirección explícita ("from left to right" / "seen from behind"). Regla de producción: **evitar planos de marcha de frente a cámara**; usar perfil, tres cuartos o vista trasera para ciclos de caminata.
- **Las etiquetas de guion dentro del prompt se renderizan como texto en el vídeo.** Dejar palabras organizativas como "Plano 1" o "Audio de fondo" en el texto que se envía al generador hizo que el modelo intentara dibujar esas palabras como letras flotantes en la imagen. El prompt final entregado al generador debe ser SOLO descripción visual/acción, cero metadatos de producción — confirma la regla de la sección "Sintaxis" de arriba con un fallo real observado, no solo teórico.
- **Bug de continuidad confirmado dentro de un mismo clip, no solo entre clips**: en un plano etiquetado como "el mismo hombre caminando", las alas están ausentes en el fotograma inicial y presentes ya en el segundo 4 del mismo clip de 8s. La comprobación de continuidad no puede limitarse a comparar el primer y último fotograma de un plano contra el plano vecino: hay que revisar también la consistencia interna del propio clip (ver [[18_continuidad_inter_plano]]).
- **Se ha observado un arma alucinada** (forma de hoja/espada en el borde del encuadre) en dos clips distintos de Miguel, pese a que su ficha dice explícitamente que no porta arma, vaina ni objeto en la cadera o la espalda. Ver [[18_continuidad_inter_plano]] para la restricción negativa por personaje que se añade a raíz de esto.

## Fuentes

Consultadas el 2026-09-16. Se prioriza ayuda actual de Flow para compatibilidad; anuncios fechados para evolución de funciones; guías de Veo para lenguaje; testimonios para fallos observados. Los vídeos se consultaron parcialmente según lo indicado arriba.

### Documentación y publicaciones oficiales

- [Google Flow — acceso al producto](https://labs.google/flow).
- [Learn about Google Flow models & supported features](https://support.google.com/flow/answer/16352836?hl=en), contrastada con [versión española](https://support.google.com/flow/answer/16352836?hl=es).
- [Create videos in Google Flow](https://support.google.com/flow/answer/16353334?hl=en).
- [Edit videos & build scenes in Google Flow](https://support.google.com/flow/answer/16935718?hl=en).
- [Manage your Google Flow credits](https://support.google.com/flow/answer/16526234?hl=en).
- [5 tips for getting started with Flow](https://blog.google/innovation-and-ai/products/flow-video-tips/), 25-06-2025. Los límites de modelos de ese anuncio son históricos.
- [Fuel your creativity with new generative media models and tools](https://blog.google/innovation-and-ai/products/generative-media-models-io-2025/), 20-05-2025. Controles de cámara originales.
- [Bringing new Veo 3.1 updates into Flow to edit AI video](https://blog.google/innovation-and-ai/products/veo-updates-flow/), octubre de 2025.
- [Veo 3.1 Ingredients to Video: More consistency, creativity and control](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video/), 13-01-2026.
- [The ultimate prompting guide for Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1), 15-10-2025. Ejemplos y demostraciones; contexto Vertex AI.
- [Video generation prompt guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide). La URL redirige actualmente a Gemini Enterprise Agent Platform.
- [How to create effective prompts with Veo 3 — Google DeepMind](https://deepmind.google/models/veo/prompt-guide/).
- [Flow by Google en X — usar una paleta como ingrediente](https://x.com/FlowbyGoogle/status/2037271961651282233), 26-03-2026. Texto indexado; acceso directo bloqueado.

### Vídeos de YouTube

- [AI Video School — Make Consistent Characters & Scenes with Google Flow’s “Jump To” (AI Video Tutorial)](https://www.youtube.com/watch?v=ubg6aNKeMjM), 30-07-2025. [Descripción, capítulos y prompts accesibles](https://zolotube.com/watch?v=ubg6aNKeMjM).
- [Klever Nuts AI — How To Use Google Flow to Create Consistent AI Characters & Videos](https://www.youtube.com/watch?v=n01ojTeeCsQ), 20-08-2026. [Descripción y capítulos accesibles](https://zolotube.com/watch?v=n01ojTeeCsQ).
- [Maamria AI — How to Lock Consistent Characters, Voices & Avatars Using Google Flow (2026)](https://www.youtube.com/watch?v=-FcU8fwMLhg), 30-05-2026. [Descripción y capítulos indexados](https://zolotube.com/watch?v=-FcU8fwMLhg).
- [Google Flow Tutorial (How To Use Google Flow) 2026](https://www.youtube.com/watch?v=5fX2xnWntaw), localizado como tutorial de abril de 2026; capítulo de cámara 14:33. Acceso directo sin contenido suficiente para extraer una técnica adicional.

### Comunidad y reportes directos

- [Google Flow users doing narrative work: how are you handling targeted corrections without collateral drift?](https://www.reddit.com/r/GoogleFlow/comments/1w3skjc/google_flow_users_doing_narrative_work_how_are/), agosto–septiembre de 2026. Ropa, objetos y correcciones locales; experiencias individuales.
- [Veo 3.1 Consistency Help: Preventing Hallucinations in Professional Dental Workflow](https://discuss.ai.google.dev/t/veo-3-1-consistency-help-preventing-hallucinations-in-professional-dental-workflow-gemini-2-5-veo-pipeline/111898). Reporte de API; no trasladar automáticamente a Flow.
- [The 22-command Gemini Flow cheat sheet…](https://www.reddit.com/r/promptingmagic/comments/1w1vkz7/the_22command_gemini_flow_cheat_sheet_for/), agosto de 2026. Propuesta de su autor, sin sintaxis oficial ni evaluación controlada.
