# Laboratorio 23: Programación dinámica: mínimo de monedas y escaleras

[Unidad](README.md) · [Entorno](../docs/ENTORNO.md) · [Funciones de referencia](../laboratorios/algoritmos.py)

## Problema y contrato

Monedas positivas ilimitadas y total≥0; retorna una combinación mínima o None si imposible. Escaleras permite saltos 1/2, con una manera de quedarse en 0.

Escribe primero qué entra, qué sale y qué casos se rechazan. Conserva la diferencia entre un requisito y una decisión de implementación. Los datos del caso son pequeños para que puedas comprobarlos a mano.

## Diseño antes de ejecutar

Lee el [desarrollo paso a paso, con justificación y tablas](DESARROLLO.md).

dp[0]=0; para s 1..total: dp[s]=min(dp[s−m]+1) para m≤s y estado alcanzable. Guardar moneda previa permite reconstruir. Escaleras F(n)=F(n−1)+F(n−2), F(0)=F(1)=1.

### Prueba de escritorio

Monedas 1/3/4: dp 0..6=[0,1,2,1,1,2,2]; para 6 seleccionar 3 y volver 3→0. Escaleras 0..5=[1,1,2,3,5,8].

Construye una tabla con entrada, paso, estado y resultado. No uses únicamente la salida final para explicar un algoritmo: señala la condición que cambia el estado y la propiedad que debe mantenerse.

## Programa completo y ejecución

1. Prepara [el entorno](../docs/ENTORNO.md). Los programas nuevos usan Python sin dependencias externas; los ejemplos comparativos del curso conservan Java y JavaScript.
2. Abre [caso_completo.py](ejemplos/caso_completo.py) y localiza la función utilizada en [algoritmos.py](../laboratorios/algoritmos.py). El archivo del caso prepara datos y representa resultado; la función compartida contiene la implementación.
3. Antes de ejecutar, predice el resultado con la prueba de escritorio.
4. Desde la raíz del curso ejecuta por separado:

```text
python unidad23-programacion-dinamica/ejemplos/caso_completo.py
```

En macOS/Linux utiliza `python3` si es tu ejecutor; en Windows puedes usar `py -3`. El programa encuentra su módulo aunque la carpeta actual sea diferente.

### Salida de referencia

```json
{"formas_escaleras_5": 8, "minimo_cambio": [3, 3]}
```

5. Cambia una entrada en tu copia o llama a la función con un caso distinto. Conserva el resultado esperado antes de ejecutar y verifica contrato, no solo ausencia de excepciones.
6. Ejecuta las pruebas del curso antes de conservar una modificación en las funciones compartidas.

## Costos y límites

Cambio O(total×k), memoria O(total) más respuesta. Es pseudopolinómico respecto a total en bits. Escaleras O(n) operaciones y dos acumuladores; enteros crecen por bits.

Distingue operación central, validación, preparación, representación y tamaño de respuesta. Si la función utiliza copias o concatenaciones, contabilízalas; una descripción de un algoritmo abstracto no garantiza el mismo costo de cualquier implementación.

## Ejercicios

1. Cambio[2,4] para 3.
2. ¿Fibonacci clásico y formas de escaleras tienen bases iguales?
3. Reconstruye mínimo para 6.

Consulta [SOLUCIONES.md](SOLUCIONES.md) después de intentar. Justifica con una traza o caso límite; copiar el resultado de referencia no demuestra comprender la decisión.

## Criterios para avanzar

- Puedo explicar entrada, salida y precondiciones de la función.
- Mi caso normal coincide con la referencia y puedo explicar cada decisión.
- Probé vacío, frontera o dato inválido según el contrato; no todos los casos tienen que aceptarse.
- Explico un límite y el costo real de la implementación.
- Conservé [evidencias de la práctica](../docs/EVIDENCIAS.md) y distinguí predicción de observación.

[Volver a la unidad](README.md) · [Volver a Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/algoritmos/).

## Comparar Python, JavaScript y Java

Abre [JavaScript](ejemplos/javascript/caso_completo.js) y [Java](ejemplos/java/CambioDinamico.java). Ambos implementan la estrategia completa, no solo una llamada al ejemplo Python. Para comparar, utiliza totales enteros de 0 a 10000 y valores positivos; en backtracking limita la colección a 20 elementos y cada valor a 10000. El límite hace observable un laboratorio pequeño y evita suponer enteros ilimitados en los tres lenguajes.

Desde la raíz, ejecuta cada paso por separado:

```text
node unidad23-programacion-dinamica/ejemplos/javascript/caso_completo.js
```

```text
javac -encoding UTF-8 -d build unidad23-programacion-dinamica/ejemplos/java/CambioDinamico.java
```

```text
java -cp build CambioDinamico
```

Crea antes la carpeta build con tu explorador o terminal. Java usa clases y colecciones tipadas; JavaScript usa Number dentro del dominio verificado; Python admite enteros arbitrarios. Compara índices, cantidades y sumas, no los espacios de impresión. null en Java/JavaScript corresponde a None en Python para un cambio imposible.
