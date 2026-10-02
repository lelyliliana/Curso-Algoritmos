# Trazas comparativas — Ordenamientos básicos

Entrada:
```text
[5, 2, 4, 1]
```

## Bubble Sort
Pasada 1:
```text
[2,5,4,1] → [2,4,5,1] → [2,4,1,5]
```
El mayor queda al final.

Pasada 2:
```text
[2,4,1,5] → [2,1,4,5]
```

Pasada 3:
```text
[1,2,4,5]
```

## Selection Sort
Busca el menor del segmento pendiente.

```text
[5,2,4,1]
 → elegir 1 → [1,2,4,5]
```
En este caso particular el primer intercambio deja el resto ordenado, aunque el algoritmo todavía realiza sus comprobaciones.

## Insertion Sort
Construye prefijo ordenado:
```text
[5]
[2,5]
[2,4,5]
[1,2,4,5]
```

## Reflexión
La salida es igual. El proceso y el costo no.
