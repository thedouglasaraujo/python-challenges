nomes = input()
lista = nomes.split(",")  # Colocar cada nome como elemento da lista
quantidade = len(lista)
remover = 0

while (quantidade != 1):  # Enquanto não sobrar apenas uma pessoa na lista
    entrada = input()
    if (entrada == "Não encontrei nada no primeiro suspeito"):
        lista.pop(0)
        quantidade -= 1
    elif (entrada == "O último da lista está limpo"):
        lista.pop()
        quantidade -= 1
    elif (entrada == "Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita"):
        if (quantidade % 2) == 0:  # Achar e remover o elemento do meio, caso a quantidade de nomes for par
            remover = (quantidade/2)+1
            lista.pop(int(remover-1))
            quantidade -= 1
        # Achar e remover o elemento do meio, caso a quantidade de nomes for ímpar
        elif (quantidade % 2) != 0:
            remover = ((quantidade-1)/2)+1
            lista.pop(int(remover-1))
            quantidade -= 1
    elif (entrada == "Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:"):
        posicao = int(input())
        lista.pop(posicao)
        quantidade -= 1
    elif (entrada == "Acho que temos mais uma opção a ser analisada…"):
        adicionar = input()
        lista.append(adicionar)
        quantidade += 1
    else:
        print("Isso não estava no combinado, a lista vai permanecer do mesmo jeito")

if (quantidade == 1):  # Quando tiver apenas uma pessoa na lista
    print("Acho que encontramos o suspeito. O seu nome é {}, vamos salvar o Sam!".format(
        lista[0]))
