# Unidad 08 — Matrices y datos bidimensionales

## Qué aprenderás
Representar filas/columnas, acceder por coordenadas y construir recorridos bidimensionales.

# 1. ¿Por qué dos dimensiones?

Notas de estudiantes en actividades:

| | A1 | A2 | A3 |
|---|---:|---:|---:|
| Ana | 4 | 5 | 3 |
| Luis | 3 | 4 | 4 |

Una colección lineal perdería parte de la estructura conceptual.

Matriz:

```text
[
 [4,5,3],
 [3,4,4]
]
```

# 2. Coordenadas

```text
matriz[fila][columna]
```

`matriz[0][1]` → 5 en este ejemplo.

No confundas fila/columna.

# 3. Recorrido completo

```text
PARA fila ← 0 HASTA filas-1
    PARA columna ← 0 HASTA columnas-1
        PROCESAR matriz[fila][columna]
    FIN PARA
FIN PARA
```

Por cada fila recorremos sus columnas.

# 4. Traza

Matriz:
```text
[1 2]
[3 4]
```

Orden fila por fila:
```text
(0,0)=1
(0,1)=2
(1,0)=3
(1,1)=4
```

# 5. Suma por fila

```text
PARA cada fila
    suma ← 0
    PARA cada columna
        suma ← suma + matriz[fila][columna]
    FIN PARA
    ESCRIBIR suma
FIN PARA
```

Observa dónde se reinicia suma: una vez por fila.

# 6. Suma por columna

Ahora el ciclo exterior puede recorrer columnas y el interior filas, o mantener otro diseño equivalente.

Pregunta qué dimensión estás resumiendo.

# 7. Diagonal principal

En una matriz cuadrada:
```text
matriz[i][i]
```

Para:
```text
1 2 3
4 5 6
7 8 9
```
diagonal = 1,5,9.

# 8. Transposición

Intercambia filas y columnas:

```text
transpuesta[columna][fila] ← original[fila][columna]
```

Dimensión m×n pasa a n×m.

# 9. Práctica guiada

Con:
```text
4 5 3
3 4 4
5 5 4
```

Calcula:
- promedio de cada estudiante (fila);
- promedio de cada actividad (columna);
- mayor nota y coordenada.

# 10. Errores frecuentes
- intercambiar índices;
- usar dimensiones incorrectas;
- reiniciar acumulador en lugar equivocado;
- asumir matriz cuadrada;
- usar diagonal en matriz no cuadrada sin definir alcance.

# 11. Ejercicios
1. Suma total.
2. Promedio por fila.
3. Mayor por columna.
4. Diagonal.
5. Buscar coordenadas.
6. Transponer.

# 12. Reto
Registro de notas: promedio por estudiante, por actividad y estudiante con mayor promedio. Define empates.

# 13. Autoevaluación
1. ¿Qué representa [fila][columna]?
2. ¿Por qué dos ciclos?
3. ¿Dónde reinicias suma por fila?
4. ¿Qué exige diagonal principal completa?
5. ¿Qué dimensiones tiene una transpuesta?

# 14. Checklist
- [ ] Accedo por coordenadas.
- [ ] Recorro filas/columnas.
- [ ] Agrego por dimensión.
- [ ] No asumo matriz cuadrada.

Continúa con cadenas.
