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

Los datos se pueden descargar desde [este archivo comprimido](./files/atp-data.zip).

Contiene los siguientes ficheros:

- `Match.csv` → estadísticas de partidos de tenis.
- `Player.csv` → estadísticas de jugadores de tenis.
- `Stats.csv` → ganadores y perderos de partidos de tenis.

→ Fuente: [Kaggle](https://www.kaggle.com/datasets/tbrownlow3/atp-tennis?select=Stats.csv).

### Carga de datos

Será necesario cargar los ficheros .csv en la base de datos utilizando herramientas Python y el ORM de Django.

A tener en cuenta:

- El procesamiento se realizará desde la url `/loaders/kaggle/`
- Habrá que implementar un formulario con 3 campos de tipo [FileField](https://docs.djangoproject.com/en/5.0/ref/forms/fields/#filefield) para subir los 3 ficheros de datos y procesarlos.
- Aprovecha el paquete [csv](https://docs.python.org/3/library/csv.html) de la librería estándar de Python para extraer la información de los ficheros .csv
- [Esta respuesta](https://stackoverflow.com/a/46251769) en StackOverflow te puede ayudar a procesar los ficheros subidos y tratarlos como .csv
- El fichero `Stats.csv` sólo se va a usar para extraer ganador y perdedor de cada uno de los partidos.
- El campo `duration` de `Match` corresponde a `match_minutes` de `Match.csv`.
- El campo `birthdate` de `Player` corresponde a `birthday` de `Player.csv`.

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
