# Mayor producto de la serie

Vamos a **desengrasar los conocimientos de Python** con el siguiente ejercicio.

Dada una **secuencia de caracteres** y un valor entero que representa el **tamaño de la serie**, se pide obtener el valor del mayor producto resultante de dividir la secuencia de caracteres en el tamaño de la serie con cálculos sucesivos.

Con un ejemplo se entenderá mejor:

| Secuencia | Tam. serie |
| --------- | ---------- |
| "63915"   | 3          |

$639 = 6\cdot3\cdot9=162$  
$391 = 3\cdot9\cdot1=27$  
$915 = 9\cdot1\cdot5=45$

Resultado final: **162**

## Función principal

La _signatura_ de la **función principal** debe ser la siguiente:

```python
def max_product(sequence: str, span: int) -> int:
    ...
```

## Control de errores

Hay que controlar tres posibles errores. Para cada uno de ellos se deberá elevar una excepción de tipo `ValueError` _(con un mensaje descriptivo)_:

- El tamaño de la serie es mayor que la longitud de la secuencia.
- El tamaño de la serie es un número negativo.
- La secuencia incluye caracteres no numéricos.

## Notas

- El fichero se debe llamar `max_product.py`
- Utiliza el enfoque que creas que mejor se adapta al problema (versión iterativa, recursiva, orientado a objetos, ...)
- Escribe todas las funciones auxiliares que creas necesarias.
- Presta atención a la calidad del código, nomenclatura de variables y eficiencia.

## Tests

Puedes descargar [los tests](./files/test_max_product.py) y probar tu programa con:

```console
$ pytest
```

> ⚠️ Es necesario tener el paquete pytest instalado: `pip install pytest`
