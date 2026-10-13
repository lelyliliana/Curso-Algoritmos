# Laboratorio 21: Greedy: selección de interva los y contraejemplo de cambio

[Unidad](README.md) · [Entorno](../docs/ENTORNO.md) · [Funciones de referencia](../laboratorios/algoritmos.py)

## Problema y contrato

Interva los[inicio, fin) válidos y monedas enteras positivas. Maximizar número deintervalos compatibles; greedy de cambio no garantiza mínimo para cualquier sistema.

Escribe primero qué entra, qué sale y qué casos se rechazan. Conserva la diferencia entre un requisito y una decisión de implementación. Los datos del caso son pequeños para que puedas comprobarlos a mano.

## Diseño antes de ejecutar

Lee el [desarrollo paso a paso, con justificación y tablas](DESARROLLO.md).

Ordenar interva los por fin creciente; aceptar si inicio≥fin último. Para monedas, tomar mayor que cabe y repetir con resto. Cada problema exige justificar selección local.

### Prueba de escritorio

(1,2)→(2,4)→(4,6), tresactividades. Monedas[1,3,4], total 6: greedy 4+1+1 usa 3; óptimo 3+3 usa 2.

Construye una tabla con entrada, paso, estado y resultado. No uses únicamente la salida final para explicar un algoritmo: señala la condición que cambia el estado y la propiedad que debe mantenerse.

## Programa completo y ejecución

1. Prepara [el entorno](../docs/ENTORNO.md). Los programas nuevos usan Python sin dependencias externas; los ejemplos comparativos del curso conservan Java y JavaScript.
2. Abre [caso_completo.py](ejemplos/caso_completo.py) y localiza la función utilizada en [algoritmos.py](../laboratorios/algoritmos.py). El archivo del caso prepara datos y representa resultado; la función compartida contiene la implementación.
3. Antes de ejecutar, predice el resultado con la prueba de escritorio.
4. Desde la raíz del curso ejecuta por separado:

```text
python unidad21-greedy/ejemplos/caso_completo.py
```

En macOS/Linux utiliza `python3` si es tu ejecutor; en Windows puedes usar `py -3`. El programa encuentra su módulo aunque la carpeta actual sea diferente.

### Salida de referencia

```json
{"greedy_cambio": [4, 1, 1], "intervalos": [[1, 2], [2, 4], [4, 6]]}
```

5. Cambia una entrada en tu copia o llama a la función con un caso distinto. Conserva el resultado esperado antes de ejecutar y verifica contrato, no solo ausencia de excepciones.
6. Ejecuta las pruebas del curso antes de conservar una modificación en las funciones compartidas.

## Costos y límites

Interva los O(n log n) por ordenación/O(n) salida. Cambioordenación O(k log k) más tamaño de salida; no prometer optimalidad universal.

Distingue operación central, validación, preparación, representación y tamaño de respuesta. Si la función utiliza copias o concatenaciones, contabilízalas; una descripción de un algoritmo abstracto no garantiza el mismo costo de cualquier implementación.

## Ejercicios

1. ¿Permitir interva los quetocan extremo?
2. Da intercambio quejustifica elegirfin más temprano.
3. Compara cambio[1,3,4] para 6.

Consulta [SOLUCIONES.md](SOLUCIONES.md) después de intentar. Justifica con una traza o caso límite; copiar el resultado de referencia no demuestra comprender la decisión.

## Criterios para avanzar

- Puedo explicar entrada, salida y precondiciones de la función.
- Mi caso normal coincide con la referencia y puedo explicar cada decisión.
- Probé vacío, frontera o dato inválido según el contrato; no todos los casos tienen que aceptarse.
- Explico un límite y el costo real de la implementación.
- Conservé [evidencias de la práctica](../docs/EVIDENCIAS.md) y distinguí predicción de observación.

[Volver a la unidad](README.md) · [Volver a Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/algoritmos/).

## Comparar Python, JavaScript y Java

Abre [JavaScript](ejemplos/javascript/caso_completo.js) y [Java](ejemplos/java/GreedyCambio.java). Ambos implementan la estrategia completa, no solo una llamada al ejemplo Python. Para comparar, utiliza totales enteros de 0 a 10000 y valores positivos; en backtracking limita la colección a 20 elementos y cada valor a 10000. El límite hace observable un laboratorio pequeño y evita suponer enteros ilimitados en los tres lenguajes.

Desde la raíz, ejecuta cada paso por separado:

```text
node unidad21-greedy/ejemplos/javascript/caso_completo.js
```

```text
javac -encoding UTF-8 -d build unidad21-greedy/ejemplos/java/GreedyCambio.java
```

```text
java -cp build GreedyCambio
```

Crea antes la carpeta build con tu explorador o terminal. Java usa clases y colecciones tipadas; JavaScript usa Number dentro del dominio verificado; Python admite enteros arbitrarios. Compara índices, cantidades y sumas, no los espacios de impresión. null en Java/JavaScript corresponde a None en Python para un cambio imposible.
