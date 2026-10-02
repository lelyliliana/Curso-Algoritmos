# Unidad 12 — Merge Sort, Quick Sort y comparación de algoritmos

## Propósito
Estudiar ordenamientos que utilizan estrategias más eficientes para colecciones grandes.

## Merge Sort
1. Divide la colección.
2. Ordena las partes.
3. Mezcla las partes ordenadas.

```text
[8,3,6,2]
 → [8,3] [6,2]
 → [8] [3] [6] [2]
 → [3,8] [2,6]
 → [2,3,6,8]
```

## Quick Sort
1. Selecciona un pivote.
2. Particiona elementos alrededor del pivote.
3. Repite sobre las particiones.

La elección del pivote influye en el comportamiento.

## Comparar correctamente
No basta decir que un algoritmo “es más rápido”. Debes indicar:
- tamaño de entrada;
- distribución de datos;
- métrica;
- implementación;
- número de repeticiones.

## Ejercicios
1. Traza Merge Sort.
2. Traza Quick Sort usando distintos pivotes.
3. Compara con Insertion Sort en una lista pequeña.
4. Explica memoria adicional de Merge Sort.

## Reto
Diseña una comparación reproducible entre al menos tres algoritmos de ordenamiento. Registra tamaño, comparaciones y tiempo; interpreta sin confundir una medición aislada con una regla universal.

## Qué sigue
**Unidad 13 — Recursividad**
