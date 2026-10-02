# Unidad 23 — Introducción a programación dinámica

## Propósito
Evitar repetir cálculos cuando un problema contiene subproblemas superpuestos y una estructura que permite reutilizar soluciones.

## Idea
Una solución recursiva puede calcular el mismo subproblema muchas veces.

### Memoización
Guardar resultados a medida que se calculan.

### Tabulación
Construir soluciones pequeñas hasta llegar al problema completo.

## Fibonacci como ejemplo didáctico
La recursión ingenua repite trabajo. Guardar resultados evita recalcular.

Fibonacci es útil para entender la técnica, aunque no representa por sí solo toda la programación dinámica.

## Pasos
1. Define el estado.
2. Identifica la relación entre estados.
3. Define casos base.
4. Decide memoización o tabulación.
5. Determina el orden de cálculo.
6. Recupera la respuesta.

## Ejercicios
1. Fibonacci con memoización.
2. Fibonacci con tabla.
3. Número de formas de subir escalones.
4. Suma mínima en una cuadrícula pequeña.

## Reto
Resuelve un problema sencillo primero mediante exploración recursiva y después reutilizando subproblemas. Compara el número de llamadas u operaciones.

## Qué sigue
**Unidad 24 — Taller de resolución de problemas**
