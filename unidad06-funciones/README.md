# Unidad 06 — Modularización: funciones y procedimientos

## Propósito
Dividir soluciones grandes en piezas pequeñas, reutilizables y comprobables.

## 1. Modularizar
En lugar de un algoritmo enorme:
```text
leerDatos
validarDatos
calcularTotal
mostrarResultado
```

Cada módulo tiene una responsabilidad.

## 2. Parámetros
```text
FUNCION calcularArea(base, altura)
  RETORNAR base * altura
FIN FUNCION
```

## 3. Retorno
Una función puede producir un valor que será utilizado por otra parte del algoritmo.

## 4. Procedimientos
Un procedimiento realiza una acción sin necesidad de retornar un valor.

## 5. Variables locales
Una variable creada dentro de un módulo debería permanecer allí cuando no necesita compartirse.

## 6. Funciones puras
Una función es más fácil de probar cuando el resultado depende únicamente de sus entradas y no modifica información externa.

## 7. Ejemplo
```text
FUNCION esPar(numero)
  RETORNAR numero MOD 2 = 0
FIN FUNCION
```

## 8. Comparación
Python:
```python
def es_par(numero):
    return numero % 2 == 0
```
Java:
```java
static boolean esPar(int numero) {
    return numero % 2 == 0;
}
```
JavaScript:
```javascript
function esPar(numero) {
  return numero % 2 === 0;
}
```

## Ejercicios
Crea funciones para:
1. calcular área de un círculo;
2. convertir Celsius a Fahrenheit;
3. obtener el mayor de dos valores;
4. determinar si un año es bisiesto;
5. calcular descuento.

## Reto — Calculadora modular
Diseña una calculadora donde cada operación sea una función independiente. Incluye validación de división entre cero y pruebas para cada función.

## Qué sigue
**Unidad 07 — Arreglos, listas y procesamiento secuencial**
