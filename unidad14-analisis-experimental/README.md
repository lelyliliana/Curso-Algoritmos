# Unidad 14 — Tiempo, memoria y análisis experimental

## Propósito
Aprender a medir algoritmos sin sacar conclusiones engañosas.

## ¿Qué podemos medir?
- tiempo;
- comparaciones;
- asignaciones;
- memoria aproximada;
- profundidad recursiva.

## Tamaño de entrada
Representaremos normalmente el tamaño mediante `n`.

Una medición útil compara varios tamaños:
```text
n = 10
n = 100
n = 1 000
n = 10 000
```

## Tiempo no es suficiente
El tiempo depende también de equipo, lenguaje, carga del sistema e implementación.

Contar operaciones ayuda a observar el crecimiento con menor dependencia del computador.

## Experimento
Para búsqueda lineal registra comparaciones buscando:
- primer elemento;
- elemento central;
- último;
- inexistente.

## Buenas prácticas
- repetir mediciones;
- usar entradas comparables;
- documentar condiciones;
- no modificar varias variables a la vez;
- separar observación de conclusión.

## Reto
Compara dos algoritmos para varios valores de n. Construye una tabla y explica cómo cambia el costo al crecer la entrada.

## Qué sigue
**Unidad 15 — Introducción a complejidad y Big O**
