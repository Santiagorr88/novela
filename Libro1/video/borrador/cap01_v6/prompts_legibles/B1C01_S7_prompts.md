# B1C01_S7 — "El centinela silencioso"

**Localización:** Interior de la Arboleda — filas de árboles de metal pálido  
**Resumen:** Miguel reclama en voz alta lo que ha venido a buscar. Entre los árboles descubre una figura guardiana que no ataca ni le cierra el paso: gira en silencio para seguir mirándolo mientras él avanza hacia el centro de la arboleda, como una aguja de brújula.  
**Planos totales:** 21 · **Con prompt listo:** 18 · **Bloqueados (no incluidos aquí):** B1C01_S7_P08

---

## 1. Plano B1C01_S7_P01  (`inicio_escena`, 8s, idioma ES)

**Ajustes:** Ingredients to Video. Modelo: Veo 3.1 Fast (fallback Lite si Fast no está disponible en la sesión). Duración 8s (coincide con el tope de generación base; no necesita Extend). Formato 16:9. Resolución: comprobar en el selector, 720p por defecto; reescalar a 1080p solo tras aprobar el plano. 1 referencia (identidad y proporciones de Miguel en forma celestial); primer plano de la escena, no hay frame previo que reutilizar. Miguel se aleja de cámara en todo el plano: no hay riesgo del bug de 'camina hacia atrás pese a pedir de frente' documentado por el autor, porque no se le pide caminar hacia la cámara.

**Referencias a adjuntar:**
- `character_library/angeles/Miguel/forms/celestial/body_reference.png`

**Prompt:**
> Plano general fijo, cámara estática a la altura de los ojos, sin ningún movimiento de encuadre durante toda la toma. Filas regulares de árboles de metal pálido ocupan todo el plano bajo una luz cenital difusa, plata fría, filtrada entre las copas; una bruma baja cubre el suelo entre los troncos y marca la profundidad y regularidad de las filas. Miguel, en su forma celestial, con la identidad y las proporciones de la referencia adjunta, camina solo entre las filas de árboles, pequeño en el encuadre, alejándose progresivamente de cámara hacia el interior de la arboleda, buscando algo con la mirada mientras recorre el espacio. Viste armadura dorada agrietada (grietas visibles, sin daño nuevo), guantes de cuero oscuro puestos e íntegros y sabatones dorados agrietados pero íntegros. No lleva arma, vaina ni ningún objeto en la cadera o en la espalda, y ambas manos permanecen completamente vacías durante todo el plano. No presenta ninguna marca física, cicatriz ni perforación visible en la piel bajo el esternón. En cada apoyo de sabatón sobre el suelo polvoriento se levanta una fina nube baja de polvo pálido justo tras el talón, que se asienta enseguida y deja una huella tenue que se difumina en uno o dos pasos; el polvo no debe elevarse por encima de la rodilla ni derivar como si hubiera viento. No aparece ningún otro personaje en el plano: la figura de niebla del centinela permanece completamente fuera de campo. No hay edificios, columnas ni ruinas de templo en el fondo, solo la arboleda de metal pálido bajo la bruma.

**Criterios de aceptación:** Miguel conserva identidad, forma celestial y proporciones de la referencia durante toda la toma. Manos vacías y sin arma ni vaina visibles en ningún fotograma, incluido el interior del clip, no solo el primer y último. Sin marca en la piel bajo el esternón. Polvo levantado en cada apoyo de sabatón, sutil, coherente con el contacto real del pie, que se asienta en 1-2 pasos sin exceso. Ningún elemento del Pewter Sentinel visible en ningún fotograma. Fondo limitado a árboles de metal pálido, sin construcciones.

---

## 2. Plano B1C01_S7_P02  (`continuacion`, 7s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 7s. Formato 16:9. Resolución a comprobar en sesión. 2 referencias (una por personaje); es continuación directa de P01 dentro del mismo plano fijo, sin frame previo aprobado todavía que reutilizar. Riesgo específico del brief: probar primero solo la anomalía de luz del centinela y añadir después el polvo de Miguel, cambiando una variable por intento si el resultado mezcla mal los dos eventos simultáneos.

**Referencias a adjuntar:**
- `character_library/angeles/Miguel/forms/celestial/body_reference.png`
- `character_library/otros/Pewter Sentinel/canonical/body_reference.png`

**Prompt:**
> Continúa el mismo plano general fijo, cámara estática a la altura de los ojos, sin corte. Las mismas filas de árboles de metal pálido bajo la luz cenital difusa y plata fría de antes. En primer término, Miguel, con la identidad de la primera referencia, continúa caminando solo entre los troncos, sin arma, sin vaina y sin ningún objeto en la cadera o la espalda, manos completamente vacías, dejando el mismo patrón leve de polvo pálido bajo cada sabatón, aún sin percatarse de nada. Al mismo tiempo, a unos cuarenta pasos, a la derecha de pantalla, uno de los 'árboles' deja de coincidir en ángulo con los demás: es la primera aparición del Pewter Sentinel, con la identidad de la segunda referencia. Esa figura debe leerse exclusivamente como niebla y vapor denso, nunca como una silueta de metal sólido con reflejo especular — sus bordes son difusos, con un ligero temblor de vapor, y la bruma ambiental se concentra algo más densa justo en torno a ella. Ambos sucesos, la marcha de Miguel en primer término y la anomalía de niebla al fondo, deben permanecer visibles a la vez durante todo el plano, sin que uno sustituya al otro. No hay edificios, columnas ni ruinas en el fondo, y no aparece ningún otro personaje además de Miguel y el centinela.

**Criterios de aceptación:** Miguel sin arma ni vaina, manos vacías, sin marca bajo el esternón, en todo el plano. El centinela se lee como niebla/vapor con bordes difusos, nunca como metal sólido con brillo especular. Ambos eventos (marcha de Miguel + anomalía de fondo) visibles simultáneamente y sostenidos, sin que el fondo quede inmóvil ni el evento del centinela se omita. Ningún personaje adicional en cuadro.

---

## 3. Plano B1C01_S7_P03  (`cambio_angulo`, 6s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 6s. Formato 16:9. 1 referencia (rostro de Miguel, prioritaria en un plano medio corto). Cambio de ángulo respecto a P02: se construye como nueva composición a partir del estado físico heredado, sin usar el frame final de P02 como arranque literal.

**Referencias a adjuntar:**
- `character_library/angeles/Miguel/canonical/face_reference.png`

**Prompt:**
> Plano medio corto (pecho a cabeza) de Miguel, a la altura de los ojos, cámara completamente fija, sin ningún desplazamiento. Miguel, con la identidad de la referencia adjunta, está de frente a cámara, aún caminando al inicio del plano, con la armadura dorada agrietada visible en el encuadre; sus manos y piernas quedan fuera de este encuadre cerrado, pero permanecen en el mismo estado que traía: sin arma, sin vaina, sin ningún objeto en la cadera o la espalda, manos completamente vacías. No presenta ninguna marca física, cicatriz ni perforación visible bajo el esternón. Durante el plano, Miguel se detiene, deteniendo su ciclo de marcha, y gira la cabeza hacia la derecha de pantalla, hacia un desajuste que percibe fuera de campo; su mirada queda fija en ese punto al terminar el plano. La luz cenital difusa cae sobre su rostro con un reflejo propio del dorado agrietado de su armadura, sombras algo más marcadas en las grietas. No aparece ningún otro personaje en el encuadre: el centinela permanece fuera de campo. Sin edificios, columnas ni ruinas en el fondo.

**Criterios de aceptación:** Miguel conserva identidad y rasgos faciales de la referencia. Sin arma, vaina ni objetos visibles cuando el encuadre lo permita; sin marca bajo el esternón. El gesto de detenerse y girar la cabeza ocurre con claridad dentro del plano, terminando con la mirada fija hacia la derecha de pantalla. Ningún otro personaje visible.

---

## 4. Plano B1C01_S7_P04  (`cambio_angulo`, 7s, idioma ES)

**Ajustes:** Ingredients to Video con descripción completa del movimiento de cámara en texto (dolly-in), preferible a fijar un frame final exacto — según la nota verificada del autor, 'frames to video' con inicio y fin no garantiza interpolación fluida en movimiento continuo. Veo 3.1 Fast (fallback Lite). Duración 7s. Formato 16:9. 2 referencias del mismo personaje (cuerpo completo + detalle de hombros/rostro) para anclar la revelación progresiva del cuerpo de niebla durante el acercamiento. Probar primero el push-in sin diálogo ni otros elementos, aislando la variable, según indica el propio brief.

**Referencias a adjuntar:**
- `character_library/otros/Pewter Sentinel/canonical/body_reference.png`
- `character_library/otros/Pewter Sentinel/supporting_references/detail_views.png`

**Prompt:**
> Travelling de aproximación (dolly-in) continuo, altura de ojos, desde un plano entero hasta un plano americano, centrado en el Pewter Sentinel, identidad de las referencias adjuntas. Al inicio, la figura es una masa alta de niebla y vapor apenas distinguible entre los árboles de metal pálido, inmóvil. A medida que la cámara avanza, el cuerpo se revela progresivamente como niebla y vapor en roce y curvado continuo, nunca como una superficie metálica lisa: se disuelve hacia abajo sin piernas ni pies definidos, sin base sólida de contacto, y flota ligeramente por encima del suelo, sin producir ninguna huella ni levantar polvo de apoyo — solo un ligero rizo de niebla baja que se arrastra cerca del suelo sin tocarlo con un borde definido. Los ojos, blancos y tenues, se hacen visibles hacia el final del acercamiento, junto con los zarcillos de peltre fundidos en ambos hombros. La luz cenital difusa se vuelve visible como haces de luz atravesando el cuerpo de vapor de arriba abajo. Miguel no aparece en ningún momento de este plano. No hay edificios, columnas ni ruinas en el fondo, ni ningún otro personaje.

**Criterios de aceptación:** El cuerpo del centinela se revela progresivamente como niebla/vapor durante todo el push-in, sin convertirse en ningún momento en superficie metálica sólida. Sin piernas ni pies definidos ni base de apoyo implícita bajo el cuerpo. Miguel ausente del encuadre en todo el plano. Ojos y zarcillos de peltre visibles y reconocibles al final del acercamiento.

---

## 5. Plano B1C01_S7_P05  (`cambio_angulo`, 7s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 7s. Formato 16:9. 1 referencia (rostro del centinela). Evaluar primero sin sonido, como recomienda el brief, para juzgar solo la lectura del vapor antes de aprobar.

**Referencias a adjuntar:**
- `character_library/otros/Pewter Sentinel/canonical/face_reference.png`

**Prompt:**
> Primer plano fijo, ligero contrapicado coherente con la altura de árbol del centinela, cámara completamente estática. El rostro de niebla del Pewter Sentinel, con la identidad de la referencia adjunta, llena el cuadro: rasgos casi ausentes bajo la bruma en roce lento y constante, sin nariz, boca ni cejas marcadas, nunca leído como máscara sólida de piel o metal. Dos ojos blancos tenues brillan desde el interior de la bruma como única fuente de luz propia, iluminando levemente el vapor inmediato a su alrededor en un halo suave. La figura no se mueve ni gesticula en ningún momento del plano; el aire circundante permanece despejado, sin bruma ambiental adicional más allá de la que rodea al propio rostro. Miguel no aparece en este plano. No hay edificios, columnas, ruinas ni ningún otro personaje en el encuadre.

**Criterios de aceptación:** El rostro se mantiene como niebla/vapor en roce continuo durante todo el plano, sin solidificarse en ningún fotograma, ni siquiera hacia el final del encuadre cerrado. Sin rasgos faciales definidos más allá de los dos ojos blancos. Halo de luz alrededor de los ojos coherente con una fuente interna, no con iluminación externa dura. Miguel ausente.

---

## 6. Plano B1C01_S7_P07  (`cambio_angulo`, 6s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 6s. Formato 16:9. 1 referencia (detalle de hombros/zarcillos de peltre). Pedir explícitamente roce mínimo continuo del vapor circundante, no ausencia de movimiento, según la limitación conocida del brief.

**Referencias a adjuntar:**
- `character_library/otros/Pewter Sentinel/supporting_references/detail_views.png`

**Prompt:**
> Plano detalle fijo, altura de ojos, cámara completamente estática, centrado exclusivamente en los zarcillos o fragmentos de peltre fundidos en los hombros del Pewter Sentinel, con la identidad de la referencia adjunta. El peltre es una superficie rígida y fija, sin roce ni deformación, con textura metálica mate marcada por una luz cenital algo más rasante y dura que revela su borde frente al vapor blando que lo envuelve; no debe leerse en ningún momento como parte del cuerpo de niebla, sino como el único elemento sólido anclado a él. Alrededor de los zarcillos, la bruma propia del centinela mantiene un roce de muy baja amplitud, volutas mínimas que difuminan el borde inferior del encuadre, para que el conjunto no se lea como humo pintado y estático. No hay rostro, manos ni el resto del cuerpo visibles en este encuadre cerrado. Miguel no aparece. Sin edificios, columnas ni ruinas en el fondo.

**Criterios de aceptación:** Los zarcillos de peltre permanecen exactamente iguales de inicio a fin del plano, sin deformarse. La niebla que los envuelve conserva un roce mínimo pero continuo durante todo el plano, sin quedar completamente estática. Ningún rostro, mano ni el resto del cuerpo visible en este encuadre. Miguel ausente.

---

## 7. Plano B1C01_S7_P09  (`cambio_angulo`, 7s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 7s. Formato 16:9. 1 referencia (rostro del centinela). Si el zoom óptico sutil endurece la textura del vapor en la prueba, repetir sin el zoom como variable de control, según indica el brief.

**Referencias a adjuntar:**
- `character_library/otros/Pewter Sentinel/canonical/face_reference.png`

**Prompt:**
> Primer plano frontal, ligero contrapicado, cámara fija con un zoom óptico lento y sutil opcional hacia el rostro del Pewter Sentinel, identidad de la referencia adjunta, hacia el final del plano. El rostro de niebla permanece inmóvil y atento, orientado hacia donde se encuentra Miguel aunque él quede fuera de este encuadre; su quietud es la única señal que ofrece — ni hostilidad ni bienvenida. Volutas finas de vapor rozan continuamente el contorno del rostro incluso a esta escala más próxima; el brillo de los ojos se mantiene estable o con una pulsación muy leve, nunca como una superficie sólida iluminada desde fuera. Si se aplica el zoom óptico, el encuadre se cierra levemente sin que la textura del vapor se endurezca en ningún momento hacia algo sólido. Miguel no aparece en este plano. Sin edificios, columnas ni ruinas, ni ningún otro personaje.

**Criterios de aceptación:** El rostro se mantiene como vapor fino en roce continuo durante todo el plano, incluso si se usa el zoom óptico, sin solidificarse. Postura y orientación del centinela idénticas de inicio a fin. Miguel ausente del encuadre en todo momento.

---

## 8. Plano B1C01_S7_P10  (`cambio_angulo`, 7s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 7s. Formato 16:9. 2 referencias (una por personaje). Diálogo en español únicamente (dialogo_es), sin mezclar con la línea en inglés del mismo plano. Vigilar explícitamente el fondo, no solo el primer término, para que el centinela no se simplifique a una silueta estática de metal mientras Miguel habla.

**Referencias a adjuntar:**
- `character_library/angeles/Miguel/forms/celestial/body_reference.png`
- `character_library/otros/Pewter Sentinel/canonical/body_reference.png`

**Prompt:**
> Plano medio, altura de ojos, cámara prácticamente fija con un travelling de aproximación muy leve. Miguel, identidad de la primera referencia, visible de cintura a cabeza en primer término, con la armadura dorada agrietada, los guantes de cuero oscuro puestos y sin arma, vaina ni ningún objeto en la cadera o la espalda; sus manos permanecen completamente vacías y no presenta ninguna marca física bajo el esternón. Al fondo, dentro del mismo encuadre, el Pewter Sentinel, identidad de la segunda referencia, permanece inmóvil, con su cuerpo de niebla y vapor en roce continuo de baja amplitud, sin volverse en ningún momento una silueta sólida y estática de metal o piedra. Miguel habla, dirigiéndose a la figura, sosteniendo la postura y el encuadre mientras pronuncia su línea, con luz cenital difusa relativamente uniforme sobre ambos, sin contrapicados ni aureola, el dorado de Miguel contenido y la bruma de fondo discreta sin invadir el primer término. No hay edificios, columnas ni ruinas en el fondo, ni ningún otro personaje. Miguel dice, en español: «He venido por lo que es mío».

**Criterios de aceptación:** Miguel sin arma, vaina ni objetos, manos vacías y sin marca bajo el esternón durante toda la línea. El centinela al fondo conserva un vapor visiblemente vivo, no una silueta estática de metal. El diálogo se pronuncia literal, en español, sin réplicas añadidas ni mezclarlo con la versión en inglés.

---

## 9. Plano B1C01_S7_P11  (`cambio_angulo`, 6s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 6s. Formato 16:9. 1 referencia (cuerpo del centinela). Pedir explícitamente continuidad del roce de vapor aunque no haya acción ni gesto, según la limitación conocida del brief.

**Referencias a adjuntar:**
- `character_library/otros/Pewter Sentinel/canonical/body_reference.png`

**Prompt:**
> Plano medio fijo, altura de ojos, centrado únicamente en el Pewter Sentinel, identidad de la referencia adjunta, de cintura o su equivalente de vapor a cabeza. La figura no responde a lo dicho por Miguel; su quietud basta como respuesta, sin ningún gesto, paso ni alteración de los zarcillos de peltre en los hombros. El rostro casi sin rasgos, los ojos blancos brillantes y el cuerpo que se disuelve en vapor hacia abajo, sin piernas ni pies definidos, se mantienen exactamente igual de inicio a fin. Se conserva un roce continuo de baja amplitud en toda la superficie de vapor como único movimiento visible, sin quedar nunca congelada ni leerse como una figura inerte. Miguel no aparece en este plano. Sin edificios, columnas ni ruinas, ni ningún otro personaje.

**Criterios de aceptación:** Postura, orientación y ausencia de gesto del centinela idénticas de inicio a fin del plano. El vapor conserva roce visible y continuo pese a la total ausencia de acción. Miguel ausente del encuadre.

---

## 10. Plano B1C01_S7_P12  (`cambio_angulo`, 6s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 6s. Formato 16:9. 1 referencia (rostro de Miguel).

**Referencias a adjuntar:**
- `character_library/angeles/Miguel/canonical/face_reference.png`

**Prompt:**
> Primer plano fijo, altura de ojos, cámara completamente estática, centrado en el rostro de Miguel, identidad de la referencia adjunta. Su expresión deja ver que la certeza que acaba de decir en voz alta se siente de pronto pequeña y prestada; la expresión se asienta hacia el final del plano, sin ningún cambio de postura corporal. La luz cenital difusa cae con menos relleno que en planos anteriores de Miguel, sin proyectar sombras nuevas en cejas ni nariz (esta arboleda no proyecta sombra), y el dorado de su armadura, visible solo en el borde inferior desenfocado del encuadre, se ve apagado, sin brillo. Fuera de este encuadre cerrado, Miguel conserva su estado: sin arma, sin vaina, manos vacías, sin marca física bajo el esternón. El Pewter Sentinel no aparece en este plano. Sin edificios, columnas ni ruinas en el fondo, ni ningún otro personaje.

**Criterios de aceptación:** El rostro de Miguel conserva identidad y rasgos de la referencia; el cambio de expresión es sutil y puramente actoral, sin ningún efecto de entorno añadido. El centinela ausente del encuadre en todo el plano.

---

## 11. Plano B1C01_S7_P14  (`cambio_angulo`, 7s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 7s. Formato 16:9. 1 referencia (cuerpo celestial de Miguel). Miguel se aleja de cámara: sin riesgo del bug de marcha hacia atrás documentado por el autor. Vigilar explícitamente que el generador no 'rellene' la ausencia de límite con ningún efecto no pedido, por pura tendencia a decorar.

**Referencias a adjuntar:**
- `character_library/angeles/Miguel/forms/celestial/body_reference.png`

**Prompt:**
> Plano general fijo, altura de ojos, cámara estática y apartada, sin ningún movimiento de encuadre. La arboleda de árboles de metal pálido se abre ante Miguel, identidad de la referencia adjunta, en todas direcciones, bajo una luz cenital difusa homogénea, pareja en todo el encuadre, con una bruma baja constante e igual en todo el plano. Miguel continúa caminando, alejándose de cámara hacia el interior de la arboleda, sin arma, sin vaina, sin ningún objeto en la cadera o la espalda, manos completamente vacías, con sus alas plegadas contra la espalda, intactas y sanas, sin ninguna marca de quemadura. Durante todo el plano no debe aparecer ninguna línea, marca, franja de luz o umbral que sugiera un límite entre las filas de árboles: la ausencia misma de esa frontera es el contenido del plano, y ningún elemento decorativo debe añadirse para sugerirla. El Pewter Sentinel no aparece en este plano. No hay edificios, columnas ni ruinas de templo, solo filas de árboles de metal pálido.

**Criterios de aceptación:** En ningún fotograma del plano aparece una línea, marca o umbral que sugiera un límite; la luz y la bruma permanecen homogéneas en todo el encuadre. Miguel conserva alas intactas sin marca de quemadura, sin arma ni vaina, en todo el plano. El centinela no aparece.

---

## 12. Plano B1C01_S7_P15  (`cambio_angulo`, 8s, idioma ES)

**Ajustes:** Ingredients to Video, describiendo el giro completo en texto en vez de fijar un frame final exacto (más fiable para rotación continua según la nota verificada del autor). Veo 3.1 Fast (fallback Lite). Duración 8s. Formato 16:9. 2 referencias: turnaround del centinela (útil para anclar los distintos ángulos de la rotación) + cuerpo celestial de Miguel. Máximo riesgo de la escena, según el propio brief: si el giro y la caminata de Miguel no se sostienen a la vez, probar primero el giro solo, incorporar después el paso de Miguel, cambiando una sola variable por intento.

**Referencias a adjuntar:**
- `character_library/otros/Pewter Sentinel/supporting_references/turnaround.png`
- `character_library/angeles/Miguel/forms/celestial/body_reference.png`

**Prompt:**
> Plano medio general fijo, altura de ojos, cámara completamente estática; el movimiento ocurre dentro del cuadro, en las propias figuras. El Pewter Sentinel, identidad de la primera referencia, centrado en el encuadre, inmóvil al inicio, gira sobre sí mismo: una rotación suave y silenciosa de toda su masa de vapor, sin ningún paso ni pierna discreta, para seguir mirando hacia donde avanza Miguel; los zarcillos de peltre, rígidos, rotan solidariamente con el núcleo mientras el resto del cuerpo se retuerce y curva en el giro, y el brillo de sus ojos se desplaza con la rotación manteniendo su intensidad, sin apagarse ni saltar de posición de golpe. Al mismo tiempo, en el borde del encuadre, Miguel, identidad de la segunda referencia, continúa caminando a su propio ritmo, sin arma, sin vaina, manos vacías, dejando el mismo patrón bajo de polvo pálido tras cada apoyo de sabatón. Ambos movimientos, el giro del centinela y la marcha de Miguel, deben sostenerse visibles a la vez durante todo el plano, sin que uno sustituya al otro. La luz cenital difusa se mantiene en raccord; el filo de luz sobre la superficie del centinela se traslada conforme gira. No hay edificios, columnas ni ruinas en el fondo, ni ningún otro personaje además de ambos.

**Criterios de aceptación:** El giro del centinela se lee como rotación fluida de toda la masa de vapor, sin ningún paso caminado ni piernas visibles. Miguel mantiene su marcha en el borde del encuadre sin arma ni vaina, con alas intactas donde sean visibles. Ambos movimientos (giro + marcha) permanecen simultáneos y visibles durante todo el plano. Si el resultado los ejecuta en serie o congela el fondo, repetir aislando primero solo el giro del centinela.

---

## 13. Plano B1C01_S7_P16  (`cambio_angulo`, 8s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 8s. Formato 16:9. 2 referencias (Miguel de perfil, centinela en rotación — se reutiliza el turnaround por continuar el mismo giro de P15). Plano de perfil con travelling lateral: coincide exactamente con la técnica que el autor verificó como fiable para ciclos de marcha, evitando el bug de caminar hacia atrás con cámara de frente.

**Referencias a adjuntar:**
- `character_library/angeles/Miguel/forms/celestial/body_reference.png`
- `character_library/otros/Pewter Sentinel/supporting_references/turnaround.png`

**Prompt:**
> Travelling lateral, paralelo a Miguel y a su misma velocidad, altura de ojos, plano americano de perfil. Miguel, identidad de la primera referencia, pasa en primer término, de perfil, avanzando a su propio ritmo, sin arma, sin vaina, sin ningún objeto en la cadera o la espalda, manos completamente vacías, dejando el mismo patrón bajo y corto de polvo pálido a cada apoyo de sabatón; el travelling mantiene su tamaño constante en cuadro, con los troncos de metal pálido pasando en paralaje detrás de él. Al fondo, a menor escala, el Pewter Sentinel, identidad de la segunda referencia, continúa girando sobre sí mismo exactamente a la misma velocidad de rotación que traía, sin salto de postura ni de velocidad, como continuación directa del giro anterior, para mantener el rostro vuelto hacia Miguel a su paso. No hay edificios, columnas ni ruinas en el fondo, ni ningún otro personaje además de ambos.

**Criterios de aceptación:** Miguel se mantiene de perfil durante todo el travelling, nunca de frente a cámara, con tamaño constante en cuadro. El giro del centinela al fondo se lee como continuación exacta de la velocidad y postura alcanzadas en el plano anterior, sin salto ni repetición. Sin arma ni vaina en Miguel.

---

## 14. Plano B1C01_S7_P17  (`cambio_angulo`, 8s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 8s. Formato 16:9. 2 referencias (Miguel cuerpo celestial, centinela ya en su pose canónica final tras completar el giro). Seguimiento desde atrás: coincide con la técnica verificada por el autor como más fiable para marcha continua. Doble verificación exigida por el brief: alas sin marca de quemadura durante todo el plano, y vapor del centinela sin solidificarse pese a quedar fijo.

**Referencias a adjuntar:**
- `character_library/angeles/Miguel/forms/celestial/body_reference.png`
- `character_library/otros/Pewter Sentinel/canonical/body_reference.png`

**Prompt:**
> Seguimiento desde atrás, misma velocidad que Miguel, altura de ojos ligeramente posterior, plano entero. Miguel, identidad de la primera referencia, de espaldas a cámara, continúa internándose en la arboleda; sus dos alas, simétricas, plegadas contra la espalda, están completamente intactas y sanas, sin ninguna marca de quemadura ni cauterización visible; sus sabatones dorados agrietados quedan visibles a cada paso, dejando el mismo patrón bajo de polvo pálido; no lleva arma, vaina ni ningún objeto en la cadera o la espalda, y sus manos permanecen vacías. Al fondo, el Pewter Sentinel, identidad de la segunda referencia, completa la rotación que traía en marcha y queda fijo, con el rostro y los ojos blancos vueltos hacia la espalda de Miguel; su cuerpo, sin piernas ni pies definidos, sin superficie metálica sólida, sin rasgo facial más allá de los ojos, sin ropa ni armadura convencional y sin arma, conserva un roce continuo de baja amplitud en toda su superficie de vapor sin quedar congelado pese a la fijeza de su orientación. La bruma de la arboleda aumenta gradualmente hacia el fondo. No hay edificios, columnas ni ruinas, ni ningún otro personaje.

**Criterios de aceptación:** Ambas alas de Miguel permanecen intactas y simétricas, sin ninguna marca de quemadura, en todo el recorrido del plano. El centinela completa su giro y queda fijo sin volverse una superficie sólida; su vapor sigue visiblemente vivo pese a la orientación fija. Sin arma en Miguel en ningún momento.

---

## 15. Plano B1C01_S7_P18  (`cambio_angulo`, 6s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 7s. Formato 16:9. 1 referencia (cuerpo del centinela). Diferenciar explícitamente 'orientación fija' (correcta) de 'vapor congelado' (incorrecta), pidiendo ambas condiciones a la vez si el generador simplifica una a costa de la otra, según el brief.

**Referencias a adjuntar:**
- `character_library/otros/Pewter Sentinel/canonical/body_reference.png`

**Prompt:**
> Plano medio fijo, altura de ojos, cámara completamente estática, centrado en el Pewter Sentinel, identidad de la referencia adjunta, ya completamente girado. El rostro y los ojos blancos brillantes permanecen fijos hacia donde avanza Miguel, fuera de este encuadre, como una aguja de brújula que no cambia de rumbo; los zarcillos de peltre en los hombros permanecen como anclajes rígidos, mientras la superficie de vapor que los envuelve mantiene un roce continuo de baja amplitud en toda su extensión, sin quedar nunca congelada pese a la fijeza de su orientación. El cuerpo, sin piernas ni pies definidos, sin superficie metálica sólida, sin ropa ni armadura convencional y sin arma, se mantiene exactamente igual de inicio a fin del plano. Miguel no aparece en este encuadre, aunque sigue avanzando fuera de campo. No hay edificios, columnas ni ruinas en el fondo, ni ningún otro personaje.

**Criterios de aceptación:** La orientación del rostro del centinela permanece fija durante todo el plano, pero su superficie de vapor conserva roce visible y continuo, sin solidificarse en ningún fotograma. Miguel ausente del encuadre.

---

## 16. Plano B1C01_S7_P19  (`cambio_angulo`, 8s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 8s. Formato 16:9. 2 referencias (Miguel cuerpo celestial, centinela en su pose fija canónica). Riesgo de oclusión de la tabla del brief: revisar inicio, oclusión parcial y final del plano por separado para comprobar que la identidad del centinela no cambia entre los fragmentos visibles entre troncos.

**Referencias a adjuntar:**
- `character_library/angeles/Miguel/forms/celestial/body_reference.png`
- `character_library/otros/Pewter Sentinel/canonical/body_reference.png`

**Prompt:**
> Seguimiento (tracking) lateral/posterior, siguiendo a Miguel a su misma velocidad, altura de ojos, plano general. Miguel, identidad de la primera referencia, de espaldas o tres cuartos, se aleja adentrándose entre las filas de árboles de metal pálido, sin arma, sin vaina, manos vacías, con sus alas intactas y sin marca de quemadura, dejando el mismo patrón de polvo pálido a cada paso. Al fondo, los troncos de metal pálido, sólidos y opacos, van ocultando progresivamente al Pewter Sentinel, identidad de la segunda referencia, que permanece fijo y vuelto hacia Miguel: el vapor de su cuerpo se corta limpiamente por la silueta de cada tronco a medida que el paralaje los interpone, sin atravesarlos en ningún momento, y el metal de los troncos nunca se vuelve translúcido. En cada franja visible entre los troncos, la textura, el color del vapor y el brillo de los ojos del centinela deben ser exactamente los mismos, como una sola figura consistente y no una distinta en cada hueco. No hay edificios, columnas ni ruinas, ni ningún otro personaje.

**Criterios de aceptación:** Los troncos ocluyen al centinela de forma progresiva y coherente, sin que su vapor los atraviese ni el metal se vuelva transparente. Todos los fragmentos visibles del centinela mantienen la misma identidad (color, densidad, brillo de ojos). Miguel conserva alas intactas sin marca de quemadura y sin arma durante todo el plano.

---

## 17. Plano B1C01_S7_P20  (`cambio_angulo`, 7s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 7s. Formato 16:9. 1 referencia (rostro del centinela, por ser los ojos el elemento clave que queda visible). Comprobar explícitamente contra el fotograma final de P19 que la naturaleza del resplandor es coherente y no se pierde ni se sustituye por un simple punto de luz, según la limitación conocida del brief.

**Referencias a adjuntar:**
- `character_library/otros/Pewter Sentinel/canonical/face_reference.png`

**Prompt:**
> Plano medio fijo, más cerrado que el anterior, altura de ojos, cámara completamente estática, centrado en el hueco entre los troncos de metal pálido donde queda el Pewter Sentinel, identidad de la referencia adjunta. Los troncos, en primer término, ocultan ya casi por completo su cuerpo; solo un resplandor tenue y difuso de sus ojos blancos y de la niebla que los rodea se distingue entre las franjas de tronco, sin apagarse del todo ni parpadear de forma errática en ningún momento del plano — la presencia del centinela persiste. Ese resplandor debe leerse como luz difusa dispersándose en vapor, con un halo suave y sin bordes duros, en contraste directo con el brillo especular y frío que tendrían los propios troncos de metal si reflejaran luz. Miguel no aparece en este encuadre. No hay edificios, columnas ni ruinas en el fondo, solo troncos de metal pálido.

**Criterios de aceptación:** El resplandor entre troncos se mantiene visible, difuso y sostenido durante todo el plano, sin apagarse ni convertirse en un simple punto de luz sin relación con vapor. No aparece ningún brillo especular de metal en el hueco entre troncos. Miguel ausente.

---

## 18. Plano B1C01_S7_P21  (`cambio_angulo`, 8s, idioma ES)

**Ajustes:** Ingredients to Video. Veo 3.1 Fast (fallback Lite). Duración 8s. Formato 16:9. 1 referencia (cuerpo celestial de Miguel). Seguimiento desde atrás: técnica verificada por el autor como fiable para marcha continua. Doble verificación exigida por el propio brief al revisar el clip generado: (1) alas intactas sin marca de quemadura durante toda la oclusión progresiva, contra character_library/angeles/Miguel/; (2) que la frase narrativa sobre la mirada del centinela en su espalda no se haya traducido en ningún efecto visual literal.

**Referencias a adjuntar:**
- `character_library/angeles/Miguel/forms/celestial/body_reference.png`

**Prompt:**
> Seguimiento desde atrás, misma velocidad que Miguel hasta perderlo entre los árboles, altura de ojos ligeramente posterior, plano entero, sin ningún corte de cámara adicional dentro del plano. Miguel, identidad de la referencia adjunta, de espaldas a cámara, sigue caminando hacia el interior de la arboleda; sus dos alas, plegadas contra la espalda, están completamente intactas y sanas, sin ninguna marca de quemadura ni cauterización en ningún momento del plano, ni siquiera mientras los troncos lo ocultan progresivamente. No lleva arma, vaina ni ningún objeto en la cadera o la espalda, sus manos permanecen vacías durante todo el recorrido, y no presenta ninguna marca física, cicatriz ni perforación visible en la piel bajo el esternón. Los árboles de metal pálido, sólidos y opacos, ocupan cada vez más el primer término hasta ocultarlo por completo hacia el final del plano; ninguna parte de su cuerpo permanece visible tras ellos en el fotograma final. El polvo pálido de sus últimos pasos queda asentado en el suelo como único rastro. La luz cenital difusa se funde progresivamente con un resplandor cálido creciente hacia el centro de la arboleda, mientras la bruma se cierra por completo tras su espalda. El Pewter Sentinel no aparece en ningún momento de este plano, y no debe añadirse ningún rayo, hilo de luz ni efecto sobreimpreso sobre la espalda de Miguel. No hay edificios, columnas ni ruinas en el fondo.

**Criterios de aceptación:** Las alas de Miguel permanecen intactas, simétricas y sin marca de quemadura en todo el proceso de oclusión progresiva. Sus manos permanecen vacías y sin arma durante todo el plano. El centinela no aparece en ningún fotograma. No se genera ningún rayo, hilo de luz ni efecto sobreimpreso sobre la espalda de Miguel representando su mirada. El plano termina con Miguel completamente oculto tras los troncos, sin ningún rastro visible salvo el polvo asentado.

---
