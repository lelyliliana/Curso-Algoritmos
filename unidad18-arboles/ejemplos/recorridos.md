# Trazado visual — Recorridos de árbol

Árbol:
```text
        8
       / \
      3   10
     / \    \
    1   6    14
```

## Preorden
raíz → izquierda → derecha
```text
8, 3, 1, 6, 10, 14
```

## Inorden
izquierda → raíz → derecha
```text
1, 3, 6, 8, 10, 14
```

En un árbol binario de búsqueda válido, este recorrido produce los valores ordenados.

## Postorden
izquierda → derecha → raíz
```text
1, 6, 3, 14, 10, 8
```

## Pregunta
¿Por qué el orden cambia aunque el árbol sea el mismo?
