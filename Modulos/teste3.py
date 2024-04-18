#Para importar todas funções de uma vez, porém esse recurso deixa o programa lento.

#importação de funções específica do módulo calc.py
from calc import *

valor1 = input("Digite um valor: ")
valor2= input("Digite o segundo valor: ")

soma = somar(valor1, valor2)

subtracao = subtrair(valor1, valor2)

divisao = dividir(valor1, valor2)

print("\n A soma é {}, \n A subtração é {}, \n A divisão é {}".format(soma, subtracao, divisao))