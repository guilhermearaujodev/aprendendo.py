#O loop for será usado para repetir algo em um intervalo
#inserir um terceiro valor de incremento, de vez contar de 1 em 1 podemos contar da maneira que preferir.
#range (inicio, final, incremento)

#exibir todos os números impares de 1 à 1000
for contadora in range(1, 1001, 2):
    print(contadora)

#tabuada
n = int(input("Informe o valor do qual deseja obter a tabuada: "))
for contadora in range(1, 11, 1):
    contadora = contadora * n
    print(contadora)


#outro exemplo de tabuada
n = int(input("Informe o valor do qual deseja obter a tabuada: "))
for contadora in range(n, n * 10 + 1, n):
    print(contadora)