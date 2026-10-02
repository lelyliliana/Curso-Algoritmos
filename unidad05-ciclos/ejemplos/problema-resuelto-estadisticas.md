# Problema resuelto — Estadísticas de una secuencia

## Enunciado
Leer N temperaturas y calcular promedio, máxima, mínima y cantidad superior a 30.

## Análisis
Necesitamos:
- un acumulador para suma;
- máximo y mínimo;
- contador para valores > 30.

## Pseudocódigo
```text
LEER n

SI n <= 0 ENTONCES
  ESCRIBIR "Cantidad inválida"
SINO
  suma ← 0
  sobre30 ← 0

  PARA i ← 1 HASTA n
    LEER temperatura

    SI i = 1 ENTONCES
      maxima ← temperatura
      minima ← temperatura
    SINO
      SI temperatura > maxima ENTONCES maxima ← temperatura
      SI temperatura < minima ENTONCES minima ← temperatura
    FIN SI

    suma ← suma + temperatura
    SI temperatura > 30 ENTONCES
      sobre30 ← sobre30 + 1
    FIN SI
  FIN PARA

  promedio ← suma / n
  ESCRIBIR promedio, maxima, minima, sobre30
FIN SI
```

## Decisión importante
Máximo y mínimo se inicializan con el primer dato real, no con 0. Así el algoritmo también funciona correctamente con valores todos negativos.

## Prueba
Datos:
```text
28, 31, 35, 29
```
Resultado:
- promedio 30.75;
- máxima 35;
- mínima 28;
- sobre 30: 2.

## Variante
Adapta el algoritmo para cantidad desconocida usando un centinela.
