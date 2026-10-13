import unittest, sys, itertools, math
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "laboratorios"))
import algoritmos as a


class Fundamentos(unittest.TestCase):
    def test_conversion_fronteras(self):
        for s, hms in [
            (0, (0, 0, 0)),
            (3599, (0, 59, 59)),
            (3600, (1, 0, 0)),
            (3661, (1, 1, 1)),
            (90000, (25, 0, 0)),
        ]:
            self.assertEqual(a.conversion_tiempo(s), hms)
        for invalido in [-1, True, 1.5]:
            with self.assertRaises(ValueError):
                a.conversion_tiempo(invalido)

    def test_descuento_fronteras(self):
        self.assertEqual(
            [a.descuento(x) for x in [0, 9999, 10000, 10001, 10009]],
            [0, 9999, 9000, 9001, 9009],
        )

    def test_resumen_vacio_y_negativos(self):
        self.assertEqual(
            a.resumen([]), {"cantidad": 0, "suma": 0, "minimo": None, "maximo": None}
        )
        self.assertEqual(a.resumen([-5, -2])["maximo"], -2)

    def test_matrices(self):
        self.assertEqual(a.suma_filas([[1, 2], [3, 4]]), [3, 7])
        self.assertEqual(a.suma_filas([[], []]), [0, 0])
        with self.assertRaises(ValueError):
            a.suma_filas([[1], [2, 3]])

    def test_palindromo_contrato(self):
        for t in ["", "Anita lava la tina", "a,b,a"]:
            self.assertTrue(a.palindromo(t))
        self.assertFalse(a.palindromo("ab"))
        self.assertFalse(a.palindromo("Áa"))

    def test_busquedas_primera_coincidencia(self):
        for n in range(7):
            for xs in itertools.combinations_with_replacement(range(3), n):
                for x in range(-1, 4):
                    esperado = xs.index(x) if x in xs else -1
                    self.assertEqual(a.busqueda_lineal(xs, x), esperado)
                    self.assertEqual(a.busqueda_binaria(xs, x), esperado)

    def test_ordenamientos_oraculo_y_preservacion(self):
        for n in range(7):
            for datos in itertools.product(range(3), repeat=n):
                original = list(datos)
                for f in [a.insercion, a.merge_sort, a.quick_sort]:
                    self.assertEqual(f(original), sorted(datos))
                    self.assertEqual(original, list(datos))

    def test_factorial_dominio(self):
        for n in range(30):
            self.assertEqual(a.factorial_rec(n), math.factorial(n))
        for n in [-1, 201, True]:
            with self.assertRaises(ValueError):
                a.factorial_rec(n)

    def test_conteos(self):
        for n in range(1, 30):
            self.assertEqual(a.contar_busquedas(list(range(n)), -1), n)
            self.assertEqual(a.contar_busquedas(list(range(n)), 0), 1)

    def test_pila(self):
        for t in ["", "([{}])", "texto(a)[b]"]:
            self.assertTrue(a.balanceado(t))
        for t in ["([)]", "((", ")("]:
            self.assertFalse(a.balanceado(t))

    def test_frecuencias(self):
        self.assertEqual(a.frecuencias("rojo azul rojo"), {"azul": 1, "rojo": 2})

    def test_arbol_no_confundir_con_bst(self):
        self.assertEqual(a.inorden(None), [])
        self.assertEqual(a.inorden((2, (9, None, None), (3, None, None))), [9, 2, 3])

    def test_bfs_ciclos_aislados(self):
        g = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["A"], "E": []}
        dist, p = a.bfs(g, "A")
        self.assertEqual(dist, {"A": 0, "B": 1, "C": 1, "D": 2})
        self.assertEqual(a.ruta(p, "D"), ["A", "B", "D"])
        self.assertIsNone(a.ruta(p, "E"))
        with self.assertRaises(ValueError):
            a.bfs({"A": ["B"]}, "A")
        with self.assertRaises(ValueError):
            a.bfs(g, "F")

    def test_maximo_oraculo(self):
        for n in range(1, 6):
            for xs in itertools.product([-5, -2, 0], repeat=n):
                self.assertEqual(a.maximo_dividir(xs), max(xs))
        with self.assertRaises(ValueError):
            a.maximo_dividir([])


class Estrategias(unittest.TestCase):
    def test_intervalos_con_oraculo_exhaustivo(self):
        universo = [(i, j) for i in range(4) for j in range(i + 1, 5)]
        for size in range(5):
            for intervalos in itertools.combinations(universo, size):
                mejor = 0
                for k in range(size + 1):
                    for subset in itertools.combinations(intervalos, k):
                        orden = sorted(subset)
                        if all(
                            orden[i][1] <= orden[i + 1][0]
                            for i in range(len(orden) - 1)
                        ):
                            mejor = max(mejor, k)
                self.assertEqual(len(a.intervalos_voraz(intervalos)), mejor)
        with self.assertRaises(ValueError):
            a.intervalos_voraz([(1, 1)])
        with self.assertRaises(ValueError):
            a.intervalos_voraz([(float("nan"), 3)])

    def test_greedy_contraejemplo(self):
        self.assertEqual(a.cambio_voraz([1, 3, 4], 6), [4, 1, 1])
        self.assertIsNone(a.cambio_voraz([4, 3], 6))
        # Con [4,3],6 una solución existe [3,3] aunque greedy retornaNone.
        self.assertEqual(a.cambio_dp([4, 3], 6), [3, 3])

    def test_backtracking_indices_con_oraculo(self):
        for n in range(7):
            for valores in itertools.product([1, 2], repeat=n):
                for objetivo in range(7):
                    esperado = {
                        tuple(i for i in range(n) if mask >> i & 1)
                        for mask in range(1 << n)
                        if sum(valores[i] for i in range(n) if mask >> i & 1)
                        == objetivo
                    }
                    observado = a.subconjuntos_suma(valores, objetivo)
                    self.assertEqual(set(observado), esperado)
                    self.assertEqual(len(observado), len(esperado))
        with self.assertRaises(ValueError):
            a.subconjuntos_suma([2, -1], 1)

    def test_dp_con_oraculo_enumeracion(self):
        for monedas in [[1], [2], [1, 3, 4], [2, 5], [3, 4], [1, 1, 3]]:
            for total in range(13):
                # Enumeración independiente de cantidades; no usa recurrencia de DP.
                unicas = sorted(set(monedas))
                mejor = None
                for cantidades in itertools.product(
                    range(total + 1), repeat=len(unicas)
                ):
                    if sum(m * c for m, c in zip(unicas, cantidades)) == total:
                        cantidad = sum(cantidades)
                        mejor = cantidad if mejor is None else min(mejor, cantidad)
                result = a.cambio_dp(monedas, total)
                if mejor is None:
                    self.assertIsNone(result)
                else:
                    self.assertEqual(sum(result), total)
                    self.assertEqual(len(result), mejor)
                    self.assertTrue(all(m in unicas for m in result))

    def test_escaleras_con_enumeracion(self):
        def enumerar(n):
            return 1 if n == 0 else sum(enumerar(n - p) for p in [1, 2] if p <= n)

        for n in range(12):
            self.assertEqual(a.escaleras(n), enumerar(n))

    def test_monedas_invalidas(self):
        for f in [a.cambio_voraz, a.cambio_dp]:
            for monedas in [[], [0, 1], [-1, 2], [True, 1]]:
                with self.assertRaises(ValueError):
                    f(monedas, 3)

    def test_fifo_conserva_particion(self):
        for n in range(8):
            ids = [str(i) for i in range(n)]
            for capacidad in range(10):
                confirmados, espera = a.reservar(ids, capacidad)
                self.assertEqual(confirmados + espera, ids)
                self.assertEqual(len(confirmados), min(n, capacidad))
        with self.assertRaises(ValueError):
            a.reservar(["X", "X"], 2)


if __name__ == "__main__":
    unittest.main()
