# criar um algoritmo da sorte de Fibonacci
# o usuário deve digitar um valor numérico inteiro e o algoritmo deverá verificar se esse valor encontra-se na sequência de Fibonacci
# caso o número esteja na sequência, o algoritmo deve exibir a mensagem "ação bem-sucedida", e caso não estejem deve exibir a mensagem "a ação falhou"
# lembrando que a sequência de Fibonacci inicia em 1 e cada novo elemtno da sequência é a soma dos dois elementos anteriores. Exemplo: 1,1,2,3,5,8,13,21, e assim por diante.

n_usuario = int(input("Por favor, informe um número inteiro: "))

anterior1 = 1
anterior2 = 0

for n_elemento in range(1, n_usuario + 1, 1):
    valor_atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = valor_atual
    if n_usuario == valor_atual:
        print("Ação bem-sucedida")
        break
    elif n_usuario < valor_atual:
        print("Ação falhou")
        break