# UT5-TNE1: Inventario

### TAREA NO EVALUABLE

![Django sticker](../../django-sticker.png)

[Objetivo](#objetivo)  
[Estructura](#estructura)  
[Esquema de la base de datos](#esquema-de-la-base-de-datos)  
[Mockups del proyecto](#mockups-del-proyecto)

## Objetivo

El objetivo de esta tarea es crear una aplicación para gestionar el **inventario tecnológico** de cualquier organización.

## Estructura

```
inventory
    inventory/
        settings.py
    stock/
        models.py
```

## Esquema de la base de datos

![Esquema BBDD](./images/inventory-db.svg)

## Mockups del proyecto

![Mockups](./images/inventory-mockups.svg)

> 💡 "Código" es el código del artículo.

## Interfaz administrativa

- Trata de trabajar lo máximo posible en la interfaz administrativa de manera que sea cómodo gestionar productos, artículos y ubicaciones.

- Para producto y artículo, si no se especifica un código al crear un nuevo objeto, este se generará de manera aleatoria como un _string_ alfanumérico de longitud 6.

- Utiliza [inlines](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#inlinemodeladmin-objects) sobre productos/artículos.
