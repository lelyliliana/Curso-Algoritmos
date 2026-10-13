# Soluciones razonadas del laboratorio 06

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Filtrar[0,1,−2] entrega[0,−2]. Imprimir no devuelve el booleano útil para decidir. Las llamadas no comparten estado mutable.

## Justificación del caso desarrollado

Llamadas es_par(0), es_par(1), es_par(−2) →true, false, true.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

O(1) operaciones bajo tamaño fijo. La función espera entrada entera; esta lección no es un parser.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
