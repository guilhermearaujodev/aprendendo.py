#Módulos são scripts Python que contêm funções e estruturas que podem ser incorporadas em outros scripts

#função de soma
def somar(a, b):
    return float(a) + float(b)

#função de subtração
def subtrair(a, b):
    return float(a) - float(b)

#função de divisão
def dividir(a, b):
    if b==0:
        return 0
    return float(a) / float(b)

#função de multiplicar
def multiplicar(a, b):
          return float(a) * float(b)