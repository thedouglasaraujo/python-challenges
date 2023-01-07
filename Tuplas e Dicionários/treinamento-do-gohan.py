pedras = int(input())
gohan = input().split(" ") #Separando cada número em um elemento
picollo = input().split(" ")
contador = 0 #Para verificar se as duas sequências são iguais 

def transformar_inteiro(lista, lista_nova): #Transformando lista de strings em lista de inteiros
  for i in lista:
    lista_nova.append(int(i))
  
picollo_int = []
gohan_int = []
transformar_inteiro(gohan, gohan_int) #Fazendo a conversão
transformar_inteiro(picollo, picollo_int)

#Criando dicionários
dicionario_gohan = {}
dicionario_picollo = {}

for partida in range(pedras): #Adicionando cada número da sequência em uma chave do dicionário
  dicionario_gohan[partida] = gohan_int[partida]
  dicionario_picollo[partida] = picollo_int[partida]

for item in dicionario_gohan:
  if dicionario_gohan[item] in dicionario_picollo.values(): #Se o número da primeira sequência estiver na segunda sequência
    for i in dicionario_picollo:
      if dicionario_picollo[i] == dicionario_gohan[item]:
        parametro = i
    del dicionario_picollo[parametro] #Removendo o número da segunda sequência para não contabilizar duas vezes em casos de repetição do número
    contador += 1
      
if contador == pedras:
  print("Dale Gohan!")
else:
  print("Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.")