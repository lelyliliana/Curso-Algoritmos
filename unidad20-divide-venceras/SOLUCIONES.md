# Soluciones razonadas del laboratorio 20

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Vacío se rechaza; no exige orden. Cuatro hojas necesitan 3 combinaciones, sin costos por copiar listas.

## Justificación del caso desarrollado

[-5,-2]/[-9,-1]→max−2/max−1→−1.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

T(n)=2T(n/2)+O(1)→O(n); stack O(log n). No mejora cota temporal de un recorrido lineal; enseña estrategia.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
