# Unidad 13 — Recursividad

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/algoritmos/)

## Qué aprenderás
Diseñar una solución recursiva con caso base y progreso, trazar la pila de llamadas y comparar con alternativas iterativas.

# 1. Una definición sobre una versión menor

Factorial:
```text
4! = 4 × 3!
3! = 3 × 2!
2! = 2 × 1!
1! = 1
```

La solución usa el mismo problema con una entrada menor.

# 2. Tres ingredientes

Una recursión correcta necesita:
1. caso base;
2. llamada recursiva;
3. progreso hacia el caso base.

Si falta progreso, no termina.

# 3. Factorial

```text
FUNCION factorial(n)
    SI n <= 1
        RETORNAR 1
    FIN SI

    RETORNAR n * factorial(n-1)
FIN FUNCION
```

Para este ejemplo debemos definir el dominio esperado, por ejemplo enteros no negativos.

# 4. Bajar por las llamadas

```text
factorial(4)
→ 4 * factorial(3)
→ 4 * 3 * factorial(2)
→ 4 * 3 * 2 * factorial(1)
→ 4 * 3 * 2 * 1
```

# 5. Volver

Las llamadas pendientes deben recibir el resultado de la siguiente:

```text
factorial(1)=1
factorial(2)=2
factorial(3)=6
factorial(4)=24
```

Consulta el árbol de ejemplo de la unidad.

# 6. Pila de llamadas

Cada llamada conserva contexto hasta poder terminar.

Conceptualmente:
```text
factorial(4)
  factorial(3)
    factorial(2)
      factorial(1)
```

Esto consume memoria de pila.

# 7. Caso base incorrecto

```text
FUNCION cuenta(n)
    RETORNAR cuenta(n-1)
FIN
```

No existe parada.

Incluso con caso base, si llamamos `cuenta(n+1)` partiendo de n positivo, nos alejamos.

# 8. Iterativo vs recursivo

Suma 1..N puede escribirse de ambas formas.

Pregunta:
- ¿cuál expresa mejor la estructura?
- ¿qué profundidad alcanza?
- ¿qué memoria usa?
- ¿el lenguaje optimiza ciertas llamadas? No lo asumas.

# 9. Problemas naturalmente recursivos

Árboles, divide y vencerás, backtracking y ciertas definiciones matemáticas suelen tener estructura recursiva.

Eso no obliga a implementarlos recursivamente en todos los contextos.

# 10. Búsqueda binaria recursiva

Cada llamada trabaja con un intervalo menor. El caso base ocurre cuando:
- encontramos objetivo; o
- el intervalo queda vacío.

Aquí la reducción es evidente.

# 11. Práctica guiada

Traza:
```text
potencia(2,4)
```

Define:
```text
potencia(base,0)=1
potencia(base,n)=base*potencia(base,n-1)
```

Dibuja llamadas y retornos.

# 12. Errores frecuentes
- Sin caso base.
- No acercarse al caso base.
- Confundir llamada con resultado.
- Usar recursividad porque “se ve avanzada”.
- Ignorar profundidad de pila.

# 13. Ejercicios
1. Suma 1..N.
2. Potencia.
3. Contar dígitos.
4. Invertir texto.
5. Binaria recursiva.
6. Traza cada una.

# 14. Reto
Resuelve el mismo problema iterativa y recursivamente. Compara claridad, número de pasos y memoria conceptual.

# 15. Autoevaluación
1. ¿Qué es caso base?
2. ¿Qué significa progreso?
3. ¿Qué conserva la pila?
4. ¿Recursivo siempre es mejor?
5. ¿Por qué árboles suelen prestarse a recursión?

# 16. Checklist
- [ ] Defino caso base.
- [ ] Demuestro progreso.
- [ ] Trazo llamadas/retornos.
- [ ] Comparo con iteración.
- [ ] Considero memoria.

Continúa con análisis experimental.


---


## Caso completo y práctica autodidacta

Consulta el [laboratorio con contrato, traza, programa y resultado esperado](LABORATORIO.md) y las [soluciones razonadas](SOLUCIONES.md).

**Problema de referencia:** Recursividad: factorial con dominio acotado.

## Continuar el curso

- **Unidad anterior:** [Unidad 12 — Merge Sort, Quick Sort y comparación](../unidad12-ordenamiento-avanzado/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 14 — Tiempo, memoria y análisis experimental](../unidad14-analisis-experimental/README.md)

---

### ¿Necesitas apoyo con este tema?

Si te bloqueaste con la práctica, necesitas revisar tu entorno o adaptar lo aprendido a tu proyecto, podemos trabajarlo en una sesión personalizada.

[**Solicitar asesoría para este tema por WhatsApp**](https://wa.me/573103618296?text=Hola%2C%20Leli.%20Estoy%20estudiando%20Unidad%2013.%20Recursividad%20del%20curso%20Algoritmos%20y%20l%C3%B3gica%20de%20programaci%C3%B3n%20%28https%3A%2F%2Fgithub.com%2Flelyliliana%2FCurso-Algoritmos%2Ftree%2Fmain%2Funidad13-recursividad%29%20y%20necesito%20una%20asesor%C3%ADa%20personalizada.%20Mi%20duda%20es%E2%80%A6)
