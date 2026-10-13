# Soluciones razonadas del laboratorio 16

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

Vacío válido; otros inválidos. FIFO atiende A y B, deja C. Cantidad igual no garantiza anidación correcta.

## Justificación del caso desarrollado

Para ([{}]): pila vacía → '(' → '([' → '([{' → '([' → '(' → vacía. En ([)] el cierre ')' no corresponde al tope '[' y se rechaza.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

BalanceoO(n)tiempo/O(n)memoria. Cola deque permite extraer frente sin mover todos los elementos como list.pop(0).

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
