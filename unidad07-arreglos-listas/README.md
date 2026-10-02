# Unidad 07 — Arreglos, listas y procesamiento secuencial

## Propósito
Procesar múltiples valores relacionados sin crear una variable diferente para cada dato.

## Concepto
```text
notas = [4.2, 3.5, 4.8, 2.9]
```

Cada elemento ocupa una posición.

## Recorrido
```text
PARA CADA nota EN notas HACER
  ESCRIBIR nota
FIN PARA
```

## Patrones fundamentales
### Suma
```text
total ← 0
PARA CADA valor EN datos
  total ← total + valor
FIN PARA
```

### Búsqueda
Recorrer hasta encontrar un elemento que cumpla una condición.

### Conteo
Incrementar un contador cuando un elemento cumple una regla.

### Máximo
Inicializar con un valor existente y comparar los demás.

## Errores frecuentes
- acceder fuera de los límites;
- inicializar máximo en 0 cuando los datos pueden ser negativos;
- modificar una colección mientras se recorre sin comprender el efecto.

## Ejercicios
1. Sumar una lista.
2. Calcular promedio.
3. Encontrar mayor y menor.
4. Contar positivos.
5. Buscar un valor.
6. Crear una nueva lista con los valores pares.

## Reto
Analiza una colección de temperaturas: promedio, máxima, mínima, cantidad sobre el promedio y posición de la primera temperatura máxima.

## Qué sigue
**Unidad 08 — Matrices y datos bidimensionales**
