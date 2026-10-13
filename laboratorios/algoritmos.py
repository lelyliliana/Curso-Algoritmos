"""Algoritmos de referencia didáctica; solo biblioteca estándar."""

from collections import deque, Counter
from math import factorial


def natural(n):
    if type(n) is not int or n < 0:
        raise ValueError("Se requiere entero no negativo")
    return n


def conversion_tiempo(segundos):
    natural(segundos)
    h, r = divmod(segundos, 3600)
    m, s = divmod(r, 60)
    return h, m, s


def descuento(centavos):
    natural(centavos)
    return centavos - (centavos * 10 // 100 if centavos >= 10000 else 0)


def resumen(valores):
    if not valores:
        return {"cantidad": 0, "suma": 0, "minimo": None, "maximo": None}
    return {
        "cantidad": len(valores),
        "suma": sum(valores),
        "minimo": min(valores),
        "maximo": max(valores),
    }


def es_par(n):
    return n % 2 == 0


def suma_filas(matriz):
    if not matriz:
        return []
    ancho = len(matriz[0])
    if any(len(f) != ancho for f in matriz):
        raise ValueError("Matriz no rectangular")
    return [sum(f) for f in matriz]


def palindromo(texto):
    normal = "".join(c.casefold() for c in texto if c.isalnum())
    return normal == normal[::-1]


def busqueda_lineal(a, x):
    for i, v in enumerate(a):
        if v == x:
            return i
    return -1


def busqueda_binaria(a, x):
    """Precondición: a ordenado ascendente. Devuelve primera coincidencia."""
    bajo, alto = 0, len(a)
    while bajo < alto:
        medio = (bajo + alto) // 2
        if a[medio] < x:
            bajo = medio + 1
        else:
            alto = medio
    return bajo if bajo < len(a) and a[bajo] == x else -1


def insercion(a):
    b = list(a)
    for i in range(1, len(b)):
        valor = b[i]
        j = i - 1
        while j >= 0 and b[j] > valor:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = valor
    return b


def merge_sort(a):
    if len(a) < 2:
        return list(a)
    m = len(a) // 2
    iz = merge_sort(a[:m])
    de = merge_sort(a[m:])
    i = j = 0
    out = []
    while i < len(iz) and j < len(de):
        if iz[i] <= de[j]:
            out.append(iz[i])
            i += 1
        else:
            out.append(de[j])
            j += 1
    return out + iz[i:] + de[j:]


def quick_sort(a):
    """Referencia con listas temporales; no es quicksort in-place."""
    if len(a) < 2:
        return list(a)
    pivote = a[len(a) // 2]
    menores = [x for x in a if x < pivote]
    iguales = [x for x in a if x == pivote]
    mayores = [x for x in a if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)


def factorial_rec(n):
    natural(n)
    if n > 200:
        raise ValueError("Limite didactico de recursion: 200")
    return 1 if n < 2 else n * factorial_rec(n - 1)


def contar_busquedas(a, x):
    comparaciones = 0
    for v in a:
        comparaciones += 1
        if v == x:
            break
    return comparaciones


def balanceado(texto):
    pila = []
    pares = {")": "(", "]": "[", "}": "{"}
    for c in texto:
        if c in "([{":
            pila.append(c)
        elif c in pares:
            if not pila or pila.pop() != pares[c]:
                return False
    return not pila


def frecuencias(texto):
    return dict(sorted(Counter(texto.split()).items()))


def inorden(arbol):
    if arbol is None:
        return []
    valor, iz, de = arbol
    return inorden(iz) + [valor] + inorden(de)


def bfs(grafo, inicio):
    if inicio not in grafo:
        raise ValueError("Nodo inicial inexistente")
    for vecinos in grafo.values():
        if any(v not in grafo for v in vecinos):
            raise ValueError("Arista hacia nodo no declarado")
    cola = deque([inicio])
    dist = {inicio: 0}
    padre = {inicio: None}
    while cola:
        u = cola.popleft()
        for v in grafo[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                padre[v] = u
                cola.append(v)
    return dist, padre


def ruta(padres, destino):
    if destino not in padres:
        return None
    out = []
    while destino is not None:
        out.append(destino)
        destino = padres[destino]
    return out[::-1]


def maximo_dividir(a):
    if not a:
        raise ValueError("No hay maximo en lista vacia")

    def resolver(lo, hi):
        if hi - lo == 1:
            return a[lo]
        m = (lo + hi) // 2
        return max(resolver(lo, m), resolver(m, hi))

    return resolver(0, len(a))


def intervalos_voraz(intervalos):
    """Intervalos [inicio,fin), inicio<fin. Retorna selección por fin creciente."""
    if any(
        type(inicio) is not int or type(fin) is not int or inicio >= fin
        for inicio, fin in intervalos
    ):
        raise ValueError("Intervalo vacio o invertido")
    elegidos = []
    ultimo = None
    for inicio, fin in sorted(intervalos, key=lambda x: (x[1], x[0])):
        if ultimo is None or inicio >= ultimo:
            elegidos.append((inicio, fin))
            ultimo = fin
    return elegidos


def cambio_voraz(monedas, total):
    natural(total)
    if not monedas or any(type(x) is not int or x <= 0 for x in monedas):
        raise ValueError("Monedas positivas")
    resultado = []
    for m in sorted(set(monedas), reverse=True):
        cantidad, total = divmod(total, m)
        resultado.extend([m] * cantidad)
    return resultado if total == 0 else None


def subconjuntos_suma(valores, objetivo):
    natural(objetivo)
    if any(type(x) is not int or x <= 0 for x in valores):
        raise ValueError("Valores enteros positivos para esta poda")
    soluciones = []
    elegidos = []

    def explorar(i, suma):
        if suma == objetivo:
            soluciones.append(tuple(elegidos))
            return
        if i == len(valores) or suma > objetivo:
            return
        elegidos.append(i)
        explorar(i + 1, suma + valores[i])
        elegidos.pop()
        explorar(i + 1, suma)

    explorar(0, 0)
    return soluciones


def cambio_dp(monedas, total):
    natural(total)
    if not monedas or any(type(x) is not int or x <= 0 for x in monedas):
        raise ValueError("Monedas positivas")
    monedas = sorted(set(monedas))
    inf = total + 1
    dp = [0] + [inf] * total
    prev = [None] * (total + 1)
    for s in range(1, total + 1):
        for m in monedas:
            if m <= s and dp[s - m] + 1 < dp[s]:
                dp[s] = dp[s - m] + 1
                prev[s] = m
    if dp[total] == inf:
        return None
    usados = []
    while total:
        m = prev[total]
        usados.append(m)
        total -= m
    return usados


def escaleras(n):
    natural(n)
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def reservar(solicitudes, capacidad):
    natural(capacidad)
    if len(set(solicitudes)) != len(solicitudes):
        raise ValueError("ID duplicado")
    return list(solicitudes[:capacidad]), list(solicitudes[capacidad:])


def demostracion(unidad):
    a = [4, 1, 3, 1]
    g = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": [], "E": []}
    if unidad == 1:
        return {
            "entrada": [18, 20, 17],
            "regla": "admitir edad >=18",
            "salida": [x for x in [18, 20, 17] if x >= 18],
        }
    if unidad == 2:
        return {
            "entrada": 7,
            "pseudocodigo": "SI n MOD 2 = 0 ENTONCES par SINO impar",
            "salida": "par" if es_par(7) else "impar",
        }
    if unidad == 3:
        return {"segundos": 3661, "hms": conversion_tiempo(3661)}
    if unidad == 4:
        return {"centavos": 10000, "a_pagar": descuento(10000)}
    if unidad == 5:
        return resumen([4, -2, 7, 0])
    if unidad == 6:
        return {"entradas": [0, 1, -2], "par": [es_par(x) for x in [0, 1, -2]]}
    if unidad == 7:
        return {"entrada": a, "salida": resumen(a), "entrada_conservada": a}
    if unidad == 8:
        return {"matriz": [[1, 2], [3, 4]], "suma_filas": suma_filas([[1, 2], [3, 4]])}
    if unidad == 9:
        return {
            "texto": "Anita lava la tina",
            "palindromo": palindromo("Anita lava la tina"),
        }
    if unidad == 10:
        return {
            "lista": [1, 1, 3, 4],
            "x": 1,
            "lineal": busqueda_lineal([1, 1, 3, 4], 1),
            "binaria": busqueda_binaria([1, 1, 3, 4], 1),
        }
    if unidad == 11:
        return {"entrada": a, "insercion": insercion(a), "entrada_conservada": a}
    if unidad == 12:
        return {"merge": merge_sort(a), "quick": quick_sort(a), "entrada_conservada": a}
    if unidad == 13:
        return {"n": 5, "factorial": factorial_rec(5)}
    if unidad == 14:
        return {
            "n": 8,
            "inicio": contar_busquedas(list(range(8)), 0),
            "ausente": contar_busquedas(list(range(8)), 99),
        }
    if unidad == 15:
        return {
            "n": [8, 16, 32],
            "peor_lineal": [contar_busquedas(list(range(n)), -1) for n in [8, 16, 32]],
        }
    if unidad == 16:
        return {
            "valido": balanceado("([{}])"),
            "invalido": balanceado("([)]"),
            "cola_fifo": list(deque(["A", "B", "C"])),
        }
    if unidad == 17:
        return frecuencias("rojo azul rojo verde azul rojo")
    if unidad == 18:
        return {"inorden": inorden((2, (1, None, None), (3, None, None)))}
    if unidad == 19:
        dist, padres = bfs(g, "A")
        return {
            "distancias": dist,
            "ruta_D": ruta(padres, "D"),
            "ruta_E": ruta(padres, "E"),
        }
    if unidad == 20:
        return {"entrada": [-5, -2, -9, -1], "maximo": maximo_dividir([-5, -2, -9, -1])}
    if unidad == 21:
        return {
            "intervalos": intervalos_voraz([(0, 3), (1, 2), (2, 4), (3, 5), (4, 6)]),
            "greedy_cambio": cambio_voraz([1, 3, 4], 6),
        }
    if unidad == 22:
        return {
            "valores": [2, 3, 5],
            "objetivo": 5,
            "indices_solucion": subconjuntos_suma([2, 3, 5], 5),
        }
    if unidad == 23:
        return {
            "minimo_cambio": cambio_dp([1, 3, 4], 6),
            "formas_escaleras_5": escaleras(5),
        }
    if unidad == 24:
        return {
            "greedy": cambio_voraz([1, 3, 4], 6),
            "dp": cambio_dp([1, 3, 4], 6),
            "criterio": "minimo numero de monedas",
        }
    if unidad == 25:
        confirmados, espera = reservar(["S01", "S02", "S03", "S04"], 2)
        return {"confirmados": confirmados, "espera": espera}
    raise ValueError("Unidad debe estar entre 1 y 25")
