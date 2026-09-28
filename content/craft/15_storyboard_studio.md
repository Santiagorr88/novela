# 15 — Storyboard Studio: guion y continuidad entre planos (2026-09-16)
**BORRADOR — pendiente de aprobación del autor**

Encargo del autor: adaptar capítulos de *Las Crónicas del Juicio* / *Chronicles of the Sundering Judgment* con las referencias ya existentes en `character_library/`. Problema a resolver: un personaje pierde una mano en un plano y la recupera en el siguiente.

**Regla de trabajo: cada plano debe declarar quién aparece, en qué estado llega y qué cambia.** Conservar el rostro no basta para conservar una lesión, la mano que sostiene un arma o la posición de los personajes. Un guion explícito reduce ambigüedades; no garantiza que el generador obedezca.

## Qué se ha podido verificar

Investigación realizada el 2026-09-16: más de 30 consultas distintas en inglés y español, documentación oficial, testimonios, búsquedas en Reddit y X/Twitter y consultas específicas de YouTube. Se leyeron [[13_presencia_cinematografica]] y [[12_calibre_b]] antes de redactar.

Tres niveles de evidencia en esta guía:

- **Documentado:** capacidades descritas por Google. Cuando corresponden a Flow en general, se indica.
- **Reportado:** experiencias de usuarios o descripciones de sus demostraciones. Acreditan lo que cuentan, no una tasa de éxito ni una función universal.
- **Propuesta de producción:** formato y controles para esta adaptación. No son una sintaxis oficial ni una receta validada experimentalmente en Storyboard Studio.

La aplicación compartida redirige actualmente a `flow.google.com`; su interfaz completa no fue accesible mediante la consulta pública. En los vídeos se pudieron consultar descripciones y capítulos, algunos mediante páginas que reproducen sus metadatos, pero **no revisar la reproducción ni obtener una transcripción íntegra**. Por tanto, no se atribuyen fallos a fotogramas que no se han visto. Las búsquedas específicas en X/Twitter no aportaron un testimonio pertinente verificable. Tampoco se encontró un reporte público comprobable de la mano que desaparece y reaparece: ese caso procede del autor.

## Storyboard Studio está dentro de Flow

El catálogo oficial identifica **Storyboard Studio**, creado por Google, con la descripción «Write a script, create the cast, and visualize a storyboard». Es una herramienta dentro del ecosistema Flow. No confundirla con servicios externos del mismo nombre, Autodesk Flow Studio ni un storyboard solicitado por chat al agente. [Catálogo de Google](https://labs.google/fx/cs/tools/flow?isTvMode=true).

Google documenta que sus **Tools** son pequeñas aplicaciones reutilizables y modificables. Un enlace compartido conserva la versión de la herramienta que se compartió: una demo de una copia modificada puede tener funciones distintas de la plantilla original. Los medios generados por una Tool se guardan en el proyecto abierto; eso no acredita que también se conserve todo su guion y sus asociaciones internas. [Ayuda de Tools](https://support.google.com/flow/answer/17104535?hl=en).

**¿La misma tecnología?** Storyboard Studio usa la infraestructura de Flow, pero no se ha verificado qué modelo ni qué contexto recibe cada operación de su plantilla. Flow ofrece varios modelos para imágenes y vídeo; no corresponde afirmar que el storyboard sea «Veo por debajo» ni que cada panel se genere con el mismo modelo que el clip final. [Modelos y funciones de Flow](https://support.google.com/flow/answer/16352836?hl=en).

## Flujo de entrada a salida

La secuencia **Script → Assets → Storyboard** aparece en testimonios directos y descripciones de demos. Su lectura práctica:

| Fase | Trabajo del autor | Qué comprobar antes de seguir |
|---|---|---|
| Script | Introducir el guion textual, separado por escenas y planos; elegir el estilo si la versión lo solicita. | Orden, personajes, acciones y diálogos extraídos. Que no haya convertido una instrucción en un personaje. |
| Assets / cast | Revisar el reparto y los recursos que la herramienta obtiene del texto. | Identidad, forma del personaje, vestuario y estado; referencia efectivamente asociada. |
| Storyboard | Generar las imágenes de las escenas y revisar la secuencia. | Anatomía, posiciones, objetos y cambios de estado entre imágenes consecutivas. |
| Vídeo en Flow | Utilizar los paneles aprobados y las referencias para generar los clips. | Que el movimiento conserve lo aprobado en la imagen fija. |

Este recorrido está descrito por usuarios de la herramienta, no por una especificación pública completa de su interfaz. Véanse el [testimonio sobre Script y Assets](https://www.reddit.com/r/GoogleFlow/comments/1uaz5d3/help_using_storyboard_studio_in_google_flow/) y la [demo de Nova Autonomous — descripción consultada](https://zolotube.com/watch?v=k2V4v4Jh3Wk).

### Formato de guion aceptado

Hay evidencia de uso de **texto libre**: historias, esquemas en prosa e incluso letras de canciones. Que entre el texto no significa que produzca un desglose útil. El testimonio de Reddit distingue precisamente entre haberlo introducido y conseguir acciones bien interpretadas.

No se ha localizado una especificación oficial del parser de Storyboard Studio: **importación nativa de PDF, DOCX, FDX, Fountain, JSON o archivos Markdown: no confirmado / puede haber cambiado**. Tampoco hay un máximo verificado de palabras, escenas o planos para esta plantilla. Trabajar con texto pegado en Script evita depender de un importador no acreditado.

Los rótulos `ESCENA`, `PLANO` y `ESTADO` de los ejemplos siguientes son organización legible para el modelo y para el autor. No son comandos. Después de introducirlos hay que comprobar cómo se han convertido en escenas y paneles: escribir tres planos no demuestra que la herramienta haya creado exactamente tres.

### ¿Puede reutilizar las imágenes de character_library/?

**En Flow, sí está documentada la incorporación de referencias desde el equipo. En el cast interno de la plantilla Storyboard Studio, no está suficientemente confirmada.** Son dos operaciones diferentes. La ayuda de Flow describe referencias visuales, ingredientes y selección de recursos mediante `@`; no demuestra que esos recursos se vinculen automáticamente a las fichas de Assets de esta Tool. [Referencias en Flow](https://support.google.com/flow/answer/16353334?hl=en).

En el hilo de Reddit, varios usuarios no consiguen importar sus personajes ni reasociar los ya generados. Una creadora que modificó Storyboard Studio relata que tuvo que añadir la carga de referencias existentes a su copia. Esto acredita una limitación en aquellas versiones, no que toda versión actual carezca de ella. [Reddit](https://www.reddit.com/r/GoogleFlow/comments/1uaz5d3/help_using_storyboard_studio_in_google_flow/), [experiencia de Carla Engelbrecht](https://www.linkedin.com/pulse/new-google-flow-ai-animation-pipeline-win-almost-dr-carla-engelbrecht-cbh9c).

Procedimiento para esta trilogía:

1. Abrir la Tool y comprobar si permite seleccionar una imagen existente para cada ficha de reparto. **No pulsar generación automática como sustituto de cargar el personaje aprobado.**
2. Si permite asociarla, comprobar la miniatura vinculada y generar una prueba corta. Un nombre coincidente no prueba que se haya adjuntado la imagen.
3. Si no permite hacerlo, usar Storyboard Studio como borrador de composición. Crear las imágenes definitivas en el espacio de imágenes de Flow con las referencias existentes, y pasar después a vídeo. La incorporación de medios y su edición sí están documentadas allí. [Imágenes en Flow](https://support.google.com/flow/answer/16729550?hl=en).
4. Registrar en la hoja de trabajo el archivo real utilizado. Una ruta escrita como `character_library/...` en el guion es una anotación: Google no puede leer el repositorio local por recibir ese texto.

No hace falta un nuevo casting. Las formas humana y celestial deben llevar identificadores distintos y referencias correspondientes; no permitir que el desglose las funda por compartir identidad narrativa.

### ¿Entrega imágenes o vídeo?

El resultado básico acreditado es **una secuencia de imágenes de storyboard**. En su experiencia de junio, Engelbrecht añadió una cuarta etapa de animación mediante Remix: no era prudente atribuir esa ampliación a la plantilla original. Las demos posteriores describen el paso de paneles a clips en Flow. **Un botón de animación dentro de toda versión de Storyboard Studio: no confirmado / puede haber cambiado.** [Experiencia de modificación](https://www.linkedin.com/pulse/new-google-flow-ai-animation-pipeline-win-almost-dr-carla-engelbrecht-cbh9c).

## Dónde se rompe la continuidad

**Caso público concreto.** Una usuaria de Storyboard Studio cuenta que las letras de una canción y después un esquema en prosa resultaron insuficientes. En una escena de coche, no bastaba con decir que Amy recogía a Brandy: necesitaba especificar la puerta del acompañante. Aun así, durante algunos clips conductora y pasajera intercambiaban posiciones. Es un fallo reportado del recorrido Storyboard Studio–Flow; no permite atribuir todos los errores al generador de paneles. [Testimonio original](https://www.reddit.com/r/GoogleFlow/comments/1uaz5d3/help_using_storyboard_studio_in_google_flow/).

**Otro fallo distinto: perder la referencia.** En ese mismo hilo, el guion reabierto conservaba los espacios para personajes, pero las imágenes seguían en All Media sin estar asociadas a Assets. El usuario encontraba una invitación a generar personajes nuevos. Estar en el mismo proyecto no había bastado para restaurar el reparto.

**Entorno que cambia.** Engelbrecht describe variaciones de una torre y su colocación al trabajar sobre una modificación de Storyboard Studio. Propuso reutilizar un panel previo como referencia de los siguientes. Es un testimonio de continuidad espacial, no una demostración de que encadenar referencias resuelva toda la anatomía. [Relato de la prueba](https://www.linkedin.com/pulse/new-google-flow-ai-animation-pipeline-win-almost-dr-carla-engelbrecht-cbh9c).

Para diagnosticar la mano, separar estas posibilidades. Son hipótesis de producción, no una inspección del código interno:

| Fallo | Pregunta de diagnóstico | Intervención |
|---|---|---|
| Error anatómico | ¿El personaje debía conservar ambas manos? | Rechazar la imagen defectuosa. No convertir el error en una lesión del canon. |
| Estado omitido | ¿La pérdida es narrativa, pero solo se menciona en un plano? | Declarar la ausencia y el lado anatómico en todos los planos posteriores afectados. |
| Referencia contradictoria | ¿Se utiliza una imagen anterior a la lesión? | Preparar una variante del estado correcto a partir de la referencia aprobada y revisar su identidad. |
| Reparto o asociación perdidos | ¿El plano recibió realmente el recurso correcto? | Comprobar la asociación, especialmente tras recargar, antes de reescribir todo el guion. |
| Estado correcto en fijo, incorrecto en movimiento | ¿La mano reaparece dentro del clip? | Corregir la generación de vídeo; aprobar un panel no valida los fotogramas intermedios. |
| Falta de visibilidad | ¿La mano está detrás del cuerpo o fuera de campo? | Distinguir ocultación de ausencia. Revisar un encuadre donde pueda comprobarse. |

No hay evidencia pública suficiente para explicar el caso del autor exclusivamente por «guion demasiado corto». La ambigüedad puede contribuir, pero también hay fallos con instrucciones explícitas.

## Cuánto detalle poner: estado comprobable por plano

**Propuesta de producción.** Aplicar calibre B al guion técnico: hechos visibles, verbos concretos y una acción principal por plano. La información útil es la que permite decidir si la imagen es correcta.

- **Identidad:** identificador estable, forma y referencia aprobada. Evitar alternar nombre, alias y títulos sin correspondencia explícita.
- **Estado de entrada:** anatomía relevante, heridas, ropa, suciedad, objeto y mano que lo sostiene. Separar el estado duradero del gesto momentáneo.
- **Espacio:** quién ocupa cada lado de pantalla, orientación y lugar de los objetos. «Izquierda anatómica» y «izquierda de pantalla» no son intercambiables.
- **Acción:** sujeto, verbo y objeto. Para una transferencia, indicar origen, destino y momento del cambio de posesión.
- **Encuadre:** tamaño de plano y qué debe quedar visible. Una imagen fija representa un instante; el movimiento se describe aparte para vídeo.
- **Estado de salida:** repetir qué cambia y qué persiste. Debe coincidir con la entrada del plano siguiente salvo elipsis declarada.
- **Sonido:** diálogo literal con hablante; narración fuera de campo separada de las personas visibles.

No hay una longitud óptima verificada. Añadir adjetivos de calidad, biografías o varios movimientos simultáneos no sustituye estos datos. No trasladar al guion la interioridad de la novela sin especificar una conducta visible.

### Ejemplo del problema de la mano

Ejercicio inventado para probar continuidad; **no introduce una amputación, vestuario ni utilería en el canon**.

Entrada insuficiente:

> El centinela herido cruza la puerta. Mira la llave. Primer plano de su reacción.

Entrada propuesta para pegar como texto y revisar después del desglose:

```text
SECUENCIA DE PRUEBA — TRES PLANOS, SIN ELIPSIS
Estilo: conservar el de las referencias aprobadas. Formato horizontal 16:9.
Personaje visible: CENTINELA_A. Una sola persona en los tres planos.
Identidad: la de la referencia adjunta de CENTINELA_A.
Estado persistente: mano izquierda anatómica ausente desde antes de la escena;
muñeca izquierda vendada. Mano derecha intacta. Túnica gris sin cambios.
Objeto: una llave de hierro, sostenida siempre con la mano derecha.
Lugar: una puerta de madera abierta; pared de piedra; luz desde la puerta.
No se produce curación ni transferencia de la llave en esta secuencia.

PLANO P01 — PLANO MEDIO FRONTAL
Entrada: CENTINELA_A está en el umbral, de frente a cámara.
Acción: avanza un paso hacia el interior.
Panel fijo: justo al terminar el paso; ambos antebrazos quedan visibles.
Continuidad: muñeca izquierda anatómica vendada, sin mano izquierda;
la derecha intacta sostiene la llave a la altura de la cintura.
Salida: queda dentro de la habitación; conserva la llave en la derecha.
Diálogo: ninguno.

PLANO P02 — DETALLE DE LA MANO DERECHA
Entrada: CENTINELA_A ya está dentro; conserva la llave en la derecha.
Acción: abre los dedos derechos para mirar la llave sobre su palma.
Panel fijo: palma derecha abierta con la única llave de hierro.
Continuidad: mano izquierda anatómica ausente; muñeca izquierda vendada,
fuera de cuadro. No interviene otra mano. No hay transferencia del objeto.
Salida: llave apoyada en la palma derecha abierta.
Diálogo: ninguno.

PLANO P03 — PLANO MEDIO FRONTAL, MISMO EJE QUE P01
Entrada: llave sobre la palma derecha; muñeca izquierda vendada y sin mano.
Acción: CENTINELA_A levanta la mirada hacia la puerta.
Panel fijo: rostro orientado a la puerta, antebrazos visibles.
Continuidad: misma túnica gris; mano izquierda anatómica ausente;
llave en la palma derecha abierta. Puerta y luz conservan su posición.
Salida: cambia la mirada; anatomía, ropa y posesión de la llave permanecen.
Diálogo: ninguno.
```

Si la mano **no debe faltar**, sustituir el estado completo: «Ambas manos anatómicamente intactas; derecha sostiene la llave; izquierda vacía». No conservar instrucciones de amputación de esta prueba. La imagen de referencia debe concordar con la versión elegida.

### Plantilla para los capítulos

```text
EPISODIO / ESCENA: [identificadores]
FUENTE: [capítulo y fragmento aprobado]
CONTINUIDAD TEMPORAL: [continuación / elipsis / recuerdo]
PERSONAJES VISIBLES: [ID, forma, referencia asociada, estado actual]
LUGAR: [referencia, estado actual, posiciones y luz]

PLANO [ID]
Encuadre e instante del panel: [...]
Estado de entrada: [...]
Acción principal: [...]
Estado de salida: [...]
Rasgos que deben persistir en este plano: [...]
Diálogo literal y hablante: [...]
Narración fuera de campo: [...]
Movimiento previsto para el clip: [...]
```

Completar los campos desde el capítulo y las fichas aprobadas. Si no consta qué mano está lesionada o qué forma aparece, dejarlo pendiente antes de generar: no resolverlo inventando canon. En EN y ES, mantener los mismos identificadores y estados; traducir las instrucciones sin intercambiar lados ni alias. No hay evidencia comparativa que permita prometer mayor consistencia por escribir en inglés. Conservar las réplicas de cada versión aprobada.

## Mismo cast, proyecto e hilo: qué aporta cada uno

**Mismo cast:** reutilizar la asociación correcta, sin regenerar la identidad para cada plano. Una referencia facial no documenta necesariamente las manos; comprobar que los rasgos críticos sean visibles en una referencia o en el panel aprobado.

**Mismo proyecto:** facilita localizar los recursos. Antes de abandonar una sesión, conservar el guion y, si la Tool ofrece guardado o exportación de su estado, comprobar que restaura las asociaciones. Tener las imágenes en All Media no basta, como muestra el reporte citado.

**Mismo hilo:** la ayuda actual de Flow sí documenta sesiones del agente guardadas por proyecto e instrucciones acompañadas de referencias. Conviene conservar la conversación de una secuencia cuando se usa ese agente. **No está confirmado que el generador interno de Storyboard Studio herede todo ese historial, ni que mantener una pestaña abierta bloquee la anatomía.** [Sesiones e instrucciones del agente](https://support.google.com/flow/answer/17093911?hl=en).

Trabajar por secuencias cortas es una propuesta para detectar errores pronto, no un límite de la herramienta. Repetir el estado crítico en cada plano incluso cuando se trabaje en el mismo hilo.

## Demos localizadas: qué enseñan y qué no demuestran

Análisis limitado a las descripciones y capítulos disponibles. Los tiempos siguientes son los publicados por sus autores, no marcas de fallos observados durante esta investigación.

| Demo | Guion y recorrido descritos | Utilidad y límite |
|---|---|---|
| **Nova Autonomous — How to Use Storyboard Studio in Google Flow (Beginner Friendly)**, 07-08-2026 | Anuncio de café: historia en una caja de texto, reparto y lugares a 1:26, paneles a 3:05 y vídeo a 4:41. El prompt completo se anuncia en un comentario fijado no recuperado. | Su descripción advierte que hay que preparar Assets antes de los paneles y referenciar personajes al animar. También reporta que la voz en off puede convertirse en un personaje visible. No se verificó visualmente la continuidad del anuncio. |
| **Luis Valencia–MarketinIA — Crea películas completas con google FLOW: Guía de Storyboard Studio**, 02-08-2026 | Fantasía medieval; guion generado con IA de seis escenas a 2:45; recursos a 3:33; clips en Flow a 6:17; montaje en Clipchamp a 8:56; resultado a 9:33. | Es el caso temático más cercano. La descripción no reproduce el guion: no permite medir su detalle ni concluir que conserve lesiones entre planos. |
| **Gk Mamun — How to Use Storyboard Studio in Google Flow (Google Storyboard Studio Tutorial for Beginners)**, 11-08-2026 | Anuncio: Script a 2:30, Assets a 2:46, storyboard a 3:15, clips a 6:15; prompt anunciado a 7:33. | Permite localizar la entrada concreta para una revisión manual posterior. No se pudo transcribir ese prompt ni auditar el resultado. |

Descripciones consultadas: [Nova](https://zolotube.com/watch?v=k2V4v4Jh3Wk), [Luis Valencia](https://zolotube.com/watch?v=ZB3VxGWjOSY), [Gk Mamun](https://zolotube.com/watch?v=MKGyBUfJK6o). En Fuentes están los enlaces originales de YouTube.

Como contraste, **Personalize Your AI Animation Tools with Google Flow**, de Carla Engelbrecht, separa la exploración de Storyboard Studio a **31:53** de su modificación a **38:51**. Esa distinción ayuda a identificar cuándo una demo deja de mostrar la plantilla de partida. Solo se consultaron el programa y los capítulos publicados. [Clase y grabación](https://maven.com/p/208fd3).

**Conclusión de la revisión de demos:** no se ha podido comprobar si reproducen el fallo de la mano. Las promesas de consistencia en títulos o descripciones no constituyen una prueba. Sí hay un ejemplo textual de usuario —el coche— que muestra por qué especificar posiciones y transiciones ayuda sin resolver todos los fallos.

## Del panel aprobado al vídeo en Flow

La combinación es viable: Flow documenta generación con imágenes como fotogramas iniciales/finales y con recursos de referencia. Adjuntar los medios y describir su función; el texto debe concordar con las imágenes. La disponibilidad depende del modelo seleccionado. [Creación de vídeo](https://support.google.com/flow/answer/16353334?hl=en), [compatibilidad por modelo](https://support.google.com/flow/answer/16352836?hl=en).

Propuesta de trabajo:

1. Aprobar el panel contra `character_library/` y el estado narrativo.
2. Usarlo como entrada visual del plano en Flow. Si la Tool no conserva bien el personaje, preparar primero ese panel en el editor de imágenes con la referencia existente.
3. Describir el movimiento de ese plano y repetir sus condiciones críticas. Una duración deseada en el guion no obliga a la herramienta: elegir una duración admitida por el modelo.
4. Revisar inicio, desarrollo y final del clip; después revisar el corte con sus vecinos. No pasar automáticamente un fotograma final defectuoso al siguiente clip.
5. Reparar o regenerar el elemento fallido. Flow permite edición de imágenes, incluida selección de una zona, pero la corrección también necesita revisión. [Edición de imágenes](https://support.google.com/flow/answer/16729550?hl=en).

## Prueba de aceptación antes de adaptar un capítulo entero

**Propuesta, todavía no ejecutada.** Probar tres planos: presentación, detalle del rasgo crítico y regreso a un plano donde vuelva a verse. Mantener la misma referencia, estilo y modelo; comparar un guion esquemático con otro que explicite estados. Hacer varias generaciones por condición: un acierto aislado no valida el método. Después probar por separado la reapertura del proyecto, para no confundir persistencia de Assets con calidad del prompt.

Registrar por plano: versión del guion, referencia efectivamente asociada, modelo visible, número de intento y motivo de rechazo. Evaluar:

- Identidad y forma correcta del personaje.
- Anatomía y lesiones según ese momento de la historia.
- Ropa, armas y objetos; posesión y mano correspondiente.
- Posición, mirada, luz y estado del lugar.
- Correspondencia entre salida de un plano y entrada del siguiente.
- Conservación de todo lo anterior al animar.

Para aceptar una secuencia, ningún plano puede contradecir el canon. Si un detalle no se ve, marcarlo como **no evaluable**, no como correcto. Si el formato detallado sigue fallando, revisar la referencia y simplificar la acción; recurrir a corrección visual o composición controlada cuando haga falta. No seguir alargando indefinidamente el prompt ni aceptar una regeneración de la mano porque el resto del plano sea atractivo.

**Expectativa realista:** Storyboard Studio puede ayudar a planificar y detectar problemas antes del vídeo. La evidencia consultada no acredita una solución completa de continuidad corporal, espacial o temporal. Esta adaptación necesita guion explícito, referencias concordantes y revisión humana plano a plano.

## Fuentes

Consulta: **2026-09-16**. Las páginas de producto son cambiantes; los testimonios describen la versión utilizada por su autor.

### Google: identificación y capacidades documentadas

- [Google Flow — catálogo con Storyboard Studio](https://labs.google/fx/cs/tools/flow?isTvMode=true). La ficha indexada identifica nombre, autor y propósito; el acceso actual redirige a Flow.
- [Storyboard Studio — enlace compartido de la Tool](https://labs.google/fx/tools/flow/shared/tool/79c9d2e6-4ad6-4636-ad05-22022f8a5a74). Consultado; interfaz interna no accesible en la lectura pública.
- [Create & manage Tools in Google Flow](https://support.google.com/flow/answer/17104535?hl=en). Tools, Remix, versiones compartidas y medios guardados en el proyecto.
- [Create videos in Google Flow](https://support.google.com/flow/answer/16353334?hl=en). Referencias, ingredientes, fotogramas y precaución frente a instrucciones contradictorias.
- [Create & edit images in Google Flow](https://support.google.com/flow/answer/16729550?hl=en). Referencias y corrección de imágenes.
- [Use the Google Flow Agent](https://support.google.com/flow/answer/17093911?hl=en). Sesiones e instrucciones; no equivale a la persistencia interna de Storyboard Studio.
- [Learn about Google Flow models & supported features](https://support.google.com/flow/answer/16352836?hl=en). Diferencias de compatibilidad entre modelos.
- [New agents, mobile apps and Gemini Omni for Google Flow and Google Flow Music](https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates/), 19-05-2026. Contexto oficial de Tools y modelos; no es un manual específico de Storyboard Studio.

### Testimonios directos

- [Help — Using Storyboard Studio in Google Flow](https://www.reddit.com/r/GoogleFlow/comments/1uaz5d3/help_using_storyboard_studio_in_google_flow/), r/GoogleFlow. Pérdida de asociaciones, dudas sobre importar personajes y ejemplo del coche.
- [Google Flow AI Animation Tool: New Pipeline Update Review](https://www.linkedin.com/pulse/new-google-flow-ai-animation-pipeline-win-almost-dr-carla-engelbrecht-cbh9c), Carla Engelbrecht, 02-06-2026. Diferencia entre plantilla y modificaciones; referencias, animación y continuidad del entorno.

### Vídeos y descripciones consultadas

- [How to Use Storyboard Studio in Google Flow (Beginner Friendly)](https://www.youtube.com/watch?v=k2V4v4Jh3Wk), Nova Autonomous, 07-08-2026. [Descripción y capítulos accesibles](https://zolotube.com/watch?v=k2V4v4Jh3Wk).
- [Crea películas completas con google FLOW: Guía de Storyboard Studio](https://www.youtube.com/watch?v=ZB3VxGWjOSY), Luis Valencia–MarketinIA, 02-08-2026. [Descripción y capítulos indexados](https://zolotube.com/watch?v=ZB3VxGWjOSY).
- [How to Use Storyboard Studio in Google Flow (Google Storyboard Studio Tutorial for Beginners)](https://www.youtube.com/watch?v=MKGyBUfJK6o), Gk Mamun, 11-08-2026. [Descripción y capítulos accesibles](https://zolotube.com/watch?v=MKGyBUfJK6o).
- [How to Create AI Movies with Consistent Characters (FREE) | Google Flow Storyboard Studio](https://www.youtube.com/watch?v=JOaR-v2oPJg), Hindi AI Gyaan, 08-07-2026. Descripción indexada consultada; promesa de consistencia no auditada visualmente.
- [How to Create Animated Videos with Google Flow's Storyboard Studio](https://www.youtube.com/watch?v=EVR7W_9dqZ4), AI Auto Lab, 26-07-2026. Descripción y capítulos indexados consultados; revisión a 2:40 y resultado anunciado a 4:00.
- [Personalize Your AI Animation Tools with Google Flow](https://maven.com/p/208fd3), Carla Engelbrecht, 02-07-2026. Programa de la demo; plantilla a 31:53 y Remix a 38:51.

### Material contrastado que no se toma como prueba de capacidades

- [How to Use Google Flow Storyboard Studio: Script Uploads, Custom Characters & Scenes](https://www.nadhebe.com/tutorials/building-pre-production-storyboards-google-flow/). Afirma importación de archivos y controles concretos que no se pudieron corroborar mediante documentación oficial ni una demostración accesible. No se adoptan como instrucciones verificadas.
- [Google Flow Storyboard Studio Guide: Missing Script Fix & Troubleshooting](https://nadhebe.com/tutorials/google-flow-storyboard-studio-guide/). No se adopta su explicación de almacenamiento interno ni sus remedios de navegador: los testimonios encontrados no prueban esas causas.
