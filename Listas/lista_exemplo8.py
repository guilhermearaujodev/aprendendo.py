#count() = retorna a quantidade de vezes que um elemento aparece na lista
#sort() = organiza a lista em ordem crescente/alfabética
#reverse() = inverte a ordem dos elementos de uma lista

#valores fora de ordem
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5]

#exibição da lista
print("A lista foi criada assim: {}".format(valores))

#contagem de elementos
contagem = valores.count(7)
print("Nessa lista o número 7 aparece {} vezes".format(contagem))

#invertendo a lista
valores.reverse()
print("A lista agora está invertida: {}".format(valores))

#ordenando a lista
valores.sort()
print("A lista agora está ordenada: {}".format(valores))