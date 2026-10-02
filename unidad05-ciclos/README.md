# Unidad 05 — Ciclos, contadores, acumuladores y centinelas

## Propósito
Resolver problemas que requieren repetir acciones sin copiar instrucciones innecesariamente.

## 1. ¿Cuándo repetir?
- Procesar 30 estudiantes.
- Sumar una lista de ventas.
- Pedir una contraseña hasta que sea válida.
- Leer datos hasta recibir una señal de finalización.

## 2. Repetición conocida
```text
PARA i ← 1 HASTA 5 HACER
  ESCRIBIR i
FIN PARA
```

## 3. Repetición condicionada
```text
MIENTRAS saldo > 0 HACER
  ...
FIN MIENTRAS
```

## 4. Contador
```text
contador ← contador + 1
```

## 5. Acumulador
```text
total ← total + valor
```

## 6. Centinela
```text
LEER nota
MIENTRAS nota ≠ -1 HACER
  total ← total + nota
  cantidad ← cantidad + 1
  LEER nota
FIN MIENTRAS
```

El valor centinela indica cuándo terminar y no forma parte de los datos.

## 7. Validación repetitiva
```text
LEER edad
MIENTRAS edad < 0 HACER
  ESCRIBIR "Dato inválido"
  LEER edad
FIN MIENTRAS
```

## 8. Riesgo de ciclo infinito
Toda repetición condicionada debe tener alguna posibilidad de modificar la condición.

## 9. Ejemplo — promedio de N valores
```text
LEER cantidad
suma ← 0

PARA i ← 1 HASTA cantidad HACER
  LEER valor
  suma ← suma + valor
FIN PARA

promedio ← suma / cantidad
ESCRIBIR promedio
```

## Ejercicios
1. Tabla de multiplicar.
2. Suma de 1 a N.
3. Factorial iterativo.
4. Contar pares entre 1 y N.
5. Promedio de N notas.
6. Leer números hasta introducir 0 y calcular suma y cantidad.

## Reto — Estadísticas de ventas
Lee ventas hasta recibir un centinela. Calcula cantidad, total, promedio, mayor y menor. Define qué hacer si no se registra ninguna venta.

## Qué sigue
**Unidad 06 — Modularización: funciones y procedimientos**
