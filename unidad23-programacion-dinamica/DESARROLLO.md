# Programación dinámica: definir estados y reconstruir la respuesta

[Laboratorio y programas](LABORATORIO.md) · [Soluciones](SOLUCIONES.md)

## El problema que greedy no resolvió

Monedas 1,3,4; cantidad ilimitada; monto 6; objetivo mínimo número de monedas. Greedy devuelve 4+1+1. Queremos una solución que garantice el mínimo bajo el contrato, incluso cuando tomar la mayor moneda no sea la decisión correcta.

La idea central es resolver montos menores y reutilizar sus mejores respuestas. No estamos guardando cualquier resultado intermedio: definimos con precisión qué significa cada estado.

## Estado y transición

`dp[s]` es el mínimo número de monedas necesario para entregar exactamente s. El estado 0 tiene valor 0: no entregar dinero requiere cero monedas.

Para terminar una solución del monto s podemos escoger su última moneda m. Antes de esa moneda necesitamos una solución válida del monto s−m. Eso genera la recurrencia:

```text
dp[0] = 0
dp[s] = mínimo(dp[s-m]+1)
        entre monedas m≤s con estado s-m alcanzable
```

Si ninguna alternativa puede formar s, el estado es imposible. No lo confundas con 0 monedas: eso significaría que el monto se cubrió sin pagar.

La implementación utiliza total+1 como marcador, porque cualquier solución con monedas enteras positivas usa a lo sumo total monedas. El marcador no es una cantidad de monedas válida.

## Construir la tabla

| Monto s | Candidatos alcanzables | Mínimo | Moneda previa |
|---:|---|---:|---:|
|0|caso base|0|ninguna|
|1|dp[0]+1 con 1|1|1|
|2|dp[1]+1 con 1|2|1|
|3|dp[2]+1 con 1; dp[0]+1 con 3|1|3|
|4|dp[3]+1 con 1; dp[1]+1 con 3; dp[0]+1 con 4|1|4|
|5|dp[4]+1 con 1; dp[2]+1 con 3; dp[1]+1 con 4|2|1|
|6|dp[5]+1 con 1; dp[3]+1 con 3; dp[2]+1 con 4|2|3|

Los candidatos para 6 son 3,2,3 monedas. Elegimos el mínimo 2. El orden de cálculo creciente funciona porque cada s−m es estrictamente menor que s; no depende de un estado futuro.

## Por qué la recurrencia es correcta

Considera una solución óptima de s y su última moneda m. Si el resto s−m no estuviera resuelto con el mínimo posible, podríamos sustituirlo por una solución mejor y disminuir la cantidad total. Eso contradiría que la solución original era óptima.

Como examinamos todas las monedas posibles para el último paso y utilizamos óptimos de montos menores, el mínimo de los candidatos cubre una solución óptima del monto actual. El caso base 0 y el orden creciente permiten aplicar el argumento de forma inductiva.

Esta justificación cambia si las monedas tienen existencias limitadas. El estado tendría que incluir información sobre disponibilidad o utilizar otra formulación; la tabla de una dimensión no modela esas restricciones automáticamente.

## Reconstruir una combinación

Conocer que el mínimo es 2 no dice todavía qué monedas entregar. Guardamos en previo[s] la moneda que produjo la mejora.

Para monto 6, previo[6]=3. Añadimos 3 a la respuesta y pasamos a monto 3. Allí previo[3]=3; añadimos otra 3 y llegamos a 0. La reconstrucción termina con[3,3].

Cuando dos decisiones dan el mismo mínimo puede haber varias respuestas óptimas. La referencia conserva la primera mejora estricta que encontró; las pruebas verifican suma, monedas permitidas y cantidad mínima, sin exigir un orden irrelevante.

Con monedas 2,4 para monto 3 no existe solución. El marcador permanece en dp[3] y se devuelveNone. Para monto 0 se devuelve[], una solución válida distinta de la imposibilidad.

## Escaleras y casos base

Para contar maneras de subir con saltos de 1 o 2, el último salto provino de n−1 o n−2. La recurrencia se parece a Fibonacci, pero los casos base son otros: hay una forma de quedarse en 0 y una de llegar a 1.

| n |0|1|2|3|4|5|
|---|---:|---:|---:|---:|---:|---:|
| maneras |1|1|2|3|5|8|

La implementación usa dos acumuladores porque cada estado depende solo de los dos anteriores. Esa reducción de memoria es posible para contar; no significa que puedas reconstruir cualquier solución de otro problema sin guardar decisiones.

## Costos y verificación

Con k denominaciones y monto t, la tabla realizaO(t×k) pasos y ocupaO(t), además de la respuesta. Es pseudopolinómica: el número t puede ser grande aunque escribirlo en binario requiera pocos bits. La cantidad de operaciones no es logarítmica respecto a su representación.

Las pruebas independientes enumeran cantidades de monedas para montos pequeños y comparan el mínimo encontrado. No replican la misma recurrencia. Eso complementa el argumento de corrección y permite detectar fallos en estados imposibles, monto 0 o reconstrucción.

**Práctica:** resuelve monedas 2,5 para montos 0..9 en una tabla manual. Señala los imposibles y reconstruye uno posible. Después propone un ejemplo con existencias limitadas y explica qué información le falta a dp[s].
