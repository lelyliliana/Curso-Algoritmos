# Unidad 22 — Backtracking

## Propósito
Explorar posibilidades y retroceder cuando una decisión parcial ya no puede producir una solución válida.

```text
elegir
  ↓
explorar
  ↓
¿sirve?
 ↙     ↘
sí      no
        ↓
     retroceder
```

## Componentes
- estado parcial;
- opciones;
- condición de validez;
- caso solución;
- acción de deshacer.

## Problemas típicos
- laberintos;
- combinaciones;
- permutaciones;
- N reinas;
- Sudoku simplificado.

## Poda
Si sabemos que un estado no puede conducir a una solución, dejamos de explorarlo.

## Ejercicios
1. Genera combinaciones.
2. Traza un laberinto pequeño.
3. Genera permutaciones de tres elementos.
4. Identifica puntos de retroceso.

## Reto
Diseña un solucionador para un pequeño problema de asignación con restricciones. Dibuja parte del árbol de búsqueda y muestra dónde ocurre la poda.

## Qué sigue
**Unidad 23 — Programación dinámica**
