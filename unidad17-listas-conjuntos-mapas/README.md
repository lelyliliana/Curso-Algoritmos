# Unidad 17 — Listas, conjuntos y mapas

## Qué aprenderás
Elegir estructuras según orden, duplicados, pertenencia y asociación clave→valor.

# 1. No existe una estructura “mejor”

Canciones en orden y repetidas → lista.  
Etiquetas únicas → conjunto.  
Frecuencia de palabras → mapa.

La estructura depende de las operaciones.

# 2. Lista

```text
[A,B,A,C]
```

Representa una secuencia y normalmente permite repetidos. Es apropiada cuando posición/orden forman parte del problema.

# 3. Conjunto

```text
{A,B,C}
```

Modela unicidad y pertenencia.

Operaciones conceptuales:
- unión;
- intersección;
- diferencia;
- pertenencia.

No dependas de un orden si la abstracción/implementación elegida no lo garantiza.

# 4. Mapa

Relaciona claves con valores:

```text
"ana" → 4
"luis" → 7
```

Una clave no es lo mismo que una posición.

# 5. Frecuencias

Entrada:
```text
sol luna sol mar sol
```

```text
frecuencia ← mapa vacío

PARA CADA palabra
    SI palabra existe
        frecuencia[palabra] ← frecuencia[palabra] + 1
    SINO
        frecuencia[palabra] ← 1
    FIN SI
FIN
```

Resultado:
```text
sol→3, luna→1, mar→1
```

# 6. Agrupación

Transacciones:
```text
comida 10
transporte 20
comida 15
```

Mapa:
```text
comida→25
transporte→20
```

# 7. Complejidad depende de implementación

Mapas/conjuntos pueden implementarse con hashing, árboles u otras estructuras.

No memorices “mapa = O(1)” sin especificar operación, implementación y caso.

# 8. Práctica guiada

Con una lista de nombres repetidos:
1. conserva secuencia;
2. obtén únicos;
3. cuenta frecuencia;
4. identifica más frecuente.

Observa que cada salida sugiere una estructura.

# 9. Errores frecuentes
- Conjunto cuando necesitas duplicados.
- Lista para búsquedas repetidas por clave sin analizar alternativas.
- Asumir orden.
- Confundir clave/índice.
- Citar complejidad sin implementación.

# 10. Ejercicios
Eliminar duplicados, intersección, frecuencias, agenda y agrupación por categoría.

# 11. Reto
Procesa transacciones y genera total por categoría. Justifica el mapa.

# 12. Autoevaluación
1. ¿Cuándo lista?
2. ¿Qué modela conjunto?
3. ¿Qué modela mapa?
4. ¿Clave e índice son iguales?
5. ¿Por qué complejidad depende de implementación?

# 13. Checklist
- [ ] Elijo estructura por operaciones.
- [ ] Manejo unicidad.
- [ ] Construyo frecuencias.
- [ ] No asumo orden/costo sin contrato.

Continúa con árboles.
