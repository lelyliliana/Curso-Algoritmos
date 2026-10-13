# Soluciones razonadas del laboratorio 19

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Ciclo no repite A; E→None; no compara pesos. Puede haber varias rutas deigual longitud, la lista de vecinos determina una.

## Justificación del caso desarrollado

A vecinos B/C→dist 1; B descubre D→dist 2; C ya encuentra D marcado. E no alcanzado no aparece. Ruta D: A→B→D.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

BFSO(V+E), memoria O(V), incluida validación previa. No resuelve mínimos pesos con aristas ponderadas.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
