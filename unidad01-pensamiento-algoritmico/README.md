# Unidad 01 — Problemas, algoritmos y pensamiento computacional

## Propósito

Antes de escribir código es necesario aprender a **entender un problema** y convertirlo en una secuencia de pasos que pueda ejecutarse y comprobarse.

En esta unidad aprenderás a distinguir entre problema, solución y algoritmo; identificar entradas, procesos, salidas y restricciones; descomponer problemas; reconocer información relevante y diseñar soluciones ordenadas.

## Objetivos

Al finalizar podrás:

- explicar qué es un algoritmo;
- diferenciar problema, algoritmo y programa;
- identificar entradas, procesos y salidas;
- reconocer restricciones y casos especiales;
- descomponer un problema grande en partes pequeñas;
- describir soluciones mediante pasos claros;
- comprobar manualmente si una solución produce el resultado esperado.

---

# 1. ¿Qué es un problema?

Un problema aparece cuando existe una situación inicial y queremos alcanzar un resultado, pero necesitamos determinar **cómo hacerlo**.

Ejemplo:

> Se conocen tres calificaciones de un estudiante y se necesita calcular la nota definitiva.

Antes de programar debemos responder:

- ¿Qué información recibimos?
- ¿Qué debemos calcular?
- ¿Qué resultado debemos entregar?
- ¿Existen restricciones?

En este caso:

| Elemento | Descripción |
|---|---|
| Entradas | Tres calificaciones |
| Proceso | Sumar las notas y dividir entre 3 |
| Salida | Nota definitiva |
| Restricción | Las notas deben pertenecer al rango permitido |

Esta forma de analizar el problema evita comenzar a escribir instrucciones sin comprender qué se necesita resolver.

---

# 2. Problema, algoritmo y programa

No son lo mismo.

## Problema

Describe **qué necesitamos resolver**.

> Calcular el promedio de tres notas.

## Algoritmo

Describe **cómo resolverlo**, mediante una secuencia ordenada de pasos.

```text
1. Leer nota1
2. Leer nota2
3. Leer nota3
4. Calcular promedio = (nota1 + nota2 + nota3) / 3
5. Mostrar promedio
```

## Programa

Es la implementación del algoritmo utilizando un lenguaje de programación.

Un mismo algoritmo puede implementarse posteriormente en Python, Java, JavaScript u otros lenguajes.

```text
PROBLEMA
   ↓
ANÁLISIS
   ↓
ALGORITMO
   ↓
PRUEBA
   ↓
PROGRAMA
```

---

# 3. ¿Qué es un algoritmo?

Un algoritmo es una secuencia **finita, ordenada y clara** de pasos para resolver un problema o realizar una tarea.

Un buen algoritmo debe:

- tener un objetivo definido;
- recibir la información necesaria;
- indicar pasos comprensibles;
- evitar ambigüedades;
- terminar;
- producir un resultado verificable.

## Ejemplo cotidiano

Problema: preparar una bebida caliente.

Una descripción como:

> Preparar café.

no es un algoritmo suficientemente detallado.

Una versión más precisa sería:

```text
1. Colocar agua en un recipiente.
2. Calentar el agua.
3. Colocar café en una taza.
4. Verter el agua caliente.
5. Mezclar.
6. Servir.
```

El nivel de detalle depende de quién ejecutará las instrucciones y de lo que necesitemos controlar.

---

# 4. Entrada, proceso y salida

Muchos problemas pueden analizarse inicialmente mediante este modelo:

```text
ENTRADA → PROCESO → SALIDA
```

## Ejemplo: área de un rectángulo

**Problema:** calcular el área de un rectángulo.

### Entrada

- base;
- altura.

### Proceso

```text
area = base × altura
```

### Salida

- área calculada.

## Ejemplo: determinar si una persona es mayor de edad

### Entrada

- edad.

### Proceso

Comparar la edad con 18.

### Salida

- indicar si es mayor de edad.

Observa que no todos los procesos son operaciones matemáticas. También pueden incluir decisiones, búsquedas, repeticiones o transformaciones de información.

---

# 5. Restricciones

Una solución correcta también debe considerar qué valores son válidos.

Problema:

> Calcular el promedio de tres calificaciones entre 0 y 5.

No basta con conocer la fórmula. Existe una restricción:

```text
0 ≤ nota ≤ 5
```

¿Qué debería ocurrir si alguien proporciona una nota de 8?

Detectar este tipo de situaciones forma parte del análisis.

---

# 6. Casos normales, casos límite y casos inválidos

Al diseñar una solución conviene imaginar diferentes escenarios.

## Caso normal

Valores habituales.

```text
notas: 4.0, 3.5, 4.5
```

## Caso límite

Valores ubicados exactamente en los extremos permitidos.

```text
nota = 0
nota = 5
```

## Caso inválido

Un valor que viola las restricciones.

```text
nota = -2
nota = 8
```

Un algoritmo debe diseñarse pensando no solamente en el ejemplo que funciona.

---

# 7. Descomposición

El pensamiento computacional permite dividir un problema complejo en problemas más pequeños.

Supongamos que necesitamos desarrollar un sistema sencillo para registrar estudiantes.

En lugar de pensar:

> Crear todo el sistema.

podemos descomponerlo:

```text
Registrar estudiante
      ↓
Validar información
      ↓
Registrar calificaciones
      ↓
Calcular promedio
      ↓
Determinar estado
      ↓
Mostrar resultado
```

Cada parte puede analizarse y resolverse de manera independiente.

---

# 8. Reconocimiento de patrones

A veces problemas diferentes comparten una misma estructura.

Ejemplo A:

> Calcular el promedio de las notas de un estudiante.

Ejemplo B:

> Calcular la temperatura promedio de una semana.

Ejemplo C:

> Calcular el promedio de ventas de una tienda.

Los datos cambian, pero aparece el mismo patrón:

```text
sumar valores
      ↓
contar valores
      ↓
dividir suma / cantidad
```

Reconocer patrones permite reutilizar ideas de solución.

---

# 9. Abstracción

Abstraer significa concentrarse en la información importante para resolver el problema y dejar temporalmente de lado detalles que no afectan la solución.

Problema:

> Determinar si una persona puede ingresar a una actividad reservada para mayores de 18 años.

Para resolverlo probablemente necesitamos:

- edad.

No necesitamos necesariamente:

- color favorito;
- estatura;
- profesión;
- número de hermanos.

Elegir correctamente la información relevante simplifica el algoritmo.

---

# 10. Diseñar antes de programar

Ante un problema nuevo utiliza inicialmente estas preguntas:

## Paso 1 — ¿Qué debo resolver?

Escribe el objetivo con tus propias palabras.

## Paso 2 — ¿Qué información recibo?

Identifica las entradas.

## Paso 3 — ¿Qué debo entregar?

Identifica las salidas.

## Paso 4 — ¿Qué reglas existen?

Identifica restricciones y condiciones.

## Paso 5 — ¿Puedo dividirlo?

Separa el problema en tareas pequeñas.

## Paso 6 — ¿Qué pasos transforman la entrada en la salida?

Diseña el algoritmo.

## Paso 7 — ¿Funciona con ejemplos diferentes?

Comprueba manualmente la solución antes de programarla.

---

# 11. Ejemplo completo

## Problema

Una tienda necesita calcular el total que debe pagar un cliente por un producto.

Se conoce:

- precio unitario;
- cantidad comprada.

## Análisis

### Entradas

```text
precio
cantidad
```

### Proceso

```text
total = precio × cantidad
```

### Salida

```text
total a pagar
```

### Restricciones

```text
precio > 0
cantidad > 0
```

## Algoritmo inicial

```text
1. Leer precio.
2. Leer cantidad.
3. Calcular total = precio × cantidad.
4. Mostrar total.
```

## Prueba manual

Si:

```text
precio = 2500
cantidad = 4
```

entonces:

```text
total = 2500 × 4
total = 10000
```

Resultado esperado:

```text
10000
```

Todavía no necesitamos Python, Java ni JavaScript para comprobar que la idea funciona.

---

# 12. Errores frecuentes

## Empezar escribiendo código inmediatamente

Puede llevar a resolver correctamente el problema equivocado.

## Confundir algoritmo con lenguaje

Un algoritmo es la solución lógica. Python o Java son formas de implementarla.

## No identificar restricciones

Una fórmula puede funcionar matemáticamente y aun así aceptar datos que el problema considera inválidos.

## Probar un solo caso

Que un ejemplo funcione no demuestra que la solución funcione para todos los casos relevantes.

## Agregar información innecesaria

Más datos no siempre significan una mejor solución.

---

# 13. Ejercicios

Para cada problema identifica:

1. objetivo;
2. entradas;
3. proceso;
4. salidas;
5. restricciones;
6. al menos un caso normal;
7. un caso límite o inválido.

## Ejercicio 1

Calcular el área de un círculo a partir de su radio.

## Ejercicio 2

Convertir una temperatura de grados Celsius a Fahrenheit.

## Ejercicio 3

Calcular cuánto debe pagar una persona por varios productos del mismo precio.

## Ejercicio 4

Determinar si un número es positivo, negativo o cero.

## Ejercicio 5

Determinar cuál de dos números es mayor.

## Ejercicio 6

Calcular el tiempo total de un viaje conociendo distancia y velocidad promedio.

---

# 14. Reto

## Organizador de presupuesto

Una persona desea conocer cuánto dinero le queda después de pagar sus gastos principales del mes.

Conoce:

- ingreso mensual;
- vivienda;
- alimentación;
- transporte;
- otros gastos.

### Tu tarea

Sin utilizar todavía un lenguaje de programación:

1. Explica el problema con tus palabras.
2. Identifica las entradas.
3. Define las salidas.
4. Identifica restricciones razonables.
5. Descompón el problema.
6. Escribe un algoritmo mediante pasos numerados.
7. Prueba el algoritmo con un caso normal.
8. Prueba un caso donde los gastos sean mayores que los ingresos.
9. Explica qué información adicional podría ser útil y cuál sería innecesaria.

---

# 15. Lista de comprobación

Antes de considerar terminado un algoritmo inicial pregúntate:

- [ ] ¿Comprendo realmente el problema?
- [ ] ¿Identifiqué las entradas?
- [ ] ¿Sé exactamente qué salida necesito?
- [ ] ¿Identifiqué restricciones?
- [ ] ¿Mis pasos están ordenados?
- [ ] ¿Cada paso es suficientemente claro?
- [ ] ¿El algoritmo termina?
- [ ] ¿Probé más de un caso?
- [ ] ¿Consideré valores límite o inválidos?
- [ ] ¿Puedo explicar la solución sin mostrar código?

---

# 16. Qué sigue

En la siguiente unidad aprenderás a representar algoritmos de manera más formal mediante:

- pseudocódigo;
- diagramas de flujo;
- pruebas de escritorio.

Continúa con:

**Unidad 02 — Pseudocódigo, diagramas de flujo y pruebas de escritorio**

---

## Idea clave

> Programar no comienza escribiendo código. Comienza comprendiendo qué problema necesitas resolver.
