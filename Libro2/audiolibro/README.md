# Audiolibro — Book 2 (English)

Texto limpio para narración/TTS, generado desde Libro2/EN/ (canónico).

- Un archivo por capítulo: audiolibro_capitulo_NN.txt, en orden de lectura.
- Primera línea hablada: "Chapter N. Título."
- Sin markdown: cursivas/negritas eliminadas conservando el texto.
- Cambios de escena marcados con una línea "..." (los motores TTS la
  interpretan como pausa sin vocalizarla; un narrador humano la lee
  como silencio breve).
- Regenerable: si la prosa EN cambia, volver a ejecutar el script de
  generación (ver historial git de esta carpeta).
