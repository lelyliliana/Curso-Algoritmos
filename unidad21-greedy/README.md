# Unidad 21 — Algoritmos voraces (Greedy)

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/algoritmos/)

## Qué aprenderás
Construir decisiones locales, distinguir factibilidad de optimalidad y buscar contraejemplos antes de afirmar que una estrategia greedy es correcta.

# 1. Idea

Un greedy:
1. considera candidatos;
2. elige según un criterio local;
3. conserva la decisión;
4. continúa sin explorar normalmente todas las alternativas.

Es atractivo porque puede ser simple y eficiente.

Pero **no siempre produce óptimo global**.

# 2. Cambio de monedas

Monedas:
```text
1,5,10,25
```

Para 30, elegir primero 25 y luego 5 funciona bien.

Pero considera:
```text
1,3,4
objetivo=6
```

Greedy tomando moneda mayor:
```text
4 + 1 + 1 = 3 monedas
```

Óptimo:
```text
3 + 3 = 2 monedas
```

Encontramos contraejemplo.

# 3. Lección

Que una estrategia funcione en diez pruebas **no demuestra** optimalidad para todas las entradas.

Necesitamos una propiedad/prueba del problema o aceptar que es heurística.

# 4. Selección de actividades

Problema clásico:
- actividades con inicio/fin;
- queremos máximo número compatibles.

Criterio de terminar primero tiene una demostración greedy clásica.

No es porque “parece lógico”, sino porque existe un argumento de intercambio que demuestra que una solución óptima puede transformarse para incluir esa elección.

# 5. Factible vs óptimo

Una solución puede:
- cumplir restricciones (factible);
- pero no ser la mejor (óptima).

Greedy puede producir cualquiera según problema.

# 6. Diseñar criterio

Preguntas:
- ¿qué candidato elijo?
- ¿cuándo es factible?
- ¿por qué conservar esta decisión no destruye una solución óptima?
- ¿puedo construir contraejemplo?

# 7. Práctica guiada

Monedas 1,3,4 para objetivos 1..12.

Compara greedy con exploración completa/dinámica en pequeño.

Busca el primer objetivo donde difieren.

# 8. Errores frecuentes
- “funcionó en mis pruebas, entonces es óptimo”.
- Confundir heurística con algoritmo óptimo probado.
- Elegir criterio por intuición.
- No distinguir factibilidad/optimalidad.

# 9. Ejercicios
Selección de actividades, cambio de monedas, contraejemplos y comparación exhaustiva.

# 10. Reto
Propón greedy de planificación y **trata de romperlo**. Si no hallas contraejemplo, eso aún no es una prueba.

# 11. Autoevaluación
1. ¿Qué caracteriza greedy?
2. ¿Retrocede normalmente?
3. ¿Factible = óptimo?
4. ¿Qué demuestra el sistema 1,3,4?
5. ¿Por qué buscar contraejemplos?

# 12. Checklist
- [ ] Defino criterio.
- [ ] Compruebo factibilidad.
- [ ] Busco contraejemplo.
- [ ] No afirmo optimalidad sin justificación.

Continúa con backtracking.


---


## Caso completo y práctica autodidacta

Consulta el [laboratorio con contrato, traza, programa y resultado esperado](LABORATORIO.md) y las [soluciones razonadas](SOLUCIONES.md).

**Problema de referencia:** Greedy: selección de intervalos y contraejemplo de cambio.

## Continuar el curso

- **Unidad anterior:** [Unidad 20 — Divide y vencerás](../unidad20-divide-venceras/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 22 — Backtracking](../unidad22-backtracking/README.md)

---

### ¿Necesitas apoyo con este tema?

Si te bloqueaste con la práctica, necesitas revisar tu entorno o adaptar lo aprendido a tu proyecto, podemos trabajarlo en una sesión personalizada.

[**Solicitar asesoría para este tema por WhatsApp**](https://wa.me/573103618296?text=Hola%2C%20Leli.%20Estoy%20estudiando%20Unidad%2021.%20Algoritmos%20voraces%20%28greedy%29%20del%20curso%20Algoritmos%20y%20l%C3%B3gica%20de%20programaci%C3%B3n%20%28https%3A%2F%2Fgithub.com%2Flelyliliana%2FCurso-Algoritmos%2Ftree%2Fmain%2Funidad21-greedy%29%20y%20necesito%20una%20asesor%C3%ADa%20personalizada.%20Mi%20duda%20es%E2%80%A6)
