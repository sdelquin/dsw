# UT5-POP2: Mis lugares favoritos

### PRUEBA OBJETIVA PRÁCTICA

![Django sticker](../../../django-sticker.png)

El objetivo de esta prueba es demostrar los conocimientos adquiridos hasta el momento en el framework de desarrollo web Django. Consiste en el desarrollo de un prototipo software para **guardar lugares favoritos**.

[Modelo entidad-relación](#modelo-entidad-relación)  
[Preparación del entorno de trabajo](#preparación-del-entorno-de-trabajo)  
[Tu tarea](#tu-tarea)  
[Entrega](#entrega)  
[Evaluación](#evaluación)

## Modelo entidad-relación

![Modelo ER](./images/erd-favplaces.svg)

## Preparación del entorno de trabajo

Descargamos el proyecto:

```console
curl -L https://raw.githubusercontent.com/sdelquin/dsw/main/ut5/pop2/notes/files/favplaces.zip -o /tmp/favplaces.zip
```

Lo descomprimimos:

```console
unzip /tmp/favplaces.zip -d ~/favplaces
```

Accedemos a la carpeta del proyecto:

```console
cd ~/favplaces
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

Debes completar las etiquetas `# TODO` en **los archivos indicados a continuación** para que el proyecto funcione igual que el [proyecto de ejemplo](http://sdelquin) proporcionado por el profe:

- `favplaces.urls`
- `places.models`
- `places.forms`
- `places.views`
- `templates/places/detail.html`

> ⚠️ No debes modificar nada del resto de código proporcionado.

### Interfaz administrativa

- La interfaz administrativa debe funcionar bajo `/admin`.
- Puedes consultar la interfaz administrativa usando las credenciales de superusuario:
  - Usuario: `admin`
  - Contraseña: `admin`

## Entrega

Para entregar el proyecto lo primero será comprimir los archivos con el siguiente comando:

```console
just zip
```

Esto generará un fichero `favplaces.zip` que será el que debas añadir a la entrega de CAMPUS.

> ⚠️ No modifiques el nombre del fichero.

## Evaluación

La evaluación de la prueba se realizará siguiendo la **rúbrica** preparada al efecto.
