# Unidad 20 — Divide y vencerás

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
