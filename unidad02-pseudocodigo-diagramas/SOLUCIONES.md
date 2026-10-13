# Soluciones razonadas del laboratorio 02

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

−3 impar,0/4 pares. Texto requiere interpretación y validación antes del cálculo; una comparación no transforma automáticamente una cadena.

## Justificación del caso desarrollado

n 7:7 MOD2=1 → impar. n 0:0 MOD2=0 → par. n−2: resto 0 → par.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

O(1) bajo modelo de enteros de tamaño fijo; enteros arbitrarios tienen costo por bits.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
