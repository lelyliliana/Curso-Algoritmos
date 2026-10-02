# Problema resuelto — Máximo por divide y vencerás

Datos:
```text
[7, 2, 9, 4, 6, 1]
```

Dividir:
```text
[7,2,9]       [4,6,1]
 /   \         /   \
...            ...
```

Cada parte obtiene su máximo:
```text
max izquierda = 9
max derecha = 6
```

Combinar:
```text
max(9,6) = 9
```

## Reflexión
Este problema también puede resolverse con un recorrido lineal muy simple. Divide y vencerás no debe utilizarse solo porque sea posible: compara claridad y costo.
