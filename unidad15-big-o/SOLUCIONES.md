# Soluciones razonadas del laboratorio 15

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Binaria reduce intervalo a mitad. Big O es una cota, no una fórmula exacta. Encontrar primero puede ser O(1), aunque peor caso sea lineal.

## Justificación del caso desarrollado

n 8→8; n 16→16; n 32→32. No equivale a afirmar que cada máquina tarda eldoble exacto.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

Cota O(n) y tambiénΘ(n) en esta familia de casos. Ignorar constantes no permite ignorar entrada ni costo de preparación cuando forma parte del problema.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
