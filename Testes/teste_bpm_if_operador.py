#IDADE BPM
#até 2 anos 120 a 140
#de 8 anos até 17 anos 80 a 100
#Adulto sedentário 70 a 80
#Idosos 50 a 60

print("VERIFICADOR DE FREQUÊNCIAS CARDÍACAS")
bpm = int(input("Por favor, informar o seu BPM: "))
idade = int(input("Por favor, informar a sua idade: "))

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Batimentos normais para a idade fornecida")
    else:
        print("Frequência cardiaca inadequada")
elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Batimentos normais para a idade fornecida")
    else:
        print("Frequência cardiaca inadequada")
elif idade >= 18 and idade < 60:
    if bpm >= 70 and bpm <= 80:
        print("Batimentos normais para a idade fornecida")
    else:
        print("Frequência cardiaca inadequada")
elif idade >= 60:
    if bpm >= 50 and bpm <= 60:
        print("Batimentos normais para a idade fornecida")
    else:
        print("Frequência cardiaca inadequada")
else:
    print("Não existe dados para a idade indicada")