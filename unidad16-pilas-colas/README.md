# Unidad 16 — Pilas y colas

## Qué aprenderás
Elegir una estructura cuando el orden de entrada/salida es parte esencial del problema.

# 1. Pila — LIFO

Último en entrar, primero en salir.

Platos:
```text
push A
push B
push C

tope → C
       B
       A
```

`pop` devuelve C.

Operaciones conceptuales:
- push;
- pop;
- peek/top;
- isEmpty.

# 2. ¿Dónde aparece?

- deshacer;
- pila de llamadas;
- delimitadores;
- DFS iterativo.

# 3. Paréntesis balanceados

Texto:
```text
(a+[b*c])
```

Cuando abre delimitador → push.

Cuando cierra → debe corresponder con el tope.

Al final la pila debe estar vacía.

No basta contar cantidad de paréntesis:
```text
)( 
```
tiene uno de cada, pero orden inválido.

# 4. Cola — FIFO

Primero en entrar, primero en salir.

```text
entrada → Ana → Luis → Sara → salida
```

Operaciones:
- enqueue;
- dequeue;
- front;
- isEmpty.

# 5. Aplicaciones

- turnos;
- tareas;
- impresión;
- BFS.

# 6. Misma secuencia, distinto resultado

Insertamos A,B,C.

Pila al retirar:
```text
C,B,A
```

Cola:
```text
A,B,C
```

La estructura codifica una política.

# 7. Implementación vs abstracción

Puedes implementar una pila con distintas estructuras internas.

Lo importante aquí es el **comportamiento abstracto** LIFO/FIFO, no confundirlo con una clase concreta de un lenguaje.

# 8. Cola eficiente

Eliminar siempre el primer elemento de un arreglo puede ser costoso en algunas implementaciones/lenguajes. Una cola real puede usar índices o estructuras adecuadas.

Elegir abstracción no elimina decisiones de implementación.

# 9. Práctica guiada

Simula:
```text
push 10
push 20
pop
push 30
peek
pop
```

Haz otra traza usando cola.

# 10. Errores frecuentes
- pop/dequeue sobre estructura vacía sin definir comportamiento.
- Confundir tope/frente.
- Elegir pila cuando se requiere orden de llegada.
- Confundir interfaz abstracta con implementación.

# 11. Ejercicios
1. Simula pila.
2. Invierte secuencia.
3. Delimitadores.
4. Fila de atención.
5. Compara misma secuencia.

# 12. Reto
Diseña simulador de atención. Define eventos, cola, caso vacío y métricas básicas.

# 13. Autoevaluación
1. ¿LIFO?
2. ¿FIFO?
3. ¿Qué hace peek?
4. ¿Por qué contar paréntesis no basta?
5. ¿Qué recorrido usa cola más adelante?

# 14. Checklist
- [ ] Trazo pila.
- [ ] Trazo cola.
- [ ] Elijo según orden.
- [ ] Manejo estructura vacía.

Continúa con conjuntos y mapas.
