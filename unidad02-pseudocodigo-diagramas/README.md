# Unidad 02 — Pseudocódigo, diagramas de flujo y pruebas de escritorio

## Propósito

En la unidad anterior aprendiste a analizar un problema antes de escribir código. Ahora aprenderás a **representar la solución** de forma clara y verificable.

Trabajaremos con tres herramientas:

1. pseudocódigo;
2. diagramas de flujo;
3. pruebas de escritorio.

Estas representaciones permiten concentrarse en la lógica sin depender todavía de Python, Java o JavaScript.

## Objetivos

Al finalizar podrás:

- escribir algoritmos sencillos mediante pseudocódigo;
- utilizar instrucciones de entrada, proceso y salida;
- reconocer los símbolos principales de un diagrama de flujo;
- transformar un algoritmo entre descripción, pseudocódigo y diagrama;
- realizar pruebas de escritorio;
- seguir el cambio de las variables paso a paso;
- detectar errores lógicos antes de implementar un programa.

---

# 1. ¿Por qué representar un algoritmo?

Una explicación escrita puede ser suficiente para problemas pequeños, pero a medida que aumenta la complejidad necesitamos una representación más estructurada.

Considera:

> Pedir dos números, sumarlos y mostrar el resultado.

Podemos describirlo así:

```text
Leer dos números.
Sumarlos.
Mostrar el resultado.
```

Es correcto, pero podemos hacerlo más preciso.

---

# 2. Pseudocódigo

El pseudocódigo expresa un algoritmo mediante instrucciones parecidas a las de un lenguaje de programación, pero sin depender de una sintaxis específica.

Ejemplo:

```text
INICIO
    LEER numero1
    LEER numero2

    suma ← numero1 + numero2

    ESCRIBIR suma
FIN
```

Lo importante es comprender la lógica.

---

# 3. Convenciones del curso

Utilizaremos una notación sencilla y consistente.

## Inicio y final

```text
INICIO

FIN
```

## Entrada

```text
LEER edad
```

## Asignación

```text
resultado ← valor
```

La flecha significa:

> calcular o tomar el valor de la derecha y guardarlo en la variable de la izquierda.

Ejemplo:

```text
area ← base * altura
```

## Salida

```text
ESCRIBIR resultado
```

## Comentarios

Cuando sea necesario explicar una decisión:

```text
// Calcular el promedio de las tres notas
```

---

# 4. Ejemplo: área de un rectángulo

## Problema

Calcular el área de un rectángulo.

## Entradas

- base;
- altura.

## Proceso

```text
area = base × altura
```

## Salida

- área.

## Pseudocódigo

```text
INICIO
    LEER base
    LEER altura

    area ← base * altura

    ESCRIBIR area
FIN
```

---

# 5. Ejemplo: promedio de tres notas

```text
INICIO
    LEER nota1
    LEER nota2
    LEER nota3

    suma ← nota1 + nota2 + nota3
    promedio ← suma / 3

    ESCRIBIR promedio
FIN
```

Observa que podemos dividir un cálculo en varios pasos si eso facilita su comprensión.

También podríamos escribir:

```text
promedio ← (nota1 + nota2 + nota3) / 3
```

Ambas soluciones pueden ser correctas.

---

# 6. El diagrama de flujo

Un diagrama de flujo representa gráficamente la secuencia de un algoritmo.

Los símbolos permiten distinguir el tipo de operación.

## Inicio / Fin

Se representa normalmente mediante una figura ovalada o terminador.

```text
( INICIO )
(  FIN   )
```

## Entrada / Salida

Se representa mediante un paralelogramo.

```text
/ LEER edad /
```

## Proceso

Se representa mediante un rectángulo.

```text
┌──────────────────┐
│ area ← base*altura│
└──────────────────┘
```

## Decisión

Se representa mediante un rombo.

```text
       ◇
   ¿edad >= 18?
     /       \
   Sí         No
```

Las decisiones se estudiarán con profundidad en la Unidad 04.

## Flechas

Indican la dirección del flujo.

```text
Inicio
  ↓
Entrada
  ↓
Proceso
  ↓
Salida
  ↓
Fin
```

---

# 7. Diagrama de flujo: área de un rectángulo

Una representación textual sería:

```text
       ( INICIO )
            ↓
     / LEER base /
            ↓
    / LEER altura /
            ↓
┌─────────────────────┐
│ area ← base * altura │
└─────────────────────┘
            ↓
     / ESCRIBIR area /
            ↓
         ( FIN )
```

Cuando dibujes el diagrama en papel o una herramienta gráfica, utiliza los símbolos correspondientes.

---

# 8. Del problema a la representación

Utiliza esta secuencia:

```text
Problema
   ↓
Análisis
   ↓
Entradas / procesos / salidas
   ↓
Pseudocódigo
   ↓
Diagrama de flujo
   ↓
Prueba de escritorio
   ↓
Implementación
```

No siempre será necesario dibujar un diagrama para cada programa real. En este curso lo utilizaremos como herramienta para aprender a visualizar el flujo de una solución.

---

# 9. Prueba de escritorio

Una prueba de escritorio consiste en **ejecutar manualmente un algoritmo**, registrando los valores que toman sus variables.

Permite comprobar la lógica sin ejecutar código.

Algoritmo:

```text
INICIO
    LEER base
    LEER altura

    area ← base * altura

    ESCRIBIR area
FIN
```

Supongamos:

```text
base = 5
altura = 3
```

Tabla:

| Paso | base | altura | area | Salida |
|---|---:|---:|---:|---|
| LEER base | 5 | — | — | — |
| LEER altura | 5 | 3 | — | — |
| area ← base * altura | 5 | 3 | 15 | — |
| ESCRIBIR area | 5 | 3 | 15 | 15 |

Resultado:

```text
15
```

---

# 10. Seguimiento de variables

Considera:

```text
INICIO
    a ← 4
    b ← 7
    c ← a + b
    a ← c * 2
    b ← a - 3

    ESCRIBIR a
    ESCRIBIR b
    ESCRIBIR c
FIN
```

No intentes resolver todo mentalmente.

| Instrucción | a | b | c |
|---|---:|---:|---:|
| a ← 4 | 4 | — | — |
| b ← 7 | 4 | 7 | — |
| c ← a + b | 4 | 7 | 11 |
| a ← c * 2 | 22 | 7 | 11 |
| b ← a - 3 | 22 | 19 | 11 |

Salida:

```text
22
19
11
```

La variable puede cambiar de valor. La asignación no es una igualdad matemática permanente.

---

# 11. Comprender la asignación

Esta instrucción:

```text
contador ← contador + 1
```

puede parecer extraña desde la matemática.

En algoritmos significa:

1. consultar el valor actual de `contador`;
2. sumarle 1;
3. guardar el nuevo resultado nuevamente en `contador`.

Si:

```text
contador = 5
```

entonces:

```text
contador ← contador + 1
contador ← 5 + 1
contador ← 6
```

Este concepto será fundamental cuando estudiemos ciclos.

---

# 12. Detectar errores mediante una prueba de escritorio

Supongamos que alguien propone este algoritmo para calcular el promedio:

```text
INICIO
    LEER nota1
    LEER nota2
    LEER nota3

    promedio ← nota1 + nota2 + nota3 / 3

    ESCRIBIR promedio
FIN
```

Probemos:

```text
nota1 = 3
nota2 = 3
nota3 = 3
```

Si las operaciones respetan la precedencia habitual:

```text
3 + 3 + 3 / 3
3 + 3 + 1
7
```

El resultado esperado era:

```text
3
```

La prueba revela el error.

Corrección:

```text
promedio ← (nota1 + nota2 + nota3) / 3
```

---

# 13. Ejemplo completo: conversión de tiempo

## Problema

Convertir una cantidad total de minutos en horas y minutos restantes.

Ejemplo:

```text
135 minutos
```

debe producir:

```text
2 horas
15 minutos
```

## Análisis

Entrada:

```text
totalMinutos
```

Procesos:

```text
horas ← división entera de totalMinutos entre 60
minutos ← residuo de totalMinutos entre 60
```

Salida:

- horas;
- minutos.

## Pseudocódigo

```text
INICIO
    LEER totalMinutos

    horas ← totalMinutos DIV 60
    minutos ← totalMinutos MOD 60

    ESCRIBIR horas
    ESCRIBIR minutos
FIN
```

En este curso:

- `DIV` representa división entera;
- `MOD` representa el residuo.

## Prueba de escritorio

Entrada:

```text
totalMinutos = 135
```

| Paso | totalMinutos | horas | minutos |
|---|---:|---:|---:|
| LEER | 135 | — | — |
| DIV 60 | 135 | 2 | — |
| MOD 60 | 135 | 2 | 15 |

Salida:

```text
2 horas, 15 minutos
```

---

# 14. Buenas prácticas de pseudocódigo

## Utiliza nombres descriptivos

Mejor:

```text
precioProducto
cantidad
totalPagar
```

Evita cuando no exista una razón:

```text
x
a
z
```

## Una instrucción comprensible por línea

Facilita leer y probar el algoritmo.

## Mantén una indentación consistente

Será especialmente importante con decisiones y ciclos.

## No copies sintaxis innecesaria de un lenguaje

El pseudocódigo debe expresar la lógica, no convertirse en Java disfrazado o Python incompleto.

## Sé consistente

No utilices `LEER` en una parte y otra convención distinta sin motivo.

---

# 15. Errores frecuentes

## Escribir pseudocódigo ambiguo

```text
Hacer los cálculos.
```

¿Qué cálculos?

## Omitir una entrada

Si una operación necesita un dato, debe existir una forma de obtenerlo.

## Utilizar una variable antes de asignarle valor

```text
total ← precio * cantidad
LEER precio
LEER cantidad
```

El orden es incorrecto.

## Confundir entrada con salida

Leer un valor y mostrar un valor son operaciones diferentes.

## Dibujar flechas sin una secuencia clara

Un diagrama debe poder recorrerse desde Inicio hasta Fin.

---

# 16. Ejercicios de pseudocódigo

Para cada ejercicio:

1. identifica entrada, proceso y salida;
2. escribe el pseudocódigo;
3. realiza al menos una prueba de escritorio.

## Ejercicio 1

Calcular el perímetro de un rectángulo.

## Ejercicio 2

Convertir kilómetros a metros.

## Ejercicio 3

Calcular el precio total de una compra conociendo precio unitario y cantidad.

## Ejercicio 4

Convertir una cantidad de horas a minutos y segundos.

## Ejercicio 5

Intercambiar los valores de dos variables utilizando una variable auxiliar.

Ejemplo:

```text
a = 5
b = 9
```

Resultado:

```text
a = 9
b = 5
```

---

# 17. Ejercicios de prueba de escritorio

Sin programar, determina la salida.

## Ejercicio A

```text
a ← 10
b ← 4
c ← a - b
b ← c * 2
a ← b + 1

ESCRIBIR a
ESCRIBIR b
ESCRIBIR c
```

## Ejercicio B

```text
x ← 8
y ← 3
z ← x MOD y
x ← x DIV y

ESCRIBIR x
ESCRIBIR z
```

Construye una tabla de seguimiento para cada ejercicio.

---

# 18. Reto — Cuenta de restaurante

Un grupo consume en un restaurante y desea repartir la cuenta entre varias personas.

Se conocen:

- valor del consumo;
- porcentaje de propina;
- número de personas.

El algoritmo debe calcular:

- valor de la propina;
- total con propina;
- valor que corresponde pagar a cada persona.

## Tu trabajo

1. Analiza el problema.
2. Identifica entradas, procesos, salidas y restricciones.
3. Escribe el pseudocódigo.
4. Dibuja el diagrama de flujo.
5. Realiza una prueba de escritorio con:
   - consumo = 120000;
   - propina = 10%;
   - personas = 4.
6. Prueba otro conjunto de datos elegido por ti.
7. Explica qué debería ocurrir si el número de personas es cero.

No implementes todavía la solución en un lenguaje.

---

# 19. Lista de comprobación

- [ ] ¿El pseudocódigo tiene inicio y final?
- [ ] ¿Las entradas están identificadas?
- [ ] ¿Cada variable recibe un valor antes de utilizarse?
- [ ] ¿Las operaciones aparecen en el orden correcto?
- [ ] ¿Los nombres de las variables son comprensibles?
- [ ] ¿El diagrama representa el mismo algoritmo?
- [ ] ¿Las flechas permiten seguir claramente el flujo?
- [ ] ¿Realicé una prueba de escritorio?
- [ ] ¿Probé valores diferentes?
- [ ] ¿El resultado obtenido coincide con el esperado?

---

# 20. Qué sigue

Ya puedes analizar un problema y representar una solución básica.

En la siguiente unidad comenzaremos a trabajar formalmente con:

- datos;
- variables;
- constantes;
- tipos de datos;
- operadores;
- expresiones.

Continúa con:

**Unidad 03 — Datos, variables, operadores y expresiones**

---

## Idea clave

> Si puedes representar y probar una solución sin depender de un lenguaje, comprenderás mejor el código cuando llegue el momento de implementarla.
