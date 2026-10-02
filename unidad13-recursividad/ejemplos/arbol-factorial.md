# Traza — Pila recursiva

```text
factorial(4)
└─ 4 * factorial(3)
       └─ 3 * factorial(2)
              └─ 2 * factorial(1)
                     └─ 1
```

## Descenso
Se crean llamadas pendientes.

## Retorno
```text
factorial(1) = 1
factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 = 6
factorial(4) = 4 * 6 = 24
```

## Idea clave
La llamada anterior no desaparece: queda pendiente hasta recibir el resultado de la siguiente.

## Error clásico
Sin caso base o sin acercarse a él, la recursión no termina correctamente.
