def contarPares(n):
    contador = 0
    for i in range(n):
        if i % 2 == 0:
            print(i)
            contador.append(i)

    return contador

def comparoLista(a, b):

    sizeA = len(a)
    sizeB = len (b)
    comparasion = 0

    if sizeA < sizeB:
        comparasion = -1
    elif sizeA > sizeB:
        comparasion = 1

    return comparasion