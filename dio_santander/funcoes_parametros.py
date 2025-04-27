"""def somar(a,b):
    return a+b
def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"o resultado da operação é = {resultado}")
    
exibir_resultado(10,15,somar)"""

'''title = "Calculadora"
adorno = "-"
def somar(a,b):
    return a+b
def exibir_resultados (a,b,funcao):
    #o parâmetro função é a func somar e serve para executarmos a conta.
    resultado = funcao(a,b)
    #aqui podemos entender que função na verdade é def somar (a,b) 
    # e está sendo executada.
    print(adorno*20)
    print(title)
    print(adorno*20)
    print(f"O resultado é = {resultado}")
exibir_resultados(10,12,somar)
#aqui a função somar está como variável e foi executada anteriormente em resultado.

op = somar
valor1= int(input("Qual valor: "))
valor2= int(input("Qual valor: "))
resultado = op(valor1, valor2)
print(f"O valor da conta é = {resultado}")'''

title = "Calculadora"
adorno = "-"
def soma(a,b):
    return a + b
def exibir_resultado(a,b,soma):
    resultado = soma(valor1,valor2)
op = soma
print(adorno*20)
print(title)
print(adorno*20)
valor1 = float(input("Qual valor: "))
valor2 = float(input("Qual valor: "))
resultado = op(valor1, valor2)
exibir_resultado(valor1, valor2, soma)
print(f"O valor da soma é = {resultado}")
