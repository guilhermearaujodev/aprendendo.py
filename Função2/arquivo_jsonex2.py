#convertendo um arquivo json em dicionario

import json

#usando a função open para criar um objeto do tipo arquivo
arquivo = open("c:\\Users\\guilherme.araujo\\Desktop\\Stu\\dicionario.json", "r", encoding="utf-8")

#colocando o conteudo do arquivo em uma variável do tipo string
conteudo = arquivo.read()
arquivo.close()

#usando o método loads para converter uma string no formato json em um dicionário
agenda = json.loads(conteudo)

print(agenda)