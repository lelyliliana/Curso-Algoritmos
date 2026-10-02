# Unidad 07 — Arreglos, listas y procesamiento secuencial

## Qué aprenderás
Representar colecciones, recorrerlas, trabajar con índices y reconocer patrones de suma, conteo, búsqueda, máximo y transformación.

# 1. El problema

Para cuatro notas podríamos crear:
```text
nota1, nota2, nota3, nota4
```

¿Y para 500?

Una colección permite tratar valores relacionados como una unidad:

```text
notas = [4.2, 3.5, 4.8, 2.9]
```

# 2. Posiciones e índices

En muchos lenguajes los índices comienzan en 0:

```text
índice:  0    1    2    3
valor:  4.2  3.5  4.8  2.9
```

Con 4 elementos, el último índice es 3.

Esta diferencia entre **cantidad** e **índice máximo** provoca muchos errores.

# 3. Recorrer por valor

```text
PARA CADA nota EN notas HACER
    ESCRIBIR nota
FIN PARA
```

Útil cuando no necesitas conocer la posición.

# 4. Recorrer por índice

```text
PARA i ← 0 HASTA longitud(notas)-1 HACER
    ESCRIBIR i, notas[i]
FIN PARA
```

Necesario cuando la posición forma parte de la respuesta.

# 5. Patrón: suma

```text
total ← 0
PARA CADA valor EN datos HACER
    total ← total + valor
FIN PARA
```

# 6. Patrón: conteo

```text
positivos ← 0
PARA CADA valor EN datos HACER
    SI valor > 0 ENTONCES
        positivos ← positivos + 1
    FIN SI
FIN PARA
```

# 7. Patrón: máximo

Si la colección no está vacía:

```text
mayor ← datos[0]

PARA i ← 1 HASTA longitud(datos)-1 HACER
    SI datos[i] > mayor ENTONCES
        mayor ← datos[i]
    FIN SI
FIN PARA
```

Esto funciona incluso si todos los números son negativos.

# 8. Patrón: transformación

Entrada:
```text
[1,2,3,4,5]
```

Queremos otra colección con pares:

```text
pares ← lista vacía

PARA CADA valor EN datos
    SI valor MOD 2 = 0
        AGREGAR valor A pares
    FIN SI
FIN PARA
```

Resultado:
```text
[2,4]
```

# 9. Buscar valor

Recorre hasta encontrarlo o terminar. En la Unidad 10 formalizaremos búsqueda lineal y binaria.

# 10. Colección vacía

Preguntas como máximo/promedio requieren decidir qué hacer si no hay elementos.

No accedas `datos[0]` sin comprobar que existe.

# 11. Modificar mientras recorres

Eliminar/agregar elementos durante un recorrido puede cambiar índices o iteradores según la estructura/lenguaje.

Como principiante, evita hacerlo hasta comprender la semántica concreta.

# 12. Práctica guiada

Temperaturas:
```text
[28,31,29,35,30]
```

Calcula manualmente:
- suma;
- promedio;
- máxima;
- posición de la máxima;
- cuántas superan 30.

Construye una tabla de traza por iteración.

# 13. Errores frecuentes
- índice fuera de rango;
- confundir longitud con último índice;
- máximo inicializado en 0;
- dividir entre cero con colección vacía;
- perder la posición cuando el problema la necesita.

# 14. Ejercicios
1. Suma.
2. Promedio.
3. Mayor/menor.
4. Contar positivos.
5. Primera aparición.
6. Crear lista de pares.
7. Contar valores mayores al promedio.

# 15. Reto
Analiza temperaturas: promedio, máxima, mínima, cantidad sobre promedio y posición de la primera máxima.

# 16. Autoevaluación
1. ¿Longitud 5 implica último índice 5?
2. ¿Cuándo recorrer por índice?
3. ¿Cómo inicializar máximo?
4. ¿Qué es acumulador?
5. ¿Qué haces con colección vacía?

# 17. Checklist
- [ ] Recorro colecciones.
- [ ] Manejo índices.
- [ ] Reconozco patrones.
- [ ] Manejo colección vacía.
- [ ] Trazo el algoritmo.

Continúa con matrices.
