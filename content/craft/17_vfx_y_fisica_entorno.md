# 17 — VFX y física del entorno (2026-09-16)
**BORRADOR — pendiente de aprobación del autor**

Objetivo: que el personaje **afecte al lugar que pisa** y que dos acontecimientos puedan leerse a la vez dentro de un solo plano. Una bota desplaza arena; una capa responde al viento; un árbol sigue cayendo mientras una mosca cruza delante del rostro. Cada efecto necesita origen, movimiento y consecuencia visible.

Aplicación: adaptación de *Las Crónicas del Juicio / Chronicles of the Sundering Judgment*. Usar las referencias existentes de `character_library/` y el estado del personaje en ese capítulo. Los ejemplos siguientes son ejercicios técnicos, no nuevos hechos del canon. Mantienen el criterio de [[12_calibre_b]] y [[13_presencia_cinematografica]]: hecho concreto + efecto observable.

## Qué está verificado y qué se propone probar

- **Flow:** la ayuda oficial documenta referencias visuales —*ingredients*— y fotogramas de inicio/final. Su disponibilidad depende del modelo y del modo; comprobar la combinación elegida antes de preparar el plano. No equivalen a un bloqueo de anatomía ni a una simulación física. [Ayuda de creación](https://support.google.com/flow/answer/16353334?hl=en), [compatibilidad](https://support.google.com/flow/answer/16352836?hl=en).
- **Storyboard Studio:** aparece en el catálogo oficial de Flow como herramienta para guion, reparto y storyboard. No se ha confirmado documentación pública que garantice capas de movimiento independientes, memoria persistente de lesiones o sincronización exacta de acontecimientos. **No confirmado / puede haber cambiado.** No trasladar automáticamente controles de la API de Google o de otros generadores a su interfaz. [Catálogo consultado](https://labs.google/fx/en-gb/tools/flow).
- **Runway Gen-4:** su guía distingue movimiento del sujeto y movimiento del entorno, propone posiciones inequívocas para varios sujetos y recomienda describir explícitamente el polvo si el movimiento implícito no basta. Es una base documentada para separar acciones. [Guía oficial](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide).
- **Experiencia de usuario en Kling:** yukumiverse cuenta que necesitó unas veinte pruebas de telequinesis y recomienda separar el gesto del personaje del movimiento del objeto. Se refiere a versiones antiguas; el vídeo se ofrecía por mensaje privado. Es testimonio directo, no demostración reproducible ni prueba de que resuelva el árbol y la mosca. [Hilo original](https://www.reddit.com/r/KlingAI_Videos/comments/1kvzv7a/).

**Todos los prompts de esta guía son propuestas originales para ensayar.** No se han generado clips para medir su tasa de acierto. «Primer plano» y «fondo» organizan el lenguaje; no crean capas editables, máscaras ni canales de animación dentro del generador.

## La regla de trabajo: causa → respuesta → resto

Antes de escribir «polvo realista» o «física cinematográfica», resolver cinco datos:

| Dato | Pregunta que debe quedar contestada | Ejemplo |
| --- | --- | --- |
| Material y estado | ¿Qué toca el personaje? | Arena seca y suelta sobre suelo compacto. |
| Causa y contacto | ¿Qué pone el material en movimiento y cuándo? | La suela apoya y empuja hacia atrás al despegar. |
| Trayectoria y escala | ¿Hacia dónde se mueve y cuánto ocupa? | Un pequeño abanico de granos sale detrás del talón. |
| Evolución | ¿Qué cae, deriva o se disipa? | Los granos caen cerca; el polvo fino deriva a la derecha. |
| Resto | ¿Qué sigue ahí después? | La huella permanece visible. |

Patrón: **«Cuando [contacto], [material] se desplaza [dirección y escala]; después [caída/disipación]. Queda [consecuencia]».**

No hace falta llenar cada prompt con las cinco casillas. Elegir los datos que evitan el fallo del plano. Si las botas quedan fuera del encuadre, no se podrá comprobar la interacción con el suelo por mucha descripción que se añada.

## Construcción de un solo plano con acciones simultáneas

Separar **posición**, **acción** y **relación temporal**. Nombrar el sujeto de cada verbo. «Él se mueve mientras cae detrás» deja ambiguo quién cae. «El personaje gira la cabeza. Al mismo tiempo, el árbol del fondo cae hacia la derecha» asigna las dos acciones.

Plantilla de preparación —los rótulos son organización editorial, no sintaxis especial de Flow—:

```text
PLANO: una toma continua; encuadre y cámara; espacio visible de cada acción.
ESTADO: referencia del personaje y condiciones físicas relevantes al comienzo.
CERCANÍA: sujeto principal + una acción legible + interacción inmediata.
FONDO: objeto identificado por posición + su acción propia + trayectoria.
SOLAPAMIENTO: mientras ocurre A, B ya está en marcha y continúa visible.
CIERRE: qué termina y qué permanece al final.
```

Convertirlo después en frases naturales. Evitar una lista de escenas o instrucciones como «corta a», que cambian la petición de simultaneidad por montaje. Si la imagen inicial ya fija identidad, vestuario y estilo, dedicar el texto sobre todo al movimiento y a los estados que importan. Google recomienda ese enfoque para imagen a vídeo. [Buenas prácticas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice).

### Caso prioritario: árbol al fondo + mosca ante el rostro

El plano tiene tres elementos: personaje cercano, mosca junto a su cara y árbol distante. Preparar una referencia de composición que deje **un hueco de fondo al lado del personaje**. El árbol debe estar reconocible desde el inicio; si se pide que aparezca, se fracture y caiga en un rincón tapado por el rostro, se acumulan problemas.

Propuesta de prompt completo:

> Una toma continua con cámara fija, plano medio corto del personaje de referencia situado en el tercio izquierdo. A la derecha queda visible un árbol inclinado, separado de su silueta, con el tronco y su zona de caída dentro del encuadre. El rostro está definido y el árbol conserva detalle suficiente para leer su movimiento. Desde el comienzo, el árbol del fondo gira hacia la derecha desde su base dañada. Mientras el árbol está cayendo, una mosca pequeña cruza de izquierda a derecha justo por delante de la nariz del personaje; este la sigue brevemente con los ojos. Durante el cruce de la mosca, el tronco continúa descendiendo en el mismo encuadre. La mosca sale por la derecha. El árbol golpea el suelo al fondo y levanta una nube baja de polvo localizada en el impacto. El tronco queda tendido y visible al terminar la toma.

La inclinación y la base dañada son condiciones del ejercicio; sustituirlas por la causa autorizada en el capítulo. No inventar una rotura previa para una escena donde el árbol debe arrancarse de raíz.

Por qué está planteado así:

- **Acciones separadas:** mosca cruza; ojos siguen; árbol gira y cae. Se evita que el modelo asigne al personaje la caída.
- **Solapamiento explícito:** el árbol ya cae cuando pasa la mosca. «Después» solo se usa para el cierre.
- **Visibilidad:** el tronco tiene su propio espacio y una trayectoria que cabe en pantalla. Un árbol diminuto contra un bosque denso será difícil de distinguir.
- **Escala:** la mosca pasa junto a la nariz, no pegada a la lente. Se reduce la posibilidad de obtener un insecto gigante o una mancha que tape todo.
- **Foco:** evitar pedir a la vez fondo completamente desenfocado y caída detallada. Google documenta profundidad de campo amplia y cambios de foco como recursos distintos; aquí interesa conservar ambas acciones legibles. No se exige nitidez macro de la mosca y del árbol distante simultáneamente. [Guía de Google](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide).

Versión corta para probar si la larga pierde una acción:

> Cámara fija, una toma continua. El personaje ocupa el lado izquierdo; el árbol inclinado se ve completo al fondo a la derecha. Mientras el árbol cae hacia la derecha, una mosca pequeña cruza ante la nariz del personaje y este la sigue con los ojos. La caída permanece visible durante el cruce. Al final, el árbol queda en el suelo y la mosca ha salido del encuadre.

La versión corta es una alternativa de prueba, no una garantía superior. Añadir el polvo de impacto después de conseguir las dos acciones. Tampoco hay una duración exacta que asegure el resultado: si se usan marcas de segundos, tratarlas como intención de ritmo, no como fotogramas clave garantizados.

### Tres patrones reutilizables

| Necesidad | Frase para el prompt |
| --- | --- |
| Dos acciones independientes | «En primer término, [A] hace [acción]. Al mismo tiempo, al fondo a la derecha, [B] hace [acción]. Ambas permanecen visibles en la misma toma». |
| Un evento breve dentro de otro largo | «Mientras [B] continúa [acción], [A] cruza [zona]. [B] sigue moviéndose durante todo el cruce». |
| Entorno causado por el personaje | «Cuando [A] apoya [parte del cuerpo/objeto], [material en el punto de contacto] responde [movimiento]. La reacción comienza en ese contacto». |

«Mientras» establece tiempo compartido; no inventa causalidad. La mosca no provoca la caída del árbol. El polvo bajo la bota sí depende de su apoyo.

## Banco de frases: física del entorno

Usar **un bloque por interacción necesaria**. No pegar todo el banco en un único prompt. Son descripciones de resultados visibles, no parámetros de un motor de partículas.

### Arena y polvo: el pie deja peso

> Plano bajo lateral con las botas y el suelo visibles. El personaje da dos pasos sobre arena seca y suelta. Cada suela se hunde ligeramente al apoyar. Al despegar la bota, un abanico pequeño de granos sale hacia atrás desde la puntera; los granos caen cerca y el polvo fino deriva a la derecha con el viento. Las dos huellas quedan marcadas detrás del personaje.

**Comprobar:** contacto antes de emisión, pies apoyados, polvo nacido bajo la bota, huella persistente. La nube no debe salir del torso ni adelantarse al paso.

Si la escena está en arena húmeda, cambiar el bloque: «La suela comprime la superficie y deja una huella de borde oscuro; pequeños terrones húmedos se desprenden al levantar el pie». No pedir una nube seca salvo que la escena lo justifique.

### Cristal roto: distinguir desplazamiento de nueva fractura

Un suelo cubierto de fragmentos ya está roto. Pisar puede desplazar los trozos; la nueva fractura necesita una pieza que todavía pueda quebrarse y una carga que lo explique.

> Plano detalle de una bota sobre fragmentos de vidrio en piedra. La bota baja y carga su peso sobre una esquirla grande cuyo centro queda elevado sobre un pequeño cascote. La esquirla se parte bajo la suela al recibir la presión. Los trozos resultantes saltan a poca altura, caen junto al pie y quedan esparcidos; los fragmentos vecinos se desplazan sobre la piedra.

**Comprobar:** rotura al cargar, no antes; piezas rígidas, no goma; fragmentos que siguen presentes al levantar el pie. No exigir un número exacto de astillas. Para un plano más amplio: «Los fragmentos crujen y se desplazan bajo cada apoyo; quedan apartados a ambos lados de la pisada». El crujido puede reforzar la acción, pero no demuestra que se haya generado una fractura visible.

### Telas y capas: anclaje, peso y viento compartido

> El viento sopla de izquierda a derecha de pantalla. La capa permanece sujeta a los hombros; su tejido pesado se desplaza hacia la derecha en pliegues amplios y el borde inferior responde con un pequeño retraso. Cuando la ráfaga afloja, el tejido baja por su peso. El polvo fino del suelo deriva en la misma dirección.

**Comprobar:** cierre fijo, masa de tela estable, borde que no atraviesa el cuerpo, dirección compatible con pelo y humo. Para tela ligera, sustituir «pliegues amplios» por «ondulaciones rápidas en los bordes». No pedir viento suave y capa horizontal tensa a la vez.

### Alas: anatomía primero, movimiento secundario después

Solo cuando corresponda a la forma canónica y a la referencia seleccionada:

> El personaje mantiene las alas en la postura de la imagen inicial. La ráfaga mueve las plumas de los extremos hacia la derecha, con pequeñas oscilaciones que disminuyen al cesar el viento. La inserción de las alas permanece fija y su estructura principal conserva la postura.

**Comprobar:** número de alas, inserciones, silueta y contacto con capa o armadura. Este bloque describe reacción al viento, no vuelo. Si hay despegue, sustentación o aterrizaje, preparar una prueba aparte: añadir batidos y desplazamiento corporal multiplica las interacciones que deben resolverse.

### Fuego, humo y chispas: tres comportamientos distintos

> La llama nace en la cabeza de la antorcha y oscila sobre ella. Su luz cálida varía sobre la mejilla y el guante próximos. El humo asciende desde la combustión y después se curva hacia la derecha con la brisa. Unas pocas brasas pequeñas suben con el aire caliente y pierden brillo al alejarse. La mano mantiene la misma posición alrededor del mango.

Para chispas por impacto, cambiar el origen y la trayectoria:

> En el instante del golpe, unas pocas chispas salen del punto de contacto en un abanico corto; describen arcos descendentes y se apagan antes de alcanzar el suelo.

**Comprobar:** emisión localizada, humo unido a la fuente, luz sobre superficies cercanas, mano y mango estables. «Chispas flotantes por toda la escena» no describe un impacto. Tampoco usar el humo para ocultar una mano que luego reaparezca con otra forma.

### Agua: contacto, salpicadura y humedad que queda

> Plano bajo lateral de una bota entrando en un charco poco profundo. Al tocar el agua, la suela empuja una salpicadura baja hacia los lados. Las gotas suben en arcos cortos, caen sobre el charco y la piedra cercana; pequeñas ondas se expanden desde la pisada. Al salir la bota, quedan gotas en el cuero y una huella húmeda sobre la piedra.

**Comprobar:** agua desplazada al contacto, regreso de gotas, superficie que se asienta, bota mojada después. Evitar una gran ola para un apoyo suave en un charco somero. Si el pie sigue pareciendo seco, simplificar a una sola pisada y un encuadre que permita leer el material mojado.

## Qué enseñan los breakdowns de VFX localizados

**Límite de la consulta:** se localizaron vídeos de YouTube, pero el acceso directo devolvió errores o un reproductor sin contenido legible. No se afirma haberlos visto fotograma a fotograma. Se distingue el desglose publicado por su creador de una descripción indexada; no se atribuyen prompts exactos que no hayan podido verificarse.

1. **Beeble / Hoon Kim — antorcha con fuego.** El desglose oficial del tutorial explica una referencia visual, máscaras y generación con SwitchX, seguida de ajuste de color entre planos. El fuego también ilumina cara, ropa y cueva. Aplicación al prompt: nombrar la fuente y las superficies afectadas por su luz. El resultado mostrado por el proveedor no demuestra que un prompt aislado en Flow produzca lo mismo. [Desglose](https://beeble.ai/blog/canvas-tutorial-fire-vfx), [vídeo enlazado por Beeble](https://www.youtube.com/watch?v=VbgtaUTmslM).
2. **The NEW After Effects VFX Workflow: RotoBrush 3, Nano Banana Pro + Kling O1 (AI Compositing).** Localizado mediante descripción y capítulos indexados: rotoscopia, fondo limpio, generación, ajuste de color y seguimiento con Mocha. La reproducción y los prompts completos no se pudieron verificar. Sirve como referencia audiovisual pendiente de revisión, no como prueba de física de partículas ni de simultaneidad conseguida solo con texto. [Vídeo](https://www.youtube.com/watch?v=eMDDDdoUgT4).
3. **INSANE AI-Generated FIRE Effect in After Effects (Easy Tutorial).** Localizado por título y descripción. Acceso directo fallido; herramienta generativa concreta, parámetros y calidad de la física **no confirmados**. No se extrae de él ninguna receta técnica. [Vídeo](https://www.youtube.com/watch?v=E7S7ccFRx04).

Conclusión operativa de la evidencia accesible: incluir **interacción**, no solo presencia del efecto. Una llama tiene fuente y luz; una salpicadura deja humedad; la arena desplazada deja huella. Si hace falta controlar por separado actor, fondo y partículas, la composición externa sigue siendo una vía de producción; no se ha verificado que Storyboard Studio ofrezca ese control por capas.

## Límites: lo que el guion no debe dar por resuelto

PhyGenBench, publicado en ICML 2025, encontró dificultades de coherencia física que el prompting por sí solo no resolvía en los modelos evaluados. No es una medición de todas las versiones disponibles hoy. Google publica comparativas favorables de realismo visual de Veo 3.1; esas preferencias humanas tampoco garantizan conservación de masa o contactos exactos en un plano concreto. [Estudio](https://proceedings.mlr.press/v267/meng25c.html), [evaluación de Google](https://deepmind.google/models/veo/).

Esta tabla es una **priorización de pruebas para el proyecto**, no un ranking experimental de modelos:

| Interacción exigida | Fallo que obliga a revisar el plano | Tratamiento de producción |
| --- | --- | --- |
| Rotura con fragmentos identificables | Piezas que aparecen, se fusionan o se recomponen. | Reducir la rotura visible; usar VFX controlado si importa el recorrido de cada pieza. |
| Contacto pie/suelo, mano/mango | Deslizamiento, penetración, objeto que cambia de forma. | Mostrar un solo contacto claro y revisar su duración completa. |
| Agua con volumen y recipientes | Líquido que atraviesa bordes o cambia de cantidad. | Evitar depender de una medición exacta; preparar simulación si el volumen es argumento. |
| Tela/alas cruzándose con el cuerpo | Intersecciones, apéndices nuevos, anclajes móviles. | Simplificar postura y amplitud; mantener la referencia visible. |
| Dos acontecimientos simultáneos | Fondo inmóvil, evento omitido o acciones ejecutadas en serie. | Rehacer composición y solapamiento; si persiste, componer pases en una sola toma final. |
| Oclusión por humo, polvo o un objeto | Mano, herida o accesorio distinto al reaparecer. | Comparar antes y después de la oclusión; rechazar cualquier cambio de estado. |
| Sincronización exacta | Impacto y reacción separados; audio anticipado. | Ajustar en edición o efectos; no prometer precisión de fotograma por texto. |

No convertir «física realista», «anatomía bloqueada», JSON o mayúsculas en garantías. No se ha encontrado una técnica pública verificable que asegure el caso árbol/mosca con una sola generación de Flow. Las búsquedas en X/Twitter tampoco aportaron una demostración reproducible con prompt, modelo y resultado para ese caso.

## Continuidad: el efecto no reinicia el personaje

Antes de cada plano, consignar en su ficha de trabajo **estado de entrada → cambio visible → estado de salida**. Esa ficha orienta el prompt y la revisión; no es una memoria automática de la herramienta.

Ejemplo técnico de continuidad, sin asignarlo a ningún personaje canónico:

```text
ENTRADA: amputación izquierda ya establecida; manga recogida en el muñón;
         mano derecha alrededor del mango; botas secas.
ACCIÓN: una pisada en el charco; la antorcha permanece en la derecha.
SALIDA: misma anatomía y misma sujeción; bota de apoyo mojada.
SIGUIENTE PLANO: empieza con esa bota mojada y esa misma anatomía.
```

Si la referencia de `character_library/` muestra un estado incompatible, seleccionar una referencia o un fotograma aprobado adecuado. No confiar en que la frase «mantén la lesión» venza a una imagen donde el miembro está intacto. Evitar también «ambas manos» en un prompt de un personaje amputado. Las referencias ayudan; el resultado exige inspección.

Para el entorno, transportar también las consecuencias: árbol tendido, fragmentos dispersos, huellas, humo residual, capa mojada. Un fotograma final puede orientar el siguiente plano si el modo lo permite, pero no certifica que el movimiento intermedio sea correcto.

## Prueba y aceptación del plano

1. **Fijar la composición.** Se ve el contacto o hay espacio separado para ambas acciones. Referencia coherente con el estado del capítulo.
2. **Probar lo indispensable.** Para árbol/mosca, empezar por caída + cruce; incorporar después polvo y reacción ocular si compiten con la lectura. La toma final conserva los acontecimientos exigidos por el guion.
3. **Cambiar una variable por intento.** Encuadre, frase temporal, escala del efecto o referencia. Registrar modelo, modo, duración y prompt; no atribuir el éxito a una frase si también cambió todo lo demás.
4. **Evaluar sin sonido primero.** ¿Se ve el impacto? ¿El fondo se mueve durante el cruce? ¿La huella queda? Después comprobar sonido e imagen juntos.
5. **Revisar contacto y oclusiones.** Inspeccionar el inicio, el contacto, la máxima deformación/ocultación y el final. Reproducir también a velocidad normal: un fotograma convincente puede esconder un movimiento imposible.
6. **Aceptar solo si persiste el estado.** Anatomía, accesorios y daños coinciden antes/después; el árbol no se levanta, el cristal no se recompone y la bota no se seca sin causa.

Si la simultaneidad sigue fallando tras variar texto y composición, preparar actor, caída y mosca como pases separados y componerlos con la misma cámara, escala, luz y oclusiones. La entrega puede seguir siendo **un solo plano**. Si se propone resolverlo mediante cortes, eso cambia la puesta en escena y debe revisarse como tal; no presentarlo como cumplimiento del plano simultáneo.

## Fuentes

Consulta: **2026-09-16**. Investigación con más de diez búsquedas distintas en inglés y español, documentación oficial, Reddit, foros, X/Twitter y búsquedas específicas de YouTube. Se listan las fuentes útiles; las páginas promocionales y resultados sin evidencia técnica no sustentan garantías de rendimiento.

- Google — [Create videos in Google Flow](https://support.google.com/flow/answer/16353334?hl=en). Referencias, fotogramas y coherencia entre texto e imagen.
- Google — [Learn about Google Flow models & supported features](https://support.google.com/flow/answer/16352836?hl=en). Compatibilidad dependiente del modelo.
- Google Labs — [AI Creative Studio for video, images and custom tools — Google Flow](https://labs.google/fx/en-gb/tools/flow). Catálogo indexado con Storyboard Studio; la apertura posterior redirigió a Flow.
- Google Cloud — [Video generation prompt guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide). Acciones, contexto y profundidad de campo.
- Google Cloud — [Best practices for generating videos](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice). Texto centrado en movimiento al usar una imagen inicial.
- Runway — [Gen-4 Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide). Movimiento de sujeto/entorno y asignación espacial de acciones.
- yukumiverse, Reddit — [How I Made a Telekinesis Scene in Kling (In About 20 Tries)](https://www.reddit.com/r/KlingAI_Videos/comments/1kvzv7a/). Testimonio directo; resultado audiovisual no público en el hilo.
- Kling AI — [How to Produce Professional-Grade Visual Effects](https://kling.ai/blog/ai-special-effects-guide-visual-effects). Ejemplos de descripciones de movimiento y luz; sus afirmaciones comerciales de precisión no se toman como garantías.
- Beeble — [Add realistic fire VFX while preserving original footage](https://beeble.ai/blog/canvas-tutorial-fire-vfx). Desglose del creador, con máscaras, referencias y ajuste de iluminación.
- Beeble / Hoon Kim — [Tutorial de fuego enlazado desde el desglose anterior](https://www.youtube.com/watch?v=VbgtaUTmslM). Vídeo localizado; consulta mediante el artículo oficial, reproducción no accesible.
- YouTube — [The NEW After Effects VFX Workflow: RotoBrush 3, Nano Banana Pro + Kling O1 (AI Compositing)](https://www.youtube.com/watch?v=eMDDDdoUgT4). Descripción y capítulos localizados; reproducción no accesible.
- YouTube — [INSANE AI-Generated FIRE Effect in After Effects (Easy Tutorial)](https://www.youtube.com/watch?v=E7S7ccFRx04). Título y descripción indexados; contenido completo no verificado.
- Meng et al., ICML 2025 — [Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation](https://proceedings.mlr.press/v267/meng25c.html). PhyGenBench y límites de la corrección física mediante prompting.
- Google DeepMind — [Veo 3.1](https://deepmind.google/models/veo/). Comparativas de realismo visual y alcance de sus evaluaciones.
