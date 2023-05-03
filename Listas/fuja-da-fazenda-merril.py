personagem = input()
mapa = []
linha = []

# Verificadores para não deixar o "p" ou "d" fazer um movimento contrário
direitad = baixod = cimad = esquerdad = False
direitap = baixop = cimap = esquerdap = False

pegos = False
passou = False
passoud = False
parar = False

for cont in range(0, 8):  # Transformar cada linha do labirinto em elemento da lista e cada caractere da linha em elemento de outra lista (matriz)
    parte_mapa = input()
    for digito in range(len(parte_mapa)):
        linha.append(parte_mapa[digito])
    mapa.append(linha[:])
    linha.clear()

# Encontrando a posição do "p"
posp1 = 0
posp2 = 0
for i in mapa:
    if "p" in i:
        posp2 = i.index("p")
        posp1 = mapa.index(i)

# Encontrando a posição do "d"
posd1 = 0
posd2 = 0
for i in mapa:
    if "d" in i:
        posd2 = i.index("d")
        posd1 = mapa.index(i)

while parar == False:
    if parar == False:
        # Movendo "p"
        if mapa[posp1][posp2+1] == "o":
            mapa[posp1][posp2] = "p"
            passou = True
            parar = True
            break
        elif mapa[posp1+1][posp2] == "o":
            mapa[posp1][posp2] = "p"
            passou = True
            parar = True
            break
        elif mapa[posp1-1][posp2] == "o":
            mapa[posp1][posp2] = "p"
            passou = True
            parar = True
            break
        elif mapa[posp1][posp2-1] == "o":
            mapa[posp1][posp2] = "p"
            passou = True
            parar = True
            break
        elif mapa[posp1][posp2+1] == "." and esquerdap == False:
            mapa[posp1][posp2] = "."
            mapa[posp1][posp2+1] = "p"
            posp2 += 1
            direitap = True
            baixop = cimap = esquerdap = False
        elif mapa[posp1+1][posp2] == "." and cimap == False:
            mapa[posp1][posp2] = "."
            mapa[posp1+1][posp2] = "p"
            posp1 += 1
            baixop = True
            direitap = cimap = esquerdap = False
        elif mapa[posp1-1][posp2] == "." and baixop == False:
            mapa[posp1][posp2] = "."
            mapa[posp1-1][posp2] = "p"
            posp1 -= 1
            cimap = True
            direitap = baixop = esquerdap = False
        elif mapa[posp1][posp2-1] == "." and direitap == False:
            mapa[posp1][posp2] = "."
            mapa[posp1][posp2-1] = "p"
            posp2 -= 1
            esquerdap = True
            direitap = baixop = cimap = False
        elif mapa[posp1][posp2+1] != "." and mapa[posp1+1][posp2] != "." and mapa[posp1-1][posp2] != "." and mapa[posp1][posp2-1] != ".":
            parar = True
        elif mapa[posp1][posp2+1] != "o" and mapa[posp1+1][posp2] != "o" and mapa[posp1-1][posp2] != "o" and mapa[posp1][posp2-1] != "o":
            parar = True
        # Movendo "d"
        if mapa[posd1][posd2+1] == "o":
            mapa[posd1][posd2] = "."
            passoud = True
            parar = True
            break
        elif mapa[posd1+1][posd2] == "o":
            mapa[posd1][posd2] = "."
            passoud = True
            parar = True
            break
        elif mapa[posd1-1][posd2] == "o":
            mapa[posd1][posd2] = "."
            passoud = True
            parar = True
            break
        elif mapa[posd1][posd2-1] == "o":
            mapa[posd1][posd2] = "."
            passoud = True
            parar = True
            break
        elif mapa[posd1][posd2+1] == "p":
            mapa[posd1][posd2+1] = "d"
            mapa[posd1][posd2] = "."
            pegos = True
            parar = True
            break
        elif mapa[posd1+1][posd2] == "p":
            mapa[posd1][posd2+1] = "d"
            mapa[posd1][posd2] = "."
            pegos = True
            parar = True
            break
        elif mapa[posd1-1][posd2] == "p":
            mapa[posd1][posd2+1] = "d"
            mapa[posd1][posd2] = "."
            pegos = True
            parar = True
            break
        elif mapa[posd1][posd2-1] == "p":
            mapa[posd1][posd2+1] = "d"
            mapa[posd1][posd2] = "."
            pegos = True
            parar = True
            break
        elif mapa[posd1][posd2+1] == "." and esquerdad == False:
            mapa[posd1][posd2] = "."
            mapa[posd1][posd2+1] = "d"
            posd2 += 1
            direitad = True
            baixod = cimad = esquerdad = False
        elif mapa[posd1+1][posd2] == "." and cimad == False:
            mapa[posd1][posd2] = "."
            mapa[posd1+1][posd2] = "d"
            posd1 += 1
            baixod = True
            direitad = cimad = esquerdad = False
        elif mapa[posd1-1][posd2] == "." and baixod == False:
            mapa[posd1][posd2] = "."
            mapa[posd1-1][posd2] = "d"
            posd1 -= 1
            cimad = True
            direitad = baixod = esquerdad = False
        elif mapa[posd1][posd2-1] == "." and direitad == False:
            mapa[posd1][posd2] = "."
            mapa[posd1][posd2-1] = "d"
            posd2 -= 1
            esquerdad = True
            direitad = baixod = cimad = False
        elif mapa[posd1][posd2+1] != "." and mapa[posd1+1][posd2] != "." and mapa[posd1-1][posd2] != "." and mapa[posd1][posd2-1] != ".":
            parar = True
        else:
            parar = True
    for linha in mapa:
        print(*linha)

# Condições para printar
if pegos == True:
    for linha in mapa:
        print(*linha)
    print(
        f"Ah não, você e {personagem} foram pegos pelo demodog e agora ele vai atravessar o portal e talvez a eleven não consiga salvar todos.")

if passou == True:
    mapa[posp1][posp2] = "."
    for linha in mapa:
        print(*linha)
    print(
        f"UFA!!! Você e {personagem} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.")

if passoud == True:
    for linha in mapa:
        print(*linha)
    print(
        f"Ah não, você e {personagem} não foram rápidos o bastante e o demodog passou pelo portal.")
