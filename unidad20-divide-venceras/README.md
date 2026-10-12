# Unidad 20 — Divide y vencerás

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/algoritmos/)

## Qué aprenderás
Reconocer problemas divisibles, definir caso base, resolver subproblemas y combinar resultados.

# 1. Patrón

```text
problema
├── subproblema A
└── subproblema B
       ↓
resolver
       ↓
combinar
```

No basta dividir: debemos poder obtener la solución original a partir de las partes.

# 2. Ya lo conoces

**Búsqueda binaria:** conserva solo una mitad.

**Merge Sort:** resuelve ambas mitades y las mezcla.

**Quick Sort:** particiona y resuelve particiones.

La combinación no tiene que ser igual en todos.

# 3. Máximo por mitades

Lista:
```text
[7,2,9,4,1,8]
```

Dividimos:
```text
[7,2,9]  [4,1,8]
```

Máximos:
```text
9 y 8
```

Combinamos:
```text
max(9,8)=9
```

# 4. Caso base

Una colección de un elemento:
```text
maximo([x]) = x
```

Sin caso base no termina.

# 5. Pseudocódigo conceptual

```text
FUNCION maximo(datos,inicio,fin)
    SI inicio = fin
        RETORNAR datos[inicio]
    FIN SI

    medio ← ...
    izq ← maximo(datos,inicio,medio)
    der ← maximo(datos,medio+1,fin)

    RETORNAR mayor(izq,der)
FIN
```

# 6. ¿Siempre conviene?

Para hallar máximo, un recorrido lineal es más simple y óptimo asintóticamente.

Divide y vencerás aquí sirve para aprender la estrategia, no porque sea necesariamente la mejor implementación secuencial.

# 7. Recurrencia intuitiva

Podemos describir trabajo:
```text
T(n) = 2T(n/2) + trabajo_de_combinar
```

No necesitas resolver formalmente todas las recurrencias todavía; úsala para visualizar de dónde proviene el costo.

# 8. Práctica guiada

Traza máximo por mitades con 8 elementos. Dibuja árbol de llamadas y combinación.

# 9. Errores frecuentes
- Dividir sin saber combinar.
- Subproblemas que no se hacen menores.
- Caso base incorrecto.
- Asumir que divide y vencerás siempre mejora.
- Confundir con programación dinámica: aquí los subproblemas suelen ser independientes/no se reutilizan de la misma forma.

# 10. Ejercicios
Explica binaria, Merge, máximo y suma por mitades.

# 11. Reto
Diseña una solución divide-y-vencerás y compárala con alternativa directa.

# 12. Autoevaluación
1. ¿Cuáles son las etapas?
2. ¿Qué hace caso base?
3. ¿Cómo combina Merge?
4. ¿Máximo por mitades es necesariamente mejor?
5. ¿Qué debe pasar con tamaño de subproblemas?

# 13. Checklist
- [ ] Identifico división.
- [ ] Defino base.
- [ ] Defino combinación.
- [ ] Comparo alternativa.

Continúa con greedy.


---

## Continuar el curso

- **Unidad anterior:** [Unidad 19 — Grafos, BFS y DFS](../unidad19-grafos/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 21 — Algoritmos voraces (Greedy)](../unidad21-greedy/README.md)

---

### ¿Necesitas apoyo con este tema?

Si te bloqueaste con la práctica, necesitas revisar tu entorno o adaptar lo aprendido a tu proyecto, podemos trabajarlo en una sesión personalizada.

[**Solicitar asesoría para este tema por WhatsApp**](https://wa.me/573103618296?text=Hola%2C%20Leli.%20Estoy%20estudiando%20Unidad%2020.%20Divide%20y%20vencer%C3%A1s%20del%20curso%20Algoritmos%20y%20l%C3%B3gica%20de%20programaci%C3%B3n%20%28https%3A%2F%2Fgithub.com%2Flelyliliana%2FCurso-Algoritmos%2Ftree%2Fmain%2Funidad20-divide-venceras%29%20y%20necesito%20una%20asesor%C3%ADa%20personalizada.%20Mi%20duda%20es%E2%80%A6)
