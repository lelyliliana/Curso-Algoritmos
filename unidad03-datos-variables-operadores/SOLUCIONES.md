# Soluciones razonadas del laboratorio 03

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

3599→(0,59,59);3600→(1,0,0);0→ceros;−1 rechazado. No es una hora del día.

## Justificación del caso desarrollado

3661 DIV3600=1; resto 61;61 DIV60=1; resto 1 →(1,1,1).

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

O(1) operaciones aritméticas; horas no se limita a 23 porque esto representa duración.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
