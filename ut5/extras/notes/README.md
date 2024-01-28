# Extras

En esta sección se detallan algunas **funcionalidades extra** de Django (incluyendo proyectos externos) que no se han visto hasta el momento y que pueden resultar de interés para el desarrollo de proyectos.

[Conversores personalizados en URLs](#conversores-personalizados-en-urls)  
[Crispy Forms](#crispy-forms)  
[Personalización de widgets](#personalización-de-widgets)  
[Testing en Django](#testing-en-django)  
[Django Browser Reload](#django-browser-reload)  
[Redirección lambda](#redirección-lambda)  
[Django Compressor](#django-compressor)

## Contexto

Para la explicación de las distintas funcionalidades vamos a trabajar sobre un proyecto de **gestión de eventos** denominado [Eventum](../eventum/) y desarrollado para esta sección.

![Eventum Logo](./images/eventum-logo.png)

La base de datos es muy sencilla. Vamos a trabajar con una única tabla:

![Eventum Database](./images/eventum-db.svg)

## Conversores personalizados en URLs

Django permite crear [conversores personalizados en URLs](https://docs.djangoproject.com/en/5.0/topics/http/urls/#registering-custom-path-converters) de manera que el objeto que llega a la vista ya está "convertido" al formato que queramos.

Ejemplo:

- [events/converters.py](../eventum/events/converters.py)
- [events/urls.py](../eventum/events/urls.py#L12)

## Crispy Forms

Personalizar formularios en Django no es tarea sencilla, especialmente a nivel estético. Existen varios proyectos que facilitan esta tarea.

Uno de los más destacados es [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) que tiene un [fork para Boostrap 5](https://github.com/django-crispy-forms/crispy-bootstrap5). Con este proyecto podemos renderizar un formulario con varios _backends_ CSS de manera muy rápida y sencilla.

Ejemplo:

- [requirements.txt](../eventum/requirements.txt#L3)
- [events/templates/events/add.html](../eventum/events/templates/events/add.html#L10)
- [eventum/settings.py](../eventum/eventum/settings.py#L130-L131)

## Personalización de widgets

Los formularios en Django admiten [especificar el tipo y características del widget](https://docs.djangoproject.com/en/5.0/ref/forms/widgets/) que se renderizará en la plantilla.

Una funcionalidad no tan obvia es la de convertir un _input "text"_ en un selector de fechas (_javascript_).

Ejemplo:

- [events/forms.py](../eventum/events/forms.py)

## Testing en Django

Django ofrece [potentes herramientas para realizar testing](https://docs.djangoproject.com/en/5.0/topics/testing/overview/) de nuestro código.

Existe un proyecto que proporciona estas mismas herramientas pero con las ventajas de **pytest**. Este proyecto se denomina [pytest-django](https://pytest-django.readthedocs.io/en/latest/).

Ejemplo:

- [requirements.txt](../eventum/requirements.txt#L4)
- [eventum/pytest.ini](../eventum/pytest.ini)
- [events/tests/](../eventum/tests/)

## Django Browser Reload

El hecho de tener que recargar el navegador cada vez que modificamos algo de nuestro proyecto Django puede llegar a ser una tarea pesada.

Para ayudarnos en esta tarea surge el proyecto [django-browser-reload](https://github.com/adamchainz/django-browser-reload) que detecta los cambios que realizamos en el código y recarga la página que estamos visualizando en el navegador.

Ejemplo:

- [requirements.txt](../eventum/requirements.txt#L2)
- [eventum/settings.py](../eventum/eventum/settings.py#L40)
- [eventum/urls.py](../eventum/eventum/urls.py#L25)

## Redirección lambda

Es muy habitual que en un proyecto Django tengamos que hacer una redirección de la página inicial a alguna vista de la aplicación principal.

Un ~~recurso~~ truco para realizar esta redirección es utilizar una **función lambda** directamente en el "path" de las URLs.

Ejemplo:

- [eventum/urls.py](../eventum/eventum/urls.py#L23)

## Django Compressor

Esta herramienta [Django Compressor](https://django-compressor.readthedocs.io/en/stable/) nos permite evitar la caché sobre los ficheros JS/CSS mediante una sencilla sintaxis. Hace que en producción tengamos _hashes_ en la ruta a los "assets".

Ejemplo:

- [requirements.txt](../eventum/requirements.txt#L5)
- [eventum/settings.py](../eventum/eventum/settings.py#L41)
- [events/templates/base.html](../eventum/events/templates/base.html#L12-L14)
