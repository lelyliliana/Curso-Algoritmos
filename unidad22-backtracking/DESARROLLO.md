# Backtracking: el estado debe volver a ser el mismo

[Laboratorio y programas](LABORATORIO.md) · [Soluciones](SOLUCIONES.md)

## Un problema con alternativas

Tenemos valores 2,3,5 y objetivo 5. Cada elemento puede utilizarse una vez. Queremos todas las selecciones que alcanzan el objetivo, expresadas mediante sus **índices**, para distinguir elementos aunque tengan el mismo valor.

En cada posición hay dos decisiones: incluirla o no incluirla. Un recorrido sistemático permite explorar ambas sin olvidar cómo llegamos al estado actual.

El estado de una llamada tiene tres partes: posición pendiente, suma de lo elegido y lista de índices elegidos. No basta conservar solo la suma si necesitamos reconstruir qué elementos la producen.

## Seguir una rama

| Paso | Posición pendiente | Índices elegidos | Suma | Acción |
|---|---:|---|---:|---|
|1|0|[]|0|incluir índice 0, valor 2|
|2|1|[0]|2|incluir índice 1, valor 3|
|3|2|[0,1]|5|guardar solución|
|4|1|[0]|2|deshacer inclusión de 1|
|5|2|[0]|2|probar rama sin 1|
|6|3|[0,2]|7|podar: excede objetivo|

Guardar la solución exige copiar la lista. Si almacenáramos la misma referencia mutable, al retirar elementos podríamos modificar también las soluciones que ya habíamos encontrado.

Al terminar la rama que empieza con índice 0, lo retiramos y exploramos sin él. La rama que omite 0 y 1 y elige 2 produce suma 5 e índices[2]. Las dos soluciones son[0,1] y[2].

## Escoger, explorar, deshacer

```text
explorar(i,suma):
    SI suma = objetivo:
        GUARDAR copia de elegidos
        RETORNAR
    SI no quedan valores O suma > objetivo:
        RETORNAR

    AÑADIR i a elegidos
    explorar(i+1,suma+valores[i])
    RETIRAR último índice

    explorar(i+1,suma)
```

La instrucción de retirar restaura el estado compartido antes de probar la alternativa. La suma se pasa como otro valor a cada llamada; la lista elegidos es la que sí se modifica y necesita restauración.

Una invariante útil: al entrar en una llamada, los índices elegidos pertenecen a posiciones anteriores a i y sus valores suman exactamente la suma indicada. Si esa relación se rompe, una salida puede parecer correcta por casualidad y fallar con otra entrada.

## Cuándo la poda es válida

El contrato exige valores estrictamente positivos. Si la suma supera el objetivo, añadir más valores no puede reducirla: la rama ya no puede dar una solución. Por eso podemos cortarla.

Si permitimos negativos, esa conclusión deja de ser válida. Una suma de 7 podría bajar a 5 al elegir−2. Cambiar el dominio obliga a revisar la poda y los casos base; no basta retirar una validación y conservar todo el algoritmo.

El objetivo 0 tiene una solución: la selección vacía. Con valores positivos no existe otra selección no vacía que sume 0, por lo que retornar al encontrarlo es correcto en este dominio.

## Repetidos y unicidad

Con valores[1,1] y objetivo 1 encontramos índices[0] y[1]. Son dos selecciones de elementos diferentes. Si el problema pidiera combinaciones de valores sin distinguir objetos, tendrías que cambiar el contrato y definir cómo eliminar duplicados.

No confundas duplicados de una representación con soluciones distintas del problema. Las pruebas comparan conjuntos de tuplas de índices y además comprueban que la implementación no repita la misma tupla.

## Costos reales

En el peor caso hay una decisión binaria por elemento: hastaO(2^n) ramas. La poda mejora algunos casos, pero no elimina esa cota de manera general. La profundidad y la lista de elección sonO(n); el conjunto de soluciones puede ser exponencial y ocupa espacio adicional proporcional a lo que devuelve.

La prueba independiente enumera máscaras de selección pequeñas y calcula su suma. No utiliza la misma poda ni el mismo árbol recursivo: sirve para detectar una omisión o una repetición en backtracking.

**Práctica:** elimina temporalmente pop en una copia, predice qué invariante romperás y utiliza[2,3,5] para observarlo. Restaura la versión correcta antes de continuar. Después compara con una variante que crea una lista nueva en cada rama y explica el costo de esas copias.
