# Unidad 05 — Ciclos, contadores, acumuladores y centinelas

## Qué aprenderás
Reconocer cuándo repetir, elegir una repetición apropiada, utilizar contadores/acumuladores y evitar ciclos infinitos.

# 1. El problema de copiar instrucciones

Mostrar 1 a 5 podría escribirse:
```text
ESCRIBIR 1
ESCRIBIR 2
...
```

¿Y 1 a 10 000?

Necesitamos expresar **la repetición**, no copiar el trabajo.

# 2. Cuando conocemos la cantidad

```text
PARA i ← 1 HASTA 5 HACER
    ESCRIBIR i
FIN PARA
```

Traza:

| iteración | i | salida |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| ... | ... | ... |
| 5 | 5 | 5 |

# 3. Cuando no conocemos cuántas veces

```text
MIENTRAS saldo > 0 HACER
    ...
FIN MIENTRAS
```

La repetición depende de una condición.

Pregunta fundamental:
> ¿qué puede hacer que la condición cambie?

# 4. Contador

Cuenta eventos.

```text
cantidadAprobados ← cantidadAprobados + 1
```

Debe inicializarse antes.

# 5. Acumulador

Suma valores.

```text
totalVentas ← totalVentas + venta
```

Inicialmente suele ser 0 para suma.

# 6. Contador ≠ acumulador

Datos: 10,20,30.

Después de procesarlos:
```text
contador = 3
acumulador = 60
```

Uno cuenta elementos; otro acumula sus valores.

# 7. Centinela

No sabemos cuántas notas llegarán. -1 significa terminar:

```text
LEER nota
MIENTRAS nota ≠ -1 HACER
    total ← total + nota
    cantidad ← cantidad + 1
    LEER nota
FIN MIENTRAS
```

El -1 **no forma parte de los datos**.

# 8. Promedio y caso vacío

```text
SI cantidad > 0 ENTONCES
    promedio ← total / cantidad
SINO
    ESCRIBIR "No hay datos"
FIN SI
```

Evita división entre cero.

# 9. Mayor y menor

No inicialices el mayor arbitrariamente en 0 si los datos pueden ser negativos.

Una estrategia:
- leer el primer dato válido;
- usarlo para inicializar mayor/menor;
- procesar los siguientes.

# 10. Validación repetitiva

```text
LEER edad
MIENTRAS edad < 0 HACER
    ESCRIBIR "Dato inválido"
    LEER edad
FIN MIENTRAS
```

# 11. Ciclo infinito

```text
x ← 1
MIENTRAS x <= 10 HACER
    ESCRIBIR x
FIN MIENTRAS
```

x nunca cambia.

Corrección:
```text
x ← x + 1
```

# 12. Ejemplo resuelto — estadísticas

Objetivo: leer N valores y obtener suma, promedio, mayor y menor.

Primero valida N > 0. Lee el primer valor para inicializar suma/mayor/menor y después procesa los restantes.

Esta estrategia evita inventar valores iniciales.

Consulta `ejemplos/problema-resuelto-estadisticas.md`.

# 13. Prueba de escritorio

Para ciclos usa columnas:
```text
iteración | dato | contador | acumulador | mayor | menor
```

No intentes seguir cinco variables mentalmente.

# 14. Errores frecuentes
- No inicializar.
- Actualizar contador fuera/dentro del lugar incorrecto.
- Incluir centinela en cálculos.
- Dividir entre cero.
- Inicializar mayor en 0 sin justificar.
- No modificar condición del MIENTRAS.

# 15. Ejercicios
1. Tabla de multiplicar.
2. Suma 1..N.
3. Factorial iterativo.
4. Contar pares.
5. Promedio de N notas.
6. Leer hasta 0.
7. Mayor/menor.
8. Validar entrada hasta ser correcta.

# 16. Reto — Estadísticas de ventas
Lee ventas hasta centinela y calcula:
- cantidad;
- total;
- promedio;
- mayor;
- menor.

Define qué ocurre si no se registra ninguna venta y realiza una tabla de traza.

# 17. Autoevaluación
1. ¿Cuándo PARA?
2. ¿Cuándo MIENTRAS?
3. ¿Contador vs acumulador?
4. ¿Qué es centinela?
5. ¿Cómo evitas incluirlo?
6. ¿Por qué mayor=0 puede ser incorrecto?
7. ¿Qué causa un ciclo infinito?

# 18. Checklist
- [ ] Elijo tipo de repetición.
- [ ] Inicializo correctamente.
- [ ] Trazo variables.
- [ ] Manejo caso vacío.
- [ ] Evito ciclos infinitos.

Continúa con funciones.
