numero = 29
eh_primo = True
divisor = 2

if numero < 2:
    eh_primo = False
else:
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            eh_primo = False
            break
        divisor += 1

if eh_primo:
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")