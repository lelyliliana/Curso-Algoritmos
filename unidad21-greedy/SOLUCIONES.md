# Soluciones razonadas del laboratorio 21

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Sí porinterva los semiabiertos. Sustituir primera actividad óptima porla demenorfin no reduce elespacio disponible para las restantes. Cambio greedy falla en 6.

## Justificación del caso desarrollado

(1,2)→(2,4)→(4,6), tresactividades. Monedas[1,3,4], total 6: greedy 4+1+1 usa 3; óptimo 3+3 usa 2.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

Interva los O(n log n) por ordenación/O(n) salida. Cambioordenación O(k log k) más tamaño de salida; no prometer optimalidad universal.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
