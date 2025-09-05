# Secuencia de Collatz en Python

Este programa genera la **secuencia de Collatz** a partir del promedio de *N* números ingresados por teclado.

- **N** se calcula como: último dígito de tu código + 3.  
- Se piden *N* números enteros al usuario.  
- Se obtiene el promedio (redondeado).  
- Con ese promedio se construye y muestra la secuencia de Collatz hasta llegar a 1.

## Ejecución

```bash
python collatz.py
```

## Ejemplo de uso

```
Ingrese el último dígito de su código: 7
Debe ingresar 10 números enteros.
Ingrese el número 1: 4
Ingrese el número 2: 5
...
Ingrese el número 10: 8

Promedio (redondeado): 6

Secuencia de Collatz:
[6, 3, 10, 5, 16, 8, 4, 2, 1]
```