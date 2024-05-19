"""A função read() realiza a leitura

de todo conteúdo do arquivo.


Sua sintaxe é:

leitura=open(‘arquivo.txt, ‘r’)

print leitura.read()

leitura.close()"""

#leitura do arquivo texto

leitura = open("arqText.txt", "r")
print(leitura.read())
leitura.close()