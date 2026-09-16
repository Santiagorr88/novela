#!/bin/bash
# Usage: count_muletillas.sh <dir-glob-for-chapters-01-27>
DIR="$1"
LANG="$2"

files=""
for i in $(seq -w 1 27); do
  f=$(ls ${DIR}/${i}_*.md 2>/dev/null)
  if [ -n "$f" ]; then files="$files $f"; fi
done

echo "Files counted: $(echo $files | wc -w)"

count() {
  local pattern="$1"
  local label="$2"
  local n=$(grep -oiE "$pattern" $files 2>/dev/null | wc -l)
  printf "%-35s %d\n" "$label" "$n"
}

if [ "$LANG" = "EN" ]; then
  count "something" "something"
  count "found himself|found herself|found themselves" "found himself/herself/themselves"
  count "a long moment|the moment|a moment" "moment (a/the/a long)"
  count "whatever" "whatever"
  count "the shape of" "the shape of"
  count "in a way" "in a way"
  count "the kind of" "the kind of"
  count "worth" "worth"
  count "rather than" "rather than"
  count "never once" "never once"
else
  count "del modo en que" "del modo en que"
  count "todavía" "todavia/todavía"
  count "jamás" "jamas/jamás"
  count "propio|propia|propios|propias" "propio/a(s)"
  count "a lo largo de" "a lo largo de"
  count "ninguno de los dos|ninguna de las dos" "ninguno/a de los/las dos"
  count "por primera vez" "por primera vez"
  count "de todos modos" "de todos modos"
  count "valer la pena|vale la pena|valía la pena|merece la pena|merecer la pena" "valer/merecer la pena"
  count "una especie de" "una especie de"
  count "algo parecido a" "algo parecido a"
fi
