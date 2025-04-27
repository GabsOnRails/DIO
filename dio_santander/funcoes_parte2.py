#parâmetros especiais

def criar_carro(modelo, ano, placa, /, marca, motor):
    #tudo que está antes do / significa que é por posição
    # o que está depois é por chave ou posição
    #hibrído sem definir o que é por chave
    print(modelo, ano,placa, marca, motor)
criar_carro("Palio", 1999, "ABZ-2345","Fiat",
            motor="1.0")

def criar_carro2 (*,modelo, ano, placa, marca, motor):
    print(modelo, ano, placa, marca,motor)
    #tudo que está depois da "*" significa que será passado
    #por chaves
criar_carro2(modelo="Palio", ano=1999, placa="ABC-1234", 
marca="Fiat", motor="1.0")

def criar_carro3 (modelo,ano,placa, /, * , marca, motor, combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)
criar_carro3 ("Palio", 1999, "ABC_1234",marca="Fiat",
              motor ="1.0", combustivel="Gasolina")
#modelo híbrido definindo o que é por chave