# UT5-POP1: Comida a domicilio

### PRUEBA OBJETIVA PRÁCTICA

![Django sticker](../../../django-sticker.png)

El objetivo de esta prueba es demostrar los conocimientos adquiridos hasta el momento en el framework de desarrollo web Django. Consiste en el desarrollo de un prototipo software para **comida a domicilio** (especialidad guachinche).

[Modelo entidad-relación](#modelo-entidad-relación)  
[Preparación del entorno de trabajo](#preparación-del-entorno-de-trabajo)  
[Tu tarea](#tu-tarea)  
[Entrega](#entrega)  
[Evaluación](#evaluación)

## Modelo entidad-relación

![Modelo ER](./images/erd-guachihome.svg)

### Order

- `code` es un código de 4 letras (mayúsculas) que identifica unívocamente a cada pedido.
- `initiated_at` es un [DateTimeField](https://docs.djangoproject.com/en/5.0/ref/models/fields/#datetimefield) indicando cuándo se inició el pedido.
- `submitted_at` es un [DateTimeField](https://docs.djangoproject.com/en/5.0/ref/models/fields/#datetimefield) indicando cuándo se confirmó el pedido.
- `price` es el precio total del pedido.
- `contact` es un nombre de contacto.

### OrderLine

Hay un modelo "intermedio" `OrderLine` que vincula productos con pedidos, pero añadiendo un **campo extra** `quantity` que indica la cantidad de cada producto para un pedido en concreto.

Por ejemplo, si añadimos 2 unidades del producto con ID 9 al pedido con ID 3, tendríamos la siguiente fila en la tabla `OrderLine`:

| order_id | product_id | quantity |
| -------- | ---------- | -------- |
| 3        | 9          | 2        |

## Preparación del entorno de trabajo

Descargamos el proyecto:

```console
curl -L https://raw.githubusercontent.com/sdelquin/dsw/main/ut5/pop1/notes/files/guachihome.zip -o /tmp/guachihome.zip
```

Lo descomprimimos:

```console
unzip /tmp/guachihome.zip -d ~/guachihome
```

Accedemos a la carpeta del proyecto:

```console
cd ~/guachihome
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

| Archivo                                            | Tarea                                             |
| -------------------------------------------------- | ------------------------------------------------- |
| `guachihome/urls.py`                               | Completar `urlpatterns`                           |
| `orders/views.py`                                  | Completar la vista `add_product_to_order`         |
| `orders/signals.py`                                | Completar la señal `update_order_price_on_delete` |
| `orders/validators.py`                             | Completar el validador `validate_phone`           |
| `orders/templates/orders/submit_order_result.html` | Completar el bloque `contents` de la plantilla    |
| `orders/templates/orders/pdf.html`                 | Completar el `tbody` de la tabla en la plantilla  |
| `products/api/urls.py`                             | Completar el fichero usando _routers_             |
| `products/api/serializers.py`                      | Completar el serializador `ProductSerializer`     |
| `products/api/views.py`                            | Completar la vista `ProductViewSet`               |

> ⚠️ No debes modificar nada del resto de código proporcionado.

### API

- La API se debe implementar usando **Router** (Django Rest Framework) para generar las URLs.
- Las URLs de la API que deben funcionar son las siguientes:
  - `/api/`
  - `/api/products/`
  - `/api/products/<pk>`

### Interfaz administrativa

- La interfaz administrativa debe funcionar bajo `/admin`.
- Puedes consultar la interfaz administrativa usando las credenciales de superusuario:
  - Usuario: `admin`
  - Contraseña: `admin`

### Un pedido de ejemplo

Puedes ver un pedido de ejemplo usando [este enlace](http://sdelquin/orders/order/IIFW).

## Entrega

Para entregar el proyecto lo primero será comprimir los archivos con el siguiente comando:

```console
just zip
```

Esto generará un fichero `guachihome.zip` que será el que debas añadir a la entrega de CAMPUS.

> ⚠️ No modifiques el nombre del fichero.

## Evaluación

La evaluación de la prueba se realizará siguiendo la **rúbrica** preparada al efecto.
