# Soluciones razonadas del laboratorio 24

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Por ejemplo 4 usaunamoneda enambos. Enumerar combinaciones pequeñas da referenciaindependiente. Casos aprobados dan evidencia, no demostración universal.

## Justificación del caso desarrollado

Para[1,3,4],6: greedy[4,1,1], DP[3,3]. Ambos suman 6; solo uno logra mínimo 2.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

Separar ordenación, salida, DPpseudopolinómica y límites de datos. No comparar tiempo de una salida distinta sin criterio común.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
