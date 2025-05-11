# https://github.com/maaslalani/slides
# CTRL-E para ejecutar el trozo de código
@intro:
    truncate -s 0 ut0/intro_done.dat
    cd ut0 && slides intro.md

# Limpiar todas las pruebas de git
[confirm('¿Limpiar todas las pruebas de git? [y/n]')]
clear:
    #!/usr/bin/env bash
    for dir in ./ut*/pop* ./ut*/tep* ./ut*/tei* ./ut*/tne*; do
      if [ -d "$dir" ]; then
        git rm -r --cached "$dir"
      fi
    done    

# Resetear el repositorio
# https://stackoverflow.com/a/26000395
[confirm('¿Borrar todo el historial de git? [y/n]')]
reset:
    #!/usr/bin/env bash
    git checkout --orphan latest_branch
    git add -A
    git commit -am "New school year"
    git branch -D main
    git branch -m main
    git push --set-upstream -f origin main

# Renderizar (y expandir) el howto para todas las POP
expand-howto:
    uv run python management/howto.py
