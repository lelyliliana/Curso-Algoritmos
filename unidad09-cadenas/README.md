# Unidad 09 — Cadenas y procesamiento de texto

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/algoritmos/)

## Qué aprenderás
Tratar texto como secuencia, normalizar según reglas explícitas y resolver conteos, búsquedas y comparaciones.

# 1. Texto como secuencia

```text
"casa"
```

puede verse conceptualmente:

```text
0:c  1:a  2:s  3:a
```

Esto permite aplicar patrones de recorridos.

# 2. Longitud y caracteres

Podemos:
- obtener longitud;
- consultar una posición;
- recorrer;
- comparar;
- construir otro texto.

Las operaciones concretas cambian entre lenguajes, pero la lógica permanece.

# 3. Contar vocales

```text
contador ← 0

PARA CADA caracter EN texto
    SI caracter pertenece a vocales
        contador ← contador + 1
    FIN SI
FIN PARA
```

Pregunta antes:
> ¿A y á cuentan como vocales? ¿Mayúsculas?

La regla define la normalización.

# 4. Normalización

Para comparar quizá decidimos:
1. minúsculas;
2. eliminar espacios;
3. retirar signos;
4. tratar o conservar tildes.

No existe una normalización correcta para todos los problemas.

“año” y “ano” no deberían considerarse iguales en muchos contextos.

# 5. Palíndromo

Texto:
```text
reconocer
```

Comparamos extremos:

```text
r ↔ r
e ↔ e
c ↔ c
...
```

Podemos usar dos índices:
```text
izquierda ← 0
derecha ← longitud-1
```

Mientras izquierda < derecha, comparamos y acercamos.

Consulta el ejemplo paso a paso existente.

# 6. Frecuencias

Texto:
```text
"casa"
```

Resultado:
```text
c:1
a:2
s:1
```

Necesitamos una estructura para asociar elemento→conteo. Más adelante veremos mapas.

# 7. Palabras

Contar palabras no siempre equivale a “contar espacios + 1”.

Considera:
```text
" hola   mundo "
```

Primero define qué separa palabras y cómo tratar espacios repetidos/signos.

# 8. Transformación

Un algoritmo puede construir una nueva cadena:
- invertir;
- filtrar caracteres;
- reemplazar según reglas;
- extraer fragmentos.

Evita modificar mentalmente mientras recorres sin definir resultado.

# 9. Práctica guiada

Texto:
```text
"Anita lava la tina"
```

Define normalización para evaluar palíndromo:
- minúsculas;
- retirar espacios.

Después compara posiciones.

Si decides ignorar otros signos/tildes, documenta la regla.

# 10. Errores frecuentes
- Normalizar sin explicar.
- Acceder fuera de límites.
- Suponer que carácter = byte en cualquier lenguaje/codificación.
- Contar palabras solo por espacios.
- Destruir información relevante al quitar tildes/signos.

# 11. Ejercicios
1. Vocales.
2. Palabras bajo regla definida.
3. Invertir.
4. Palíndromo.
5. Carácter frecuente.
6. Primera posición de un carácter.
7. Eliminar espacios repetidos.

# 12. Reto
Analizador: caracteres, palabras, vocales, frecuencia de palabras y palabra más larga. Documenta normalización y empates.

# 13. Autoevaluación
1. ¿Por qué texto puede recorrerse?
2. ¿Qué es normalización?
3. ¿Existe una normalización universal?
4. ¿Cómo funciona comparación simétrica?
5. ¿Por qué “espacios + 1” puede fallar?

# 14. Checklist
- [ ] Recorro texto.
- [ ] Defino normalización.
- [ ] Manejo índices.
- [ ] Documento reglas lingüísticas.

Continúa con búsqueda.


---

## Continuar el curso

- **Unidad anterior:** [Unidad 08 — Matrices y datos bidimensionales](../unidad08-matrices/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 10 — Búsqueda lineal y búsqueda binaria](../unidad10-busqueda/README.md)

---

### ¿Necesitas apoyo con este tema?

Si te bloqueaste con la práctica, necesitas revisar tu entorno o adaptar lo aprendido a tu proyecto, podemos trabajarlo en una sesión personalizada.

[**Solicitar asesoría para este tema por WhatsApp**](https://wa.me/573103618296?text=Hola%2C%20Leli.%20Estoy%20estudiando%20Unidad%2009.%20Cadenas%20y%20procesamiento%20de%20texto%20del%20curso%20Algoritmos%20y%20l%C3%B3gica%20de%20programaci%C3%B3n%20%28https%3A%2F%2Fgithub.com%2Flelyliliana%2FCurso-Algoritmos%2Ftree%2Fmain%2Funidad09-cadenas%29%20y%20necesito%20una%20asesor%C3%ADa%20personalizada.%20Mi%20duda%20es%E2%80%A6)
