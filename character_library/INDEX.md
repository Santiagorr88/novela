# Character Library

Biblioteca reutilizable de identidad visual para generación de imágenes y vídeo, organizada a partir de los paquetes Character Studio existentes en `video_production/images_personajes/`. Cada personaje separa la identidad estable (`canonical/`) de sus formas (`forms/`) y estados narrativos (`states/`).

**Estado: 80/80 personajes con carpeta propia completos** (85 carpetas de origen − 5 fusionadas como formas humanas de otro personaje: Mikel Ardon→Miguel, Milo Ray→Ereloth, Cam Loren→Camael, Sabio de la Cumbre→Azael, Arin Cross→Thaeriel), más **Pewter Sentinel** (guardián de la Arboleda, no es un personaje de `personajes.md`). Trabajo iniciado por Codex (Miguel, Gabriel, Lucifer) y continuado por Claude para el resto.

**Estructura por bando (2026-09-16)**: cada personaje vive en `angeles/`, `demonios/` o `humanos/` según su bando; `otros/` reúne entidades sin bando (Pewter Sentinel). Los enlaces de abajo ya apuntan a la ruta correcta.

## Orden de autoridad

Cuando dos referencias discrepen, aplicar este orden:

1. El `README.md` del personaje y el `README.md` de la forma o estado activo.
2. `canonical/face_reference.png` para rostro, edad aparente, pelo y ojos.
3. `canonical/body_reference.png` para proporciones, vestuario, materiales y silueta.
4. `supporting_references/` para expresiones y ángulos adicionales.
5. El prompt del plano solo decide pose, encuadre, acción, luz y escenario.

Las referencias de apoyo nunca deben introducir rasgos que contradigan el lock textual.

**Nota de método**: `face_reference.png` de cada personaje es una imagen generada (no un recorte) a partir del `master-reference` aprobado, vía `gemini_gen.py` — las fuentes originales solo traen hojas multipanel sin ningún primer plano limpio aislado. `body_reference.png` es siempre copia literal del `master-reference` de origen, sin generación ni modificación.

## Uso mínimo

1. Adjuntar `canonical/face_reference.png` y `canonical/body_reference.png`.
2. Partir de `prompts/01_portrait_prompt.txt` o `prompts/02_fullbody_prompt.txt`.
3. Añadir el bloque de la forma y del estado narrativo que corresponda.
4. Describir aparte el plano: acción, cámara, escenario e iluminación.
5. Comprobar rostro, lateralidad, manos, accesorios y elementos prohibidos antes de aprobar el resultado.

## Personajes con formas múltiples

| Personaje | Formas | Notas |
|---|---|---|
| [Miguel](angeles/Miguel/README.md) | `celestial` (canónica); `human` (Mikel Ardon) | Estado `burned_left_wing` disponible; versión v1 archivada en `archive/`. |
| [Ereloth](angeles/Ereloth/README.md) | `celestial` (canónica); `human` (Milo Ray) | Autoinserto del autor — ver `[[user_ereloth_autor]]`; solo se organizaron referencias ya aprobadas, ningún rasgo nuevo inventado. |
| [Azael](angeles/Azael/README.md) | `celestial` (canónica); `human` (El Sabio de la Cumbre) | Identidad confirmada en `content/lore/grafo_conocimiento.md` (H9). |
| [Camael](angeles/Camael/README.md) | `celestial` (canónica); `human` (Cam Loren) | **NEEDS_REVIEW** — ver abajo. |
| [Thaeriel](angeles/Thaeriel/README.md) | canónica (ángel); `human` (Arin Cross) | Identidad confirmada en `content/lore/grafo_conocimiento.md` (H8). |
| [Lucifer](demonios/Lucifer/README.md) | canónica (demonio); `forms/demonic/` y `forms/human/` | Subcarpetas creadas por Codex como marcadores, **sin poblar** — no hay fuente de imágenes asignada todavía. |

Personajes con "Human Form" documentado en `personajes.md` pero **sin** paquete de imágenes fuente (no se creó `forms/`, solo se anota en el README): Gabriel (Gabren Elion), Rafael (Rapha Elion), Zadkiel (Zad Lorien).

## Todos los personajes (80)

| Personaje | Bando | Formas | Estado |
|---|---|---|---|
| [Aamon](demonios/Aamon/README.md) | Demonio | — | READY |
| [Agares](demonios/Agares/README.md) | Demonio | — | READY |
| [Amy](demonios/Amy/README.md) | Demonio | — | READY |
| [Anael](angeles/Anael/README.md) | Ángel | — | READY |
| [Andras](demonios/Andras/README.md) | Demonio | — | NEEDS_REVIEW — alas y segunda daga en `body_reference` no confirmadas por el lock ni por `personajes.md`; ver README |
| [Asmodeus](demonios/Asmodeus/README.md) | Demonio | — | READY |
| [Azael](angeles/Azael/README.md) | Ángel | celestial, human | READY |
| [Balam](demonios/Balam/README.md) | Demonio | — | READY |
| [Barachiel](angeles/Barachiel/README.md) | Ángel | — | READY |
| [Barbas](demonios/Barbas/README.md) | Demonio | — | NEEDS_REVIEW — alas confirmadas por el lock pero sin diseño/color fijado; `body_reference` es la única autoridad de momento |
| [Belial](demonios/Belial/README.md) | Demonio | — | READY |
| [Camael](angeles/Camael/README.md) | Ángel | celestial, human | NEEDS_REVIEW — `forms/human/` (Cam Loren): el `master-reference` de origen muestra una figura alada y con armadura, contradiciendo su propio `identity_lock.txt` ("luchador clandestino desarmado"); revisar la imagen fuente en `video_production/images_personajes/mortales/camloren/` antes de usar en producción |
| [Cassiel](angeles/Cassiel/README.md) | Ángel | — | READY |
| [Corin Vasse](humanos/Corin%20Vasse/README.md) | Mortal | — | NEEDS_REVIEW — `master-reference` de origen probablemente equivocado (muestra una figura alada/con armadura, no un mecánico mortal); `face_reference.png` se generó a partir de las hojas de expresiones/turnaround (consistentes con el lock) en vez del master; revisar `video_production/images_personajes/mortales/corinvasse/corinvasse-master-reference.png` |
| [Daith](angeles/Daith/README.md) | Ángel | — | READY |
| [Dantalion](demonios/Dantalion/README.md) | Demonio | — | READY |
| [Dez](humanos/Dez/README.md) | Mortal | — | READY |
| [Elom](angeles/Elom/README.md) | Ángel | — | NEEDS_REVIEW — `identity_lock.txt` de origen no especifica rostro, cuerpo ni altura (solo vestuario y arma); README lo declara explícitamente en vez de inventar rasgos |
| [Ereloth](angeles/Ereloth/README.md) | Ángel | celestial, human | READY |
| [Eshriel](angeles/Eshriel/README.md) | Ángel | — | READY |
| [Ezequiel](angeles/Ezequiel/README.md) | Ángel | — | READY |
| [Ezihel](angeles/Ezihel/README.md) | Ángel | — | READY |
| [Flauros](demonios/Flauros/README.md) | Demonio | — | READY |
| [Foras](demonios/Foras/README.md) | Demonio | — | READY |
| [Gabriel](angeles/Gabriel/README.md) | Ángel | — | READY |
| [Gusion](demonios/Gusion/README.md) | Demonio | — | READY |
| [Hadriel](angeles/Hadriel/README.md) | Ángel | — | READY |
| [Halaliel](humanos/Halaliel/README.md) | Mortal | — | READY |
| [Iofiel](angeles/Iofiel/README.md) | Ángel | — | READY |
| [Jahiel](angeles/Jahiel/README.md) | Ángel | — | READY |
| [Jeremiel](angeles/Jeremiel/README.md) | Ángel | — | READY |
| [Jophiel](angeles/Jophiel/README.md) | Ángel | — | READY |
| [Joran](humanos/Joran/README.md) | Mortal | — | READY |
| [Kadan](angeles/Kadan/README.md) | Ángel | — | READY |
| [Karin](angeles/Karin/README.md) | Ángel | — | READY |
| [Kaviel](angeles/Kaviel/README.md) | Ángel | — | READY |
| [Kemuel](angeles/Kemuel/README.md) | Ángel | — | READY |
| [Korvel](demonios/Korvel/README.md) | Demonio | — | READY |
| [Krass](demonios/Krass/README.md) | Demonio | — | READY — nota de continuidad: Corin Vasse lleva su alma reencarnada, diseños no compartidos |
| [Kurel](angeles/Kurel/README.md) | Ángel | — | READY |
| [Kushiel](angeles/Kushiel/README.md) | Ángel | — | READY |
| [Laila](angeles/Laila/README.md) | Ángel | — | READY — lock minimalista, sin inventar rasgos |
| [Leraje](demonios/Leraje/README.md) | Demonio | — | READY |
| [Leviathan](demonios/Leviathan/README.md) | Demonio | — | NEEDS_REVIEW — `identity_lock.txt` dice "ojos ciegos" pero el `master-reference` muestra ojos brillantes de pupila hendida; discrepancia preexistente en la fuente, no introducida en esta pasada |
| [Lucifer](demonios/Lucifer/README.md) | Demonio | demonic (vacía), human (vacía) | READY (canónica) — `forms/` sin poblar |
| [Malphas](demonios/Malphas/README.md) | Demonio | — | READY |
| [Malthus](demonios/Malthus/README.md) | Demonio | — | READY |
| [Marbas](demonios/Marbas/README.md) | Demonio | — | READY |
| [Miguel](angeles/Miguel/README.md) | Ángel | celestial, human | READY |
| [Naamah](demonios/Naamah/README.md) | Demonio | — | READY |
| [Nael](angeles/Nael/README.md) | Ángel | — | READY |
| [Nocthel](demonios/Nocthel/README.md) | Demonio | — | READY |
| [Nymos](demonios/Nymos/README.md) | Demonio | — | READY |
| [Orifiel](angeles/Orifiel/README.md) | Ángel | — | READY |
| [Orobas](demonios/Orobas/README.md) | Demonio | — | READY |
| [Pewter Sentinel](otros/Pewter%20Sentinel/README.md) | Otros (guardián de la Arboleda, sin bando) | — | READY |
| [Phenex](demonios/Phenex/README.md) | Demonio | — | READY |
| [Rafael](angeles/Rafael/README.md) | Ángel | — | READY — forma humana (Rapha Elion) documentada sin imágenes fuente |
| [Raguel](angeles/Raguel/README.md) | Ángel | — | READY |
| [Raum](demonios/Raum/README.md) | Demonio | — | READY |
| [Raziel](angeles/Raziel/README.md) | Ángel | — | READY |
| [Remiel](angeles/Remiel/README.md) | Ángel | — | READY — lock minimalista |
| [Ronove](demonios/Ronove/README.md) | Demonio | — | READY |
| [Sachael](angeles/Sachael/README.md) | Ángel | — | READY — lock minimalista |
| [Sariel](angeles/Sariel/README.md) | Ángel | — | READY |
| [Selaphiel](angeles/Selaphiel/README.md) | Ángel | — | READY |
| [Selke](humanos/Selke/README.md) | Mortal | — | READY |
| [Selm](demonios/Selm/README.md) | Demonio | — | READY |
| [Stolas](demonios/Stolas/README.md) | Demonio | — | READY |
| [Thaeriel](angeles/Thaeriel/README.md) | Ángel | human (Arin Cross) | READY |
| [Thariel](angeles/Thariel/README.md) | Ángel | — | READY |
| [Thoria](angeles/Thoria/README.md) | Ángel | — | READY |
| [Uriel](angeles/Uriel/README.md) | Ángel | — | READY |
| [Valefar](demonios/Valefar/README.md) | Demonio | — | READY |
| [Vem](demonios/Vem/README.md) | Demonio | — | READY |
| [Vepar](demonios/Vepar/README.md) | Demonio | — | READY |
| [Vine](demonios/Vine/README.md) | Demonio | — | READY |
| [Vual](demonios/Vual/README.md) | Demonio | — | READY |
| [Yaron](angeles/Yaron/README.md) | Ángel | — | READY |
| [Zadkiel](angeles/Zadkiel/README.md) | Ángel | — | READY — forma humana (Zad Lorien) documentada sin imágenes fuente |
| [Zaphiel](angeles/Zaphiel/README.md) | Ángel | — | READY |

## Necesita revisión del autor

- **Camael / Cam Loren** (`Camael/forms/human/`): la imagen fuente muestra un personaje alado y con armadura, no el "luchador clandestino desarmado" de su propio `identity_lock.txt`. Revisar `video_production/images_personajes/mortales/camloren/camloren-master-reference.png`.
- **Corin Vasse** (`Corin Vasse/`): el `master-reference` de origen parece ser la imagen equivocada (alada/con armadura, no un mecánico mortal). El resto del paquete (expresiones, turnaround, details, poses) sí es consistente entre sí y con el lock — el `face_reference.png` de la biblioteca se generó a partir de esas hojas en vez del master para no heredar el error, pero `body_reference.png` es copia literal del master y por tanto hereda el diseño incorrecto (regla de "nunca modificar la fuente"). Revisar `video_production/images_personajes/mortales/corinvasse/corinvasse-master-reference.png`.
- **Elom**: `identity_lock.txt` no define rostro, cuerpo ni altura — solo vestuario y arma. No se ha inventado nada; si se quiere una identidad facial/corporal completa, hay que ampliarlo en origen.
- **Andras**: `body_reference.png` muestra alas membranosas y una segunda daga que ni el lock ni `personajes.md` confirman — tratar como diseño heredado no canónico hasta que el autor lo confirme o lo descarte.
- **Barbas**: tiene alas confirmadas por el lock pero sin diseño/color fijado en el texto; `body_reference.png` es la única autoridad visual por ahora.
- **Leviathan**: el lock dice "ojos ciegos" pero el master muestra ojos brillantes con pupila hendida — discrepancia ya existente en la fuente, no introducida en esta organización.
- **Lucifer**: `forms/demonic/` y `forms/human/` existen como carpetas vacías (marcador de Codex) — no hay paquete de imágenes fuente asignado todavía para ninguna de las dos.
