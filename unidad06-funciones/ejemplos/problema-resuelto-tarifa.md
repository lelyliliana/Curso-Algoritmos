# Problema resuelto — Separar responsabilidades

## Enunciado
Calcular el costo de un servicio según cantidad y precio, aplicando descuento cuando corresponda.

## Diseño monolítico
Podríamos escribir todo en una sola secuencia, pero crecería mal.

## Descomposición
```text
esCantidadValida(cantidad)
calcularSubtotal(precio, cantidad)
calcularDescuento(subtotal, cantidad)
calcularTotal(subtotal, descuento)
```

## Pseudocódigo
```text
FUNCION esCantidadValida(cantidad)
  RETORNAR cantidad > 0
FIN FUNCION

FUNCION calcularSubtotal(precio, cantidad)
  RETORNAR precio * cantidad
FIN FUNCION

FUNCION calcularDescuento(subtotal, cantidad)
  SI cantidad >= 10 ENTONCES
    RETORNAR subtotal * 0.10
  FIN SI
  RETORNAR 0
FIN FUNCION
```

## Ventaja
Cada regla puede probarse independientemente.

## Pruebas
Para `calcularDescuento`:
- cantidad 9 → 0;
- cantidad 10 → 10 %;
- cantidad 11 → 10 %.

El límite queda explícitamente probado.
