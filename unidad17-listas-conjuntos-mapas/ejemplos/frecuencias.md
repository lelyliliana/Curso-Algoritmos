# Problema resuelto — Frecuencia de palabras

Entrada:
```text
sol luna sol mar luna sol
```

Mapa:
```text
sol  → 3
luna → 2
mar  → 1
```

## Algoritmo
```text
frecuencias ← mapa vacío

PARA CADA palabra EN palabras
  SI palabra existe EN frecuencias
    frecuencias[palabra] ← frecuencias[palabra] + 1
  SINO
    frecuencias[palabra] ← 1
  FIN SI
FIN PARA
```

## Idea
La clave representa el elemento; el valor almacena su conteo.

## Pregunta
¿Qué estructura usarías si solo quisieras saber cuáles palabras diferentes existen, sin contar?
