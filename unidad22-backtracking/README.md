# Unidad 22 — Backtracking

## Qué aprenderás
Explorar un espacio de decisiones, construir estados parciales y retroceder cuando una rama deja de ser viable.

# 1. Diferencia con greedy

Greedy elige y normalmente no vuelve.

Backtracking:
```text
elegir → explorar → si falla → deshacer → probar otra opción
```

# 2. Árbol de búsqueda

Para permutaciones de A,B,C:

```text
          []
      /    |    \
     A     B     C
    / \   ...
   AB AC
   |   |
  ABC ACB
```

Cada nodo es un estado parcial.

# 3. Plantilla

```text
FUNCION explorar(estado)
    SI estado es solución
        REGISTRAR/RETORNAR
    FIN SI

    PARA CADA opcion posible
        SI opcion es válida
            elegir opcion
            explorar(estado)
            deshacer opcion
        FIN SI
    FIN PARA
FIN
```

El “deshacer” restaura el estado para explorar otra rama.

# 4. Poda

Si una solución parcial viola una restricción, no necesitamos completar esa rama.

Ejemplo: asignar personas a horarios sin conflictos. En cuanto dos asignaciones chocan, podamos.

# 5. Laberinto

Estado:
```text
posición + celdas visitadas/camino
```

Opciones:
```text
arriba,abajo,izquierda,derecha
```

Validez:
- dentro;
- no pared;
- no repetir de forma inválida.

# 6. Costo

El espacio de búsqueda puede crecer exponencialmente/factorialmente.

La poda puede ayudar muchísimo, pero no convierte mágicamente cualquier problema en eficiente.

# 7. Primera solución vs todas

El algoritmo cambia según quieras:
- encontrar una;
- contar;
- enumerar todas;
- optimizar.

Define el objetivo.

# 8. Práctica guiada

Genera permutaciones de [A,B,C]. Dibuja árbol y marca cuándo se añade/quita un elemento.

# 9. Errores frecuentes
- No deshacer estado.
- No copiar/restaurar correctamente.
- Poda que elimina soluciones válidas.
- No definir caso solución.
- Confundir poda con “saltar porque parece malo”.

# 10. Ejercicios
Combinaciones, laberinto, permutaciones y asignación con restricciones.

# 11. Reto
Diseña asignador pequeño. Dibuja árbol, restricciones y podas justificadas.

# 12. Autoevaluación
1. ¿Qué es estado parcial?
2. ¿Por qué deshacer?
3. ¿Qué es poda?
4. ¿Primera solución y todas requieren mismo flujo?
5. ¿Por qué puede ser costoso?

# 13. Checklist
- [ ] Defino estado.
- [ ] Enumero opciones.
- [ ] Valido.
- [ ] Deshago.
- [ ] Justifico poda.

Continúa con programación dinámica.
