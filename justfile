# https://github.com/maaslalani/slides
# CTRL-E para ejecutar el trozo de código
@intro:
    truncate -s 0 ut0/intro_done.dat
    cd ut0 && slides intro.md

# Renderizar (y expandir) el howto para todas las POP
expand-howto:
    python management/howto.py
