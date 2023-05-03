mochilas = int(input())
nomes = list()
dividido = list()
quantidade = list()
cont_mochilas = 0
cont_x = 3
ind = 0
entrada = "entrada"
nomes.append(input().split(' '))

# Colocando cada nome como uma lista dentro de outra lista
for i in nomes:
    for n in i:
        dividido.append([n])

for k in dividido:
    tamanho = int(input())
    cont_tamanho = 0
    # Adicionando os dois primeiros itens em cada lista
    k.append("Lanterna")
    k.append("Omega 3 da top therm")
    while cont_tamanho != (tamanho - 2):
        k.append("x")
        cont_tamanho += 1

# Laços para verificar o tamanho de cada mochila após adicionar os dois primeiros itens
for k in dividido:
    quantidade.append(len(k))

for k in dividido:
    while (cont_x) != len(k):
        k.remove("x")

itens_adicionados = int(input())
contador_itens = 0
for z in k:
    while contador_itens != itens_adicionados:
        item = input()
        indice = int(input())
        # Adicionar item caso a mochila tenha espaço
        if (len(dividido[indice]) < quantidade[indice]):
            contador_itens += 1
            dividido[indice].append(item)
        else:  # Printar caso a mochila esteja cheia
            print("Mochila cheia. Não vai dar para levar.")
            contador_itens += 1

entrada = input()
while (entrada != "CHEGAMOS NO CIN!"):
    if (entrada == "Tirar da mochila"):
        objeto = input()
        ind = int(input())
        if (objeto) in dividido[ind]:
            dividido[ind].remove(objeto)
            print(f'{objeto} usado com sucesso da mochila {ind}.')
        else:
            print(f'Você não tem {objeto} na mochila {ind}.')
        entrada = input()
    elif (entrada == "Guardar na mochila"):
        objeto = input()
        ind = int(input())
        if (len(dividido[ind]) < quantidade[ind]):
            dividido[ind].append(objeto)
            print(f'{objeto} adicionado na mochila {ind}.')
        else:
            print(f'Mochila {ind} cheia!')
        entrada = input()
    else:
        print("Ação inválida.")
        entrada = input()

# Tirando o nome do dono da mochila em cada lista para poder printar apenas os elementos
for k in dividido:
    k.pop(0)

# Printando cada mochila e seus itens
for name in nomes:
    for a in name:
        print(f"Mochila de {a} chegou assim:")
        posicao = name.index(a)
        for t in dividido[posicao]:
            print(t)
