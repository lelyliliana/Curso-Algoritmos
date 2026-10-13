# Soluciones razonadas del laboratorio 13

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

fact 3=6, fact 0=1; negativo y>200 se rechazan. Iteración puede evitar stack recursivo, pero no elimina tamaño del resultado.

## Justificación del caso desarrollado

fact 5→5×fact 4→5×4×3×2×fact 1→120. fact 0=1.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

O(n) llamadas y O(n) stack; el costo de enteros grandes crece con sus bits. No se declara tiempo constante por multiplicación arbitraria.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
