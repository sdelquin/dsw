# VirtualBox

Abrimos una terminal **desde la máquina real**:

![Open terminal](./images/open-terminal.png)

Y ejecutamos lo siguiente:

```console
curl http://amy/daw/2daw/dsw/bootstrap.sh | bash -s dsw
```

> ⚠️ Este proceso puede durar varios minutos. ¡Paciencia!

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

Por último **modificamos la contraseña** que está por defecto para el usuario `alu` poniendo otra distinta QUE NO DEBEMOS OLVIDAR:

```console
passwd
```

![passwd](./images/passwd.png)
