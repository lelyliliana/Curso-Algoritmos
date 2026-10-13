# Laboratorio 25: Proyecto final: asignación FIFO de cupos

[Unidad](README.md) · [Entorno](../docs/ENTORNO.md) · [Funciones de referencia](../laboratorios/algoritmos.py)

## Problema y contrato

IDs de solicitud únicos en orden de llegada y capacidad entera≥0. Las primeras solicitudes hasta capacidad se confirman; restopasaalistadeespera.

Escribe primero qué entra, qué sale y qué casos se rechazan. Conserva la diferencia entre un requisito y una decisión de implementación. Los datos del caso son pequeños para que puedas comprobarlos a mano.

## Diseño antes de ejecutar

Validar dominio e IDs; dividir cola sin reordenar; conservar cadapersonaexactamenteunavez. Separar requisito de equidad FIFO de optimización de número de personas.

### Prueba de escritorio

[S01, S02, S03, S04], capacidad 2→confirmados S01/S02, espera S03/S04. Con capacidad 0 todosesperan.

Construye una tabla con entrada, paso, estado y resultado. No uses únicamente la salida final para explicar un algoritmo: señala la condición que cambia el estado y la propiedad que debe mantenerse.

## Programa completo y ejecución

1. Prepara [el entorno](../docs/ENTORNO.md). Los programas nuevos usan Python sin dependencias externas; los ejemplos comparativos del curso conservan Java y JavaScript.
2. Abre [caso_completo.py](ejemplos/caso_completo.py) y localiza la función utilizada en [algoritmos.py](../laboratorios/algoritmos.py). El archivo del caso prepara datos y representa resultado; la función compartida contiene la implementación.
3. Antes de ejecutar, predice el resultado con la prueba de escritorio.
4. Desde la raíz del curso ejecuta por separado:

```text
python unidad25-proyecto-final/ejemplos/caso_completo.py
```

En macOS/Linux utiliza `python3` si es tu ejecutor; en Windows puedes usar `py -3`. El programa encuentra su módulo aunque la carpeta actual sea diferente.

### Salida de referencia

```json
{"confirmados": ["S01", "S02"], "espera": ["S03", "S04"]}
```

5. Cambia una entrada en tu copia o llama a la función con un caso distinto. Conserva el resultado esperado antes de ejecutar y verifica contrato, no solo ausencia de excepciones.
6. Ejecuta las pruebas del curso antes de conservar una modificación en las funciones compartidas.

## Costos y límites

O(n) validación/salida, O(n) espacio. Es una base funcional local, no aplicación con usuarios, persistencia oregistro web.

Distingue operación central, validación, preparación, representación y tamaño de respuesta. Si la función utiliza copias o concatenaciones, contabilízalas; una descripción de un algoritmo abstracto no garantiza el mismo costo de cualquier implementación.

## Ejercicios

1. Rechaza ID duplicado.
2. Prueba capacidad mayor que total.
3. Amplíacancelaciónypromoción con invariantes.

Consulta [SOLUCIONES.md](SOLUCIONES.md) después de intentar. Justifica con una traza o caso límite; copiar el resultado de referencia no demuestra comprender la decisión.

## Criterios para avanzar

- Puedo explicar entrada, salida y precondiciones de la función.
- Mi caso normal coincide con la referencia y puedo explicar cada decisión.
- Probé vacío, frontera o dato inválido según el contrato; no todos los casos tienen que aceptarse.
- Explico un límite y el costo real de la implementación.
- Conservé [evidencias de la práctica](../docs/EVIDENCIAS.md) y distinguí predicción de observación.

[Volver a la unidad](README.md) · [Volver a Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/algoritmos/).
