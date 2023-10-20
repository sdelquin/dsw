# Miniproyecto

El miniproyecto a realizar será un **banco online**.

## Arranque

✨ El nombre del proyecto Django será `bank`:

```console
django-admin startproject bank .
```

## Modelo entidad-relación

![ER Banco](./images/bank.svg)

## Tipos de transacciones

Habrá 4 tipos de transacciones:

1. Compras
2. Transferencias entrantes
3. Transferencias salientes
4. Comisiones

## Estado de los objetos

Habrá 3 tipos de estados:

1. Activo.
2. Bloqueado.
3. De baja.

## Código de cuenta cliente

Nuestro CCC (Código de Cuenta Cliente) seguirá la siguiente expresión regular:

`B[1-9]:\d\d\d\d-\d\d\d\d`

`B[1-9]` indicará el banco al que hacemos referencia:

- `B1`: Banco del grupo 1.
- `B2`: Banco del grupo 2.
- `B3`: Banco del grupo 3.
- `B4`: Banco del grupo 4.
- `B5`: Banco del grupo 5.
- `B6`: Banco del grupo 6.
- `B7`: Banco del grupo 7.
- `B8`: Banco del grupo 8.

Las cuentas, dentro del mismo banco, se irán asignando de manera correlativa. Por ejemplo, para el banco `B1`:

- `B1:0000-0001`
- `B1:0000-0002`
- `B1:0000-0003`

## Transferencias

Podemos tener **transferencias entrantes** o **transferencias salientes**.

### Protocolo de transferencias

Supongamos que el banco 1 quiere enviar una transferencia al banco 2. Para ello, el banco 1 tendría que hacer una petición POST al banco 2 a través de la siguiente URL:

`http://bank2.aula109/transfer/incoming`

Con los campos:

| Campo       | Descripción                                      |
| ----------- | ------------------------------------------------ |
| `sender`    | Nombre del ordenante                             |
| `cac`       | Código de cuenta cliente (_client account code_) |
| `concept`   | Concepto                                         |
| `amount`    | Importe                                          |
| `timestamp` | Fecha y hora                                     |

Códigos de respuesta:

- Si todo ha ido bien se debe devolver un [200 OK](https://docs.djangoproject.com/en/4.2/ref/request-response/#httpresponse-objects).
- Si ha habido algún error se debe devolver un [400 Bad Request](https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpResponseBadRequest) indicando en el mensaje de error la descripción de lo sucedido.

## Compras

Sólo es posible **realizar compras usando tarjeta**.

### Protocolo de compras

Supongamos que un cliente del banco 1 compra una pachanga en el comercio "Dulces Dorado" pagando con tarjeta.

Para que "Dulces Dorado" pueda hacer el cobro tendría que hacer una petición POST a la siguiente URL:

`http://bank1.aula109/payment`

Con los campos:

| Campo       | Descripción                                    |
| ----------- | ---------------------------------------------- |
| `business`  | Comercio                                       |
| `ccc`       | Código de tarjeta cliente (_client card code_) |
| `pin`       | Código de seguridad de la tarjeta              |
| `amount`    | Importe                                        |
| `timestamp` | Fecha y hora                                   |

Códigos de respuesta:

- Si todo ha ido bien se debe devolver un [200 OK](https://docs.djangoproject.com/en/4.2/ref/request-response/#httpresponse-objects).
- Si el código de seguridad de la tarjeta no es el correcto se debe devolver un [403 Forbidden](https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpResponseForbidden).
- Si ha habido algún otro error se debe devolver un [400 Bad Request](https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpResponseBadRequest) indicando en el mensaje de error la descripción de lo sucedido.
