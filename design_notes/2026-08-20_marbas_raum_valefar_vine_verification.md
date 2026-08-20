# Verificación Marbas/Raum/Valefar/Vine contra prosa real — 2026-08-20

**Alcance**: verificación de solo lectura sobre `main` (confirmado con `git branch --show-current`, sin cambio de rama). Continúa la misma disciplina que `2026-08-20_naamah_verification.md` y la auditoría nocturna del 2026-08-19: el outline no es fiable sin cotejarlo contra la prosa ya escrita, y las jerarquías de mando del encargo no se dan por buenas sin verificar la ficha directamente.

## Paso 1 — Ficha y jerarquía real (`content/lore/personajes.md`, líneas 2072-2115)

Los cuatro están fichados como **Captains bajo Belial → Foras/Vepar** (líneas 2062-2116), no bajo ningún otro Commander:

- **Marbas** — Captain / Corrupted Technology, arma *Tekrion* (implantes), personalidad "amoral scientist—mocking, ironic—believes perfection is mechanical" → **bajo Foras** (línea 2157: "Leaders under Marbas (Captain) → Foras (Commander)").
- **Raum** — Captain / Dream Invasion, arma *Lethae* (espejo), personalidad "poetic, disturbing; speaks as if he knows every finale" → **bajo Foras** (línea 2196).
- **Valefar** — Captain / Gates and Seals, arma *Oblivion* (llave), personalidad "precise, meticulous, paranoid—trusts not even Lucifer" → **bajo Vepar** (línea 2274).
- **Vine** — Captain / Beast Control, arma *Ferox* (flauta), personalidad "instinctive, savage, unpredictable" → **bajo Vepar** (línea 2313).

**Resultado de la verificación de jerarquía**: la premisa del encargo era correcta tal cual estaba formulada — no hizo falta ninguna corrección de cadena de mando (a diferencia del caso Ronove/Dantalion documentado en `personajes.md` antes de la ficha de Ronove, donde el encargo original sí asumía mal la jerarquía). Split limpio 2+2 por Commander: Marbas/Raum → Foras; Valefar/Vine → Vepar.

## Verificación de cero apariciones

```
grep -rl "Marbas\|Raum\|Valefar\|Vine" project/Chronicles_of_the_Sundering_Judgment/chapters/EN/*.md
```
→ 0 resultados para los cuatro nombres (confirmado independientemente esta sesión; coincide con el hallazgo 3 de `design_notes/2026-08-19_overnight_audit.md`, que ya había verificado lo mismo con `grep -ril` sin límites de palabra, descartando falsos positivos como "Vine" dentro de "divine").

## Verificación de outline

```
grep -n "Marbas\|Raum\|Valefar\|Vine\b" content/lore/arco_argumental_completo.md
```
→ 0 resultados. No existe material de outline específico para ninguno de los cuatro — mismo caso que Ronove/Dantalion/Phenex/Leraje y que Eshriel/Jahiel/Zaphiel: el diseño se hace desde cero contra la ficha y contra la prosa ya aprobada, no contra el outline.

## Verificación contra la prosa real de Foras/Vepar ya escrita

Leídos completos antes de diseñar nada: `B2C21pt5_EN.md` ("The Tide Remembers"), `B3C11_EN.md` ("The In-Between War"), `B3C28_EN.md` ("The Uneasy Vanguard"), `B3C28pt5_EN.md`/`pt6`/`pt7` (interludios de Naamah, misma sesión), `B3C44_EN.md` ("The New Pantheon"), y `design_notes/2026-08-19_overnight_audit.md` / `2026-08-20_naamah_verification.md` para el estado ya corregido de la contradicción de Belial.

Arco Foras/Vepar confirmado en la prosa (no en el outline, que en esta zona ya está marcado como parcialmente superado — ver Hallazgo 2 de la auditoría nocturna):

1. **B2C21.5** (Libro II): Malthus (Captain bajo Foras) muere en el cruce de caminos ante el poder imposible de un mortal. Foras encaja el golpe con frialdad calculadora; Vepar responde con un insulto cortés ("imaginative") calculado para pudrir con el tiempo, no para provocar una respuesta inmediata. Foras predice explícitamente, en su propio POV: *"The lesser captains would test him next, small provocations disguised as ordinary business, each one calibrated to see how much he'd let slide before he answered."* — esta línea es la semilla literal que ancla el interludio de Marbas/Raum (ver Paso 2).
2. **B3C11** (Libro III): Vepar y Camael, comandantes rivales de bando, se enfrentan tres veces en el campo (dos batallas normales + el vacío de Thamorak) sin hablarse nunca cara a cara — solo por pantalla.
3. **B3C28**: cuarto encuentro, primero hablado. Negocian un compromiso táctico real (escudo avanzado + incursiones de Vepar) tras chocar de doctrina. Vepar cierra con su tic ya fijado ("Acceptable. For now.").
4. **B3C28.5-28.7** (misma sesión): Naamah se apropia del crédito político del acuerdo de campo ante la corte de Lucifer, sin que Vepar se entere de lo que ha cedido. Establece que Vepar es "characteristically slower and considerably more thorough" respecto a la política de corte — le da igual, mientras la flota siga funcionando.
5. **B3C44** (post-clímax, tras la disolución de Belial en B3C40 — ver Hallazgo 2 de la auditoría, ya corregido: Belial no sobrevive degradado, su forma se disuelve): Hell queda sin Lord. Varios pretendientes marchan sobre la fortaleza vacía y fracasan, incluido **Foras**, cuyos "sermones sobre la pureza del dominio" ya no mueven a sus propios soldados. **Vepar, característicamente, se niega directamente a competir**, ocupado en su flota "y la lealtad particular que aparentemente había construido con ciertos comandantes angélicos durante las conversaciones de paz" — Asmodeus lo juzga la única respuesta de toda la corte "actually worth respecting".

**Conclusión**: el cisma entre Foras y Vepar es real, gradual y está completamente documentado en prosa ya aprobada — empieza como rivalidad de corte cortés en el Libro II (B2C21.5) y termina, en el Libro III, con Foras fracasando como pretendiente bajo la corte fragmentada de Asmodeus mientras Vepar se mantiene al margen, protegido por una alianza que ningún otro Commander de Hell se atrevería a sostener. Los cuatro capitanes fichados bajo ellos nunca han tenido que reaccionar a ninguno de estos dos momentos — es terreno limpio.

## Paso 2 — Decisión de forma

Se descarta agrupar a los cuatro en un solo interludio: Foras y Vepar tienen arcos demasiado distintos a estas alturas (uno ascendente y pragmático, el otro fracasando por dogma) como para que sus capitanes compartan una sola escena sin diluir el contraste. En su lugar, **dos interludios, cada uno anclado al Commander real de sus dos capitanes y al punto de la línea temporal donde ese Commander tiene más material ya escrito que pagar**:

### Interludio 1 — Marbas y Raum (Foras), Libro II, justo después de B2C21.5
Punto de inserción: inmediatamente después de la muerte de Malthus, dramatizando la propia predicción de Foras citada arriba — sus otros dos capitanes deciden si probar la debilidad aparente de su comandante o no. Marbas (amoral, oportunista, "perfection is mechanical") es el candidato natural para intentar la prueba; Raum (fatalista, "speaks as if he knows every finale") es el contrapeso que desaconseja. Foras responde con el mismo método frío y no-espectacular ya establecido en B2C21.5 (control demostrado, no ira visible) — el interludio funciona como el "ensayo" que confirma por qué su respuesta a Vepar, más adelante, será igual de paciente y exacta.

### Interludio 2 — Valefar y Vine (Vepar), Libro III, justo después de B3C44
Punto de inserción: en las semanas posteriores a la disolución de la fortaleza de Belial y al fracaso de Foras, cuando la alianza de Vepar con "ciertos comandantes angélicos" ya es un hecho consumado y conocido en la corte. Valefar (paranoico, "trusts not even Lucifer", su dominio entero es control de acceso) es el capitán que más tiene que objetar, en carácter, a una alianza con el enemigo histórico — la lee literalmente como una puerta sin sellar. Vine (instintivo, salvaje, impredecible) es el contrapeso que no quiere doctrina de ningún lado, solo una guerra que ya no llega. Vepar los maneja con el mismo pragmatismo frío y desinteresado de la política de corte que ya lo define — no los convence con un discurso, les da una tarea concreta que canaliza la objeción de cada uno sin negar que la alianza sigue en pie.

Ambos interludios comparten el mismo tema de fondo (un comandante gestionando el disenso de sus propios capitanes en un momento de vulnerabilidad visible), pero desde extremos opuestos del cisma — uno cuando el cisma apenas empieza (Libro II), el otro cuando ya es un hecho consumado e irreversible (Libro III, a las puertas del epílogo de la trilogía).
