nome = input()
quantidade = int(input())
contador = 0
lista = []

while (contador != quantidade):
    filmes = input()
    lista.append(filmes.split(" - ")) #Separar cada filme e sua nota em lista
    contador += 1
    
#Bubble-sort para ordenar as notas dos filmes
for notas in range(len(lista)-1,0,-1):
  for i in range(notas):
    if (lista[i][1])<lista[i+1][1]:
      trocar = lista[i]
      lista[i] = lista[i+1]
      lista[i+1] = trocar

#Condições para printar
if(nome == "Bonna"):
  print("Os filmes sugeridos por Bonna são:")
  for i in lista:
    print(i[0] + " - " + i[1])
elif(nome == "João"):
  print("Os filmes sugeridos por João são:")
  for i in lista:
    print(i[0] + " - " + i[1])