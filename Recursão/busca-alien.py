numeros_das_salas = input().split(' ')
salas = []
direcoes = []
bin = []


def busca_binaria(lista):
    if len(lista) % 2 == 0:
        meio = int((len(lista)/2) + 1)  # Meio caso o número seja par
        # Diminuindo 1 para igualar ao índice (Se o meio é o 6º elemento, seu índice é 5)
        meio -= 1
    else:
        meio = int(((len(lista)-1)/2)+1)  # Meio caso o número seja ímpar
        meio -= 1
    if len(lista) > meio and len(lista) >= 1:
        if lista[meio] < numero_escolhido and len(lista) != 1:
            lista = lista[meio+1:]  # Corta os números da Esquerda
            direcoes.append("Direita ->")
        elif lista[meio] > numero_escolhido and len(lista) != 1:
            lista = lista[:meio]  # Corta os números da Direita
            direcoes.append("Esquerda ->")
        elif lista[meio] == numero_escolhido or lista[meio] < numero_escolhido or lista[meio] > numero_escolhido:
            direcoes.append("Meio")
        if "Meio" not in direcoes and len(lista) >= 1:
            busca_binaria(lista)  # Recursão para continuar procurando o item


def binario(num):
    divisao = int(num/2)
    if divisao < 1:
        bin.append(num % 2)
    if divisao >= 1:
        bin.append(num % 2)
        binario(divisao)  # Recursão para calcular o Binário


def formatar_binario(lista):
    if len(lista) < qnt_bits:
        lista.insert(0, 0)  # Formata o binário para a quantidade de bits
        formatar_binario(lista)  # Recursão para adicionar 0 no número binário


for i in numeros_das_salas:
    salas.append(int(i))
numero_escolhido = int(input())
qnt_bits = int(input())

binario(numero_escolhido)
bin = bin[::-1]  # Inverte os restos das divisões
formatar_binario(bin)
str_list = [str(i) for i in bin]
num_bin = ''.join(str_list)  # Formatação para o print

# Condições para printar
if numero_escolhido < int(numeros_das_salas[0]) or numero_escolhido > int(numeros_das_salas[(len(salas))-1]):
    print("Acho que a Doutora se confundiu, pois é impossível chegar nesse número pois ele é menor que a menor sala ou maior que o maior da sala.")
else:
    busca_binaria(salas)
if len(num_bin) > qnt_bits and "Meio" in direcoes and numero_escolhido in salas:
    print("Consegui encontar a saída, mas não consigo falar pois o número é muito grande para essa quantidade de bits.")
elif numero_escolhido in salas:
    print(*direcoes, end=(", seguindo por essas coordenadas você vai chegar no número {}.".format(num_bin)))
elif numero_escolhido not in salas and len(direcoes) > 0 and len(num_bin) <= qnt_bits:
    print(*direcoes, end=(", mas não consegui achar."))
elif len(direcoes) > 0 and len(num_bin) > qnt_bits and numero_escolhido not in salas:
    print("Busquei muito, mas não achei a sala, que nem posso dizer, já que tenho poucos bits.")
