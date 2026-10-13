# Soluciones razonadas del laboratorio 12

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

<=al elegir izquierda conserva estabilidad. Pivote porposición no garantiza mediana de valores, por lo que sigue habiendo peor caso.

## Justificación del caso desarrollado

Merge:[4,1]/[3,1]→[1,4]/[1,3]→[1,1,3,4]. Quick pivote 3→[1,1]/[3]/[4]→mismo resultado.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

Merge O(n log n) y memoria O(n) adicional másstack. Quick tiempo medio O(n log n), peor O(n²); listas retenidas pueden usar O(n²) memoria en peor caso de particiones extremas.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
