# Soluciones razonadas del laboratorio 08

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Irregular se rechaza antes de recorrer como rectángulo. Para columnas necesitas conocer ancho y un acumulador por columna.

## Justificación del caso desarrollado

[[1,2],[3,4]] →fila 0:1+2=3; fila 1:3+4=7.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

O(f×c) tiempo; salida O(f). [[],[]] es rectangular con cero columnas y produce[0,0].

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
