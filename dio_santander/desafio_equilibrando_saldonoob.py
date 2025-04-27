saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())


atualizado = saldo_atual + valor_deposito
saque = atualizado - valor_retirada
print(f"Saldo atualizado na conta: {saque}")

    