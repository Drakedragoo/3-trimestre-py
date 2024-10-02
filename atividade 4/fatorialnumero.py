numero = 5
fatorial = 1
contador = numero

while contador > 0:
    fatorial *= contador
    contador -= 1

print(f"O fatorial de {numero} é", fatorial)