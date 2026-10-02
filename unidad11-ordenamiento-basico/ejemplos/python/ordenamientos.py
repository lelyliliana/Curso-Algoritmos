def burbuja(datos):
    a = datos.copy()
    for limite in range(len(a)-1, 0, -1):
        for i in range(limite):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a

def seleccion(datos):
    a = datos.copy()
    for i in range(len(a)-1):
        menor = i
        for j in range(i+1, len(a)):
            if a[j] < a[menor]:
                menor = j
        a[i], a[menor] = a[menor], a[i]
    return a

def insercion(datos):
    a = datos.copy()
    for i in range(1, len(a)):
        actual = a[i]
        j = i - 1
        while j >= 0 and a[j] > actual:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = actual
    return a
