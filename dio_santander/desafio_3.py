saldo_total = int(input())
valor_saque = int(input())

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.
if saldo_total >= valor_saque:
  saldo_atualizado = saldo_total - valor_saque
  print(f"Saque realizado com sucesso! Novo saldo: {saldo_atualizado}")
else:
  print("Saldo insuficiente. Saque nao realizado!")