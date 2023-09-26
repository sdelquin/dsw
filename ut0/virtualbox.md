# VirtualBox

Esta sección explica cómo montar **la máquina virtual** con la que vamos a trabajar en el módulo de DSW.

## Descarga e instalación

Abrimos una terminal **desde la máquina real**:

![Open terminal](./images/open-terminal.png)

Y ejecutamos lo siguiente:

```console
curl http://amy/daw/2daw/dsw/bootstrap.sh | bash -s dsw
```

> ⚠️ Este proceso puede durar varios minutos. ¡Paciencia!

## Arranque y configuración

Ahora abrimos VirtualBox:

![Open terminal](./images/open-virtualbox.png)

Debería aparecer una nueva máquina virtual llamada **dsw**. Arrancamos esta máquina:

![Open vm](./images/open-vm.png)

En pocos segundos nos aparecerá la **ventana de login**:

![Login](./images/login-vm.png)

Accedemos al sistema con las siguientes credenciales:

- Usuario: `alu`
- Contraseña: `tranquilidad`

A continuación abrimos una terminal **desde la máquina virtual**:

![Open terminal vm](./images/open-terminal-vm.png)

Y ejecutamos lo siguiente:

```console
curl http://amy/daw/2daw/dsw/setup.sh | bash -s dsw
```

> ⚠️ Cuando nos lo solicite tendremos que poner la contraseña (ojo porque no se ve cuando la escribimos).

## Clave de acceso

Por último **modificamos la contraseña** que está por defecto para el usuario `alu` poniendo otra distinta QUE NO DEBEMOS OLVIDAR.

Para ello ejecutamos el comando `passwd`:

![passwd](./images/passwd.png)

## Pasos posteriores

1. La primera vez que entramos a la máquina virtual puede que no se vea ocupando completamente la pantalla. Esto lo resolvemos muy fácil:

![Pantalla completa](./images/full-screen.jpg)

2. Abre una terminal y lanza el siguiente comando para comprobar que tu IP se corresponde con la que debe. Ejemplo: Si tu número de PC es el 12, el comando debería dar como salida: `10.109.12.20`

```console
ip -br a | perl -nle 'print $1 if /(10.[^\/]+)/'
```

> 💡 Si la IP que saca el comando no es la que corresponda, avisa al profe.

3. No instales otra shell que no sea la que viene por defecto `bash` ya que puede afectar a las configuraciones predefinidas.
