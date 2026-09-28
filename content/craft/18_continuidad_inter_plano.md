# 18 — Continuidad inter-plano (2026-09-16)
**BORRADOR — pendiente de aprobación del autor**

Problema del autor: Storyboard Studio genera planos donde una mano desaparece y vuelve a aparecer. El agente de **Continuidad inter-plano** debe impedir que un plano aprobado entregue al siguiente un cuerpo, un objeto o una herida distintos sin una acción que lo explique.

**Regla de trabajo: cada plano recibe un estado físico, muestra cambios concretos y entrega un estado comprobado. Lo que sale de encuadre no deja de existir.** Una referencia de personaje fija su identidad; hace falta además registrar qué está haciendo y qué conserva en ese momento.

## Qué se toma del cine real

El/la *script supervisor* desglosa la continuidad por escenas y días de la historia, sigue acciones y miradas, registra vestuario y utilería con notas y fotografías, y conserva datos de plano, toma y cámara para montaje. La continuidad se comprueba en el orden narrativo aunque se ruede en otro orden. [ScreenSkills: Script supervisor](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/technical/script-supervisor-film-and-tv-drama/).

Traslado operativo al proyecto — estos son los datos que debe pedir nuestro agente:

| Área | Anotación que permite reconstruir el instante del corte |
| --- | --- |
| Cuerpo | De pie/sentado/arrodillado, orientación del torso, apoyo del peso, pie adelantado, fase del gesto. |
| Manos y contacto | Mano anatómica, altura, palma, dedos, objeto sujetado, agarre y punto de contacto. «Mano cerca del vaso» no equivale a «vaso sujeto». |
| Utilería | Identificador del objeto, dueño, posición, orientación, estado y cantidades: vaso a media altura de líquido, dos piezas sobre la mesa. |
| Daño y vestuario | Herida y lado del cuerpo, sangre seca/fresca, rotura, suciedad, cierres, guantes, pliegues relevantes. |
| Espacio | Posición respecto a marcas del decorado, objetivo de la mirada, dirección de desplazamiento y lado del eje de cámara. |
| Toma | Acción o réplica donde se corta, duración, versión elegida y fotografías de entrada/salida. |

La nota útil es «mano derecha sostiene el vaso por el tercio inferior; líquido a mitad; izquierda apoyada en la mesa». «Mantener continuidad» no permite reconstruir nada. Para nuestros ángeles se añaden alas, plumas, emblemas y efectos luminosos al mismo inventario físico.

## Herramientas: qué está verificado y qué no

Consulta documental: **16 de septiembre de 2026**. Las funciones dependen de modelo, interfaz, región y acceso. Registrar la configuración utilizada; un tutorial antiguo no prueba que el botón siga disponible hoy.

| Herramienta | Evidencia consultada | Aplicación y límite |
| --- | --- | --- |
| Google Flow | La ayuda documenta imágenes de inicio/final y referencias mediante Ingredients. | Usar la imagen de arranque para la composición y las referencias para identidad. No asumir que cualquier modelo admite combinar todos los tipos de entrada. [Crear vídeos](https://support.google.com/flow/answer/16353334?hl=en). |
| Google Flow: edición | Documenta guardar un frame y reutilizarlo como ingrediente, inicio o final; Extend para vídeos generados con Veo; Scenebuilder para ordenar y recortar clips. | Permite construir la cadena manualmente. Ordenar clips no corrige su anatomía. [Editar vídeos y construir escenas](https://support.google.com/flow/answer/16935718?hl=en). |
| Google Storyboard Studio | El catálogo oficial de Flow lo presenta como herramienta de Google para escribir guion, crear reparto y visualizar storyboard. | Existencia confirmada en el catálogo indexado; la apertura directa redirigió a acceso con sesión. **Herencia automática del estado físico, importación de nuestro JSON y encadenamiento automático de frames: no confirmado / puede haber cambiado.** [Catálogo de Flow](https://labs.google/fx/es/tools/flow). |
| Runway Gen-4 | La documentación identifica la imagen de entrada como primer frame y ofrece Use Current Frame para reutilizar el fotograma visible. La página ya avisa de que describe una generación anterior. | Técnica documentada para Gen-4; no extrapolar sus controles a toda versión posterior. [Creating with Gen-4 Video](https://help.runwayml.com/hc/en-us/articles/37327109429011-Creating-with-Gen-4-Video). |
| Kling VIDEO 3.0 | La guía oficial incluye Start & End Frames, referencias de elementos con frame inicial y modos de varios planos. | Controles de guía, sujetos a revisión del resultado. La afirmación comercial de consistencia no sustituye una comprobación de manos y objetos. [Guía VIDEO 3.0](https://app.klingai.com/cn/quickstart/klingai-video-3-model-user-guide). |
| Sora | La API documenta extensión de un vídeo completado mediante vídeo y prompt. Esa misma referencia anuncia su cierre para el 24-09-2026. | Comparador técnico para la extensión con contexto de vídeo; no basar un pipeline nuevo en su disponibilidad. No se presupone una interfaz de storyboard vigente. [Create a video extension](https://developers.openai.com/api/reference/typescript/resources/videos/methods/extend). |

El JSON que sigue es **diseño del proyecto**, no un formato de importación oficial. El agente lo convierte en instrucciones de plano y adjunta las imágenes mediante los controles realmente disponibles. Escribir una ruta de archivo dentro del prompt no carga la imagen.

## Técnicas encontradas y lo que aportan

### Último frame como primer frame

La operación verificable en Flow es guardar el fotograma y asignarlo como inicio de la siguiente generación. Conserva una referencia visual precisa del punto de unión. No aporta por sí sola trayectoria, velocidad ni lo que queda detrás del cuerpo; tampoco demuestra que el generador vaya a conservar cada detalle.

El tutorial de AI Video School **How to Create Single Continuous Shots with Veo in Google Flow**, de julio de 2025, compara extensión y encadenamiento de fotogramas. Se consultaron su página de YouTube y el texto accesible de la transcripción; no se inspeccionó el metraje completo. Sus restricciones antiguas de audio/modelo no se trasladan a la interfaz actual. [Vídeo](https://www.youtube.com/watch?v=6iBc4aoiwf4), [transcripción accesible](https://glasp.co/youtube/6iBc4aoiwf4).

Hay testimonios directos de usuarios que obtienen cambios de exposición y un tono progresivamente naranja al reutilizar frames. Otro hilo describe discrepancias entre el final solicitado y el obtenido. Son reportes de versiones y casos concretos, sin tasa de fallo generalizable. Justifican revisar la cadena, no declarar que siempre fracasa. [Image to video consistency](https://www.reddit.com/r/VEO3/comments/1n53ow8/), [Veo 3.1 fast with last frame issue](https://www.reddit.com/r/VEO3/comments/1p85j89/veo_31_fast_with_last_frame_issue/).

### Extensión, dos extremos y referencias persistentes

- **Extender un vídeo aprobado:** opción para continuar la acción usando el clip anterior. Comprobar en la cuenta el modelo compatible y revisar de nuevo la unión. No confundir extensión con un corte a otro ángulo.
- **Dar inicio y final:** útil cuando una acción debe terminar en una pose determinada. Los extremos deben poder conectarse con el movimiento y tiempo pedidos. Revisar el recorrido: dos imágenes correctas pueden ocultar una mano deformada entre ambas.
- **Mantener referencias de identidad y de escenario:** Runway recomienda vistas del personaje y del entorno para construir secuencias. Aquí se reutilizan las referencias existentes de `character_library/`; no se abre un proceso de casting ni de rediseño. [How to create longer videos and films](https://help.runwayml.com/hc/en-us/articles/26871350018835-How-to-create-longer-videos-and-films).
- **Separar acciones complejas en planos controlables:** propuesta de producción del proyecto. Un cambio de agarre, una oclusión y un cambio de cámara simultáneos dificultan localizar el fallo. Planificar un gesto principal por generación cuando el montaje lo permita.

### Qué enseñan las pruebas comparativas

Curious Refuge publicó una prueba con las mismas imágenes inicial/final en Veo 3.1 y Kling 2.5 Turbo: abrir una puerta y coger un bocadillo con ambas manos. El autor reporta errores de interacción y conservación del objeto. Es evidencia primaria de esa prueba, no una clasificación actual de modelos. [Comparativa y descripción de resultados](https://www.linkedin.com/posts/curiousrefuge_kling-and-veo-are-two-of-the-biggest-kids-activity-7399196716010242048-a1Vr).

Traction/Futureproof comparó movimiento con una misma imagen y prompt en varias herramientas; su informe de agosto de 2025 describe deformaciones de extremidades. Sirve para decidir **qué inspeccionar**, no para atribuir esos resultados a las versiones de hoy. [Can AI Video Keep Up with Human Movement?](https://www.tractionco.com/insights/can-ai-video-keep-up-with-human-movement-a-futureproof-field-test).

Se hicieron búsquedas específicas de tutoriales, demos y comparativas en YouTube, además de consultas en español, documentación, Reddit y X/Twitter. YouTube devolvió contenido parcial o errores de acceso en varias aperturas. Las búsquedas de X/Twitter no aportaron una prueba pertinente y verificable; no se usan como respaldo. No se ejecutó un ensayo propio de generación: el procedimiento siguiente debe validarse con clips del proyecto.

## Procedimiento del agente: del plano aprobado al siguiente

1. **Preparar el estado de escena.** Leer el pasaje adaptado y elegir forma/estado narrativo y referencias vigentes. Fijar posiciones, objetos, heridas y eje de cámara. Mantener un inventario también de personajes y objetos temporalmente fuera de plano.
2. **Resolver la entrada.** Recuperar el estado de salida aprobado del plano anterior de la misma escena. Si el montaje intercala otra escena, recuperar la última versión de esta escena; no heredar del clip contiguo de otra localización. El primer plano necesita una entrada explícita derivada del guion.
3. **Elegir el enlace.** Continuación de cámara: último frame aprobado o extensión. Corte a otro ángulo: construir y aprobar la nueva imagen inicial con las mismas posiciones físicas, usando el final anterior como referencia de estado. No usarlo obligatoriamente como primer frame: forzaría el encuadre viejo. Elipsis: declarar tiempo y cambios autorizados por el guion.
4. **Describir entrada, acción y salida deseada.** Nombrar manos por lado anatómico, contacto y visibilidad. Añadir solo los cambios previstos. «Sigue igual» queda prohibido en los datos entregados al generador.
5. **Generar y mirar el clip entero.** Comparar con la entrada y con las referencias maestras. Inspeccionar especialmente oclusiones, entradas/salidas de objetos, agarres y cambios de dirección. Un frame final correcto no aprueba el tramo anterior.
6. **Elegir la toma y el corte.** El frame semilla es el último fotograma **retenido en el montaje**, identificado por índice y tiempo. Si el archivo acaba deformado, recortar antes solo cuando se preserve la acción necesaria; si no, regenerar. Exportar la imagen del frame seleccionado sin interfaz superpuesta y conservando proporciones.
7. **Registrar lo observado.** Escribir el estado final y la descripción del frame a partir de la toma elegida. Compararlos con lo requerido: una mano desaparecida es un defecto, nunca un cambio válido que el pipeline deba heredar.
8. **Aprobar y publicar la herencia.** Solo una salida revisada alimenta otra generación. Si cambia la toma o el corte de un plano, invalidar las entradas y uniones dependientes y revisarlas. Guardar vínculo a versiones, no solo nombres de archivos reutilizables.

**Tres verificaciones por enlace:** referencia maestra ↔ plano actual; final aprobado de A ↔ inicio de B; desarrollo completo de B ↔ cambios autorizados. La primera detecta deriva acumulada aunque cada unión aislada parezca aceptable.

La descripción textual del frame final permite reconstruir una instrucción y auditar el estado. La semilla visual es la imagen exportada. Una *seed* numérica, si el modelo la ofrece, es otro parámetro: no equivale a ninguna de las dos ni garantiza continuidad.

## Contrato de datos obligatorio por plano

Propuesta `version_esquema: "1.0"`. Claves en español y `snake_case`. Dos tipos reutilizables: **estado** y **frame**. Los campos existen desde planificación; las observaciones aún no producidas llevan `null` y bloquean la aprobación. `[]` significa ausencia comprobada de elementos, nunca «no lo he rellenado».

| Campo | Tipo y obligación |
| --- | --- |
| `version_esquema`, `id_escena`, `id_plano`, `version_plano` | Cadenas; identifican este contrato y esta revisión. |
| `fuente_narrativa` | Cadena con libro/capítulo/pasaje; en una prueba, indicarlo expresamente. |
| `id_plano_anterior`, `version_anterior` | Cadenas; `null` solo al abrir la escena, con motivo en `enlace`. |
| `referencias_personajes` | Lista: `id_personaje`, `forma`, `estados_narrativos`, `archivos`. Las rutas deben existir y corresponder a la forma elegida. |
| `enlace` | Objeto: `tipo` (`continuacion`, `cambio_angulo`, `elipsis`, `inicio_escena`), `metodo`, `tiempo_transcurrido`, `justificacion`, `frame_heredado`. Este último tiene tipo frame o `null` justificado. |
| `generacion` | Objeto: `herramienta`, `modelo`, `modo`, `fecha`, `estilo`, `relacion_aspecto`, `duracion_solicitada_s`. Desconocidos se declaran; no se inventa el modelo interno de Storyboard Studio. |
| `estado_entrada` | Estado completo requerido al comienzo. Hereda los hechos persistentes; actualiza proyección y visibilidad cuando cambia la cámara. |
| `accion_plano` | Cadena con movimiento, ritmo, apoyos/contactos y punto donde termina; referencia a réplica si la hay. |
| `cambios_autorizados` | Lista: `campo`, `antes`, `despues`, `causa`, `momento`. Vacía si nada debe cambiar. Heridas nuevas requieren respaldo narrativo. |
| `estado_salida_previsto` | Estado completo que se desea obtener. No cuenta como observación. |
| `estado_salida_observado` | Estado completo comprobado; `null` hasta revisar la toma. |
| `frame_final` | Frame real y `descripcion_textual`; `null` hasta seleccionar la toma y el corte. |
| `control_calidad` | Objeto: `resultado` (`pendiente`, `aprobado`, `rechazado`), `revision`, `evidencias`, `incidencias`. Cada incidencia identifica campo, momento, esperado, observado y reparación. |

### Tipo estado: cuerpo persistente y proyección visible

Cada estado contiene `personajes`, `objetos_escena`, `entorno` y `camara`. Incluir todos los personajes activos de la escena, aunque no aparezcan en ese encuadre.

| Campo del personaje | Contenido obligatorio |
| --- | --- |
| `id_personaje`, `pose_corporal`, `posicion_escena` | Identidad estable, apoyos/orientación y posición respecto a anclas del escenario. |
| `extremidades` | Mapa de brazos, manos, piernas/pies y alas aplicables, por lado anatómico. Cada entrada: `presencia_fisica`, `visibilidad`, `posicion`, `contacto`. |
| `objetos_en_mano` | `mano_derecha` y `mano_izquierda`: listas de identificadores. Vacías solo si están libres. El agarre se describe en `contacto`; el objeto se detalla en `objetos_escena`. |
| `heridas` | Lista con zona, lado, tipo, estado y visibilidad. Una herida tapada permanece registrada. |
| `vestuario_visible` | Mapa de piezas, color, estado y colocación. |
| `vestuario_oculto` | Mapa de piezas persistentes y causa de ocultación. |
| `direccion_mirada` | `objetivo`, `orientacion_cabeza`, `direccion_pantalla`; objetivo estable aunque cambie su proyección. |

`presencia_fisica`: `presente` o `ausente_canonico`. `visibilidad`: `visible`, `parcial`, `oculta`, `fuera_de_encuadre`, `no_aplica`. **Una mano tapada por el torso es `presente` + `oculta`; nunca `ausente_canonico`.** Una amputación solo entra con respaldo del guion. `no_aplica` sirve, por ejemplo, para alas ausentes en una forma humana, no para evitar describir una mano.

`objetos_escena` registra por objeto `id_objeto`, `ubicacion`, `portador`, `orientacion`, `estado`, `cantidad_o_nivel`, `visibilidad`. Un vaso fuera de cuadro conserva su nivel hasta que una acción lo cambie. Un objeto que pasa de mano debe conservar el mismo identificador y registrar entrega/recepción.

`entorno` registra `anclas_espaciales`, `luz`, `clima`, `estado_decorado`. `camara` registra `encuadre`, `posicion`, `eje_accion`, `lado_eje`, `movimiento`. Izquierda/derecha corporal siempre es la del personaje; izquierda/derecha de pantalla se declara aparte. Prohibido resolver un raccord invirtiendo horizontalmente una imagen sin revisar daños, armas y asimetrías.

El tipo **frame** contiene `archivo_imagen`, `archivo_video`, `version_toma`, `indice_fotograma`, `tiempo_s`, `fps`, `descripcion_textual`. Índice desde cero; en vídeo de frecuencia variable, el tiempo de presentación es la autoridad. Un frame heredado debe señalar una salida aprobada; en planificación puede estar pendiente, pero no se permite generar una continuación dependiente sin resolverlo.

### Campo nuevo: restricciones_negativas (2026-09-18, verificado por el autor)

Prueba real en Google Flow: apareció una forma de hoja/espada en el borde del encuadre en dos clips distintos de Miguel, pese a que su ficha (`character_library/angeles/Miguel/README.md`) dice explícitamente "no lleva arma, vaina ni objeto en la cadera o la espalda". Las referencias de identidad e incluso el estado estructurado no bastan para evitar que el generador invente un objeto que el canon prohíbe explícitamente — hace falta decirlo también en negativo.

Se añade al contrato de cada plano un campo `restricciones_negativas`: lista de cadenas, una por elemento que el canon prohíbe expresamente para algún personaje u objeto de la escena y que el generador podría alucinar (armas no canónicas, edificios/columnas en el fondo si la localización es desierto abierto, manos o extremidades de más, personajes adicionales no listados en `personajes_en_plano`). El agente de Continuidad rellena este campo a partir de las fichas de `personajes.md` y `character_library` ("sin arma", "sin vaina", "manos vacías salvo lo listado en objetos_en_mano"); el agente de Google Flow lo traduce a negaciones explícitas dentro del prompt principal (`"...with empty hands, no weapon, no sheath at the hip or back..."`), que es la técnica que se confirmó funcional el 2026-09-18 (ver [[14_google_flow]]).

También se confirmó que un salto de continuidad puede ocurrir **dentro de un mismo clip** (alas ausentes en el fotograma 0, presentes en el segundo 4 de un clip de 8s), no solo entre el plano A y el plano B. El paso 5 del "Procedimiento del agente" de arriba ("Generar y mirar el clip entero") ya cubre esto en diseño; esta nota confirma que es un riesgo real y observado, no solo teórico — no basta con comparar el primer y último fotograma.

### Regla de herencia y validación

`estado_entrada(B)` conserva los hechos persistentes de `estado_salida_observado(A)` y solo añade los cambios de enlace autorizados. El cambio de cámara altera visibilidad y posición en pantalla, no la mano que sostiene algo ni el ala herida. En un corte sobre movimiento se registra la fase elegida para que el gesto no se repita ni se salte.

Validación mínima: identificadores únicos; referencias existentes; ambas manos descritas; todos los objetos sujetados presentes en el inventario; correspondencia entre contactos y portadores; ningún cambio de presencia física sin causa; descripción del frame compatible con imagen y estado observado. Si algo no se puede determinar y afecta al raccord, resultado `pendiente`, con incidencia concreta.

Las versiones EN/ES usan los mismos identificadores, referencias y estados. Al traducir prompts, conservar lados anatómicos, negaciones y cantidades. El traductor no puede convertir «mano oculta» en «mano ausente».

## Ejemplo: Miguel, forma celestial vigente

Fuentes leídas: [ficha de Miguel](../lore/personajes.md), [README de identidad](../../character_library/angeles/Miguel/README.md), [forma celestial](../../character_library/angeles/Miguel/forms/celestial/README.md), [forma humana](../../character_library/angeles/Miguel/forms/human/README.md) y [estado de ala izquierda quemada](../../character_library/angeles/Miguel/states/burned_left_wing/README.md). Se inspeccionaron también `canonical/face_reference.png` y `canonical/body_reference.png`.

**Distinción de fuentes:** `personajes.md` menciona armadura con grietas antiguas y Solmire. El paquete visual vigente especifica base sin grieta en el peto, sin arma/vaina y con manos vacías. Este ejemplo usa esa base visual aprobada; no niega la existencia de Solmire ni modifica la ficha. Si un pasaje requiere arma o daño, se registra su estado narrativo antes de generar. La nota de producción que el README enlaza en `design_notes/2026-09-16_flow_storyboard_studio_cap01.md` no existe en este checkout; no se le atribuye contenido no leído.

**Ensayo técnico de raccord, no escena nueva de la novela.** Dos planos de Miguel inmóvil sobre fondo neutro, sin diálogo ni sucesos narrativos. La pose se propone para la prueba; rostro, armadura, paleta, guantes, manos vacías y alas proceden de sus referencias. Se mantiene el estilo `3D-Animation` indicado en el README vigente.

Para evitar repetir tres veces el mismo estado extenso, el ejemplo se expresa en dos bloques JSON. `estados_ejemplo` es un diccionario didáctico: antes de entregar el plano, el agente sustituye las cadenas de referencia por una copia completa del objeto. No son instrucciones `$ref` ni una función atribuida a Flow.

```json
{
  "estados_ejemplo": {
    "miguel_inmovil": {
      "personajes": [
        {
          "id_personaje": "miguel",
          "pose_corporal": "De pie, erguido, torso frontal; peso repartido; brazos separados ligeramente del tronco.",
          "posicion_escena": "Centro de la marca de ensayo, sin desplazamiento.",
          "extremidades": {
            "brazo_derecho": {"presencia_fisica": "presente", "visibilidad": "visible", "posicion": "Extendido junto al costado derecho, a la izquierda de pantalla.", "contacto": "Ninguno."},
            "mano_derecha": {"presencia_fisica": "presente", "visibilidad": "visible", "posicion": "A la altura del muslo derecho, dedos relajados, palma hacia el muslo.", "contacto": "Sin objeto ni contacto con el muslo."},
            "brazo_izquierdo": {"presencia_fisica": "presente", "visibilidad": "visible", "posicion": "Extendido junto al costado izquierdo, a la derecha de pantalla.", "contacto": "Ninguno."},
            "mano_izquierda": {"presencia_fisica": "presente", "visibilidad": "visible", "posicion": "A la altura del muslo izquierdo, dedos relajados, palma hacia el muslo.", "contacto": "Sin objeto ni contacto con el muslo."},
            "pierna_derecha": {"presencia_fisica": "presente", "visibilidad": "parcial", "posicion": "Recta bajo el torso; parte superior tapada por el faldón.", "contacto": "Apoyo a través del pie derecho."},
            "pie_derecho": {"presencia_fisica": "presente", "visibilidad": "visible", "posicion": "A la izquierda de pantalla, punta hacia cámara.", "contacto": "Planta apoyada en el suelo."},
            "pierna_izquierda": {"presencia_fisica": "presente", "visibilidad": "parcial", "posicion": "Recta bajo el torso; parte superior tapada por el faldón.", "contacto": "Apoyo a través del pie izquierdo."},
            "pie_izquierdo": {"presencia_fisica": "presente", "visibilidad": "visible", "posicion": "A la derecha de pantalla, punta hacia cámara.", "contacto": "Planta apoyada en el suelo."},
            "ala_derecha": {"presencia_fisica": "presente", "visibilidad": "parcial", "posicion": "Elevada y abierta detrás del hombro derecho, a la izquierda de pantalla; raíz oculta por el torso.", "contacto": "Ninguno."},
            "ala_izquierda": {"presencia_fisica": "presente", "visibilidad": "parcial", "posicion": "Elevada y abierta detrás del hombro izquierdo, a la derecha de pantalla; raíz oculta por el torso.", "contacto": "Ninguno."}
          },
          "objetos_en_mano": {"mano_derecha": [], "mano_izquierda": []},
          "heridas": [],
          "vestuario_visible": {
            "armadura": "Oro radiante, filigrana de plumas y canales cian; peto sin grieta; estrella cian-blanca de ocho puntas centrada sobre el esternón.",
            "guantes": "Cuero oscuro en ambas manos; conservar las protecciones doradas visibles de la referencia corporal.",
            "faldones": "Azul medianoche con bordes dorados, separados al centro, sin roturas.",
            "grebas_y_escarpes": "Oro, ambos presentes, sin daño."
          },
          "vestuario_oculto": {"tejido_posterior": "No evaluable desde delante; conservar la construcción de la referencia, sin reinterpretarla."},
          "direccion_mirada": {"objetivo": "Punto de ensayo a la altura de los ojos sobre el eje óptico.", "orientacion_cabeza": "Frontal, mentón nivelado.", "direccion_pantalla": "Hacia cámara."}
        }
      ],
      "objetos_escena": [],
      "entorno": {"anclas_espaciales": "Marca central de ensayo; fondo neutro sin utilería.", "luz": "Suave y neutra, estable; ojos y emblema cian conservan intensidad.", "clima": "No aplica al ensayo interior.", "estado_decorado": "Sin cambios."},
      "camara": {"encuadre": "Cuerpo completo con margen para manos, pies y extensión de ambas alas.", "posicion": "Frontal y fija.", "eje_accion": "Línea entre Miguel y el punto de mirada.", "lado_eje": "Sobre el eje; sin cruce.", "movimiento": "Ninguno."}
    }
  }
}
```

```json
{
  "version_esquema": "1.0",
  "id_escena": "ensayo_miguel_01",
  "id_plano": "ensayo_miguel_01_p02",
  "version_plano": "v01",
  "fuente_narrativa": "Prueba técnica sin capítulo asignado; identidad tomada de la ficha y del paquete celestial vigente.",
  "id_plano_anterior": "ensayo_miguel_01_p01",
  "version_anterior": "v01",
  "referencias_personajes": [
    {
      "id_personaje": "miguel",
      "forma": "celestial",
      "estados_narrativos": [],
      "archivos": [
        "character_library/angeles/Miguel/canonical/face_reference.png",
        "character_library/angeles/Miguel/canonical/body_reference.png"
      ]
    }
  ],
  "enlace": {
    "tipo": "continuacion",
    "metodo": "ultimo_frame_como_inicio",
    "tiempo_transcurrido": "Sin elipsis.",
    "justificacion": "Conservar exactamente pose, apoyos, manos vacías y alas de P01.",
    "frame_heredado": null
  },
  "generacion": {
    "herramienta": "Google Flow",
    "modelo": "Pendiente de registrar el modelo seleccionado en la cuenta.",
    "modo": "Frames, condicionado a disponibilidad.",
    "fecha": "2026-09-16",
    "estilo": "3D-Animation",
    "relacion_aspecto": "16:9",
    "duracion_solicitada_s": 4
  },
  "estado_entrada": "estados_ejemplo.miguel_inmovil",
  "accion_plano": "Miguel mantiene la postura durante el plano. Respiración leve del torso; manos, pies y alas conservan posición; cabeza y mirada permanecen frontales.",
  "cambios_autorizados": [],
  "estado_salida_previsto": "estados_ejemplo.miguel_inmovil",
  "estado_salida_observado": null,
  "frame_final": null,
  "control_calidad": {
    "resultado": "pendiente",
    "revision": "sin_revision",
    "evidencias": [],
    "incidencias": [
      {"campo": "enlace.frame_heredado", "momento": "Antes de generar P02", "esperado": "Frame final aprobado de P01 con imagen, toma, índice y tiempo.", "observado": "No hay clips generados en este ejemplo.", "reparacion": "Generar y aprobar P01; exportar su último frame retenido y registrar sus datos."}
    ]
  }
}
```

**No hay toma aprobada implícita en este ejemplo.** Los `null` reflejan que todavía no se han generado vídeos. Antes de generar P02 se expande el estado, se confirma duración/modelo disponible y se carga la imagen heredada. Después se completa `estado_salida_observado` a partir del vídeo y se registra `frame_final`.

Descripción textual prevista para comparar con el final real: «Miguel frontal de cuerpo completo; ambas manos enguantadas, vacías y separadas del torso a la altura de los muslos; ambos pies apoyados. Dos alas blanco perla intactas, elevadas simétricamente, con raíces ocultas tras el torso. Peto dorado sin grieta, estrella de ocho puntas centrada, faldones azul medianoche. Mira al frente. Fondo y luz neutros». Solo copiarla a `frame_final.descripcion_textual` si coincide con la imagen obtenida.

Para una prueba de oclusión, acercar después la cámara hasta dejar la mano derecha fuera de cuadro. Cambiar su `visibilidad` a `fuera_de_encuadre` y conservar `presencia_fisica: "presente"`, posición y mano vacía. Al volver a plano general, debe reaparecer la misma mano, sin objeto añadido. Si el guion activa el ala quemada, el daño corresponde al **ala izquierda anatómica**: de frente queda a la derecha del espectador; de espaldas, a la izquierda. No activar ese estado por asociación con una imagen antigua.

## Prueba de aceptación del pipeline

Propuesta de ensayo, todavía no ejecutado: generar la secuencia **general → encuadre con mano fuera de campo → general** con el estado anterior. Probar, cuando la interfaz lo permita, un enlace mediante frame exportado y otro mediante extensión. Mantener referencias y acción; registrar modelo y configuración. En el cambio de encuadre, preparar la composición nueva conforme al mismo estado.

Medir por toma: manos presentes cuando deben verse; objetos no autorizados; lado y estado de alas; correspondencia con referencia facial; deriva de color; repetición o salto de movimiento en el corte. Registrar tomas rechazadas y causa, no solo la seleccionada. Éxito mínimo: toda la secuencia cumple los estados y todas sus uniones están aprobadas. Una muestra favorable valida el caso ensayado, no garantiza otras acciones.

**Orden de reparación:** corregir datos contradictorios → corregir imagen de arranque → simplificar el gesto o separar acciones → regenerar el plano defectuoso → revisar descendientes. Un fundido, un corte de recurso o una corrección de color no arreglan una extremidad que desaparece dentro de la toma.

## Checklist de detección de salto de continuidad

- [ ] ¿A y B pertenecen a la misma escena y al momento narrativo correcto? Si hay elipsis, ¿cada cambio tiene una causa autorizada?
- [ ] ¿La entrada de B procede de la versión y del corte aprobados de A, no de una toma descartada?
- [ ] ¿Se comprobó el clip entero, además del último frame de A y el primero de B?
- [ ] ¿Cada mano, brazo, pie y ala tiene el mismo estado físico? ¿Se distingue ocultación o recorte de ausencia anatómica?
- [ ] ¿Una mano que reaparece conserva guante, posición y objeto? ¿Se ha contado algún dedo duplicado o una mano fusionada con la ropa?
- [ ] ¿Cada objeto sigue en la misma mano o lugar? Si cambia de portador, ¿se ve o se justifica la entrega y queda registrado el instante?
- [ ] ¿El contacto es físicamente coherente: dedos alrededor del objeto, apoyo en la superficie, sin atravesar cuerpo ni utilería?
- [ ] ¿Las heridas y quemaduras conservan lado, extensión y antigüedad? ¿Se ha regenerado por error una parte dañada?
- [ ] ¿Vestuario, cierres, emblemas, manchas, guantes y estado de las alas coinciden con la forma y el momento de la historia?
- [ ] ¿La pose y el apoyo del peso permiten continuar el gesto? ¿El montaje repite un paso, cambia de pie o detiene bruscamente la velocidad?
- [ ] ¿La mirada llega al mismo objetivo del espacio? ¿El cambio de cámara conserva una orientación comprensible respecto al eje?
- [ ] ¿Líquidos, cantidades y posiciones del decorado cambian solo después de una acción que lo explique?
- [ ] ¿Los elementos temporalmente ocultos permanecen en el inventario y reaparecen en el lugar previsto?
- [ ] ¿La referencia maestra sigue coincidiendo con el rostro, proporciones y paleta, o se acumuló deriva entre clips?
- [ ] ¿Luz, exposición, temperatura de color y estilo se mantienen sin un cambio narrativo? ¿Un resplandor oculta un defecto anatómico?
- [ ] ¿El frame semilla es el último retenido realmente en montaje, sin desenfoque que impida evaluar el detalle crítico? ¿Se anotaron archivo, versión, índice y tiempo?
- [ ] ¿`descripcion_textual`, imagen final y `estado_salida_observado` describen lo mismo? ¿Se mantuvieron separados de la salida prevista?
- [ ] ¿El prompt y las referencias cargadas coinciden? ¿La versión EN/ES conserva lados, cantidades y ausencias?
- [ ] ¿Una regeneración o cambio de corte ha invalidado correctamente las uniones posteriores?
- [ ] ¿Quedan dudas sobre un dato que afecta al raccord? Si las hay, ¿el estado sigue `pendiente` en vez de aprobarse por suposición?

**Criterio de rechazo:** una extremidad, un objeto o una herida cambia sin causa; un contacto es imposible; o la referencia final contradice el estado declarado. Detener la cadena en ese plano y señalar momento y campo afectados. La aprobación estética no compensa un fallo físico.

## Fuentes

Consultadas el 16-09-2026. Las guías oficiales respaldan funciones; los informes de sus propios autores y usuarios respaldan experiencias concretas. No se atribuye a ninguna fuente externa el esquema JSON ni las reglas de aprobación diseñadas aquí.

### Oficiales y profesionales

- [ScreenSkills — Script supervisor (Film and TV Drama)](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/technical/script-supervisor-film-and-tv-drama/): función profesional y registros de continuidad.
- [Google Flow — Create videos in Google Flow](https://support.google.com/flow/answer/16353334?hl=en): frames y referencias.
- [Google Flow — Edit videos & build scenes in Google Flow](https://support.google.com/flow/answer/16935718?hl=en): guardar frames, extensión y montaje.
- [Google Labs — Google Flow, catálogo con Storyboard Studio](https://labs.google/fx/es/tools/flow): ficha indexada; apertura directa con redirección a inicio de sesión.
- [Runway — Creating with Gen-4 Video](https://help.runwayml.com/hc/en-us/articles/37327109429011-Creating-with-Gen-4-Video): imagen inicial y Use Current Frame; documentación marcada como generación anterior.
- [Runway — How to create longer videos and films](https://help.runwayml.com/hc/en-us/articles/26871350018835-How-to-create-longer-videos-and-films): planificación, referencias y montaje.
- [Kling AI — Kling VIDEO 3.0 Model User Guide](https://app.klingai.com/cn/quickstart/klingai-video-3-model-user-guide): extremos, elementos y varios planos.
- [OpenAI — Create a video extension](https://developers.openai.com/api/reference/typescript/resources/videos/methods/extend): extensión de vídeo y aviso de retirada de la API.

### Pruebas y experiencias de primera mano

- [Reddit, r/VEO3 — Image to video consistency](https://www.reddit.com/r/VEO3/comments/1n53ow8/): exposición y deriva naranja al encadenar.
- [Reddit, r/VEO3 — Veo 3.1 fast with last frame issue](https://www.reddit.com/r/VEO3/comments/1p85j89/veo_31_fast_with_last_frame_issue/): discrepancia entre frame solicitado y generado.
- [Curious Refuge — prueba de Frames to Video en Veo 3.1 y Kling 2.5 Turbo](https://www.linkedin.com/posts/curiousrefuge_kling-and-veo-are-two-of-the-biggest-kids-activity-7399196716010242048-a1Vr): puerta, manos y bocadillo; texto del autor consultado.
- [Traction / Futureproof — Can AI Video Keep Up with Human Movement? A Futureproof Field Test](https://www.tractionco.com/insights/can-ai-video-keep-up-with-human-movement-a-futureproof-field-test): prueba de movimiento de agosto de 2025, no benchmark actual.

### Vídeos localizados y alcance de la consulta

- [AI Video School — How to Create Single Continuous Shots with Veo in Google Flow (AI Video Tutorial)](https://www.youtube.com/watch?v=6iBc4aoiwf4), 21-07-2025: página del vídeo y [transcripción parcial](https://glasp.co/youtube/6iBc4aoiwf4) consultadas; extensión frente a encadenamiento. Sin inspección completa del metraje.
- [Google — Creating in Flow | How to use Google’s new AI Filmmaking Tool](https://www.youtube.com/watch?v=9nVEfjmDlVk): localizado mediante indexación de título y descripción; apertura directa limitada por HTTP 429. Las capacidades citadas se verificaron en la ayuda oficial, no en un visionado supuesto.
- [Litany of Ignition — prueba comparativa de diálogo y sincronización labial, título exacto no recuperado](https://www.youtube.com/watch?v=s48XFLJKrAE): enlazada por su autor en la discusión de Curious Refuge; apertura sin contenido recuperable. Referencia audiovisual localizada para revisión, no evidencia de continuidad inspeccionada.

### Fuentes internas

- [13 — Presencia cinematográfica](13_presencia_cinematografica.md) y [12 — Calibre B](12_calibre_b.md): tono, canon y estados físicos.
- [Personajes](../lore/personajes.md): ficha de Miguel.
- [Miguel — identidad y referencias](../../character_library/angeles/Miguel/README.md), [forma celestial](../../character_library/angeles/Miguel/forms/celestial/README.md), [forma humana](../../character_library/angeles/Miguel/forms/human/README.md) y [ala izquierda quemada](../../character_library/angeles/Miguel/states/burned_left_wing/README.md).
- [Referencia facial](../../character_library/angeles/Miguel/canonical/face_reference.png) y [referencia corporal](../../character_library/angeles/Miguel/canonical/body_reference.png): imágenes inspeccionadas para el ejemplo.
