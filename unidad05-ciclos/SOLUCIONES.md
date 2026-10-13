# Soluciones razonadas del laboratorio 05

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

[-5,-2] tiene máximo−2; vacío devuelve None para extremos. Un 0 artificial no pertenece a la lista.

## Justificación del caso desarrollado

[4,−2,7,0]: suma 4→2→9→9; cantidad 4, mínimo−2, máximo 7.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

O(n); resumen devuelve tamaño constante. max/min/sum son recorridos separados en esta referencia.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
