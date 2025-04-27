while True:
    numero = int(input("informe um número: "))

    if numero == 10:
        break

    print(numero)

for numero in range(101):

    
    if numero % 2 == 0:
        continue
    print(numero, end = " ")