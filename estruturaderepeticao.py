#Sintaxe da estrutura For:
#For {referência}
#in {sequência}: {bloco de código}

for n in range(10):
    print(n)

for n in range(5,16):
    print(n)

for n in range(10, 0, -1):
    print(n)

#Sintaxe da estrutura While:
#While condição
#{bloco de código}

x = 1

while x <= 15:
    print(x)
    x = x + 1
    
qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    
    #Entrada de valores
    valor = float(input("Digite um valor: "))

#Caso digite um valor negativo o laço encerra
media = soma / qtd
print("\n Total de Soma: ",soma)
print("\n Quantidade de valores digitados: ",qtd)
print("\n Média dos valores: ", media)