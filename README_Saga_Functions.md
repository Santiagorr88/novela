# 📘 README – Funciones y Scripts Narrativos

Este repositorio contiene los scripts que orquestan la generación narrativa de la trilogía *Chronicles of the Sundering Judgment*. Cada archivo tiene una responsabilidad clara para mantener coherencia, continuidad temática, control de misterios y gestión de lore.

---

## 🧠 `memory_plan.py`

**Propósito**: Mantener memoria progresiva y generar una estructura base para cada capítulo.

- `get_rolling_memory(chapter_no: int) -> str`:  
  Devuelve una memoria acumulada con todos los resúmenes de capítulos anteriores. Útil para alimentar a la IA con el lore anterior y garantizar continuidad narrativa.

- `get_chapter_plan(chapter_no: int) -> str`:  
  Genera un esquema base con estructura dramática para el capítulo actual. Sirve como punto de partida para la IA generadora.

---

## 📝 `chapter_recap_writer.py`

**Propósito**: Registrar el resumen de cada capítulo para su uso en memoria futura.

- `write_chapter_recap(chapter_no: int, full_text: str, summary: str)`:  
  Guarda el resumen del capítulo generado en `src/chapters/recap/`, nombrado por número. Esto permite a los scripts de memoria recuperar contexto previo.

---

## 🎯 `beat_planner.py`

**Propósito**: Definir la secuencia emocional y narrativa (beats) de cada capítulo.

- `get_beats_for_chapter(chapter_no: int) -> List[str]`:  
  Devuelve una lista de beats sugeridos (tensión, revelación, decisión, giro, etc.) para el capítulo en curso.  
  Sirve como guía estructural para mantener ritmo emocional coherente a lo largo de la trilogía.

---

## 🌌 `theme_manager.py`

**Propósito**: Registrar y rastrear temas narrativos por capítulo.

- `register_themes(chapter_no: int, themes: List[str])`:  
  Añade temas clave tratados en cada capítulo a un diccionario central. Esto sirve para verificar consistencia temática global (redención, pérdida, juicio, etc.).

- `get_themes_for_chapter(chapter_no: int)`:  
  Devuelve los temas registrados para un capítulo dado.

- `get_all_registered_themes()`:  
  Devuelve un conjunto de todos los temas que han aparecido en la saga hasta ahora.

---

## 🧩 `mystery_tracker.py`

**Propósito**: Llevar un seguimiento claro de los misterios del lore y controlar cuándo se introducen o resuelven.

- `register_mystery(mystery: str, chapter_no: int)`:  
  Marca un misterio como *introducido* o *resuelto* en un capítulo específico.

- `get_open_mysteries()`:  
  Devuelve los misterios aún abiertos (sin resolver).

- `get_resolved_mysteries()`:  
  Devuelve los misterios que ya han sido resueltos por la narración.

- `get_all_mysteries()`:  
  Devuelve todos los misterios definidos.

---

## 📖 `lore_diff_tracker.py`

**Propósito**: Comparar versiones anteriores del lore con el nuevo texto generado para detectar incoherencias o cambios no intencionados.

- `detect_lore_differences(old_text: str, new_text: str)`:  
  Compara dos versiones del texto y reporta cambios clave en personajes, objetos, lugares o eventos. Útil para prevenir errores de continuidad.

---

## 🕊️ `prophecy_manager.py`

**Propósito**: Controlar la aparición de profecías dentro del texto.

- `get_available_prophecies()`:  
  Lista las profecías disponibles para ser reveladas.

- `mark_prophecy_as_used(prophecy: str, chapter_no: int)`:  
  Registra que una profecía ha sido utilizada en un capítulo determinado. Evita duplicación o adelanto prematuro.

---

## 🧠 `saga_state.py`

**Propósito**: Controlar el estado global de la saga (libro, capítulo, personajes claves activos, armas en juego, etc.)

- Guarda información como:
  - Capítulo actual
  - Estado de reencarnación de Miguel
  - Ubicación de Solmire
  - Nivel de revelación de los Olvidados

Esto permite que los generadores verifiquen si ciertos eventos son válidos o demasiado prematuros.

---

## 🌍 `prompt_universo.md`

**Propósito**: Archivo maestro que contiene el lore, reglas, jerarquías, lugares, profecías, misterios y estructura de los libros.  
Este archivo es alimentado constantemente a la IA generadora y debe mantenerse actualizado y consistente.

---

## 📦 Integración esperada (ejemplo de flujo)

1. Se llama `get_rolling_memory` + `get_chapter_plan`.
2. Se genera capítulo → Se guarda recap con `write_chapter_recap`.
3. Se registran temas (`theme_manager`) y misterios (`mystery_tracker`).
4. Se definen beats (`beat_planner`) según esquema dramático.
5. Se valida que el capítulo no contradiga lore con `lore_diff_tracker`.
6. Se actualiza `saga_state` si hay eventos clave.
7. Se valida o usa alguna profecía (`prophecy_manager`) si es necesario.
8. Todo se ajusta al marco definido en `prompt_universo.md`.


## como lanzar manualmente los capitulos y registrarlos
Cambiamos los nombres de los capitulso el cual si queremos que sea inmutable le ponemos el argumento, tambien el capitulo
luego la ruta de donde esta el capitulo.
 python manual_register.py --inmutable --chapter 1 --file src/chapters/B1C01.md

python manual_register.py -final_chapter   --inmutable   --chapter 28   --book 1   --file src/chapters/B1C28.md


para un archivo md generarlo pdf.
python src/scripts/export_pdf.py   --file src/chapters/B1C01.md   --title "B1C01 – The Tree Outside Time"   --output output/pdf/en/B1C01_The_Tree_Outside_Time.pdf