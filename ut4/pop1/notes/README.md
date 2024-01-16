# UT5-POP1: Editor Markdown

### PRUEBA OBJETIVA PRÁCTICA

![Django sticker](../../../django-sticker.png)

El objetivo de esta prueba es demostrar los conocimientos adquiridos hasta el momento en el framework de desarrollo web Django. Consiste en el desarrollo de un prototipo software para **escribir y renderizar documentos Markdown**.

[Modelo entidad-relación](#modelo-entidad-relación)  
[Preparación del entorno de trabajo](#preparación-del-entorno-de-trabajo)  
[Tu tarea](#tu-tarea)  
[Markdown](#markdown)  
[Entrega](#entrega)  
[Evaluación](#evaluación)

## Modelo entidad-relación

![Modelo ER](./images/erd-mkedit.svg)

- `ref` es una referencia **única** al documento (con formato [UUID](https://docs.djangoproject.com/en/5.0/ref/models/fields/#uuidfield)).
- `title` es el título del documento.
- `contents` es el contenido del documento.
- `created` es el _timestamp_ cuando se creó el documento.
- `updated` es el _timestamp_ cuando se actualizó el documento.

## Preparación del entorno de trabajo

Descargamos el proyecto:

```console
curl -L https://raw.githubusercontent.com/sdelquin/dsw/main/ut4/pop1/notes/files/mkedit.zip -o /tmp/mkedit.zip
```

Lo descomprimimos:

```console
unzip /tmp/mkedit.zip -d ~/mkedit
```

Accedemos a la carpeta del proyecto:

```console
cd ~/mkedit
```

Creamos el entorno virtual:

```console
just mkvenv
```

Activamos el entorno virtual:

```console
v
```

Instalamos las dependencias del proyecto:

```console
just pipi  # 😜
```

En este punto el proyecto ya debería estar preparado para empezar a trabajar. Comprueba que todo va bien ejecutando lo siguiente:

```console
$ just check
python manage.py check
System check identified no issues (0 silenced).
```

## Tu tarea

Debes completar **los archivos indicados a continuación** para que el proyecto funcione igual que el [proyecto de ejemplo](http://sdelquin) proporcionado por el profe:

- `documents/views.py`
- `documents/templates/documents/render.html`
- `documents/forms.py`

> ⚠️ No debes modificar nada del resto de código proporcionado.

## Markdown

Para pasar contenido _Markdown_ a _HTML_ usamos:

```python
import markdown

markdown.markdown(text, extensions=['extra'])
```

> 💡 Sólo es necesario renderizar el atributo `contents` del documento.

Aquí tienes un documento de ejemplo con todas las funcionalidades Markdown: http://sdelquin/documents/b4c762d7-7fb7-4812-a767-5b8cfad4d5e4/edit/

## Interfaz administrativa

Puedes consultar la interfaz administrativa usando las credenciales de superusuario:

- Usuario: `admin`
- Contraseña: `admin`

## Entrega

Para entregar el proyecto lo primero será comprimir los archivos con el siguiente comando:

```console
just zip
```

Esto generará un fichero `mkedit.zip` que será el que debas añadir a la entrega de CAMPUS.

> ⚠️ No modifiques el nombre del fichero.

## Evaluación

La evaluación de la prueba se realizará siguiendo la **rúbrica** preparada al efecto.
