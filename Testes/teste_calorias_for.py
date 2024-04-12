# elaborar um algoritmo de quantos alimentos o usuário consumiu no dia, o número de calorias de cada um dos alimentos e no final exibir o total de calorias

quantidade_alimentos = int(input("Por favor, informe quantos alimentos você consumiu hoje? "))
total_calorias = 0

for alimento in range(1, quantidade_alimentos + 1, 1):
    caloria = int(input("Informe a quantidade de calorias do {} alimento: ".format(alimento)))
    total_calorias = total_calorias + caloria

print("Foram consumidas {} calorias ao longo do dia.".format(total_calorias))