# 16 — Cámara y luz: vocabulario para Dirección/Previz (2026-09-16)
**BORRADOR — pendiente de aprobación del autor**

Encargo del autor: convertir capítulos de *Las Crónicas del Juicio / Chronicles of the Sundering Judgment* en planos que puedan montarse juntos. Problema de partida: un personaje pierde una mano y la recupera en otro plano. **La cámara debe mostrar el estado de la historia; la iluminación debe permitir reconocerlo.** Una descripción fotográfica precisa ayuda a dirigir la generación, pero no garantiza continuidad anatómica.

Uso: referencia para redactar cada plano en Google Flow/Veo y preparar su paso por Storyboard Studio. Personajes y formas ya definidos en `character_library/`: se utilizan sus referencias; no se hace casting ni se inventa otra apariencia. Los ejemplos de este documento son ejercicios técnicos, no escenas nuevas ni modificaciones del canon.

## La regla de oro: un recurso dominante, sin repetir fórmula

Aplicación de [[13_presencia_cinematografica]] a fotografía: elegir **una decisión expresiva dominante por plano**. Puede ser la distancia, una revelación lateral, el foco o una fuente de luz. Las otras decisiones sostienen esa intención. No encadenar contrapicado + órbita + zoom + contraluz en cada presentación.

La variedad se mide por función: mostrar escala, seguir un esfuerzo, descubrir una consecuencia, mantener una distancia. Cambiar «travelling» por «dolly» sin cambiar el plano no aporta variedad. Tampoco hay que cambiar de luz entre contracampos para que parezcan distintos: **el raccord se conserva aunque la cobertura repita recursos**. Reservar los gestos más marcados para momentos que los justifiquen.

Calibre B ([[12_calibre_b]]): sustituir «luz épica de desesperación» por una fuente, una dirección y un efecto visible. La niebla física solo aparece si el lugar la admite; no es el acabado obligatorio de la fantasía.

## Qué está verificado y qué necesita prueba

- **Flow:** su ayuda documenta generación con texto, referencias visuales —ingredientes— y fotogramas inicial/final. El texto debe ser compatible con las imágenes. La disponibilidad depende del modelo y, en ciertas funciones, de la región. Escribir una ruta local en el prompt no adjunta una imagen: hay que cargar o seleccionar el recurso. [Ayuda oficial de Flow](https://support.google.com/flow/answer/16353334?hl=en).
- **Veo:** Google publica vocabulario de encuadre, movimiento, óptica y luz; advierte que algunos ángulos y efectos ópticos avanzados no tienen soporte oficial garantizado. Son instrucciones semánticas, no una cámara virtual con trayectoria matemáticamente bloqueada. La documentación de Vertex AI no demuestra que cada control exista en Flow. [Guía de generación de vídeo](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide).
- **Storyboard Studio:** se localizaron un tutorial y un hilo de usuarios con ese nombre, pero no se verificó una especificación oficial propia que garantice memoria corporal entre planos ni un formato obligatorio de guion. **No confirmado / puede haber cambiado.** La ficha propuesta aquí es una convención de trabajo del proyecto, no una sintaxis oficial de esa herramienta.
- **Runway:** su biblioteca ofrece términos con ejemplos generados en Gen-4.5. Su guía de Gen-4 recomienda empezar con movimiento simple y formulación positiva. Son paralelismos útiles de redacción; no pruebas de idéntico comportamiento en Veo. No se trasladan controles ni parámetros a Sora o Kling sin comprobar su versión. [Biblioteca de cámara](https://help.runwayml.com/hc/en-us/articles/46749315925395-Camera-Terms-Prompts-Examples), [guía Gen-4](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide).

Los patrones siguientes son propuestas de Dirección/Previz, no resultados de ensayos realizados en este proyecto. Conservar el término inglés junto a una descripción física facilita la correspondencia entre EN y ES; no se ha verificado que mezclar idiomas mejore por sí solo la obediencia del modelo.

## Tamaño de plano: decir exactamente qué entra

El tamaño describe el recorte; el ángulo describe desde dónde miramos. Las equivalencias no son idénticas en todas las escuelas: **el límite corporal escrito prevalece sobre la etiqueta**. Nomenclatura de referencia: [StudioBinder, tamaños de plano](https://www.studiobinder.com/blog/types-of-camera-shots-sizes-in-film/).

| Plano ES (término EN) | Recorte y utilidad | Patrón de frase propuesto |
|---|---|---|
| Gran plano general (*extreme wide shot / extreme long shot*) | Domina el lugar; figura muy pequeña. Escala o aislamiento. | «El patio ocupa casi todo el encuadre; la figura se distingue junto a la puerta». |
| Plano general (*wide shot / long shot*) | Cuerpo y entorno legibles. Geografía de la acción. | «Se ven el personaje completo, el umbral y la distancia hasta la mesa». |
| Plano entero (*full shot*) | Cabeza a pies. Postura y desplazamiento. | «El cuerpo completo permanece dentro del cuadro mientras cruza el pasillo». |
| Plano americano (*cowboy shot / medium long shot*) | Aproximadamente desde medio muslo; precisar corte. | «Encuadre desde medio muslo hasta la cabeza; ambas manos quedan dentro del cuadro». |
| Plano medio (*medium shot*) | Cintura a cabeza. Gesto y conversación. | «Encuadre desde la cintura; el antebrazo descansa sobre la mesa visible». |
| Plano medio corto (*medium close-up*) | Pecho a cabeza. Reacción contenida. | «Encuadre desde el pecho; el personaje levanta la mirada». |
| Primer plano (*close-up*) | Cara dominante. Lectura del gesto. | «El rostro llena el cuadro; la mirada se dirige fuera de campo a la derecha». |
| Primerísimo primer plano (*extreme close-up*) | Recorte facial muy cerrado; precisar límites. | «Solo entran los ojos y el puente de la nariz». |
| Plano detalle (*detail shot / insert shot*) | Objeto o parte del cuerpo relevante. | «La mano y el cierre ocupan el cuadro; se ve cómo los dedos lo sueltan». |

**Detalle no equivale a macro.** *Macro* implica mostrar algo pequeño con gran ampliación; no hace falta para un guante entero. *Establishing shot* nombra la función de situar, no un tamaño obligatorio.

Complementos de encuadre: plano de dos (*two-shot*), sobre el hombro (*over-the-shoulder / OTS*), subjetivo (*point-of-view / POV*). En un OTS, identificar el hombro y a quién vemos; en un POV, quién mira y desde qué posición. [Guía de encuadres de StudioBinder](https://www.studiobinder.com/blog/ultimate-guide-to-camera-shots/).

Patrón: «Sobre el hombro derecho de A, situado en primer término a la izquierda del cuadro; B permanece al fondo a la derecha». No usar únicamente «A mira a B»: deja sin resolver la posición de cámara.

## Movimiento: cámara y acción ocurren a la vez

Una trayectoria necesita **inicio + dirección + velocidad relativa + final**. Escribir quién se mueve en cada oración. «Acercamiento al personaje» puede convertirse en un personaje que camina hacia cámara; «la cámara avanza; el personaje permanece sentado» elimina esa ambigüedad.

| Movimiento ES (EN) | Mecánica que debe quedar clara |
|---|---|
| Plano fijo (*locked-off / static shot*) | Posición, orientación y encuadre constantes. La acción ocurre dentro. |
| Paneo / panorámica horizontal (*pan left/right*) | Giro horizontal desde un punto fijo. |
| Panorámica vertical (*tilt up/down*) | Giro vertical desde un punto fijo. |
| Travelling de aproximación/retroceso (*dolly in/out; push-in/pull-back*) | La cámara se desplaza hacia el sujeto o se aleja. |
| Travelling lateral (*truck left/right; lateral tracking shot*) | Traslación lateral; si sigue al sujeto, indicar su velocidad relativa. |
| Seguimiento (*tracking / following / leading shot*) | Relación con el sujeto: detrás, delante o en paralelo; concretar recorrido. |
| Elevación/descenso (*pedestal up/down*) | Traslación vertical de la cámara; distinta de inclinarla. |
| Grúa (*crane / jib shot*) | Ascenso, descenso o arco amplio; señalar el encuadre de llegada. |
| Arco / órbita (*arc / orbit shot*) | Recorrido alrededor del sujeto; describir lado y vista final. |
| Cámara estabilizada (*Steadicam-style / stabilized tracking*) | Cualidad fluida del recorrido; necesita una trayectoria. |
| Cámara en mano (*handheld*) | Oscilación del encuadre; precisar intensidad. |
| Barrido (*whip pan*) | Giro muy rápido con desenfoque de movimiento. |

Distinciones contrastadas con [StudioBinder, movimientos](https://www.youtube.com/watch?v=IiyBo-qLDeM) y [Dom the AI Tutor, guía del autor](https://techtutorzone.com/38-camera-movement-prompts-for-ai-filmmaking-the-masterclass/). Las etiquetas de soporte describen un aspecto visual en IA; no solicitan que aparezca una grúa o un operador.

### Patrones de simultaneidad

- **Acompañar y revelar:** «Plano americano de perfil. La cámara se desplaza en travelling lateral hacia la derecha (*truck right*), paralela al personaje y a su velocidad mientras camina. Él conserva su tamaño en cuadro; los pilares cercanos pasan ante el fondo y dejan ver progresivamente el portón. Termina cuando se detiene ante él».
- **Seguir de frente:** «La cámara retrocede (*backward tracking*) mientras el personaje avanza hacia ella. Mantiene un plano medio y la misma distancia; el corredor queda visible detrás de sus hombros».
- **Descubrir una consecuencia:** «Desde el rostro, la cámara gira hacia abajo (*tilt down*) mientras el personaje baja el antebrazo. El giro termina en plano detalle del vendaje sobre la mesa; la cámara conserva su posición».
- **Abrir escala:** «La cámara asciende en grúa (*crane up*) mientras el personaje permanece en el umbral. Comienza a su altura y termina en un plano general elevado que muestra el patio detrás».
- **Observar:** «Plano general fijo (*locked-off wide shot*). El personaje entra por la izquierda, cruza hasta la mesa y se detiene. El marco de la puerta conserva su posición durante todo el plano».
- **Acompañar con urgencia:** «Seguimiento desde atrás, cámara en mano de oscilación leve (*subtle handheld*), mientras corre hacia la salida. La puerta permanece como destino visible». La oscilación no debe impedir leer la acción.

Usar «mientras» para simultaneidad y «después» para fases sucesivas. No pedir varias llegadas incompatibles dentro de un clip corto. Si importa la sincronía exacta, comprobarla en el vídeo: una marca temporal en el texto expresa intención, no garantiza un evento en un fotograma concreto.

### Zoom óptico, zoom digital y dolly

- **Zoom óptico (*optical zoom*):** cambia la focal con cámara quieta. Patrón: «Desde posición fija, zoom óptico lento de plano medio a primer plano mientras escucha». En generación se pide su apariencia, no una lente física verificable.
- **Zoom digital (*digital zoom / crop-in*):** ampliación por recorte. Si se necesita un recorte exacto, hacerlo en montaje sobre un plano aprobado; el texto generativo puede reinterpretar el contenido.
- **Dolly:** cambia el punto de vista y las relaciones de perspectiva. Patrón: «La cámara avanza hacia el rostro; el borde próximo de la mesa sale progresivamente del cuadro». No llamarlo zoom.
- **Dolly zoom:** combina desplazamiento y cambio opuesto de focal para mantener aproximadamente el tamaño del sujeto mientras cambia la perspectiva del fondo. Reservarlo para un beat específico y probarlo aislado; no es sinónimo de acercamiento dramático.

En un travelling, el desplazamiento relativo de elementos cercanos y lejanos —paralaje— ayuda a revisar si hubo traslación o solo ampliación. Referencia visual: [StudioBinder, Camera Movement](https://www.youtube.com/watch?v=IiyBo-qLDeM).

## Ángulo: altura y orientación por separado

Los efectos narrativos son posibilidades, no significados automáticos. Un contrapicado también puede mostrar a alguien encerrado bajo un techo. [StudioBinder, ángulos](https://www.studiobinder.com/blog/types-of-camera-shot-angles-in-film/).

| Ángulo ES (EN) | Posición | Uso y frase propuesta |
|---|---|---|
| Altura de ojos (*eye-level shot*) | Cámara a la altura de los ojos del sujeto. | Relación directa: «A la altura de sus ojos mientras permanece sentado». |
| Picado (*high-angle shot*) | Desde arriba, mirando hacia abajo. | Exponer posición o vulnerabilidad: «Desde el rellano, mirando hacia el personaje al pie de la escalera». |
| Contrapicado (*low-angle shot*) | Desde abajo, mirando hacia arriba. | Peso o amenaza: «Desde la altura de su cintura, inclinada hacia el rostro». |
| Cenital (*top-down / overhead shot*) | Vertical desde arriba. | Geografía: «Directamente sobre la mesa, eje óptico perpendicular al tablero». |
| Nadir (*straight-up shot; extreme worm’s-eye view*) | Vertical desde abajo. | Altura extrema: «Desde el suelo, mirando verticalmente hacia la abertura del techo». |
| Holandés (*Dutch / canted angle*) | Horizonte inclinado por giro sobre el eje óptico. | Desequilibrio: «Horizonte inclinado de forma constante durante el plano». |

*Worm’s-eye view* puede interpretarse como contrapicado muy bajo: añadir «verticalmente hacia arriba» si se necesita nadir. *Aerial* no exige cenital. Una cámara baja que mira horizontalmente tampoco es, por esa sola altura, un contrapicado.

## Focal y foco: dirigir la atención

**Gran angular (*wide-angle lens*)** para dar espacio al entorno; **teleobjetivo (*telephoto lens*)** para un campo estrecho y apariencia de planos próximos entre sí. La perspectiva depende del punto de vista: no atribuir a una cifra de focal un resultado independiente de la distancia. En IA, los milímetros son una indicación estética que debe validarse; describir también el resultado visible. [StudioBinder, lentes](https://www.studiobinder.com/wp-content/uploads/2021/09/Camera-Lenses-Explained-vol1-Ebook-StudioBinder.pdf).

**Poca profundidad de campo (*shallow depth of field*)** separa al sujeto del fondo desenfocado; **foco profundo (*deep focus*)** conserva varios términos legibles; **cambio de foco (*rack focus*)** traslada la nitidez durante el plano. [Runway, ejemplos de foco](https://help.runwayml.com/hc/en-us/articles/46749315925395-Camera-Terms-Prompts-Examples).

Patrón: «Cámara fija. El cierre está nítido en primer término; cuando la mano lo suelta, el foco pasa al rostro situado detrás. El cierre queda desenfocado». Es una transición de atención, no un zoom ni una transformación del objeto.

No desenfocar el miembro cuya continuidad hay que comprobar. Si rostro y mano importan a la vez, disponerlos en un plano de foco compatible o darles cobertura separada.

## Luz: fuente, dirección, calidad y continuidad

Nombrar primero la fuente del espacio: ventana, brasero, cielo cubierto. Después, el efecto sobre el sujeto. Distinguir luz —cómo llega— de etalonaje (*color grading*) —cómo se trata el color de la imagen—. «Paleta fría» no explica qué ilumina una cara.

### Funciones y esquemas

| Término ES (EN) | Qué hace | Patrón propuesto |
|---|---|---|
| Luz clave / principal (*key light*) | Modela el sujeto; referencia de dirección. | «La ventana situada junto a la puerta ilumina lateralmente el rostro». |
| Relleno (*fill light*) | Reduce la oscuridad de las sombras. | «Un rebote tenue permite leer la mejilla opuesta». |
| Contraluz (*backlight*) | Llega desde detrás; puede separar figura y fondo. | «La abertura posterior ilumina el borde de los hombros». |
| Luz de borde (*rim light*) | Delinea un contorno. | «Un filo de luz recorre el hombro orientado al ventanal». |
| Luz práctica (*practical light*) | Fuente visible dentro de la escena. | «El brasero permanece encendido al fondo; su luz cálida alcanza el costado próximo». |
| Luz motivada (*motivated lighting*) | Tiene una causa reconocible en el lugar. | «La claridad de la puerta se prolonga sobre las manos cercanas». |

Clave, relleno y contraluz forman el esquema de tres puntos; no es obligatorio completarlo en cada plano. [StudioBinder, tres puntos](https://www.studiobinder.com/blog/three-point-lighting-setup/). Una práctica puede justificar iluminación adicional: que aparezca una vela no obliga a que toda la escena parezca expuesta únicamente por ella. [StudioBinder, luz práctica](https://www.studiobinder.com/blog/what-is-practical-lighting-in-film/).

### Calidad, contraste y hora

- **Luz dura (*hard light*):** sombras de borde definido. «La franja de sol corta el antebrazo con un límite nítido». **Luz suave/difusa (*soft / diffused light*):** transición gradual. «La ventana amplia y velada deja sombras suaves bajo los ojos». Dura no equivale a intensa; suave no equivale a tenue. [StudioBinder, luz dura](https://www.studiobinder.com/blog/what-is-hard-light-photography/), [Aputure, difusión](https://aputure.com/EN-US/products/light-dome-se).
- **Clave baja (*low-key lighting*):** predominio de sombras y contraste. «El fondo permanece oscuro; cara y vendaje conservan detalle». No confundir con subexponer todo. **Clave alta (*high-key lighting*):** imagen luminosa con sombras contenidas; no significa blancos quemados. [StudioBinder, clave baja](https://www.studiobinder.com/blog/what-is-low-key-lighting-definition/), [catálogo de iluminación](https://www.studiobinder.com/camera-shots/lighting/).
- **Hora dorada (*golden hour*):** sol bajo, apariencia cálida y sombras largas. **Hora azul (*blue hour*):** ambiente crepuscular azulado. El nombre de la hora debe acompañarse de dirección y visibilidad: «Sol bajo desde detrás de la muralla; el rostro recibe claridad del cielo». Son elecciones condicionadas por la hora canónica, no filtros intercambiables. [Google Cloud, guía de Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1).

Tres recetas para adaptar al lugar, sin imponerlas a todo el libro:

1. **Leer desgaste:** ventana lateral amplia, relleno débil, fondo algo más oscuro; las marcas siguen visibles. Cámara quieta si el beat está en el cuerpo.
2. **Mostrar autoridad cotidiana:** luz ambiente relativamente uniforme, altura de ojos, espacio para la reacción de otros. La autoridad no exige contrapicado ni aureola.
3. **Revelar un peligro:** una fuente lateral ya establecida deja una zona del fondo legible; el desplazamiento de cámara descubre lo que estaba oculto. La luz no se enciende mágicamente para acompañar el giro.

### Raccord de iluminación

Registrar la fuente en coordenadas del decorado: «ventana junto a la puerta norte», no solo «luz desde la izquierda». Al cambiar de posición de cámara, esa fuente puede aparecer a la derecha de pantalla. Mantener «izquierda» en ambos contracampos puede invertir falsamente la iluminación.

Separar **fuente fija** de **aspecto variable sobre un cuerpo que gira**. Patrón: «La ventana conserva posición e intensidad; mientras el personaje vuelve la cabeza, su mejilla entra gradualmente en sombra». Mantener exposición y balance de blancos estables si no hay un cambio motivado. Es una instrucción que se revisa, no un bloqueo técnico garantizado.

## Atmósfera: materia visible, con lugar y movimiento

Vocabulario de entorno presente en la [guía de Google](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide). Estos patrones son propuestas propias:

| Elemento (EN) | Especificación útil |
|---|---|
| Niebla (*fog*) | «Banco bajo detrás de la figura; rostro y manos permanecen despejados». |
| Bruma ligera (*haze*) | «Velo tenue al fondo que hace visible la dirección de la luz». |
| Humo (*smoke*) | «Sale del brasero y asciende hacia la abertura superior». |
| Polvo suspendido (*dust motes*) | «Partículas escasas visibles dentro del haz de la ventana». |
| Polvo levantado (*airborne dust / dust cloud*) | «Cada pisada levanta polvo a la altura de los tobillos». |
| Luz volumétrica (*volumetric lighting / light shafts*) | «Un haz oblicuo atraviesa la bruma entre la ventana y el suelo». |

Elegir una materia dominante salvo que la escena exija varias. Especificar origen, densidad, altura y dirección cuando afecten a la lectura. La atmósfera no debe ocultar sistemáticamente el estado corporal ni desaparecer entre planos contiguos. En fantasía, «partículas brillantes» puede introducir apariencia de magia: no añadirlas si el capítulo no la establece.

## Ficha mínima que entrega Dirección/Previz

La ficha conserva decisiones para el equipo. El prompt final selecciona las instrucciones necesarias para la modalidad usada; no tiene que copiar todos los rótulos.

```text
PLANO: [identificador y beat del capítulo]
REFERENCIAS: [recurso real de character_library/; forma y estado aprobados]
ESTADO: [lesión, lado anatómico, vestuario, objeto y mano que lo sostiene]
ESPACIO: [posición inicial/final; dirección de pantalla; fuente fija de luz]
ENCUADRE: [tamaño + límites visibles; altura/ángulo; foco]
ACCIÓN: [una acción principal]
CÁMARA: [fija o trayectoria; velocidad relativa; inicio y llegada]
LUZ: [fuente + dirección + calidad + contraste; cambio motivado, si existe]
ATMÓSFERA: [solo la necesaria]
SALIDA: [postura, estado y composición para enlazar el plano siguiente]
REVISIÓN: [qué debe permanecer visible y qué invalida la toma]
```

**Con fotograma inicial aprobado:** priorizar acción y cámara, más el estado crítico que podría perderse. **Con referencia de identidad como ingrediente:** aún hay que establecer puesta en escena, encuadre y luz; un retrato no determina el plano completo. **Desde texto:** explicitar además sujeto, lugar y composición. La recomendación de concentrar el texto en movimiento cuando la imagen ya fija la escena está documentada en [Runway Gen-4](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide); su aplicación a este flujo es una propuesta que debe probarse.

Patrón compacto:

> [Tamaño y ángulo]. [Sujeto identificado] realiza [acción]. La cámara [trayectoria] mientras [acción simultánea], manteniendo [relación de encuadre] y revelando [elemento existente]. [Fuente y efecto de luz]. [Estado crítico persistente]. Termina en [composición concreta].

No exportar corchetes pendientes. Configurar duración y formato en los controles disponibles; escribirlos en la ficha no asegura que la aplicación los aplique.

## Caso de continuidad: una mano no reaparece por cambiar de plano

Una pérdida de mano, una quemadura y un guante son estados distintos. El documento 13 menciona una mano quemada de Belial; **eso no autoriza a convertirla en amputación ni a inventar su lateralidad**. Dirección/Previz debe recibir del capítulo y del responsable de continuidad el estado exacto. La luz tampoco debe borrar visualmente la lesión.

Ejercicio hipotético, ajeno al canon: personaje con ausencia establecida de mano izquierda y vendaje aprobado en el extremo del antebrazo.

- **Plano A, recorrido:** «Plano americano de perfil. Camina hacia la derecha de pantalla mientras la cámara lo acompaña lateralmente a su velocidad. El antebrazo izquierdo termina en el vendaje de la referencia, visible durante el recorrido; la mano derecha permanece junto al cuerpo. La ventana del rellano ilumina de lado el vendaje. Termina detenido ante la mesa».
- **Plano B, consecuencia:** «Plano detalle fijo del extremo vendado del antebrazo izquierdo, apoyado sobre la mesa. Conserva forma y longitud de la referencia aprobada. La claridad sigue llegando desde la ventana del rellano». No describir dedos de ese lado ni pedir que agarre un objeto.
- **Plano C, reacción:** «Primer plano a la altura de los ojos. El personaje mira hacia la mesa; el fondo conserva la ventana en su ubicación correspondiente». El brazo queda fuera de campo; el registro de continuidad conserva su estado para la siguiente aparición.

Si la referencia base contradice la lesión, no compensarla con un párrafo cada vez más largo: hace falta una referencia de ese estado aprobada por el flujo correspondiente. Este encargo no crea ni modifica imágenes.

El texto esquemático puede contribuir al fallo, pero no está demostrado que sea su única causa. Un usuario del foro de Google documenta alteraciones de geometría durante movimientos aun usando referencias y extremos de clip; usuarios de Reddit describen movimientos de cámara ignorados. Son testimonios, no mediciones de fiabilidad. [Foro de Google](https://discuss.ai.google.dev/t/veo-3-1-consistency-help-preventing-hallucinations-in-professional-dental-workflow-gemini-2-5-veo-pipeline/111898), [hilo de Flow](https://www.reddit.com/r/GoogleFlow/comments/1v9bnjt/flow_seems_to_be_ignoring_camera_movement/).

## Revisión antes de aceptar un plano

1. **Cuerpo y objetos:** comprobar inicio, tramo medio y final; revisar especialmente oclusiones y giros. Verificar lado anatómico, integridad corporal, vestuario y mano que sostiene cada objeto. Una mano oculta no es una mano ausente.
2. **Cámara:** comparar recorrido pedido y obtenido. ¿Se trasladó la cámara o giró el personaje? ¿Llegó al encuadre previsto? ¿Apareció un corte dentro de la toma?
3. **Luz:** comprobar fuente, sombras, exposición y color al compararlo con el plano anterior. La herida debe seguir siendo reconocible cuando está visible.
4. **Montaje:** comprobar dirección de desplazamiento, miradas y lado del eje de acción. Una órbita puede cruzarlo; conservar orientación o preparar una transición que la explique.
5. **Corrección:** cambiar una variable cada vez. Si falla el recorrido, probar menos amplitud o separar revelación y reacción en dos planos. Si falla la anatomía, rechazar la toma; una cámara vistosa no la salva.

Propuesta de prueba: misma referencia, mismo beat y misma luz; comparar plano fijo, travelling lateral corto y acercamiento sencillo. Anotar modelo, fecha, prompt y fallo observado. Elegir el recurso que cuenta el beat y mantiene el estado, sin convertir un único resultado satisfactorio en garantía general.

## Vídeos: qué consultar y cómo traducirlo a texto

Se consultaron páginas, descripciones indexadas y, cuando existía, el artículo del propio creador. **No se reprodujeron ni verificaron íntegramente los vídeos**; no se atribuyen aquí resultados medidos a sus demostraciones. Las búsquedas de análisis *shot-by-shot* no proporcionaron una pieza suficientemente verificable para incorporarla como fundamento.

| Canal / vídeo | Utilidad para Dirección/Previz |
|---|---|
| **StudioBinder — Ultimate Guide to Camera Movement, The Shot List Ep6** | Contrastar giro, desplazamiento y zoom. Tras ver un ejemplo, escribir qué se mueve, desde dónde y hasta dónde; evitar resumirlo como «cámara cinematográfica». |
| **Dom the AI Tutor / Tech Tutor Zones — ALL Camera Movement Prompts in AI Filmmaking (38 Cinematic Moves)** | Biblioteca de prompts y ejemplos; el artículo propio permite contrastar seguimiento frontal, posterior y lateral. Usar esa distinción para coordinar cámara y actor. |
| **Antonio Garci — Garciconsejos: Luz Dura y Luz Suave** | Recurso en español sobre iluminación fotográfica. Traducir la observación a borde de sombra y transición tonal; no tomarlo como ensayo de Veo. |
| **How to Use Storyboard Studio in Google Flow (Step-by-Step)** | Tutorial localizado para reconocer el flujo mostrado. Autoría y capacidades concretas no verificadas mediante documentación oficial propia de Storyboard Studio; no fundamenta garantías de continuidad. |

Ejercicio de análisis plano a plano: registrar tamaño inicial/final, elemento que motiva el movimiento, momento de revelación y fuente de luz. Convertirlo en una instrucción literal adaptada al capítulo; no copiar la estética completa de una película sobre todos los personajes.

## Fuentes

Consulta: **2026-09-16**. Investigación previa a la redacción: más de treinta consultas diferenciadas en inglés y español, incluyendo documentación oficial, foros, Reddit, X/Twitter y búsquedas específicas en YouTube. Fuentes técnicas principales: fabricantes y autores de los materiales. Los testimonios no se usan para certificar funciones.

### Documentación y técnica

- Google — [Crear vídeos en Google Flow / Create videos in Google Flow](https://support.google.com/flow/answer/16353334?hl=en).
- Google Cloud — [Video generation prompt guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide).
- Google Cloud — [The ultimate prompting guide for Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1).
- Runway — [Camera Terms, Prompts, & Examples](https://help.runwayml.com/hc/en-us/articles/46749315925395-Camera-Terms-Prompts-Examples).
- Runway — [Gen-4 Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide).
- StudioBinder — [Guide to Camera Shots: Every Shot Size Explained](https://www.studiobinder.com/blog/types-of-camera-shots-sizes-in-film/).
- StudioBinder — [50+ Types of Camera Shots, Angles, and Techniques](https://www.studiobinder.com/blog/ultimate-guide-to-camera-shots/).
- StudioBinder — [Camera Angles Explained](https://www.studiobinder.com/blog/types-of-camera-shot-angles-in-film/).
- StudioBinder — [Camera Lenses Explained — ebook](https://www.studiobinder.com/wp-content/uploads/2021/09/Camera-Lenses-Explained-vol1-Ebook-StudioBinder.pdf), extracto indexado; lectura íntegra bloqueada por el tamaño del PDF.
- StudioBinder — [Three-Point Video Lighting: Key, Fill, & Backlight Setup Guide](https://www.studiobinder.com/blog/three-point-lighting-setup/).
- StudioBinder — [What is Practical Lighting in Film?](https://www.studiobinder.com/blog/what-is-practical-lighting-in-film/).
- StudioBinder — [What is Hard Light](https://www.studiobinder.com/blog/what-is-hard-light-photography/).
- StudioBinder — [What is Low Key Lighting](https://www.studiobinder.com/blog/what-is-low-key-lighting-definition/).
- StudioBinder — [Lighting Techniques in Film](https://www.studiobinder.com/camera-shots/lighting/).
- Aputure — [Light Dome SE](https://aputure.com/EN-US/products/light-dome-se), documentación del fabricante sobre difusión.
- Dom the AI Tutor — [38 Camera Movement Prompts for AI Filmmaking: The Masterclass](https://techtutorzone.com/38-camera-movement-prompts-for-ai-filmmaking-the-masterclass/), artículo del creador vinculado a su vídeo.

### Vídeos localizados y páginas consultadas

- StudioBinder — [Ultimate Guide to Camera Movement — Every Camera Movement Technique Explained [The Shot List Ep6]](https://www.youtube.com/watch?v=IiyBo-qLDeM).
- Dom the AI Tutor / Tech Tutor Zones — [ALL Camera Movement Prompts in AI Filmmaking (38 Cinematic Moves)](https://www.youtube.com/watch?v=zQI_pWw9qWo).
- Antonio Garci — [Garciconsejos: Luz Dura y Luz Suave](https://www.youtube.com/watch?v=AEs_v3faTfs), descripción indexada; apertura directa fallida.
- [How to Use Storyboard Studio in Google Flow (Step-by-Step) — AI movie from start to finish!](https://www.youtube.com/watch?v=mSw8xFPpn2o), descripción indexada; contenido completo no accesible.

### Contraste de experiencias y límites de acceso

- Google AI Developers Forum — [Veo 3.1 Consistency Help: Preventing Hallucinations in Professional Dental Workflow](https://discuss.ai.google.dev/t/veo-3-1-consistency-help-preventing-hallucinations-in-professional-dental-workflow-gemini-2-5-veo-pipeline/111898), experiencia de un usuario, no especificación oficial.
- Reddit, r/GoogleFlow — [Flow seems to be ignoring camera movement instructions?](https://www.reddit.com/r/GoogleFlow/comments/1v9bnjt/flow_seems_to_be_ignoring_camera_movement/), testimonio comunitario.
- Reddit, r/GoogleFlow — [Help — Using Storyboard Studio in Google Flow](https://www.reddit.com/r/GoogleFlow/comments/1uaz5d3/help_using_storyboard_studio_in_google_flow/), extracto indexado sobre el uso del nombre de la herramienta.
- X/Twitter, Leo Grundström — [How to Create High-Quality Faceless YouTube Videos (The Full Process)](https://x.com/grundstromleo/status/2036909231195251002), extracto indexado localizado; apertura fallida. No se usa para validar funciones ni cifras.
