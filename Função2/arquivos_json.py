import json

#cria dicionario
contatos = {
    "Clark Kent":
        {"celular":"12345",
        "email":"clark@krypton.com"},
    "Bruce Wayne":
        {"celular":"654321",
        "email":"bat@caverna.com"}
}

#dumps é um método que converte um objeto para o formato json
#indent vamos formatar e indentar
#convertendo o dicionário para uma string o formato json
print(json.dumps(contatos, indent=4))

#criando o arquivo
arquivo = open("c:\\Users\\guilherme.araujo\\Desktop\\Stu\\dicionario.json", "w", encoding="UTF-8")

conteudo = json.dumps(contatos, indent=4)
#escreve o json dentro do arquivo
arquivo.write(conteudo)
arquivo.close()