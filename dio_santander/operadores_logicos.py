saldo = 1500
saque = 300
limite = 210
conta_especial = True

exp = (saldo >= saque and saque <= limite ) or (conta_especial and saldo >= saque)
print(exp)

conta_normal_saldo_suficiente = (saldo >= saque and saque <=limite)
conta_especial = (conta_especial and saldo >= saque)
exp2 = conta_normal_saldo_suficiente or conta_especial
print(exp2)

