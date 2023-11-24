# UT4-TNE2: Encuestas

### TAREA NO EVALUABLE

![Django sticker](../../django-sticker.png)

## Objetivo

El objetivo de esta tarea es crear una aplicación web para **desplegar encuestas anónimas**.

## Esquema de la base de datos

![Base de datos de encuestas](./images/polls-db.svg)

Notas:

- Es necesario añadir un campo `choices` de tipo [ManyToManyField](https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_many/) en la tabla `Poll`.

## Mockups del proyecto

![Mockups](./images/polls-mockups.svg)
