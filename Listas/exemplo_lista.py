#Utilizar a estrutura de listas quando precisar reunir uma coleção de valores que abordam o mesmo assunto

lista_instrumentos = ["Bateria", "Guitarra", "Violão"]

#tipo da lista
print(type(lista_instrumentos))

print("---------------------")

#todos os itens da lista
print(lista_instrumentos)

print("---------------------")

#escolher o item da lista pelo indice
print(lista_instrumentos[1])

print("---------------------")

#verificar a lista com o loop for
for instrumento in lista_instrumentos:
    print(instrumento)