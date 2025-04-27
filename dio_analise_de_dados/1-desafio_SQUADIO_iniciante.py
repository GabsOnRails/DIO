# Realizando o primeiro desafio do SQUADIO
# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input(""))

if quantidade_passos > 0:
    for x in range(quantidade_passos):
        x+=1
        if x ==1:
          palavra = "passo"
        else:
          palavra = "passos"
        print(f"Explorador: {x} {palavra}")
else:
    print("Nenhum passo dado na floresta.")