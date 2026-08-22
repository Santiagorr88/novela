# Auditoría de coherencia narrativa — resumen consolidado

**Fecha**: 2026-08-22
**Alcance**: 159 capítulos, 19 agentes paralelos + 1 agente de mapeo previo.
**Método**: cada agente leyó solo su hilo/hilos asignados en orden real, con el registro de vida/muerte compartido (`2026-08-22_coherence_audit_thread_map.md`) como verdad de referencia. Ningún agente editó prosa — todo lo de abajo son propuestas, no cambios aplicados.

Informes individuales completos en `design_notes/2026-08-22_coherence_<hilo>.md` (19 archivos). Este documento es el índice priorizado.

---

## Grupo A — Contradicciones reales de prosa (algo que un lector notaría)

1. **Azael conoce a Ereloth y Thaeriel por nombre antes de la "reunión".** `Libro3/EN/14_Reading_the_Scars.md` lo muestra pensando en ambos por nombre y actividad actual, dos capítulos antes de que los tres se reencuentren "por primera vez desde el Primer Sundering" en `L3/16`. Contradice la premisa establecida de que cada uno cree ser el único superviviente.

2. **Mikel es señalado como uno de los tres Forgotten.** `Libro2/EN/43_A_Memory_of_Three.md` tiene un blocking de escena donde la atención de la figura misteriosa (Azael) se posa sobre Mikel para el rol de "suffer" de la profecía de los tres — justo lo que el fix de canon (Michael NO es uno de los Forgotten, es su aliado catalizador) dice que no debe pasar. Nunca se corrige después.

3. **Thamorak: `L3/22` contradice la escena de origen de `L3/14`/`L3/17`.** Le atribuye a Michael un rol previo de "guardián/wildcard" del ciclo respecto a Thamorak que no tenía cuando se entera de su existencia por primera vez. *(Ya corregí la imprecisión correspondiente en `prompt_universo.md`; el bug de prosa sigue sin tocar.)*

4. **El "cuarto fracaso" de Foras se cuenta dos veces de forma incompatible.** `L3/49` (POV Asmodeus) monta la escena como "tres pretendientes distintos ya fracasaron, luego un cuarto" — pero `L3/50` y `L3/51` (dos POV distintos) confirman que fue Foras solo, marchando cuatro veces, todas en la misma semana.

5. **Nael: el documento de canon contradice la prosa** (ya detectado por el mapeo previo). `personajes_muertes_reencarnaciones.md` la da por muerta en el capítulo 5 y construye una subtrama entera de reencarnación ("Nathaniel Vale") sobre esa muerte falsa. La prosa real la muestra sanada y viva.

---

## Grupo B — Promesas narrativas planteadas y nunca resueltas

6. **Corin Vasse.** Humano con don sin explicar, disputado por Vual y Sariel (`L1/26`), marcado "retomable en Libro II/III". Nunca reaparece — confirmado por grep en los 159 capítulos.

7. **La estrofa de la Necrópolis** (`L1/30`, "alguien terminará esa lectura algún día"). `L3/47_The_Final_Verse` es un objeto textual distinto (otra página, otra autoría, otro contenido) — confirmado independientemente por dos agentes distintos.

8. **La búsqueda organizada de Solmire** (Orifiel/Laila, `L2/04-05`, confirmada "sin resolver" en `L2/45`). Solmire se recupera en `L3/07` sin que esta búsqueda ni sus personajes se mencionen nunca más.

9. **El Codex Mortalis falsificado** (Agares/Vual/Nymos, `L2/47-48`). Nunca vuelve a aparecer en Libro III; el "verso real" del Codex (`L3/47`) no reconoce que una versión corrupta ya circulaba, y la intriga plantada en Lucifer sobre esa cadencia familiar nunca se retoma.

10. **El verso retenido de Raziel** (`L2/46`, `L2/49`). Raziel, Selaphiel y sus tres capitanes existen solo en esos capítulos — cero apariciones en Libro I o III, incluido el capítulo donde el Codex se completa por otra vía.

11. **Kushiel roba tropas a Camael** (`L3/11`), con amenaza explícita de "Rite of Questioned Command". Nunca hay reckoning ni consecuencia visible; las batallas posteriores de Camael no mencionan el déficit.

12. **El cierre del arco de Camael no está escrito.** El propio mapa de hilos daba esto por resuelto citando `L3/23` y `/41`, pero en `L3/49` Gabriel solo *piensa* en ofrecerle un puesto y nunca se lo dice — Camael termina la trilogía sin la escena de cierre que sí tiene Uriel en `L3/44`.

13. **La promesa de Zadkiel sobre el ciclo doblado** (`L1/54`). Confirmado huérfana: no vuelve a aparecer en Libro III, y ni siquiera Iofiel (su propia capitana), presente cuando el coste se paga en `L3/40`/`L3/47`, traza la conexión.

14. **Belial nunca recibe el informe sobre el origen de Lament que él mismo pidió** (`L1/54`: "find out what that spear was"). Se responde temáticamente en el duelo con Thaeriel (`L3/19`), pero el texto nunca reconoce que la investigación original quedó abandonada.

---

## Grupo C — Decisiones de autor, no bugs (deriva intencional posible)

15. **Atribución de roles de la profecía "Judge/Suffer/Create" cambia de personaje.** `L1/43` liga Judge→Solmire, Suffer→Lament(Thaeriel); desde `L2/43` en adelante Thaeriel pasa a codificarse como "Judgment" y "Suffer" desaparece, reemplazado por el "Balance" de Azael (que no estaba en la profecía original). Puede ser lectura-incompleta-corregida-después intencional, pero ningún capítulo lo reconoce como tal.

16. **Salto temporal sin anclar en el arco de Thaeriel/Arin.** Entre `L1/54` (Arin aún estudiante/empleado en Navarion) y `L2/02` (ya mercenario con una década de contratos) no hay puente textual, aunque es compatible con los ~9 años que separan Libro I de Libro II.

---

## Grupo D — Cosmético / redacción, arreglo de una línea

17. Frase de la quemadura de Belial (`L1/54` "would not fade" vs `L2/09` "had healed weeks ago") — leve tensión de énfasis, no contradicción dura.
18. Ubicación de Lament (`L3/46` vs `L3/52`) — ambigüedad de redacción reconciliable, no contradicción real; propuesta de una frase para eliminar la ambigüedad.
19. Cita errónea de la muerte de Aamon en `personajes.md` (línea 1351: dice B1C13, es B1C15) — error de documento de apoyo, no de prosa.

---

## Confirmado limpio (sin acción necesaria)

Colapso de Belial vs. reglas de Muerte Final · desaparición del Enforcer de Belial (ambigüedad deliberada, consistente) · muerte de Malthus · legión huérfana de Aamon · aritmética de encuentros Camael-Vepar (sí cuadra: "twice... interrupted" + "fourth") · "primer trato" de Gabriel con el Infierno (acotado correctamente a su experiencia personal) · destinos finales de Solmire y Aetheris · "desaparición" de Ereloth en Libro III Parte 2 (ya corregida) · arco completo de Thaeriel (nunca muere, memoria intacta, no cae en Thae'Zakar) · Raphael y Charon Corp · hueco de outline de Malphas (no deja rastro, seguro archivar) · cronología de conocimiento de Iofiel.

---

## Recuento

- **19 hilos auditados**, 1 sin completar aún reportado limpio en su mayoría.
- **5 contradicciones reales de prosa** (Grupo A).
- **9 promesas narrativas huérfanas** (Grupo B).
- **2 posibles derivas intencionales que necesitan confirmación de autor** (Grupo C).
- **3 arreglos cosméticos de una línea** (Grupo D).
- **~12 hilos/puntos específicos confirmados limpios**, incluidos varios que el mapeo previo daba por sospechosos.
