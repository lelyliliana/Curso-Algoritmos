# Visualización conceptual del crecimiento

La tabla no representa segundos. Muestra valores de funciones para observar su crecimiento.

| n | 1 | log₂(n) aprox. | n | n log₂(n) | n² |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 | 0 | 1 |
| 10 | 1 | 3.3 | 10 | 33 | 100 |
| 100 | 1 | 6.6 | 100 | 664 | 10 000 |
| 1 000 | 1 | 10 | 1 000 | 10 000 | 1 000 000 |

## Qué observar
Al multiplicar n por 10:
- O(1) permanece;
- O(log n) crece lentamente;
- O(n) se multiplica por 10;
- O(n²) aproximadamente por 100.

## No confundir
Big O no predice el tiempo exacto. Dos algoritmos O(n) pueden tener constantes muy distintas.
