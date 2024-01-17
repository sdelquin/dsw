# Mayor número siguiente

Vamos a **seguir desengrasando los conocimientos de Python** con el siguiente ejercicio.

Dado un número entero positivo _n_ calcula el mayor número siguiente a _n_ reordenando los dígitos de _n_.

Con un ejemplo se entenderá mejor:

| _n_  | Mayor número siguiente |
| ---- | ---------------------- |
| 2017 | 2071                   |

## Función principal

La _signatura_ de la **función principal** debe ser la siguiente:

```python
def find_next_bigger_number(n: int) -> int:
    ...
```

## Control de errores

En el caso de que los dígitos no puedan ser reordenados para obtener un número mayor, el resultado debe ser -1.

| _n_ | Mayor número siguiente |
| --- | ---------------------- |
| 531 | -1                     |

## Notas

- El fichero se debe llamar `fnbn.py`
- Haz uso de cualquier librería/paquete Python que creas que te puede ayudar. Es posible que [itertools](https://docs.python.org/3/library/itertools.html) tenga lo que estás buscando 😜.
- Utiliza el enfoque que creas que mejor se adapta al problema (versión iterativa, recursiva, orientado a objetos, ...)
- Escribe todas las funciones auxiliares que creas necesarias.
- Presta atención a la calidad del código, nomenclatura de variables y eficiencia.

## Tests

1. Abre una terminal y accede a la carpeta donde tengas tu solución.

2. Ejecuta lo siguiente para descargar los tests:

```console
curl -LO https://raw.githubusercontent.com/sdelquin/dsw/main/ut0/files/test_fnbn.py
```

3. Lanza los tests mediante el siguiente comando:

```console
pytest
```

> ⚠️ Es necesario tener el paquete pytest instalado: `pip install pytest`
