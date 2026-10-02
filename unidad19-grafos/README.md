# Unidad 19 — Grafos, BFS y DFS

## Qué aprenderás
Modelar redes, representar adyacencias y recorrer grafos controlando ciclos.

# 1. Grafo

Ciudades y carreteras:

```text
A --- B
|     |
C --- D
```

Vértices: A,B,C,D. Aristas: conexiones.

# 2. Tipos

**No dirigido:** A-B implica conexión en ambos sentidos.  
**Dirigido:** A→B no implica B→A.  
**Ponderado:** aristas tienen costo/distancia.

BFS/DFS básicos no resuelven por sí solos caminos mínimos con pesos arbitrarios.

# 3. Lista de adyacencia

```text
A: B,C
B: A,D
C: A,D
D: B,C
```

# 4. Matriz de adyacencia

Una tabla V×V marca conexiones.

Conceptualmente:
- matriz usa O(V²) espacio;
- lista suele ahorrar espacio en grafos dispersos, dependiendo de representación.

# 5. Ciclos y visitados

```text
A-B-C-A
```

Sin conjunto de visitados puedes volver indefinidamente.

# 6. BFS

Usa cola:

```text
encolar inicio
marcar visitado

MIENTRAS cola no vacía
    actual ← desencolar
    PARA CADA vecino
        SI no visitado
            marcar visitado
            encolar vecino
        FIN SI
    FIN
FIN
```

Explora por niveles.

En grafos no ponderados puede hallar mínimo número de aristas desde origen si registramos distancia/predecesor.

# 7. DFS

Profundiza por un camino antes de retroceder.

Puede implementarse con pila explícita o recursión.

El orden exacto depende del orden en que consideramos vecinos.

# 8. Comparar

BFS no es “mejor” que DFS.

Pregunta:
- ¿necesito niveles?
- ¿distancia en aristas?
- ¿explorar profundidad?
- ¿qué estructura/frente debo mantener?

# 9. Componentes

En un grafo no dirigido, si desde A no alcanzamos X, pueden pertenecer a componentes diferentes.

Podemos iniciar recorridos desde nodos aún no visitados para descubrir componentes.

# 10. Reconstruir camino

Guarda:
```text
predecesor[vecino] ← actual
```

Al encontrar destino, retrocede por predecesores.

# 11. Práctica guiada

Dibuja seis nodos con un ciclo y uno aislado.

Tabla:
```text
paso | cola/pila | actual | visitados
```

Traza BFS y DFS.

# 12. Errores frecuentes
- No marcar visitados.
- Marcar demasiado tarde y añadir repetidos.
- Asumir un único orden válido.
- BFS básico con pesos arbitrarios.
- Confundir dirigido/no dirigido.

# 13. Ejercicios
Representación, BFS, DFS, alcanzabilidad, componentes y camino por predecesores.

# 14. Reto
Modela ciudades. Desde una ciudad encuentra alcanzables y un camino con mínimo número de conexiones usando BFS.

# 15. Autoevaluación
1. ¿Vértice/arista?
2. ¿Dirigido?
3. ¿Por qué visitados?
4. ¿Qué usa BFS?
5. ¿Qué usa DFS?
6. ¿BFS sirve para pesos arbitrarios?

# 16. Checklist
- [ ] Modelo grafos.
- [ ] Represento adyacencia.
- [ ] Trazo BFS/DFS.
- [ ] Manejo ciclos.
- [ ] Comprendo límites de BFS.

Continúa con estrategias.
