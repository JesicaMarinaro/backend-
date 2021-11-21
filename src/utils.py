def contarPares(n):
    contador = 0
    for i in range(n):
        if i % 2 == 0:
            print(i)
            contador.append(i)

    return contador