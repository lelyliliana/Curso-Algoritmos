# Unidad 03 — Datos, variables, operadores y expresiones

## Propósito
Aprender a representar información dentro de un algoritmo y construir expresiones correctas antes de implementar una solución.

## Objetivos
- Distinguir datos, variables y constantes.
- Reconocer números, texto y valores lógicos.
- Utilizar operadores aritméticos, relacionales y lógicos.
- Comprender precedencia y uso de paréntesis.
- Traducir expresiones entre pseudocódigo, Python, Java y JavaScript.

## 1. Datos y variables
Una variable representa un espacio lógico cuyo valor puede cambiar.

```text
edad ← 20
nombre ← "Laura"
activo ← VERDADERO
```

Una constante representa un valor que conceptualmente no debería cambiar durante el algoritmo.

```text
PI ← 3.1416
```

## 2. Tipos de información
Trabajaremos inicialmente con:
- enteros;
- reales;
- texto;
- caracteres;
- booleanos.

Elegir correctamente el tipo evita operaciones sin sentido.

## 3. Operadores aritméticos
```text
+ suma
- resta
* multiplicación
/ división
DIV división entera
MOD residuo
```

Ejemplo:
```text
total ← precio * cantidad
resto ← numero MOD 2
```

## 4. Operadores relacionales
```text
>  <  >=  <=  =  ≠
```
Una comparación produce VERDADERO o FALSO.

## 5. Operadores lógicos
```text
Y
O
NO
```

Ejemplo:
```text
puedeEntrar ← edad >= 18 Y tieneEntrada
```

## 6. Precedencia
No dependas de recordar reglas cuando una expresión pueda ser ambigua. Usa paréntesis.

Incorrecto para un promedio:
```text
promedio ← n1 + n2 + n3 / 3
```

Claro:
```text
promedio ← (n1 + n2 + n3) / 3
```

## 7. Una idea, varios lenguajes
Pseudocódigo:
```text
area ← base * altura
```
Python:
```python
area = base * altura
```
Java:
```java
double area = base * altura;
```
JavaScript:
```javascript
const area = base * altura;
```

La sintaxis cambia. La operación algorítmica es la misma.

## 8. Ejemplo completo
Problema: convertir segundos totales en minutos y segundos.

```text
INICIO
  LEER totalSegundos
  minutos ← totalSegundos DIV 60
  segundos ← totalSegundos MOD 60
  ESCRIBIR minutos, segundos
FIN
```

Para 145 segundos:
```text
minutos = 2
segundos = 25
```

## Errores frecuentes
- usar una variable antes de asignarla;
- mezclar texto y números sin intención;
- olvidar paréntesis;
- confundir asignación con comparación;
- realizar división entera cuando se necesita decimal.

## Ejercicios
1. Convertir centímetros a metros.
2. Calcular área y perímetro de un círculo.
3. Calcular salario semanal a partir de horas y valor por hora.
4. Extraer horas, minutos y segundos de una cantidad total de segundos.
5. Determinar mediante una expresión lógica si una edad pertenece al rango 18–60.

## Reto
Diseña un algoritmo que calcule el costo de un viaje conociendo distancia, rendimiento del vehículo, precio del combustible y peajes. Define datos, tipos, expresiones y restricciones. Realiza dos pruebas de escritorio.

## Lista de comprobación
- [ ] Cada variable tiene un propósito claro.
- [ ] Elegí tipos adecuados.
- [ ] Las expresiones respetan el orden esperado.
- [ ] Utilicé paréntesis cuando mejoran claridad.
- [ ] Probé los cálculos manualmente.

## Qué sigue
**Unidad 04 — Decisiones y lógica booleana**
