# Unidad 25 — Proyecto final

## Propósito

Demostrar que puedes convertir un problema abierto en una solución algorítmica explicable, comprobable y analizada.

El proyecto no comienza con código.

# Proyecto — Red de rutas y tareas

Construye una aplicación que modele elementos conectados como una red y resuelva varias operaciones.

Puedes adaptar el dominio:
- ciudades;
- puntos de un campus ficticio;
- estaciones;
- dependencias de tareas;
- red de recursos ficticia.

Evita datos personales reales.

# Etapa 1 — Define el problema

Escribe:
- contexto;
- usuario;
- objetivo;
- alcance;
- qué queda fuera.

Formula al menos cinco preguntas que tu solución debe responder.

# Etapa 2 — Entradas, salidas y restricciones

Ejemplo:
```text
entrada: origen, destino, conexiones
salida: existe/no existe camino
restricción: nodos deben existir
```

Incluye casos inválidos.

# Etapa 3 — Modelo

Define:
- qué representa un nodo;
- qué representa una arista;
- dirigido/no dirigido;
- ponderado/no ponderado;
- representación elegida.

Justifica lista/matriz de adyacencia u otra estructura.

# Etapa 4 — Operaciones básicas

Implementa operaciones para:
- agregar/consultar elementos;
- agregar conexiones;
- validar entradas.

Separa estas responsabilidades de los algoritmos de recorrido cuando sea razonable.

# Etapa 5 — Alcanzabilidad

Implementa BFS o DFS para responder si existe conexión.

Antes:
1. escribe pseudocódigo;
2. traza un caso;
3. explica visitados.

# Etapa 6 — Comparación BFS/DFS

Implementa ambos para al menos una operación.

No concluyas “X es mejor” solo porque una ejecución tardó menos.

Compara:
- orden;
- estructura auxiliar;
- trabajo;
- memoria/frente;
- propiedad que necesitas.

# Etapa 7 — Búsqueda/organización adicional

Incluye una colección asociada al dominio que necesite búsqueda.

Decide:
- lineal;
- ordenar+binaria;
- conjunto/mapa;
según cantidad de consultas y requisitos.

# Etapa 8 — Casos de prueba

Incluye:
- normal;
- límite;
- inválido;
- sin solución;
- ciclo;
- nodo aislado;
- grafo desconectado.

Para cada prueba indica resultado esperado.

# Etapa 9 — Complejidad

Define variables:
```text
V = vértices
E = aristas
n = tamaño de colección adicional
```

Analiza operaciones principales. No escribas Big O sin explicar qué representa cada símbolo.

# Etapa 10 — Alternativas

Selecciona una operación y diseña dos soluciones.

Ejemplos:
- búsqueda lineal vs estructura indexada;
- BFS vs DFS para alcanzabilidad;
- lista vs conjunto para visitados.

Compara corrección, costo y claridad.

# Etapa 11 — Experimento

Elige una comparación donde medir aporte.

Documenta:
- tamaños;
- datos;
- repeticiones;
- métricas;
- resultados;
- interpretación.

Separa medición de complejidad teórica.

# Etapa 12 — Lenguaje

Puedes implementar en Python, Java o JavaScript.

La elección debe justificarse por entorno/objetivo; **no cambia los criterios algorítmicos**.

# Etapa 13 — README reproducible

Otra persona debe poder:
1. comprender el problema;
2. ejecutar;
3. cargar/usar datos de ejemplo;
4. reproducir pruebas;
5. comprender algoritmos;
6. interpretar resultados.

# Etapa 14 — Revisión final

Usa `CHECKLIST.md` y `RUBRICA.md`.

Pregúntate:
- ¿puedo dibujar el modelo?
- ¿puedo trazar BFS/DFS?
- ¿cada estructura tiene razón?
- ¿las pruebas intentan romper la solución?
- ¿Big O coincide con implementación?
- ¿otra persona puede reproducirla?

# Entregables

- descripción;
- requisitos/restricciones;
- modelo;
- pseudocódigo;
- implementación;
- pruebas;
- resultados;
- análisis de complejidad;
- comparación;
- experimento cuando corresponda;
- README.

Consulta también `PLANTILLA_PROYECTO.md`.

# Extensiones opcionales

Solo después de cumplir el núcleo:
- visualización;
- lectura de archivos;
- interfaz;
- persistencia;
- algoritmos de rutas con peso, si puedes explicar sus supuestos.

Una extensión no compensa fundamentos incompletos.

# Cierre

> Un buen algoritmo no es solamente el que produce una respuesta: es el que puedes explicar, comprobar, comparar y mejorar.
