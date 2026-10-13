# Unidad 10 — Búsqueda lineal y búsqueda binaria

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/algoritmos/)

## Qué aprenderás
Localizar elementos, trazar comparaciones y comprender por qué la búsqueda binaria exige una propiedad previa: orden.

# 1. El problema

Datos:
```text
[18, 7, 25, 3, 11]
```

Queremos encontrar 3.

Sin información adicional, una estrategia segura es revisar elementos.

# 2. Búsqueda lineal

```text
FUNCION buscarLineal(datos, objetivo)
    PARA i ← 0 HASTA longitud(datos)-1
        SI datos[i] = objetivo
            RETORNAR i
        FIN SI
    FIN PARA
    RETORNAR -1
FIN FUNCION
```

Traza para objetivo 3:

| i | valor | ¿igual? |
|---:|---:|---|
| 0 | 18 | no |
| 1 | 7 | no |
| 2 | 25 | no |
| 3 | 3 | sí |

Resultado: índice 3.

# 3. Si no existe

Se recorren todos los elementos y retorna -1 según este contrato.

El valor de “no encontrado” es una decisión de interfaz; otros lenguajes/diseños pueden usar otra representación.

# 4. Ventaja lineal

No necesita colección ordenada.

También permite buscar por una condición compleja:
> primera temperatura > 35.

# 5. Búsqueda binaria

Ahora datos ordenados:

```text
[3,7,11,18,25,30,42]
```

Buscamos 25.

En lugar de empezar desde 3:
1. miramos el centro;
2. comparamos;
3. descartamos la mitad imposible.

# 6. Traza

```text
izq=0 der=6
medio=3 → 18
25 > 18 → descartar 0..3

izq=4 der=6
medio=5 → 30
25 < 30 → descartar 5..6

izq=4 der=4
medio=4 → 25
encontrado
```

# 7. Pseudocódigo

```text
izquierda ← 0
derecha ← longitud(datos)-1

MIENTRAS izquierda <= derecha
    medio ← (izquierda + derecha) DIV 2

    SI datos[medio] = objetivo
        RETORNAR medio
    SINO SI datos[medio] < objetivo
        izquierda ← medio + 1
    SINO
        derecha ← medio - 1
    FIN SI
FIN MIENTRAS

RETORNAR -1
```

# 8. ¿Por qué debe estar ordenado?

Si centro=18 y objetivo=25, podemos descartar la izquierda **solo porque sabemos** que todos esos valores son <=18 según el orden.

En datos:
```text
[18,7,25,3,11]
```
esa inferencia no existe.

# 9. ¿Ordenar para buscar una sola vez?

Ordenar tiene costo.

Si tienes datos desordenados y harás una única búsqueda, ordenar primero podría costar más que buscar linealmente.

Si harás muchas búsquedas, la decisión puede cambiar.

La elección depende del contexto.

# 10. Duplicados

Si existen varios 25, una búsqueda binaria básica puede encontrar **alguna** aparición, no necesariamente la primera.

Buscar primera/última aparición requiere adaptar el algoritmo.

# 11. Comparaciones

Lineal, peor caso: puede revisar n elementos.

Binaria: reduce aproximadamente a la mitad cada paso.

Formalizaremos esto con Big O en la Unidad 15.

# 12. Práctica guiada

Traza ambas búsquedas sobre 16 valores ordenados. Cuenta comparaciones para:
- primer elemento;
- último;
- inexistente.

# 13. Errores frecuentes
- Aplicar binaria a datos desordenados.
- Actualizar mal izquierda/derecha y crear ciclo.
- Confundir valor con índice.
- Asumir primera aparición con duplicados.
- Ordenar sin considerar el costo.

# 14. Ejercicios
1. Traza lineal.
2. Cuenta comparaciones.
3. Traza binaria.
4. Objetivo inexistente.
5. Duplicados.
6. Primera coincidencia por condición con lineal.

# 15. Reto
Compara número de comparaciones para tamaños crecientes. No midas solo tiempo: registra trabajo lógico.

# 16. Autoevaluación
1. ¿Lineal requiere orden?
2. ¿Binaria por qué sí?
3. ¿Qué descarta cada comparación?
4. ¿Qué ocurre con duplicados?
5. ¿Siempre conviene ordenar antes?

# 17. Checklist
- [ ] Trazo lineal.
- [ ] Trazo binaria.
- [ ] Comprendo requisito de orden.
- [ ] Distingo índice/valor.
- [ ] Elijo estrategia según contexto.

Continúa con ordenamientos.


---


## Caso completo y práctica autodidacta

Consulta el [laboratorio con contrato, traza, programa y resultado esperado](LABORATORIO.md) y las [soluciones razonadas](SOLUCIONES.md).

**Problema de referencia:** Búsqueda lineal y binaria con duplicados.

## Continuar el curso

- **Unidad anterior:** [Unidad 09 — Cadenas y procesamiento de texto](../unidad09-cadenas/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 11 — Ordenamientos básicos](../unidad11-ordenamiento-basico/README.md)

---

### ¿Necesitas apoyo con este tema?

Si te bloqueaste con la práctica, necesitas revisar tu entorno o adaptar lo aprendido a tu proyecto, podemos trabajarlo en una sesión personalizada.

[**Solicitar asesoría para este tema por WhatsApp**](https://wa.me/573103618296?text=Hola%2C%20Leli.%20Estoy%20estudiando%20Unidad%2010.%20B%C3%BAsqueda%20lineal%20y%20b%C3%BAsqueda%20binaria%20del%20curso%20Algoritmos%20y%20l%C3%B3gica%20de%20programaci%C3%B3n%20%28https%3A%2F%2Fgithub.com%2Flelyliliana%2FCurso-Algoritmos%2Ftree%2Fmain%2Funidad10-busqueda%29%20y%20necesito%20una%20asesor%C3%ADa%20personalizada.%20Mi%20duda%20es%E2%80%A6)
