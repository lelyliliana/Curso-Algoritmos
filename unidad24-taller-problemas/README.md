# Unidad 24 — Taller integrador de resolución de problemas

## Propósito

Hasta aquí cada unidad te presentaba una estrategia. Ahora el enunciado **no te dirá qué usar**.

La habilidad central es reconocer el problema, proponer alternativas y justificar una solución.

## Antes de empezar

Debes poder trabajar con:
- decisiones y ciclos;
- funciones;
- colecciones;
- búsqueda/ordenamiento;
- complejidad;
- estructuras;
- recorridos de grafos;
- estrategias algorítmicas.

Si solo puedes resolver un problema cuando alguien te dice “usa un mapa” o “usa BFS”, vuelve a practicar antes de continuar.

# 1. Método de resolución

Para cada problema sigue estas etapas.

## Etapa A — Comprender
1. Reformula con tus palabras.
2. Identifica entradas/salidas.
3. Escribe restricciones.
4. Crea ejemplos propios.
5. Identifica casos límite/inválidos.

## Etapa B — Diseñar
6. Identifica patrones conocidos.
7. Propón al menos una estrategia.
8. Elige estructuras.
9. Escribe pseudocódigo.

## Etapa C — Comprobar
10. Haz prueba de escritorio.
11. Construye casos que intenten romper tu solución.
12. Determina corrección esperada.

## Etapa D — Analizar
13. Define n.
14. Estima tiempo/espacio.
15. Compara alternativa cuando aporte.

## Etapa E — Implementar
16. Implementa cuando corresponda.
17. Prueba.
18. Explica diferencias entre algoritmo y detalles del lenguaje.

Usa `plantilla-solucion.md`.

# 2. Problemas por nivel

## Nivel 1 — Colecciones

### Primer duplicado
Determina el primer valor que aparece por segunda vez.

No empieces programando. Pregunta:
- ¿necesito conservar orden?
- ¿qué estructura ayuda a saber si ya vi un valor?

### Dos valores
Determina si dos posiciones distintas suman un objetivo.

Compara al menos una solución directa con otra que use una estructura adicional.

# 3. Nivel 2 — Decisiones de costo

### Muchas búsquedas
Tienes 100 000 identificadores y miles de consultas.

Incluye en el análisis el costo de preparar/ordenar los datos.

No compares solo una búsqueda aislada.

# 4. Nivel 3 — Greedy

### Agenda de intervalos
Selecciona el máximo número de actividades compatibles.

Propón criterio, busca contraejemplos y justifica por qué funciona o no.

### Cambio de monedas
Compara greedy con una estrategia que garantice óptimo en casos pequeños.

# 5. Nivel 4 — Grafos

### Red de contactos
Determina:
- conectividad;
- mínimo número de saltos.

Debes explicar por qué el recorrido elegido responde a cada pregunta.

### Dependencias
Tareas A→B. Determina si existe ciclo.

Investiga/deriva cómo un recorrido puede detectar una dependencia cíclica; no copies un algoritmo que no puedas trazar.

# 6. Nivel 5 — Exploración

### Laberinto
Define:
- movimientos;
- obstáculos;
- visitados;
- qué significa encontrar “una ruta” frente a “la ruta más corta”.

La definición cambia la estrategia.

# 7. Nivel 6 — Investigación guiada

### Ruta con costo
Las conexiones tienen pesos.

BFS básico ya no garantiza mínimo costo arbitrario.

Investiga una técnica apropiada y responde:
- qué supuesto necesita;
- qué estructura utiliza;
- por qué es correcta bajo esos supuestos.

El objetivo es aprender a incorporar un algoritmo nuevo desde sus fundamentos.

# 8. Cómo evaluar tu propia solución

No preguntes solo “¿funciona?”.

Pregunta:
- ¿responde exactamente al enunciado?
- ¿maneja límites?
- ¿puedo explicar cada estructura?
- ¿tengo contraejemplos?
- ¿la complejidad corresponde al código?
- ¿comparé alternativas justamente?

# 9. Reto final del taller

Elige uno de los problemas y produce una solución completa utilizando las cinco etapas del método.

Después entrégasela a otra persona —o reléela al día siguiente— e intenta reconstruir la lógica **solo con tu documentación**.

# 10. Autoevaluación

1. ¿Puedo elegir una estructura sin que me la indiquen?
2. ¿Puedo distinguir “funciona” de “es óptimo”?
3. ¿Puedo definir n?
4. ¿Puedo construir un contraejemplo?
5. ¿Puedo explicar por qué BFS no sirve para cualquier peso?
6. ¿Puedo comparar dos soluciones sin mirar solo tiempo?

# 11. Checklist

- [ ] Reformulo problemas.
- [ ] Diseño antes de programar.
- [ ] Pruebo límites.
- [ ] Justifico estructuras.
- [ ] Analizo costo.
- [ ] Comparo alternativas.
- [ ] Puedo aprender una técnica nueva explicando sus supuestos.

Continúa con el proyecto final.
