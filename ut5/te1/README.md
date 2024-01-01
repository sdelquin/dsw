# UT5-TE1: Banco online 2.0

### TAREA EVALUABLE

![Django sticker](../../django-sticker.png)

[Nuevas funcionalidades](#nuevas-funcionalidades)  
[Entrega de la tarea](#entrega-de-la-tarea)

## Nuevas funcionalidades

### Volcado CSV de transacciones

Se deberá implementar la descarga de transacciones de una cuenta en formato CSV desde la interfaz de usuario.

### Justificante PDF de transferencia saliente

Se deberá implementar la descarga de un justificante en PDF cuando una transferencia saliente se realice de forma satisfactoria.

### Internacionalización de la web

Se deberá internacionalizar la web del banco permitiendo elegir entre idioma español o idioma inglés.

### API

Se deberá implementar una API REST con los siguientes puntos de entrada:

| Ruta                      | Descripción                                          |
| ------------------------- | ---------------------------------------------------- |
| `/api/accounts/`          | Listado de cuentas _(del cliente autenticado)_       |
| `/api/accounts/<pk>/`     | Detalle de cuenta                                    |
| `/api/transactions/`      | Listado de transacciones _(del cliente autenticado)_ |
| `/api/transactions/<pk>/` | Detalle de transacción                               |
| `/api/cards/`             | Listado de tarjetas _(del cliente autenticado)_      |
| `/api/cards/<pk>/`        | Detalle de tarjeta                                   |

Notas:

- Sólo podrá acceder cada cliente a sus datos bancarios a través de la API previa autenticación.
- Todos los accesos serán únicamente a través de método GET.
- El formato de respuesta de todas las rutas será `json`.

## Entrega de la tarea

### Recetas

Incluir un fichero [justfile](../../ut0/justfile) con (al menos) las siguientes recetas:

- `dockup`
- `clean`
- `zip`

### Docker

1. Incluir los requerimientos del proyecto en `requirements.txt`.
2. Incluir los ficheros `Dockerfile` y `docker-compose.yaml` según [las indicaciones correspondientes](../../ut0/docker.md).

### Instrucciones de subida

1. Comprimir el proyecto con: `just zip`
2. Se habilitará una entrega en el **Campus Virtual** donde se tendrá que subir el proyecto comprimido.
3. Incluir en el texto de entrada de la entrega las **credenciales de administración y de usuario "habitual"**.
4. Es suficiente con que lo suba una persona del grupo.
