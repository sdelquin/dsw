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
- Utiliza el enfoque que creas que mejor se adapta al problema (versión iterativa, recursiva, orientado a objetos, ...)
- Escribe todas las funciones auxiliares que creas necesarias.
- Haz uso de cualquier librería/paquete Python que creas que te puede ayudar.
- Presta atención a la calidad del código, nomenclatura de variables y eficiencia.

## Tests

Puedes descargar [los tests](./files/test_fnbn.py) y probar tu programa con:

```console
$ pytest
```

> ⚠️ Es necesario tener el paquete pytest instalado: `pip install pytest`
