# Trazado visual — Arreglos e índices

Colección:
```text
índice:   0   1   2   3   4
valor:   12   7  19   7   5
```

## Recorrido para sumar
| i | datos[i] | suma antes | suma después |
|---:|---:|---:|---:|
| 0 | 12 | 0 | 12 |
| 1 | 7 | 12 | 19 |
| 2 | 19 | 19 | 38 |
| 3 | 7 | 38 | 45 |
| 4 | 5 | 45 | 50 |

## Buscar 7
La primera coincidencia está en índice 1. Si el problema pide **todas** las posiciones, detenerse allí sería incorrecto.

## Encontrar máximo
Inicializa máximo con el primer elemento:
```text
maximo ← datos[0]
```
Luego compara desde el siguiente.

## Preguntas
1. ¿Qué cambia si la lista está vacía?
2. ¿Qué significa buscar primera aparición vs. todas?
3. ¿Por qué índice y valor no son lo mismo?
