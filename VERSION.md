# Versión 1.1: problemas resueltos y verificación

Fecha: 2026-10-13.

Se conserva el recorrido 1–25 y los ejemplos originales. Se añaden 25 laboratorios,25 soluciones razonadas y 25 casos completos en Python, junto con versiones Java/JavaScript de las tres estrategias avanzadas.

## Qué mejoró

Contratos, fronteras, tablas de ejecución, casos vacíos/invalidación, costos reales y preservación de entrada. Greedy distingue una regla correcta para interva los de una heurística que falla en cambio de monedas. Backtracking conserva índices y deshace elecciones. DP incluye recurrencia, estados imposibles y reconstrucción de una combinación mínima.

Las unidades 24/25 incorporan comparación bajo un criterio y una base funcional FIFO para asignar cupos. La base no se presenta como una aplicación web con usuarios o persistencia.

## Límites de implementación

La búsqueda binaria exige orden ascendente; verificarlo tiene costo adicional. Quick Sort usa listas temporales, no partición in-place; inorder utiliza concatenaciones y puede tener costo cuadrático en árboles sesgados. Los conteos experimentales no son benchmarks de rendimiento. DP de monedas es pseudopolinómica respecto al total representado en bits. La recursión y el número de soluciones tienen límites prácticos.

Consulta docs/VERIFICACION.md para pruebas realizadas y docs/EVIDENCIAS.md para conservar tu propia argumentación.
