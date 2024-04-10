#laço para tem a ideia de determinar um ponto inicial e um ponto final para a repetição, controlando o número de voltas

#contadora = i (i de iperação, ou seja, de uma volta que aconteceu.
i = 1
numero = int(input("Por favor, informe o valor do qual deseja a tabuada: "))

while i <=10:
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")
    i = i + 1