# Soluciones razonadas del laboratorio 18

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Vacío→[]. Con 9 sale[9,2,3], no ordenado. Unacumulador evita copias deconcatenación y logra O(n) en el recorrido.

## Justificación del caso desarrollado

Raíz 2 con hijos 1/3: visita 1→2→3. En un árbol general inorder no garantiza lista ordenada.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

Recorrido O(n) conceptualmente; esta versión concatena listas y puede costar O(n²) en árbol muy sesgado. Resultado O(n), stack O(h).

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
