# Instrucciones para el desarrollo de las POP

## Antes de empezar

- Trabaja en la carpeta adecuada:

```console
mkdir -p ~/dsw/{{ ut }}/{{ pop }} && cd ~/dsw/{{ ut }}/{{ pop }}
```

- Mira el ejercicio del examen y crea la estructura del proyecto:

```console
pypas get <ejercicio>
```

- Abre _Visual Studio Code_ para empezar a trabajar:

```console
code .
```

## Durante la prueba

- Sólo puedes consultar la documentación de [aprendepython.es](https://aprendepython.es) y [djangoproject.com](https://docs.djangoproject.com).
- Utiliza únicamente recursos que hayamos visto en clase hasta el momento.
- Puedes mostrar la descripción del ejercicio con `pypas doc`
- Puedes comprobar tu ejercicio contra los casos de prueba con `pypas test`

## Al finalizar

- Crea un fichero `.zip` con el contenido del ejercicio:

```console
cd ~/dsw/{{ ut }}/{{ pop }} && pypas zip'
```

- Abre un navegador **en la máquina virtual** y accede a la entrega de la actividad **en el aula virtual de Desarrollo web en entorno servidor**.
- Sube únicamente el fichero comprimido `.zip` creado anteriormente.

## Evaluación

- La puntuación final de la prueba estará en función del **número de tests** que se hayan superado.
- Podrá haber penalizaciones por **copia** o **calidad del código**.