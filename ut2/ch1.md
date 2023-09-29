# UT2: Construyendo un blog

➡️ **CAPÍTULO 1: CONSTRUYENDO UN BLOG**

## Carpeta de trabajo

Crear una carpeta para el proyecto:

```console
$ take mysite
```

> 💡 `take` es un alias para `mkdir` + `cd`

## Entorno virtual

Crear el entorno virtual correspondiente:

```console
~/mysite$ python -m venv .venv --prompt mysite
```

Activar el entorno virtual:

```console
~/mysite$ source .venv/bin/activate
```

> 💡 El alias `v` permite activar el entorno virtual.

Desactivar el entorno virtual:

```console
(mysite) ~/mysite$ deactivate
```

> 💡 El alias `d` permite desactivar el entorno virtual.

🚨 **IMPORTANTE**: El entorno virtual `.venv` se debe ignorar para control de versiones, así que hay que incluirlo en el fichero `.gitignore`

✨ [Creación de entornos virtuales](https://docs.python.org/es/3/library/venv.html)

## Django

Instalar Django:

```console
(mysite) ~/mysite$ pip install django
```

Comprobar la versión de Django instalada:

```console
(mysite) ~/mysite$ python -m django --version
```

Crear el proyecto:

```console
(mysite) ~/mysite$ django-admin startproject mysite .
```

> ⚠️ Ojo con el punto del final para indicar que se cree en la carpeta de trabajo actual.

## Justfile

El fichero `justfile` (sin extensión) suele vivir en el raíz de nuestro proyecto.

```makefile
runserver:
    python manage.py runserver

migrate:
    python manage.py migrate

startapp app:
    python manage.py startapp {{ app }}
```

Podemos lanzar una "receta" (_recipe_) con:

```console
(mysite) ~/mysite$ just migrate
```

> 💡 ¡Funciona el autocompletado!

Podemos listar las recetas con:

```console
(mysite) ~/mysite$ just -l
runserver
migrate
startapp app
```

✨ [Documentación de just](https://just.systems/man/en/)

## Base de datos

La base de datos por defecto de un proyecto Django es `db.sqlite3`.

🚨 **IMPORTANTE**: La base de datos `db.sqlite3` se debe ignorar para control de versiones, así que hay que incluirla en el fichero `.gitignore`

## Requerimientos

Es una buena práctica crear un fichero `requirements.txt` en el raíz del proyecto con todas las dependencias que tiene nuestro proyecto. En este caso sólo tenemos Django, así que el fichero sólo tendría 1 línea con el contenido `django`.

## Referencias Django

- [Explicación de los ajustes de proyecto](https://docs.djangoproject.com/en/4.2/topics/settings/)
- [Tipos de campos para modelos](https://docs.djangoproject.com/en/4.2/ref/models/fields/)
