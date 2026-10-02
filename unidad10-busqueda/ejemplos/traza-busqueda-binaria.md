# Traza — Búsqueda binaria

Datos ordenados:
```text
índice: 0  1  2   3   4   5   6
valor:  2  5  8  12  16  23  38
```

Objetivo: **23**

| Paso | izquierda | derecha | medio | valor medio | decisión |
|---:|---:|---:|---:|---:|---|
| 1 | 0 | 6 | 3 | 12 | 23 > 12 → descartar izquierda incluida mitad |
| 2 | 4 | 6 | 5 | 23 | encontrado |

Solo fueron necesarias 2 comparaciones centrales.

## Contraste
Una búsqueda lineal desde el inicio revisaría:
```text
2, 5, 8, 12, 16, 23
```

## Condición indispensable
La búsqueda binaria depende del **orden**. Aplicarla sobre datos desordenados rompe la lógica de descarte.
