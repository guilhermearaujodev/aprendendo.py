#Para incluir um valor em uma posição específica da lista, vamos utilizar o método insert

#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

#incluindo um valor em uma posição específica da lista
jedi.insert(3, "Luminara")

#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)