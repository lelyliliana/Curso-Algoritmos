# Unidad 19 — Introducción a grafos, BFS y DFS

## Propósito
Modelar relaciones entre elementos y recorrer redes.

Un grafo contiene:
- vértices o nodos;
- aristas o conexiones.

Puede ser dirigido/no dirigido y ponderado/no ponderado.

## Representaciones
### Lista de adyacencia
```text
A: B, C
B: A, D
C: A, D
D: B, C
```

### Matriz de adyacencia
Útil para representar conexiones en una tabla.

## BFS
Recorre por niveles y utiliza una **cola**.

## DFS
Profundiza por un camino antes de retroceder. Puede utilizar una **pila** o recursividad.

## Aplicaciones
- redes sociales;
- rutas;
- dependencias;
- mapas;
- conexiones entre páginas.

## Ejercicios
1. Convierte un dibujo en lista de adyacencia.
2. Ejecuta BFS manual.
3. Ejecuta DFS manual.
4. Detecta nodos alcanzables.
5. Compara el orden producido por ambos recorridos.

## Reto
Modela una pequeña red de ciudades y conexiones. Determina alcanzabilidad y recorrido desde una ciudad elegida.

## Qué sigue
**Unidad 20 — Divide y vencerás**
