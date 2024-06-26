#Usando o módulo sys do python, poderemos verificar o tamanho de qualquer objeto por meio do método getsizeof().

#primeiro importamos o módulo sys
import sys

#depois criamos algumas variáveis de exemplo
nome = "Bruce Wayne"
idade = 30
peso = 92.3
lista = []

#Vamos exibir em uma mensagem o nome da variável, o tipo (type) e o tamanho (getsizeof)
print("A variável nome é do tipo {} e tem {} bytes".format(type(nome), sys.getsizeof(nome)))
print("A variável idade é do tipo {} e tem {} bytes".format(type(idade), sys.getsizeof(idade)))
print("A variável peso é do tipo {} e tem {} bytes".format(type(peso), sys.getsizeof(peso)))
print("O objeto lista é do tipo {} e tem {} bytes".format(type(lista), sys.getsizeof(lista)))