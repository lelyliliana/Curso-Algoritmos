# Unidad 15 — Introducción a complejidad y notación Big O

## Propósito
Describir cómo crece el costo de un algoritmo cuando aumenta el tamaño de la entrada.

Big O no dice exactamente cuántos segundos tarda un programa. Describe una **tendencia de crecimiento**.

## O(1)
Costo aproximadamente independiente de n.
Ejemplo: acceder a una posición conocida de un arreglo.

## O(log n)
El problema se reduce por un factor en cada paso.
Ejemplo: búsqueda binaria.

## O(n)
El trabajo crece proporcionalmente con los elementos.
Ejemplo: recorrer una lista.

## O(n log n)
Aparece en algoritmos eficientes como Merge Sort.

## O(n²)
Dos recorridos anidados sobre n elementos son un patrón frecuente.
Ejemplo: varios ordenamientos básicos.

## O(2^n) y O(n!)
Crecimientos muy rápidos que aparecen en ciertas exploraciones exhaustivas.

## Ignorar constantes
```text
3n + 10 → O(n)
```
Nos interesa el término dominante al crecer n.

## Mejor, promedio y peor caso
El mismo algoritmo puede comportarse de forma diferente según la entrada. Indica qué caso estás analizando.

## Ejercicios
Clasifica fragmentos conceptuales:
1. acceso directo;
2. un recorrido;
3. dos recorridos consecutivos;
4. dos ciclos anidados;
5. reducir n a la mitad repetidamente.

## Reto
Relaciona las mediciones de la Unidad 14 con sus órdenes de crecimiento esperados. Explica coincidencias y diferencias.

## Qué sigue
**Unidad 16 — Pilas y colas**
