# Auditoría de coherencia — Hilo 13 (Naamah y sus capitanes) + Hilo 28 (Aamon y la legión huérfana)

**Fecha**: 2026-08-22
**Alcance**: `Libro1/EN/13_The_Devils_Gambit.md`, `Libro1/EN/15_The_Price_of_Truth.md`, `Libro2/EN/23_A_Thiefs_Legacy.md`, `Libro2/EN/26_Report_from_the_Abyss.md`, `Libro2/EN/50_The_Unaccounted_Variable.md`, `Libro3/EN/30_Whose_Idea_This_Was_Already.md`, `Libro3/EN/31_What_No_One_Came_Back_For.md`, `Libro3/EN/32_Two_Ways_to_Ruin_a_Man.md`.
**Fuente de verdad**: `2026-08-22_coherence_audit_thread_map.md` (secciones 2 y 3).
**Método**: lectura completa de los ocho capítulos en el orden indicado, cotejo contra el registro de vida/muerte y el mapa de hilos, y verificación cruzada puntual contra `content/lore/personajes.md` para las fichas de Aamon, Naamah, Gusion, Phenex, Leraje, Ronove y Dantalion.

---

## Resultado general

**No se detectaron incoherencias reales en la prosa** para este hilo. Los tres puntos que el encargo pedía verificar explícitamente se sostienen:

### 1. Consistencia de la muerte de Aamon

`Libro1/EN/15_The_Price_of_Truth.md` es inequívoco: Belial maniobra a Aamon herido hacia un sigilo marcado de antemano ("herding him... toward a stretch of ground marked with a sigil"), lo derriba de un golpe sobre las líneas grabadas, y clava a Ruach en su corazón mientras la invocación drena su esencia hacia el portal ("Ruach's spiked head drove into the center of Aamon's black heart... Aamon's body went still beneath him within seconds"). Coincide exactamente con la síntesis del mapa de referencia.

Las tres referencias póstumas revisadas son consistentes entre sí y con esa escena, y en ningún momento tratan a Aamon como vivo:
- `Libro2/EN/23_A_Thiefs_Legacy.md`: Sariel reconstruye el robo a partir de las notas de Belial y lee "the sacrifice of Aamon, Marshal of the Infernal Legions" — lo trata como muerto, como una expedición de robo con sacrificio, sin contradecir el método.
- `Libro2/EN/26_Report_from_the_Abyss.md`: el informe de Sariel a Gabriel repite la misma síntesis ("sacrificed Aamon, Marshal of the Infernal Legions, to buy the final approach").
- `Libro2/EN/50_The_Unaccounted_Variable.md`: Belial recuerda a Aamon en pasado ("the theft that had cost Aamon his life to secure it"), consistente con el mismo hecho.

Nota menor de vocabulario, no una incoherencia: `Libro1/EN/13` llama a Aamon "Commander" (nivel jerárquico), mientras `Libro2/EN/23` y `/26` usan "Marshal of the Infernal Legions". Verificado contra `content/lore/personajes.md` (línea 1328): la ficha de Aamon usa exactamente ambos — "Commander / Military Master" como categoría y "Marshal of Infernal Legions" como título formal — y el mismo patrón se repite con Vepar (Commander, dirigido como "Marshal" en diálogo a lo largo del Libro III). Es terminología del propio universo, no una contradicción.

### 2. El vacío de dos libros (legión sin reasignar)

Ninguno de los tres capítulos de Libro2 revisados (`23`, `26`, `50`) menciona, insinúa o da por resuelta la situación de la legión de Aamon. Los tres se concentran en el robo de Lament y en la propia crisis de Belial; la legión huérfana simplemente no aparece como tema hasta `Libro3/EN/31_What_No_One_Came_Back_For.md`, donde Naamah encuentra un manifiesto de suministros todavía autorizado bajo "Commander Aamon" y localiza a Ronove y Dantalion en el Cinder Watch, sin mando real desde la muerte de su comandante. El vacío narrativo de dos libros se sostiene sin ninguna mención intermedia que lo contradiga.

El propio capítulo 31 da además una explicación burocrática plausible y consistente con el resto del tono de la obra (vía Gusion): una legión huérfana no se resuelve automáticamente, y nadie se tomó el trabajo de corregir el papeleo — "That's not a mistake, Duchess. That's an embarrassment nobody's found it worth the paperwork to correct." Esto cierra con solidez narrativa el hueco de dos libros en vez de dejarlo como una simple laguna sin explicar.

Los capitanes recuperados (Ronove, Dantalion) y los omitidos (Andras, que sigue su propio hilo independiente en `Libro3/EN/26`) coinciden exactamente con la ficha de personajes bajo Aamon (`content/lore/personajes.md`, líneas 1349-1509).

### 3. Caracterización y motivación de Naamah

Consistente en los tres capítulos:
- `Libro3/EN/30`: se apropia del crédito del mes de alianza Vepar-Camael sin mentir técnicamente — "I did not lie... What she offered, on top of that plain truth, was simply the shape of the telling."
- `Libro3/EN/31`: reclutamiento oportunista de una legión que "ya estaba ahí, sin que nadie la reclamara" — la misma lógica de apropiación legal-pero-no-del-todo-honesta aplicada esta vez a soldados, no a una historia.
- `Libro3/EN/32`: gestiona a Phenex y Leraje ofreciendo a cada uno una verdad parcial calibrada para no mentirles y sin embargo controlar el resultado — mismo patrón de manipulación "verdad exacta, pero nunca la verdad completa."

El motivo declarado por el mapa ("apropiación de crédito y reclutamiento oportunista") se sostiene literalmente en los tres capítulos, con el mismo registro de voz, el mismo cálculo de coste/beneficio a largo plazo, y el mismo uso del velo Neriah como herramienta de control de la escena. Los capitanes (Gusion, Phenex, Leraje) coinciden con sus fichas en `personajes.md` (Captain/Mortal Politics, Captain/Artistic Corruption, Captain/Venom Archer respectivamente) en armas y temperamento.

---

## Hallazgo secundario (no bloqueante, solo documentación — no es la prosa)

`content/lore/personajes.md`, línea 1351, nota interna del 2026-08-20, afirma: *"Aamon murió en `B1C13_EN.md`"*. La prosa aprobada mata a Aamon en el capítulo 15 (`Libro1/EN/15_The_Price_of_Truth.md`), no en el 13 (`Libro1/EN/13_The_Devils_Gambit.md`, que es solo la planificación de la traición, sin muerte). Esto no es una incoherencia de la obra — es un segundo caso, en un documento distinto, del mismo patrón de referencia interna equivocada que el propio mapa de auditoría ya documentó como Hallazgo #3 (`book3_part1_expanded_beats.md` decía erróneamente "B2C37"). La ficha de personaje de Aamon en el mismo archivo (encabezado, línea ~1325) no comete el error; solo la nota de proceso adjunta sí.

**Arreglo mínimo propuesto** (no aplicado): corregir la nota en `personajes.md` línea 1351 de `B1C13_EN.md` a `B1C15_EN.md` (o al nombre de archivo actual, `Libro1/EN/15_The_Price_of_Truth.md`).

---

## Conclusión

Sin hallazgos de incoherencia real en la prosa de los ocho capítulos auditados. La muerte de Aamon es tratada de forma consistente en todas las referencias posteriores, el vacío de reasignación de su legión se mantiene íntegro durante dos libros sin contradicción intermedia, y la caracterización de Naamah se sostiene estable en sus tres capítulos. El único punto a corregir es cosmético y vive en un documento de lore de apoyo (`personajes.md`), no en la prosa.
