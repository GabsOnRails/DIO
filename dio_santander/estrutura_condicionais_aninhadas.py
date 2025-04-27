conta_normal=False
conta_universitaria = False
saque = int(input("qual valor: "))
saldo = 600
cheque_especial = 250

if conta_normal:
    if saldo >= saque:
        print("saque realizado")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado com cheque especial")
    else:
        print("sem valor na conta")

elif conta_universitaria:
    if saldo >= saque:
        print("saque realizado!")
    else:
        print("sem limite")
        
else:
    print("o sistema nao reconheceu seu tipo de conta")

