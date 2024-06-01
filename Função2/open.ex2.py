#o modo "w" indica que é o modo de escrita
#podemos indicar o modo que o arquivo será manipulado
# "r" abrir para letiura(modo padrão)
# "x" abrir para a criação de arquivo, gerando uma falha se existir um arquivo de mesmo nome
# "a" abrindo a escrita, anexando o novo conteúdo ao final do conteúdo já existente no arquivo.
# "b" abrir em modo binário
# "t" abrir em modo texto (modo padrão)
# "+" abrir para atualização (escrita e leitura)

conteudo = "Eu gosto de presentes!"

arquivo = open("c:\\Users\\guilherme.araujo\\Desktop\\Stu\\novo_teste.txt", "w", encoding="UTF-8")

arquivo.write(conteudo)

arquivo.close()