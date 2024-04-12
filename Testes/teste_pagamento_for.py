# criar um script simples para ajudar crianças a controlar seus gastos
# deve informar quantos pagamentos foram feitas ao longo de um dia
# na sequência, informar o valor de cada uma
# no final exibir o valor total gasto e uma média do valor de cada transação

quantidade_pagamento = int(input("Por favor, informar quantos pagamentos foram realizados: "))
valor_total = 0

for n_pagamento in range (1, quantidade_pagamento + 1, 1):
    pagamento = float(input("Por favor, informar o valor gasto do {} pagamento ".format(n_pagamento)))
    valor_total = valor_total + pagamento

media = valor_total / quantidade_pagamento
print("Neste dia, foi gasto um total de R${}, com uma média de R${} por pagamento".format(valor_total, media))