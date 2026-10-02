# Unidad 04 — Decisiones y lógica booleana

## Qué aprenderás
Diseñar algoritmos que eligen caminos, construir condiciones correctas, combinar reglas y probar valores límite.

## Antes de empezar
Debes comprender variables, expresiones y operadores relacionales.

# 1. Un algoritmo no siempre hace lo mismo

Problema:
> Permitir entrada si una persona tiene al menos 18 años.

Para edad 20 hacemos una cosa; para edad 15, otra.

Necesitamos una **decisión**.

# 2. Condición

```text
edad >= 18
```

No produce un número: produce VERDADERO o FALSO.

| edad | edad >= 18 |
|---:|---|
| 17 | FALSO |
| 18 | VERDADERO |
| 25 | VERDADERO |

El valor 18 es un **caso límite** importante.

# 3. Decisión simple

```text
SI temperatura > 30 ENTONCES
    ESCRIBIR "Hace calor"
FIN SI
```

Si la condición es falsa, el bloque simplemente no se ejecuta.

# 4. Decisión doble

```text
SI edad >= 18 ENTONCES
    ESCRIBIR "Mayor de edad"
SINO
    ESCRIBIR "Menor de edad"
FIN SI
```

Exactamente uno de los caminos se ejecuta.

# 5. Decisiones múltiples

Clasificar nota:

```text
SI nota >= 4.5 ENTONCES
    nivel ← "Excelente"
SINO SI nota >= 3 ENTONCES
    nivel ← "Aprobado"
SINO
    nivel ← "No aprobado"
FIN SI
```

## ¿Por qué importa el orden?

Si comprobáramos primero:
```text
nota >= 3
```
una nota 4.8 entraría allí y nunca llegaría a “Excelente”.

# 6. Condiciones compuestas

```text
edad >= 18 Y tieneDocumento
```

Para entrar, ambas deben ser verdaderas.

### Y
| A | B | A Y B |
|---|---|---|
| F | F | F |
| F | V | F |
| V | F | F |
| V | V | V |

### O
Es verdadero cuando al menos una condición es verdadera.

### NO
Invierte el valor lógico.

# 7. Traducir lenguaje natural

> Puede recibir descuento si es estudiante **o** tiene más de 65 años.

```text
esEstudiante O edad > 65
```

> Puede ingresar si es mayor de edad **y** tiene entrada.

```text
edad >= 18 Y tieneEntrada
```

No programes hasta poder escribir la regla claramente.

# 8. Paréntesis

```text
esClientePremium O (compra >= 100000 Y tieneCupon)
```

Los paréntesis dejan clara la intención.

# 9. Ejemplo resuelto — descuento

Reglas:
- compra < 100000: 0%;
- 100000 a <200000: 5%;
- >=200000: 10%.

```text
SI compra >= 200000 ENTONCES
    descuento ← 0.10
SINO SI compra >= 100000 ENTONCES
    descuento ← 0.05
SINO
    descuento ← 0
FIN SI

total ← compra * (1 - descuento)
```

## Pruebas
| compra | descuento |
|---:|---:|
| 99999 | 0% |
| 100000 | 5% |
| 199999 | 5% |
| 200000 | 10% |

Los límites revelan errores mejor que probar solo 150000.

# 10. Condiciones solapadas

Reglas mal diseñadas:
- niño: edad <= 12;
- adolescente: edad >= 12 y <=17.

Edad 12 pertenece a ambas.

Antes de escribir SI, corrige la definición.

# 11. Validación

Si nota debe estar entre 0 y 5:

```text
SI nota < 0 O nota > 5 ENTONCES
    ESCRIBIR "Nota inválida"
SINO
    // clasificar
FIN SI
```

Primero protege el dominio; luego aplica reglas.

# 12. Prueba de escritorio

Para cada decisión registra:
- entrada;
- condición evaluada;
- resultado lógico;
- camino ejecutado;
- salida.

# 13. Errores frecuentes
- Usar > cuando el límite requiere >=.
- Ordenar mal condiciones múltiples.
- Crear reglas solapadas.
- No validar entrada.
- Escribir condiciones tan complejas que nadie puede explicarlas.

# 14. Ejercicios graduados

## Básicos
1. Positivo, negativo o cero.
2. Par/impar.
3. Mayor de dos.

## Intermedios
4. Mayor de tres.
5. Clasificación de nota con validación.
6. Año bisiesto.

## Aplicación
7. Tarifa por edad y horario.
8. Acceso según edad, documento y autorización.

# 15. Reto — Tarifa de envío

Define una tarifa según:
- peso;
- zona;
- urgencia.

Tu solución debe:
1. escribir reglas sin solapamientos;
2. validar datos;
3. identificar límites;
4. crear pseudocódigo;
5. probar al menos seis casos, incluidos límites.

# 16. Autoevaluación
1. ¿Qué produce una condición?
2. ¿Cuándo usar decisión doble?
3. ¿Por qué importa el orden?
4. ¿Qué diferencia hay entre Y y O?
5. ¿Qué es un caso límite?
6. ¿Qué es una regla solapada?

# 17. Checklist
- [ ] Traduzco reglas a condiciones.
- [ ] Manejo límites.
- [ ] Combino condiciones.
- [ ] Evito solapamientos.
- [ ] Pruebo casos normales, límite e inválidos.

Continúa con ciclos.
