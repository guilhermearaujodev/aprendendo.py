#Desvio Simples
#Só é realizado quando o resultado for verdadeiro

nome = input("Informe o nome do funcionário: ")
salario = float(input("Informe o salário do funcionário: "))

if salario < 0:
    #salario = salario * -1
    #abs e uma funcao no python que transforma um valor negativo em positivo
    salario = abs(salario)
    print("Atenção! Foi informado um salário negativo.")

print(f"O funcionário {nome} tem um salário de R${salario}")