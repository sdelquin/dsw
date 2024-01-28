# Extras

En esta sección se detallan algunas funcionalidades extra de Django que no se han visto hasta el momento y que pueden resultar de interés para el desarrollo de proyectos.

[Conversores personalizados en URLs](#conversores-personalizados-en-urls)  
[Crispy Forms](#crispy-forms)  
[Personalización de widgets](#personalización-de-widgets)  
[Testing en Django](#testing-en-django)

## Contexto

Para la explicación de las distintas funcionalidades vamos a trabajar sobre un proyecto de gestión de eventos **Eventum** con una única tabla:

![Eventum Database](./images/db-eventum.svg)

## Conversores personalizados en URLs

Django permite crear [conversores personalizados en URLs](https://docs.djangoproject.com/en/5.0/topics/http/urls/#registering-custom-path-converters) de manera que el objeto que llega a la vista ya está "convertido" al formato que queramos.

Ejemplo:

- [events/converters.py](../eventum/events/converters.py)
- [events/urls.py](../eventum/events/urls.py)

## Crispy Forms

Personalizar formularios en Django no es tarea sencilla, especialmente a nivel estético. Existen varios proyectos que facilitan esta tarea.

Uno de los más destacados es [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) que tiene un [fork para Boostrap 5](https://github.com/django-crispy-forms/crispy-bootstrap5). Con este proyecto podemos renderizar un formulario con varios _backends_ CSS de manera muy rápida y sencilla.

Ejemplo:

- [events/templates/events/add.html](../eventum/events/templates/events/add.html)
- [eventum/settings.py](../eventum/eventum/settings.py)

## Personalización de widgets

Los formularios en Django admiten [especificar el tipo y características del widget](https://docs.djangoproject.com/en/5.0/ref/forms/widgets/) que se renderizará en la plantilla.

Una funcionalidad no tan obvia es la de convertir un _input "text"_ en un selector de fechas (_javascript_).

Ejemplo:

- [events/forms.py](../eventum/events/forms.py)

## Testing en Django

Django ofrece [potentes herramientas para realizar testing](https://docs.djangoproject.com/en/5.0/topics/testing/overview/) de nuestro código.

Existe un proyecto que proporciona estas mismas herramientas pero con las ventajas de **pytest**. Este proyecto se denomina [pytest-django](https://pytest-django.readthedocs.io/en/latest/).

Ejemplo:

- [events/tests/](../eventum/tests/)
- [eventum/settings.py](../eventum/eventum/settings.py)
- [eventum/pytest.ini](../eventum/pytest.ini)
