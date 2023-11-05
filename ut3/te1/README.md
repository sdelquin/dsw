# UT3-TE1: Banco online

### TAREA EVALUABLE

![Django sticker](../../django-sticker.png)

[Puesta en marcha](#puesta-en-marcha)  
[Modelo entidad-relación](#modelo-entidad-relación)  
[Tipos de objetos](#tipos-de-objetos)  
[Transacciones](#transacciones)  
[Comisiones](#comisiones)  
[Secciones de la web](#secciones-de-la-web)  
[Entrega de la tarea](#entrega-de-la-tarea)

## Puesta en marcha

### 🐱 Repositorio

Requisitos del repositorio GitHub del proyecto:

- El nombre será el nombre del banco (todo en minúsculas y usando guión medio si hay que separar algo). Ejemplos:
  - `yladia-bank`
  - `bankus`
  - `bank-and-roll`
  - `bankarta`
- El repositorio debe ser **privado**.
- Habrá que añadir al profe (`@sdelquin`) como colaborador para que pueda ver el código.

### 🐍 Proyecto Django

El nombre del proyecto Django será `bank`:

```console
django-admin startproject bank .
```

## Modelo entidad-relación

![ER Banco](./images/bank.svg)

> 💡 Tanto `password` como `pin` habrá que almacenarlos como un hash en la base de datos utilizando para ello el algoritmo [PBKDF2](https://docs.djangoproject.com/en/4.2/topics/auth/passwords/).

## Tipos de objetos

### Bancos

El identificador de cada banco corresponderá con el identificador del grupo (empezando en 1).

Podemos obtener la información de los bancos a través del siguiente código Python:

```python
>>> import requests

>>> url = 'https://raw.githubusercontent.com/sdelquin/dsw/main/ut3/te1/files/banks.json'
>>> response = requests.get(url)
>>> banks = response.json()
```

### Tipos de transacciones

Habrá (al menos) 4 tipos de transacciones:

1. Compras
2. Transferencias entrantes
3. Transferencias salientes
4. Comisiones

### Estado de los objetos

Habrá (al menos) 3 tipos de estados:

1. Activo.
2. Bloqueado.
3. De baja.

### Código de cuenta cliente

El código de cuenta cliente seguirá la siguiente expresión regular:

`A\d-\d\d\d\d`

Las cuentas, dentro del mismo banco, se irán asignando de manera correlativa. Por ejemplo, **para el banco 1**:

- `A1-0001`
- `A1-0002`
- `A1-0003`

> 💡 "A" viene de "Account"

### Código de tarjeta

El código de tarjeta cliente seguirá la siguiente expresión regular:

`C\d-\d\d\d\d`

Las tarjetas, dentro del mismo, se irán asignando de manera correlativa. Por ejemplo, **para el banco 1**:

- `C1-0001`
- `C1-0002`
- `C1-0003`

> 💡 "C" hace referencia a "Card"

Los **códigos PIN** de las tarjetas serán secuencias de 3 caracteres alfanuméricos (dígitos y/o letras en mayúsculas) generados aleatoriamente. Ejemplos:

- `X4B`
- `3YA`
- `99T`

> ⚠️ Recuerda almacenar estos códigos de seguridad "hasheados" en la base de datos.

## Transacciones

### Pagos

Sólo es posible **realizar pagos usando tarjeta**.

#### Protocolo de pagos

Supongamos que un cliente del banco 1 compra una pachanga en el comercio "Dulces Dorado" pagando con tarjeta.

Para que "Dulces Dorado" pueda hacer el cobro tendría que hacer una petición POST a la siguiente URL:

`http://bank1/payment`

Con los campos:

| Campo      | Descripción                                        |
| ---------- | -------------------------------------------------- |
| `business` | Comercio                                           |
| `ccc`      | Código de **tarjeta cliente** (_client card code_) |
| `pin`      | Código de seguridad de la tarjeta → **hasheado**   |
| `amount`   | Importe                                            |

Códigos de respuesta:

- Si todo ha ido bien se debe devolver un [200 OK](https://docs.djangoproject.com/en/4.2/ref/request-response/#httpresponse-objects).
- Si el código de seguridad de la tarjeta no es el correcto se debe devolver un [403 Forbidden](https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpResponseForbidden).
- Si ha habido algún otro error se debe devolver un [400 Bad Request](https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpResponseBadRequest) indicando en el mensaje de error la descripción de lo sucedido.

#### Simulando pagos

Para simular un pago debemos realizar **una petición POST** al banco.

##### Línea de comandos

Podemos simular un pago utilizando la herramienta de línea de comandos [curl](https://curl.se/).

Ejemplo de uso:

```bash
curl -X POST -d '{"business": "Dulcería Dorado", "ccc": "C1-0001", "pin": "R8K", "amount": "7"}' http://bank1/payment
```

##### Navegador

Podemos simular un pago utilizando la herramienta web [httpie.io](https://httpie.io/app)

Ejemplo de uso:

![Httpie](./images/httpie.png)

### Transferencias

Podemos tener **transferencias entrantes** o **transferencias salientes**.

#### Protocolo de transferencias

Supongamos que el banco 1 quiere enviar una transferencia al banco 2. Para ello, el banco 1 tendría que hacer una petición POST al banco 2 a través de la siguiente URL:

`http://bank2/transfer/incoming`

Con los campos:

| Campo     | Descripción                                      |
| --------- | ------------------------------------------------ |
| `sender`  | Nombre del ordenante                             |
| `cac`     | Código de cuenta cliente (_client account code_) |
| `concept` | Concepto                                         |
| `amount`  | Importe                                          |

Códigos de respuesta:

- Si todo ha ido bien se debe devolver un [200 OK](https://docs.djangoproject.com/en/4.2/ref/request-response/#httpresponse-objects).
- Si ha habido algún error se debe devolver un [400 Bad Request](https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpResponseBadRequest) indicando en el mensaje de error la descripción de lo sucedido.

#### Nómina

Dado que **debe haber ingresos** en la cuenta para que sea sostenible, podemos simular el ingreso de la nómina utilizando una transferencia.

Para ello realizamos una petición POST de tipo transferencia del mismo modo que hicimos para [simular pagos](#simulando-pagos).

## Comisiones

Habrá que aplicar (al menos) las siguientes comisiones:

|                  | $[0€-50€)$ | $[50€-500€)$ | $≥500€$ |
| ---------------- | ---------- | ------------ | ------- |
| Transf. saliente | 2%         | 4%           | 6%      |
| Transf. entrante | 1%         | 2%           | 3%      |
| Pagos            | 3%         | 5%           | 7%      |

## Secciones de la web

Habrá que implementar (al menos) las siguientes secciones de la web:

- Registro.
- Login.
- Edición del perfil.
- Solicitud/Gestión de cuentas cliente.
- Solicitud/Gestión de tarjetas.
- Solicitud/Gestión de transferencias.
- Visualización de movimientos (transacciones).
- Procesamiento de pagos.

## Entrega de la tarea

- Se habilitará una entrega en el **Campus Virtual** donde se tendrá que subir únicamente **la URL al proyecto incluyendo el commit específico**.

- Para ello basta con acceder en GitHub a la carpeta donde se encuentre el proyecto:

  → `https://github.com/alu/bank`

  , y pulsar la tecla <kbd>y</kbd> para que la URL se nos convierta en un formato tipo:

  → `https://github.com/alu/bank/tree/ffaabb62206fa0c0f350dfe0a4ba370ed00b9218`

  > 💡 La parte de la url que consta de 40 caracteres es el **hash del commit** y lo identifica de manera unívoca: `ffaabb62206fa0c0f350dfe0a4ba370ed00b9218`

- Por lo tanto, **lo único que hay que subir es la URL que incluye dicho hash**.
- Es suficiente con que lo suba una persona del grupo.

- El proyecto deberá estar funcional en las URLs de cada banco (red interna del departamento).
