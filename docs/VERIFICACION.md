# Verificación de Algoritmos 1.1

La validación distingue ejecución, tests de propiedades y argumentos de corrección. No se declara superioridad de rendimiento a partir de una salida ni un tiempo aislado.

## Cómo reproducir

Desde raíz ejecuta los comandos de ENTORNO.md. Las pruebas de Python usan unittest de biblioteca estándar; las comparativas requieren JDK/Node.

## Resultados (2026-10-13)

- Los **25 casos completos de Python** ejecutaron y produjeron JSON válido.
- Las **21 pruebas automáticas** de unittest aprobaron. Incluyen enumeraciones de entradas pequeñas, búsqueda/ordenamiento, grafos con ciclos, intervalos óptimos, subconjuntos, cambio mínimo y asignación FIFO.
- **9 ejemplos Java** compilaron con perfil Java 21 y ejecutaron; **9 ejemplos JavaScript** pasaron revisión de sintaxis y ejecutaron.
- **13 propiedades adicionales en Java y 13 en JavaScript** aprobaron: contraejemplo greedy, mínimo/imposibilidad de cambio, casos de backtracking, datos inválidos, ordenamiento y preservación de entrada.
- Catálogo, laboratorios, soluciones y enlaces locales revisados sin archivos faltantes.

Entorno utilizado: Python 3.12.14, JDK 21.0.12.1 y Node.js 24.19.0. No hay paquetes externos en los programas ni en las pruebas del curso. Los formateadores de edición no son dependencias necesarias para estudiar.

Los oráculos pequeños son independientes: sorted para ordenamiento, enumeración de máscaras para subconjuntos, cantidades de monedas para mínimo y selecciones compatibles para intervalos. No se sustituyó el algoritmo por la misma implementación bajo otro nombre para declararlo correcto.

## Límites

Las pruebas agotan dominios pequeños declarados, no todas las entradas posibles. Los ejemplos comparativos compilan y se ejecutan dentro del dominio compartido. Los contratos, la complejidad y los argumentos del laboratorio complementan la evidencia empírica.
