# Soluciones razonadas del laboratorio 23

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Imposible→None; total 0→[]. Fibonacci clásico 0/1 difiere de las bases 1/1 de escaleras. Para 6 solución[3,3].

## Justificación del caso desarrollado

Monedas 1/3/4: dp 0..6=[0,1,2,1,1,2,2]; para 6 seleccionar 3 y volver 3→0. Escaleras 0..5=[1,1,2,3,5,8].

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

Cambio O(total×k), memoria O(total) más respuesta. Es pseudopolinómico respecto a total en bits. Escaleras O(n) operaciones y dos acumuladores; enteros crecen por bits.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
