# Unidad 04 — Decisiones y lógica booleana

## Propósito
Diseñar algoritmos capaces de elegir entre diferentes caminos según los datos.

## 1. Condición
Una condición produce VERDADERO o FALSO.

```text
edad >= 18
nota >= 3
saldo > 0
```

## 2. Decisión simple
```text
SI temperatura > 30 ENTONCES
  ESCRIBIR "Hace calor"
FIN SI
```

## 3. Decisión doble
```text
SI edad >= 18 ENTONCES
  ESCRIBIR "Mayor de edad"
SINO
  ESCRIBIR "Menor de edad"
FIN SI
```

## 4. Decisión múltiple
```text
SI nota >= 4.5 ENTONCES
  nivel ← "Excelente"
SINO SI nota >= 3 ENTONCES
  nivel ← "Aprobado"
SINO
  nivel ← "No aprobado"
FIN SI
```

El orden importa.

## 5. Condiciones compuestas
```text
SI edad >= 18 Y tieneDocumento ENTONCES
...
```

## 6. Tablas de verdad
### Y
| A | B | A Y B |
|---|---|---|
| F | F | F |
| F | V | F |
| V | F | F |
| V | V | V |

### O
Solo es falso cuando ambas condiciones son falsas.

### NO
Invierte el valor lógico.

## 7. Casos límite
Si una condición dice `edad > 18`, una persona de exactamente 18 queda fuera. Pregunta siempre si corresponde `>` o `>=`.

## 8. Comparación de lenguajes
Pseudocódigo:
```text
SI numero MOD 2 = 0 ENTONCES
  ESCRIBIR "Par"
SINO
  ESCRIBIR "Impar"
FIN SI
```
Python:
```python
if numero % 2 == 0:
    print("Par")
else:
    print("Impar")
```
Java:
```java
if (numero % 2 == 0) {
    System.out.println("Par");
} else {
    System.out.println("Impar");
}
```
JavaScript:
```javascript
if (numero % 2 === 0) {
  console.log("Par");
} else {
  console.log("Impar");
}
```

## Ejercicios
1. Positivo, negativo o cero.
2. Mayor de dos números.
3. Mayor de tres números.
4. Año bisiesto.
5. Clasificación de una nota.
6. Validar que una fecha tenga mes entre 1 y 12.

## Reto — Tarifa de envío
Calcula una tarifa según peso, zona y si el envío es urgente. Define reglas sin solapamientos, prueba valores en los límites y explica por qué el orden de las decisiones es correcto.

## Qué sigue
**Unidad 05 — Ciclos, contadores, acumuladores y centinelas**
