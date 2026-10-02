# Contraejemplo — Cuando greedy falla

Sistema de monedas:
```text
1, 3, 4
```

Objetivo:
```text
6
```

## Estrategia greedy
Tomar siempre la moneda más grande posible:

```text
4 + 1 + 1 = 3 monedas
```

## Solución mejor
```text
3 + 3 = 2 monedas
```

## Conclusión
La decisión local "elige la moneda más grande" no garantiza la solución global óptima para cualquier sistema de monedas.

La corrección de una estrategia greedy debe justificarse para el problema concreto.
