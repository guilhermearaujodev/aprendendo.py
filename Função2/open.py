#função open é nativa do Py, retorna dentro do script um objeto do tipo arquivo
#encoding interpretar a codificação do arquivo
#conseguimos ler arquivos que estao salvos no hd e passar para estrutura de dados para manipular

arquivo = open("c:\\Users\\guilherme.araujo\\Desktop\\Stu\\teste.txt", encoding="UTF-8")

#metodo read le o arquivo de uma vez e retorna uma string
#print(arquivo.read())

#metodo readline para retornar apenas uma linha do arquivo
#print(arquivo.readline())
#print(arquivo.readline())

#metodo readlines para retornar listas, onde cada item da lista é uma linha do arquivo
#print(arquivo.readlines())

for linha in arquivo.readlines():
    print(linha)

#fechar o arquivo
arquivo.close()