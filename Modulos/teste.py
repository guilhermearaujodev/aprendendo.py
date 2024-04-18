#importação do módulo calc.py
import calc

valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")

#armazenando a soma
soma = calc.somar(valor1, valor2)

#exibir soma
print("A soma é {}".format(soma))