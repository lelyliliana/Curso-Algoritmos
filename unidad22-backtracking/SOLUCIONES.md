# Soluciones razonadas del laboratorio 22

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Soluciones(0),(1); sondos elecciones distintas. Connegativos sumaalta podría bajar después, por lo que esta poda sería incorrecta. Sinpop contaminación entre ramas.

## Justificación del caso desarrollado

[2,3,5], objetivo 5: escoger 0/1→suma 5→(0,1); deshacer; escoger 2→(2).

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

O(2^n) ramas en peor caso, más costo de salida; stack O(n). Valores repetidos son objetos distintos por índice.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
