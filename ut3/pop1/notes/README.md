# UT3-POP1: Viajar es vivir

### PRUEBA OBJETIVA PRÁCTICA

![Django sticker](../../../django-sticker.png)

El objetivo de esta prueba es demostrar los conocimientos adquiridos hasta el momento en el framework de desarrollo web Django. Consiste en el desarrollo de un prototipo software para **gestionar información de vuelos**.

[Modelo entidad-relación](#modelo-entidad-relación)  
[Preparación del entorno de trabajo](#preparación-del-entorno-de-trabajo)  
[Tu tarea](#tu-tarea)  
[Entrega](#entrega)  
[Evaluación](#evaluación)

## Modelo entidad-relación

![Modelo ER](./images/erd-travel.svg)

- `departure_from` es una clave ajena a `Airport`.
- `arrival_to` es una clave ajena a `Airport`.
- `airline` es una clave ajena a `Airline`.

## Preparación del entorno de trabajo

Descargamos el proyecto:

```console
curl -L https://raw.githubusercontent.com/sdelquin/dsw/main/ut3/pop1/notes/files/travel.zip -o /tmp/travel.zip
```

Lo descomprimimos:

```console
unzip /tmp/travel.zip -d ~/travel
```

Accedemos a la carpeta del proyecto:

```console
cd ~travel
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

Debes completar los archivos necesarios (marcados con 🚩) para que el proyecto funcione igual que el proyecto de ejemplo que va a indicar el profe en clase.

### `flights/`

```
flights
├── __init__.py
├── admin.py
├── apps.py
├── management
│   └── commands
│       ├── _utils.py
│       └── populate_flights.py
├── migrations
│   ├── 0001_initial.py
│   ├── 0002_alter_flight_airline_alter_flight_code.py
│   ├── 0003_alter_flight_options_and_more.py
│   └── __init__.py
├── models.py
├── static
│   ├── css
│   │   ├── bootstrap.min.css
│   │   └── custom.css
│   ├── img
│   │   └── travel-logo.svg
│   └── js
│       ├── bootstrap.bundle.min.js
│       └── custom.js
├── templates
│   ├── base.html
│   ├── flights
│   │   └── flight
│   │       ├── detail.html 🚩
│   │       └── list.html 🚩
│   ├── header.html
│   ├── pagination.html 🚩
│   ├── search.html 🚩
│   └── breadcrumbs.html 🚩
├── tests.py
├── urls.py 🚩
└── views.py 🚩
```

### `airlines/`

```
airlines
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   ├── 0001_initial.py
│   ├── 0002_alter_airline_iata.py
│   ├── 0003_alter_airline_iata.py
│   ├── 0004_airline_slug.py
│   └── __init__.py
├── models.py
├── templates
│   └── airlines
│       └── airline
│           └── detail.html 🚩
├── tests.py
├── urls.py 🚩
└── views.py 🚩
```

### `airports/`

```
airports
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   ├── 0001_initial.py
│   ├── 0002_alter_airport_iata.py
│   ├── 0003_alter_airport_iata.py
│   ├── 0004_airport_photo.py
│   ├── 0005_airport_web.py
│   ├── 0006_remove_airport_web.py
│   ├── 0007_airport_slug.py
│   └── __init__.py
├── models.py
├── templates
│   └── airports
│       └── airport
│           └── detail.html 🚩
├── tests.py
├── urls.py 🚩
└── views.py 🚩
```

### Aclaraciones

#### Interfaz administrativa

- Las credenciales de la interfaz administrativa son:
  - Usuario: `alu`
  - Contraseña: `tranquilidad`

#### Plantillas

- Si pulsamos en "botón derecho → Ver código fuente de la página" sobre la aplicación de ejemplo tendremos el código de las plantillas.
- Uso de `easy-thumbnails` en plantillas:
  - Para listado de vuelos: `{% thumbnail <image> 0x25 autocrop %}`
  - Para detalle de aerolínea: `{% thumbnail <image> 400x0 autocrop %}`
  - Para detalle de aeropuerto: `{% thumbnail <image> 600x300 crop='smart' %}`
- La [documentación de Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) te ayudará con las plantillas.
- Ojo a `breadcrumbs.html` que se modifica con el cambio de sección y además muestra la ciudad de búsqueda si se da el caso.
- El "title" de cada página también se modifica.

#### Paginación

- [Documentación de apoyo](https://docs.djangoproject.com/en/4.2/ref/paginator/#paginator-class) para implementar la paginación (10 items por página).

#### Búsqueda

- La búsqueda tiene que [funcionar independiente de mayúsculas/minúsculas así como con partes de la palabra](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#icontains). Por ejemplo `mad` o `Madrid` deberían funcionar para el destino Madrid.
- El código Javascript de `js/custom.js` hace que se lance una petición GET con la ciudad indicada al pulsar <kbd>Enter</kbd> o bien al hacer clic en "Search".

#### Comportamiento

- La URL raíz del proyecto `/` debe redirigir al listado de vuelos.
- Al pulsar en el icono del sitio nos lleva a la URL raíz `/`.
- Si clicamos en los logos de las líneas aéreas nos lleva a su página de detalle.
- En las vistas de detalle se debe lanzar un 404 si no se encuentra el objeto en cuestión.

## Entrega

Para entregar el proyecto lo primero será comprimir los archivos con el siguiente comando:

```console
just zip
```

Esto generará un fichero `travel.zip` que será el que debas añadir a la entrega de CAMPUS.

## Evaluación

La evaluación de la prueba se realizará siguiendo la **rúbrica** preparada al efecto.
