# Corin Vasse

Mecánico mortal, seis años en el mismo taller de pueblo; reencarnación mortal e inconsciente del comandante neutral Krass. Edad aparente no especificada en la fuente.

## Identidad inmutable

- Estructura facial: rasgos no especificados por la fuente más allá de una rigidez pétrea y defensiva perceptible, que borra su habitual expresión distendida de mecánico.
- Marca distintiva: pequeña cicatriz en un nudillo por un resbalón antiguo con una llave inglesa.
- Manos: grasa de motor grisácea persistente bajo las uñas.
- Vestuario inmutable: abrigo de lona desgastado.
- Color de pelo, color de ojos y estatura: no especificados por la fuente.

El diseño visual establecido en las referencias (pelo oscuro, ojos claros, abrigo de cuero marrón con hombreras y túnica azul) es consistente entre las hojas de expresiones, turnaround, detalles y poses, pero no adquiere por ello autoridad narrativa más allá de lo listado arriba.

## Vestuario y accesorio

- Abrigo largo marrón con hombreras reforzadas y cierres metálicos, túnica azul interior, pantalón oscuro y botas con refuerzos dorados — diseño consistente en las hojas de referencia (ver nota técnica abajo sobre una excepción).
- Llave inglesa (wrench) como accesorio de oficio recurrente en las poses de referencia.

## Nota narrativa

Corin Vasse lleva sin saberlo el alma reencarnada de Krass (`demonios/krass`, procesado por separado en `character_library/Krass/`) — un vínculo narrativo únicamente; no copiar el diseño visual de Krass en Corin Vasse ni viceversa.

## Referencias

- `canonical/face_reference.png`: autoridad para rostro, pelo y ojos. Generado a partir de `corinvasse-reference-turnaround.png` y `corinvasse-reference-details.png` (ver nota técnica).
- `canonical/body_reference.png`: autoridad para proporciones, vestuario y accesorios.
- `supporting_references/expressions.png` y `turnaround.png`: apoyo secundario.

**Nota técnica:** el archivo fuente `corinvasse-master-reference.png` (copiado sin modificar en `canonical/body_reference.png`, según la regla del pipeline de no reencodear ni alterar fuentes) es visualmente inconsistente con el resto de la ficha de este personaje y con su identity_lock: muestra alas y armadura que no corresponden a un mecánico mortal, mientras que `corinvasse-reference-expressions.png`, `-turnaround.png`, `-details.png` y `-poses.png` sí son consistentes entre sí y con el lock. Por eso `face_reference.png` se generó a partir de esas hojas y no del master-reference. Se recomienda revisar/regenerar el master-reference de origen en `video_production/images_personajes/mortales/corinvasse/` antes de usar `body_reference.png` en producción.

Las fuentes originales permanecen en `video_production/images_personajes/mortales/corinvasse/`.
