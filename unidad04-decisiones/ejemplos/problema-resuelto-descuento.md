# Problema resuelto — Descuento por cantidad

## Enunciado
Una tienda aplica 10 % de descuento cuando una compra contiene 10 o más unidades del mismo producto. Calcular subtotal, descuento y total.

## 1. Entradas
- precio unitario;
- cantidad.

## 2. Restricciones
```text
precio > 0
cantidad > 0
```

## 3. Salidas
- subtotal;
- descuento;
- total.

## 4. Estrategia
Primero calcular subtotal. Después decidir si corresponde descuento.

## 5. Pseudocódigo
```text
INICIO
  LEER precio
  LEER cantidad

  subtotal ← precio * cantidad

  SI cantidad >= 10 ENTONCES
    descuento ← subtotal * 0.10
  SINO
    descuento ← 0
  FIN SI

  total ← subtotal - descuento

  ESCRIBIR subtotal, descuento, total
FIN
```

## 6. Prueba normal
```text
precio = 5000
cantidad = 12
subtotal = 60000
descuento = 6000
total = 54000
```

## 7. Caso límite
Con cantidad = 10, sí aplica descuento porque la condición utiliza >=.

Con cantidad = 9, no aplica.

## 8. Pregunta de diseño
¿Qué cambiaría si el descuento dependiera del subtotal y no de la cantidad?
