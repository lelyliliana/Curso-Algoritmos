# Unidad 23 — Programación dinámica

## Qué aprenderás
Detectar subproblemas repetidos, definir estado/transición y resolver mediante memoización o tabulación.

# 1. El problema de repetir trabajo

Fibonacci ingenuo:

```text
fib(5)
├── fib(4)
│   ├── fib(3)
│   └── fib(2)
└── fib(3)
```

`fib(3)` se calcula más de una vez.

Eso es un **subproblema superpuesto**.

# 2. No toda recursión es DP

Para aplicar programación dinámica buscamos típicamente:
- subproblemas superpuestos;
- una estructura de solución donde respuestas de subproblemas permitan construir la solución mayor (optimal substructure en problemas de optimización, o relación equivalente en conteo).

# 3. Estado

El estado debe contener la información mínima necesaria para definir un subproblema.

Fibonacci:
```text
estado = n
```

Escaleras:
```text
estado = escalón actual/restante
```

En problemas más complejos puede tener varias dimensiones.

# 4. Transición

Fibonacci:
```text
F(n)=F(n-1)+F(n-2)
```

La transición relaciona estados.

# 5. Casos base

```text
F(0)=0
F(1)=1
```

Sin bases, no construimos soluciones.

# 6. Memoización — top-down

```text
FUNCION fib(n)
    SI n está en memo
        RETORNAR memo[n]
    SI n <= 1
        RETORNAR n

    memo[n] ← fib(n-1)+fib(n-2)
    RETORNAR memo[n]
FIN
```

Calcula bajo demanda y guarda.

# 7. Tabulación — bottom-up

```text
tabla[0] ← 0
tabla[1] ← 1

PARA i ← 2 HASTA n
    tabla[i] ← tabla[i-1]+tabla[i-2]
FIN
```

Construye en un orden donde dependencias ya existen.

# 8. Fibonacci es solo la puerta

Es didáctico, pero DP también aparece en:
- caminos;
- selección/optimización;
- secuencias;
- conteo;
- particiones.

La dificultad real suele ser definir el estado.

# 9. Escaleras

Puedes subir 1 o 2 escalones.

Formas de llegar a n:
```text
formas(n)=formas(n-1)+formas(n-2)
```

¿Por qué? El último salto vino desde n-1 o n-2.

Aquí derivamos la transición desde la estructura del problema.

# 10. Reconstruir solución

En problemas de optimización, obtener solo el valor óptimo puede no bastar. Puede ser necesario guardar decisiones/predecesores para reconstruir qué opciones formaron la solución.

# 11. Memoria

A veces una tabla completa puede reducirse si el estado actual depende solo de pocos estados anteriores.

Optimiza memoria **después** de comprender la transición.

# 12. Práctica guiada

Escaleras n=5:
1. define estados 0..5;
2. casos base;
3. llena tabla;
4. explica cada celda.

# 13. Errores frecuentes
- Aplicar DP porque hay recursión.
- Estado incompleto.
- Transición sin justificar.
- Orden de tabulación antes de dependencias.
- Optimizar memoria demasiado pronto.

# 14. Ejercicios
Fibonacci memo/tab, escaleras, suma mínima en cuadrícula y conteo sencillo.

# 15. Reto
Resuelve un problema pequeño por exploración recursiva y después reutiliza subproblemas. Compara llamadas/estados.

# 16. Autoevaluación
1. ¿Qué es estado?
2. ¿Qué es transición?
3. ¿Memo vs tabulación?
4. ¿Toda recursión es DP?
5. ¿Por qué Fibonacci repite?
6. ¿Cuándo guardar decisiones?

# 17. Checklist
- [ ] Detecto repetición.
- [ ] Defino estado.
- [ ] Derivo transición.
- [ ] Defino bases.
- [ ] Elijo memo/tabulación.
- [ ] Puedo reconstruir si hace falta.

Continúa con taller integrador.
