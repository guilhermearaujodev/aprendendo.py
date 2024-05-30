#Os dicionarios de dados são estruturas em py que funcionam seguindo a logica de chave e valor, poderemos associar dois dados, fazendo com que um desses dados seja uma chave unica que identificara um valor

dicionario = {
    "Yoda":"Mestre Jedi",
    "Mace Windu":"Mestre Jedi",
    "Anakin Skywalker":"Cavaleiro Jedi",
    "R2-D2":"Droide",
    "Dex":"Balconista"
}

#mostrar os valores
#for valor in dicionario.values():
#    print(valor)

#mostrar as chaves
#print(dicionario.keys())
#for chave in dicionario.keys():
#    print(chave)

#mostrar o valor =
#print(dicionario["R2-D2"])

#mostrar chave e valor = items
#print(dicionario.items())

for chave, valor in dicionario.items():
    print("{} -- {}".format(chave, valor))