# Trazado — BFS y DFS

Grafo:
```text
A — B — D
|   |
C — E
```

Una lista de adyacencia posible:
```text
A: B, C
B: A, D, E
C: A, E
D: B
E: B, C
```

> El orden exacto puede variar según el orden en que se almacenen los vecinos.

## BFS desde A
Usa cola.

```text
visitar A
encolar B,C
visitar B → descubrir D,E
visitar C
visitar D
visitar E
```

Un orden posible:
```text
A, B, C, D, E
```

## DFS desde A
Profundiza antes de retroceder.

Un orden posible:
```text
A, B, D, E, C
```

## Idea clave
BFS y DFS recorren el mismo grafo con estrategias diferentes.
