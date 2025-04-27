saldo_inicial = 1000
mensagem_inicial=int(input("Sejam bem vindos ao Banco Thor Peixinho & Jack Tubarão.\nNo que podemos te ajudar hoje?\n[1]- Depósito [2]- Saque [3]- Empréstimo\nDigite a opção: "))
   #depósito
if mensagem_inicial == 1:
    valor_deposito = float(input(f"Seu saldo atual é de R${saldo_inicial}!\nQual valor deseja depositar?\nR$"))
    if valor_deposito >0:
        saldo_deposito = saldo_inicial+valor_deposito
        print(f"Depósito realizado com sucesso! Seu saldo atual é de {saldo_deposito:.2f}\nDeseja realizar outra operação?.")
    outras_operacoes = int(input("[1]- Depósito [2]- Saque [3]- Sair\n"))
    if outras_operacoes == 1:
            valor_deposito2=float(input(f"Seu saldo atual é de R${saldo_deposito}!\nQual valor deseja depositar?\nR$"))
            if valor_deposito2 >0:
                print(f"Depósito realizado com sucesso! Seu saldo atual é de {saldo_deposito+valor_deposito2:.2f}\nObrigado por utilizar nossos serviços.")
    elif outras_operacoes == 2:
        valor_saque2 = float(input(f"Seu saldo atual é de R${saldo_deposito}!\nQual valor deseja sacar?\nR$"))
        if valor_saque2 > saldo_deposito:
            print("Valor inválido. Por favor começar a operação novamente!") 
        elif valor_saque2 < saldo_deposito:
            print(f"Saque realizado com sucesso! Seu saldo atual é de R${saldo_deposito-valor_saque2:.2f}\nObrigado por utilizar nossos serviços.")
    elif outras_operacoes == 3:
         print(f"Seu saldo atual é de R${saldo_deposito}\nObrigado por utilizar nossos serviços.")
    #saque
elif mensagem_inicial == 2:
    valor_saque = float(input(f"Seu saldo atual é de R${saldo_inicial}!\nQual valor deseja sacar?\nR$")) 
    if valor_saque > saldo_inicial:
        print("Valor de saque maior que o saldo atual. Por favor começar a operação novamente.")
    elif valor_saque < saldo_inicial:
        saldo_saque = saldo_inicial - valor_saque
        print(f"Saque realizado com sucesso! Seu saldo atual é de R${saldo_saque:.2f}\nDeseja realizar outra operação?")
        outras_operacoes = int(input("[1]- Depósito [2]- Saque [3]- Sair\n"))
        if outras_operacoes == 1:
            valor_deposito3=float(input(f"Seu saldo atual é de R${saldo_saque}!\nQual valor deseja depositar?\nR$"))
            if valor_deposito3 >0:
                print(f"Depósito realizado com sucesso! Seu saldo atual é de {saldo_saque+valor_deposito3:.2f}\nObrigado por utilizar nossos serviços.")
        elif outras_operacoes == 2:
            valor_saque3 = float(input(f"Seu saldo atual é de R${saldo_saque}!\nQual valor deseja sacar?\nR$"))
            if valor_saque3 > saldo_saque:
                print("Valor de saque maior que o saldo atual. Por favor começar a operação novamente!") 
            elif valor_saque3 < saldo_saque:
                print(f"Saque realizado com sucesso! Seu saldo atual é de R${saldo_saque-valor_saque3:.2f}\nObrigado por utilizar nossos serviços.")
        elif outras_operacoes == 3:
         print(f"Seu saldo atual é de R${saldo_saque}\nObrigado por utilizar nossos serviços.")
    #emprestimo
elif mensagem_inicial == 3:
    valor_emprestimo = float(input(f"Seu saldo atual é de R${saldo_inicial}!\nQual valor do empréstimo?\nR$"))
    saldo_emprestimo = saldo_inicial+valor_emprestimo
    print(f"Empréstimo realizado com sucesso! Seu saldo atual é de R${saldo_emprestimo:.2f}\nDeseja realizar outra operação?")
    outras_operacoes = int(input("[1]- Depósito [2]- Saque [3]- Sair\n"))
    if outras_operacoes == 1:
        valor_deposito2=float(input(f"Seu saldo atual é de R${saldo_emprestimo}!\nQual valor deseja depositar?\nR$"))
        if valor_deposito2 >0:
            print(f"Depósito realizado com sucesso! Seu saldo atual é de {saldo_emprestimo+valor_deposito2:.2f}\nObrigado por utilizar nossos serviços.")
    elif outras_operacoes == 2:
        valor_saque2 = float(input(f"Seu saldo atual é de R${saldo_emprestimo}!\nQual valor deseja sacar?\nR$")) 
        if valor_saque2 > saldo_emprestimo:
            print("Valor de saque maior que saldo atual. Por favor começar a operação novamente.")
        elif valor_saque2 < saldo_emprestimo:
            print(f"Saque realizado com sucesso! Seu saldo atual é de R${saldo_emprestimo-valor_saque2:.2f}\nObrigado por utilizar nossos serviços.")
    elif outras_operacoes == 3:
         print(f"Seu saldo atual é de R${saldo_emprestimo}\nObrigado por utilizar nossos serviços.")
else:
    print("Opção não encontrada. Por favor comece a operação novamente!")