# Unidad 06 — Modularización: funciones y procedimientos

## Qué aprenderás
Dividir problemas, diseñar contratos de funciones, usar parámetros/retornos y comprobar módulos de forma aislada.

# 1. Problema: algoritmo gigante

Imagina un algoritmo que:
- lee compra;
- valida;
- calcula descuento;
- calcula impuesto;
- imprime factura.

Todo mezclado funciona al principio, pero se vuelve difícil de probar.

Podemos separar responsabilidades.

# 2. Función

```text
FUNCION calcularArea(base, altura)
    RETORNAR base * altura
FIN FUNCION
```

Contrato:
```text
entradas: base, altura
salida: área
```

# 3. Llamar

```text
areaHabitacion ← calcularArea(4, 3)
```

La función retorna 12.

# 4. Parámetros

Los nombres dentro de la función representan entradas.

```text
FUNCION esMayor(edad, limite)
    RETORNAR edad >= limite
FIN FUNCION
```

Una función general puede ser reutilizable sin volverse excesivamente abstracta.

# 5. Retorno

```text
resultado ← calcularDescuento(total)
```

RETORNAR entrega un valor al llamador.

No confundas retornar con imprimir.

Una función que imprime el área no es equivalente a una que retorna el área: la segunda permite utilizarla en otros cálculos.

# 6. Procedimiento

En pseudocódigo podemos distinguir acciones sin retorno:

```text
PROCEDIMIENTO mostrarMenu()
    ESCRIBIR "1. Crear"
    ESCRIBIR "2. Salir"
FIN PROCEDIMIENTO
```

Los lenguajes concretos expresan esto de formas diferentes.

# 7. Variables locales

```text
FUNCION calcularTotal(precio,cantidad)
    subtotal ← precio*cantidad
    RETORNAR subtotal
FIN FUNCION
```

subtotal pertenece al módulo salvo que exista una razón para compartirlo.

# 8. Funciones puras

```text
FUNCION esPar(numero)
    RETORNAR numero MOD 2 = 0
FIN FUNCION
```

Misma entrada → mismo resultado y sin modificar estado externo.

Suelen ser fáciles de probar.

# 9. Ejemplo resuelto — tarifa

En vez de mezclar todo:

```text
FUNCION calcularTarifa(peso, urgente)
    ...
    RETORNAR tarifa
FIN FUNCION
```

Luego el algoritmo principal:
```text
LEER peso
LEER urgente
tarifa ← calcularTarifa(peso, urgente)
ESCRIBIR tarifa
```

La lógica queda separada de entrada/salida.

# 10. Diseñar antes de escribir

Para cada función define:

| pregunta | ejemplo |
|---|---|
| ¿qué hace? | calcula área |
| ¿qué recibe? | base, altura |
| ¿qué retorna? | número |
| ¿qué restricciones? | valores >=0 |
| ¿qué no debería hacer? | leer teclado/imprimir sin necesidad |

# 11. Demasiados parámetros

Una función con 12 parámetros puede indicar que el problema necesita mejor modelado/descomposición.

No existe un número mágico, pero úsalo como señal para revisar diseño.

# 12. Comparación de lenguajes

Pseudocódigo:
```text
FUNCION esPar(numero)
  RETORNAR numero MOD 2 = 0
FIN FUNCION
```

Python, Java y JavaScript del directorio de ejemplos implementan la misma idea. Observa qué cambia (sintaxis) y qué permanece (algoritmo).

# 13. Pruebas

Para `esPar`:
```text
2 → verdadero
3 → falso
0 → verdadero
-4 → verdadero
```

Prueba límites y casos menos obvios.

# 14. Errores frecuentes
- Función que hace demasiadas cosas.
- Imprimir cuando debería retornar.
- Depender de variables globales sin necesidad.
- Duplicar lógica en vez de extraer una responsabilidad.
- Crear funciones diminutas sin beneficio solo por “modularizar”.

# 15. Ejercicios
Crea funciones para:
1. área;
2. Celsius→Fahrenheit;
3. mayor de dos;
4. año bisiesto;
5. descuento;
6. validación de rango;
7. promedio de una colección (más adelante con arreglos).

# 16. Reto — Calculadora modular

Diseña:
```text
sumar
restar
multiplicar
dividir
```

La división debe manejar divisor cero según el contrato que definas.

Para cada función documenta entradas, salida y pruebas.

# 17. Autoevaluación
1. ¿Función vs procedimiento?
2. ¿Retornar vs imprimir?
3. ¿Qué es parámetro?
4. ¿Qué es variable local?
5. ¿Por qué una función pura suele ser fácil de probar?
6. ¿Cuándo modularizar puede empeorar claridad?

# 18. Checklist
- [ ] Defino contratos.
- [ ] Separo responsabilidades.
- [ ] Retorno valores cuando corresponde.
- [ ] Evito estado global innecesario.
- [ ] Pruebo módulos aislados.

Continúa con arreglos y listas.
