# Docker

Si queremos levantar nuestro proyecto Django en local sin necesidad de prerequisitos, podemos hacer uso de [Docker](https://www.docker.com/) y lanzar contenedores ligeros con la infraestructura necesaria.

![Docker Logo](./images/docker-logo.svg)

## Django + sqlite

Si nuestro proyecto se basa en Django junto con una base de datos sqlite3 podemos hacer uso de estos dos ficheros:

### `Dockerfile`

```docker
FROM python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
```

### `docker-compose.yaml`

```yaml
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
```

Bastaría con guardar ambos ficheros en el raíz de nuestro proyecto y ejecutar:

```console
docker compose up
```

✨ El proyecto estará disponible en: http://localhost:8000

> 💡 Es necesario tener un fichero `requirements.txt` con las dependencias Python de nuestro proyecto.

## Django + PostgreSQL

En el caso de que nuestro proyecto Django trabaje con PostgreSQL, debemos modificar el fichero `docker-compose.yaml`:

```yaml
services:
  db:
    image: postgres
    volumes:
      - ./data/db:/var/lib/postgresql/data
    environment:
      - DB_NAME=app
      - DB_USER=app
      - DB_PASSWORD=app
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    environment:
      - DB_NAME=app
      - DB_USER=app
      - DB_PASSWORD=app
    depends_on:
      - db
```

Para que este servicio funcione necesitamos que nuestra configuración de la base de datos en el `settings.py` de nuestro proyecto Django tenga la siguiente estructura:

```python
from prettyconf import config
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='app'),
        'USER': config('DB_USERNAME', default='app'),
        'PASSWORD': config('DB_PASSWORD', default='app'),
        'HOST': config('DB_HOST', default='localhost')
    }
}
```
