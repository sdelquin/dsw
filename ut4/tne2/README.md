# UT4-TNE2: Encuestas

### TAREA NO EVALUABLE

![Django sticker](../../django-sticker.png)

[Objetivo](#objetivo)  
[Nombre del proyecto](#nombre-del-proyecto)  
[Esquema de la base de datos](#esquema-de-la-base-de-datos)  
[Aplicaciones](#aplicaciones)  
[Mockups del proyecto](#mockups-del-proyecto)

## Objetivo

El objetivo de esta tarea es crear una aplicación web para **desplegar encuestas anónimas** para analizar cualquier tipo de temática.

## Nombre del proyecto

El proyecto se debe llamar `analytika`.

## Esquema de la base de datos

![Base de datos de encuestas](./images/analytika-db.svg)

### Claves ajenas

| Tabla    | Clave ajena       |
| -------- | ----------------- |
| `Vote`   | `poll → Poll`     |
| `Vote`   | `choice → Choice` |
| `Choice` | `poll → Poll`     |

### Interfaz administrativa

Puede ser muy interesante incorporar `inlines` para las opciones de cada encuesta. [Ver aquí la documentación al respecto](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.InlineModelAdmin).

Con este mecanismo podemos tener en la misma pantalla la encuesta y sus posibles opciones. Un ejemplo de algo similar:

![Inline Django](./images/admin_with_inlines.png)

## Aplicaciones

Habrá 3 aplicaciones:

1. `polls` (con su modelo `Poll`)
2. `choices` (con su modelo `Choice`)
3. `votes` (con su modelo `Vote`)

## Mockups del proyecto

![Mockups](./images/analytika-mockups.svg)
