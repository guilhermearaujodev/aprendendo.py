#IDADE BPM
#até 2 anos 120 a 140
#de 8 anos até 17 anos 80 a 100
#Adulto sedentário 70 a 80
#Idosos 50 a 60

print("VERIFICADOR DE FREQUÊNCIAS CARDÍACAS")
bpm = int(input("Por favor, informar o seu BPM: "))
idade = int(input("Por favor, informar a sua idade: "))

if idade <= 2:
    if bpm >= 120:
        if bpm <= 140:
            print("Batimentos normais para a idade fornecida")
        else:
            print("Batimentos acima do indicado para a idade")
    else:
        print("Batimentos abaixo dos indicado para a idade")
elif idade >= 8:
    if idade <= 17:
        if bpm >= 80:
            if bpm <= 100:
                print("Batimentos normais para a idade fornecida")
            else:
                print("Batimentos acima para a idade fornecida")
        else:
            print("Batimentos abaixo para a idade fornecida")
    if idade >= 18:
        if idade <= 60:
            if bpm >= 70:
                if bpm <= 80:
                    print("Batimentos normais para a idade fornecida")
                else:
                    print("Batimentos acima para a idade fornecida")
            else:
                print("Batimentos abaixo para a idade fornecida")
        else:
            if bpm >= 50:
                if bpm <= 60:
                    print("Batimentos normais para a idade fornecida")
                else:
                    print("Batimentos acima para a idade fornecida")
            else:
                print("Batimentos abaixo para a idade fornecida")
else:
    print("Não foi possível verificar os batimentos para essa idade")