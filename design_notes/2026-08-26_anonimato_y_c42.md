# Anonimato de Arin Cross / Milo Ray en Libro I + reencuadre del cap. 42

**Alcance:** Libro1/EN y Libro1/ES (mecánica EN primero, ES espejo). Un archivo fuera de `Libro1/` también se tocó por ser espejo confirmado del cap. 51: `project/Chronicles_of_the_Sundering_Judgment/chapters/EN/B1C28_EN.md`. No se tocó `content/lore/personajes.md` ni ningún otro archivo de lore (conservan los nombres, son referencia interna). Verificado con `git diff` tras cada bloque de ediciones.

---

## 1. Anonimización — tabla de menciones (antes → después)

Grep de partida: `Arin`, `Milo`, `Cross`, `Ray` en `Libro1/EN/*.md` y `Libro1/ES/*.md`. Apariciones reales en 5 capítulos: **07, 11, 12, 47, 51** (coincide con la tabla de primera aparición en L1 de `content/lore/presencia_biblia.md` §1.2 — Cap. 7 para Arin/Thaeriel, Cap. 47 para Milo/Ereloth).

| Cap. | Antes (EN) | Después (EN) |
|---|---|---|
| 07 | `"Hey, Arin"` (saludo de un estudiante, sin respuesta) | saludo descuidado sin nombre — se conserva el gesto (lo saludan, no responde), desaparece el nombre |
| 07 | "a single overheard name, Arin, nothing more" | frase eliminada; el catálogo de Sariel queda solo en "the plain fact of his face" |
| 11 | "Arin Cross, for the better part of an hour, did nothing remarkable..." | "The mercenary, for the better part of an hour..." |
| 12 | "Sariel had been watching Arin Cross for the better part of a week" | "...watching the mercenary..." |
| 12 | "Arin Cross did not run." | "The mercenary did not run." |
| 12 | "arrested inches from Arin's outstretched hand" / "sleeping in Arin for a week" | "his outstretched hand" / "sleeping in him for a week" |
| 12 | "Arin blinked, staring at his own outstretched hand..." | "He blinked, staring at his own outstretched hand..." |
| 47 | "Arin Cross was shelving books..." | "A mercenary was shelving books..." |
| 47 | "Arin had spent enough of his working life..." (×2 más, mismo párrafo/siguientes) | "He had spent..." / "He knelt there a while..." |
| 47 | "Milo Ray stopped mid-chord..." | "A street musician stopped mid-chord..." |
| 47 | "Milo felt none of that rhythm anymore" | "He felt none of that rhythm anymore" |
| 51 | "a young man named Arin Cross went down mid-stride" | "a young man went down mid-stride" |
| 51 | "a musician named Milo Ray stopped tuning his guitar" | "a musician stopped tuning his guitar" |
| B1C28_EN.md (espejo del 51) | mismas dos líneas | mismo cambio, aplicado en espejo |

El espejo ES del cap. 51 (`Libro1/ES/51_The_Echo_of_the_Sword.md`) **ya estaba anonimizado** de origen — dice "un joven" y "un músico" sin nombre en las líneas 81 y 83. No requirió edición; confirmado por grep antes de tocar nada.

Todas las demás filas de la tabla se replicaron 1:1 en el espejo ES correspondiente (mismo capítulo, misma línea), con "el mercenario" / "un mercenario" y "un músico callejero" como equivalentes de "the mercenary" / "a mercenary" / "a street musician". Verificado al final: `grep -rn "Arin\|Milo Ray\|\bMilo\b" Libro1/EN Libro1/ES` → sin resultados.

**Ajuste adicional en cap. 47 (ambos idiomas), fuera del simple cambio de nombre:** la frase que describía las líneas de luz en las palmas del mercenario "in patterns that resembled... chains" / "en patrones que se parecían... a cadenas" se suavizó a "in patterns he couldn't parse" / "en patrones que no lograba descifrar". Esa imagen de cadenas es la seña visual específica de Thaeriel en `content/lore/presencia_biblia.md` §1.2 ("fuego pálido envuelto en cadenas") — dejarla intacta habría revelado el poder/identidad concretos aunque el nombre desapareciera, y el encargo es explícito: "PROHIBIDO: mostrar poderes o revelar identidad." El resto de la escena de resonancia (el dolor fantasma, el peso de lanza, la reacción de Sariel al camión en el cap. 12) se dejó intacto: es intriga genuina y sin etiqueta — Sariel nunca logra clasificar lo que ve ("It answered to no one — not angel, not demon, nothing his training had a name for"), que es exactamente el registro que el autor autorizó ("puedes hablar de un mercenario [con un poder que ni Sariel puede nombrar]").

---

## 2. Lectura del "joven de la biblioteca" en el cap. 47 y su eco en el 51

Leí el capítulo 47 completo y el tramo del 51 que lo espeja (líneas ~70–95 EN). Conclusión: **es Arin (ahora "el mercenario"), no un tercer personaje.** Evidencia:

- El 47 lo nombra explícitamente tres veces seguidas en el mismo pasaje de la biblioteca (antes de mi edición: "Arin Cross was shelving books... Arin had spent enough of his working life... Arin knelt there a while..."), y describe un rasgo de caracterización coherente con el resto de sus apariciones (trabajo cerca de "heridas genuinas", vida hecha de "moments mucho más peligrosos que un pasillo de biblioteca" — encaja con el perfil de mercenario ya visto en cap. 7/11/12).
- El eco del cap. 51 (línea 81 original) lo vuelve a nombrar como "a young man named Arin Cross", con **la misma localización exacta** (estanterías superiores de la biblioteca de Navarion) y el mismo tipo de dolor fantasma. Es una repetición deliberada del mismo beat narrativo, no una escena nueva.

Existe un **tercer personaje real** en el capítulo 51, pero está en una escena aparte, más adelante (líneas ~103–119 EN / ES), en una playa distinta: "un joven" de cabello encanecido temprano que camina por la orilla tocándose un colgante metálico, soñando con "torres en llamas" y una palabra que guarda en el pecho — *Miguel*. Este es, casi con certeza, la reencarnación de Miguel/Mikel Ardon (protagonista de Libro 2), no Arin ni un "precursor del colgante" adicional. Ya estaba correctamente anónimo en ambos idiomas (ES ya decía "un joven" sin nombre; EN tampoco lo nombra) — **no requirió ningún cambio**, y no debe confundirse con la escena de la biblioteca. Tampoco hay mención de "pendant"/"colgante" en ningún otro punto de Libro1 fuera de esas dos líneas del cap. 51.

---

## 3. Reencuadre del cap. 42 — "The Master of Lament" / "El Maestro de Lamentum"

**Qué se cambió:** todo el tramo que dramatizaba dominio/maestría por combate (líneas 3–51 EN originales: duelos de entrenamiento contra su teniente Rovash, la sala de entrenamiento tallada en piedra negra, Foras observando en persona, el discurso final a las legiones) se reescribió como una **marcha de varias semanas** desde el Sepulcro Doliente hasta el trono de Lucifer, con tres guarniciones del Cielo cayendo en el camino (esto además ancla en la propia prosa la línea de Lucifer "the weapon that broke a dozen garrisons in a single night", que antes quedaba un poco suelta respecto de una escena de solo entrenamiento). Durante la marcha, Belial libra una discusión consigo mismo en dos frentes:

- **Quedársela** = poder propio y ruptura — puede sentir "exactamente cuán poco haría falta" para dar media vuelta con la legión y construir un trono propio sin pedir permiso a nadie.
- **Entregarla** = la apuesta larga — la aritmética de un usurpador solitario (ejército propio, sin trono en que apoyarse, sin nombre que la historia distinga del simple robo) contra la de un rey que recuerda por más tiempo a quien le entrega un arma de rodillas que a quien solo supo usarla bien.

Rovash deja de ser su sparring partner y pasa a ser el teniente que marcha con él y le trae noticias de la fortaleza (Foras y los capitanes de Vepar "contando espadas" en su ausencia) — este diálogo además siembra, de forma deliberada pero no idéntica, la línea "the captains are already counting swords" que el lector reencuentra en boca del teniente del cap. 51. La visión del arcángel llorando se conserva, pero ahora ocurre durante el primer combate real (la primera guarnición cayendo), no en un duelo de entrenamiento — es el único "presupuesto de imagen" que gasté en todo el tramo, reutilizando una imagen ya establecida en vez de añadir una nueva. El peso físico de la lanza queda como correlato literal de la resolución de Belial: se aligera un poco las mañanas en que despierta ya decidido a terminar la marcha, sin desaparecer nunca del todo — esto sustituye la vieja idea de "dominarla" por algo más honesto con la aflicción como mecánica.

**Qué NO se tocó:** la escena de entrega final (líneas 53–69 EN / 53–69 ES: Belial se arrodilla ante Lucifer, el diálogo completo) queda exactamente como estaba, ya aprobada. Solo corregí una frase suelta dentro de ese tramo intocable que había quedado huérfana tras el reencuadre: "bleeding for her in the training hall" → "bleeding for her on the march" (y su espejo ES "en la sala de entrenamiento" → "durante la marcha"), porque la sala de entrenamiento ya no existe en la nueva versión del capítulo y la frase original habría contradicho la propia escena de cierre. Es el único cambio dentro del bloque "no la toques".

**Corrección de continuidad menor, de paso:** el ES del capítulo usaba "Sepulcro Llorante" en la línea 29 original, mientras el resto del libro (caps. 13, 15, 16, 18, 19, 20, 27, etc.) usa consistentemente "Sepulcro Doliente" para el mismo lugar. Al reescribir el párrafo de apertura fijé "Sepulcro Doliente" para alinear con el resto de Libro I — vale la pena que quede registrado por si el autor prefiere lo contrario.

**Extensión:** el tramo reescrito pasó de ~25 párrafos a 15, un recorte comparable al -23%/-33% que craft/12 documenta para capítulos de interioridad — no fue el objetivo, pero es la magnitud esperable al quitar los cinco duelos de entrenamiento repetidos.

### 3 títulos candidatos (sin aplicar — decide el autor)

1. **EN:** *What He Carried to the Throne* — **ES:** *Lo que le llevó al trono*
   (centra el capítulo en el objeto y el trayecto, no en el dominio del arma.)
2. **EN:** *Every League a Temptation* — **ES:** *Cada legua, una tentación*
   (el más literal respecto del encargo del autor — la marcha como serie de decisiones.)
3. **EN:** *The Long Wager* — **ES:** *La apuesta larga*
   (nombra directamente el cálculo de ambición paciente que cierra el capítulo — Belial apostando a la memoria de un rey en vez de al poder inmediato.)

---

## 4. Verificación

- `grep -rn "Arin\|Milo Ray\|\bMilo\b" Libro1/EN Libro1/ES` → sin resultados tras las ediciones.
- `git diff --stat` confirma los 6 capítulos tocados en cada idioma (07, 11, 12, 42, 47, 51) más el espejo `B1C28_EN.md`. `Libro1/EN/_manifest.json` y `Libro1/ES/_manifest.json` aparecen en el diff porque ya estaban modificados antes de empezar esta tarea (working tree previo) — no los toqué.
- Paridad de párrafos verificada línea por línea en el cap. 42: 24 párrafos en EN, 24 en ES, mismos separadores en blanco, mismo patrón de diálogo (comillas en EN, raya en ES).
- Réplicas de diálogo preexistentes: ninguna de las líneas de diálogo tocadas en 07/11/12/47/51 contenía los nombres a anonimizar (todas las apariciones de "Arin"/"Milo" estaban en narración, salvo el saludo "Hey, Arin" del cap. 7, que sí es una réplica — se eliminó el nombre dentro de ella porque es precisamente el tipo de mención que el encargo pide anonimizar; el resto de la línea de diálogo original no tenía comillas propias, era una cita indirecta dentro de la narración).
