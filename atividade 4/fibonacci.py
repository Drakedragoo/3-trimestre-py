n1, n2 = 0, 1
contador = 0

while contador < 10:
    print(n1)
    proximo = n1 + n2
    n1 = n2
    n2 = proximo
    contador += 1