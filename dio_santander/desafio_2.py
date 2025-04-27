# 20 - Exercício 2

## Substituindo caractere repetido

#Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências
#de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere

nome = input("coloque seu nome: ")
min = nome[0].lower()
sub = nome.replace(min, "$")
nome_final = min + sub[1:]
print(nome_final)
















