# Visualización — Árbol de backtracking

Problema simplificado: elegir números de `[2,3,5]` que sumen 5.

```text
                    suma 0
                 /    |    \
              +2     +3     +5
              /       \      ✓
           +3          +2
            ✓           ✓
```

Una exploración real debe definir:
- si cada elemento puede usarse una vez;
- si el orden crea soluciones diferentes;
- cuándo una rama ya no puede servir.

## Poda
Si todos los números son positivos y la suma parcial supera 5, esa rama puede descartarse.

## Idea
Backtracking no es "probar al azar". Es exploración sistemática con decisiones, validación y retroceso.
