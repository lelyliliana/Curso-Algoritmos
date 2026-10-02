# Trazas — Merge Sort y Quick Sort

Entrada:
```text
[8, 3, 6, 2]
```

## Merge Sort
División:
```text
[8,3,6,2]
   /     \
[8,3]   [6,2]
 / \     / \
[8][3]  [6][2]
```

Combinación:
```text
[8] + [3] → [3,8]
[6] + [2] → [2,6]
[3,8] + [2,6] → [2,3,6,8]
```

## Quick Sort
Si usamos 6 como pivote:
```text
menores: [3,2]
pivote:  [6]
mayores: [8]
```
Luego se resuelve la partición [3,2].

## Pregunta
¿Qué ocurre si la elección de pivote produce particiones muy desequilibradas repetidamente?
