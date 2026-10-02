# Unidad 12 — Merge Sort, Quick Sort y comparación

## Qué aprenderás
Comprender divide y vencerás aplicado al ordenamiento y comparar algoritmos sin reducir todo a “más rápido”.

# 1. ¿Por qué otro ordenamiento?

Los algoritmos básicos son excelentes para aprender, pero su crecimiento puede ser costoso en colecciones grandes.

Merge Sort y Quick Sort introducen estrategias más sofisticadas.

# 2. Merge Sort — dividir

```text
[8,3,6,2]
→ [8,3] [6,2]
→ [8] [3] [6] [2]
```

Subcolecciones de un elemento ya están ordenadas.

# 3. Merge — mezclar

```text
[8] + [3] → [3,8]
[6] + [2] → [2,6]
```

Luego:
```text
[3,8] + [2,6]
→ comparar 3/2 → 2
→ 3/6 → 3
→ 8/6 → 6
→ 8
→ [2,3,6,8]
```

La mezcla eficiente aprovecha que ambas partes ya están ordenadas.

# 4. Costo de memoria

Una implementación típica de Merge Sort necesita almacenamiento auxiliar para mezclar.

Tiempo y memoria son dimensiones diferentes.

# 5. Quick Sort — particionar

Escogemos pivote.

Ejemplo conceptual:
```text
[8,3,6,2], pivote=6
menores: [3,2]
pivote: [6]
mayores: [8]
```

Después repetimos en particiones.

Las implementaciones reales pueden particionar in-place y manejar iguales de distintas formas.

# 6. Elección de pivote

Un pivote desfavorable repetidamente puede generar particiones muy desequilibradas.

Por eso no digas simplemente “Quick Sort siempre O(n log n)”: estudiaremos mejor/esperado/peor caso con complejidad.

# 7. Comparación conceptual

| aspecto | Merge | Quick |
|---|---|---|
| idea | dividir+mezclar | particionar |
| memoria auxiliar | frecuente | depende implementación |
| peor caso típico | O(n log n) | O(n²) |
| promedio/esperado típico | O(n log n) | O(n log n) |

Estas expresiones se profundizan en Big O.

# 8. ¿Y los algoritmos básicos?

Para colecciones pequeñas o casi ordenadas, Insertion puede ser competitivo y además simple.

Bibliotecas reales pueden combinar estrategias.

No existe un ganador universal fuera de contexto.

# 9. Práctica guiada

Traza Merge y Quick sobre:
```text
[8,3,6,2,7,1]
```

Para Quick documenta qué pivote elegiste.

# 10. Experimentos

Si mides:
- usa mismas entradas;
- repite;
- registra tamaño;
- documenta lenguaje/implementación;
- separa tiempo de comparaciones/memoria.

# 11. Errores frecuentes
- Comparar tiempos de una sola ejecución.
- No documentar pivote.
- Confundir promedio con peor caso.
- Ignorar memoria.
- Asumir que teoría predice exactamente milisegundos.

# 12. Ejercicios
1. Traza Merge.
2. Traza Quick con dos pivotes.
3. Compara con Insertion pequeño.
4. Explica memoria de Merge.
5. Entrada que produzca particiones pobres para una estrategia de pivote dada.

# 13. Reto
Diseña comparación reproducible entre tres algoritmos y separa conclusiones teóricas de observaciones experimentales.

# 14. Autoevaluación
1. ¿Qué mezcla Merge?
2. ¿Por qué puede mezclar eficientemente?
3. ¿Qué hace partición en Quick?
4. ¿Por qué importa pivote?
5. ¿Tiempo y memoria son la misma métrica?

# 15. Checklist
- [ ] Trazo Merge.
- [ ] Trazo Quick.
- [ ] Documento pivote.
- [ ] Comparo varias métricas.
- [ ] Evito absolutos sin contexto.

Continúa con recursividad.
