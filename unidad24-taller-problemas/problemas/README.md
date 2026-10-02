# Taller integrador de resolución de problemas

## Regla del taller

Los problemas **no indican qué algoritmo o estructura debes utilizar**. Parte del aprendizaje consiste en reconocer el patrón y justificar la elección.

Para cada problema entrega:

1. reformulación;
2. entradas y salidas;
3. restricciones;
4. ejemplos propios;
5. casos límite;
6. estrategia;
7. estructura de datos;
8. pseudocódigo;
9. pruebas;
10. complejidad esperada;
11. implementación;
12. alternativas consideradas.

---

## Problema 1 — Primer duplicado

Dada una secuencia, determina el primer valor que aparece por segunda vez.

Ejemplo:
```text
[4, 7, 2, 7, 4]
```

Resultado:
```text
7
```

### Preguntas
- ¿Necesitas conservar orden?
- ¿Qué ocurre si no hay repetidos?
- ¿Puedes hacerlo sin comparar cada elemento con todos los demás?

---

## Problema 2 — Dos valores que suman

Dada una colección y un objetivo, determina si existen dos posiciones diferentes cuyos valores sumen el objetivo.

No asumas que la colección está ordenada.

---

## Problema 3 — Muchas consultas

Tienes una colección de 100 000 identificadores y debes realizar miles de búsquedas.

Compara al menos dos estrategias. Incluye el costo de preparar los datos, no solamente el costo de una consulta.

---

## Problema 4 — Agenda de intervalos

Selecciona la mayor cantidad posible de actividades que no se solapen.

Cada actividad tiene:
```text
inicio, fin
```

Justifica la regla de selección.

---

## Problema 5 — Red de contactos

Dadas relaciones entre personas:
- determina si dos personas están conectadas;
- encuentra cuántos saltos mínimos las separan cuando exista conexión.

Modela explícitamente la red.

---

## Problema 6 — Texto frecuente

Dado un documento:
- normaliza según reglas definidas por ti;
- cuenta palabras;
- encuentra las 10 más frecuentes;
- conserva evidencia de empates.

---

## Problema 7 — Laberinto

Encuentra una ruta desde entrada hasta salida en una cuadrícula con obstáculos.

Define:
- movimientos permitidos;
- representación;
- criterio de visitado;
- qué significa “mejor ruta”, si aplica.

---

## Problema 8 — Cambio de monedas

Para un sistema de monedas dado, encuentra el mínimo número de monedas para un valor objetivo.

Compara una estrategia greedy con otra que pueda garantizar la solución para el sistema analizado.

---

## Problema 9 — Dependencias

Un conjunto de tareas contiene dependencias del tipo:
```text
A debe ocurrir antes que B
```

Determina si las dependencias contienen un ciclo.

---

## Problema 10 — Ruta de costo

Modela ubicaciones conectadas con costos. Formula cómo encontrarías una ruta de menor costo.

Este problema sirve como puente: investiga qué algoritmo sería apropiado y explica por qué. No implementes una técnica que no puedas explicar.

---

# Criterio de cierre

No existe una única implementación obligatoria. Una solución se considera sólida cuando:
- satisface requisitos;
- maneja límites;
- puede explicarse;
- tiene pruebas;
- la estructura elegida tiene sentido;
- el análisis de costo es coherente.
