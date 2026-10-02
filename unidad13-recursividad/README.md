# Unidad 13 — Recursividad

## Propósito
Comprender problemas que pueden definirse en términos de versiones más pequeñas de sí mismos.

Una solución recursiva necesita:
- caso base;
- reducción hacia el caso base;
- llamada recursiva.

## Factorial
```text
FUNCION factorial(n)
  SI n <= 1
    RETORNAR 1
  FIN SI
  RETORNAR n * factorial(n-1)
FIN FUNCION
```

Para factorial(4):
```text
4 * factorial(3)
4 * 3 * factorial(2)
4 * 3 * 2 * factorial(1)
4 * 3 * 2 * 1
```

## Pila de llamadas
Cada llamada pendiente necesita conservar su contexto. La recursividad tiene costo de memoria y puede desbordar la pila si no converge.

## Recursivo no significa automáticamente mejor
Compara claridad, costo y profundidad con una alternativa iterativa.

## Ejercicios
1. Suma 1..N.
2. Potencia.
3. Contar dígitos.
4. Invertir texto.
5. Búsqueda binaria recursiva.

## Reto
Resuelve un mismo problema de forma iterativa y recursiva. Traza ambas versiones y compara claridad, operaciones y memoria conceptual.

## Qué sigue
**Unidad 14 — Tiempo, memoria y análisis experimental**
