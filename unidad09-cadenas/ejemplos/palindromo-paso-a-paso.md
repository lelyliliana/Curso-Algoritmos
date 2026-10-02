# Problema resuelto — Palíndromo

## Problema
Determinar si un texto se lee igual de izquierda a derecha y viceversa.

## Antes de comparar
Define normalización. Para este ejemplo:
- convertir a minúsculas;
- retirar espacios.

Entrada:
```text
Anita lava la tina
```

Normalizada:
```text
anitalavalatina
```

## Estrategia
Comparar extremos:
```text
a ... a
 n . n
  i i
   ...
```

Dos índices avanzan hacia el centro.

## Pregunta importante
¿Se eliminan tildes y signos? No existe una respuesta universal: debe formar parte de la especificación.
