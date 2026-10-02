def busqueda_lineal(datos, objetivo):
    for i, valor in enumerate(datos):
        if valor == objetivo:
            return i
    return -1

def busqueda_binaria(datos, objetivo):
    izquierda, derecha = 0, len(datos) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if datos[medio] == objetivo:
            return medio
        if datos[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

datos = [2, 5, 8, 12, 16, 23, 38]
print(busqueda_lineal(datos, 16))
print(busqueda_binaria(datos, 16))
