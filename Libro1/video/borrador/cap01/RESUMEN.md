# Piloto — Libro I, Capítulo 1 ("Una Herida en el Mundo")

**BORRADOR — pendiente de aprobación del autor. NO listo para producción.** Generado la noche del 2026-09-16 al 2026-09-17, de forma autónoma, por el Workflow multi-agente de la Etapa 1 de la skill cinematográfica. Nada de esto se ha commiteado.

**Veredicto final, tras las dos capas de QA (el propio pipeline + revisión independiente de Codex): el enfoque (especialistas por dominio + doble QA) es razonable y ya demuestra que detecta fallos reales, pero este primer guion concreto no está listo para enviarse a generación.** Léase como material de preproducción a corregir, no como guion final. Informe completo en [REVISION_CODEX.md](REVISION_CODEX.md) — es duro y específico, léelo entero antes de decidir cómo seguir.

## Qué se generó

El capítulo (2.014 palabras EN / 2.003 ES, paridad de párrafos correcta: 35↔35) se dividió en **6 escenas**, 122 planos, 930 s (15,5 min) en total. Cada plano pasó por 4 agentes especializados (Dirección/Previz, Luz, VFX, Continuidad inter-plano) y un agente de traducción a Google Flow / Storyboard Studio.

Archivos: `B1C01_S1.json` … `B1C01_S6.json`, `guion_completo.json` (todo junto), `REVISION_CODEX.md` (revisión independiente completa, 186 líneas).

## Los 3 problemas más importantes que hay que resolver antes de seguir

### 1. Fallo estructural en el esquema que yo mismo diseñé esta noche

Simplifiqué el contrato de `content/craft/18_continuidad_inter_plano.md` para que fuera manejable por un agente en un pilotaje: convertí el "estado" (que el documento 18 pide como objeto estructurado, campo a campo) en texto descriptivo libre (`estado_entrada`, `estado_salida_previsto` como strings). Codex tiene razón en que esto es una simplificación real, no solo una diferencia de formato: **faltan los campos que el documento 18 marca como obligatorios y que existen justo para bloquear un plano que no se puede aprobar todavía** — `estado_salida_observado`, `frame_final`, `control_calidad`, `enlace`, versionado de plano. Sin esos campos, nada en el JSON impide automáticamente que una incidencia detectada bloquee de verdad el envío del plano siguiente; hoy solo lo dice el texto de una nota. Antes de otro piloto completo, el esquema de la fase de Continuidad necesita ampliarse para que las incidencias bloqueen de verdad, no solo se describan.

### 2. Duplicación de beats narrativos entre escenas (afecta al ritmo y a los 930 s)

Codex detectó que varios beats del texto se representan dos veces en escenas distintas (el giro hacia el llamado del párrafo 10 aparece al final de S1 Y al principio de S2; el guardián del párrafo 32 se resuelve en S5 y se repite en la apertura de S6). Esto significa que los 930 s "sin relleno artificial" que reporté antes no son del todo ciertos — hay sostenidos y repeticiones que inflan la duración. Necesita una pasada de segmentación más ajustada, probablemente con menos solapamiento en los límites de escena.

### 3. Conflictos de canon — 2 de 3 ya resueltos por el autor (2026-09-18)

- ✅ **Gabriel — RESUELTO: sin armadura, siempre.** Confirmado contra `canonical/body_reference.png`: túnica azul y plata, sin peto metálico. El README ya está corregido. La causa raíz era más profunda de lo que parecía: el README apuntaba a un archivo `design_notes/2026-09-16_flow_storyboard_studio_cap01.md` que nunca existió en este checkout — eran pruebas descartadas. Se limpiaron las mismas referencias fantasma en los README de Miguel, Lucifer y Pewter Sentinel.
- ✅ **Pewter Sentinel — RESUELTO: diseño de niebla/vapor, tal cual la imagen canónica.** El autor decidió que el rediseño de niebla (ojos blancos brillantes, cuerpo que se disuelve en vapor sin piernas, zarcillos de peltre en los hombros) es el vigente para el capítulo 1 también, **aunque el texto describa una figura sólida**. Pendiente: los planos de la escena S5 (`B1C01_S5.json`) todavía describen la versión sólida y hay que reescribirlos en la próxima pasada para que coincidan con el diseño de niebla — esto cambia bastante la escena (sin piernas/pies que mostrar, flotación, cara casi sin rasgos con ojos brillantes en vez de rostro liso "sin un solo rasgo").
- ⏳ **Curación del ala de Miguel en el flashback (S3) — pendiente.** El pipeline construyó una progresión hasta un ala "cicatrizada/cerrada" que el capítulo no describe con ese detalle (solo dice que Gabriel cauteriza el ala rota durante tres noches). No es necesariamente un error, pero es una concreción visual inventada por el agente que no debería fijarse como canon solo por haberse escrito una vez.

## Otros hallazgos de Codex (con detalle línea a línea en REVISION_CODEX.md)

- El veredicto de QA automático del propio pipeline ("3 fronteras incoherentes, 2 coherentes") era **demasiado optimista**: Codex reclasifica S4→S5 como también incoherente (la herida de Miguel se silencia antes de tiempo, no solo en S5→S6 como decía el QA interno), y encuentra que el QA interno tiene además un falso positivo (interpretó "todavía suplicando" como habla en curso cuando el propio plano lo describe como estado emocional, no diálogo).
- Dentro de las escenas revisadas en detalle (S2 y S5, elegidas al azar), **no** encontró el bug original que motivó todo esto (una mano que desaparece y reaparece) — buena señal para el agente de Continuidad — pero sí encontró fallos de menor entidad: un plano que repite el mismo umbral dos veces (S5 P01→P02), un giro que se resuelve dos veces (S5 P19→P20), y un conflicto de guante/piel en el momento de tocar la espada (S6_P22 exige contacto de piel pero el vestuario declarado sigue siendo el guante).
- Los prompts de Flow **no están listos para copiar y pegar todavía**: mezclan diálogo ES y EN en el mismo prompt, algunos piden más de las 3 referencias recomendadas por el documento 14 (42 de 122 planos), y algunas "referencias_adjuntas" apuntan a un README en vez de a una imagen real.

## Qué NO se ha hecho (a propósito)

- No se ha generado ningún vídeo real en Flow.
- No se ha commiteado ni hecho push de nada.
- No se ha corregido nada de lo anterior automáticamente — son decisiones de canon (Gabriel, Pewter Sentinel) o de diseño del pipeline (esquema, segmentación) que te corresponden a ti.

## Próximo paso sugerido

1. Lee `REVISION_CODEX.md` completo — es más preciso que este resumen.
2. Decide los 3 conflictos de canon (Gabriel, Pewter Sentinel, ala de Miguel).
3. Decide si quieres que ampliemos el esquema de Continuidad para que cumpla el contrato completo del documento 18 (bloqueo real, no solo textual) antes de otro piloto — mi recomendación es sí, es la pieza que más se acerca a resolver el bug original de raíz.
4. Con eso resuelto, una segunda pasada del pipeline sobre este mismo capítulo, ya corrigiendo lo anterior, sería la prueba real de si el método funciona.
