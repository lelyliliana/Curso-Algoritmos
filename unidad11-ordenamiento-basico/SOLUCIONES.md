# Soluciones razonadas del laboratorio 11

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Inversa necesita 3 desplazamientos para tamaño 3; ordenada no desplaza. Multiconjunto de salida debe coincidir, no basta estar ordenado.

## Justificación del caso desarrollado

[4,1,3,1]→[1,4,3,1]→[1,3,4,1]→[1,1,3,4].

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

Mejor O(n) con entrada ordenada; peor O(n²); copia O(n). Usar>y no≥conserva orden relativo de iguales.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
