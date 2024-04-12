# É necessário uma senha para logar na maquina
# A senha é composta pela palavra "LIBERDADE" seguida do fatorial dos minutos que a máquina estiver marcando no momento da digitação da senha
# Exemplo: se a máquina marcar 5 minutos, a senha será "LIBERDADE120"
#exemplo de fatorial 5: 5 * 4 * 3 * 2 * 1

minutos = int(input("Informe o número dos minutos do horário atual: "))
fatorial = minutos

for numero in range (1, minutos):
    fatorial = fatorial * numero

print(f"A senha é LIBERDADE{fatorial}")
