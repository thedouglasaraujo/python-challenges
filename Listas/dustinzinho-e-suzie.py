tamanho = int(input())
linhas = 0
contador = 0
lista = []
soma = []
linha2 = []
linha3 = []
linha4 = []
senha = []

#Colocar cada linha da matriz como elemento da lista
while (linhas != tamanho):
  linha = input().split(" ")
  lista.append(linha)
  linhas += 1
  
#Soma Linha
for linha in lista:
    while contador < tamanho-1:
      soma = int(linha[contador]) + int(linha[(contador+1)])
      linha2.append(soma) #Adicionando cada soma em uma lista
      contador += 1
    contador = 0
    
maximo = max(linha2) #Verificando a maior soma dentro da lista

for linha in lista:
    while contador < tamanho-1:
      soma = int(linha[contador]) + int(linha[(contador+1)])
      if soma == maximo: #Quando a soma for igual a maior soma da lista, registrar na lista da senha os índices da matriz
        senha.append(linha[contador])
        senha.append(linha[(contador+1)])
      contador += 1
    contador = 0
        
senha = senha[0:2] #Caso o valor da soma apareça mais vezes, salvar na lista da senha apenas os índices da primeira ocorrência

# Soma Coluna
contador2 = 0
contador = 0
while contador2 != tamanho:
  soma = int(lista[contador][contador2]) + int(lista[(contador+1)][contador2])
  linha3.append(soma)
  contador += 1
  if (contador == tamanho-1):
    contador = 0
    contador2 += 1
maximo3 = max(linha3)


contador = 0
contador2 = 0
senha2 = []
while contador2 != tamanho:
  soma = int(lista[contador][contador2]) + int(lista[(contador+1)][contador2])
  if soma == maximo3:
    senha.append(lista[contador][contador2])
    senha.append(lista[(contador+1)][contador2])
  contador += 1
  if (contador == tamanho-1):
    contador = 0
    contador2 += 1
    
senha = senha[0:4]

#Soma Diagonal
contador2 = 1
contador = 0
while contador != tamanho-1:
  soma = int(lista[contador][contador]) + int(lista[contador2][contador2])
  linha4.append(soma)
  contador2 += 1
  contador += 1
    
maximo4 = max(linha4)

contador2 = 1
contador = 0
while contador != tamanho-1:
  soma = int(lista[contador][contador]) + int(lista[contador2][contador2])
  if soma == maximo4:
    senha.append(lista[contador][contador])
    senha.append(lista[contador2][contador2])
  contador2 += 1
  contador += 1

print("Falei que era fácil Dustinzinho...")
print("Pegando todas os números que formam as combinações dos pares de cada sentido temos...")
print("Password: "+senha[0]+senha[1]+senha[2]+senha[3]+senha[4]+senha[5])