# Audiolibro — Book 3 (English)

Texto limpio para narración/TTS, generado desde Libro3/EN/ (canónico).

- Un archivo por capítulo: audiolibro_capitulo_NN.txt, en orden de lectura.
- Primera línea hablada: "Chapter N. Título."
- Sin markdown: cursivas/negritas eliminadas conservando el texto.
- Cambios de escena marcados con una línea "..." (los motores TTS la
  interpretan como pausa sin vocalizarla; un narrador humano la lee
  como silencio breve).
- Regenerable: si la prosa EN cambia, volver a ejecutar el script de
  generación (ver historial git de esta carpeta).

**Pronunciación**: la guía canónica de todos los nombres inventados está en
`../../audiolibro_guia_pronunciacion.md` (raíz del proyecto) — leerla antes
de grabar el primer episodio o configurar el TTS.
