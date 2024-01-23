# UT5-TNE2: ATP

### TAREA NO EVALUABLE

![Django sticker](../../django-sticker.png)

[Objetivo](#objetivo)  
[Estructura del proyecto](#estructura-del-proyecto)  
[Esquema de la base de datos](#esquema-de-la-base-de-datos)  
[Origen de datos](#origen-de-datos)  
[Puntos de entrada API](#puntos-de-entrada-api)

## Objetivo

El objetivo de esta tarea es **construir una API REST** con [Django REST Framework](https://www.django-rest-framework.org/) para datos estadísticos del circuito masculino de tenis [ATP](https://www.atptour.com/es) (Asociación de Tenistas Profesionales).

Previo a la API habrá que implementar un artefacto que nos **permita cargar los datos** estadísticos en la base de datos del proyecto.

## Estructura del proyecto

```
atp
    atp/
        ...
        settings.py
    loaders/
        ...
        views.py
    matches/
        ...
        models.py
    players/
        ...
        models.py
```

## Esquema de la base de datos

![Esquema BBDD](./images/atp-db.svg)

A tener en cuenta:

- El campo `winner` de `Match` es una clave ajena a `Player` indicando el ganador del partido.
- El campo `loser` de `Match` es una clave ajena a `Player` indicando el perdedor del partido.

## Origen de datos

Los datos provienen de [Kaggle](https://www.kaggle.com/datasets/tbrownlow3/atp-tennis?select=Stats.csv) pero se ha hecho un filtrado de los mismos con [este script en R](./datatrim.R) para dejar los ficheros preparados para su tratamiento en el proyecto, dejando únicamente datos del año 2019.

Los ficheros de datos son los siguientes:

- [matches.csv](./files/matches.csv) → estadísticas de partidos de tenis.
- [players.csv](./files/players.csv) → estadísticas de jugadores de tenis.
- [stats.csv](./files/stats.csv) → ganadores y perdedores de partidos de tenis.

Estando en la carpeta correspondiente, puedes **descargar los ficheros** con los siguientes comandos:

```console
curl -LO https://raw.githubusercontent.com/sdelquin/dsw/main/ut5/tne2/files/matches.csv
curl -LO https://raw.githubusercontent.com/sdelquin/dsw/main/ut5/tne2/files/players.csv
curl -LO https://raw.githubusercontent.com/sdelquin/dsw/main/ut5/tne2/files/stats.csv
```

### Carga de datos

Será necesario cargar los ficheros .csv en la base de datos utilizando herramientas Python y el ORM de Django.

A tener en cuenta:

- El procesamiento se realizará desde la **url** `/loaders/kaggle/`
- Esta vista sólo debe estar accesible para **usuarios administradores**.
- Habrá que implementar un **formulario con 3 campos** de tipo [FileField](https://docs.djangoproject.com/en/5.0/ref/forms/fields/#filefield) para subir los 3 ficheros de datos y procesarlos.
- Aprovecha el paquete [csv](https://docs.python.org/3/library/csv.html) de la librería estándar de Python para extraer la información de los ficheros .csv
- [Esta respuesta](https://stackoverflow.com/a/46251769) en StackOverflow te puede ayudar a procesar los ficheros subidos y tratarlos como .csv
- El fichero `stats.csv` sólo se va a usar para extraer ganador y perdedor de cada uno de los partidos.
- El campo `duration` de `players.csv` indica la duración del partido **en minutos**.

## Puntos de entrada API

Los **puntos de entrada a la API** serán los siguientes:

| Punto de entrada          | Descripción                            |
| ------------------------- | -------------------------------------- |
| `/api/players/`           | Listado de jugadores                   |
| `/api/players/pk/`        | Detalle de jugador                     |
| `/api/matches/`           | Listado de partidos                    |
| `/api/matches/pk/`        | Detalle de partido                     |
| `/api/matches/pk/winner/` | Detalle de jugador ganador de partido  |
| `/api/matches/pk/loser/`  | Detalle de jugador perdedor de partido |
