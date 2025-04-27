texto =input("informe seu texto: ")
vogais ="AEIOU"
for letra in texto:
    if letra.upper()in vogais:
        print(letra, end = " ")
else:
    print() 



