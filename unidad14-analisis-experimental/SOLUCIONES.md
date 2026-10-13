# Soluciones razonadas del laboratorio 14

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Ausente produce 16/32. Usa reloj apropiado, varias repeticiones y condiciones comparables. Una medida aislada no determina crecimiento asintótico.

## Justificación del caso desarrollado

n 8: objetivo 0→1 comparación; objetivo 99→8. El peor caso está ausente oal final.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

O(n) comparaciones en peor caso. El script reporta conteos, no un benchmark de velocidad entre lenguajes.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
