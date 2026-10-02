# Memoización y tabulación — Fibonacci

## Recursión ingenua
Para calcular F(5), aparecen subproblemas repetidos:

```text
F(5)
├─ F(4)
│  ├─ F(3)
│  └─ F(2)
└─ F(3)
   ├─ F(2)
   └─ F(1)
```

F(3), F(2), etc. se recalculan.

## Memoización
Al calcular F(3), guarda su resultado. La siguiente vez se consulta.

## Tabulación
Construye:
| i | F(i) |
|---:|---:|
| 0 | 0 |
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |
| 4 | 3 |
| 5 | 5 |

## Idea clave
Programación dinámica no significa simplemente "usar una tabla". Deben existir subproblemas y una relación que permita reutilizar resultados.
