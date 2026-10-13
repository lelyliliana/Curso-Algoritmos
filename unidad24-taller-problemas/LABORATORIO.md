# Laboratorio 24: Taller: comparar estrategias con un criterio verificable

[Unidad](README.md) · [Entorno](../docs/ENTORNO.md) · [Funciones de referencia](../laboratorios/algoritmos.py)

## Problema y contrato

Mismo objetivo: minimizar número de monedas, con denominaciones positivas ilimitadas. Comparaheurística y solución exacta.

Escribe primero qué entra, qué sale y qué casos se rechazan. Conserva la diferencia entre un requisito y una decisión de implementación. Los datos del caso son pequeños para que puedas comprobarlos a mano.

## Diseño antes de ejecutar

Definir contrato; diseñar casos; ejecutar greedy y DP; verificar suma y cantidad; documentar cuál garantiza óptimo y por qué. No elegirpor longitud de código.

### Prueba de escritorio

Para[1,3,4],6: greedy[4,1,1], DP[3,3]. Ambos suman 6; solo uno logra mínimo 2.

Construye una tabla con entrada, paso, estado y resultado. No uses únicamente la salida final para explicar un algoritmo: señala la condición que cambia el estado y la propiedad que debe mantenerse.

## Programa completo y ejecución

1. Prepara [el entorno](../docs/ENTORNO.md). Los programas nuevos usan Python sin dependencias externas; los ejemplos comparativos del curso conservan Java y JavaScript.
2. Abre [caso_completo.py](ejemplos/caso_completo.py) y localiza la función utilizada en [algoritmos.py](../laboratorios/algoritmos.py). El archivo del caso prepara datos y representa resultado; la función compartida contiene la implementación.
3. Antes de ejecutar, predice el resultado con la prueba de escritorio.
4. Desde la raíz del curso ejecuta por separado:

```text
python unidad24-taller-problemas/ejemplos/caso_completo.py
```

En macOS/Linux utiliza `python3` si es tu ejecutor; en Windows puedes usar `py -3`. El programa encuentra su módulo aunque la carpeta actual sea diferente.

### Salida de referencia

```json
{"criterio": "minimo numero de monedas", "dp": [3, 3], "greedy": [4, 1, 1]}
```

5. Cambia una entrada en tu copia o llama a la función con un caso distinto. Conserva el resultado esperado antes de ejecutar y verifica contrato, no solo ausencia de excepciones.
6. Ejecuta las pruebas del curso antes de conservar una modificación en las funciones compartidas.

## Costos y límites

Separar ordenación, salida, DPpseudopolinómica y límites de datos. No comparar tiempo de una salida distinta sin criterio común.

Distingue operación central, validación, preparación, representación y tamaño de respuesta. Si la función utiliza copias o concatenaciones, contabilízalas; una descripción de un algoritmo abstracto no garantiza el mismo costo de cualquier implementación.

## Ejercicios

1. Encuentra otros montos dondecoinciden.
2. Diseña oráculo bruto para pequeños.
3. ¿Coincidir en 10casos prueba verdad universal?

Consulta [SOLUCIONES.md](SOLUCIONES.md) después de intentar. Justifica con una traza o caso límite; copiar el resultado de referencia no demuestra comprender la decisión.

## Criterios para avanzar

- Puedo explicar entrada, salida y precondiciones de la función.
- Mi caso normal coincide con la referencia y puedo explicar cada decisión.
- Probé vacío, frontera o dato inválido según el contrato; no todos los casos tienen que aceptarse.
- Explico un límite y el costo real de la implementación.
- Conservé [evidencias de la práctica](../docs/EVIDENCIAS.md) y distinguí predicción de observación.

[Volver a la unidad](README.md) · [Volver a Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/algoritmos/).
