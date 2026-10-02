# Unidad 11 — Ordenamientos básicos

## Qué aprenderás
Comprender Bubble, Selection e Insertion Sort mediante invariantes intuitivas, trazas y comparación de trabajo.

# 1. ¿Qué significa ordenar?

Entrada:
```text
[5,2,4,1]
```

Salida ascendente:
```text
[1,2,4,5]
```

La salida contiene los mismos elementos; cambia su orden según un criterio.

# 2. Bubble Sort

Compara vecinos e intercambia si están invertidos.

Primera pasada:
```text
[5,2,4,1]
5/2 → [2,5,4,1]
5/4 → [2,4,5,1]
5/1 → [2,4,1,5]
```

El mayor “burbujeó” al final.

Idea que debes poder explicar:
> después de una pasada completa, un elemento extremo queda colocado.

# 3. Selection Sort

Busca el menor de la zona pendiente y lo coloca al inicio.

```text
[5,2,4,1]
menor=1
→ [1,2,4,5]  (tras intercambio inicial, luego continúa)
```

La parte izquierda crece ordenada.

# 4. Insertion Sort

Construye una zona ordenada.

```text
[5 | 2,4,1]
[2,5 | 4,1]
[2,4,5 | 1]
[1,2,4,5]
```

Cada nuevo elemento se inserta en la posición adecuada dentro de la parte ordenada.

# 5. No memorices código

Para cada algoritmo responde:
- ¿qué parte ya está resuelta?
- ¿qué compara?
- ¿qué mueve?
- ¿qué cambia después de una pasada?
- ¿cómo se comporta con datos ya ordenados?

# 6. Comparaciones y movimientos

Dos algoritmos pueden producir el mismo resultado y realizar distinto trabajo.

Registra:
```text
comparaciones
intercambios/movimientos
```

No confundas “pocas líneas de código” con “poco trabajo”.

# 7. Datos ya ordenados

Insertion puede necesitar pocos desplazamientos en datos casi ordenados.

Una implementación de Bubble con detección de “sin intercambios” puede terminar antes.

Selection normalmente sigue buscando el mínimo de la zona restante.

Las implementaciones concretas importan.

# 8. Repetidos y estabilidad

Un algoritmo estable conserva el orden relativo de elementos equivalentes.

Esto importa si ordenamos registros por una clave después de haberlos ordenado por otra.

La estabilidad depende del algoritmo/implementación.

# 9. Práctica guiada

Traza los tres con:
```text
[5,2,4,1]
```

Usa una tabla:
```text
paso | comparación | movimiento | estado
```

# 10. Errores frecuentes
- Memorizar código sin poder trazar.
- Confundir comparaciones con intercambios.
- Comparar implementaciones distintas sin documentarlo.
- Decir “X es mejor” sin escenario.

# 11. Ejercicios
Traza:
- [4,3,2,1];
- [1,2,3,4];
- [3,1,4,2];
- repetidos.

Cuenta operaciones.

# 12. Reto
Implementa/representa los tres, genera varias entradas y explica qué observaste. No conviertas una medición pequeña en una ley universal.

# 13. Autoevaluación
1. ¿Qué hace Bubble?
2. ¿Qué zona resuelve Selection?
3. ¿Qué construye Insertion?
4. ¿Comparación e intercambio son lo mismo?
5. ¿Qué significa estabilidad?

# 14. Checklist
- [ ] Trazo los tres.
- [ ] Explico la estrategia.
- [ ] Cuento trabajo.
- [ ] Comparo con contexto.

Continúa con Merge/Quick.
