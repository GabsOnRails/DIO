valor_de_saque = int(input("Qual valor"))
limite = 1500
limite_especial = 3000

if valor_de_saque <= limite:
    print("Valor sacado")
elif valor_de_saque < limite_especial:
    print("Limite especial usado")
else:
    print("Sem Saldo")