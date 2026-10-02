# Unidad 10 — Búsqueda lineal y búsqueda binaria

## Propósito
Comprender dos estrategias para localizar información y analizar cuándo puede utilizarse cada una.

## Búsqueda lineal
Examina elementos uno por uno.

```text
FUNCION buscar(datos, objetivo)
  PARA i ← 0 HASTA longitud(datos)-1
    SI datos[i] = objetivo
      RETORNAR i
    FIN SI
  FIN PARA
  RETORNAR -1
FIN FUNCION
```

Funciona aunque los datos no estén ordenados.

## Búsqueda binaria
Requiere datos ordenados. Compara con el elemento central y descarta aproximadamente la mitad restante en cada paso.

```text
izquierda ← 0
derecha ← longitud(datos)-1

MIENTRAS izquierda <= derecha
  medio ← (izquierda + derecha) DIV 2
  SI datos[medio] = objetivo
    RETORNAR medio
  SINO SI datos[medio] < objetivo
    izquierda ← medio + 1
  SINO
    derecha ← medio - 1
  FIN SI
FIN MIENTRAS
RETORNAR -1
```

## Comparación
| Aspecto | Lineal | Binaria |
|---|---|---|
| Requiere orden | No | Sí |
| Estrategia | recorrer | dividir |
| Peor caso | revisa todos | reduce a la mitad |

## Ejercicios
1. Traza búsqueda lineal.
2. Cuenta comparaciones.
3. Traza búsqueda binaria en 16 elementos.
4. Busca primer valor que cumpla una condición.
5. Explica por qué no debes aplicar binaria directamente sobre datos desordenados.

## Reto
Construye un experimento que compare número de comparaciones de ambas búsquedas para colecciones de distintos tamaños.

## Qué sigue
**Unidad 11 — Algoritmos de ordenamiento básicos**
