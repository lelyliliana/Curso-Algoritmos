# Unidad 18 — Árboles

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/algoritmos/)

## Qué aprenderás
Representar jerarquías, identificar propiedades y trazar recorridos y búsquedas en árboles binarios.

# 1. Jerarquía

```text
raíz
├── documentos
│   ├── tesis
│   └── clases
└── imagenes
```

No es una secuencia lineal: existen relaciones padre-hijo.

# 2. Conceptos

- raíz;
- padre/hijo;
- hoja;
- profundidad;
- altura;
- subárbol.

Aclara la convención al contar altura/profundidad: algunas definiciones cuentan aristas y otras nodos.

# 3. Árbol binario

```text
      A
     / \
    B   C
   / \
  D   E
```

Cada nodo tiene hasta dos hijos.

# 4. Recorridos

Preorden (raíz-izquierda-derecha):
```text
A B D E C
```

Inorden (izquierda-raíz-derecha):
```text
D B E A C
```

Postorden (izquierda-derecha-raíz):
```text
D E B C A
```

Traza las visitas; no memorices solo nombres.

# 5. ¿Por qué distintos?

La tarea define el orden. Procesar padre antes de hijos no es igual que procesar hijos antes del padre.

# 6. Árbol binario de búsqueda (BST)

Regla típica:
```text
menores < nodo < mayores
```

Insertando 8,3,10,1,6:

```text
      8
     / \
    3  10
   / \
  1   6
```

# 7. Buscar 6

```text
6 < 8 → izquierda
6 > 3 → derecha
encontrado
```

Aprovechamos la propiedad de orden.

# 8. La forma importa

Insertar 1,2,3,4,5 en un BST simple puede producir:

```text
1
 \
  2
   \
    3
     \
      4
```

Se aproxima a una lista. “Es árbol” no garantiza costo logarítmico.

# 9. Balance

AVL, Red-Black y otras estructuras mantienen propiedades de balance mediante trabajo adicional. Aquí basta comprender por qué importa.

# 10. Práctica guiada

Inserta:
```text
8,3,10,1,6,14,4,7,13
```

Dibuja y obtiene pre/in/postorden.

# 11. Errores frecuentes
- Árbol binario = BST.
- Asumir balance.
- Mezclar convenciones de altura.
- Memorizar recorridos sin trazarlos.

# 12. Ejercicios
Raíz/hojas, recorridos, inserción, búsqueda y comparación equilibrado/degenerado.

# 13. Reto
Representa catálogo jerárquico y elige recorrido para mostrarlo. Justifica.

# 14. Autoevaluación
1. ¿Binario y BST son iguales?
2. ¿Qué visita primero preorden?
3. ¿Por qué inorden de BST produce orden bajo la regla usual?
4. ¿Por qué forma afecta costo?
5. ¿Qué es hoja?

# 15. Checklist
- [ ] Dibujo árboles.
- [ ] Trazo recorridos.
- [ ] Inserto/busco BST.
- [ ] No asumo balance.

Continúa con grafos.


---

## Continuar el curso

- **Unidad anterior:** [Unidad 17 — Listas, conjuntos y mapas](../unidad17-listas-conjuntos-mapas/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 19 — Grafos, BFS y DFS](../unidad19-grafos/README.md)

---

### ¿Necesitas apoyo con este tema?

Si te bloqueaste con la práctica, necesitas revisar tu entorno o adaptar lo aprendido a tu proyecto, podemos trabajarlo en una sesión personalizada.

[**Solicitar asesoría para este tema por WhatsApp**](https://wa.me/573103618296?text=Hola%2C%20Leli.%20Estoy%20estudiando%20Unidad%2018.%20Introducci%C3%B3n%20a%20%C3%A1rboles%20del%20curso%20Algoritmos%20y%20l%C3%B3gica%20de%20programaci%C3%B3n%20%28https%3A%2F%2Fgithub.com%2Flelyliliana%2FCurso-Algoritmos%2Ftree%2Fmain%2Funidad18-arboles%29%20y%20necesito%20una%20asesor%C3%ADa%20personalizada.%20Mi%20duda%20es%E2%80%A6)
