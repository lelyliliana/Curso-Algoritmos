# Soluciones razonadas del laboratorio 25

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Duplicado requiere corregir entrada, no asignar dos cupos. Si sobra capacidadtodosse confirman. Alcancelarpromueveelprimer IDen espera, conservandounicidadyorden.

## Justificación del caso desarrollado

[S01, S02, S03, S04], capacidad 2→confirmados S01/S02, espera S03/S04. Con capacidad 0 todosesperan.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

O(n) validación/salida, O(n) espacio. Es una base funcional local, no aplicación con usuarios, persistencia oregistro web.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
