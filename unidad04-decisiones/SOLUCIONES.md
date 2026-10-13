# Soluciones razonadas del laboratorio 04

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

El límite 10000 quedaría excluido;10009 paga 9009. Negativo se rechaza antes de aplicar regla, no se vuelve un abono.

## Justificación del caso desarrollado

9999 → sin descuento;10000 → descuento 1000, pago 9000;10001 → descuento 1000, pago 9001.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

O(1); la política de redondeo es parte del contrato.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
