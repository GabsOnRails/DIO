saldo_atual = float(1000.00)
mensagem_inicial = print((f"Olá, seja bem vindo ao banco Thor Peixinho & Jack Tubarão! Seu saldo atual é de: R$ {saldo_atual:.2f}!"))
opcao = (input("No que podemos te ajudar hoje? \n[1]- Depósito [2]- Saque [3]- Empréstimo\n:" ))
#Mensagem de boas vindas

#primeiro bloco
if opcao == "1":
    deposito = float(input("Qual valor deseja depositar?\n:R$"))
    saldo_deposito = saldo_atual + deposito
    mensagem = input(f"Seu saldo atual é de: R${saldo_deposito:.2f}!\nDeseja realizar um saque? [1]- Sim [2]- Não\n:")
    #saque
    if mensagem == "1":
        saque = float(input("Qual valor deseja sacar?\n:R$"))
        if saque > saldo_deposito:
            mensagem_saque = input("Seu saldo é menor que o valor de saque. Deseja fazer um empréstimo?\n[1]- Sim [2]- Não\n:")
            if mensagem_saque == "1":
                #emprestimo
                emprestimo = float(input("Qual o valor do empréstimo?\nR$:"))
                saldo_com_emprestimo = saldo_deposito + emprestimo
                mensagem_emprestimo = input(f"Seu saldo atual é de: R${saldo_com_emprestimo:.2f}!\nDeseja realizar um saque [1]- Sim [2]- Não\n:")
                if mensagem_emprestimo== "1":
                    saque_emprestimo = float(input("Qual valor deseja sacar?\nR$:"))
                    saque_emprestimo_final = saldo_com_emprestimo - saque_emprestimo
                    print(f"Saque realizado com sucesso! Seu saldo é de: R${saque_emprestimo_final:.2f}! Obrigado por utilizar nossos serviços. Tenha um ótimo dia!")
                else:
                    print(f"Seu saldo atual é de: R${saldo_com_emprestimo:.2f}!\nObrigado por utilizar nossos serviços. Tenha um ótimo dia!")     
            else:
                print("Obrigado por utilizar nossos serviços. Tenha um ótimo dia!")
        else:
            print(f"Saque realizado com sucesso! Seu saldo atual é de:R${saldo_deposito-saque:.2f}! Obrigado por utilizar nossos serviços. Tenha um ótimo dia!")  
    else:
        print(f"Seu saldo atual é de: R${saldo_deposito:.2f}!\nObrigado por utilizar nossos serviços. Tenha um ótimo dia!")
    #saque feito 
elif opcao =="2":
    mensagem_saque2 = float(input("Qual valor deseja sacar?\nR$:"))
    if mensagem_saque2 > saldo_atual:
        print("Valor maior que seu saldo atual! Para prosseguir realize um depósito ou empréstimo.")
    else:
        valor_saque = saldo_atual - mensagem_saque2
        print(f"Saque realizado com sucesso! Seu valor atual é de:R${valor_saque:.2f}!\nObrigado por utilizar nosso serviços. Tenha um ótimo dia!")
 #empréstimo  
else:
    emprestimo_mensagem = input("Deseja prosseguir com o emprestimo?\n[1]- Sim [2]- Não\n:")
    if emprestimo_mensagem =='1':
        emprestimo2 = float(input("Qual o valor do empréstimo?\nR$:"))
        saldo_com_emprestimo = saldo_atual + emprestimo2
        mensagem_emprestimo = input(f"Seu saldo atual é de: R${saldo_com_emprestimo:.2f}!\nDeseja realizar um saque [1]- Sim [2]- Não\n:")
        if mensagem_emprestimo== "1":
                    saque_emprestimo = float(input("Qual valor deseja sacar?\nR$:"))
                    saque_emprestimo_final = saldo_com_emprestimo - saque_emprestimo
                    print(f"Saque realizado com sucesso! Seu saldo é de: R${saque_emprestimo_final:.2f}! Obrigado por utilizar nossos serviços. Tenha um ótimo dia!")
        else:
                    print(f"Seu saldo atual é de: R${saldo_com_emprestimo}!\nObrigado por utilizar nossos serviços. Tenha um ótimo dia!")
    else:
        print(f"Obrigado por utilizar nosso serviços. Seu saldo atual é de: R${saldo_atual:.2f}!\nTenha um ótimo dia!")