# if <condição>:
#     <ação a ser realizada se a condição for verdadeira>
# else:
#     <ação a ser realizada se a condição for falsa>
# o if composto é utilizado quando queremos fazer algo quando o teste der verdadeiro e algo quando o teste der falso
rm = input("Insira seu RM")
idade = input("Insira sua idade")

if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno de RM{}!".format(rm))
    print("Mais informações serão enviadas para seu e-mail cadastrado!")
else:
    print("Sua participação não foi autorizada por causa da sua idade")

