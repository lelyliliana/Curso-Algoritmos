# Greedy: una elección local necesita una justificación

[Laboratorio y programas](LABORATORIO.md) · [Soluciones](SOLUCIONES.md)

## Dos problemas que parecen similares

Una estrategia voraz decide qué hacer ahora sin explorar todas las consecuencias futuras. Eso puede ser útil, pero no permite concluir automáticamente que encuentre el óptimo. Separaremos dos problemas: seleccionar el mayor número de actividades compatibles y entregar cambio con el menor número de monedas.

En ambos hay una elección local. En el primero podemos justificarla bajo el contrato definido; en el segundo veremos un contraejemplo. La garantía pertenece al problema y al criterio de selección, no a la palabra greedy.

## Selección de actividades

La entrada contiene interva los con extremos enteros y principio menor que final. Usamos interva los semiabiertos: una actividad que termina a las 2 permite otra que empieza exactamente a las 2. Si tu contexto exige una pausa entre actividades, esa sería otra restricción que tendrías que modelar antes.

Objetivo: maximizar **cantidad de actividades**, sin pesos ni prioridades. No buscamos duración total ni el mayor beneficio económico.

| Actividad | Inicio | Fin |
|---|---:|---:|
| A |0|3|
| B |1|2|
| C |2|4|
| D |3|5|
| E |4|6|

Ordenamos por final creciente: B, A, C, D, E. Elegir la que empieza primero no es equivalente a elegir la que termina primero.

| Paso | Candidata | Fin anterior | Decisión | Selección |
|---|---|---:|---|---|
|1|B(1,2)|ninguno|aceptar|B|
|2|A(0,3)|2|rechazar:0<2|B|
|3|C(2,4)|2|aceptar:2≥2|B, C|
|4|D(3,5)|4|rechazar:3<4|B, C|
|5|E(4,6)|4|aceptar:4≥4|B, C, E|

El estado que debemos conservar es el final de la última actividad elegida. Como están ordenadas por final, aceptar una compatible deja el mayor margen disponible para las siguientes.

## Argumento de intercambio

Considera una selección óptima y su primera actividadO. La candidataG que termina primero no termina después deO. SustituirO porG no impide ninguna actividad posterior que ya era compatible conO: su inicio es al menos fin(O), y por tanto también al menos fin(G).

Así existe una solución óptima que empieza conG. Después de elegirla, el problema restante tiene el mismo formato: seleccionar entre actividades cuyo inicio no es anterior a fin(G). Podemos repetir el argumento.

Ese razonamiento prueba el criterio para este contrato. Si cada actividad tiene un beneficio distinto, maximizar cantidad deja de representar el objetivo; el intercambio anterior no prueba máximo beneficio.

## Cambio de monedas: el criterio puede fallar

Denominaciones 1,3,4; monto 6; monedas ilimitadas; objetivo mínimo número de monedas.

| Paso voraz | Elegida | Resto |
|---|---:|---:|
|1|4|2|
|2|1|1|
|3|1|0|

La suma es correcta, pero usa tres monedas. La alternativa 3+3 entrega la misma suma con dos. Por tanto, demostrar que el algoritmo entrega cambio no demuestra que lo minimice.

Con monedas 3 y 4 para monto 6 el problema es aún más claro: elegir 4 deja resto 2, que no puede completarse. El programa retorna None, aunque 3+3 sí es una solución. Debes interpretar None como **la estrategia voraz no completó el cambio**, no como una prueba general de imposibilidad.

## Pseudocódigo del recorrido

```text
ORDENAR actividades por final
seleccion ← colección vacía
ultimo_final ← sin actividad
PARA cada actividad:
    SI no hay actividad previa O inicio ≥ ultimo_final:
        AÑADIR actividad
        ultimo_final ← final
RETORNAR seleccion
```

Para el cambio, las denominaciones se recorren de mayor a menor y se toma tantas veces cada una como cabe. Lee ambas funciones en algoritmos.py y localiza dónde se implementa cada decisión.

## Costos y preguntas de revisión

Ordenar actividades cuestaO(n log n); el recorrido posterior cuestaO(n). La respuesta ocupaO(k). Para monedas, debes contar ordenación y el número de monedas que escribes en la respuesta; una lista enorme no se produce en tiempo constante.

Antes de usar greedy en otro problema, identifica decisión local, estado que conserva, criterio de éxito y argumento que permite no explorar alternativas. Si no puedes justificar el último, trata la estrategia como una heurística y compara con una referencia pequeña.

**Práctica:** agrega una actividad muy larga que comienza antes que todas. Comprueba que elegir por inicio puede reducir la cantidad final. Después asigna beneficios distintos y explica por qué la regla de fin temprano ya no prueba el nuevo objetivo.
