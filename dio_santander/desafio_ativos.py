ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)
    ativos.sort()
# TODO: Ordenar os ativos em ordem alfabética.
for ativos in ativos:
    print(ativos)

# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.