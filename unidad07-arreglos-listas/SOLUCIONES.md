# Soluciones razonadas del laboratorio 07

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Son dos datos, aunque valores iguales. Posiciones 1/3 en lista original; un elemento produce mínimo=máximo=ese valor.

## Justificación del caso desarrollado

[4,1,3,1] tiene cantidad 4, suma 9, mínimo 1, máximo 4; ambos 1 cuentan.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

O(n) tiempo y O(1) resumen. Conservar datos no implica copiar toda lista si solo se lee.

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
