# Entorno para estudiar Algoritmos

[Curso](../README.md) · [Laboratorios](../laboratorios/README.md)

## Ruta inicial con Python

Los 25 casos nuevos requieren Python 3.10 o superior y solo biblioteca estándar. No necesitas instalar pandas, servicios, notebooks ni paquetes adicionales. Python representa enteros arbitrarios, pero su tamaño y costo siguen siendo finitos en una máquina real.

1. Descarga ZIP o clona el curso y extrae a una carpeta personal.
2. Comprueba tu ejecutor: `python --version`, `python3 --version` o `py -3 --version`, según la instalación de tu sistema.
3. Abre la primera unidad y predice salida antes de ejecutar.
4. Desde raíz ejecuta `python unidad01-pensamiento-algoritmico/ejemplos/caso_completo.py` (cambia únicamente el ejecutor si corresponde).
5. Sigue unidad→laboratorio→soluciones y conserva tus pruebas de escritorio.

Cada caso importa las funciones de laboratorios/algoritmos.py mediante la ruta de su propio archivo; no depende de variables globales de tu terminal. Ejecutar desde otra carpeta no cambia el contrato del caso.

## Comparación opcional entre lenguajes

Instala Java 21 (JDK, incluye javac/java) y Node.js 18 o superior si deseas ejecutar implementaciones comparativas. La ruta principal funciona con Python sin instalar los otros dos. Las unidades 21–23 contienen versiones completas de greedy, backtracking y DP; otras unidades conservan los ejemplos previos en Java/JavaScript.

Desde raíz crea una carpeta build con tu explorador o terminal. Ejecuta primero javac y después java, con nombres de archivo/clase indicados en el laboratorio. En Windows las barras de ruta de los ejemplos pueden sustituirse por las de tu terminal; no cambies el nombre de una clase pública sin modificar el archivo.

## Verificaciones del curso

Desde raíz, un comando por vez:

```text
python scripts/verificar_material.py
```

```text
python scripts/ejecutar_casos.py
```

```text
python -m unittest discover -s tests -v
```

Para una unidad: `python scripts/ejecutar_casos.py --unidad 23`. Las pruebas utilizan casos pequeños y referencias independientes de enumeración; no necesitan Internet.

El script comparativo opcional `python scripts/verificar_comparativos.py` requiere node, javac y java disponibles. Compila en carpeta temporal; no deja archivos.class entre las lecciones.

## Dominio y límites

Búsqueda binaria exige orden ascendente; comparar tiempos no elimina ese requisito. Backtracking puede producir una cantidad exponencial de soluciones. DP de monedas usa memoria proporcional al total: no pruebes montos gigantes como si la cota fuera logarítmica. Java y JavaScript fijan un dominio pequeño común para comparar sin desbordamientos; Python tampoco es una licencia para ignorar costo de memoria/recursión.

## Fuentes de los lenguajes

- [Python: tutorial](https://docs.python.org/3/tutorial/).
- [Java: aprendizaje y herramientas](https://dev.java/learn/).
- [Node.js: ejecutar programas](https://nodejs.org/en/learn/command-line/run-nodejs-scripts-from-the-command-line).

[Verificación realizada](VERIFICACION.md) · [Plantilla de evidencias](EVIDENCIAS.md).
