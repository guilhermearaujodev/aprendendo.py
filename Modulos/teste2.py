#Se fizermos a importação de cada função, não precisamos escrever o nome do módulo e o sinal de ponto.

#importação de funções específica do módulo calc.py
from calc import somar, subtrair

#solicitando valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")

#armazenando a soma
soma = somar(valor1, valor2)

#armazenando a subtração
subtracao = subtrair(valor1, valor2)

print("A soma é {}".format(soma))
print("A subtração é {}".format(subtracao))