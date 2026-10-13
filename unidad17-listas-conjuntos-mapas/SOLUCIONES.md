# Soluciones razonadas del laboratorio 17

[Volver al laboratorio](LABORATORIO.md)

## Respuestas y decisiones

No en esta referencia: contrato es exacto. Set pierde repetición. Definecasefold/puntuación si objetivo loexige, sin cambiarlo tácitamente.

## Justificación del caso desarrollado

rojo azul rojo verde azul rojo→rojo 3, azul 2, verde 1.

No basta afirmar que el ejemplo funciona: relaciona cada salida con su entrada y con la regla del contrato. Cambiar el contrato puede hacer válida otra solución, pero debes declararlo antes de comparar.

## Comprobaciones adicionales

Prueba un caso pequeño que distinga tu solución de una implementación defectuosa. Para ordenamiento conserva multiplicidades y entrada; para búsqueda comprueba presencia/ausencia; para optimización compara con una referencia independiente pequeña. Cuando existan múltiples respuestas correctas, verifica sus propiedades en lugar de exigir un orden accidental.

## Complejidad defendible

Conteo O(n) esperado de tokens con hashing; ordenar k claves añade O(k log k); memoria O(k).

Una respuesta que omite validación, copias o tamaño de salida puede atribuir al programa una cota que no cumple. Consulta [las pruebas y verificación](../docs/VERIFICACION.md) para reproducir los casos revisados.
