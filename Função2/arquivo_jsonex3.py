#para ler um arquivo e fechar sem o close
with open("c:\\Users\\guilherme.araujo\\Desktop\\Stu\\teste.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())