## Substituindo caractere repetido

#Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois 
# primeiros caracteres de cada string.

#Ex:

#abc xyz → **xyc abz**

nome1 = "abc"
nome2 ="zyx"
novo_nome = nome1 [:2] + nome2 [2:]
novo_nome2 = nome2 [:2] + nome1 [2:]
print(novo_nome, novo_nome2)

"""palavra1 = input("coloque a palavra 1 aqui: ")
palavra2 = input("coloque a palavra 2 aqui: ")
palavra1_min = palavra1[0:2].lower()
palavra1_inicial = palavra1[0:2]
palavra1_substituir = palavra1.replace(palavra1_inicial, "bb")

palavra2_min = palavra2[0:2].lower()
palavra2_inicial = palavra2[0:2]
palavra2_substituir = palavra2.replace(palavra2_inicial, "at")
#print(f"Ops, entendemos: {palavra1_substituir}")
#print(f"Ops, você quis dizer: {palavra2_substituir}")
print(palavra1_substituir.split() + palavra2_substituir.split())"""










