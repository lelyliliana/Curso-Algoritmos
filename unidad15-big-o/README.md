# Unidad 15 — Complejidad y notación Big O

## Qué aprenderás
Describir cómo crece el costo al aumentar n, reconocer patrones y distinguir análisis asintótico de tiempo real.

# 1. Big O no son segundos

Si un algoritmo tarda 2 ms hoy, eso no dice por sí solo cómo crecerá.

Big O describe una cota/tendencia asintótica del crecimiento, omitiendo constantes y términos menos dominantes según el análisis.

# 2. O(1)

```text
valor ← datos[5]
```

Acceder a una posición conocida suele modelarse como costo constante respecto al número de elementos.

No significa literalmente “una instrucción”.

# 3. O(n)

```text
PARA CADA elemento EN datos
    PROCESAR elemento
FIN
```

Si n se duplica, el trabajo dominante suele aproximadamente duplicarse.

# 4. O(n²)

```text
PARA i ...
    PARA j ...
        PROCESAR
```

Si ambos ciclos recorren n, aparecen aproximadamente n×n combinaciones.

Pero “dos ciclos” no implica siempre n²: si son consecutivos:
```text
n + n = 2n → O(n)
```

# 5. O(log n)

Búsqueda binaria reduce el espacio aproximadamente a la mitad:

```text
1024 → 512 → 256 → ... → 1
```

Pocos pasos adicionales aunque n crezca mucho.

# 6. O(n log n)

Merge Sort divide en niveles logarítmicos y realiza trabajo lineal de mezcla por nivel, dando el patrón O(n log n).

# 7. O(2^n) y O(n!)

Aparecen en ciertas exploraciones combinatorias exhaustivas.

Crecen tan rápido que entradas moderadas pueden volverse impracticables.

# 8. Término dominante

```text
3n² + 5n + 100
→ O(n²)
```

Para n grande domina el término cuadrático.

# 9. Constantes

```text
1000n
```
sigue siendo O(n).

Eso **no significa** que las constantes sean irrelevantes en rendimiento real; Big O responde otra pregunta.

# 10. Mejor/peor/promedio

Búsqueda lineal:
- mejor: objetivo primero → O(1);
- peor: último/inexistente → O(n);
- promedio requiere supuestos sobre distribución/posición.

Siempre indica qué caso analizas.

# 11. Espacio

También podemos analizar memoria adicional.

Un algoritmo puede tener:
```text
tiempo O(n)
espacio O(n)
```

# 12. Práctica guiada

Clasifica:
1. acceso directo;
2. un recorrido;
3. dos recorridos consecutivos;
4. dos ciclos anidados n×n;
5. reducir n a la mitad;
6. recorrer n dentro de log n niveles.

Explica, no adivines por forma visual.

# 13. Relación con experimento

Unidad 14 observa comportamiento concreto.

Big O analiza crecimiento abstracto.

Los resultados experimentales deberían ser compatibles con la teoría a suficiente escala, pero ruido/constantes/implementación pueden ocultar la tendencia en tamaños pequeños.

# 14. Errores frecuentes
- Big O = segundos.
- Dos ciclos siempre n².
- O(1) = una operación.
- Ignorar qué representa n.
- Decir “O(n) siempre más rápido que O(n²)” para cualquier n/implementación.

# 15. Reto
Analiza cinco algoritmos del curso y justifica tiempo/espacio. Relaciona dos con datos experimentales.

# 16. Autoevaluación
1. ¿Qué describe Big O?
2. ¿Por qué 3n+10 → O(n)?
3. ¿Dos ciclos consecutivos?
4. ¿Por qué binaria es logarítmica?
5. ¿Constantes no importan nunca?
6. ¿Tiempo y espacio pueden diferir?

# 17. Checklist
- [ ] Defino n.
- [ ] Reconozco patrones.
- [ ] Distingo teoría/medición.
- [ ] Indico caso analizado.
- [ ] Considero espacio.

Continúa con estructuras.
