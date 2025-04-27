## Média de 4 notas

"""Escreva um programa em Python que leia quatro números
e calcule a média entre esses números"""
linha = "="
nota_1 = float(input("Nota 1: ")) 
nota_2 = float(input("Nota 2: ")) 
nota_3 = float(input("Nota 3: ")) 
nota_4 = float(input("Nota 4: ")) 
#sistema FMU N1#
média = ((nota_1 + nota_2 + nota_3 + nota_4) /4) * 0.4
print(linha*25)
print(f"Média das notas: {média}")
print(linha*25)