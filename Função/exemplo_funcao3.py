#O comando return faz com que uma função seja encerrada e um determinado valor seja devolvido para o local onde ocorreu a chamada da função


def calcularVelocidadeMedia(distancia, tempo):
    velocidade_media = distancia/tempo
    return velocidade_media

dist = float(input("Informe a distância"))
temp = float(input("Informe o tempo"))

#chamando a função com valores definidos pelo usuário
print("A velocidade média é {}".format(calcularVelocidadeMedia(dist, temp)))