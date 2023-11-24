# UT5-TE1: Banco online 2.0

### TAREA EVALUABLE

![Django sticker](../../django-sticker.png)

[Entrega de la tarea](#entrega-de-la-tarea)  
[Nuevas funcionalidades](#nuevas-funcionalidades)

## Nuevas funcionalidades

### Volcado CSV de transacciones

Se deberá implementar la descarga de transacciones de una cuenta en formato CSV desde la interfaz de usuario.

### Justificante PDF de transferencia saliente

Se deberá implementar la descarga de un justificante en PDF cuando una transferencia saliente se realice de forma satisfactoria.

### Internacionalización de la web

Se deberá internacionalizar la web del banco permitiendo elegir entre idioma español o idioma inglés.

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
3. Es suficiente con que lo suba una persona del grupo.
