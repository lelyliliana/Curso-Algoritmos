# Soluciones razonadas del laboratorio 10

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

2→−1;4→3; vacío→−1. Sin precondición no se garantiza resultado. Ordenación más consultas tiene costo distinto a una sola búsqueda.

## Justificación del caso desarrollado

[1,1,3,4], x 1: lo 0/hi 4→m 2, v 3, hi 2→m 1, v 1, hi 1→m 0, v 1, hi 0; retorna 0.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

Lineal O(n), binaria O(log n), espacio O(1). Verificar orden cuesta O(n), por eso no está dentro de cada consulta.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
