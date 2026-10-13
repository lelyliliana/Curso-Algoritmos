# Soluciones razonadas del laboratorio 09

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

"a, b, a" sí;"ab" no; vacío sí por contrato. casefold cambia mayúsculas, no elimina el acento;Á no se convierte en A sin otra normalización.

## Justificación del caso desarrollado

Anita lava la tina →anitalavalatina →igual a reverso. Cadena solo espacios normaliza a vacía.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

O(n) tiempo y O(n) espacio por normalización/reverso. Esta implementación no es comparación in-place.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
