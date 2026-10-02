# Unidad 14 — Tiempo, memoria y análisis experimental

## Qué aprenderás
Diseñar experimentos reproducibles, medir distintas dimensiones y separar observación de conclusión.

# 1. ¿Cuál algoritmo es “más rápido”?

Esa pregunta está incompleta.

Necesitamos saber:
- tamaño de entrada;
- datos;
- equipo;
- lenguaje;
- implementación;
- métrica;
- repeticiones.

Una sola medición no establece una ley.

# 2. Tamaño de entrada

Usaremos `n` para representar una dimensión relevante.

Ejemplos:
- cantidad de elementos de una lista;
- cantidad de nodos;
- filas/columnas de una matriz.

Define qué significa n en cada experimento.

# 3. Qué medir

Podemos medir:
- tiempo;
- comparaciones;
- asignaciones/movimientos;
- memoria aproximada;
- profundidad recursiva.

No todas responden la misma pregunta.

# 4. Búsqueda lineal como laboratorio

Lista de n elementos.

Casos:
- objetivo primero;
- centro;
- último;
- inexistente.

Registra comparaciones.

Para n=10, inexistente requiere 10 comparaciones en el algoritmo básico.

Para n=100, 100.

Ya vemos una tendencia sin cronómetro.

# 5. Medir tiempo

El tiempo real incluye ruido:
- procesos del sistema;
- calentamiento del runtime/JIT;
- caché;
- resolución del reloj;
- recolección de memoria;
- equipo.

Por eso repetimos y resumimos apropiadamente.

# 6. Experimento justo

Si comparas A/B:
- mismas entradas;
- misma máquina/entorno;
- misma tarea;
- varias repeticiones;
- tamaños crecientes.

No cambies simultáneamente algoritmo, lenguaje y dataset y atribuyas todo al algoritmo.

# 7. Tabla

| n | algoritmo | comparaciones | tiempo rep1 | rep2 | rep3 |
|---:|---|---:|---:|---:|---:|
| 100 | lineal | 100 | ... | ... | ... |

Conserva datos crudos además del resumen.

# 8. Gráficas

Una gráfica n vs tiempo/operaciones puede revelar tendencia.

Pero una gráfica bonita no corrige un experimento mal diseñado.

# 9. Memoria

Merge Sort puede usar memoria auxiliar; recursividad usa pila; estructuras mantienen datos adicionales.

Optimizar tiempo puede aumentar memoria.

# 10. Observación vs conclusión

Observación:
> En estas pruebas, A tardó menos para n>=10000.

Conclusión prudente:
> Bajo estas condiciones, A mostró mejor tiempo para esos tamaños.

Evita:
> A siempre es mejor.

# 11. Práctica guiada

Compara búsqueda lineal/binaria por número de comparaciones para n=16,32,64,128.

Predice antes.

# 12. Errores frecuentes
- una sola ejecución;
- datasets diferentes;
- n mal definido;
- confundir ms con complejidad;
- ignorar memoria;
- generalizar fuera del experimento.

# 13. Reto
Compara dos algoritmos, crea tabla, gráfica si quieres y redacta resultados separando evidencia e interpretación.

# 14. Autoevaluación
1. ¿Qué es n?
2. ¿Por qué tiempo tiene ruido?
3. ¿Por qué contar operaciones?
4. ¿Qué hace una comparación justa?
5. ¿Observación y regla universal son iguales?

# 15. Checklist
- [ ] Defino n.
- [ ] Defino métricas.
- [ ] Repito.
- [ ] Controlo condiciones.
- [ ] Interpreto prudentemente.

Continúa con Big O.
