saldo = 2500
saque = float(input("qual o valor: "))

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")