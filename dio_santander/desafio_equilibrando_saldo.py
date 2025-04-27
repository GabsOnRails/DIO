saldo_atual = float(1000.00)
mensagem_inicial = print((f"Olá, seja bem vindo ao banco Thor Peixinho & Jack Tubarão! Seu saldo atual é de: R$ {saldo_atual:.2f}!"))
opcao = (input("No que podemos te ajudar hoje? \n[1]- Depósito [2]- Saque [3]- Sair\n:" ))
#Mensagem de boas vindas
if opcao == "1":
   deposito =float(input("Qual valor deseja depositar?\n:R$ "))
   saldo_atualizado1 = saldo_atual + deposito
   saldo_com_deposito = input(f"Seu saldo atual é de:R$ {saldo_atualizado1:.2f}!")
   saque1 = input("Deseja realizar um saque?\n[1]- Sim [2]- Não\n:")
   if saque1 == "1":
    valor_saque = float(input("Qual valor deseja sacar?\n:R$ "))
    if valor_saque > saldo_atualizado1:
        emprestimo =(input("O valor solicitado é maior do que seu saldo atual.\nDeseja realizar um empréstimo: [1]- Sim [2]- Não\n:"))
        if emprestimo == "1":
            emprestimo = float(input("Qual valor do empréstimo?\n:R$ "))
            saldo_atual_emprestimo = saldo_atualizado1 + emprestimo
            mensagem_emprestimo = input(f"Seu valor atual é de: R$ {saldo_atual_emprestimo:.2f}\nDeseja realizar um saque?\n[1]- Sim [2]- Não\n:")
            if mensagem_emprestimo == "1":
                saque_emprestimo = float(input("Qual valor deseja sacar?\n:R$ "))
                saldo_atualizado_emprestimo = saldo_atual_emprestimo - saque_emprestimo
                print(f"Seu saldo atual é de:R$ {saldo_atualizado_emprestimo:.2f}!\nObrigado por utilizar nossos serviços.")
            else:
                print(f"Seu saldo atual é de:R$ {saldo_atual_emprestimo:.2f}!\nObrigado por utilizar nossos serviços.")
        else:
            print(f"Seu saldo atual é de:R$ {saldo_atualizado1:.2f}!\nObrigado por usar nossos serviços.")
    else:
       print(f"Seu saldo atual é de:R$ {saldo_atualizado1-valor_saque:.2f}!\nObrigado por utilizar nossos serviços.")
   else:
       print(f"Seu saldo atual é de:R$ {saldo_atualizado1:.2f}!\nObrigado por usar nossos serviços.")
    
#saque
elif opcao == "2":
    valor_saque = float(input("Qual valor deseja sacar?\n:R$ "))
    if valor_saque > saldo_atual:
        mensagem_saque = input("O valor é maior que seu saldo atual. Deseja fazer um depósito?\n[1]- Sim [2]- Não\n:")
        if mensagem_saque == "1":
            deposito2 =float(input("Qual valor deseja depositar?\n:R$ "))
            saldo_atualizado2 = saldo_atual + deposito2
            saldo_com_deposito2 = input(f"Seu saldo atual é de:R$ {saldo_atualizado2:.2f}!")
            saque2 = input("Deseja realizar um saque?\n[1]- Sim [2]- Não\n:")
            if saque2 == "1":
                valor_saque2 = float(input("Qual valor deseja sacar?\n:R$ "))
                if valor_saque2 > saldo_atualizado2:
                    print("Valor maior que o permitido. Por favor começar a operação novamente!")
                else:
                    print(f"Seu saldo atual é de:R$ {saldo_atualizado2 - valor_saque2:.2f}!\nObrigado por utilizar nossos serviços.")
    
            else:
                print(f"Seu saldo atual é de:R$ {saldo_atualizado2:.2f}!\nObrigado por utilizar nossos serviços.")
        else:
            print("Obrigado por utilizar nossos serviços!")
    else:
        print(f"Seu valor atual é de:R$ {saldo_atual-valor_saque:.2f}!\nObrigado por utilizar nossos serviços.")
            
else:
    print("Obrigado por utilizar nossos serviços!")













