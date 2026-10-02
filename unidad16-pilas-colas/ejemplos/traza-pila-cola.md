# Trazado visual — Pila y cola

## Misma secuencia de entrada
Insertamos:
```text
A, B, C
```

## Pila — LIFO
Después de push:
```text
tope
 ↓
[C]
[B]
[A]
```

Extracciones:
```text
pop → C
pop → B
pop → A
```

## Cola — FIFO
```text
frente → [A][B][C] ← final
```

Extracciones:
```text
dequeue → A
dequeue → B
dequeue → C
```

## Decisión
Si necesitas atender en orden de llegada, una pila contradice el requisito.
